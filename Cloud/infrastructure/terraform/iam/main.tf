# Grant user permissions to manage service account keys
resource "google_project_iam_binding" "service_account_key_admin" {
  project = var.project
  role    = "roles/iam.serviceAccountKeyAdmin"
  members = [
    "user:${var.user_email}"
  ]
}

# Note: Service account and its permissions are managed in service_accounts.tf 