"""
Gemini Analysis Connector

This script connects the Airflow DAG to the Gemini analysis pipeline.
It handles the Gemini-based analysis of preprocessed Reddit data.

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

def gemini_analysis_process():
    """
    Connector function to run the Gemini analysis pipeline.
    
    Imports and executes the main Gemini analysis module,
    with comprehensive logging for debugging path and import issues.
    
    Raises:
        ImportError: If the required modules cannot be imported
        Exception: For any other errors during execution
    """
    try:
        from scripts.gemini_analyzer import analyze_data
        
        logging.info(f"Current working directory: {os.getcwd()}")
        logging.info(f"Project root: {PROJECT_ROOT}")
        logging.info(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.info(f"Python path: {sys.path}")
        
        analyze_data()
    except ImportError as e:
        logging.error(f"Import error: {e}")
        logging.error(f"Current working directory: {os.getcwd()}")
        logging.error(f"Project root: {PROJECT_ROOT}")
        logging.error(f"Scripts directory: {CLOUD_SCRIPTS_DIR}")
        logging.error(f"Python path: {sys.path}")
        raise
    except Exception as e:
        logging.error(f"Error running Gemini analysis: {e}")
        raise

if __name__ == "__main__":
    gemini_analysis_process() 