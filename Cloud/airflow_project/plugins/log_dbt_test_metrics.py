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

def extract_dbt_test_metrics(log_path):
    """Extract metrics from DBT test task logs"""
    # Get the base path without attempt number
    base_path = re.sub(r'/attempt=\d+\.log$', '', log_path)
    logging.info(f"Base log path: {base_path}")
    
    # Extract task name from path
    task_match = re.search(r'/task_id=([^/]+)/', log_path)
    task_name = task_match.group(1) if task_match else None
    if not task_name:
        error_msg = f"Could not extract task name from log path: {log_path}"
        logging.error(error_msg)
        raise ValueError(error_msg)
    logging.info(f"Extracted task name: {task_name}")
    
    # Try attempts in descending order starting from 2
    for attempt in range(2, 0, -1):
        try_path = f"{base_path}/attempt={attempt}.log"
        logging.info(f"Trying log path: {try_path}")
        
        if not os.path.exists(try_path):
            logging.warning(f"Log file not found at: {try_path}")
            continue
            
        try:
            metrics = {
                'tests_passed': 0,
                'tests_failed': 0,
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
                
                # Look for start time
                if "Running with dbt" in line and timestamp_match:
                    try:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        start_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                    logging.info(f"Found start time: {start_time}")
                
                # Count test results - look for the specific dbt output format
                elif "PASS" in line and "of" in line and "[RUN]" not in line:
                    metrics['tests_passed'] += 1
                    logging.info(f"Found passed test: {line.strip()}")
                elif "FAIL" in line and "of" in line and "[RUN]" not in line:
                    metrics['tests_failed'] += 1
                    logging.info(f"Found failed test: {line.strip()}")
                
                # Look for completion and final test counts
                elif "Done. PASS=" in line:
                    # Extract final counts from summary line
                    summary_match = re.search(r"PASS=(\d+) WARN=(\d+) ERROR=(\d+)", line)
                    if summary_match:
                        metrics['tests_passed'] = int(summary_match.group(1))
                        metrics['tests_failed'] = int(summary_match.group(2)) + int(summary_match.group(3))
                        logging.info(f"Found final test counts - Passed: {metrics['tests_passed']}, Failed: {metrics['tests_failed']}")
                
                # Get end time from last timestamp
                if timestamp_match:
                    try:
                        current_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%d, %H:%M:%S UTC")
                    except ValueError:
                        current_time = datetime.strptime(timestamp_match.group(1).strip(), "%Y-%m-%dT%H:%M:%S.%f%z")
                    end_time = current_time
            
            # Calculate duration if we have both timestamps
            if start_time and end_time:
                metrics['duration_seconds'] = (end_time - start_time).total_seconds()
                statsd_client.timing('dbt_test.duration', metrics['duration_seconds'] * 1000)
                logging.info(f"Calculated duration: {metrics['duration_seconds']} seconds")
            
            # Success is when all tests pass
            success = metrics['tests_failed'] == 0 and metrics['tests_passed'] > 0
            metrics['next_attempt'] = 1 if success else metrics['attempt'] + 1
            
            # Send metrics to StatsD
            statsd_client.gauge(f'dbt_test.{task_name}.tests_passed', metrics['tests_passed'])
            statsd_client.gauge(f'dbt_test.{task_name}.tests_failed', metrics['tests_failed'])
            statsd_client.gauge(f'dbt_test.{task_name}.current_attempt', metrics['attempt'])
            
            if success:
                statsd_client.incr(f'dbt_test.{task_name}.success')
            else:
                statsd_client.incr(f'dbt_test.{task_name}.retry')
            
            logging.info(f"""
            DBT Test Task Metrics Summary for {task_name}:
            - Tests Passed: {metrics['tests_passed']}
            - Tests Failed: {metrics['tests_failed']}
            - Current Attempt: {metrics['attempt']}
            - Next Attempt Should Be: {metrics['next_attempt']}
            - Duration: {metrics['duration_seconds']:.2f} seconds
            """)
            
            return metrics
            
        except Exception as e:
            logging.warning(f"Failed to read metrics from attempt {attempt}: {str(e)}")
            continue
    
    # If we get here, we couldn't read any log files
    statsd_client.incr(f'dbt_test.{task_name}.error')
    error_msg = f"Could not find any valid log files in attempts 1-2 at base path: {base_path}"
    logging.error(error_msg)
    raise FileNotFoundError(error_msg) 