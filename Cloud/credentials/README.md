# Credentials Management

This directory contains service account credentials and other sensitive files.
Do not commit any files in this directory to version control.

Required files:
1. `service-account.json` - GCP service account key file

## Setup Instructions

1. Move your service account JSON file here and rename it to `service-account.json`
2. Update the GOOGLE_APPLICATION_CREDENTIALS path in your .env file
3. Never commit credentials to version control 