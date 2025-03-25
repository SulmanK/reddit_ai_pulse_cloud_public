#!/bin/bash

# =============================================================================
# cleanup.sh
# -----------------------------------------------------------------------------
# A comprehensive cleanup script for the Reddit AI Pulse Cloud infrastructure.
# This script systematically removes all GCP resources created by the project.
#
# The script performs cleanup in the following order:
# 1. IAM (roles and bindings)
# 2. Cloud Scheduler jobs
# 3. Cloud Functions
# 4. GCS buckets and contents
# 5. BigQuery datasets and tables
# 6. Artifact Registry repositories
# 7. Cloud Run services
# 8. Service accounts
# 9. Compute Engine resources
# 10. VPC, subnets, and firewall rules
# 11. Monitoring resources (alerts, dashboards)
# 12. Terraform state
# 13. Log buckets
#
# The script includes error handling, retries for dependent resources,
# and creates detailed logs of the cleanup process in the resource_info directory.
#
# Usage:
#   ./cleanup.sh
#
# Requirements:
#   - GCP project configuration in .env file
#   - Authenticated gcloud CLI
#   - Required permissions to delete resources
# =============================================================================

set -e  # Exit immediately if a command exits with a non-zero status

# Create resource_info directory
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Creating resource_info directory..."
RESOURCE_INFO_DIR="../resource_info"
mkdir -p "$RESOURCE_INFO_DIR"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Loading project configuration..."
source ../../../.env

# Set gcloud project
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Setting gcloud project..."
gcloud config set project "$GCP_PROJECT_ID"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Starting cleanup of existing resources..."

# List all resources using Cloud Asset Inventory
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Listing all project resources..."
gcloud asset search-all-resources --scope=projects/"$GCP_PROJECT_ID" > "$RESOURCE_INFO_DIR/project_resources.txt"

# List all IAM policies
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Listing all IAM policies..."
gcloud asset search-all-iam-policies --scope=projects/"$GCP_PROJECT_ID" > "$RESOURCE_INFO_DIR/iam_policies.txt"

# 1. Clean up IAM
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 1. Cleaning up IAM..."
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Current IAM policy:"
gcloud projects get-iam-policy "$GCP_PROJECT_ID" --format=json > "$RESOURCE_INFO_DIR/current_iam.json"

# List all service accounts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Current service accounts:"
gcloud iam service-accounts list --project="$GCP_PROJECT_ID" --format="table(email,displayName)" > "$RESOURCE_INFO_DIR/service_accounts.txt"

# Remove all IAM bindings except owner and essential service accounts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Removing non-essential IAM bindings..."
for binding in $(gcloud projects get-iam-policy "$GCP_PROJECT_ID" --format="table(bindings.role)" | grep roles/ | grep -v "roles/owner"); do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Processing role: $binding"
    members=$(gcloud projects get-iam-policy "$GCP_PROJECT_ID" --format="get(bindings.members)" --filter="bindings.role=$binding")
    for member in $members; do
        if [[ $member != *"@developer.gserviceaccount.com" && $member != *"@cloudservices.gserviceaccount.com" && $member != *"@appspot.gserviceaccount.com" ]]; then
            TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$TIMESTAMP] Removing binding for $member with role $binding"
            gcloud projects remove-iam-policy-binding "$GCP_PROJECT_ID" \
                --member="$member" \
                --role="$binding" --quiet 2>/dev/null || true
        fi
    done
done

# 2. Delete Cloud Scheduler jobs
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 2. Deleting Cloud Scheduler jobs..."

# Delete specific scheduler jobs by name
for job in "start-vm-daily" "stop-vm-daily"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting scheduler job: $job"
    gcloud scheduler jobs delete "$job" --location="$GCP_REGION" --quiet 2>/dev/null || true
done

# 3. Delete Cloud Functions
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 3. Deleting Cloud Functions..."
functions=$(gcloud functions list --format="get(name)" 2>/dev/null || true)
for func in $functions; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting function: $func"
    gcloud functions delete "$(basename "$func")" --region="$GCP_REGION" --quiet 2>/dev/null || true
done

# 4. Delete GCS buckets
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 4. Deleting GCS buckets..."
buckets=$(gsutil ls 2>/dev/null || true)
for bucket in $buckets; do
    if [[ "$bucket" == "gs://$GCP_PROJECT_ID"* || \
          "$bucket" == "gs://reddit-ai-pulse-1"* || \
          "$bucket" == "gs://gcf-sources-"* ]]; then
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        echo "[$TIMESTAMP] Deleting bucket: $bucket"
        # Force delete all versions of objects
        gsutil -m rm -r -f "$bucket"/** 2>/dev/null || true
        # Force delete any remaining objects (including versioned)
        gsutil -m rm -r -f "$bucket" 2>/dev/null || true
        # Try to delete the bucket itself
        gsutil rb -f "$bucket" 2>/dev/null || true
    fi
done

# 4.25 Delete BigQuery resources
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 4.25. Deleting BigQuery resources..."

# Delete tables in processed_data dataset
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting tables in processed_data dataset..."
tables=$(bq ls --format=sparse "$GCP_PROJECT_ID:processed_data" 2>/dev/null | tail -n +3 | awk '{print $1}')
for table in $tables; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting table: processed_data.$table"
    bq rm -f -t "$GCP_PROJECT_ID:processed_data.$table" 2>/dev/null || true
done

# Delete tables in raw_data dataset
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting tables in raw_data dataset..."
tables=$(bq ls --format=sparse "$GCP_PROJECT_ID:raw_data" 2>/dev/null | tail -n +3 | awk '{print $1}')
for table in $tables; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting table: raw_data.$table"
    bq rm -f -t "$GCP_PROJECT_ID:raw_data.$table" 2>/dev/null || true
done

# Delete datasets
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting datasets..."
for dataset in "raw_data" "processed_data"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting dataset: $dataset"
    bq rm -r -f "$GCP_PROJECT_ID:$dataset" 2>/dev/null || true
done

# 4.5 Delete Artifact Registry resources
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 4.5. Deleting Artifact Registry resources..."

# Delete images from cloud-run-source-deploy repository
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting Docker images from cloud-run-source-deploy repository..."
for image in "start-vm" "stop-vm"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting image: $image"
    gcloud artifacts docker images delete "us-central1-docker.pkg.dev/$GCP_PROJECT_ID/cloud-run-source-deploy/$image:latest" --quiet --delete-tags 2>/dev/null || true
done

# Delete the repository itself
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting cloud-run-source-deploy repository..."
gcloud artifacts repositories delete cloud-run-source-deploy --location="$GCP_REGION" --quiet 2>/dev/null || true

# Direct repository deletion for gcf-artifacts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Attempting to delete gcf-artifacts repository..."
gcloud artifacts repositories delete gcf-artifacts --location="$GCP_REGION" --quiet --async 2>/dev/null || true

# Short wait to allow deletion to start
sleep 10

# 4.75 Delete Cloud Run services
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 4.75. Deleting Cloud Run services..."

# Delete specific Cloud Run services
for service in "start-vm" "stop-vm"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting Cloud Run service: $service"
    gcloud run services delete "$service" --region="$GCP_REGION" --quiet 2>/dev/null || true
done

# Wait for Cloud Run services to be deleted
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for Cloud Run services deletion..."
sleep 30

# 5. Delete service accounts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 5. Deleting service accounts..."

# First remove all IAM bindings for these accounts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Removing IAM bindings for specific service accounts..."
for sa in "airflow-service-account" "airflow-service-account-v2" "vm-scheduler-sa" "cloud-run-vm-manager"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Removing IAM bindings for $sa..."
    
    # Get all bindings in one call and process them
    gcloud projects get-iam-policy "$GCP_PROJECT_ID" \
        --filter="bindings.members:${sa}@$GCP_PROJECT_ID.iam.gserviceaccount.com OR bindings.members:deleted:serviceAccount:${sa}@$GCP_PROJECT_ID.iam.gserviceaccount.com" \
        --format="table(bindings.role)" | while read role; do
        if [[ ! -z "$role" && "$role" != "ROLE" ]]; then
            TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$TIMESTAMP] Removing role $role from $sa..."
            gcloud projects remove-iam-policy-binding "$GCP_PROJECT_ID" \
                --member="serviceAccount:${sa}@$GCP_PROJECT_ID.iam.gserviceaccount.com" \
                --role="$role" --quiet || true
        fi
    done
done

# Then delete the service accounts
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting service accounts..."
for sa in "airflow-service-account" "airflow-service-account-v2" "vm-scheduler-sa" "cloud-run-vm-manager"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting service account $sa..."
    gcloud iam service-accounts delete "${sa}@$GCP_PROJECT_ID.iam.gserviceaccount.com" --quiet || true
done

# Wait for service account operations to complete
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for service account operations to complete..."
sleep 30

# Verify service account deletion
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Verifying service account deletion..."
for sa in "airflow-service-account" "airflow-service-account-v2" "vm-scheduler-sa" "cloud-run-vm-manager"; do
    if gcloud iam service-accounts describe "${sa}@$GCP_PROJECT_ID.iam.gserviceaccount.com" 2>/dev/null; then
         TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
         echo "[$TIMESTAMP] WARNING: Service account $sa still exists!"
    else
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        echo "[$TIMESTAMP] Confirmed: Service account $sa has been deleted."
    fi
done

# 6. Delete Compute Engine resources
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 6. Deleting Compute Engine resources..."
instances=$(gcloud compute instances list --format="get(name)" 2>/dev/null || true)
for instance in $instances; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting instance: $instance"
    gcloud compute instances delete "$instance" --zone="$GCP_ZONE" --quiet 2>/dev/null || true
done

# 7. Delete VPC and subnet
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 7. Deleting VPC and subnet..."

# First, delete specific firewall rules
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting specific firewall rules..."
for rule in "allow-internal" "allow-ssh"; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting firewall rule: $rule"
    gcloud compute firewall-rules delete "$rule" --quiet 2>/dev/null || true
done

# Then delete any remaining firewall rules associated with the VPC
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting any remaining firewall rules..."
firewall_rules=$(gcloud compute firewall-rules list --filter="network=reddit-pipeline-vpc" --format="get(name)")
for rule in $firewall_rules; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting firewall rule: $rule"
    gcloud compute firewall-rules delete "$rule" --quiet 2>/dev/null || true
done

# Wait for firewall rules to be deleted
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for firewall rules deletion..."
sleep 30  # Increased wait time

# Verify no firewall rules remain
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Verifying firewall rules deletion..."
remaining_rules=$(gcloud compute firewall-rules list --filter="network=reddit-pipeline-vpc" --format="get(name)")
if [[ ! -z "$remaining_rules" ]]; then
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] WARNING: Some firewall rules still exist: $remaining_rules"
    echo "[$TIMESTAMP] Attempting forced deletion..."
    for rule in $remaining_rules; do
        gcloud compute firewall-rules delete "$rule" --quiet --force 2>/dev/null || true
    done
    sleep 30
fi

# Delete all routes associated with the VPC
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting routes..."
routes=$(gcloud compute routes list --filter="network=reddit-pipeline-vpc" --format="get(name)")
for route in $routes; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting route: $route"
    gcloud compute routes delete "$route" --quiet 2>/dev/null || true
done

# Wait for routes to be deleted
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for routes deletion..."
sleep 20

# Delete subnet with retries
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting subnet 'reddit-pipeline-subnet'..."
max_retries=3
retry_count=0
while [ $retry_count -lt $max_retries ]; do
    if gcloud compute networks subnets delete "reddit-pipeline-subnet" \
        --region="$GCP_REGION" --quiet 2>/dev/null; then
        echo "[$TIMESTAMP] Subnet deleted successfully"
        break
    else
        retry_count=$((retry_count+1))
        if [ $retry_count -lt $max_retries ]; then
            TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$TIMESTAMP] Retry $retry_count: Waiting before retrying subnet deletion..."
            sleep 30
        fi
    fi
done

# Wait for subnet deletion to complete
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for subnet deletion to complete..."
sleep 30

# Delete the VPC with retries
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Deleting VPC 'reddit-pipeline-vpc'..."
retry_count=0
while [ $retry_count -lt $max_retries ]; do
    if gcloud compute networks delete "reddit-pipeline-vpc" --quiet 2>/dev/null; then
        TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
        echo "[$TIMESTAMP] VPC deleted successfully"
        break
    else
        retry_count=$((retry_count+1))
        if [ $retry_count -lt $max_retries ]; then
            TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$TIMESTAMP] Retry $retry_count: Waiting before retrying VPC deletion..."
            sleep 30
        fi
    fi
done

# Verify VPC deletion
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Verifying VPC deletion..."
if gcloud compute networks describe "reddit-pipeline-vpc" --format="get(name)" 2>/dev/null; then
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] WARNING: VPC still exists after cleanup attempts"
else
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Confirmed: VPC has been deleted"
fi

# 8. Delete monitoring resources
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 8. Deleting monitoring resources..."
# Delete alert policies
policies=$(gcloud monitoring alert-policies list --format="get(name)" 2>/dev/null || true)
for policy in $policies; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting alert policy: $policy"
    gcloud monitoring alert-policies delete "$policy" --quiet 2>/dev/null || true
done

# Delete dashboards
dashboards=$(gcloud monitoring dashboards list --format="get(name)" 2>/dev/null || true)
for dashboard in $dashboards; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Deleting dashboard: $dashboard"
    gcloud monitoring dashboards delete "$dashboard" --quiet 2>/dev/null || true
done

# 9. Clean up Terraform state
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 9. Cleaning up Terraform state..."
cd ..  # Move up to terraform directory
rm -f .terraform.lock.hcl terraform.tfstate terraform.tfstate.backup tfplan 2>/dev/null || true
rm -rf .terraform 2>/dev/null || true
cd resource_scripts  # Return to resource_scripts directory

# 10. Save resource lists for verification
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 10. Saving final state..."
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Final IAM policy:"
gcloud projects get-iam-policy "$GCP_PROJECT_ID" --format=json > "$RESOURCE_INFO_DIR/final_iam.json"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Final service accounts:"
gcloud iam service-accounts list --project="$GCP_PROJECT_ID" --format="table(email,displayName)" > "$RESOURCE_INFO_DIR/final_service_accounts.txt"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Final resources:"
gcloud asset search-all-resources --scope=projects/"$GCP_PROJECT_ID" > "$RESOURCE_INFO_DIR/final_resources.txt"

# 11. Verify cleanup
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 11. Verifying cleanup..."
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Checking service accounts..."
gcloud iam service-accounts list --project="$GCP_PROJECT_ID"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Checking GCS buckets..."
gsutil ls

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Cleanup completed! Resource lists saved to $RESOURCE_INFO_DIR:"
echo "- project_resources.txt: Initial resource list"
echo "- iam_policies.txt: Initial IAM policies"
echo "- final_resources.txt: Final resource list"
echo "- final_iam.json: Final IAM policy"
echo "Review these files in the $RESOURCE_INFO_DIR directory to ensure proper cleanup."

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] You can now run test.sh for a fresh deployment."

# 4.6 Delete Log Buckets
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] 4.6. Deleting Log Buckets..."

# List and delete log buckets
log_buckets=$(gcloud logging buckets list --format="table(name,location)" 2>/dev/null || true)
if [[ ! -z "$log_buckets" ]]; then
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Found log buckets:"
    echo "$log_buckets"
    while IFS=$'\t' read -r name location; do
        if [[ "$name" != "NAME" && "$name" != "_Required" && "$name" != "_Default" ]]; then
            TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$TIMESTAMP] Deleting log bucket: $name in $location"
            gcloud logging buckets delete "$name" --location="$location" --quiet 2>/dev/null || true
        fi
    done <<< "$log_buckets"
fi

# Wait for log operations to complete
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Waiting for log operations to complete..."
sleep 30