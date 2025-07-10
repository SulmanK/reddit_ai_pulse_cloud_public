---
title: "Data Engineering Subreddit"
date: "2025-07-10"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Why there aren’t databases for images, audio and video](https://www.reddit.com/r/dataengineering/comments/1lwc30f/why_there_arent_databases_for_images_audio_and/) (Score: 41)
    * Discusses the reasons why specialized databases for storing images, audio, and video aren't as prevalent as databases for other data types, and alternative storage solutions like blob storage and data lakes.
2.  [[META] Mods, can we also please remove all these kind of posts](https://www.reddit.com/r/dataengineering/comments/1lw9mod/meta_mods_can_we_also_please_remove_all_these/) (Score: 30)
    *  A meta discussion about removing common or low-quality posts, like beginner questions or company self-promotion, from the dataengineering subreddit.
3.  [Suggestion Required for Storing Parquet files cheaply](https://www.reddit.com/r/dataengineering/comments/1lwdn2k/suggestion_required_for_storing_parquet_files/) (Score: 11)
    *  Seeking suggestions for cost-effective methods to store Parquet files, addressing issues like slow retrieval from cloud storage and potential alternative solutions like BigQuery or Bigtable.
4.  [DLT + Airflow + DBT/SQLMesh](https://www.reddit.com/r/dataengineering/comments/1lw8q6w/dlt_airflow_dbtsqlmesh/) (Score: 9)
    * Discusses how people are using DLT, Airflow, DBT, and SQLMesh together, particularly focusing on experiences and setups within cloud environments like Azure and AWS.
5.  [API layer for 3rd party to access DB](https://www.reddit.com/r/dataengineering/comments/1lw8qt1/api_layer_for_3rd_party_to_access_db/) (Score: 9)
    * Discusses best practices for building a secure API layer for third-party access to a database, including the use of API Gateways, authentication methods, and considerations for request volume and response speed.
6.  [Good practice for beginners: Materialized view](https://www.reddit.com/r/dataengineering/comments/1lwcb06/good_practice_for_beginners_materialized_view/) (Score: 8)
    *  Discusses the use of materialized views for beginners, weighing the pros and cons in terms of query optimization, resource consumption, and potential alternatives like dbt.
7.  [Tools for Managing Database Artifacts](https://www.reddit.com/r/dataengineering/comments/1lwevet/tools_for_managing_database_artifacts/) (Score: 7)
    *  Discusses the tools for managing database artifacts, DevOps and CICD practices.
8.  [Built a Serverless News NLP Pipeline (AWS + DuckDB + Streamlit) – Feedback Welcome!](https://www.reddit.com/r/dataengineering/comments/1lwedtl/built_a_serverless_news_nlp_pipeline_aws_duckdb/) (Score: 6)
    *  A post about a serverless news NLP pipeline built using AWS, DuckDB, and Streamlit, inviting feedback from the community.
9.  [Seeking advice on Pipeline Optimization](https://www.reddit.com/r/dataengineering/comments/1lwimpe/seeking_advice_on_pipeline_optimization/) (Score: 5)
    * Seeking advice on optimizing a data pipeline.
10. [Right way to put JSON with nested arrays in Data Vault 2.0](https://www.reddit.com/r/dataengineering/comments/1lwm5v8/right_way_to_put_json_with_nested_arrays_in_data/) (Score: 1)
    * Discussion about how to handle JSON data with nested arrays in Data Vault 2.0, focusing on the use of Links and Hubs to model relationships between data entities.
11. [I Changed My Mind: AI Will Replace Us](https://medium.com/@danthelion/i-changed-my-mind-ai-will-replace-us-8b7460f2a233) (Score: 0)
    * Expresses concerns about AI replacing data engineers.
12. [Best (cost-effective) way to write low-volume Confluent kafka topics as delta/iceberg in Azure?](https://www.reddit.com/r/dataengineering/comments/1lw9d3d/best_costeffective_way_to_write_lowvolume/) (Score: 0)
    *  Seeking advice on the most cost-effective method for writing low-volume Confluent Kafka topics as Delta/Iceberg in Azure, comparing different approaches like Structured Streaming.
13. [A conversational feed of real time market data](https://www.reddit.com/r/dataengineering/comments/1lwj3hx/a_conversational_feed_of_real_time_market_data/) (Score: 0)
    * A post about A conversational feed of real time market data.
14. [Free timestamp to code converter](https://www.reddit.com/r/dataengineering/comments/1lwl0oz/free_timestamp_to_code_converter/) (Score: 0)
    * A post about a free timestamp to code converter.

# Detailed Analysis by Thread
**[Why there aren’t databases for images, audio and video (Score: 41)](https://www.reddit.com/r/dataengineering/comments/1lwc30f/why_there_arent_databases_for_images_audio_and/)**
*  **Summary:** The thread discusses why traditional databases are not well-suited for storing large media files (images, audio, video). It explores alternative solutions such as blob storage (S3, Azure Blobs), data lakes, and NoSQL databases like Cassandra/Scylla. The discussion also touches on the benefits of storing file paths in databases and the possibility of using linked data and the semantic web.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Traditional databases are inefficient and slow for storing large binary data (blobs).
    * Blob storage (S3, Azure Blobs) is a more suitable and cost-effective solution for storing media files, with database tables storing the paths to these files.
    * NoSQL databases like Cassandra/Scylla can be used for storing raster images, and techniques like similarity search can be applied.

**[[META] Mods, can we also please remove all these kind of posts (Score: 30)](https://www.reddit.com/r/dataengineering/comments/1lw9mod/meta_mods_can_we_also_please_remove_all_these/)**
*  **Summary:** This thread is a meta-discussion about the quality of posts in the dataengineering subreddit. Users are requesting moderators to remove repetitive posts, such as "how to get into data engineering" and promotional content. The moderators are responding with information about current automod rules and their efforts to combat spam and low-quality content.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  The subreddit is flooded with repetitive beginner questions and company self-promotion.
    *  Moderators are actively working to remove spam and low-quality content using automod rules and manual bans.
    *  Some users feel guilty of posting the types of content being criticized.

**[Suggestion Required for Storing Parquet files cheaply (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1lwdn2k/suggestion_required_for_storing_parquet_files/)**
*  **Summary:** The thread revolves around finding a cost-effective solution for storing and retrieving Parquet files. Users are discussing the issues of slow retrieval speeds from cloud storage (GCS) and considering alternatives such as using BigQuery, Bigtable, and partitioning the data.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  Pulling individual Parquet files from GCS can be slow due to network hops and metadata scans.
    *  BigQuery, Bigtable, and DreamFactory can be used together to improve data load times.
    *  Consider the small files problem and the provisioning of cluster/executor machines when using Spark to read Parquet files.

**[DLT + Airflow + DBT/SQLMesh (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1lw8q6w/dlt_airflow_dbtsqlmesh/)**
*  **Summary:**  This thread discusses the integration of DLT (Delta Live Tables), Airflow, and DBT/SQLMesh in data engineering workflows, with a focus on how these tools are being used in Azure and AWS environments. Users share their experiences and setups, particularly regarding containerization, secrets management, and infrastructure as code.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * AWS Fargate can be used to run containers with DBT projects, storing passwords in secrets manager and managing infrastructure with Terraform.
    * For inserting data into MS SQL databases, SSIS (SQL Server Integration Services) could be used.
    * The thread seeks input on how to best integrate these tools in Azure.

**[API layer for 3rd party to access DB (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1lw8qt1/api_layer_for_3rd_party_to_access_db/)**
*  **Summary:** This thread discusses best practices for creating an API layer to allow third-party access to a database. The discussion covers using REST or GraphQL APIs, API Gateways, authentication methods (IAM roles, JWTs, OAuth), and considerations for security, rate limiting, and performance.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Building a secure API layer (REST or GraphQL) outside the VPC is the best practice, using an API Gateway for security and access control.
    * SFTP/SSH can be configured within the VPC to allow third-party access to specific folders with data refreshes.
    * AWS API Gateway with API key authentication can be used with a Lambda function within the VPC, managing rate limits and request validation.

**[Good practice for beginners: Materialized view (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1lwcb06/good_practice_for_beginners_materialized_view/)**
*  **Summary:** This thread discusses the use of materialized views as a good practice for beginners in data engineering. The discussion covers the benefits and drawbacks of materialized views, alternative solutions like dbt, and the importance of query optimization and indexing.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Materialized views can be a quick solution for complex business logic but have drawbacks like exclusive locks during refresh, time-consuming refreshes, and resource consumption.
    * Query optimization and indexing should be considered before implementing materialized views.
    * Migrating from materialized views to dbt can offer better resource management and partitioning capabilities.

**[Tools for Managing Database Artifacts (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1lwevet/tools_for_managing_database_artifacts/)**
*  **Summary:**  This thread discusses the tools and practices for managing database artifacts, mentioning DevOps and CICD principles.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    * The selection of tools depends on IT security and tech stack.
    * DBT is a good tool to use.

**[Built a Serverless News NLP Pipeline (AWS + DuckDB + Streamlit) – Feedback Welcome! (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1lwedtl/built_a_serverless_news_nlp_pipeline_aws_duckdb/)**
*  **Summary:** The thread points to open-source project showcases.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    *  The thread is a pointer to community projects.

**[Seeking advice on Pipeline Optimization (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1lwimpe/seeking_advice_on_pipeline_optimization/)**
*  **Summary:** The thread points to community learning resources.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Blocking is a good first step for pipeline optimization.
    * Fuzzy matching isn't going to be 100% reliable.
    * The thread is a pointer to community learning resources.

**[Right way to put JSON with nested arrays in Data Vault 2.0 (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lwm5v8/right_way_to_put_json_with_nested_arrays_in_data/)**
*  **Summary:**  The thread discusses how to handle JSON data with nested arrays in Data Vault 2.0, focusing on the use of Links and Hubs to model relationships between data entities.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    * A Link is used to handle many to many relationships in raw vault and it links (connects) two hubs.

**[I Changed My Mind: AI Will Replace Us (Score: 0)](https://medium.com/@danthelion/i-changed-my-mind-ai-will-replace-us-8b7460f2a233)**
*  **Summary:** Expresses concerns about AI replacing data engineers.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    * The thread suggests banning these types of posts.

**[Best (cost-effective) way to write low-volume Confluent kafka topics as delta/iceberg in Azure? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lw9d3d/best_costeffective_way_to_write_lowvolume/)**
*  **Summary:** Seeking advice on the most cost-effective method for writing low-volume Confluent Kafka topics as Delta/Iceberg in Azure, comparing different approaches like Structured Streaming.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    * Writing a simple Python service might be faster than sourcing a solution.
    * Set structured streaming to use AvailableNow trigger.

**[A conversational feed of real time market data (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lwj3hx/a_conversational_feed_of_real_time_market_data/)**
*  **Summary:** The thread points to open-source project showcases.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    *  The thread is a pointer to community projects.

**[Free timestamp to code converter (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lwl0oz/free_timestamp_to_code_converter/)**
*  **Summary:** The thread points to open-source project showcases and raises questions about the need for a timestamp to code converter.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top Points of View:**
    * The thread is a pointer to community projects.
    * Asks about use case and whether the service is really needed.
