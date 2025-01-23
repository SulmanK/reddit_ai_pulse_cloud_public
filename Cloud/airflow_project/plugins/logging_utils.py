"""
Shared utility functions for Airflow plugins.

This module contains common functionality used across different plugin modules.
"""

import logging
import os
from datetime import datetime

def get_log_path(task_instance, task_id):
    """
    Construct the log file path from task instance.
    
    Args:
        task_instance: The Airflow task instance object
        task_id: The task identifier
        
    Returns:
        str: The complete log file path
    """
    dag_id = task_instance.dag_id
    # Get the actual run date from the logical date
    run_date = task_instance.get_dagrun().execution_date
    
    # Determine if this is a manual or scheduled run
    run_type = task_instance.get_dagrun().run_type
    log_prefix = 'manual' if run_type == 'manual' else 'scheduled'
    
    # Format the execution date based on run type
    if run_type == 'scheduled':
        # Format for scheduled runs: 2025-01-08T00:35:00+00:00
        execution_date = run_date.strftime('%Y-%m-%dT%H:%M:%S+00:00')
    else:
        # Format for manual runs: keep microseconds
        execution_date = run_date.strftime('%Y-%m-%dT%H:%M:%S.%f') + '+00:00'
    
    attempt = task_instance.try_number
    
    # Get unique run identifier
    run_id = task_instance.get_dagrun().run_id
    
    # Add debug logging
    logging.info(f"Constructing log path with run_type: {run_type}")
    logging.info(f"Log prefix: {log_prefix}")
    logging.info(f"Execution date: {execution_date}")
    logging.info(f"Run ID: {run_id}")
    
    # Construct the log path to match Airflow's structure
    log_path = f"/opt/airflow/airflow_project/logs/dag_id={dag_id}/run_id={run_id}/task_id={task_id}/attempt={attempt}.log"
    logging.info(f"Constructed log path: {log_path}")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    return log_path 