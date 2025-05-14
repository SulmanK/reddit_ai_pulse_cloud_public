---
title: "Data Engineering Subreddit"
date: "2025-05-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [An open source resource to data stack evolution - Data Stack Survey](https://www.metabase.com/blog/metabase-community-data-stack-survey-2025) (Score: 8)
    * The thread discusses a data stack survey resource.
2.  [Automating Data/Model Validation](https://www.reddit.com/r/dataengineering/comments/1kma2lu/automating_datamodel_validation/) (Score: 8)
    * This thread is about automating the data model validation process.
3.  [Advice needed for normalizing database for a personal rock climbing project](https://www.reddit.com/r/dataengineering/comments/1kmch5u/advice_needed_for_normalizing_database_for_a/) (Score: 7)
    * This thread is about normalizing a database for a personal rock climbing project.
4.  [Airflow vs Github Action for orchestration](https://www.reddit.com/r/dataengineering/comments/1kmmv20/airflow_vs_github_action_for_orchestration/) (Score: 7)
    * The discussion centers on the comparison between Airflow and Github Actions for orchestration.
5.  [Any data professionals out there using a tool called Data Virtuality?](https://www.reddit.com/r/dataengineering/comments/1kmdjpk/any_data_professionals_out_there_using_a_tool/) (Score: 6)
    * People are sharing their experiences with Data Virtuality.
6.  [How to best approach data versioning at scale in Databricks](https://www.reddit.com/r/dataengineering/comments/1km7g2k/how_to_best_approach_data_versioning_at_scale_in/) (Score: 5)
    * This thread explores different approaches to data versioning in Databricks.
7.  [Help with Researching Analytical DBs: StarRocks, Druid, Apache Doris, ClickHouse — What Should I Know?](https://www.reddit.com/r/dataengineering/comments/1kmezq9/help_with_researching_analytical_dbs_starrocks/) (Score: 3)
    * This thread provides learning resources for analytical databases like StarRocks, Druid, Apache Doris, and ClickHouse.
8.  [dbt and Snowflake:  Keeping metadata in sync BOTH WAYS](https://www.reddit.com/r/dataengineering/comments/1kmk8lw/dbt_and_snowflake_keeping_metadata_in_sync_both/) (Score: 2)
    * The discussion revolves around keeping metadata in sync between dbt and Snowflake.
9.  [Automating SAP Excel Reports (DBT + Snowflake + Power BI) – How to reliably identify source tables and field names?](https://www.reddit.com/r/dataengineering/comments/1kmlg94/automating_sap_excel_reports_dbt_snowflake_power/) (Score: 1)
    * The post asks for advice on automating SAP Excel reports.
10. [If AI is gold, how can data engineers sell shovels?](https://www.reddit.com/r/dataengineering/comments/1kmol3p/if_ai_is_gold_how_can_data_engineers_sell_shovels/) (Score: 1)
    * The post discusses how data engineers can leverage AI.
11. [How about using AI for Query Optimization?](https://www.reddit.com/r/dataengineering/comments/1kmflek/how_about_using_ai_for_query_optimization/) (Score: 0)
    * This thread is about using AI for query optimization.

# Detailed Analysis by Thread
**[An open source resource to data stack evolution - Data Stack Survey (Score: 8)](https://www.metabase.com/blog/metabase-community-data-stack-survey-2025)**
*  **Summary:**  The thread is about sharing an open-source resource related to data stack evolution in the form of a Data Stack Survey.
*  **Emotion:** The overall emotional tone is Positive, with some neutral sentiment.
*  **Top 3 Points of View:**
    *   The resource is appreciated and considered valuable.
    *   Someone has submitted.
    *   N/A
**[Automating Data/Model Validation (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1kma2lu/automating_datamodel_validation/)**
*  **Summary:**  This thread discusses methods and tools for automating data and model validation, including using Saitology, Pytest, and Soda Core.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Use [Saitology](https://saitology.com/wrunner/?q=mva) for elegant and simple validation.
    *   Writing tests is crucial, and Pytest is a good option.
    *   Use Soda Core to define checks as YAML files and trigger them in Python or SQL-based workflows.
**[Advice needed for normalizing database for a personal rock climbing project (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kmch5u/advice_needed_for_normalizing_database_for_a/)**
*  **Summary:**  The thread provides advice on how to normalize a database for a personal rock climbing project, covering topics like weather data integration, database design principles, and the use of star schemas.
*  **Emotion:** The overall emotional tone is Positive to Neutral.
*  **Top 3 Points of View:**
    *   It's likely that you will have weather information by route or problem, instead use midpoint for the crag to get the weather prediction.
    *   The project could be turned into a user-facing data warehouse like Snowflake or BigQuery.
    *   You need some basic knowledge of database design to create a "normalized" model for transactional database.
**[Airflow vs Github Action for orchestration (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kmmv20/airflow_vs_github_action_for_orchestration/)**
*  **Summary:**  The thread discusses the pros and cons of using Airflow versus Github Actions for data orchestration, with opinions ranging from Github Actions being suitable for simple pipelines to being a garbage take.
*  **Emotion:** The overall emotional tone is Positive to Neutral.
*  **Top 3 Points of View:**
    *   Github Actions can be fine for simple pipelines that just need to get kicked off on a schedule.
    *   Large enterprises use Azure DevOps to run dbt.
    *   Scheduled CI runners don't have a guaranteed runtime in most cases.
**[Any data professionals out there using a tool called Data Virtuality? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kmdjpk/any_data_professionals_out_there_using_a_tool/)**
*  **Summary:**  The thread is about data professionals sharing their experiences with Data Virtuality.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Data Virtuality has bugs and limitations.
    *   Migration was a nightmare with vendor lock.
    *   Use fivetran+dbt cloud, or dlthub for ingestion.
**[How to best approach data versioning at scale in Databricks (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1km7g2k/how_to_best_approach_data_versioning_at_scale_in/)**
*  **Summary:**  The thread explores approaches to data versioning at scale in Databricks.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Consider SCD instead of delta time travel and giving access to the same table with applied row level security.
    *   Use row-level security and a "version" column.
    *   Use a single Delta table with a version or snapshot column.
**[Help with Researching Analytical DBs: StarRocks, Druid, Apache Doris, ClickHouse — What Should I Know? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kmezq9/help_with_researching_analytical_dbs_starrocks/)**
*  **Summary:**  The thread is about sharing community-submitted learning resources for analytical databases like StarRocks, Druid, Apache Doris, and ClickHouse.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Community-submitted learning resources can be found at https://dataengineering.wiki/Learning+Resources
    *   N/A
    *   N/A
**[dbt and Snowflake:  Keeping metadata in sync BOTH WAYS (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kmk8lw/dbt_and_snowflake_keeping_metadata_in_sync_both/)**
*  **Summary:**  The discussion revolves around keeping metadata in sync between dbt and Snowflake.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Use a dbt-native solution with on run start/end hooks to write/read metadata to/from a designated table.
    *   N/A
    *   N/A
**[Automating SAP Excel Reports (DBT + Snowflake + Power BI) – How to reliably identify source tables and field names? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kmlg94/automating_sap_excel_reports_dbt_snowflake_power/)**
*  **Summary:**  The post asks for advice on automating SAP Excel reports.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Use Power Query in Power BI for early transforms.
    *   Consult with veteran SAP professionals to identify source tables.
    *   Use Microsoft’s Azure Data Factory, Fivetran or DreamFactory to streamline integration with SAP data.
**[If AI is gold, how can data engineers sell shovels? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kmol3p/if_ai_is_gold_how_can_data_engineers_sell_shovels/)**
*  **Summary:**  The post discusses how data engineers can leverage AI.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Focus on fundamentals, and be a good employee and teammate.
    *   Work with data scientists to make their lives easier.
    *   Understand getting structured outputs from AI using things like instructor.
**[How about using AI for Query Optimization? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kmflek/how_about_using_ai_for_query_optimization/)**
*  **Summary:**  This thread is about using AI for query optimization.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Employ experienced and knowledgeable employees instead of relying on LLMs.
    *   Enterprise databases have been doing it since the 00s.
    *   AI is too challenging for mid-level and above coding tasks.
