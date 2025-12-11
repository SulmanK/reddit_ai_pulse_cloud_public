---
title: "Data Engineering Subreddit"
date: "2025-11-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Got to process 2m+ files (S3) - any tips?](https://www.reddit.com/r/dataengineering/comments/1p8se1b/got_to_process_2m_files_s3_any_tips/) (Score: 19)
    *   This thread discusses tips and strategies for processing a large number of files (2 million+) stored in Amazon S3.
2.  [Pivot from dev to data engineering](https://www.reddit.com/r/dataengineering/comments/1p8wmlv/pivot_from_dev_to_data_engineering/) (Score: 12)
    *   This thread explores the similarities and differences between development and data engineering roles, including potential stressors and required skills.
3.  [Airflow dag task stuck in queued state even if dag is running](https://www.reddit.com/r/dataengineering/comments/1p8h2eh/airflow_dag_task_stuck_in_queued_state_even_if/) (Score: 9)
    *   This thread seeks help on resolving an issue where an Airflow DAG task remains stuck in a queued state despite the DAG running.
4.  [Specialising on fabric, worth it or waste of time?](https://www.reddit.com/r/dataengineering/comments/1p8rapv/specialising_on_fabric_worth_it_or_waste_of_time/) (Score: 6)
    *   This thread discusses the pros and cons of specializing in Microsoft Fabric, considering its potential market value and comparing it with other technologies like Databricks and Snowflake.
5.  [Which paid tool is better for database CI/CD with MSSQL / MySQL — Liquibase or Bytebase?](https://www.reddit.com/r/dataengineering/comments/1p8rcar/which_paid_tool_is_better_for_database_cicd_with/) (Score: 6)
    *   This thread compares Liquibase and Bytebase for database CI/CD, focusing on their strengths and weaknesses in different scenarios, particularly with MSSQL and MySQL.
6.  [DE managing my own database?](https://www.reddit.com/r/dataengineering/comments/1p8f3lu/de_managing_my_own_database/) (Score: 5)
    *   This thread addresses the scenario of a data engineer managing their own database, discussing the challenges, responsibilities, and alternatives, particularly when facing resistance from traditional DBAs.
7.  [Phased Databricks migration](https://www.reddit.com/r/dataengineering/comments/1p8t368/phased_databricks_migration/) (Score: 5)
    *   This thread discusses strategies for a phased migration to Databricks, including advice on setting up Unity Catalog, Delta Lake, and Autoloader.
8.  [What job title would be appropriate for my situation](https://www.reddit.com/r/dataengineering/comments/1p8txqx/what_job_title_would_be_appropriate_for_my/) (Score: 5)
    *   This thread discusses suitable job titles for a person in a data-related role, considering the need for a standard, high-level title for leveraging future opportunities.
9.  [Is this an use case for Lambda Views/Architecture? How to handle realtime data models](https://www.reddit.com/r/dataengineering/comments/1p8k8kd/is_this_an_use_case_for_lambda_viewsarchitecture/) (Score: 4)
    *   This thread discusses whether the poster's specific problem is an use case for Lambda Views/Architecture and asks for advice on how to handle realtime data models.
10. [Ingestion and storage 101 - Can someone give me some tips?](https://www.reddit.com/r/dataengineering/comments/1p8yd8z/ingestion_and_storage_101_can_someone_give_me/) (Score: 3)
    *   This thread seeks advice on ingestion and storage strategies, particularly in the context of using Azure Data Factory (ADF) and Power BI.
11. [Declarative data processing for "small data"?](https://www.reddit.com/r/dataengineering/comments/1p8ew4k/declarative_data_processing_for_small_data/) (Score: 2)
    *   This thread explores declarative data processing approaches for smaller datasets.
12. [DATAOPS TOOLS: bruin core Vs. dbtran = fivetran + dbt core](https://www.reddit.com/r/dataengineering/comments/1p8zgpr/dataops_tools_bruin_core_vs_dbtran_fivetran_dbt/) (Score: 2)
    *   This thread discusses and compares different DataOps tools.
13. [Delta Sharing Protocol](https://www.reddit.com/r/dataengineering/comments/1p8tjav/delta_sharing_protocol/) (Score: 1)
    *   This thread discusses the Delta Sharing Protocol.
14. [Is there a "middleware" missing between Terraform and Agentic workflows?](https://www.reddit.com/r/dataengineering/comments/1p94m7p/is_there_a_middleware_missing_between_terraform/) (Score: 0)
    *   This thread asks about the need for a middleware between Terraform and Agentic workflows.

# Detailed Analysis by Thread
**[ Got to process 2m+ files (S3) (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1p8se1b/got_to_process_2m_files_s3_any_tips/)**
*   **Summary:** The thread is about seeking advice on how to efficiently process a large number of files (2 million+) stored in Amazon S3. Users suggest various approaches, from using AWS Lambda with SQS, Apache Spark, and Docker containers to simpler methods involving parallel processing and local file manipulation.
*   **Emotion:** The overall emotional tone is Neutral, as users are primarily sharing technical advice and solutions. There is a hint of positivity in some comments related to the challenge being "fun".
*   **Top 3 Points of View:**
    *   Use a controller lambda + SQS + worker lambda setup for distributed processing.
    *   Utilize Apache Spark with auto loader for distributed reads and checkpointing.
    *   For a one-off run, avoid over-engineering and process files locally in parallel.

**[ Pivot from dev to data engineering (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1p8wmlv/pivot_from_dev_to_data_engineering/)**
*   **Summary:** The thread discusses the pros and cons of pivoting from a software development role to a data engineering role.  It covers the similarities and differences in stress levels, required skills, and the types of challenges encountered in each field.
*   **Emotion:** The overall emotional tone is mixed, with a slight Positive leaning. Some comments express concerns about stress in DE, while others highlight the interesting aspects and potential benefits.
*   **Top 3 Points of View:**
    *   Data Engineering can be as stressful or more stressful than software development.
    *   Data Engineering roles involve dealing with unstructured data and constantly changing data sources.
    *   A background in backend development can be beneficial for transitioning to data engineering.

**[ Airflow dag task stuck in queued state even if dag is running (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1p8h2eh/airflow_dag_task_stuck_in_queued_state_even_if/)**
*   **Summary:** The thread discusses a problem where an Airflow DAG task is stuck in the queued state, even though the DAG is running.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Set the schedule to @once.
    *   Reboot your docker instance and clear airflow state.
    *   Airflow is weirdly flaky.

**[ Specialising on fabric, worth it or waste of time? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p8rapv/specialising_on_fabric_worth_it_or_waste_of_time/)**
*   **Summary:**  The thread explores the value of specializing in Microsoft Fabric, considering current market trends and the importance of transferable skills.
*   **Emotion:**  The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Focus on fundamental concepts like data modeling and transformations rather than specific technologies.
    *   Specializing in Fabric is useful if you're in a Microsoft-first environment; otherwise, prioritize Snowflake and dbt.
    *   Make sure you're picking up plenty of transferrable skills along the way (modelling, dq, mdm etc).

**[ Which paid tool is better for database CI/CD with MSSQL / MySQL — Liquibase or Bytebase? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p8rcar/which_paid_tool_is_better_for_database_cicd_with/)**
*   **Summary:** The thread compares Liquibase and Bytebase for database CI/CD, noting their strengths and weaknesses for different use cases. Liquibase is recommended for smaller teams, while Bytebase is recommended for when a strong UI with approvals and audit is needed.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Liquibase is a solid choice for migration-as-code in git, contexts for environments, and drift detection.
    *   Bytebase is strong for review workflows, SQL linting, environment pipelines, and permission guardrails.
    *   Focus on using a deploy service account per environment with least privilege and gating releases with tests.

**[ DE managing my own database? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p8f3lu/de_managing_my_own_database/)**
*   **Summary:** The thread discusses the situation where a data engineer is asked to manage their own database, addressing the challenges and potential solutions, especially when there's a conflict with a traditional DBA.
*   **Emotion:** The overall emotional tone is mixed with Negative and Positive elements.  There's frustration towards the "boomer dba energy," but also encouragement for the DE to learn and manage the database themselves.
*   **Top 3 Points of View:**
    *   It's generally not recommended to manage your own database unless it's a managed service.
    *   Old-school Microsoft DBAs can be difficult to work with.
    *   Consider migrating to a managed Postgres instance.

**[ Phased Databricks migration (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p8t368/phased_databricks_migration/)**
*   **Summary:** The thread discusses strategies for a phased migration to Databricks, focusing on how to structure the migration to maximize efficiency and minimize rework.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Make Phase 1 disposable-light: land raw data to ADLS Gen2 on day one and use SQL MI/SSIS only for extraction, not transformation.
    *   Stand up Unity Catalog, Delta Lake (bronze/silver/gold), and Databricks Autoloader now.
    *   Keep Phase 1, but aim everything at ADLS/Delta and Databricks from day one so almost nothing gets thrown away.

**[ What job title would be appropriate for my situation (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p8txqx/what_job_title_would_be_appropriate_for_my/)**
*   **Summary:** The thread discusses the appropriate job title for a person in a unique data-related role and the importance of having a title that accurately reflects the responsibilities and offers leverage for future career opportunities.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   You need a layer above you otherwise they're setting you up for failure.
    *   Go with Staff Software Engineer.
    *   Your position won’t really matter - as long as you can leverage your experience later.

**[ Is this an use case for Lambda Views/Architecture? How to handle realtime data models (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p8k8kd/is_this_an_use_case_for_lambda_viewsarchitecture/)**
*   **Summary:** The thread is a question about whether the poster's specific problem is an use case for Lambda Views/Architecture and asks for advice on how to handle realtime data models.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 1 Points of View:**
    *   The commenter needs more information, such as the size of the data and the db/dwh being used, to determine if Lambda Views/Architecture is a good fit.

**[ Ingestion and storage 101 - Can someone give me some tips? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p8yd8z/ingestion_and_storage_101_can_someone_give_me/)**
*   **Summary:** The thread seeks advice on ingestion and storage strategies, particularly in the context of using Azure Data Factory (ADF) and Power BI.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 2 Points of View:**
    *   Use ADF / azure function and write it to delta. Have power bi read from storage.
    *   Use Simple Python script that calls the API and saves the raw data to S3 (“raw lawyer”), json format and Another simple Python script that applies some basic transformations to the S3 files and saves the results to postgres or whatever

**[ Declarative data processing for "small data"? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p8ew4k/declarative_data_processing_for_small_data/)**
*   **Summary:** The thread explores declarative data processing approaches for smaller datasets.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 2 Points of View:**
    *   Look at Luigi
    *   try to do declarative/implicit programming with github.com/mloda-ai/mloda

**[ DATAOPS TOOLS: bruin core Vs. dbtran = fivetran + dbt core (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p8zgpr/dataops_tools_bruin_core_vs_dbtran_fivetran_dbt/)**
*   **Summary:** The thread discusses and compares different DataOps tools.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 1 Points of View:**
    *   The co-founder of Bruin offers to connect the user with many of Bruin's users.

**[ Delta Sharing Protocol (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p8tjav/delta_sharing_protocol/)**
*   **Summary:** The thread discusses the Delta Sharing Protocol.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 2 Points of View:**
    *   Pushdown with Delta Sharing works when your filters are simple, hit the partitioned Date column and are applied before the first action.
    *   Predicate push down may not work with delta share.

**[ Is there a "middleware" missing between Terraform and Agentic workflows? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p94m7p/is_there_a_middleware_missing_between_terraform/)**
*   **Summary:** The thread asks about the need for a middleware between Terraform and Agentic workflows.
*   **Emotion:** The overall emotional tone is Positive.
*   **Top 1 Points of View:**
    *   The commenter has their own layer for data pipelines and event services and would like to discuss this with the poster.
