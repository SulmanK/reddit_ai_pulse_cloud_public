"""
Data Ingestion and Preprocessing Connector

This script connects the Airflow DAG to the Reddit data ingestion and preprocessing pipeline.
It handles the initial data collection from Reddit API and preprocessing steps.

Owner: Sulman Khan
"""

import os
import sys
import logging
from pathlib import Path

# Setup paths for Docker environment
AIRFLOW_DIR = "/opt/airflow"  # Root in Docker container
PROJECT_ROOT = AIRFLOW_DIR  # Cloud directory is mounted here
CLOUD_SCRIPTS_DIR = os.path.join(PROJECT_ROOT, 'scripts')

# Add necessary paths
sys.path.extend([PROJECT_ROOT, CLOUD_SCRIPTS_DIR])

def ingest_preprocess_process():
    """
    Connector function to run the ingest and preprocess pipeline.
    
    Imports and executes the main ingestion and preprocessing module,
    with comprehensive logging for debugging path and import issues.
    
    Raises:
        ImportError: If the required modules cannot be imported
        Exception: For any other errors during execution
    """
    try:
        from scripts.ingest_preprocess import ingest_and_preprocess
        from config.config import SUBREDDITS
        
        logging.info(f"Current working directory: {os.getcwd()}")
        logging.info(f"Project root: {PROJECT_ROOT}")
        logging.info(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.info(f"Python path: {sys.path}")
        
        # Get configuration from environment variables
        project_id = os.environ.get("GCP_PROJECT_ID")
        bucket_name = os.environ.get("GCS_BUCKET_NAME")
        dataset_id = "processed_data"  # This is a fixed value as per the main script
        
        if not project_id or not bucket_name:
            raise ValueError("Missing required environment variables: GCP_PROJECT_ID or GCS_BUCKET_NAME")
        
        ingest_and_preprocess(
            project_id=project_id,
            dataset_id=dataset_id,
            subreddits=SUBREDDITS,
            bucket_name=bucket_name
        )
    except ImportError as e:
        logging.error(f"Import error: {e}")
        logging.error(f"Current working directory: {os.getcwd()}")
        logging.error(f"Project root: {PROJECT_ROOT}")
        logging.error(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.error(f"Python path: {sys.path}")
        raise
    except Exception as e:
        logging.error(f"Error running ingest and preprocess: {e}")
        raise

if __name__ == "__main__":
    ingest_preprocess_process() 