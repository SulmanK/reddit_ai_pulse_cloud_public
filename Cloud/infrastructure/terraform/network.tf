# Network resources
resource "google_compute_network" "vpc" {
  name                    = var.network_name
  auto_create_subnetworks = false

  lifecycle {
    prevent_destroy = false
    ignore_changes = [
      name,
      auto_create_subnetworks
    ]
  }
}

resource "google_compute_subnetwork" "subnet" {
  name          = var.subnet_name
  ip_cidr_range = var.subnet_cidr
  region        = var.region
  network       = google_compute_network.vpc.id

  lifecycle {
    prevent_destroy = false
    ignore_changes = [
      name,
      ip_cidr_range
    ]
  }
}

# Allow SSH access
resource "google_compute_firewall" "allow_ssh" {
  name    = "allow-ssh"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]  # Be cautious with this in production
  target_tags   = ["airflow-vm"]  # Tag for the VM
}

# Allow internal communication
resource "google_compute_firewall" "allow_internal" {
  name    = "allow-internal"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["0-65535"]
  }
  allow {
    protocol = "udp"
    ports    = ["0-65535"]
  }
  allow {
    protocol = "icmp"
  }

  source_ranges = ["10.0.0.0/24"]  # Subnet CIDR
} 