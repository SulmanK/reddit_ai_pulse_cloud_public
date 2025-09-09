---
title: "Data Engineering Subreddit"
date: "2025-07-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "airflow", "data pipelines"]
---

# Overall Ranking and Top Discussions
1.  [[D] Anyone switched from Airflow to low-code data pipeline tools?](https://www.reddit.com/r/dataengineering/comments/1m3tswv/anyone_switched_from_airflow_to_lowcode_data/) Score: 41
    * Discussing the transition from Airflow to low-code data pipeline tools, addressing challenges with Airflow and exploring alternatives like Integrate.io, Dagster, and Prefect.
2.  [In Your Data Platform, Do You Wait for All Sources Before Running Transformations, or Run Isolated Pipelines?](https://www.reddit.com/r/dataengineering/comments/1m3oadd/in_your_data_platform_do_you_wait_for_all_sources/) Score: 9
    * Discussing whether to wait for all data sources before running transformations or to run isolated pipelines.
3.  [Why SQL Partitioning Matters: The Hidden Superpower Behind Fast, Scalable Databases](https://www.reddit.com/r/dataengineering/comments/1m3ox68/why_sql_partitioning_matters_the_hidden/) Score: 9
    * Discussing SQL partitioning and its impact on database performance.
4.  [Opinions on OpenMetadata?](https://www.reddit.com/r/dataengineering/comments/1m42t0u/opinions_on_openmetadata/) Score: 7
    * Discussing opinions and experiences with OpenMetadata as a data catalog tool.
5.  [Natural Language Database Catalog Tool](https://www.reddit.com/r/dataengineering/comments/1m3ohg0/natural_language_database_catalog_tool/) Score: 5
    * Showcasing open-source projects related to natural language database catalog tools.
6.  [Need help building a chatbot for scanned documents](https://www.reddit.com/r/dataengineering/comments/1m3seuq/need_help_building_a_chatbot_for_scanned_documents/) Score: 4
    * Seeking advice on building a chatbot for scanned documents.
7.  [Looking for DAMA Mock Exams](https://www.reddit.com/r/dataengineering/comments/1m431pa/looking_for_dama_mock_exams/) Score: 3
    * Looking for resources for DAMA mock exams.
8.  [How to update realtime serving store from Databricks DLT](https://www.reddit.com/r/dataengineering/comments/1m3o411/how_to_update_realtime_serving_store_from/) Score: 2
    * Discussing how to update a real-time serving store from Databricks DLT.
9.  [Help needed regarding data transfer from BigQuery to snowflake.](https://www.reddit.com/r/dataengineering/comments/1m3qucs/help_needed_regarding_data_transfer_from_bigquery/) Score: 2
    * Seeking help regarding data transfer from BigQuery to Snowflake.
10. [S3 Iceberg table to Datawarehouse](https://www.reddit.com/r/dataengineering/comments/1m3vvwm/s3_iceberg_table_to_datawarehouse/) Score: 2
    * Discussing the use of S3 Iceberg tables and data warehouses, including alternatives to Redshift.
11. [Adding to on premise SQL Server process](https://www.reddit.com/r/dataengineering/comments/1m44d5t/adding_to_on_premise_sql_server_process/) Score: 2
    * Seeking advice on adding to an on-premise SQL Server process.
12. [Anyone modernized their aws data pipelines? What did you go for?](https://www.reddit.com/r/dataengineering/comments/1m458fs/anyone_modernized_their_aws_data_pipelines_what/) Score: 1
    * Asking about experiences modernizing AWS data pipelines.
13. [Fake relational data](https://mocksmith.dev) Score: 0
    * Providing feedback on a tool for generating fake relational data.
14. [Is data engineering right for me?](https://www.reddit.com/r/dataengineering/comments/1m3x0fe/is_data_engineering_right_for_me/) Score: 0
    * Discussing whether data engineering is the right career path.

# Detailed Analysis by Thread
**[[D] Anyone switched from Airflow to low-code data pipeline tools? (Score: 41)](https://www.reddit.com/r/dataengineering/comments/1m3tswv/anyone_switched_from_airflow_to_lowcode_data/)**
*   **Summary:** The thread discusses the challenges of using Airflow for data pipeline orchestration and the exploration of low-code/no-code alternatives. Users share experiences with tools like Integrate.io, Dagster, Prefect, and Azure Data Factory, highlighting the benefits and drawbacks of each. The discussion includes topics such as pipeline ownership, separating concerns, CI/CD, and the trade-offs between custom-coded solutions and low-code platforms.
*   **Emotion:** The overall emotional tone is Neutral. While some comments express frustration with Airflow, the majority offer objective advice and share their experiences with different tools. A single comment expressed "Positive" sentiment for Airbyte.
*   **Top 3 Points of View:**
    *   Airflow can become difficult to manage and scale when marketing and product teams need more pipelines, leading to exploration of low-code alternatives.
    *   Low-code tools like Integrate.io can empower non-engineers to build pipelines through a UI, but may require trade-offs in terms of control and customization.
    *   Dagster and Prefect are good middle ground options because they still use Python but are more structured.

**[In Your Data Platform, Do You Wait for All Sources Before Running Transformations, or Run Isolated Pipelines? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1m3oadd/in_your_data_platform_do_you_wait_for_all_sources/)**
*   **Summary:** This thread discusses the strategy of waiting for all data sources before running transformations versus running isolated pipelines in a data platform. Users share their approaches, emphasizing that the best approach is often case-by-case and depends on factors such as SLAs, dependencies, and available tools like Databricks DLT.
*   **Emotion:** The emotional tone is primarily Neutral, with users offering practical advice and sharing their experiences.
*   **Top 3 Points of View:**
    *   The best approach is case-by-case, depending on SLAs and dependencies.
    *   Running isolated pipelines is preferable to avoid orchestration bottlenecks and enable faster reruns.
    *   Tools like Databricks DLT can help manage dependencies and data flows.

**[Why SQL Partitioning Matters: The Hidden Superpower Behind Fast, Scalable Databases (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1m3ox68/why_sql_partitioning_matters_the_hidden/)**
*   **Summary:** This thread is about an article on SQL partitioning. Users comment on the article's quality and suggest improvements, such as adding DML scripts for real-world examples to enhance clarity.
*   **Emotion:** The emotional tone is mostly Positive, with users praising the article.
*   **Top 3 Points of View:**
    *   The article is well-written.
    *   Adding DML scripts would improve clarity and value.
    *   The image in the article is confusing.

**[Opinions on OpenMetadata? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m42t0u/opinions_on_openmetadata/)**
*   **Summary:** The thread asks for opinions on OpenMetadata, a data catalog tool. Users generally have positive experiences, citing its flexibility and customizability, but note potential issues with the OSS version and MySQL backend.
*   **Emotion:** The emotional tone is generally Positive, with users sharing their favorable experiences with OpenMetadata.
*   **Top 3 Points of View:**
    *   OpenMetadata is a great tool with a lot of flexibility and is easy to extend.
    *   The OSS version may have some issues, particularly with MySQL backend.
    *   Lineage tracking is easily customizable.

**[Natural Language Database Catalog Tool (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1m3ohg0/natural_language_database_catalog_tool/)**
*   **Summary:** This thread is a showcase of an open-source project, with a bot providing links to the dataengineering.wiki and an Airtable form for project submissions.
*   **Emotion:** The emotional tone is Neutral. It is a bot posting links.
*   **Top 3 Points of View:**
    *   Open-source project showcase can be found at: https://dataengineering.wiki/Community/Projects
    *   Projects can be submitted for featuring at: https://airtable.com/appDgaRSGl09yvjFj/pagmImKixEISPcGQz/form
    *   The post is automated and handled by a bot.

**[Need help building a chatbot for scanned documents (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1m3seuq/need_help_building_a_chatbot_for_scanned_documents/)**
*   **Summary:** This thread is about seeking help and ideas for building a chatbot for scanned documents. Users suggest extracting specific information to a database and using LLMs for classification and indexing, as well as offering collaboration.
*   **Emotion:** The overall emotional tone is Positive, driven by users expressing excitement and offering assistance.
*   **Top 3 Points of View:**
    *   Extract specific standardized information from each PDF to a database.
    *   Use LLMs to detect and classify project locations, sizes, and costs.
    *   Collaboration can be beneficial in solving this problem.

**[Looking for DAMA Mock Exams (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m431pa/looking_for_dama_mock_exams/)**
*   **Summary:** This thread involves a user looking for DAMA mock exams, with a suggestion to check a specific YouTube channel and website.
*   **Emotion:** The emotional tone is Neutral with the comment sharing links.
*   **Top 3 Points of View:**
    *   Check the YT channel: https://m.youtube.com/@datastrategypros
    *   Check LinkedIn for more resources.
    *   Check the site: https://www.datastrategypros.com/

**[How to update realtime serving store from Databricks DLT (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m3o411/how_to_update_realtime_serving_store_from/)**
*   **Summary:** The thread discusses updating a real-time serving store from Databricks DLT, suggesting using the Databricks JDBC connector to write directly to Postgres with SCD Type 2 merge logic.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Use Databricks JDBC connector.
    *   Write directly from DLT to Postgres.
    *   Use SCD Type 2 merge logic to handle updates.

**[Help needed regarding data transfer from BigQuery to snowflake. (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m3qucs/help_needed_regarding_data_transfer_from_bigquery/)**
*   **Summary:** This thread is about transferring data from BigQuery to Snowflake. Users offer several suggestions, including using GCP Cloud Storage with Snowpipe, Python with dlt, Estuary, and leveraging Google Analytics connectors.
*   **Emotion:** The emotional tone is Positive to Neutral, with users offering helpful suggestions and promoting their solutions.
*   **Top 3 Points of View:**
    *   Use GCP Cloud Storage with Snowpipe.
    *   Use Python with dlt or Sling.
    *   Check out Estuary for setting up a data flow.

**[S3 Iceberg table to Datawarehouse (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m3vvwm/s3_iceberg_table_to_datawarehouse/)**
*   **Summary:** This thread discusses using S3 Iceberg tables with data warehouses. A user recommends using Trino over Redshift for read-only workflows, citing significant performance improvements.
*   **Emotion:** The emotional tone is Positive with the user sharing how much better the workflow performs with Trino.
*   **Top 3 Points of View:**
    *   Redshift is not ideal for everything.
    *   Trino is great for read-only workflows on Iceberg data lakes.
    *   Trino offers significantly better query performance compared to Athena.

**[Adding to on premise SQL Server process (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m44d5t/adding_to_on_premise_sql_server_process/)**
*   **Summary:** The thread discusses adding to an on-premise SQL Server process, questioning the need for different tooling when SSIS already provides the required functionality.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   SSIS already provides transformation functionality out of the box.
    *   Using different tooling may not address the listed issues.

**[Anyone modernized their aws data pipelines? What did you go for? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1m458fs/anyone_modernized_their_aws_data_pipelines_what/)**
*   **Summary:** This thread asks about experiences modernizing AWS data pipelines, with a user questioning the query patterns that lead to cost increases.
*   **Emotion:** The emotional tone is Neutral, with the comment asking for more details about the queries.
*   **Top 3 Points of View:**
    *   Question about the types of queries causing monthly cost increases.
    *   Concern about querying the entire dataset in S3.

**[Fake relational data (Score: 0)](https://mocksmith.dev)**
*   **Summary:** Providing feedback on a tool for generating fake relational data. Users comment that the tool is too difficult to use and that the same can be done with Python.
*   **Emotion:** The emotional tone is Positive.
*   **Top 3 Points of View:**
    *   The tool is too rough to use.
    *   There's too much button clicking.
    *   The same can be done with Python code or an LLM.

**[Is data engineering right for me? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1m3x0fe/is_data_engineering_right_for_me/)**
*   **Summary:** Discussing whether data engineering is the right career path. Users express that data engineering involves solving "data puzzles" and working with domain experts to achieve goals.
*   **Emotion:** The emotional tone is Positive.
*   **Top 3 Points of View:**
    *   Data engineering is for those that enjoy fixing, automating and preventing data issues.
    *   Data engineering is consulting side and developer side.
    *   Data engineering depends on the tools and if you don't care for the business side.
