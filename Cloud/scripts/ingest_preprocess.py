"""
Data Ingestion and Preprocessing Module for Cloud Environment

This module orchestrates the complete data pipeline for Reddit data collection,
from ingestion through preprocessing, using Google Cloud services.

Owner: Sulman Khan
"""

import os
import sys

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from dotenv import load_dotenv
from datetime import datetime
from utils.custom_logging import setup_logging


# Load environment variables
load_dotenv(os.path.join(CLOUD_DIR, '.env'))

# Set up credentials path based on environment

from pyspark.sql import SparkSession
from google.cloud import bigquery
from google.cloud import storage
from typing import List, Optional

# Import local modules
from preprocessing import data_processing, daily_summary
from reddit import reddit_client
from config.config import SUBREDDITS

# Configure logging with absolute path
LOGS_DIR = os.path.join(CLOUD_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
logger = setup_logging(script_name='ingest_preprocess', log_dir=LOGS_DIR)

def create_spark_session(project_id: str) -> SparkSession:
    """Creates a Spark session configured for BigQuery."""
    spark = (SparkSession.builder
             .appName("RedditDataPipeline")
             .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.27.1")
             .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
             .config("spark.hadoop.google.cloud.auth.service.account.enable", "true")
             .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
             .getOrCreate())
    
    # Set project ID for BigQuery
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    spark.conf.set("viewsEnabled", "true")
    spark.conf.set("materializationDataset", f"{project_id}.temp")
    
    return spark

def setup_bigquery_environment(client: bigquery.Client, project_id: str, subreddits: List[str]) -> None:
    """Verifies the BigQuery environment exists."""
    try:
        # Verify datasets exist
        for dataset_id in ["raw_data", "processed_data"]:
            try:
                client.get_dataset(f"{project_id}.{dataset_id}")
                logger.info(f"Verified dataset {dataset_id} exists")
            except Exception as e:
                logger.error(f"Dataset {dataset_id} not found: {e}")
                raise
                
        logger.info("BigQuery environment verification completed successfully")
    except Exception as e:
        logger.error(f"Failed to verify BigQuery environment: {e}")
        raise

def verify_table_exists(client: bigquery.Client, project_id: str, dataset_id: str, table_id: str) -> None:
    """Verifies that a table exists in BigQuery."""
    try:
        # Get the numeric project ID
        project = client.project
        full_table_id = f"{project}.{dataset_id}.{table_id}"
        client.get_table(full_table_id)
        logger.info(f"Verified table {full_table_id} exists")
    except Exception as e:
        logger.error(f"Table {full_table_id} not found: {e}")
        raise

def ingest_and_preprocess(project_id: str, dataset_id: str, subreddits: List[str], bucket_name: str) -> None:
    """
    Main function to run the Reddit data ingestion and preprocessing pipeline.
    
    Pipeline steps:
    1. Fetch Reddit data and save to GCS
    2. Use Spark to read from GCS and write to BigQuery raw and processed tables
    3. Generate daily summaries
    
    Args:
        project_id: GCP project ID
        dataset_id: BigQuery dataset ID
        subreddits: List of subreddits to process
        bucket_name: GCS bucket name for raw data
    """
 #   setup_logging()
    spark = None
    try:
        # Initialize clients with explicit project
        bq_client = bigquery.Client(project=project_id)
        storage_client = storage.Client(project=project_id)
        
        # Create Spark session
        spark = create_spark_session(project_id)
        logger.info("Created Spark session successfully")
        
        # Verify BigQuery environment
        setup_bigquery_environment(bq_client, project_id, subreddits)
        
        # Initialize Reddit client
        reddit = reddit_client.create_reddit_instance(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            username=os.environ["REDDIT_USERNAME"],
            password=os.environ["REDDIT_PASSWORD"],
            user_agent=os.environ["REDDIT_USER_AGENT"]
        )
        
        # Fetch Reddit data and save to GCS
        for subreddit in subreddits:
            reddit_client.fetch_and_save_posts(
                reddit=reddit,
                storage_client=storage_client,
                bigquery_client=bq_client,
                project_id=project_id,
                dataset_id=dataset_id,
                bucket_name=bucket_name,
                subreddit_name=subreddit
            )
            logger.info(f"Completed fetching posts for r/{subreddit}")
        
        # Process data using Spark (both raw and processed tables)
        data_processing.preprocess_data(spark, bq_client, project_id, dataset_id, subreddits, bucket_name)
        logger.info("Data processing completed successfully")
        
        # Generate daily summaries
        logger.info("Generating daily summaries...")
        daily_summary.generate_daily_summaries(spark, project_id, dataset_id, subreddits, bucket_name)
        logger.info("Daily summary generation completed successfully")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise
    finally:
        if spark:
            spark.stop()
            logger.info("Spark session stopped")

if __name__ == "__main__":
    # Required environment variables
    required_vars = [
        "GCP_PROJECT_ID",
        "GOOGLE_APPLICATION_CREDENTIALS",
        "REDDIT_CLIENT_ID",
        "REDDIT_CLIENT_SECRET",
        "REDDIT_USERNAME",
        "REDDIT_PASSWORD",
        "REDDIT_USER_AGENT",
        "GCS_BUCKET_NAME"
    ]
    
    # Check for required environment variables
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Configuration
    PROJECT_ID = os.environ["GCP_PROJECT_ID"]
    DATASET_ID = "processed_data"
    BUCKET_NAME = os.environ["GCS_BUCKET_NAME"]
    
    ingest_and_preprocess(PROJECT_ID, DATASET_ID, SUBREDDITS, BUCKET_NAME) 