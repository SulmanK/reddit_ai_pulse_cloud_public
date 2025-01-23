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

def extract_gemini_metrics(log_path):
    """Extract metrics from Gemini analysis task logs"""
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
                'outputs_generated': 0,
                'attempt': attempt,
                'duration_seconds': 0,
                'subreddits_processed': 0
            }
            
            with open(try_path, 'r') as f:
                log_content = f.readlines()
                
            success = False
            start_time = None
            end_time = None
            
            for line in log_content:
                timestamp_match = re.search(r"\[(.*?)\]", line)
                
                # Look for start time when model is loaded
                if "Model loaded" in line and timestamp_match:
                    try:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                    logging.info(f"Found start time: {start_time}")
                
                # Count subreddits being analyzed
                elif "Analyzing data for subreddit:" in line:
                    metrics['subreddits_processed'] += 1
                    logging.info(f"Found subreddit being processed: {metrics['subreddits_processed']}")
                
                # Count successful outputs
                elif "Output saved to" in line:
                    metrics['outputs_generated'] += 1
                    logging.info(f"Found output generated: {metrics['outputs_generated']}")
                
                # Look for completion
                elif "Analysis complete - all files processed and uploaded to GCS" in line:
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
                statsd_client.timing('gemini.duration', metrics['duration_seconds'] * 1000)
                logging.info(f"Calculated duration: {metrics['duration_seconds']} seconds")
            
            # Success is when all subreddits have outputs
            success = metrics['outputs_generated'] == metrics['subreddits_processed']
            metrics['next_attempt'] = 1 if success else metrics['attempt'] + 1
            
            # Send metrics to StatsD
            statsd_client.gauge('gemini.outputs_generated', metrics['outputs_generated'])
            statsd_client.gauge('gemini.subreddits_processed', metrics['subreddits_processed'])
            statsd_client.gauge('gemini.current_attempt', metrics['attempt'])
            
            if success:
                statsd_client.incr('gemini.success')
            else:
                statsd_client.incr('gemini.retry')
            
            logging.info(f"""
            Gemini Task Metrics Summary:
            - Subreddits Processed: {metrics['subreddits_processed']}
            - Outputs Generated: {metrics['outputs_generated']}
            - Current Attempt: {metrics['attempt']}
            - Next Attempt Should Be: {metrics['next_attempt']}
            - Duration: {metrics['duration_seconds']:.2f} seconds
            """)
            
            return metrics
            
        except Exception as e:
            logging.warning(f"Failed to read metrics from attempt {attempt}: {str(e)}")
            continue
    
    # If we get here, we couldn't read any log files
    statsd_client.incr('gemini.error')
    error_msg = f"Could not find any valid log files in attempts 1-2 at base path: {base_path}"
    logging.error(error_msg)
    raise FileNotFoundError(error_msg) 