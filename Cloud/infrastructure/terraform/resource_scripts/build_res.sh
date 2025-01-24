#!/bin/bash

# =============================================================================
# build_res.sh
# -----------------------------------------------------------------------------
# Main deployment script for the Reddit AI Pulse Cloud infrastructure.
# This script sets up and configures all necessary GCP resources for the project.
#
# The script performs the following operations:
# 1. Loads environment configuration
# 2. Generates terraform.tfvars from environment variables
# 3. Sets up Docker and Artifact Registry
# 4. Builds and pushes Cloud Run images
# 5. Initializes and applies Terraform configuration
# 6. Updates Cloud Run URLs in .env file
# 7. Manages service account credentials
# 8. Uploads secrets to GitHub
# 9. Configures Git repository settings
#
# The script includes error handling, logging, and automatic backup
# of sensitive files. It can optionally commit changes to Git.
#
# Usage:
#   ./build_res.sh
#
# Requirements:
#   - .env file with required configuration
#   - Authenticated gcloud CLI
#   - Docker installed and configured
#   - GitHub CLI installed and authenticated
#   - Terraform installed
# =============================================================================

# Store the base directory path (from resource_scripts)
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Loading project configuration..."
source ../../../.env

# Generate terraform.tfvars from environment variables
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Generating terraform.tfvars from environment variables..."

# Generate terraform.tfvars with environment variables
cat > ../terraform.tfvars << EOL
project      = "${GCP_PROJECT_ID}"
region       = "${GCP_REGION}"
zone         = "${GCP_ZONE}"
alert_email_address = "${ALERT_EMAIL}"
vm_instance_name = "${VM_INSTANCE_NAME}"
vm_machine_type = "${VM_MACHINE_TYPE}"
machine_type = "${VM_MACHINE_TYPE}"
bucket_name  = "${GCS_BUCKET_NAME}"
dataset_raw = "${BIGQUERY_DATASET_RAW}"
dataset_processed = "${BIGQUERY_DATASET_PROCESSED}"
gh_pat = "${GH_PAT}"
gh_owner = "${GH_OWNER}"
gh_repo = "${GH_REPO}"
network_name = "${NETWORK_NAME}"
subnet_name = "${SUBNET_NAME}"
subnet_cidr = "${SUBNET_CIDR}"
service_account_email = "${SA_EMAIL}"
EOL

# Set gcloud project and configure docker
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Setting gcloud project and configuring Docker..."
gcloud config set project "$GCP_PROJECT_ID"

# Configure Docker auth using gcloud credentials
echo "[$TIMESTAMP] Setting up Docker authentication..."
gcloud auth configure-docker us-central1-docker.pkg.dev --quiet

# Create Artifact Registry repository if it doesn't exist
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Creating Artifact Registry repository..."
gcloud artifacts repositories create cloud-run-source-deploy \
    --repository-format=docker \
    --location="$GCP_REGION" \
    --description="Docker repository for Cloud Run images" \
    2>/dev/null || true

# Build and push Cloud Run images
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Building and pushing Cloud Run images..."
cd ../core/cloud_run

# Build and push start-vm image
echo "[$TIMESTAMP] Building start-vm image (this may take 1-2 minutes)..."
docker build -t "us-central1-docker.pkg.dev/$GCP_PROJECT_ID/cloud-run-source-deploy/start-vm:latest" --build-arg FUNCTION_TARGET=start_vm .
echo "[$TIMESTAMP] Pushing start-vm image to Artifact Registry (this may take 30-60 seconds)..."
docker push "us-central1-docker.pkg.dev/$GCP_PROJECT_ID/cloud-run-source-deploy/start-vm:latest"
echo "[$TIMESTAMP] ✓ Completed start-vm image build and push"

# Build and push stop-vm image
echo "[$TIMESTAMP] Building stop-vm image (this may take 1-2 minutes)..."
docker build -t "us-central1-docker.pkg.dev/$GCP_PROJECT_ID/cloud-run-source-deploy/stop-vm:latest" --build-arg FUNCTION_TARGET=stop_vm .
echo "[$TIMESTAMP] Pushing stop-vm image to Artifact Registry (this may take 30-60 seconds)..."
docker push "us-central1-docker.pkg.dev/$GCP_PROJECT_ID/cloud-run-source-deploy/stop-vm:latest"
echo "[$TIMESTAMP] ✓ Completed stop-vm image build and push"

# Return to terraform directory for Terraform operations
cd ../..

# Initialize Terraform
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Initializing Terraform..."
terraform init

# Validate configuration
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Validating Terraform configuration..."
terraform validate

# Plan changes
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Planning Terraform changes..."
terraform plan -out=tfplan

# Apply changes
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Applying Terraform changes..."
terraform apply tfplan

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Function to send credentials to website repository
send_credentials_to_website() {
    local credentials_file="$1"

    if [ ! -f "$credentials_file" ]; then
        log_message "Error: Credentials file not found at $credentials_file"
        return 1
    fi

    log_message "Sending credentials to $GH_WEBSITE_REPO repository..."

    # Create a temporary file for the payload
    local temp_payload=$(mktemp)

    # Create the full payload JSON using jq to ensure proper formatting
    jq -n \
        --arg event "update_credentials" \
        --argjson creds "$(cat $credentials_file)" \
        '{
            event_type: $event,
            client_payload: {
                credentials: $creds
            }
        }' > "$temp_payload"

    # Debug: Show payload structure (hide sensitive data)
    log_message "Debug: Sending payload with formatted credentials"

    # Trigger the workflow using the temp file
    curl -X POST \
        -H "Accept: application/vnd.github.v3+json" \
        -H "Authorization: token $GH_PAT" \
        -H "Content-Type: application/json" \
        "https://api.github.com/repos/$GH_OWNER/$GH_WEBSITE_REPO/dispatches" \
        --data @"$temp_payload"

    # Store the curl result
    local result=$?

    # Clean up temp file
    rm -f "$temp_payload"

    if [ $result -eq 0 ]; then
        log_message "Successfully triggered credentials update workflow"
    else
        log_message "Failed to trigger credentials update workflow"
        return 1
    fi
}

# Get URLs from Terraform output and gcloud
get_cloud_run_urls() {
    # Try to refresh Terraform state first
    terraform refresh >/dev/null 2>&1 || true
    
    # Try to get URLs from Terraform outputs
    STOP_VM_URL=$(terraform output -raw stop_vm_url 2>/dev/null) || true
    START_VM_URL=$(terraform output -raw start_vm_url 2>/dev/null) || true
    
    # If either URL is empty, fall back to gcloud
    if [ -z "$STOP_VM_URL" ] || [ -z "$START_VM_URL" ]; then
        echo "[$TIMESTAMP] Terraform outputs not available, falling back to gcloud..."
        
        # Get URLs directly from gcloud
        STOP_VM_URL=$(gcloud run services describe stop-vm --region="$GCP_REGION" --format="get(status.url)" 2>/dev/null) || true
        START_VM_URL=$(gcloud run services describe start-vm --region="$GCP_REGION" --format="get(status.url)" 2>/dev/null) || true
    fi
    
    # Verify we have both URLs
    if [ -z "$STOP_VM_URL" ] || [ -z "$START_VM_URL" ]; then
        echo "[$TIMESTAMP] Failed to get Cloud Run URLs from both Terraform and gcloud"
        return 1
    fi
    
    echo "[$TIMESTAMP] Successfully retrieved Cloud Run URLs"
    return 0
}

# Update .env file with Cloud Run URLs
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Updating .env file with Cloud Run URLs..."

# Get URLs using our new function
if ! get_cloud_run_urls; then
    echo "[$TIMESTAMP] Failed to get Cloud Run URLs. Would you like to:"
    echo "1. Skip URL updates and continue"
    echo "2. Exit and troubleshoot"
    read -p "Enter your choice (1 or 2): " choice
    
    case $choice in
        1)
            echo "[$TIMESTAMP] Skipping URL updates..."
            ;;
        2)
            echo "[$TIMESTAMP] Exiting for troubleshooting. Please check:"
            echo "1. Cloud Run services: gcloud run services list"
            echo "2. Terraform state: terraform show"
            exit 1
            ;;
        *)
            echo "[$TIMESTAMP] Invalid choice. Exiting."
            exit 1
            ;;
    esac
fi

# Define .env file path
ENV_FILE="../../../Cloud/.env"

# Create backup of .env file
if [ -f "$ENV_FILE" ]; then
    cp "$ENV_FILE" "${ENV_FILE}.backup"
fi

# Update URLs in the existing .env file
{
    if [ -f "$ENV_FILE" ]; then
        # Create a temporary file
        cp "$ENV_FILE" "${ENV_FILE}.tmp"
        
        # Ensure URLs have proper https:// prefix
        STOP_VM_URL=$(echo "$STOP_VM_URL" | sed 's|^https:/|https://|')
        START_VM_URL=$(echo "$START_VM_URL" | sed 's|^https:/|https://|')
        
        # Update or add STOP_VM_FUNCTION_URL
        if grep -q "^STOP_VM_FUNCTION_URL=" "${ENV_FILE}.tmp"; then
            sed -i "s|^STOP_VM_FUNCTION_URL=.*|STOP_VM_FUNCTION_URL=${STOP_VM_URL}|" "${ENV_FILE}.tmp"
        else
            echo -e "\n# VM Function URLs" >> "${ENV_FILE}.tmp"
            echo "STOP_VM_FUNCTION_URL=${STOP_VM_URL}" >> "${ENV_FILE}.tmp"
        fi
        
        # Update or add START_VM_FUNCTION_URL
        if grep -q "^START_VM_FUNCTION_URL=" "${ENV_FILE}.tmp"; then
            sed -i "s|^START_VM_FUNCTION_URL=.*|START_VM_FUNCTION_URL=${START_VM_URL}|" "${ENV_FILE}.tmp"
        else
            echo "START_VM_FUNCTION_URL=${START_VM_URL}" >> "${ENV_FILE}.tmp"
        fi
        
        # Replace the original file
        mv "${ENV_FILE}.tmp" "$ENV_FILE"
    else
        # If .env doesn't exist, create it with a warning
        echo "[$TIMESTAMP] Warning: No existing .env file found at $ENV_FILE"
        echo "[$TIMESTAMP] Creating new .env file with Cloud Run URLs only"
        echo "# VM Function URLs" > "$ENV_FILE"
        echo "STOP_VM_FUNCTION_URL=${STOP_VM_URL}" >> "$ENV_FILE"
        echo "START_VM_FUNCTION_URL=${START_VM_URL}" >> "$ENV_FILE"
    fi
} || {
    echo "[$TIMESTAMP] Error updating .env file"
    if [ -f "${ENV_FILE}.backup" ]; then
        mv "${ENV_FILE}.backup" "$ENV_FILE"
    fi
    exit 1
}

echo "[$TIMESTAMP] Updated Cloud Run URLs in .env file:"
echo "STOP_VM_FUNCTION_URL=${STOP_VM_URL}"
echo "START_VM_FUNCTION_URL=${START_VM_URL}"

# Create and download new key for service account
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Generating new service account key..."
echo "Using service account: $SA_EMAIL"

# Store absolute paths
TEMP_KEY_PATH="$BASE_DIR/temp-key.json"
CREDENTIALS_DIR="$BASE_DIR/../../../Cloud/credentials"
FINAL_KEY_PATH="$CREDENTIALS_DIR/service-account.json"

echo "[$TIMESTAMP] Debug: Using paths:"
echo "Temp key: $TEMP_KEY_PATH"
echo "Credentials dir: $CREDENTIALS_DIR"
echo "Final key: $FINAL_KEY_PATH"

# Check and delete existing key if it exists
if [ -f "$FINAL_KEY_PATH" ]; then
    echo "[$TIMESTAMP] Found existing key, deleting..."
    rm "$FINAL_KEY_PATH"
fi

# Create the key with error checking
if ! gcloud iam service-accounts keys create "$TEMP_KEY_PATH" \
    --iam-account="$SA_EMAIL"; then
    echo "[$TIMESTAMP] Error: Failed to create service account key"
    exit 1
fi

# Debug: Check if temp key exists and has content
echo "[$TIMESTAMP] Debug: Checking temp key..."
ls -l "$TEMP_KEY_PATH"
echo "[$TIMESTAMP] Debug: Temp key contents size (bytes):"
wc -c "$TEMP_KEY_PATH"

# Ensure credentials directory exists
mkdir -p "$CREDENTIALS_DIR"

# Debug: Check credentials directory
echo "[$TIMESTAMP] Debug: Checking credentials directory..."
ls -la "$CREDENTIALS_DIR"

# Move the key to credentials directory with error checking
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Updating service account credentials..."

# Use dd for explicit copy with error checking
if ! dd if="$TEMP_KEY_PATH" of="$FINAL_KEY_PATH" bs=4096; then
    echo "[$TIMESTAMP] Error: Failed to copy service account key to credentials directory"
    exit 1
fi

# Debug: Check if final file exists and has content
echo "[$TIMESTAMP] Debug: Checking final key..."
ls -l "$FINAL_KEY_PATH"
echo "[$TIMESTAMP] Debug: Final key contents size (bytes):"
wc -c "$FINAL_KEY_PATH"

# Clean up temp key
rm "$TEMP_KEY_PATH"

echo "[$TIMESTAMP] Successfully created and moved service account key"

# Send credentials to website repository
log_message "Sending credentials to website repository..."
send_credentials_to_website "$FINAL_KEY_PATH"

# Git commit and push changes
if [ "${AUTO_COMMIT:-false}" = "true" ]; then
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Committing and pushing changes..."
    
    # Store current directory
    CURRENT_DIR=$(pwd)
    
    # Change to repo root for git operations
    cd "$BASE_DIR/../../.."
    
    # Stage changes
    echo "[$TIMESTAMP] Staging changes..."
    git add Cloud/.env
    git add Cloud/credentials/service-account.json
    
    # Create commit with detailed message
    echo "[$TIMESTAMP] Creating commit..."
    git commit -m "Update infrastructure configuration [automated]
    
    - Update Cloud Run URLs in .env
    - Update service account credentials
    
    URLs:
    STOP_VM_FUNCTION_URL=${STOP_VM_URL}
    START_VM_FUNCTION_URL=${START_VM_URL}"
    
    # Push changes
    echo "[$TIMESTAMP] Pushing changes..."
    git push origin main
    
    # Return to original directory
    cd "$CURRENT_DIR"
fi

# Function to upload a secret to GitHub
upload_github_secret() {
    local secret_name="$1"
    local secret_value="$2"
    
    echo "[$TIMESTAMP] Uploading $secret_name to GitHub Secrets..."
    
    # Only add quotes for non-JSON values that contain spaces
    if [[ "$secret_name" != "GCP_SERVICE_ACCOUNT_KEY" ]] && [[ "$secret_value" == *" "* ]]; then
        secret_value="\"$secret_value\""
    fi
    
    # Use GitHub CLI if available, otherwise use REST API
    if command -v gh &> /dev/null; then
        if ! gh secret set "$secret_name" -b"$secret_value" --repo="${GH_OWNER}/${GH_REPO}"; then
            echo "[$TIMESTAMP] Error: Failed to set GitHub secret $secret_name using GitHub CLI"
            return 1
        fi
    else
        echo "[$TIMESTAMP] GitHub CLI not found, please install it first: https://cli.github.com/"
        return 1
    fi
    
    echo "[$TIMESTAMP] Successfully uploaded $secret_name to GitHub Secrets"
    return 0
}

# Function to upload .env contents as secrets
upload_env_secrets() {
    local env_file="$1"
    echo "[$TIMESTAMP] Processing .env file for GitHub Secrets..."
    
    while IFS='=' read -r key value || [ -n "$key" ]; do
        # Skip empty lines and comments
        [[ -z "$key" || "$key" =~ ^# ]] && continue
        
        # Remove quotes and spaces from value
        value=$(echo "$value" | tr -d '"' | tr -d "'")
        
        # Convert key to uppercase and replace dots with underscores for GitHub Secrets
        secret_key=$(echo "$key" | tr '[:lower:]' '[:upper:]' | tr '.' '_')
        
        # Upload to GitHub Secrets
        if ! upload_github_secret "$secret_key" "$value"; then
            echo "[$TIMESTAMP] Warning: Failed to upload $secret_key"
        fi
    done < "$env_file"
}

# Upload secrets to GitHub
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Starting GitHub Secrets upload process..."

# Check for GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "[$TIMESTAMP] Error: GitHub CLI (gh) is not installed. Please install it from: https://cli.github.com/"
    echo "[$TIMESTAMP] After installation, authenticate with: gh auth login"
    exit 1
fi

# Check GitHub authentication
if ! gh auth status &> /dev/null; then
    echo "[$TIMESTAMP] Error: Not authenticated with GitHub. Please run: gh auth login"
    exit 1
fi

# Upload service account key to GitHub Secrets
echo "[$TIMESTAMP] Uploading service account key to GitHub Secrets..."
if ! upload_github_secret "GCP_SERVICE_ACCOUNT_KEY" "$(cat "$FINAL_KEY_PATH")"; then
    echo "[$TIMESTAMP] Error: Failed to upload service account key to GitHub Secrets"
    exit 1
fi

# Upload .env contents to GitHub Secrets
echo "[$TIMESTAMP] Uploading .env contents to GitHub Secrets..."
if ! upload_env_secrets "$ENV_FILE"; then
    echo "[$TIMESTAMP] Failed to upload environment secrets"
    exit 1
fi

# Trigger the upload-secrets workflow
echo "[$TIMESTAMP] Triggering upload-secrets workflow..."
if ! gh api repos/${GH_OWNER}/${GH_REPO}/dispatches \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -f event_type=secrets_updated; then
    echo "[$TIMESTAMP] Warning: Failed to trigger upload-secrets workflow"
fi

# Update .gitignore to exclude sensitive files
GITIGNORE_FILE="$BASE_DIR/../../../.gitignore"
echo "[$TIMESTAMP] Updating .gitignore..."
{
    echo "# Sensitive files"
    echo "Cloud/.env"
    echo "Cloud/credentials/service-account.json"
    echo "Cloud/infrastructure/terraform/terraform.tfvars"
} >> "$GITIGNORE_FILE"

# Remove sensitive files from git
echo "[$TIMESTAMP] Removing sensitive files from git..."
git rm -f --cached "$ENV_FILE" 2>/dev/null || true
git rm -f --cached "$FINAL_KEY_PATH" 2>/dev/null || true
git rm -f --cached "$BASE_DIR/../terraform.tfvars" 2>/dev/null || true

# Create a commit for the cleanup
if [ "${AUTO_COMMIT:-false}" = "true" ]; then
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Creating cleanup commit..."
    
    # Store current directory
    CURRENT_DIR=$(pwd)
    
    # Change to repo root for git operations
    cd "$BASE_DIR/../../.."
    
    # Create commit
    git add .gitignore
    git commit -m "Remove sensitive files and update .gitignore [automated]
    
    - Move sensitive data to GitHub Secrets
    - Remove tracked sensitive files
    - Update .gitignore"
    
    # Push changes
    echo "[$TIMESTAMP] Pushing changes..."
    git push origin main
    
    # Return to original directory
    cd "$CURRENT_DIR"
fi

echo "[$TIMESTAMP] GitHub Secrets upload process completed!"

# Verify deployment
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Verifying deployment..."
terraform output

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Infrastructure deployment completed!"

