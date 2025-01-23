# Use Python 3.11 slim image
FROM python:3.11-slim

# Install Google Cloud SDK and SSH client
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    openssh-client && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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