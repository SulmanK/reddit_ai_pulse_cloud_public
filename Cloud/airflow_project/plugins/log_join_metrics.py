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

def extract_join_metrics(log_path):
    """Extract metrics from join task logs"""
    # Get the base path without attempt number
    base_path = re.sub(r'/attempt=\d+\.log$', '', log_path)
    
    # Try attempts in descending order starting from 2
    for attempt in range(2, 0, -1):
        try_path = f"{base_path}/attempt={attempt}.log"
        if not os.path.exists(try_path):
            continue
            
        try:
            metrics = {
                'records_joined': 0,
                'attempt': attempt,
                'duration_seconds': 0
            }
            
            with open(try_path, 'r') as f:
                log_content = f.readlines()
            
            success = False
            start_time = None
            end_time = None
            
            for line in log_content:
                # Look for timestamps with new format
                timestamp_match = re.search(r"\[(.*?)\]", line)
                
                # Update start time condition to match actual log
                if "Executing <Task(BashOperator): run_dbt_join_summary_analysis>" in line and timestamp_match:
                    try:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                
                # Update end time condition to match actual log
                elif "Marking task as SUCCESS" in line and timestamp_match:
                    try:
                        end_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        end_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                    success = True
                
                # Extract row count from dbt output
                elif "CREATE TABLE" in line and "rows" in line:
                    rows_match = re.search(r"CREATE TABLE \((\d+\.?\d*) rows", line)
                    if rows_match:
                        metrics['records_joined'] = int(float(rows_match.group(1)))
            
            # Calculate duration if we have both timestamps
            if start_time and end_time:
                metrics['duration_seconds'] = (end_time - start_time).total_seconds()
                statsd_client.timing('join.duration', metrics['duration_seconds'] * 1000)
            
            metrics['next_attempt'] = 1 if success else metrics['attempt'] + 1
            
            # Send metrics using the StatsD client
            statsd_client.gauge('join.records_joined', metrics['records_joined'])
            statsd_client.gauge('join.current_attempt', metrics['attempt'])
            
            if success:
                statsd_client.incr('join.success')
            else:
                statsd_client.incr('join.retry')
            
            logging.info(f"""
            Join Task Metrics Summary:
            - Records Joined: {metrics['records_joined']}
            - Current Attempt: {metrics['attempt']}
            - Next Attempt Should Be: {metrics['next_attempt']}
            - Duration: {metrics['duration_seconds']:.2f} seconds
            """)
            
            return metrics
            
        except Exception as e:
            logging.warning(f"Failed to read metrics from attempt {attempt}: {str(e)}")
            continue
    
    # If we get here, we couldn't read any log files
    statsd_client.incr('join.error')
    raise FileNotFoundError(f"Could not find any valid log files in attempts 1-2 at base path: {base_path}") 