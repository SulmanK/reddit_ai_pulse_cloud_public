"""
Sentiment Analysis Module for Cloud Environment

This module performs emotion analysis on Reddit comments using a pre-trained model.
It processes comments from BigQuery and saves the sentiment analysis results.

Owner: Sulman Khan
"""

import os
import sys
from datetime import datetime
from google.cloud import bigquery
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import mlflow
import mlflow.transformers

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from utils.custom_logging import get_logger, setup_logging

# Configure logging with absolute path
LOGS_DIR = os.path.join(CLOUD_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
logger = setup_logging(script_name='sentiment_analysis', log_dir=LOGS_DIR)

# Define emotion labels mapping
EMOTION_LABELS = {
    'admiration': 'Admiration', 'amusement': 'Amusement', 'anger': 'Anger',
    'annoyance': 'Annoyance', 'approval': 'Approval', 'caring': 'Caring',
    'confusion': 'Confusion', 'curiosity': 'Curiosity', 'desire': 'Desire',
    'disappointment': 'Disappointment', 'disapproval': 'Disapproval',
    'disgust': 'Disgust', 'embarrassment': 'Embarrassment',
    'excitement': 'Excitement', 'fear': 'Fear', 'gratitude': 'Gratitude',
    'grief': 'Grief', 'joy': 'Joy', 'love': 'Love',
    'nervousness': 'Nervousness', 'optimism': 'Optimism', 'pride': 'Pride',
    'realization': 'Realization', 'relief': 'Relief', 'remorse': 'Remorse',
    'sadness': 'Sadness', 'surprise': 'Surprise', 'neutral': 'Neutral'
}

def initialize_emotion_analyzer():
    """
    Initialize the emotion analysis model and tokenizer.
    
    Returns:
        pipeline: The emotion analysis pipeline
        
    Raises:
        Exception: If there is an error loading the model
    """
    try:
        model_name = "SamLowe/roberta-base-go_emotions"
        local_model_path = "/models/models--SamLowe--roberta-base-go_emotions/snapshots/58b6c5b44a7a12093f782442969019c7e2982299"

        model = AutoModelForSequenceClassification.from_pretrained(local_model_path)
        tokenizer = AutoTokenizer.from_pretrained(local_model_path)

        emotion_analyzer = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer
        )

        return emotion_analyzer
    except Exception as e:
        logger.error(f"Error initializing emotion analyzer: {e}")
        raise

def truncate_text(text, max_length=500):
    """
    Truncates text to a maximum length while trying to preserve complete sentences.
    
    Args:
        text (str): The text to truncate
        max_length (int): Maximum length of text (default 500 to stay well within model limits)
    
    Returns:
        str: Truncated text
    """
    if not text or len(text) <= max_length:
        return text
    
    # Try to find the last sentence boundary before max_length
    truncated = text[:max_length]
    last_period = truncated.rfind('.')
    last_question = truncated.rfind('?')
    last_exclamation = truncated.rfind('!')
    
    # Find the last sentence boundary
    cut_point = max(last_period, last_question, last_exclamation)
    
    # If no sentence boundary found, just cut at max_length
    if cut_point == -1:
        return truncated.rsplit(' ', 1)[0] + '...'
    
    return text[:cut_point + 1]

def perform_sentiment_analysis(text, emotion_analyzer):
    """
    Perform sentiment analysis on the given text.
    
    Args:
        text (str): Text to analyze
        emotion_analyzer: The emotion analysis model
    
    Returns:
        tuple: (sentiment_label, sentiment_score, emotion_description)
    """
    try:
        if not text or text.strip() == "":
            return "Neutral", 0.0, "No content"
            
        # Truncate text before analysis
        truncated_text = truncate_text(text)
        
        # Perform emotion analysis
        emotion_output = emotion_analyzer(truncated_text)
        
        if not emotion_output or len(emotion_output) == 0:
            return "Neutral", 0.0, "Analysis failed"
            
        # Get the predicted emotion and score
        emotion_label = emotion_output[0]['label']
        emotion_score = emotion_output[0]['score']
        
        # Map emotion to sentiment
        sentiment_mapping = {
            'joy': 'Positive',
            'love': 'Positive',
            'admiration': 'Positive',
            'approval': 'Positive',
            'caring': 'Positive',
            'excitement': 'Positive',
            'gratitude': 'Positive',
            'pride': 'Positive',
            'optimism': 'Positive',
            'relief': 'Positive',
            'anger': 'Negative',
            'annoyance': 'Negative',
            'disappointment': 'Negative',
            'disapproval': 'Negative',
            'disgust': 'Negative',
            'embarrassment': 'Negative',
            'fear': 'Negative',
            'grief': 'Negative',
            'nervousness': 'Negative',
            'remorse': 'Negative',
            'sadness': 'Negative',
            'confusion': 'Neutral',
            'curiosity': 'Neutral',
            'realization': 'Neutral',
            'surprise': 'Neutral',
            'neutral': 'Neutral'
        }
        
        sentiment_label = sentiment_mapping.get(emotion_label.lower(), 'Neutral')
        
        return sentiment_label, float(emotion_score), emotion_label
        
    except Exception as e:
        logger.error(f"Error during sentiment analysis: {str(e)}")
        return "Neutral", 0.0, "Error in analysis"

def analyze_sentiment():
    """
    Main function to perform sentiment analysis on Reddit comments.
    
    Pipeline steps:
    1. Set up logging and MLflow tracking
    2. Initialize sentiment analyzer
    3. Connect to BigQuery
    4. Process comments and save results
    
    Note:
        - Uses MLflow for experiment tracking
        - Implements batch processing
        - Handles BigQuery transactions safely
    """
    try:
        # MLflow setup
        mlflow.set_tracking_uri("http://mlflow:5000")
        mlflow.set_experiment("reddit_sentiment_analysis_experiments")
        
        with mlflow.start_run() as run:
            mlflow.log_param("model_name", "SamLowe/roberta-base-go_emotions")
            
            # Initialize components
            emotion_analyzer = initialize_emotion_analyzer()
            logger.info("Emotion analysis model loaded")

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
            sentiment_results = []
            for row in rows:
                try:
                    comment_id = row.comment_id
                    comment_body = row.comment_body
                    
                    # Perform sentiment analysis
                    sentiment_label, sentiment_score, _ = perform_sentiment_analysis(
                        comment_body, emotion_analyzer
                    )
                    
                    # Add to batch
                    sentiment_results.append({
                        'comment_id': comment_id,
                        'sentiment_score': sentiment_score,
                        'sentiment_label': sentiment_label
                    })
                    
                    logger.info(f"Analyzed sentiment for comment_id: {comment_id}")
                    
                except Exception as e:
                    logger.error(f"Error processing comment {comment_id}: {str(e)}")
                    continue

            # Batch insert results to BigQuery
            if sentiment_results:
                table_id = 'processed_data.sentiment_analysis_results'
                
                try:
                    # Get table reference
                    table_ref = client.dataset('processed_data').table('sentiment_analysis_results')
                    table = client.get_table(table_ref)
                    
                    # Convert results to rows
                    rows_to_insert = [
                        {
                            'comment_id': result['comment_id'],
                            'sentiment_score': result['sentiment_score'],
                            'sentiment_label': result['sentiment_label']
                        }
                        for result in sentiment_results
                    ]
                    
                    # Insert data
                    errors = client.insert_rows_json(table, rows_to_insert)
                    
                    if errors:
                        logger.error(f"Encountered errors while inserting rows: {errors}")
                        raise Exception(f"Failed to insert rows: {errors}")
                    else:
                        logger.info(f"Successfully inserted {len(rows_to_insert)} sentiment results")
                        
                except Exception as e:
                    logger.error(f"Error inserting results to BigQuery: {str(e)}")
                    raise

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    analyze_sentiment() 