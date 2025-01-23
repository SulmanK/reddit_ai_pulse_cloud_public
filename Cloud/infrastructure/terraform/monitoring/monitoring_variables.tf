variable "project" {
  description = "The GCP project ID"
  type        = string
}

variable "alert_email_address" {
  description = "Email address for monitoring alerts"
  type        = string
}

variable "slack_webhook_url" {
  description = "Slack webhook URL for alerts (optional)"
  type        = string
  default     = ""
}

variable "monitoring_notification_channels" {
  description = "List of notification channel IDs to use for alerts"
  type        = list(string)
  default     = []
}

variable "alert_thresholds" {
  description = "Map of alert thresholds for different metrics"
  type = object({
    cpu_utilization = number
    task_failure_rate = number
    processing_errors = number
  })
  default = {
    cpu_utilization = 0.8    # 80%
    task_failure_rate = 0.2  # 20%
    processing_errors = 10
  }
} 