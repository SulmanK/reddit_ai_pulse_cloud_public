# Variables for subreddits should be defined in variables.tf
# Datasets
resource "google_bigquery_dataset" "raw_data" {
  dataset_id  = "raw_data"
  description = "Raw data from Reddit subreddits"
  location    = "US"
  project     = var.project

  delete_contents_on_destroy = false  # Protect against accidental data loss
}

resource "google_bigquery_dataset" "processed_data" {
  dataset_id  = "processed_data"
  description = "Processed data from Reddit subreddits"
  location    = "US"
  project     = var.project

  delete_contents_on_destroy = false
}

# Dynamic raw tables for each subreddit
resource "google_bigquery_table" "raw_subreddit_tables" {
  for_each = toset(var.subreddits)
  
  dataset_id = google_bigquery_dataset.raw_data.dataset_id
  table_id   = "raw_${lower(each.value)}"
  project    = var.project

  deletion_protection = false  # Set to true in production

  schema = jsonencode([
    {
      name = "post_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "subreddit",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "title",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "author",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "url",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "score",
      type = "INTEGER",
      mode = "NULLABLE"
    },
    {
      name = "created_utc",
      type = "FLOAT",
      mode = "NULLABLE"
    },
    {
      name = "comments",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "ingestion_timestamp",
      type = "FLOAT",
      mode = "NULLABLE"
    }
  ])
}

# Dynamic processed posts tables for each subreddit
resource "google_bigquery_table" "processed_posts_tables" {
  for_each = toset(var.subreddits)
  
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "posts_${lower(each.value)}"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "post_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "subreddit",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "title",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "author",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "url",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "score",
      type = "INTEGER",
      mode = "NULLABLE"
    },
    {
      name = "created_utc",
      type = "TIMESTAMP",
      mode = "NULLABLE"
    },
    {
      name = "ingestion_timestamp",
      type = "TIMESTAMP",
      mode = "NULLABLE"
    }
  ])
}

# Dynamic processed comments tables for each subreddit
resource "google_bigquery_table" "processed_comments_tables" {
  for_each = toset(var.subreddits)
  
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "comments_${lower(each.value)}"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "post_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "comment_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "author",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "body",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "created_utc",
      type = "TIMESTAMP",
      mode = "NULLABLE"
    }
  ])
}

# Utility tables
resource "google_bigquery_table" "daily_summary" {
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "daily_summary_data"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "id",
      type = "INTEGER",
      mode = "REQUIRED"
    },
    {
      name = "subreddit",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "post_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "post_score",
      type = "INTEGER",
      mode = "NULLABLE"
    },
    {
      name = "post_url",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "comment_id",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "summary_date",
      type = "DATE",
      mode = "REQUIRED"
    },
    {
      name = "processed_date",
      type = "TIMESTAMP",
      mode = "REQUIRED"
    },
    {
      name = "needs_processing",
      type = "BOOLEAN",
      mode = "REQUIRED"
    },
    {
      name = "post_content",
      type = "STRING",
      mode = "NULLABLE"
    },
    {
      name = "comment_body",
      type = "STRING",
      mode = "NULLABLE"
    }
  ])
}

resource "google_bigquery_table" "text_summary" {
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "text_summary_results"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "comment_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "comment_summary",
      type = "STRING",
      mode = "NULLABLE"
    }
  ])
}

resource "google_bigquery_table" "sentiment_analysis" {
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "sentiment_analysis_results"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "comment_id",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "sentiment_score",
      type = "FLOAT",
      mode = "NULLABLE"
    },
    {
      name = "sentiment_label",
      type = "STRING",
      mode = "NULLABLE"
    }
  ])
}

resource "google_bigquery_table" "processing_metadata" {
  dataset_id = google_bigquery_dataset.processed_data.dataset_id
  table_id   = "processing_metadata"
  project    = var.project

  deletion_protection = false

  schema = jsonencode([
    {
      name = "subreddit",
      type = "STRING",
      mode = "REQUIRED"
    },
    {
      name = "last_processed_timestamp",
      type = "FLOAT",
      mode = "NULLABLE"
    },
    {
      name = "last_update_time",
      type = "TIMESTAMP",
      mode = "REQUIRED"
    }
  ])
} 