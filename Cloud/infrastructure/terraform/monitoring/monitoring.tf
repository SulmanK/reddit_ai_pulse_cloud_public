# Cloud Monitoring Dashboard
resource "google_monitoring_dashboard" "airflow_dashboard" {
  dashboard_json = jsonencode({
    displayName = "Reddit Pipeline Dashboard"
    gridLayout = {
      columns = "2"
      widgets = [
        # VM Metrics
        {
          title = "VM CPU Utilization"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\""
                }
              }
            }]
          }
        },
        {
          title = "VM Memory Usage"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"compute.googleapis.com/instance/memory/usage\" resource.type=\"gce_instance\""
                }
              }
            }]
          }
        },
        # Airflow Task Metrics
        {
          title = "DAG Success Rate"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"custom.googleapis.com/airflow/dag_success_rate\""
                }
              }
            }]
          }
        },
        {
          title = "Task Duration"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"custom.googleapis.com/airflow/task_duration\""
                }
              }
            }]
          }
        },
        # Pipeline Metrics
        {
          title = "Records Processed"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"custom.googleapis.com/reddit/records_processed\""
                }
              }
            }]
          }
        },
        {
          title = "Processing Errors"
          xyChart = {
            dataSets = [{
              timeSeriesQuery = {
                timeSeriesFilter = {
                  filter = "metric.type=\"custom.googleapis.com/reddit/processing_errors\""
                }
              }
            }]
          }
        }
      ]
    }
  })
}

# Alert Policies
resource "google_monitoring_alert_policy" "vm_cpu_utilization" {
  display_name = "High CPU Utilization Alert"
  combiner     = "OR"
  conditions {
    display_name = "CPU Usage > 80%"
    condition_threshold {
      filter          = "metric.type=\"compute.googleapis.com/instance/cpu/utilization\" resource.type=\"gce_instance\""
      duration        = "300s"
      comparison      = "COMPARISON_GT"
      threshold_value = 0.8
      trigger {
        count = 1
      }
    }
  }
  notification_channels = [google_monitoring_notification_channel.email.id]
}

resource "google_monitoring_alert_policy" "airflow_task_failures" {
  display_name = "Airflow Task Failures Alert"
  combiner     = "OR"
  conditions {
    display_name = "Task Failure Rate > 20%"
    condition_threshold {
      filter          = "metric.type=\"${google_monitoring_metric_descriptor.airflow_task_failure_rate.type}\" AND resource.type=\"gce_instance\""
      duration        = "300s"
      comparison      = "COMPARISON_GT"
      threshold_value = 0.2
      trigger {
        count = 1
      }
    }
  }
  notification_channels = [google_monitoring_notification_channel.email.id]
  enabled = true
  depends_on = [google_monitoring_metric_descriptor.airflow_task_failure_rate]
}

resource "google_monitoring_alert_policy" "pipeline_errors" {
  display_name = "Pipeline Processing Errors Alert"
  combiner     = "OR"
  conditions {
    display_name = "Processing Error Rate"
    condition_threshold {
      filter          = "metric.type=\"${google_monitoring_metric_descriptor.processing_errors.type}\" AND resource.type=\"gce_instance\""
      duration        = "300s"
      comparison      = "COMPARISON_GT"
      threshold_value = 10
      trigger {
        count = 1
      }
    }
  }
  notification_channels = [google_monitoring_notification_channel.email.id]
  enabled = true
  depends_on = [google_monitoring_metric_descriptor.processing_errors]
}

resource "google_monitoring_alert_policy" "vm_automation" {
  display_name = "VM Automation Alert"
  combiner     = "OR"
  conditions {
    display_name = "VM Start/Stop Failures"
    condition_threshold {
      filter          = "metric.type=\"${google_monitoring_metric_descriptor.vm_automation_failures.type}\" AND resource.type=\"gce_instance\""
      duration        = "0s"
      comparison      = "COMPARISON_GT"
      threshold_value = 0
      trigger {
        count = 1
      }
    }
  }
  notification_channels = [google_monitoring_notification_channel.email.id]
  enabled = true
  depends_on = [google_monitoring_metric_descriptor.vm_automation_failures]
}

# Notification Channels
resource "google_monitoring_notification_channel" "email" {
  display_name = "Email Notification Channel"
  type         = "email"
  labels = {
    email_address = var.alert_email_address
  }
}

# Optional: Slack notification channel
resource "google_monitoring_notification_channel" "slack" {
  count = var.slack_webhook_url != "" ? 1 : 0
  
  display_name = "Slack Notification Channel"
  type         = "slack"
  labels = {
    channel_name = "#airflow-alerts"
  }
  sensitive_labels {
    auth_token = var.slack_webhook_url
  }
}

# First, define the custom metric descriptors
resource "google_monitoring_metric_descriptor" "airflow_task_failure_rate" {
  description = "Rate of Airflow task failures"
  display_name = "Airflow Task Failure Rate"
  type = "custom.googleapis.com/airflow/task_failure_rate"
  metric_kind = "GAUGE"
  value_type = "DOUBLE"
  unit = "1"
  labels {
    key = "task_id"
    value_type = "STRING"
    description = "The ID of the Airflow task"
  }
}

resource "google_monitoring_metric_descriptor" "processing_errors" {
  description = "Number of processing errors in the pipeline"
  display_name = "Pipeline Processing Errors"
  type = "custom.googleapis.com/reddit/processing_errors"
  metric_kind = "GAUGE"
  value_type = "INT64"
  unit = "1"
}

resource "google_monitoring_metric_descriptor" "vm_automation_failures" {
  description = "Number of VM automation failures"
  display_name = "VM Automation Failures"
  type = "custom.googleapis.com/airflow/vm_automation_failures"
  metric_kind = "GAUGE"
  value_type = "INT64"
  unit = "1"
} 