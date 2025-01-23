# Cloud Run service for start_vm
resource "google_cloud_run_service" "start_vm" {
  name     = "start-vm"
  location = var.region
  project  = var.project

  template {
    spec {
      service_account_name = data.google_service_account.cloud_run_sa.email
      timeout_seconds = 900  # 15 minutes
      containers {
        image = "us-central1-docker.pkg.dev/${var.project}/cloud-run-source-deploy/start-vm:latest"
        
        env {
          name  = "PROJECT_ID"
          value = var.project
        }
        env {
          name  = "ZONE"
          value = var.zone
        }
        env {
          name  = "INSTANCE"
          value = var.vm_instance_name
        }
        env {
          name  = "GH_REPO"
          value = var.gh_repo
        }
        env {
          name  = "FUNCTION_TARGET"
          value = "start_vm"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Cloud Run service for stop_vm
resource "google_cloud_run_service" "stop_vm" {
  name     = "stop-vm"
  location = var.region
  project  = var.project

  template {
    spec {
      service_account_name = data.google_service_account.cloud_run_sa.email
      timeout_seconds = 900  # 15 minutes
      containers {
        image = "us-central1-docker.pkg.dev/${var.project}/cloud-run-source-deploy/stop-vm:latest"
        
        env {
          name  = "PROJECT_ID"
          value = var.project
        }
        env {
          name  = "ZONE"
          value = var.zone
        }
        env {
          name  = "INSTANCE"
          value = var.vm_instance_name
        }
        env {
          name  = "GH_REPO"
          value = var.gh_repo
        }
        env {
          name  = "FUNCTION_TARGET"
          value = "stop_vm"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Remove the service account creation block and instead use a data source to reference the existing one
data "google_service_account" "cloud_run_sa" {
  account_id = "cloud-run-vm-manager"
  project    = var.project
}

# Grant necessary permissions to Cloud Run service account
resource "google_project_iam_member" "cloud_run_compute_admin" {
  project = var.project
  role    = "roles/compute.instanceAdmin.v1"
  member  = "serviceAccount:${data.google_service_account.cloud_run_sa.email}"
}

# IAM - Allow unauthenticated access to Cloud Run services
resource "google_cloud_run_service_iam_member" "start_vm_public" {
  service  = google_cloud_run_service.start_vm.name
  location = google_cloud_run_service.start_vm.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_cloud_run_service_iam_member" "stop_vm_public" {
  service  = google_cloud_run_service.stop_vm.name
  location = google_cloud_run_service.stop_vm.location
  role     = "roles/run.invoker"
  member   = "allUsers"
} 