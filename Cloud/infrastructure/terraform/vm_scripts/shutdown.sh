#!/bin/bash

# =============================================================================
# shutdown.sh
# -----------------------------------------------------------------------------
# VM shutdown script for the Reddit AI Pulse Cloud project.
# This script performs a graceful shutdown of Airflow services and data backup.
#
# The script performs the following operations:
# 1. Ensures execution as airflow user
# 2. Sources environment configuration
# 3. Gracefully stops Airflow containers
# 4. Creates timestamped backup of Airflow logs
# 5. Syncs logs to Google Cloud Storage
# 6. Cleans up old logs based on retention policy
#
# The script includes error handling and logging to ensure
# data is properly preserved before VM shutdown.
#
# Usage:
#   ./shutdown.sh
#
# Requirements:
#   - Must be run as airflow user
#   - Docker and Docker Compose installed
#   - GCS bucket configured in environment
#   - gsutil authenticated and configured
# =============================================================================

# Enable error handling
set -e
set -o pipefail

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Ensure script runs as airflow user
if [ "$(whoami)" != "airflow" ]; then
    log_message "This script must be run as airflow user"
    log_message "Current user: $(whoami)"
    log_message "Switching to airflow user..."
    exec sudo -u airflow "$0" "$@"
fi

# Enable logging
exec 1> >(logger -s -t $(basename $0)) 2>&1

# Source environment variables
log_message "Sourcing environment variables..."
if [ -f "/opt/airflow/${GH_REPO}/Cloud/.env" ]; then
    source "/opt/airflow/${GH_REPO}/Cloud/.env"
elif [ -f "/opt/airflow/.env" ]; then
    source "/opt/airflow/.env"
else
    log_message "ERROR: Could not find .env file"
    exit 1
fi

# Change to the docker directory
cd /opt/airflow/${GH_REPO}/Cloud/docker

# Gracefully stop Airflow containers
log_message "Stopping Airflow containers..."
docker compose --env-file ../.env down 

# Create timestamp for log directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure GCS_BUCKET_NAME is set
if [ -z "${GCS_BUCKET_NAME}" ]; then
    log_message "Error: GCS_BUCKET_NAME environment variable is not set"
    exit 1
fi

# Simple log sync - just sync the entire logs directory
log_message "Syncing Airflow logs to GCS bucket..."

# Use the correct logs directory
LOG_DIR="/opt/airflow/${GH_REPO}/Cloud/airflow_project/logs"

log_message "Using logs directory: ${LOG_DIR}"
if [ -d "$LOG_DIR" ]; then
    log_message "Found logs directory. Contents:"
    find "$LOG_DIR" -type f -ls
    
    log_message "Running sync command to GCS..."
    if gsutil -m rsync -r -d "$LOG_DIR" "gs://${GCS_BUCKET_NAME}/airflow_logs/${TIMESTAMP}"; then
        log_message "Successfully synced logs to gs://${GCS_BUCKET_NAME}/airflow_logs/${TIMESTAMP}"
        
        # Verify the upload
        log_message "Verifying uploaded contents:"
        gsutil ls -r "gs://${GCS_BUCKET_NAME}/airflow_logs/${TIMESTAMP}/**" || log_message "No files found in GCS"
    else
        log_message "Warning: Failed to sync logs to GCS"
    fi
else
    log_message "ERROR: Logs directory not found at ${LOG_DIR}"
    log_message "Current directory structure:"
    ls -R /opt/airflow/${GH_REPO}/Cloud/airflow_project/
fi

# Clean up old logs from GCS (keep last 30 days)
log_message "Cleaning up old logs from GCS..."
CUTOFF_DATE=$(date -d "-30 days" +%Y%m%d)
if gsutil ls "gs://${GCS_BUCKET_NAME}/airflow_logs/" &>/dev/null; then
    gsutil ls "gs://${GCS_BUCKET_NAME}/airflow_logs/" | while read -r log_dir; do
        dir_date=$(basename "$log_dir" | cut -d'_' -f1)
        if [[ "$dir_date" < "$CUTOFF_DATE" ]]; then
            log_message "Removing old logs: $log_dir"
            gsutil -m rm -r "$log_dir"
        fi
    done
fi

# Clean up local logs older than 7 days
log_message "Cleaning up local logs older than 7 days..."
find "${LOG_DIR}" -type f -mtime +7 -delete 2>/dev/null || true

log_message "Shutdown completed successfully" 