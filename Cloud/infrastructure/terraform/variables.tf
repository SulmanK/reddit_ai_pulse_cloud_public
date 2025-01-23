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

variable "alert_email_address" {
  description = "Email address for monitoring alerts and notifications"
  type        = string
  sensitive   = true
}

variable "vm_instance_name" {
  description = "Name of the VM instance"
  type        = string
}

variable "vm_machine_type" {
  description = "Machine type for the VM"
  type        = string
}

variable "bucket_name" {
  description = "Name of the GCS bucket"
  type        = string
}

variable "dataset_raw" {
  description = "Name of the raw BigQuery dataset"
  type        = string
}

variable "dataset_processed" {
  description = "Name of the processed BigQuery dataset"
  type        = string
}

variable "gh_pat" {
  description = "GitHub personal access token for cloning the repository"
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

variable "network_name" {
  description = "Name of the VPC network"
  type        = string
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
}

variable "subnet_cidr" {
  description = "CIDR range for the subnet"
  type        = string
}

variable "machine_type" {
  description = "The machine type for the Airflow VM"
  type        = string
}

variable "service_account_email" {
  description = "The email address of the service account"
  type        = string
}

variable "subreddits" {
  description = "List of subreddits to create tables for"
  type        = list(string)
  default     = [
                  "dataengineering",
                  "machinelearning",
                  "datascience",
                  "claudeai",
                  "singularity",
                  "localllama",
                  "openai",
                  "stablediffusion"
                ]
} 