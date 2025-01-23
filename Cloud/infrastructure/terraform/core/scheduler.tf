# Service account for Cloud Scheduler
resource "google_service_account" "scheduler_sa" {
  account_id   = "vm-scheduler-sa"
  display_name = "Service Account for VM Scheduler"

  lifecycle {
    ignore_changes = [
      account_id,
      display_name
    ]
  }
}

# Grant necessary permissions
resource "google_project_iam_member" "scheduler_sa_compute_admin" {
  project = var.project
  role    = "roles/compute.instanceAdmin.v1"
  member  = "serviceAccount:${google_service_account.scheduler_sa.email}"
}

# Cloud Scheduler job for starting VM (4:00 PM EST)
resource "google_cloud_scheduler_job" "start_vm_schedule" {
  name             = "start-vm-daily"
  description      = "Starts the Airflow VM daily at 4:00 PM EST"
  schedule         = "0 16 * * *"  # 16:00 = 4:00 PM
  time_zone        = "America/New_York"
  attempt_deadline = "900s"  # 15 minutes

  http_target {
    http_method = "POST"
    uri         = google_cloud_run_service.start_vm.status[0].url
    
    body = base64encode(jsonencode({
      trigger_source = "scheduler"
    }))

    headers = {
      "Content-Type" = "application/json"
    }
  }
}

# Cloud Scheduler job for stopping VM (6:00 PM EST)
resource "google_cloud_scheduler_job" "stop_vm_schedule" {
  name             = "stop-vm-daily"
  description      = "Stops the Airflow VM daily at 6:00 PM EST (backup)"
  schedule         = "0 18 * * *"  # 18:00 = 6:00 PM
  time_zone        = "America/New_York"
  attempt_deadline = "900s"  # 15 minutes

  http_target {
    http_method = "POST"
    uri         = google_cloud_run_service.stop_vm.status[0].url
    
    body = base64encode(jsonencode({
      trigger_source = "scheduler"
    }))

    headers = {
      "Content-Type" = "application/json"
    }
  }
} 