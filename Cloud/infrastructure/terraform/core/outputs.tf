output "start_vm_url" {
  description = "The URL of the start VM Cloud Run service"
  value       = google_cloud_run_service.start_vm.status[0].url
}

output "stop_vm_url" {
  description = "The URL of the stop VM Cloud Run service"
  value       = google_cloud_run_service.stop_vm.status[0].url
} 