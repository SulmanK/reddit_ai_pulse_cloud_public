variable "project" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "retention_days" {
  description = "Number of days to retain logs"
  type        = number
  default     = 30
} 