---
title: "Data Engineering Subreddit"
date: "2025-10-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "SQL", "GCP"]
---

# Overall Ranking and Top Discussions

1.  [[D] DataGrip Is Now Free for Non-Commercial Use](https://blog.jetbrains.com/datagrip/2025/10/01/datagrip-is-now-free-for-non-commercial-use/) (Score: 124)
    * The thread discusses the recent announcement that DataGrip is now free for non-commercial use and users are sharing their experiences and comparing it with other SQL IDEs.

2.  [Dealing with metadata chaos across catalogs — what’s actually working?](https://www.reddit.com/r/dataengineering/comments/1ohqjar/dealing_with_metadata_chaos_across_catalogs_whats/) (Score: 47)
    * The thread discusses the challenges of managing metadata across different data catalogs and tools, and potential solutions like OpenMetadata and Unity Catalog.

3.  [going all in on GCP, why not? is a hybrid stack better?](https://www.reddit.com/r/dataengineering/comments/1ohrt4e/going_all_in_on_gcp_why_not_is_a_hybrid_stack/) (Score: 18)
    * The thread discusses the pros and cons of going all-in on Google Cloud Platform (GCP) for data engineering, compared to a hybrid stack.

4.  [Your internal engineering knowledge base that writes and updates itself from your GitHub repos](https://v.redd.it/8ufz9srd2qxf1) (Score: 11)
    *  The thread discusses an internal engineering knowledge base that writes and updates itself from GitHub repos.

5.  [Are DE jobs moving?](https://www.reddit.com/r/dataengineering/comments/1oieor6/are_de_jobs_moving/) (Score: 8)
    *  The thread discusses the trend of data engineering jobs being offshored to countries with lower labor costs.

6.  [Moving away Glue jobs to Snowflake](https://www.reddit.com/r/dataengineering/comments/1ohz0ai/moving_away_glue_jobs_to_snowflake/) (Score: 7)
    *  The thread discusses strategies for migrating data and ETL processes from AWS Glue to Snowflake.

7.  [Building ADF via Terraform](https://www.reddit.com/r/dataengineering/comments/1ohwq97/building_adf_via_terraform/) (Score: 4)
    *  The thread discusses the challenges and alternatives to building Azure Data Factory (ADF) pipelines using Terraform.

8.  [What's the documentation that has facts across the top and dimensions across the side with X's for intersections](https://www.reddit.com/r/dataengineering/comments/1oie75u/whats_the_documentation_that_has_facts_across_the/) (Score: 2)
    *  The thread asks for the name of a type of documentation that has facts across the top and dimensions across the side.

9.  [Migrating from Spreadsheets to PostgreSQL](https://www.reddit.com/r/dataengineering/comments/1oif45q/migrating_from_spreadsheets_to_postgresql/) (Score: 2)
    * The thread discusses the process and tools involved in migrating data from spreadsheets to a PostgreSQL database.

10. [Looking for ETL tool recommendations for integrating with these apps (all have APIs)](https://www.reddit.com/r/dataengineering/comments/1oiivs8/looking_for_etl_tool_recommendations_for/) (Score: 2)
    * The thread asks for ETL tools recommendations for integrating with applications using APIs.

11. [How to build real-time user-facing analytics with Kafka + Flink + Doris](https://www.reddit.com/r/dataengineering/comments/1oii80y/how_to_build_realtime_userfacing_analytics_with/) (Score: 1)
    * The thread discusses how to build real-time user-facing analytics with Kafka, Flink, and Doris.

12. [Syncing Data from Redshift SQL DB to Snowflane](https://www.reddit.com/r/dataengineering/comments/1oicqfv/syncing_data_from_redshift_sql_db_to_snowflane/) (Score: 0)
    * The thread discusses ways to sync data from Redshift SQL DB to Snowflake.

13. [We built GoMask for test data management - launched last week](https://www.reddit.com/r/dataengineering/comments/1oi8spz/we_built_gomask_for_test_data_management_launched/) (Score: 0)
    * The thread is a showcase for GoMask, a new tool for test data management.

14. [Java](https://www.reddit.com/r/dataengineering/comments/1oieqhi/java/) (Score: 0)
    * The thread discusses the importance of software engineering principles in data engineering.

15. [Making BigQuery pipelines easier (and cleaner) with Dataform](https://www.reddit.com/r/dataengineering/comments/1oihozf/making_bigquery_pipelines_easier_and_cleaner_with/) (Score: 0)
    * The thread discusses using Dataform to make BigQuery pipelines easier and cleaner.

# Detailed Analysis by Thread

**[[D] DataGrip Is Now Free for Non-Commercial Use (Score: 124)](https://blog.jetbrains.com/datagrip/2025/10/01/datagrip-is-now-free-for-non-commercial-use/)**
*   **Summary:**  The thread discusses the recent announcement that DataGrip is now free for non-commercial use. Users are sharing their experiences with the tool and comparing it with alternatives like Dbeaver and PyCharm. Many are excited about the free offering for hobby projects.
*   **Emotion:** The emotional tone is predominantly positive. Many users express excitement and gratitude about the new free offering. Some users are neutral, asking questions about DataGrip's features or comparing it to other tools.
*   **Top 3 Points of View:**
    *   DataGrip is a fantastic SQL IDE and is highly recommended.
    *   The price of DataGrip was previously too high for personal use, making the free version welcome.
    *   Users are comparing DataGrip with tools like Dbeaver and PyCharm to understand the benefits of each.

**[Dealing with metadata chaos across catalogs — what’s actually working? (Score: 47)](https://www.reddit.com/r/dataengineering/comments/1ohqjar/dealing_with_metadata_chaos_across_catalogs_whats/)**
*   **Summary:** The thread discusses the problem of managing metadata across various data catalogs and tools. Users are sharing their experiences and discussing potential solutions, including open-source tools like OpenMetadata and DataHub, as well as cloud-based solutions like Unity Catalog. The discussion also touches on the challenges of balancing governance and agility.
*   **Emotion:** The overall emotional tone is neutral and informative. Users are sharing their experiences and discussing different solutions in a professional manner.  There is also a hint of negativity regarding the complexity of the problem.
*   **Top 3 Points of View:**
    *   Open source tools like OpenMetadata and DataHub are effective for federating metadata across different systems without vendor lock-in.
    *   Unity Catalog is a good option, especially for Databricks users, and its open-source nature limits lock-in.
    *   A single, central metastore per cluster or data lake is preferable to a federated metastore to avoid data quality issues.

**[going all in on GCP, why not? is a hybrid stack better? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1ohrt4e/going_all_in_on_gcp_why_not_is_a_hybrid_stack/)**
*   **Summary:** The thread discusses the considerations and potential benefits/drawbacks of adopting Google Cloud Platform (GCP) exclusively for data engineering tasks, compared to a hybrid approach.  Users share their experiences and recommendations for tools and architectures within GCP.
*   **Emotion:** The thread's emotional tone is mainly neutral and practical, with users offering advice and sharing their experiences. Some comments express a positive sentiment towards GCP.
*   **Top 3 Points of View:**
    *   Using Cloud Composer, BigQuery, and dbt Core on Cloud Run is a viable and effective stack for data engineering on GCP.
    *   For batch loads, BigQuery and Dataflow are sufficient, and Fivetran can be too expensive.
    *   Hybrid-capable platforms like SSIS should not be abandoned for cloud-only platforms due to vendor lock-in concerns.

**[Your internal engineering knowledge base that writes and updates itself from your GitHub repos (Score: 11)](https://v.redd.it/8ufz9srd2qxf1)**
*   **Summary:**  The thread discusses an internal engineering knowledge base that automatically generates and updates documentation from GitHub repositories.
*   **Emotion:** The overall emotional tone is neutral. There's curiosity about the knowledge base and how it works. Some comments express a bit of skepticism about the existence of documentation.
*   **Top 3 Points of View:**
    *   The knowledge base is interesting and potentially useful.
    *   Question about finding the right document and section to update.
    *   Skepticism about the existence of documentation.

**[Are DE jobs moving? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1oieor6/are_de_jobs_moving/)**
*   **Summary:**  The thread discusses the trend of data engineering jobs being offshored to countries with lower labor costs.  Users share their experiences and opinions on the topic, including the impact on job security and potential strategies for navigating the changing job market.
*   **Emotion:** The overall emotional tone is negative to neutral, with concerns about job security and the impact of offshoring.
*   **Top 3 Points of View:**
    *   Data engineering jobs are increasingly being offshored to cheaper countries.
    *   Offshoring can lead to management and miscommunication overhead, potentially negating cost savings.
    *   Working for private businesses (rather than corporations) might reduce the risk of offshoring.

**[Moving away Glue jobs to Snowflake (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ohz0ai/moving_away_glue_jobs_to_snowflake/)**
*   **Summary:**  The thread discusses strategies for migrating data and ETL processes from AWS Glue to Snowflake. Users are providing advice on efficient data ingestion and transformation techniques.
*   **Emotion:** The thread exhibits a neutral and helpful tone, with users offering solutions and best practices.
*   **Top 3 Points of View:**
    *   For efficient data ingestion, avoid Python scripts for large volumes. Instead, use dedicated tools like Fivetran or load data from cloud storage using COPY INTO.
    *   To extract data and load to your table, you can just use a custom JDBC connection.
    *   Use Glue jobs to store data as iceberg table format then register it to snowflake.

**[Building ADF via Terraform (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ohwq97/building_adf_via_terraform/)**
*   **Summary:** The thread discusses the use of Terraform for building Azure Data Factory (ADF) pipelines. Users share their experiences and suggest alternative approaches, such as using Azure DevOps and YAML-based deployments.
*   **Emotion:** The emotional tone is mixed, with some users expressing reservations about using Terraform for ADF.
*   **Top 3 Points of View:**
    *   Using PowerShell with ADF is recommended over Terraform.
    *   Azure DevOps and YAML deployments are better suited for managing ADF releases.
    *   Using Terraform for this may not be the best approach.

**[What's the documentation that has facts across the top and dimensions across the side with X's for intersections (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oie75u/whats_the_documentation_that_has_facts_across_the/)**
*   **Summary:** The thread asks for the name of a type of documentation that has facts across the top and dimensions across the side with X's for intersections.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Bus Matrix
    *   Dimension Matrix

**[Migrating from Spreadsheets to PostgreSQL (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oif45q/migrating_from_spreadsheets_to_postgresql/)**
*   **Summary:** The thread discusses the process and tools involved in migrating data from spreadsheets to a PostgreSQL database.
*   **Emotion:** The emotional tone is positive and helpful, with suggestions on how to start.
*   **Top 3 Points of View:**
    *   Start with DBeaver + SQLite.
    *   Strictly use people info table and class info table.

**[Looking for ETL tool recommendations for integrating with these apps (all have APIs) (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oiivs8/looking_for_etl_tool_recommendations_for/)**
*   **Summary:** The thread asks for ETL tools recommendations for integrating with applications using APIs.
*   **Emotion:** The emotional tone is negative with the user saying "Low code ETL sounds terrifying".
*   **Top 3 Points of View:**
    *   Low code ETL is terrifying

**[How to build real-time user-facing analytics with Kafka + Flink + Doris (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1oii80y/how_to_build_realtime_userfacing_analytics_with/)**
*   **Summary:** The thread discusses how to build real-time user-facing analytics with Kafka, Flink, and Doris.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   User thinks the title could have been generated from a LLM prompt.
    *   There is so much stuff in DE.

**[Syncing Data from Redshift SQL DB to Snowflane (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oicqfv/syncing_data_from_redshift_sql_db_to_snowflane/)**
*   **Summary:** The thread discusses ways to sync data from Redshift SQL DB to Snowflake.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Airbyte maybe
    *   The poster recommends using ingestr.

**[We built GoMask for test data management - launched last week (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oi8spz/we_built_gomask_for_test_data_management_launched/)**
*   **Summary:** The thread is a showcase for GoMask, a new tool for test data management.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   No distinct viewpoints in the discussion; the post is just a showcase.

**[Java (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oieqhi/java/)**
*   **Summary:** The thread discusses the importance of software engineering principles in data engineering.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Good data engineering is based on SWE

**[Making BigQuery pipelines easier (and cleaner) with Dataform (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oihozf/making_bigquery_pipelines_easier_and_cleaner_with/)**
*   **Summary:** The thread discusses using Dataform to make BigQuery pipelines easier and cleaner.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   No distinct viewpoints in the discussion; the post links to learning resources.
