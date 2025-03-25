#!/bin/bash

# =============================================================================
# startup.sh
# -----------------------------------------------------------------------------
# VM initialization script for the Reddit AI Pulse Cloud project.
# This script sets up the complete Airflow environment on a fresh VM instance.
#
# The script performs the following operations:
# 1. Installs system dependencies (Docker, Python, Git)
# 2. Creates and configures airflow user
# 3. Sets up directory structure with proper permissions
# 4. Fetches secrets from Google Cloud Storage
# 5. Clones project repository
# 6. Configures Docker environment
# 7. Initializes Airflow services
#
# The script includes comprehensive error handling, logging,
# and security configurations for production deployment.
#
# Usage:
#   Automatically executed on VM startup via metadata
#
# Requirements:
#   - GCP VM instance
#   - GCS bucket with secrets
#   - GitHub repository access
#   - Proper IAM permissions
# =============================================================================

# Enable error handling
set -e
set -o pipefail

# Enable logging
exec 1> >(logger -s -t $(basename $0)) 2>&1

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log_message "Starting custom startup script..."

# Update package list and install dependencies
log_message "Installing dependencies..."
apt-get update
apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    python3 \
    python3-venv \
    python3-pip

# Add Docker's official GPG key and repository
echo "Setting up Docker repository..."
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker packages
echo "Installing Docker..."
apt-get update
apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

# Create airflow user and set up Docker permissions
echo "Setting up airflow user and Docker permissions..."
useradd -m -s /bin/bash airflow || true
usermod -aG docker airflow

# Add system user to Docker group
echo "Adding system user to Docker group..."
usermod -aG docker $SUDO_USER || true
systemctl restart docker

# Create all required directories with proper ownership
echo "Creating required directories..."
mkdir -p /opt/airflow/{logs,tmp,airflow_project/{logs,dags,plugins},credentials} \
         /opt/airflow/logs/{scheduler,webserver,worker,dag_processor,dag_id=reddit_pipeline} \
         /opt/airflow/airflow_project/logs/{scheduler,webserver,worker,dag_processor,dag_id=reddit_pipeline} \
         /opt/airflow/results

# Get airflow user ID
AIRFLOW_UID=$(id -u airflow)

# Set base directory permissions
chown -R ${AIRFLOW_UID}:0 /opt/airflow
chmod -R 775 /opt/airflow

# Set directory permissions (777 for logs and results to ensure write access)
find /opt/airflow/logs -type d -exec chmod 777 {} \;
find /opt/airflow/airflow_project/logs -type d -exec chmod 777 {} \;
chmod 777 /opt/airflow/results

# Get bucket name from metadata
BUCKET_NAME=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/bucket-name")
if [ -z "$BUCKET_NAME" ]; then
    log_message "Error: Failed to get bucket name from metadata"
    exit 1
fi

# Fetch secrets from GCS with retries
log_message "Fetching secrets from GCS..."
log_message "Using bucket: ${BUCKET_NAME}"

# Try to download secrets with retries
MAX_RETRIES=10
RETRY_COUNT=0
SECRET_DOWNLOADED=false

while [ $RETRY_COUNT -lt $MAX_RETRIES ] && [ "$SECRET_DOWNLOADED" = false ]; do
  if gsutil cp gs://${BUCKET_NAME}/secrets/.env /opt/airflow/.env && \
     gsutil cp gs://${BUCKET_NAME}/secrets/service-account.json /opt/airflow/credentials/service-account.json; then
    SECRET_DOWNLOADED=true
    log_message "Successfully downloaded secrets on attempt $((RETRY_COUNT+1))"
  else
    RETRY_COUNT=$((RETRY_COUNT+1))
    log_message "Failed to download secrets (attempt $RETRY_COUNT/$MAX_RETRIES), retrying in 10 seconds..."
    sleep 60
  fi
done

if [ "$SECRET_DOWNLOADED" = false ]; then
  log_message "Error: Failed to download secrets after $MAX_RETRIES attempts"
  exit 1
fi

# Set proper permissions for secrets
chown ${AIRFLOW_UID}:0 /opt/airflow/.env /opt/airflow/credentials/service-account.json
chmod 600 /opt/airflow/.env /opt/airflow/credentials/service-account.json
chmod 700 /opt/airflow/credentials

# Source environment variables
source /opt/airflow/.env

# Clone repository as airflow user
echo "Cloning repository..."
cd /opt/airflow
sudo -u airflow git clone "https://oauth2:${GH_PAT}@github.com/${GH_OWNER}/${GH_REPO}.git"
if [ ! -d "${GH_REPO}" ]; then
    echo "Failed to clone repository"
    exit 1
fi

# Copy .env file to the repository
cp /opt/airflow/.env /opt/airflow/${GH_REPO}/Cloud/

# Set repository permissions
echo "Setting repository permissions..."
chown -R ${AIRFLOW_UID}:0 /opt/airflow/${GH_REPO}
find /opt/airflow/${GH_REPO} -type d -exec chmod 775 {} \;
find /opt/airflow/${GH_REPO} -type f -exec chmod 664 {} \;

# Create and set permissions for both results directories
echo "Setting up results directories..."
mkdir -p /opt/airflow/results
mkdir -p /opt/airflow/${GH_REPO}/Cloud/results

# Set ownership and permissions for results directories
chown -R ${AIRFLOW_UID}:0 /opt/airflow/results /opt/airflow/${GH_REPO}/Cloud/results
chmod -R 777 /opt/airflow/results /opt/airflow/${GH_REPO}/Cloud/results

# Set up credentials directories and permissions
log_message "Setting up credentials directories and permissions..."
mkdir -p /opt/airflow/credentials
mkdir -p /opt/airflow/${GH_REPO}/Cloud/credentials

# Set base permissions for credentials directories
chown -R ${AIRFLOW_UID}:0 /opt/airflow/credentials
chown -R ${AIRFLOW_UID}:0 /opt/airflow/${GH_REPO}/Cloud/credentials
chmod 755 /opt/airflow/credentials
chmod 755 /opt/airflow/${GH_REPO}/Cloud/credentials

# Copy and set permissions for service account file
log_message "Setting up service account credentials..."
cp /opt/airflow/credentials/service-account.json /opt/airflow/${GH_REPO}/Cloud/credentials/
chown ${AIRFLOW_UID}:0 /opt/airflow/credentials/service-account.json
chown ${AIRFLOW_UID}:0 /opt/airflow/${GH_REPO}/Cloud/credentials/service-account.json
chmod 644 /opt/airflow/credentials/service-account.json
chmod 644 /opt/airflow/${GH_REPO}/Cloud/credentials/service-account.json

# Make scripts executable
echo "Setting up scripts..."
chmod 775 /opt/airflow/${GH_REPO}/Cloud/docker/build.sh
chmod 775 /opt/airflow/${GH_REPO}/Cloud/infrastructure/terraform/vm_scripts/start_dag.sh

# Run build script as airflow user
echo "Running build script..."
cd /opt/airflow/${GH_REPO}/Cloud/docker
sudo -u airflow bash -c './build.sh'

echo "Startup script completed successfully" 