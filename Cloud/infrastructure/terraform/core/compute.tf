# Compute Engine instance
resource "google_compute_instance" "vm_instance" {
  name         = var.vm_instance_name
  machine_type = var.vm_machine_type
  zone         = var.zone
  tags         = ["airflow-vm"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 50  # Size in GB
      type  = "pd-balanced"  # Use balanced persistent disk for good performance
    }
  }

  network_interface {
    network    = var.network_name
    subnetwork = var.subnet_name
    access_config {
      // Ephemeral public IP
    }
  }

  metadata = {
    bucket-name = var.bucket_name
    startup-script = file("${path.module}/../vm_scripts/startup.sh")
  }

  service_account {
    email  = var.service_account_email
    scopes = ["cloud-platform"]
  }
} 