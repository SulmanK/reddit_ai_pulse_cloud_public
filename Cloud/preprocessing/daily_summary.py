"""
Daily Summary Generation Module for Cloud Environment

This module handles the generation of daily summaries from processed Reddit data using PySpark.
It aggregates posts and comments data for each subreddit on a daily basis, storing results in BigQuery.

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
from datetime import datetime
from utils.custom_logging import get_logger
from google.cloud import bigquery

# Configure logging
logger = get_logger(__name__)

def get_last_processed_timestamp(spark: SparkSession, project_id: str, dataset_id: str) -> datetime:
    """Gets the last processed timestamp from the daily_summary table."""
    try:
        summary_df = spark.read.format('bigquery') \
            .option('table', f"{project_id}.{dataset_id}.daily_summary_data") \
            .load()
        
        last_processed = summary_df.agg(F.max("processed_date")).collect()[0][0]
        return last_processed if last_processed else None
    except Exception as e:
        logger.warning(f"No existing summary data found: {e}")
        return None

def generate_daily_summaries(spark: SparkSession, project_id: str, dataset_id: str, subreddits: list, bucket_name: str):
    """
    Generates daily summaries of the processed data using PySpark.
    Implements incremental loading by only processing data since the last processed timestamp.
    """
    current_timestamp = datetime.now()
    last_processed = get_last_processed_timestamp(spark, project_id, dataset_id)
    total_summaries_added = 0
    
    if last_processed:
        logger.info(f"Processing summaries from {last_processed} to {current_timestamp}")
    else:
        logger.info("No previous summaries found. Processing all available data.")

    for subreddit in subreddits:
        logger.info(f"Processing daily summary for subreddit: {subreddit}")

        # Load posts and comments tables from BigQuery
        posts_df = spark.read.format('bigquery') \
            .option('table', f"{project_id}.{dataset_id}.posts_{subreddit.lower()}") \
            .load()

        posts_count = posts_df.count()
        logger.info(f"Found {posts_count} posts for {subreddit}")

        comments_df = spark.read.format('bigquery') \
            .option('table', f"{project_id}.{dataset_id}.comments_{subreddit.lower()}") \
            .load()

        comments_count = comments_df.count()
        logger.info(f"Found {comments_count} comments for {subreddit}")

        # Filter posts and comments based on created_utc timestamp
        if last_processed:
            daily_posts_df = posts_df.filter(
                (F.col("created_utc") > last_processed) &
                (F.col("created_utc") <= current_timestamp)
            )

            daily_comments_df = comments_df.filter(
                (F.col("created_utc") > last_processed) &
                (F.col("created_utc") <= current_timestamp)
            )
        else:
            daily_posts_df = posts_df.filter(F.col("created_utc") <= current_timestamp)
            daily_comments_df = comments_df.filter(F.col("created_utc") <= current_timestamp)

        filtered_posts_count = daily_posts_df.count()
        logger.info(f"Filtered to {filtered_posts_count} posts for processing")

        if filtered_posts_count == 0:
            logger.info(f"No new posts to summarize for {subreddit}")
            continue

        # Join posts and comments on post_id
        joined_df = daily_posts_df.alias("posts").join(
            daily_comments_df.alias("comments"), 
            "post_id", 
            "right"
        )
        
        # Prepare the daily summary
        daily_summary_df = joined_df.select(
            F.monotonically_increasing_id().alias("id"),
            F.col("subreddit"),
            F.col("posts.post_id").alias("post_id"),
            F.col("posts.score").alias("post_score"),
            F.col("posts.url").alias("post_url"),
            F.col("comments.comment_id").alias("comment_id"),
            F.to_date(F.col("comments.created_utc")).alias("summary_date"),
            F.current_timestamp().alias("processed_date"),
            F.lit(True).alias("needs_processing"),
            F.col("posts.title").alias("post_content"),
            F.col("comments.body").alias("comment_body")
        )

        # Filter out rows where required fields are null
        daily_summary_df = daily_summary_df.filter(
            (F.col("comment_body").isNotNull()) & 
            (F.col("comment_id").isNotNull()) &
            (F.col("post_id").isNotNull())
        )

        filtered_summaries_count = daily_summary_df.count()
        logger.info(f"Generated {filtered_summaries_count} summaries before deduplication")

        # Deduplication Logic
        existing_summary_df = spark.read.format('bigquery') \
            .option('table', f"{project_id}.{dataset_id}.daily_summary_data") \
            .load()

        # Perform a left anti-join to get only new records
        new_daily_summary_df = daily_summary_df.join(
            existing_summary_df,
            ["post_id", "comment_id"],  # Using composite key for deduplication
            "left_anti"
        )

        new_summaries_count = new_daily_summary_df.count()
        
        if new_summaries_count > 0:
            # Write the new daily summaries to BigQuery
            new_daily_summary_df.write.format('bigquery') \
                .option('table', f"{project_id}.{dataset_id}.daily_summary_data") \
                .option('temporaryGcsBucket', bucket_name) \
                .mode('append') \
                .save()
            
            total_summaries_added += new_summaries_count
            logger.info(f"Successfully added {new_summaries_count} new summaries for {subreddit}")
        else:
            logger.info(f"No new unique summaries to add for {subreddit}")

    logger.info(f"Processing complete. Total new summaries added: {total_summaries_added}") 