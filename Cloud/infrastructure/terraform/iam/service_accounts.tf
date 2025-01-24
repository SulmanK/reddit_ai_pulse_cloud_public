# Airflow Service Account
resource "google_service_account" "airflow_service_account" {
  account_id   = "airflow-service-account-v2"
  display_name = "Airflow Service Account"
  project      = var.project
  description  = "Service account for Airflow operations"

  lifecycle {
    ignore_changes = [
      display_name,
      description,
      disabled
    ]
  }
}

# Cloud Run Service Account for VM Management
resource "google_service_account" "cloud_run_vm_manager" {
  account_id   = "cloud-run-vm-manager"
  display_name = "Cloud Run VM Manager"
  project      = var.project
  description  = "Service account for Cloud Run services to manage VM instances"

  lifecycle {
    ignore_changes = [
      display_name,
      description,
      disabled
    ]
  }
}

# Add delay after service account creation
resource "time_sleep" "wait_30_seconds" {
  depends_on = [
    google_service_account.airflow_service_account,
    google_service_account.cloud_run_vm_manager
  ]
  create_duration = "30s"
  destroy_duration = "30s"
}

# Grant necessary permissions to Airflow Service Account
resource "google_project_iam_member" "airflow_storage_admin" {
  project = var.project
  role    = "roles/storage.admin"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
  depends_on = [time_sleep.wait_30_seconds]
}

resource "google_project_iam_member" "airflow_bigquery_admin" {
  project = var.project
  role    = "roles/bigquery.admin"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
  depends_on = [google_project_iam_member.airflow_storage_admin]
}

resource "google_project_iam_member" "airflow_compute_admin" {
  project = var.project
  role    = "roles/compute.admin"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
  depends_on = [google_project_iam_member.airflow_bigquery_admin]
}

resource "google_project_iam_member" "airflow_monitoring_admin" {
  project = var.project
  role    = "roles/monitoring.admin"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
  depends_on = [google_project_iam_member.airflow_compute_admin]
}

resource "google_project_iam_member" "airflow_logging_writer" {
  project = var.project
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
  depends_on = [google_project_iam_member.airflow_monitoring_admin]
}

# Grant permissions to Cloud Run VM Manager Service Account
resource "google_project_iam_member" "cloud_run_compute_admin" {
  project = var.project
  role    = "roles/compute.instanceAdmin.v1"
  member  = "serviceAccount:${google_service_account.cloud_run_vm_manager.email}"
  depends_on = [time_sleep.wait_30_seconds]
}

resource "google_project_iam_member" "cloud_run_service_account_user" {
  project = var.project
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.cloud_run_vm_manager.email}"
  depends_on = [google_project_iam_member.cloud_run_compute_admin]
}

# Output the service account emails
output "airflow_service_account_email" {
  value = google_service_account.airflow_service_account.email
  depends_on = [
    google_service_account.airflow_service_account,
    google_project_iam_member.airflow_storage_admin,
    google_project_iam_member.airflow_bigquery_admin,
    google_project_iam_member.airflow_compute_admin,
    google_project_iam_member.airflow_monitoring_admin,
    google_project_iam_member.airflow_logging_writer
  ]
}

output "cloud_run_service_account_email" {
  value = google_service_account.cloud_run_vm_manager.email
  depends_on = [
    google_service_account.cloud_run_vm_manager,
    google_project_iam_member.cloud_run_compute_admin,
    google_project_iam_member.cloud_run_service_account_user
  ]
} 