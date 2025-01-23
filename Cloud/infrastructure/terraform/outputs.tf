output "project_id" {
  value = var.project
}

output "bucket_name" {
  value = google_storage_bucket.reddit_data.name
}

output "airflow_sa_email" {
  value = google_service_account.airflow_sa.email
}

output "vpc_name" {
  value = google_compute_network.vpc.name
}

output "subnet_name" {
  value = google_compute_subnetwork.subnet.name
}

# Cloud Run service URLs
output "start_vm_url" {
  description = "The URL of the start VM Cloud Run service"
  value       = module.core.start_vm_url
}

output "stop_vm_url" {
  description = "The URL of the stop VM Cloud Run service"
  value       = module.core.stop_vm_url
} 