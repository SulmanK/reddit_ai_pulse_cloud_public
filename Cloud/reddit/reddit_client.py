"""
Reddit API Client Module for Cloud Environment

This module handles the interaction with Reddit's API using PRAW.
It collects data from specified subreddits and stores raw data in GCS.
Includes incremental loading to avoid duplicate data collection.

Owner: Sulman Khan
"""

import os
import sys

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

import json
import praw
from datetime import datetime, timedelta
from google.cloud import storage, bigquery
from typing import Dict, List, Optional, Tuple
import time
from utils.custom_logging import get_logger
from config.config import REDDIT_CONFIG

# Configure logging
logger = get_logger(__name__)

def extract_post_data(post: praw.models.Submission) -> Dict:
    """Extracts relevant data from a Reddit post."""
    post_data = {
        'subreddit': str(post.subreddit),
        'post_id': post.id,
        'title': post.title,
        'author': str(post.author),
        'url': post.url,
        'score': post.score,
        'created_utc': post.created_utc,
        'ingestion_timestamp': datetime.utcnow().timestamp(),
        'comments': []
    }
    
    # Get top comments
    post.comment_sort = 'top'
    post.comments.replace_more(limit=0)
    for comment in post.comments[:10]:  # Get top 10 comments
        try:
            comment_data = {
                'comment_id': comment.id,
                'author': str(comment.author),
                'body': comment.body,
                'created_utc': comment.created_utc
            }
            post_data['comments'].append(comment_data)
        except Exception as e:
            logger.warning(f"Error processing comment {comment.id}: {e}")
            continue
    
    return post_data

def save_to_gcs(storage_client: storage.Client, bucket_name: str, 
                subreddit_name: str, posts: List[Dict]) -> None:
    """Saves posts data to Google Cloud Storage."""
    try:
        # Get bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Generate blob name with current timestamp
        batch_timestamp = datetime.utcnow()
        blob_name = get_gcs_blob_name(subreddit_name, batch_timestamp)
        blob = bucket.blob(blob_name)
        
        # If no posts, create a dummy file with a placeholder message
        if not posts:
            dummy_post = {
                "subreddit": subreddit_name,
                "post_id": "no_posts_today",
                "title": "There are no posts for this subreddit today",
                "author": "placeholder",
                "url": f"https://www.reddit.com/r/{subreddit_name}/",
                "score": 0,
                "created_utc": batch_timestamp.timestamp(),
                "ingestion_timestamp": batch_timestamp.timestamp(),
                "comments": []
            }
            ndjson_data = json.dumps(dummy_post)
            logger.info(f"No posts found for {subreddit_name}, creating dummy file: {blob_name}")
        else:
            # Convert to newline-delimited JSON
            ndjson_data = '\n'.join(json.dumps(post) for post in posts)
            logger.info(f"Saved {len(posts)} posts to GCS: {blob_name}")
            
        blob.upload_from_string(ndjson_data)
        
    except Exception as e:
        logger.error(f"Error saving to GCS: {e}")
        raise

def create_reddit_instance(client_id: str, client_secret: str, 
                         username: str, password: str, user_agent: str) -> praw.Reddit:
    """Creates an instance of the Reddit client (praw.Reddit)."""
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=user_agent
        )
        logger.info("Successfully created Reddit instance")
        return reddit
    except Exception as e:
        logger.error(f"Error connecting to Reddit API: {e}")
        raise

def get_last_processed_timestamp(client: bigquery.Client, project_id: str, 
                               dataset_id: str, subreddit: str) -> float:
    """Gets the timestamp of the last processed post for a subreddit from the metadata table."""
    query = f"""
    SELECT last_processed_timestamp
    FROM `{project_id}.{dataset_id}.processing_metadata`
    WHERE subreddit = '{subreddit.lower()}'
    ORDER BY last_update_time DESC
    LIMIT 1
    """
    try:
        query_job = client.query(query)
        result = next(query_job.result(), None)
        return float(result.last_processed_timestamp) if result else 0.0
    except Exception as e:
        logger.warning(f"Error getting last timestamp for {subreddit}: {e}")
        return 0.0

def verify_metadata_table(client: bigquery.Client, project_id: str, dataset_id: str) -> None:
    """Verifies that the processing_metadata table exists and has the correct schema."""
    table_id = f"{project_id}.{dataset_id}.processing_metadata"
    
    try:
        table = client.get_table(table_id)
        logger.info(f"Found existing metadata table: {table_id}")
    except Exception as e:
        logger.warning(f"Metadata table not found, creating: {e}")
        # Create table with schema
        schema = [
            bigquery.SchemaField("subreddit", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("last_processed_timestamp", "FLOAT", mode="REQUIRED"),
            bigquery.SchemaField("last_update_time", "TIMESTAMP", mode="REQUIRED")
        ]
        table = bigquery.Table(table_id, schema=schema)
        table = client.create_table(table, exists_ok=True)
        logger.info(f"Created metadata table: {table_id}")

def update_processing_metadata(client: bigquery.Client, project_id: str, dataset_id: str, 
                             subreddit: str, last_processed_timestamp: float) -> None:
    """Updates the processing metadata for a subreddit with retry logic."""
    # First verify table exists
    verify_metadata_table(client, project_id, dataset_id)
    
    table_id = f"{project_id}.{dataset_id}.processing_metadata"
    current_time = datetime.utcnow().isoformat()
    
    rows_to_insert = [{
        'subreddit': subreddit,
        'last_processed_timestamp': last_processed_timestamp,
        'last_update_time': current_time
    }]

    max_retries = 3
    retry_count = 0
    last_error = None

    while retry_count < max_retries:
        try:
            # Try to get the table first to ensure it exists
            client.get_table(table_id)
            
            # Then try to insert
            errors = client.insert_rows_json(table_id, rows_to_insert)
            if not errors:
                logger.info(f"Successfully updated metadata for {subreddit}")
                return
            else:
                raise Exception(f"Errors occurred while inserting rows: {errors}")
        except Exception as e:
            last_error = e
            retry_count += 1
            if retry_count < max_retries:
                logger.warning(f"Attempt {retry_count} failed, retrying in {2**retry_count} seconds: {e}")
                time.sleep(2**retry_count)  # Exponential backoff
            else:
                logger.error(f"Failed to update metadata after {max_retries} attempts: {e}")
                raise last_error

def get_gcs_blob_name(subreddit_name: str, batch_timestamp: datetime) -> str:
    """
    Generates a GCS blob name for the Reddit data.
    Format: raw/reddit_data/YYYY/MM/DD/subreddit/batch_HHMMSS.json
    """
    date_path = batch_timestamp.strftime("%Y/%m/%d")
    time_str = batch_timestamp.strftime("%H%M%S")
    return f"raw/reddit_data/{date_path}/{subreddit_name}/batch_{time_str}.json"

def fetch_and_save_posts(reddit: praw.Reddit, storage_client: storage.Client, 
                        bigquery_client: bigquery.Client, project_id: str,
                        dataset_id: str, bucket_name: str, subreddit_name: str) -> None:
    """Fetches posts from a subreddit and saves them to GCS and BigQuery."""
    try:
        # Get last processed timestamp
        last_timestamp = get_last_processed_timestamp(bigquery_client, project_id, dataset_id, subreddit_name)
        
        # Fetch and process posts
        subreddit = reddit.subreddit(subreddit_name)
        new_posts = []
        latest_timestamp = last_timestamp

        for post in subreddit.new(limit=20):  # Adjust limit as needed
            post_timestamp = float(post.created_utc)
            
            # Skip if we've already processed this post
            if post_timestamp <= last_timestamp:
                continue
                
            latest_timestamp = max(latest_timestamp, post_timestamp)
            
            try:
                post_data = extract_post_data(post)
                new_posts.append(post_data)
                logger.info(f"Collected post {post.id} from r/{subreddit_name}")
            except Exception as e:
                logger.error(f"Error processing post {post.id}: {e}")
                continue

        # Always save to GCS, even if new_posts is empty
        save_to_gcs(storage_client, bucket_name, subreddit_name, new_posts)
        
        if new_posts:
            # Update processing metadata with retry logic
            update_processing_metadata(
                bigquery_client,
                project_id,
                dataset_id,
                subreddit_name,
                latest_timestamp
            )
        else:
            logger.info(f"No new posts to process for r/{subreddit_name}")

    except Exception as e:
        logger.error(f"Failed to fetch posts from r/{subreddit_name}: {e}")
        raise 