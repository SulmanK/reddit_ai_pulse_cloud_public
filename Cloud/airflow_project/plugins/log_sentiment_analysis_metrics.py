import logging
import re
import time
import statsd
import os
from datetime import datetime
from airflow_project.plugins.logging_utils import get_log_path

# Initialize StatsD client
statsd_client = statsd.StatsClient(
    host='statsd-exporter',
    port=9125,
    prefix='airflow.reddit'
)

def extract_sentiment_metrics(log_path):
    """Extract metrics from sentiment analysis task logs"""
    # Get the base path without attempt number
    base_path = re.sub(r'/attempt=\d+\.log$', '', log_path)
    logging.info(f"Base log path: {base_path}")
    
    # Try attempts in descending order starting from 2
    for attempt in range(2, 0, -1):
        try_path = f"{base_path}/attempt={attempt}.log"
        logging.info(f"Trying log path: {try_path}")
        
        if not os.path.exists(try_path):
            logging.warning(f"Log file not found at: {try_path}")
            continue
            
        try:
            metrics = {
                'sentiments_processed': 0,
                'attempt': attempt,
                'duration_seconds': 0
            }
            
            with open(try_path, 'r') as f:
                log_content = f.readlines()
                
            success = False
            start_time = None
            end_time = None
            
            for line in log_content:
                timestamp_match = re.search(r"\[(.*?)\]", line)
                
                # Look for start time when model is loaded
                if "Emotion analysis model loaded" in line and timestamp_match:
                    try:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                    logging.info(f"Found start time: {start_time}")
                
                # Look for completion and total count
                elif "Successfully inserted" in line:
                    # Extract total count from "Successfully inserted X sentiment results"
                    count_match = re.search(r"Successfully inserted (\d+) sentiment results", line)
                    if count_match:
                        metrics['sentiments_processed'] = int(count_match.group(1))
                        logging.info(f"Found {metrics['sentiments_processed']} sentiments processed")
                    
                    if timestamp_match:
                        try:
                            end_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                        except ValueError:
                            end_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                        success = True
                        logging.info(f"Found end time: {end_time}")
            
            # Calculate duration if we have both timestamps
            if start_time and end_time:
                metrics['duration_seconds'] = (end_time - start_time).total_seconds()
                statsd_client.timing('sentiment.duration', metrics['duration_seconds'] * 1000)
                logging.info(f"Calculated duration: {metrics['duration_seconds']} seconds")
            
            metrics['next_attempt'] = 1 if success else metrics['attempt'] + 1
            
            # Send metrics to StatsD
            statsd_client.gauge('sentiment.sentiments_processed', metrics['sentiments_processed'])
            statsd_client.gauge('sentiment.current_attempt', metrics['attempt'])
            
            if success:
                statsd_client.incr('sentiment.success')
            else:
                statsd_client.incr('sentiment.retry')
            
            logging.info(f"""
            Sentiment Analysis Task Metrics Summary:
            - Sentiments Processed: {metrics['sentiments_processed']}
            - Current Attempt: {metrics['attempt']}
            - Next Attempt Should Be: {metrics['next_attempt']}
            - Duration: {metrics['duration_seconds']:.2f} seconds
            """)
            
            return metrics
            
        except Exception as e:
            logging.warning(f"Failed to read metrics from attempt {attempt}: {str(e)}")
            continue
    
    # If we get here, we couldn't read any log files
    statsd_client.incr('sentiment.error')
    error_msg = f"Could not find any valid log files in attempts 1-2 at base path: {base_path}"
    logging.error(error_msg)
    raise FileNotFoundError(error_msg) 