"""
GitHub Integration Module

This module handles pushing processed data to GitHub repositories and triggering associated workflows.
It includes functionality to:
1. Push markdown files to a specified repository
2. Trigger website sync workflows
3. Handle file versioning and updates

Dependencies:
    - requests: For making HTTP requests to GitHub API
    - base64: For encoding file content
    - glob: For file pattern matching
    - os: For path operations
    - datetime: For date handling

Environment Variables Required:
    - GH_PAT: Personal access token for GitHub API authentication
    - GH_OWNER: GitHub username/organization
    - GH_REPO: Target repository name
    - GH_WEBSITE_REPO: Website repository name
"""

import glob
import requests
from base64 import b64encode
import json
import os
from datetime import datetime

# Define base paths for Docker environment
AIRFLOW_DIR = "/opt/airflow"
RESULTS_DIR = os.path.join(AIRFLOW_DIR, "results")

def trigger_website_sync(**context):
    """
    Trigger the sync-content.yml workflow in the website repository.
    
    This function sends a POST request to GitHub Actions API to trigger
    a workflow that syncs content between repositories.
    
    Args:
        **context: Airflow context dictionary containing execution information
        
    Raises:
        Exception: If the workflow trigger fails
    
    Returns:
        None
    """
    url = f"https://api.github.com/repos/{os.environ['GH_OWNER']}/{os.environ['GH_WEBSITE_REPO']}/actions/workflows/sync-content-cloud.yml/dispatches"
    
    headers = {
        "Authorization": f"token {os.environ['GH_PAT']}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "ref": "main"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 204:
        print(f"Failed to trigger workflow: {response.status_code}")
        print(f"Response: {response.text}")
        raise Exception("Failed to trigger website sync workflow")
    
    print("Successfully triggered website sync workflow")

def push_gemini_results(**context):
    """
    Push Gemini analysis markdown files to GitHub and trigger website sync.
    
    This function:
    1. Locates markdown files in the results directory for the current date
    2. Pushes each file to the specified GitHub repository
    3. Maintains the same directory structure in GitHub
    4. Triggers a website sync workflow after successful push
    
    Args:
        **context: Airflow context dictionary containing execution information
        
    Raises:
        ValueError: If no markdown files are found
        Exception: If GitHub API calls fail
        
    Returns:
        None
        
    Directory Structure:
        results/
        └── YYYY/
            └── MM/
                └── DD/
                    ├── llm_subreddit1.md
                    ├── llm_subreddit2.md
                    └── ...
    """
    # Get current date for the folder path
    current_date = datetime.now()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    
    # Path to results directory in Docker container
    results_path = os.path.join(RESULTS_DIR, year, month, day, "*.md")
    
    # Get all markdown files
    md_files = glob.glob(results_path)
    
    if not md_files:
        raise ValueError(f"No markdown files found in {results_path}")
            
    for md_file in md_files:
        # Read the markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
                
        # Get the filename for GitHub path
        filename = os.path.basename(md_file)
        
        # GitHub API endpoint - storing in 'results' directory
        url = f"https://api.github.com/repos/{os.environ['GH_OWNER']}/{os.environ['GH_REPO']}/contents/Cloud/results/{year}/{month}/{day}/{filename}"
        
        headers = {
            "Authorization": f"token {os.environ['GH_PAT']}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        try:
            # Check if file exists
            response = requests.get(url, headers=headers)
            sha = response.json()["sha"] if response.status_code == 200 else None
            
            # Encode content
            content_bytes = content.encode('utf-8')
            content_encoded = b64encode(content_bytes).decode('utf-8')
            
            # Prepare the commit
            body = {
                "message": f"Update analysis for {filename} - {current_date}",
                "content": content_encoded,
                "sha": sha  # Include SHA if file exists
            }
            
            # Push to GitHub
            response = requests.put(url, headers=headers, json=body)
            
            if not (response.status_code == 200 or response.status_code == 201):
                print(f"Failed to push {filename}: {response.json()}")
                raise Exception(f"GitHub API call failed for {filename}: {response.json()}")
                    
            print(f"Successfully pushed {filename} to GitHub")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            raise
        
    # After all files are pushed successfully, trigger the website sync once
    trigger_website_sync()