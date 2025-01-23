"""
Text Summarization Module for Cloud Environment

This module handles the summarization of Reddit comments using a pre-trained BART model.
It processes comments from BigQuery and saves the generated summaries.

Owner: Sulman Khan
"""

import os
import sys
from datetime import datetime
from google.cloud import bigquery
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import mlflow
import mlflow.transformers
import torch

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from utils.custom_logging import get_logger, setup_logging

# Configure logging with absolute path
LOGS_DIR = os.path.join(CLOUD_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
logger = setup_logging(script_name='summarize', log_dir=LOGS_DIR)

def create_summarizer():
    """
    Initialize and return the summarization model.
    
    Returns:
        pipeline: The summarization pipeline
        
    Raises:
        Exception: If there is an error loading the model
    """
    try:
        # Set environment variable for tokenizer
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        
        # Load model and tokenizer
        model_name = "philschmid/bart-large-cnn-samsum"
        local_model_path = "/models/models--philschmid--bart-large-cnn-samsum/snapshots/e49b3d60d923f12db22bdd363356f1a4c68532ad"

        tokenizer = AutoTokenizer.from_pretrained(local_model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(
            local_model_path,
            torch_dtype=torch.float32,
            device_map="auto",
            low_cpu_mem_usage=True
        )
        
        summarizer = pipeline(
            "summarization",
            model=model,
            tokenizer=tokenizer,
            framework="pt"
        )
        
        return summarizer
    except Exception as e:
        logger.error(f"Error loading summarization model: {str(e)}")
        raise

def generate_summary(comment_body, summarizer):
    """
    Generate summary for a given comment.
    
    Args:
        comment_body (str): Text to summarize
        summarizer: The summarization pipeline
        
    Returns:
        str: Summarized text or original text if short enough
    """
    if not comment_body:
        return ""
        
    if len(comment_body.split()) <= 59:
        logger.info("Comment is less than the max length")
        return comment_body 
        
    try:
        summary = summarizer(comment_body, max_length=60, min_length=15, do_sample=False, truncation=True)
        if summary and isinstance(summary, list) and len(summary) > 0:
            return summary[0]['summary_text']
    except Exception as e:
        logger.error(f"Summarization failed: {e}")
    
    return ""

def summarize_posts():
    """
    Main function to summarize Reddit posts and comments.
    
    Pipeline steps:
    1. Set up logging and MLflow tracking
    2. Initialize summarizer model
    3. Connect to BigQuery
    4. Process comments and save summaries
    
    Note:
        - Uses MLflow for experiment tracking
        - Implements efficient text processing
        - Handles BigQuery transactions safely
    """
    try:
        # MLflow setup
        mlflow.set_tracking_uri("http://mlflow:5000")
        mlflow.set_experiment("reddit_summarization_experiments")
        
        with mlflow.start_run() as run:
            # Log parameters
            mlflow.log_param("model_name", "philschmid/bart-large-cnn-samsum")
            mlflow.log_param("max_length", 60)
            mlflow.log_param("min_length", 15)
            mlflow.log_param("do_sample", False)

            # Initialize components
            summarizer = create_summarizer()
            logger.info("Summarization model loaded")

            # Initialize BigQuery client
            client = bigquery.Client()
            
            # Fetch data from current_summary_staging view
            query = """
                SELECT 
                    post_id, subreddit, post_score, post_url, comment_id,
                    summary_date, post_content, comment_body
                FROM `processed_data.current_summary_staging`
            """
            
            query_job = client.query(query)
            rows = list(query_job.result())
            logger.info(f"Fetched {len(rows)} rows from BigQuery")

            # Process each comment
            summaries = []
            for row in rows:
                try:
                    comment_id = row.comment_id
                    comment_body = row.comment_body
                    
                    # Generate summary
                    summary_text = generate_summary(comment_body, summarizer)
                    
                    # Add to batch
                    summaries.append({
                        'comment_id': comment_id,
                        'comment_summary': summary_text
                    })
                    
                    logger.info(f"Generated summary for comment_id: {comment_id}")
                    
                except Exception as e:
                    logger.error(f"Error processing comment {comment_id}: {str(e)}")
                    continue

            # Batch insert results to BigQuery
            if summaries:
                table_id = 'processed_data.text_summary_results'
                
                try:
                    # Get table reference
                    table_ref = client.dataset('processed_data').table('text_summary_results')
                    table = client.get_table(table_ref)
                    
                    # Convert results to rows
                    rows_to_insert = [
                        {
                            'comment_id': summary['comment_id'],
                            'comment_summary': summary['comment_summary']
                        }
                        for summary in summaries
                    ]
                    
                    # Insert data
                    errors = client.insert_rows_json(table, rows_to_insert)
                    
                    if errors:
                        logger.error(f"Encountered errors while inserting rows: {errors}")
                        raise Exception(f"Failed to insert rows: {errors}")
                    else:
                        logger.info(f"Successfully inserted {len(rows_to_insert)} summaries")
                        
                except Exception as e:
                    logger.error(f"Error inserting results to BigQuery: {str(e)}")
                    raise

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    summarize_posts() 