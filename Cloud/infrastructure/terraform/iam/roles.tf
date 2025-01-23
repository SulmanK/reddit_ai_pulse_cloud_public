# Grant monitoring permissions to service account
resource "google_project_iam_member" "monitoring_permissions" {
  project = var.project
  role    = "roles/monitoring.viewer"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
}

# Grant logging permissions
resource "google_project_iam_member" "logging_permissions" {
  project = var.project
  role    = "roles/logging.viewer"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
}

# Grant Cloud Functions permissions
resource "google_project_iam_member" "functions_permissions" {
  project = var.project
  role    = "roles/cloudfunctions.developer"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
}

# Grant Cloud Scheduler permissions
resource "google_project_iam_member" "scheduler_permissions" {
  project = var.project
  role    = "roles/cloudscheduler.admin"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
}

# Grant Service Account User permissions
resource "google_project_iam_member" "sa_user_permissions" {
  project = var.project
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.airflow_service_account.email}"
}

# Grant Cloud Run service account logging permissions
resource "google_project_iam_member" "cloud_run_logging" {
  project = var.project
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloud_run_vm_manager.email}"
}

# Grant Cloud Run service account monitoring permissions
resource "google_project_iam_member" "cloud_run_monitoring" {
  project = var.project
  role    = "roles/monitoring.metricWriter"
  member  = "serviceAccount:${google_service_account.cloud_run_vm_manager.email}"
} 