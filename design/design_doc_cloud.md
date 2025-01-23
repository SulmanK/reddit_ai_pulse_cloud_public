# Reddit Data Pipeline - Ultra Cost-Optimized Cloud Implementation

## Goal
✅ Transform the local Reddit data pipeline into a minimal, cost-effective cloud solution using GCP services, focusing on core functionality and minimal running costs.

## Current Implementation Status

### ✅ Phase 1: Infrastructure Setup (Completed)
- [x] VPC and networking configuration
- [x] Service accounts and IAM roles
- [x] BigQuery datasets
- [x] Terraform configuration
- [x] Monitoring and logging setup

### ✅ Phase 2: Docker Configuration (Completed)
- [x] Base Airflow image
- [x] Specialized service images (webserver, scheduler, worker)
- [x] MLflow container
- [x] Monitoring containers (Prometheus, Grafana)
- [x] Docker Compose configuration
- [x] End-to-end testing in Docker environment

### ✅ Phase 3: Pipeline Components (Completed)
- [x] DAG implementation and testing
- [x] Metric collection and monitoring
- [x] GitHub integration
- [x] DBT transformations
- [x] MLflow integration

### ✅ Phase 4: VM Deployment (Next Up)
- [x] VM provisioning with e2-small
- [x] Docker setup on VM
- [x] Environment configuration
- [x] Pipeline deployment and testing
- [x] Performance optimization

### ✅ Phase 5: Cloud Automation (Pending)
- [x] Cloud Scheduler setup
- [x] VM start/stop automation
- [x] Monitoring alerts
- [x] Cost optimization verification

## Technical Architecture

### Infrastructure Components
```
Cloud/
├── terraform/                  # Infrastructure as Code
│   ├── compute.tf             # VM and compute resources
│   ├── network.tf             # VPC and networking
│   ├── storage.tf             # GCS and BigQuery
│   ├── iam.tf                 # Service accounts and permissions
│   └── variables.tf           # Configuration variables
├── docker/                    # Container configurations
│   ├── Dockerfile.base        # Base Airflow image
│   ├── Dockerfile.webserver   # Airflow webserver
│   ├── Dockerfile.mlflow      # MLflow server
│   └── docker-compose.yml     # Service orchestration
├── airflow_project/           # Airflow configuration
│   ├── dags/                  # Pipeline DAG definitions
│   │   ├── reddit_pipeline_dag.py    # Main pipeline DAG
│   │   ├── push_to_github_dag.py     # GitHub sync DAG
│   │   └── scripts/                  # Task scripts
│   ├── plugins/               # Custom plugins
│   │   ├── logging_utils.py          # Logging utilities
│   │   └── metrics/                  # Metric collectors
│   └── logs/                 # Airflow logs
└── scripts/                  # Utility scripts
    ├── ingest_preprocess.py  # Data ingestion
    ├── summarize.py          # Text summarization
    └── sentiment_analysis.py # Sentiment analysis
    └── gemini_analysis.py    # Gemini summarization
    └── cleanup_bigquery.py   # BigQuery cleanup

```

### Service Architecture
```
                                     ┌─────────────────┐
                                     │  Cloud Function │
                                     │    (Start VM)   │
                                     └────────┬────────┘
                                              │
                                              ▼
┌──────────┐    ┌────────┐    ┌─────────────────────────────┐
│ Reddit   │───>│   GCS  │───>│        Airflow VM           │
│   API    │    │ Bucket │    │  ┌─────────┐   ┌─────────┐ │
└──────────┘    └────────┘    │  │ Airflow │   │ MLflow  │ │
                              │  │ Services │   │ Server  │ │
                              │  └────┬────┘   └────┬────┘ │
                              └───────┼───────────┬─┘      │
                                     │           │         │
                              ┌──────▼──┐   ┌────▼─────┐  │
                              │ BigQuery │   │ Metrics  │  │
                              │         │   │ Monitor  │  │
                              └─────────┘   └──────────┘  │
                                              ▲           │
                                              │           │
                                     ┌────────┴────────┐  │
                                     │  Cloud Function │  │
                                     │    (Stop VM)    │  │
                                     └─────────────────┘  │
                                     └───────────────────┘
```

### Component Details

#### 1. Data Processing Pipeline
- **Ingestion & Preprocessing**
  - Reddit API data collection
  - GCS raw data storage
  - Initial data cleaning

- **Data Transformation**
  - DBT models for BigQuery
  - Incremental processing
  - Data quality checks

- **ML Processing**
  - Text summarization with Claude AI
  - Sentiment analysis with RoBERTa
  - MLflow experiment tracking

#### 2. Infrastructure Components
- **Compute Resources**
  - e2-small VM instance
  - Docker container orchestration
  - Cloud Functions for automation

- **Storage Solutions**
  - GCS for raw data and artifacts
  - BigQuery for processed data
  - Local volumes for container state

- **Networking**
  - Custom VPC configuration
  - IAP for secure access
  - Internal service communication

#### 3. Monitoring & Logging
- **Metrics Collection**
  - StatsD for Airflow metrics
  - Prometheus for system metrics
  - Custom metric parsers

- **Visualization**
  - Grafana dashboards
  - Cloud Monitoring
  - BigQuery data validation

#### 4. Security & Access Control
- **Authentication**
  - Service account management
  - IAM role assignments
  - API key management

- **Network Security**
  - VPC firewall rules
  - SSL/TLS encryption
  - Secure secret management

### Core Services

#### ✅ Compute Layer (Configured)
- Single Airflow VM
  - Machine type: `e2-small`
  - OS: Ubuntu LTS
  - Docker-based deployment
  - Combined scheduler/worker
  - Automated startup/shutdown
  - Estimated monthly cost: $6-8 (running 4h/day)

#### ✅ Storage Layer (Implemented)
- GCS Buckets
  - `reddit-raw-data`
  - `reddit-processed`
  - Aggressive cleanup
  - Estimated cost: $1-2/month

#### ✅ Database Layer (Completed)
- BigQuery
  - Leverage free tier
  - Optimize query patterns
  - Estimated cost: $0-10/month

#### ✅ Monitoring Stack (Completed)
1. **Cloud Monitoring**
   - Custom dashboard for VM automation
   - Alert policies for critical events
   - Metric collection for all services

2. **Local Monitoring**
   - Prometheus for metric collection
   - Grafana for visualization
   - StatsD for Airflow metrics


#### ✅ VM Deployment
- [x] Provision e2-standard-2 instance
- [x] Configure Docker and dependencies
- [x] Deploy pipeline components
- [x] Test end-to-end flow
- [x] Optimize performance

#### ✅ Cloud Automation
- [x] Set up Cloud Scheduler
- [x] Implement VM start/stop functions
- [x] Configure monitoring alerts
- [x] Verify cost optimization

## Required Scripts

### VM Startup Script
```bash
#!/bin/bash
# Start Docker services
docker-compose -f /opt/airflow/Cloud/docker/docker-compose.yml up -d

# Wait for services
sleep 30

# Verify health
curl -f http://localhost:8080/health
```

### VM Shutdown Script
```bash
#!/bin/bash
# Check pipeline status
if [[ $(docker-compose ps -q | wc -l) -gt 0 ]]; then
    # Graceful shutdown
    docker-compose down
fi
```

### Cloud Functions
```python
def start_vm(event, context):
    """Start Airflow VM on schedule"""
    compute = google.cloud.compute_v1.InstancesClient()
    compute.start(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)

def stop_vm(event, context):
    """Stop VM after pipeline completion"""
    compute = google.cloud.compute_v1.InstancesClient()
    compute.stop(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)
```

## Cost Optimization Strategies
✅ **VM Management**
   - Start only when needed
   - Automatic shutdown after pipeline completion
   - Use preemptible VM when possible

✅ **Storage**
   - Aggressive cleanup policies
   - Minimal data retention
   - Use BigQuery free tier efficiently

✅ **Operations**
   - Single VM for all Airflow components
   - Batch processing to minimize runtime
   - Automated resource management

## Security Considerations
1. **Access Control**
   - Service account with minimal permissions
   - Secure secret management
   - Network security rules

2. **Data Security**
   - Encrypted data at rest
   - Secure communication
   - Access logging

## Risks and Mitigations
1. **Cost Overruns**
   - Implemented VM scheduling
   - Set up budget alerts
   - Regular cost monitoring

2. **Service Disruption**
   - Health monitoring
   - Automated recovery
   - Alert notifications

3. **Data Loss**
   - Regular backups
   - Data replication
   - Recovery procedures 