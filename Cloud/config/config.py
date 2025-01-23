"""
GCP Configuration Management Module

This module manages configuration settings for the Reddit Data Pipeline cloud implementation.
It handles GCP service configurations, credentials, and environment-specific settings.
"""

import os
from google.cloud import storage  # type: ignore
from google.cloud import bigquery  # type: ignore
from google.oauth2 import service_account
from dotenv import load_dotenv
from typing import Dict, Any

# Load environment variables
load_dotenv()

# GCP Project Configuration
GCP_CONFIG = {
    "project_id": os.getenv("GCP_PROJECT_ID"),
    "region": os.getenv("GCP_REGION"),
    "zone": os.getenv("GCP_ZONE"),
}

# VM Configuration
VM_CONFIG = {
    "instance_name": os.getenv("VM_INSTANCE_NAME"),
    "machine_type": os.getenv("VM_MACHINE_TYPE"),
    "zone": os.getenv("GCP_ZONE"),
}

# Storage Configuration
STORAGE_CONFIG = {
    "raw_bucket": os.getenv("GCS_BUCKET_RAW"),
    "processed_bucket": os.getenv("GCS_BUCKET_PROCESSED"),
}

# BigQuery Configuration
BIGQUERY_CONFIG = {
    "raw_dataset": os.getenv("BIGQUERY_DATASET_RAW"),
    "processed_dataset": os.getenv("BIGQUERY_DATASET_PROCESSED")
}

# Reddit API Configuration
REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
}

# Gemini API Configuration
GEMINI_CONFIG = {
    "GOOGLE_GEMINI_API_KEY": os.getenv("GOOGLE_GEMINI_API_KEY"),
}

# GCS Bucket Configuration
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")

def get_gcp_credentials():
    """
    Get GCP credentials from service account key file.
    
    Returns:
        google.oauth2.service_account.Credentials: GCP credentials object
    """
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    return service_account.Credentials.from_service_account_file(credentials_path)

def get_storage_client():
    """
    Get authenticated GCS client.
    
    Returns:
        google.cloud.storage.Client: Authenticated GCS client
    """
    credentials = get_gcp_credentials()
    return storage.Client(credentials=credentials, project=GCP_CONFIG["project_id"])

def get_bigquery_client():
    """
    Get authenticated BigQuery client.
    
    Returns:
        google.cloud.bigquery.Client: Authenticated BigQuery client
    """
    credentials = get_gcp_credentials()
    return bigquery.Client(credentials=credentials, project=GCP_CONFIG["project_id"])

def get_vm_config() -> Dict[str, Any]:
    """
    Get VM configuration settings.
    
    Returns:
        Dict[str, Any]: VM configuration dictionary
    """
    return VM_CONFIG

def get_storage_config() -> Dict[str, str]:
    """
    Get storage configuration settings.
    
    Returns:
        Dict[str, str]: Storage configuration dictionary
    """
    return STORAGE_CONFIG

def get_bigquery_config() -> Dict[str, str]:
    """
    Get BigQuery configuration settings.
    
    Returns:
        Dict[str, str]: BigQuery configuration dictionary
    """
    return BIGQUERY_CONFIG

# Target subreddits (keeping from local implementation)
SUBREDDITS = [
    "dataengineering",
    "machinelearning",
    "datascience",
    "claudeai",
    "singularity",
    "localllama",
    "openai",
    "stablediffusion"
] 

