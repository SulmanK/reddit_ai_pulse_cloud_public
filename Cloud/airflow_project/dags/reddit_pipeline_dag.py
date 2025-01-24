"""
Reddit Text Insight & Sentiment Pipeline DAG (Cloud Version)

This DAG orchestrates the collection, processing, and analysis of Reddit data through several stages:
1. Data ingestion from Reddit API and preprocessing
2. Initial data staging with dbt
3. Text summarization using BART model
4. Sentiment analysis using multiple models
5. Final data transformation and joining
6. LLM analysis using Gemini
7. VM shutdown upon completion

Note: The final 'shutdown_vm' task may appear as "failed" in the Airflow UI. This is expected behavior
because the task shuts down the VM (and thus Airflow itself) before it can report its completion status.
A task showing as "failed" in this specific case actually indicates that the VM shutdown was successful.

Schedule: Daily at 4:00 PM EST (21:00 UTC)
Owner: Sulman Khan
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.stats import Stats
from datetime import datetime, timedelta
import os
import time
import requests
import json

import statsd
import re
import logging
from airflow.stats import Stats
from contextlib import contextmanager


# Import plugins with correct paths
from airflow_project.plugins.logging_utils import get_log_path
from airflow_project.plugins.log_ingest_preprocess_metrics import extract_metrics_from_log
from airflow_project.plugins.log_dbt_test_metrics import extract_dbt_test_metrics
from airflow_project.plugins.log_summarize_metrics import extract_summarize_metrics
from airflow_project.plugins.log_sentiment_analysis_metrics import extract_sentiment_metrics
from airflow_project.plugins.log_join_metrics import extract_join_metrics
from airflow_project.plugins.log_update_processing_status_metrics import extract_update_status_metrics
from airflow_project.plugins.log_gemini_metrics import extract_gemini_metrics
from airflow_project.plugins.push_to_github import push_gemini_results

# Set environment variables for project paths
os.environ['PROJECT_ROOT'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
os.environ['DBT_PROJECT_DIR'] = '/opt/airflow/dbt_reddit_summary_cloud'

# Import process connectors
from scripts.ingest_preprocess_connector import ingest_preprocess_process
from scripts.summarize_connector import summarize_process
from scripts.sentiment_connector import sentiment_analysis_process
from scripts.gemini_connector import gemini_analysis_process

# Initialize StatsD client
statsd_client = statsd.StatsClient(
    host='statsd-exporter',
    port=9125,
    prefix='airflow.reddit'
)

@contextmanager
def track_time():
    """Context manager to track execution time"""
    start_time = time.time()
    yield
    duration = (time.time() - start_time) * 1000  # Convert to milliseconds
    Stats.timing('reddit.ingest.duration', duration)

def parse_ingest_metrics(**context):
    """Parse metrics from ingest task logs"""
    task_instance = context['task_instance']
    log_path = get_log_path(task_instance, task_id='ingest_and_preprocess')
    logging.info(f"Generated log path for metrics parsing: {log_path}")
    return extract_metrics_from_log(log_path)

def parse_dbt_metrics(task_id):
    """Create a function to parse metrics for any DBT task"""
    def _parse_metrics(**context):
        log_path = get_log_path(context['task_instance'], task_id=task_id)
        return extract_dbt_test_metrics(log_path)
    return _parse_metrics

def parse_summarize_metrics(**context):
    """Parse metrics from summarize task logs"""
    log_path = get_log_path(context['task_instance'], task_id='run_summarize')
    return extract_summarize_metrics(log_path)

def parse_sentiment_metrics(**context):
    """Parse metrics from sentiment analysis task logs"""
    log_path = get_log_path(context['task_instance'], task_id='run_sentiment_analysis')
    return extract_sentiment_metrics(log_path)

def parse_join_metrics(**context):
    """Parse metrics from join operation by querying the database and logs"""
    log_path = get_log_path(context['task_instance'], task_id='run_dbt_join_summary_analysis')
    return extract_join_metrics(log_path)

DBT_TEST_CMD = 'cd /opt/airflow/dbt_reddit_summary_cloud && dbt deps && dbt test --select {selector}'

def trigger_vm_shutdown(**context):
    """
    Trigger the Cloud Function to stop the VM.
    This will be called after DAG completion or failure.
    Returns True to mark task as successful even though VM shutdown will prevent status update.
    """
    function_url = os.environ.get('STOP_VM_FUNCTION_URL')
    if not function_url:
        raise ValueError("STOP_VM_FUNCTION_URL environment variable not set")

    payload = {
        'trigger_source': 'dag'
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(function_url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to trigger VM shutdown: Status {response.status_code}, Response: {response.text}")
    
    # Mark as successful before VM shuts down
    context['task_instance'].xcom_push(key='shutdown_initiated', value=True)
    return True

# Define the DAG
with DAG(
    'reddit_pipeline',
    default_args={
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    },
    #description='Reddit data pipeline - Cloud Version',
    #schedule_interval='0 22 * * *',  # Run at 22:00 UTC (5:00 PM EST)
    description='Reddit data pipeline - Cloud Version (Manual Trigger Only)',
    schedule_interval=None,  # Set to None for manual triggers only
    start_date=datetime(2024, 1, 1),
    catchup=False,
    max_active_runs=1
) as dag:

    # 1st Stage: Ingest and Preprocess
    ingest_task = PythonOperator(
        task_id='ingest_and_preprocess',
        python_callable=ingest_preprocess_process,
        provide_context=True
    )
    
    # 2nd Stage: Ingest Metrics
    ingest_metrics_task = PythonOperator(
        task_id='parse_ingest_metrics',
        python_callable=parse_ingest_metrics,
        provide_context=True
    )

    # 3rd Stage: DBT Test Raw Sources
    dbt_test_raw_sources = BashOperator(
        task_id='test_raw_sources',
        bash_command=DBT_TEST_CMD.format(selector='source:raw_data source:processed_data'),
        dag=dag
    )

    # 4th Stage: DBT Test Raw Metrics
    dbt_test_raw_metrics_task = PythonOperator(
        task_id='parse_dbt_test_raw_metrics',
        python_callable=parse_dbt_metrics('test_raw_sources'),
        provide_context=True
    )

    # 5th Stage: Run DBT Staging Models
    dbt_staging_task = BashOperator(
        task_id='run_dbt_staging',
        bash_command='cd /opt/airflow/dbt_reddit_summary_cloud && dbt run --select current_summary_staging',
        dag=dag
    )

    # 6th Stage: Test Staging Models
    dbt_test_staging_models = BashOperator(
        task_id='test_staging_models',
        bash_command=DBT_TEST_CMD.format(
            selector='source:summary_analytics.daily_summary_data source:summary_analytics.current_summary_staging'
        ),
        dag=dag
    )

    # 7th Stage: DBT Test Staging Metrics
    dbt_test_staging_metrics_task = PythonOperator(
        task_id='parse_dbt_test_staging_metrics',
        python_callable=parse_dbt_metrics('test_staging_models'),
        provide_context=True
    )

    # 8th Stage: Generate Text Summaries
    summarize_task = PythonOperator(
        task_id='run_summarize',
        python_callable=summarize_process,
        provide_context=True
    )

    # 9th Stage: Summarize Metrics
    summarize_metrics_task = PythonOperator(
        task_id='parse_summarize_metrics',
        python_callable=parse_summarize_metrics,
        provide_context=True
    )

    # 10th Stage: Test Summarize Models
    dbt_test_summarize_models = BashOperator(
        task_id='test_summarize_models',
        bash_command=DBT_TEST_CMD.format(selector='source:summary_analytics.text_summary_results'),
        dag=dag
    )

    # 11th Stage: Test Summarize Metrics
    dbt_test_summarize_metrics_task = PythonOperator(
        task_id='parse_dbt_test_summarize_metrics',
        python_callable=parse_dbt_metrics('test_summarize_models'),
        provide_context=True
    )

    # 12th Stage: Sentiment Analysis
    sentiment_task = PythonOperator(
        task_id='run_sentiment_analysis',
        python_callable=sentiment_analysis_process,
        provide_context=True
    )

    # 13th Stage: Sentiment metrics
    sentiment_metrics_task = PythonOperator(
        task_id='parse_sentiment_metrics',
        python_callable=parse_sentiment_metrics,
        provide_context=True
    )

    # 14th Stage: Test Sentiment Analysis Models
    dbt_test_sentiment_analysis = BashOperator(
        task_id='test_sentiment_analysis',
        bash_command=DBT_TEST_CMD.format(selector='source:summary_analytics.sentiment_analysis_results'),
        dag=dag
    )

    # 15th Stage: Test Sentiment Analysis Metrics
    dbt_test_sentiment_metrics_task = PythonOperator(
        task_id='parse_dbt_test_sentiment_metrics',
        python_callable=parse_dbt_metrics('test_sentiment_analysis'),
        provide_context=True
    )   

    # 16th Stage: Join Summarized and Sentiment Data
    dbt_join_summary_analysis_task = BashOperator(
        task_id='run_dbt_join_summary_analysis',
        bash_command='cd /opt/airflow/dbt_reddit_summary_cloud && dbt run --select +joined_summary_analysis',
        dag=dag
    )
    
    # 17th Stage: Join Metrics
    join_metrics_task = PythonOperator(
        task_id='parse_join_metrics',
        python_callable=parse_join_metrics,
        provide_context=True
    )

    # 18th Stage: Test Joined Summary Analysis
    dbt_test_joined_summary_analysis_task = BashOperator(
        task_id='test_joined_summary_analysis',
        bash_command=DBT_TEST_CMD.format(selector='joined_summary_analysis'),
        dag=dag
    )

    # 19th Stage: Test Joined Summary Analysis Metrics
    dbt_test_joined_summary_analysis_metrics_task = PythonOperator(
        task_id='parse_dbt_test_joined_summary_analysis_metrics',
        python_callable=parse_dbt_metrics('test_joined_summary_analysis'),
        provide_context=True
    )

    # 20th Stage: Update Processing Status
    task_update_status = BashOperator(
        task_id='update_processing_status',
        bash_command='cd /opt/airflow/dbt_reddit_summary_cloud && dbt run --select update_processing_status',
        dag=dag
    )

    # 21th Stage: Update Processing Status Metrics
    test_processing_status_metrics = PythonOperator(
        task_id='test_processing_status_metrics',
        python_callable=lambda ti: extract_update_status_metrics(
            get_log_path(ti, 'update_processing_status')
        ),
        dag=dag
    )

    # 22th Stage: dbt test update processing status
    dbt_test_update_processing_status = BashOperator(
        task_id='test_update_processing_status',
        bash_command=DBT_TEST_CMD.format(selector='update_processing_status'),
        dag=dag
    )

    # 23th Stage: Test Update Processing Status Metrics
    dbt_test_update_processing_status_metrics = PythonOperator(
        task_id='parse_dbt_test_update_processing_status_metrics',
        python_callable=parse_dbt_metrics('test_update_processing_status'),
        provide_context=True
    )

    # 24th Stage: Gemini Analyzer
    gemini_task = PythonOperator(
        task_id='run_gemini',
        python_callable=gemini_analysis_process,
        dag=dag
    )

    # 25th Stage; Log Gemini Metrics
    test_gemini_metrics = PythonOperator(
        task_id='test_gemini_metrics',
        python_callable=lambda ti: extract_gemini_metrics(
            get_log_path(ti, 'run_gemini')
        ),
        dag=dag
    )
    
    # 26th Stage: Push Gemini Results to GitHub
    push_gemini_results_task = PythonOperator(
        task_id='push_gemini_results',
        python_callable=push_gemini_results,
        provide_context=True,
        email_on_failure=True,
        email_on_retry=True
    )

    # 27th Stage: Shutdown VM using Cloud Run
    shutdown_vm = PythonOperator(
        task_id='shutdown_vm',
        python_callable=trigger_vm_shutdown,
        provide_context=True,
        trigger_rule='all_done',  # Run even if upstream tasks fail
        retries=0,  # Don't retry on failure since VM will be shutting down
        dag=dag,
        email_on_failure=True,

        
        doc="""
        Shuts down the VM using Cloud Run.
        Note: This task will appear as "failed" in the UI because the VM
        shutdown occurs before Airflow can mark the task as complete.
        This is expected behavior and indicates a successful shutdown.
        """
    )
    
    # Define task dependencies
    ingest_task >> ingest_metrics_task >> \
    dbt_test_raw_sources >> dbt_test_raw_metrics_task >> \
    dbt_staging_task >> dbt_test_staging_models >> dbt_test_staging_metrics_task >> \
    summarize_task >> summarize_metrics_task >> dbt_test_summarize_models >> dbt_test_summarize_metrics_task  >> \
    sentiment_task >> sentiment_metrics_task >> dbt_test_sentiment_analysis >> dbt_test_sentiment_metrics_task >> \
    dbt_join_summary_analysis_task >> join_metrics_task >> dbt_test_joined_summary_analysis_task >> dbt_test_joined_summary_analysis_metrics_task >> \
    task_update_status >> test_processing_status_metrics >> dbt_test_update_processing_status >> dbt_test_update_processing_status_metrics >> \
    gemini_task >> test_gemini_metrics >> \
    push_gemini_results_task >> shutdown_vm 