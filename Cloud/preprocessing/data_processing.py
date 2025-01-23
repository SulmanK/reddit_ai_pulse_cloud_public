"""
Data Processing Module for Cloud Environment

This module handles the preprocessing of raw Reddit data using PySpark.
It includes functions for cleaning and transforming posts and comments data,
adapted for cloud environment using BigQuery and Cloud Storage.

Owner: Sulman Khan
"""

import os
import sys

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, LongType, ArrayType, DoubleType, TimestampType
from better_profanity import Profanity
import re
from utils.custom_logging import get_logger
from google.cloud import bigquery
from google.cloud import storage
from datetime import datetime

# Configure logging
logger = get_logger(__name__)

def get_profanity_pattern():
    """Get the profanity pattern using better-profanity's word list and additional patterns."""
    profanity = Profanity()
    profanity.load_censor_words()
    
    # Add some additional phrases that might not be in the default list
    additional_phrases = {
        'wtf', 'stfu', 'bullcrap', 'dhead', 'douche'
    }
    profanity.add_censor_words(additional_phrases)
    
    # Common false positives to exclude
    false_positives = {
        'frank', 'floor', 'fridge', 'future', 'first', 'flip', 'fact', 'from', 'for',
        'food', 'free', 'front', 'frame', 'fresh', 'friday', 'friend'
    }
    
    # Get all words and escape special regex characters, excluding false positives
    all_words = [re.escape(str(word)) for word in profanity.CENSOR_WORDSET 
                 if str(word).lower() not in false_positives]
    
    # Create base pattern from words with strict word boundaries
    word_pattern = r'\b(' + '|'.join(all_words) + r')\b'
    
    # More precise patterns for common obfuscation techniques
    edge_cases = [
        r'\b[f]+[\W_]*[u]+[\W_]*[c]+[\W_]*[k]+(?:ing|er|ed)?\b',
        r'what\s+the\s+[f]+[\W_]*(?:[u]+[\W_]*)?[c]+[\W_]*[k]+\b',
        r'\bthe\s+[f]+[\W_]*(?:[u]+[\W_]*)?[c]+[\W_]*[k]+\b',
        r'\bbull\s*cr[a@4]p\b'
    ]
    
    # Combine patterns with case insensitivity
    full_pattern = f"(?i)(?:{word_pattern}|{'|'.join(edge_cases)})"
    
    logger.info(f"Loaded {len(all_words)} profanity words and phrases")
    return full_pattern

def get_last_processed_batch(client: bigquery.Client, dataset_id: str, subreddit: str) -> float:
    """Gets the last processed timestamp for processed data in BigQuery."""
    try:
        query = f"""
        SELECT MAX(UNIX_SECONDS(created_utc)) as max_epoch 
        FROM `{dataset_id}.posts_{subreddit.lower()}`
        """
        query_job = client.query(query)
        result = next(query_job.result())
        return float(result.max_epoch) if result.max_epoch else 0
    except Exception as e:
        logger.warning(f"No existing processed data found for {subreddit}: {e}")
        return 0

def preprocess_data(spark: SparkSession, bq_client: bigquery.Client, project_id: str, dataset_id: str, subreddits: list, bucket_name: str):
    """
    Processes Reddit data from GCS and writes to both raw and processed BigQuery tables.
    Data flow: GCS -> Spark -> BigQuery (raw and processed tables)
    Only processes new data since the last processed timestamp.
    """
    # Initialize profanity filtering
    profanity_pattern = get_profanity_pattern()
    logger.info("Initialized profanity filter pattern")
    
    for subreddit in subreddits:
        logger.info(f"Processing data for subreddit: {subreddit}")

        # Get last processed timestamp
        last_processed = get_last_processed_batch(bq_client, dataset_id, subreddit)
        
        # Get today's date for loading
        today = datetime.utcnow().strftime("%Y/%m/%d")
        gcs_path = f"gs://{bucket_name}/raw/reddit_data/{today}/{subreddit}/*.json"
        
        # Read raw data from GCS
        df = spark.read.json(gcs_path)

        if df.count() == 0:
            logger.info(f"No new data to process for {subreddit}")
            continue

        # Filter based on timestamp - created_utc is already a float
        df = df.filter(F.col("created_utc") > last_processed)

        # Write raw data to BigQuery - keep data types as is
        raw_df = df.select(
            F.col("post_id").cast("string").alias("post_id"),
            F.col("subreddit").cast("string").alias("subreddit"),
            F.col("title").cast("string").alias("title"),
            F.col("author").cast("string").alias("author"),
            F.col("url").cast("string").alias("url"),
            F.col("score").cast("integer").alias("score"),
            F.col("created_utc").cast("float").alias("created_utc"),
            F.to_json(F.col("comments")).alias("comments"),  # Convert comments array to JSON string
            F.col("ingestion_timestamp").cast("float").alias("ingestion_timestamp")
        ).filter(  # Ensure REQUIRED fields are not null
            (F.col("post_id").isNotNull()) &
            (F.col("subreddit").isNotNull())
        )
        
        # Write raw data to BigQuery
        raw_table = f"{project_id}.raw_data.raw_{subreddit.lower()}"
        raw_df.write \
            .format("bigquery") \
            .option("table", raw_table) \
            .option("temporaryGcsBucket", bucket_name) \
            .mode("append") \
            .save()
        
        logger.info(f"Wrote raw data to BigQuery for {subreddit}")

        # Process posts for processed table
        df_posts_filtered = df.filter(
            (F.col("title").isNotNull()) & 
            (F.col("title") != "") & 
            (F.col("title") != "[deleted]") &
            (F.col("author").isNotNull()) & 
            (F.col("author") != "") & 
            (F.col("author") != "[deleted]") &
            (F.col("subreddit").isNotNull()) &
            (F.col("url").isNotNull()) &
            (F.col("score").isNotNull()) &
            (F.col("created_utc").isNotNull())
        ).dropDuplicates(["post_id"])

        # Censor profanity in posts
        df_posts_filtered = df_posts_filtered.withColumn(
            "title",
            F.regexp_replace(F.col("title"), profanity_pattern, "***")
        )
        
        # Select and cast columns for posts - convert timestamps to TIMESTAMP type for processed tables
        df_posts_filtered = df_posts_filtered.select(
            F.col("post_id").cast("string").alias("post_id"),
            F.col("subreddit").cast("string").alias("subreddit"),
            F.col("title").cast("string").alias("title"),
            F.col("author").cast("string").alias("author"),
            F.col("url").cast("string").alias("url"),
            F.col("score").cast("integer").alias("score"),
            F.from_unixtime(F.col("created_utc")).cast("timestamp").alias("created_utc"),
            F.current_timestamp().alias("ingestion_timestamp")
        ).filter(  # Final validation
            (F.col("post_id").isNotNull()) &
            (F.col("subreddit").isNotNull()) &
            (F.col("title").isNotNull()) &
            (F.col("author").isNotNull()) &
            (F.col("url").isNotNull()) &
            (F.col("score").isNotNull()) &
            (F.col("created_utc").isNotNull()) &
            (F.col("ingestion_timestamp").isNotNull())
        )

        # Write processed posts to BigQuery
        posts_table = f"{project_id}.{dataset_id}.posts_{subreddit.lower()}"
        df_posts_filtered.write \
            .format("bigquery") \
            .option("table", posts_table) \
            .option("temporaryGcsBucket", bucket_name) \
            .mode("append") \
            .save()

        # Process comments - extract from the comments array
        comments_df = df.select(
            F.col("post_id"),
            F.explode_outer(F.col("comments")).alias("comment")
        ).select(
            F.col("post_id"),
            F.col("comment.body").alias("body"),
            F.col("comment.author").alias("author"),
            F.col("comment.comment_id").alias("comment_id"),
            F.from_unixtime(F.col("comment.created_utc")).cast("timestamp").alias("created_utc")
        )

        # Filter and clean comments
        comments_df = comments_df.filter(
            (F.col("body").isNotNull()) & 
            (F.col("body") != "") & 
            (F.col("body") != "[deleted]") &
            (F.col("author").isNotNull()) & 
            (F.col("author") != "") & 
            (F.col("author") != "[deleted]")
        ).dropDuplicates(["comment_id"])

        # Censor profanity in comments
        comments_df = comments_df.withColumn(
            "body",
            F.regexp_replace(F.col("body"), profanity_pattern, "***")
        )

        # Write processed comments to BigQuery
        comments_table = f"{project_id}.{dataset_id}.comments_{subreddit.lower()}"
        comments_df.write \
            .format("bigquery") \
            .option("table", comments_table) \
            .option("temporaryGcsBucket", bucket_name) \
            .mode("append") \
            .save()

        logger.info(f"Completed processing data for {subreddit}") 