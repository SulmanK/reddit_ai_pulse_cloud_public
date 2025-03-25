# Service Account and IAM configuration
resource "google_service_account" "airflow_sa" {
  account_id   = "airflow-service-account"
  display_name = "Service Account for Airflow"
  description  = "Used by Airflow to interact with GCP services"
}

# Add a delay to ensure service account is fully propagated
resource "time_sleep" "wait_for_sa" {
  depends_on = [google_service_account.airflow_sa]
  create_duration = "90s"
}

# Grant Storage Admin role
resource "google_project_iam_member" "storage_admin" {
  project = var.project
  role    = "roles/storage.admin"
  member  = "serviceAccount:${google_service_account.airflow_sa.email}"
  depends_on = [time_sleep.wait_for_sa]
}

# Grant BigQuery Admin role
resource "google_project_iam_member" "bigquery_admin" {
  project = var.project
  role    = "roles/bigquery.admin"
  member  = "serviceAccount:${google_service_account.airflow_sa.email}"
  depends_on = [time_sleep.wait_for_sa]
}

# Grant Service Account User role
resource "google_project_iam_member" "service_account_user" {
  project = var.project
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.airflow_sa.email}"
  depends_on = [time_sleep.wait_for_sa]
}

# Grant Compute Admin role for VM management
resource "google_project_iam_member" "compute_admin" {
  project = var.project
  role    = "roles/compute.admin"
  member  = "serviceAccount:${google_service_account.airflow_sa.email}"
  depends_on = [time_sleep.wait_for_sa]
} 