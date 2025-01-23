#!/bin/bash
set -e

# Load environment variables
source ../.env

# Function to build and tag an image
build_image() {
    local service=$1
    local tag="${DOCKER_REGISTRY}/reddit-airflow-${service}:latest"
    echo "Building ${service} image..."
    docker build --no-cache -t "$tag" -f "Dockerfile.${service}" .
    echo "Successfully built ${service} image: ${tag}"
}

# Build base image first
echo "Building base image..."
docker build --no-cache -t reddit-airflow-base:latest -f Dockerfile.base .

# Build service images
build_image "webserver"
build_image "scheduler"
build_image "worker"

# Build MLflow image
echo "Building MLflow image..."
docker build --no-cache -t "${DOCKER_REGISTRY}/reddit-mlflow:latest" -f Dockerfile.mlflow .

echo "All images built successfully!" 