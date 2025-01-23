# Test Plan for Phase 2 & 3

## Phase 2: Docker Configuration Tests

### 1. Image Building
```bash
# Run build script
cd Cloud/docker
./build.sh

# Verify images
docker images | grep 'reddit-airflow\|reddit-mlflow'
```

Expected results:
- reddit-airflow-base
- reddit-airflow-webserver
- reddit-airflow-scheduler
- reddit-airflow-worker
- reddit-mlflow

### 2. Container Startup
```bash
# Start services
docker-compose up -d

# Check container status
docker-compose ps
```

Expected status:
- All containers: "Up"
- Health checks: "healthy"

### 3. Service Connectivity
```bash
# Test endpoints
curl http://localhost:8080/health  # Airflow
curl http://localhost:5000         # MLflow
curl http://localhost:9090/-/healthy  # Prometheus
curl http://localhost:3000/api/health # Grafana
```

## Phase 3: Monitoring Tests

### 1. Cloud Monitoring
- [ ] Verify dashboard creation
- [ ] Test alert policies
- [ ] Check metric collection
- [ ] Validate log exports

### 2. Grafana Setup
- [ ] Access Grafana UI
- [ ] Check Prometheus data source
- [ ] Verify Airflow metrics
- [ ] Test dashboard panels

### 3. Metrics Validation

#### Cloud Monitoring Metrics:
- VM status
- Function executions
- Resource utilization
- Cost metrics

#### Grafana Pipeline Metrics:
- DAG success rates
- Task durations
- Queue lengths
- Worker utilization

### 4. Alert Testing

1. **Cloud Monitoring Alerts**
```bash
# Simulate VM start failure
# (Test by temporarily revoking permissions)
```

2. **Grafana Alerts**
```bash
# Simulate high task failure rate
# (Test by submitting failing tasks)
```

## Test Execution Steps

1. **Infrastructure Check**
```bash
# Verify infrastructure
./scripts/test.sh
```

2. **Docker Setup**
```bash
# Build and start containers
cd Cloud/docker
./build.sh
docker-compose up -d
```

3. **Monitoring Setup**
```bash
# Verify Cloud Monitoring
gcloud monitoring dashboards list

# Check Grafana
curl http://localhost:3000/api/health
```

4. **Integration Test**
```bash
# Run a test DAG
airflow dags trigger test_monitoring_dag
```

## Success Criteria

### Phase 2
- [ ] All Docker images build successfully
- [ ] Containers start and are healthy
- [ ] Services are accessible
- [ ] Volume mounts are working

### Phase 3
- [ ] Cloud Monitoring dashboard shows metrics
- [ ] Grafana displays pipeline metrics
- [ ] Alerts are properly configured
- [ ] Logs are being exported

## Rollback Plan

1. **Container Issues**
```bash
# Stop containers
docker-compose down

# Clean up
docker system prune -a

# Rebuild
./build.sh
```

2. **Monitoring Issues**
```bash
# Reset Grafana
docker-compose restart grafana

# Recreate Cloud Monitoring
terraform taint google_monitoring_dashboard.vm_automation
terraform apply
``` 