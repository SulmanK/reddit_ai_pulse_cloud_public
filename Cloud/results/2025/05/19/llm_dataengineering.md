---
title: "Data Engineering Subreddit"
date: "2025-05-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ETL", "data pipelines"]
---

# Overall Ranking and Top Discussions
1. [[D] New Parquet writer allows easy insert/delete/edit](https://www.reddit.com/r/dataengineering/comments/1kqb50f/new_parquet_writer_allows_easy_insertdeleteedit/) (Score: 57)
    * Discusses a new Parquet writer feature and how it handles concurrent read/write operations and integration with delta tables.
2.  [real time CDC into OLAP](https://www.reddit.com/r/dataengineering/comments/1kq6wd3/real_time_cdc_into_olap/) (Score: 13)
    * Discusses using Spark streaming and Flink for Change Data Capture (CDC) into Online Analytical Processing (OLAP) systems, with a focus on ease of use and alternatives.
3.  [How to practice debugging data pipeline](https://www.reddit.com/r/dataengineering/comments/1kq0b4x/how_to_practice_debugging_data_pipeline/) (Score: 10)
    * Discusses practicing debugging data pipelines using commands like awk, sed, grep, and cut to identify data quality issues.
4.  [Am I doing it right? I feel a little lost transitioning into Data Engineering](https://www.reddit.com/r/dataengineering/comments/1kqjuap/am_i_doing_it_right_i_feel_a_little_lost/) (Score: 9)
    * Discusses the transition into data engineering, evaluating current skillsets and offering encouragement and resources.
5.  [CI/CD with Airflow](https://www.reddit.com/r/dataengineering/comments/1kqanms/cicd_with_airflow/) (Score: 7)
    * Discusses various approaches to CI/CD with Airflow, including git sync, Bitbucket pipelines, Ansible scripts, and the use of monorepos.
6.  [Data Analyst transitioning to Data Engineer](https://www.reddit.com/r/dataengineering/comments/1kqh82y/data_analyst_transitioning_to_data_engineer/) (Score: 6)
    * Discusses the transition from data analyst to data engineer, including technical requirements, market trends, and potential automation risks.
7.  [Fivetran Managed Data Lake - GCS and BigQuery External Tables](https://www.reddit.com/r/dataengineering/comments/1kpwg8x/fivetran_managed_data_lake_gcs_and_bigquery/) (Score: 5)
    * Discusses the Fivetran Managed Data Lake Service and its ability to automatically register tables in BigQuery metastore.
8.  [Anyone found a good ETL tool for syncing Salesforce data without needing dev help?](https://www.reddit.com/r/dataengineering/comments/1kqcuz1/anyone_found_a_good_etl_tool_for_syncing/) (Score: 5)
    * Discusses ETL tools for syncing Salesforce data without needing development help, recommending tools like AWS AppFlow, Fivetran, and BigQuery Data Transfer.
9.  [Any alternative to SMS parsing on iOS for extracting periodic transactional data?](https://www.reddit.com/r/dataengineering/comments/1kq9gej/any_alternative_to_sms_parsing_on_ios_for/) (Score: 3)
    * A bot shares a community-submitted learning resources link to help with the extraction of periodic transactional data from SMS on iOS.
10. [Snowflake summit 2025 After party](https://www.reddit.com/r/dataengineering/comments/1kqeans/snowflake_summit_2025_after_party/) (Score: 2)
    * A thread pointing out that the Summit referenced Vegas and not SF.
11. [SAP BDC imlelemntation](https://www.reddit.com/r/dataengineering/comments/1kqf8bn/sap_bdc_imlelemntation/) (Score: 1)
    * Discusses implementing SAP BDC and suggests exporting SAP data to flat files for ingestion into Delta Lake.
12. [Feedbacks on my Open Project - QuickELT](https://www.reddit.com/r/dataengineering/comments/1kqj32s/feedbacks_on_my_open_project_quickelt/) (Score: 1)
    * Discusses an open-source ELT project, QuickELT, with suggestions for improvement, including using dlt or adding a dbt runner.

# Detailed Analysis by Thread
**[ [D] New Parquet writer allows easy insert/delete/edit (Score: 57)](https://www.reddit.com/r/dataengineering/comments/1kqb50f/new_parquet_writer_allows_easy_insertdeleteedit/)**
*  **Summary:** A discussion about a new Parquet writer that enables easy insert/delete/edit operations. Users are curious about how the feature handles concurrent read/write operations and its potential integration with Delta tables.
*  **Emotion:** The overall emotional tone is positive, with some neutral inquiries.
*  **Top 3 Points of View:**
    * The feature is a welcome addition.
    * Concern about concurrent read/write handling.
    * Interest in its potential use with Delta tables.

**[real time CDC into OLAP (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1kq6wd3/real_time_cdc_into_olap/)**
*  **Summary:** This thread discusses using Spark Streaming and Flink for real-time Change Data Capture (CDC) into OLAP systems. Users share their experiences and preferences for different tools and approaches.
*  **Emotion:** The overall emotional tone is neutral, with a focus on technical discussions and sharing information.
*  **Top 3 Points of View:**
    * Spark Streaming with longer trigger intervals is a viable approach.
    * Flink-CDC is easy to use as it doesn't require Kafka and Debezium.
    * ConduitIO is a lightweight alternative for mixing and matching source and destination connectors.

**[How to practice debugging data pipeline (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1kq0b4x/how_to_practice_debugging_data_pipeline/)**
*  **Summary:** The thread discusses how to effectively practice debugging data pipelines. The consensus revolves around mastering command-line tools and deliberately introducing errors into datasets.
*  **Emotion:** The overall emotional tone is neutral and helpful.
*  **Top 3 Points of View:**
    * Mastering commands like awk, sed, grep, and cut is crucial.
    * Deliberately introduce errors into datasets to practice debugging.
    * A systematic approach to isolating problems is efficient.

**[Am I doing it right? I feel a little lost transitioning into Data Engineering (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1kqjuap/am_i_doing_it_right_i_feel_a_little_lost/)**
*  **Summary:** This thread addresses concerns about transitioning into data engineering. Users receive encouragement and resources to aid their journey.
*  **Emotion:** The overall emotional tone is positive and supportive.
*  **Top 3 Points of View:**
    * The poster's background is beyond entry-level.
    * Implementing technologies is only half the battle; understanding when and where to use them is also important.
    * Community guides and learning resources are helpful.

**[CI/CD with Airflow (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kqanms/cicd_with_airflow/)**
*  **Summary:** This thread explores various methods for implementing CI/CD with Airflow. The discussion includes using git sync, Bitbucket pipelines, Ansible scripts, and the potential benefits of a monorepo.
*  **Emotion:** The overall emotional tone is neutral to positive, with a focus on sharing practical advice and experiences.
*  **Top 3 Points of View:**
    * Git sync is easy to set up with Bitnami's Helm chart.
    * A monorepo approach is recommended for Airflow DAGs instead of git submodules.
    * Ansible scripts can be used to create a CI/CD pipeline to sync GitLab code with Airflow.

**[Data Analyst transitioning to Data Engineer (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kqh82y/data_analyst_transitioning_to_data_engineer/)**
*  **Summary:** The discussion revolves around the transition from a data analyst role to a data engineer position. It covers technical requirements, market conditions, and potential automation threats.
*  **Emotion:** The emotional tone is largely neutral, with some positivity regarding career prospects and some concern about automation.
*  **Top 3 Points of View:**
    * The technical requirements for data engineering can vary greatly.
    * The market for data engineers is up and down, but salaries are typically better.
    * Both data analysts and data engineers are equally likely to be affected by AI automation.

**[Fivetran Managed Data Lake - GCS and BigQuery External Tables (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kpwg8x/fivetran_managed_data_lake_gcs_and_bigquery/)**
*  **Summary:** This thread focuses on Fivetran's Managed Data Lake Service and its capabilities in registering tables in BigQuery metastore and keeping metadata up to date automatically.
*  **Emotion:** The thread has a positive emotional tone, with the Fivetran PM expressing enthusiasm and helpfulness.
*  **Top 2 Points of View:**
    * The Managed Data Lake Service automates table registration in BigQuery.
    * Users are encouraged to open support tickets for assistance.

**[Anyone found a good ETL tool for syncing Salesforce data without needing dev help? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kqcuz1/anyone_found_a_good_etl_tool_for_syncing/)**
*  **Summary:** This thread asks for recommendations for ETL tools that can sync Salesforce data without requiring developer assistance. Various tools and approaches are suggested.
*  **Emotion:** The overall tone is generally positive and helpful, with users sharing their experiences and recommendations.
*  **Top 3 Points of View:**
    * AWS AppFlow is a good option for non-technical users.
    * Fivetran is considered a good option.
    * BigQuery Data Transfer for Salesforce is easy to set up within BigQuery.

**[Any alternative to SMS parsing on iOS for extracting periodic transactional data? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kq9gej/any_alternative_to_sms_parsing_on_ios_for/)**
*   **Summary:** This thread asks about alternatives to SMS parsing on iOS for extracting periodic transactional data. A bot posted a resource.
*   **Emotion:** Neutral
*   **Top 1 Points of View:**
    * Use community learning resources.

**[Snowflake summit 2025 After party (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kqeans/snowflake_summit_2025_after_party/)**
*   **Summary:** A thread pointing out that the Summit referenced Vegas and not SF.
*   **Emotion:** Neutral
*   **Top 1 Points of View:**
    * The Snowflake Summit location might be incorrect.

**[SAP BDC imlelemntation (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kqf8bn/sap_bdc_imlelemntation/)**
*   **Summary:** Discussion about SAP BDC Implementation
*   **Emotion:** Neutral
*   **Top 1 Points of View:**
    * Extract SAP data into flat files for Delta Lake ingestion if not using SAP's Databricks implementation.

**[Feedbacks on my Open Project - QuickELT (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kqj32s/feedbacks_on_my_open_project_quickelt/)**
*   **Summary:** Discussions about an open-source ELT project, QuickELT.
*   **Emotion:** Neutral
*   **Top 1 Points of View:**
    *  Consider using dlt or adding a dbt runner for improved functionality.
