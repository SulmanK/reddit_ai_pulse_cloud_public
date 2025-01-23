import os
import json
import time
import logging
import traceback
import subprocess
import platform
from flask import Flask, request, jsonify, make_response
from google.cloud import compute_v1

# Create Flask app
app = Flask(__name__)

def get_gcloud_path():
    """Get the full path to gcloud executable based on OS"""
    if platform.system() == "Windows":
        # Common installation paths for gcloud on Windows
        possible_paths = [
            r"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
            r"C:\Program Files\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
            os.path.expanduser("~") + r"\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        raise Exception("gcloud not found. Please ensure Google Cloud SDK is installed and in PATH")
    return "gcloud"  # For non-Windows systems, assume it's in PATH

@app.route("/", methods=["POST"])
def start_vm_http():
    """
    HTTP endpoint for Cloud Run to start a Compute Engine instance.
    Accepts POST requests with optional JSON body:
    {'trigger_source': 'scheduler'|'manual'|'dag'}
    """
    return start_vm(request)

def start_vm(request):
    """
    Function to start a Compute Engine instance and execute startup script.
    """
    project = os.environ.get('PROJECT_ID')
    zone = os.environ.get('ZONE')
    instance = os.environ.get('INSTANCE')
    gh_repo = os.environ.get('GH_REPO')

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info(f"Environment: PROJECT_ID={project}, ZONE={zone}, INSTANCE={instance}, GH_REPO={gh_repo}")

    # Parse request data
    trigger_source = "scheduler"
    if request and hasattr(request, 'is_json') and request.is_json:
        data = request.get_json()
        if data and 'trigger_source' in data:
            trigger_source = data.get('trigger_source')
    
    logger.info(f"Start triggered by: {trigger_source}")

    try:
        # Get gcloud path
        gcloud_path = get_gcloud_path()
        logger.info(f"Using gcloud path: {gcloud_path}")

        # Check if instance is running
        status_cmd = [gcloud_path, "compute", "instances", "describe", instance,
                     f"--zone={zone}", f"--project={project}",
                     "--format=get(status)"]
        status = subprocess.run(status_cmd, text=True, capture_output=True)
        
        is_running = status.stdout.strip().upper() == "RUNNING"
        
        if not is_running:
            # Start the instance
            start_cmd = [gcloud_path, "compute", "instances", "start", instance,
                        f"--zone={zone}", f"--project={project}", "--quiet"]
            logger.info(f"Starting instance with command: {' '.join(start_cmd)}")
            process = subprocess.run(start_cmd, text=True, capture_output=True)
            
            if process.returncode != 0:
                error_msg = f"Failed to start instance: {process.stderr}"
                logger.error(error_msg)
                return jsonify({'status': 'error', 'message': error_msg}), 500
            
            # Wait for VM to be fully started
            logger.info("Waiting 90 seconds for VM to be fully ready...")
            time.sleep(90)

        # Execute startup script
        logger.info("Executing startup script...")
        startup_cmd = [gcloud_path, "compute", "ssh", "--quiet", f"airflow@{instance}",
                      f"--zone={zone}", f"--project={project}", 
                      "--command", f"bash /opt/airflow/{gh_repo}/Cloud/infrastructure/terraform/vm_scripts/start_dag.sh"]
        
        process = subprocess.run(startup_cmd, text=True, capture_output=True)
        
        if process.returncode == 0:
            logger.info("Startup script executed successfully")
            logger.info(f"Startup stdout: {process.stdout}")
            msg = f'Successfully started instance and executed startup script'
            return jsonify({'status': 'success', 'message': msg})
        else:
            error_msg = f"Startup script failed: {process.stderr}"
            logger.error(error_msg)
            return jsonify({'status': 'error', 'message': error_msg}), 500

    except Exception as e:
        error_msg = f'Error during startup process: {str(e)}'
        logger.error(error_msg)
        logger.error(f"Full stack trace: {traceback.format_exc()}")
        return jsonify({'status': 'error', 'message': error_msg}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 9099)), debug=False) 