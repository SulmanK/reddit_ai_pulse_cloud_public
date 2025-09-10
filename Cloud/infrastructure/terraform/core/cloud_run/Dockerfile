# Use Python 3.11 slim image
FROM python:3.11-slim

# Install dependencies and Google Cloud SDK
RUN apt-get update && apt-get install -y \
    curl \
    openssh-client \
    && curl https://sdk.cloud.google.com | bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add gcloud to PATH
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV PORT=9099

# Run the application with gunicorn
CMD exec gunicorn --bind :$PORT ${FUNCTION_TARGET}:app --workers 1 --threads 8 --timeout 0 