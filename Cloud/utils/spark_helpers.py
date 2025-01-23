from pyspark.sql import SparkSession

def create_spark_session(app_name: str) -> SparkSession:
    """
    Create a Spark session configured for GCP.
    
    Args:
        app_name: Name of the Spark application
        
    Returns:
        SparkSession configured for GCP
    """
    return (SparkSession.builder
            .appName(app_name)
            .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.27.1")
            .config("spark.hadoop.google.cloud.auth.service.account.enable", "true")
            .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", 
                   "/opt/airflow/keys/service-account.json")
            .getOrCreate())

def read_from_gcs(spark: SparkSession, bucket: str, path: str) -> DataFrame:
    """
    Read data from Google Cloud Storage.
    
    Args:
        spark: SparkSession
        bucket: GCS bucket name
        path: Path to file in bucket
        
    Returns:
        DataFrame with loaded data
    """
    gcs_path = f"gs://{bucket}/{path}"
    return spark.read.format("parquet").load(gcs_path)

def read_from_bigquery(spark: SparkSession, project: str, dataset: str, table: str) -> DataFrame:
    """
    Read data from BigQuery.
    
    Args:
        spark: SparkSession
        project: GCP project ID
        dataset: BigQuery dataset name
        table: BigQuery table name
        
    Returns:
        DataFrame with loaded data
    """
    table_id = f"{project}.{dataset}.{table}"
    return (spark.read.format("bigquery")
           .option("table", table_id)
           .load())

def write_to_bigquery(df: DataFrame, project: str, dataset: str, table: str, mode: str = "overwrite"):
    """
    Write data to BigQuery.
    
    Args:
        df: DataFrame to write
        project: GCP project ID
        dataset: BigQuery dataset name
        table: BigQuery table name
        mode: Write mode (overwrite/append)
    """
    table_id = f"{project}.{dataset}.{table}"
    (df.write.format("bigquery")
     .option("table", table_id)
     .mode(mode)
     .save()) 