import os
import json
import logging
import subprocess
from flask import Flask, request, jsonify
import platform
import traceback

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
def stop_vm_http():
    """
    HTTP endpoint for Cloud Run to stop a Compute Engine instance.
    Accepts POST requests with optional JSON body:
    {'trigger_source': 'scheduler'|'manual'|'dag'}
    """
    return stop_vm(request)

def stop_vm(request):
    """
    Function to stop a Compute Engine instance.
    Only runs shutdown script if VM is running.
    
    Args:
        request (flask.Request): The request object
        - If called from manual trigger: expects JSON with {'trigger_source': 'manual'}
        - If called from Scheduler: no specific payload needed
    Returns:
        JSON response with status message
    """
    project = os.environ.get('PROJECT_ID')
    zone = os.environ.get('ZONE')
    instance = os.environ.get('INSTANCE')
    gh_repo = os.environ.get('GH_REPO')

    # Setup detailed logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Log environment variables (excluding any sensitive data)
    logger.info(f"Environment: PROJECT_ID={project}, ZONE={zone}, INSTANCE={instance}, GH_REPO={gh_repo}")

    # Parse request data if present
    trigger_source = "scheduler"
    if request and hasattr(request, 'is_json') and request.is_json:
        data = request.get_json()
        if data and 'trigger_source' in data:
            trigger_source = data.get('trigger_source')
    
    logger.info(f"Shutdown triggered by: {trigger_source}")

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
            msg = f'Instance {instance} is already stopped (Triggered by: {trigger_source})'
            logger.info(msg)
            return jsonify({'status': 'success', 'message': msg})

        # Execute shutdown script via SSH since VM is running
        logger.info("Executing shutdown script via SSH...")
        shutdown_cmd = f"bash /opt/airflow/{gh_repo}/Cloud/infrastructure/terraform/vm_scripts/shutdown.sh"
        ssh_cmd = [gcloud_path, "compute", "ssh", "--quiet", f"airflow@{instance}", 
                  f"--zone={zone}", f"--project={project}", "--command", shutdown_cmd]
        
        logger.info(f"Executing command: {' '.join(ssh_cmd)}")
        process = subprocess.run(ssh_cmd, text=True, capture_output=True)
        
        if process.returncode != 0:
            logger.error(f"SSH command failed with return code {process.returncode}")
            logger.error(f"SSH stderr: {process.stderr}")
            logger.error(f"SSH stdout: {process.stdout}")
            raise Exception(f"Failed to execute shutdown script: {process.stderr}")
        
        logger.info("Shutdown script executed successfully. Stopping instance...")
        logger.info(f"SSH stdout: {process.stdout}")

        # Stop the instance
        stop_cmd = [gcloud_path, "compute", "instances", "stop", instance, 
                   f"--zone={zone}", f"--project={project}", "--quiet"]
        logger.info(f"Executing stop command: {' '.join(stop_cmd)}")
        process = subprocess.run(stop_cmd, text=True, capture_output=True)
        
        if process.returncode != 0:
            logger.error(f"Stop command failed with return code {process.returncode}")
            logger.error(f"Stop stderr: {process.stderr}")
            logger.error(f"Stop stdout: {process.stdout}")
            raise Exception(f"Failed to stop instance: {process.stderr}")
        
        logger.info(f"Stop command stdout: {process.stdout}")
        msg = f'Successfully executed shutdown script and stopped instance {instance} (Triggered by: {trigger_source})'
        logger.info(msg)
        return jsonify({'status': 'success', 'message': msg})

    except Exception as e:
        error_msg = f'Error during shutdown process: {str(e)}'
        logger.error(error_msg)
        logger.error(f"Full stack trace: {traceback.format_exc()}")
        return jsonify({'status': 'error', 'message': error_msg}), 500

if __name__ == "__main__":
    # For local testing with Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 9099)), debug=False) 