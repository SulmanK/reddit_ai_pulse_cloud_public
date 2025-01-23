"""
Sentiment Analysis Connector

This script connects the Airflow DAG to the sentiment analysis pipeline.
It handles the sentiment analysis of preprocessed Reddit data.

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

def sentiment_analysis_process():
    """
    Connector function to run the sentiment analysis pipeline.
    
    Imports and executes the main sentiment analysis module,
    with comprehensive logging for debugging path and import issues.
    
    Raises:
        ImportError: If the required modules cannot be imported
        Exception: For any other errors during execution
    """
    try:
        from scripts.sentiment_analysis import analyze_sentiment
        
        logging.info(f"Current working directory: {os.getcwd()}")
        logging.info(f"Project root: {PROJECT_ROOT}")
        logging.info(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.info(f"Python path: {sys.path}")
                
        analyze_sentiment()
    except ImportError as e:
        logging.error(f"Import error: {e}")
        logging.error(f"Current working directory: {os.getcwd()}")
        logging.error(f"Project root: {PROJECT_ROOT}")
        logging.error(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.error(f"Python path: {sys.path}")
        raise
    except Exception as e:
        logging.error(f"Error running sentiment analysis: {e}")
        raise

if __name__ == "__main__":
    sentiment_analysis_process() 