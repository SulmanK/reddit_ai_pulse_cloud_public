variable "project" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region to deploy resources"
  type        = string
}

variable "zone" {
  description = "The GCP zone to deploy resources"
  type        = string
}

variable "vm_instance_name" {
  description = "Name of the VM instance"
  type        = string
}

variable "vm_machine_type" {
  description = "Machine type for the VM"
  type        = string
}

variable "network_name" {
  description = "The name of the VPC network"
  type        = string
}

variable "subnet_name" {
  description = "The name of the subnet"
  type        = string
}

variable "subnet_cidr" {
  description = "The CIDR range for the subnet"
  type        = string
}

variable "bucket_name" {
  description = "Name of the GCS bucket"
  type        = string
}

variable "gh_pat" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}

variable "gh_owner" {
  description = "GitHub repository owner"
  type        = string
}

variable "gh_repo" {
  description = "GitHub repository name"
  type        = string
}

variable "machine_type" {
  description = "The machine type for the Airflow VM"
  type        = string
}

variable "service_account_email" {
  description = "The email address of the service account to be used by the Airflow instance"
  type        = string
  sensitive   = true
} 