#!/bin/bash

# =============================================================================
# start_dag.sh
# -----------------------------------------------------------------------------
# Airflow DAG initialization script for the Reddit AI Pulse Cloud project.
# This script starts the Airflow services and triggers the main pipeline DAG.
#
# The script performs the following operations:
# 1. Ensures execution as airflow user
# 2. Starts Docker Compose services
# 3. Waits for containers to be healthy
# 4. Unpauses and triggers the reddit_pipeline DAG
# 5. Monitors initial DAG and task status
#
# The script includes error handling and provides
# helpful commands for monitoring DAG progress.
#
# Usage:
#   ./start_dag.sh
#
# Requirements:
#   - Must be run as airflow user
#   - Docker and Docker Compose installed
#   - .env file with Airflow configuration
#   - Reddit pipeline DAG deployed
# =============================================================================

# Enable error handling
set -e
set -o pipefail

# Ensure script runs as airflow user
if [ "$(whoami)" != "airflow" ]; then
    echo "This script must be run as airflow user"
    echo "Current user: $(whoami)"
    echo "Switching to airflow user..."
    exec sudo -u airflow "$0" "$@"
fi

# Source environment variables
source /opt/airflow/.env

# Change to the docker directory
cd /opt/airflow/${GH_REPO}/Cloud/docker

# Start Docker Compose with environment file
docker compose --env-file ../.env up -d

echo "Waiting for containers to be healthy..."
sleep 180  # Wait for 3 minutes

# Trigger the DAG
echo "Triggering reddit_pipeline_dag..."
docker compose --env-file ../.env exec airflow-webserver airflow dags unpause reddit_pipeline
docker compose --env-file ../.env exec airflow-webserver airflow dags trigger reddit_pipeline

# Monitor DAG status
echo "Checking DAG status..."
docker compose --env-file ../.env exec airflow-webserver airflow dags list-runs -d reddit_pipeline

# Show task status
echo "Checking task status..."
docker compose --env-file ../.env exec airflow-webserver airflow tasks list reddit_pipeline --tree

echo "Airflow DAG started successfully"

# Note: You can monitor the DAG progress using:
echo "To monitor progress, use these commands:"
echo "- List runs: docker compose --env-file ../.env exec airflow-webserver airflow dags list-runs -d reddit_pipeline"
echo "- Show tasks: docker compose --env-file ../.env exec airflow-webserver airflow tasks list reddit_pipeline --tree"
echo "- View logs: docker compose --env-file ../.env exec airflow-webserver airflow tasks logs reddit_pipeline TASK_ID RUN_ID" 