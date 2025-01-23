terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
    time = {
      source  = "hashicorp/time"
      version = "~> 0.9.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

provider "time" {}

# IAM module should be first as other modules depend on service accounts
module "iam" {
  source     = "./iam"
  project    = var.project
  user_email = var.alert_email_address
}

# Core module depends on IAM for service accounts
module "core" {
  source = "./core"
  
  project      = var.project
  region       = var.region
  zone         = var.zone
  gh_pat       = var.gh_pat
  gh_owner     = var.gh_owner
  gh_repo      = var.gh_repo
  machine_type = var.machine_type
  
  network_name = google_compute_network.vpc.name
  subnet_name  = google_compute_subnetwork.subnet.name
  subnet_cidr  = var.subnet_cidr
  service_account_email = module.iam.airflow_service_account_email
  
  vm_instance_name = var.vm_instance_name
  vm_machine_type = var.vm_machine_type
  bucket_name = var.bucket_name
  
  depends_on = [module.iam]
}

# Monitoring depends on both IAM and core
module "monitoring" {
  source = "./monitoring"
  
  project = var.project
  alert_email_address = var.alert_email_address
  
  depends_on = [module.core, module.iam]
}

# Logging depends on IAM and core
module "logging" {
  source = "./logging"
  
  project = var.project
  
  depends_on = [module.core, module.iam]
} 