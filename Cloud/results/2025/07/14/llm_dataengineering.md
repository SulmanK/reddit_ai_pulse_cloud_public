---
title: "Data Engineering Subreddit"
date: "2025-07-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How do you get questions answered (without AI)?](https://www.reddit.com/r/dataengineering/comments/1lzl4dc/how_do_you_get_questions_answered_without_ai/) (Score: 22)
    * Discusses various methods for finding answers to technical questions without relying on AI, including using search engines, documentation, and community resources.
2.  [Question on optimal partitioning structure for parquet on s3 duckdb query](https://www.reddit.com/r/dataengineering/comments/1lzbege/question_on_optimal_partitioning_structure_for/) (Score: 11)
    * Asks about the best way to partition Parquet files on S3 for querying with DuckDB, with responses focusing on tailoring the partitioning scheme to match query patterns.
3.  [Airflow 2.0 to 3.0 migration](https://www.reddit.com/r/dataengineering/comments/1lzv8r4/airflow_20_to_30_migration/) (Score: 8)
    * Discusses the migration process from Airflow 2.0 to 3.0, providing links to official documentation and highlighting potential issues encountered during the upgrade.
4.  [Need Advice: What to Do After Finishing My SSIS Solution for Final Year Project?](https://www.reddit.com/r/dataengineering/comments/1lziopf/need_advice_what_to_do_after_finishing_my_ssis/) (Score: 6)
    * Seeks advice on what to do after completing an SSIS solution for a final year project, with suggestions focusing on logging, monitoring, and restartability.
5.  [Is this ELT or ETL?](https://www.reddit.com/r/dataengineering/comments/1lztpb4/is_this_elt_or_etl/) (Score: 3)
    * Debates whether a particular data process qualifies as ELT or ETL, with some arguing it's neither due to the absence of explicit extraction and loading steps.
6.  [Are you guys managing to keep up?](https://www.reddit.com/r/dataengineering/comments/1lzwqiq/are_you_guys_managing_to_keep_up/) (Score: 3)
    * Discusses the challenges of keeping up with the rapid pace of change in the data engineering field, with some focusing on specific technologies like Databricks and MS Fabric.
7.  [Data Extraction from Google Maps](https://www.reddit.com/r/dataengineering/comments/1lzp0qn/data_extraction_from_google_maps/) (Score: 2)
    * Asks about data extraction from Google Maps, with a suggestion to check if scraping is allowed and to write an automated script.

# Detailed Analysis by Thread
**[How do you get questions answered (without AI)? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1lzl4dc/how_do_you_get_questions_answered_without_ai/)**
*  **Summary:** The thread explores methods for finding answers to technical questions without relying solely on AI. It covers using search engines (DuckDuckGo, Google), official documentation, Stack Overflow, GitHub issues, niche communities (Slack/Discord), and personal networks. Some users also mentioned using LLMs to refine search terms but ultimately verifying the information through official sources.
*  **Emotion:** Predominantly Neutral with some Positive sentiment. The positive sentiment likely comes from users sharing successful strategies.
*  **Top 3 Points of View:**
    * Use LLMs to generate keywords, then verify the results through documentation and other sources.
    * Rely on a combination of search engines like DuckDuckGo and Stack Overflow, followed by official documentation.
    * Build a personal knowledge base by saving useful information and leveraging networks of experts.

**[Question on optimal partitioning structure for parquet on s3 duckdb query (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1lzbege/question_on_optimal_partitioning_structure_for/)**
*  **Summary:** The thread discusses optimal partitioning strategies for Parquet files stored on S3 when querying with DuckDB. The consensus is that the best partitioning scheme depends on the specific query patterns and filtering criteria. It's recommended to test different setups and measure performance to determine the most efficient approach.
*  **Emotion:** Mostly Neutral, with some hints of Positive sentiment stemming from the solutions oriented advice shared.
*  **Top 3 Points of View:**
    * Partitioning should align with the most common filtering criteria in queries.
    * The impact of folder lookup is generally negligible unless there are thousands of partitions.
    * The best approach is to conduct empirical testing with different partitioning schemes and measure performance.

**[Airflow 2.0 to 3.0 migration (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1lzv8r4/airflow_20_to_30_migration/)**
*  **Summary:** This thread focuses on migrating from Airflow 2.0 to 3.0. Users share links to the official Airflow documentation for upgrading and discuss potential issues, such as import changes (everything is from airflow.sdk now) and problems with dynamic task mapping, specifically regarding data type conversions.
*  **Emotion:** Mostly Neutral. A small amount of Positive sentiment is likely due to the information being shared regarding the migration.
*  **Top 3 Points of View:**
    * Follow the official Airflow upgrade guide.
    * Be aware of import changes, as modules have moved to airflow.sdk.
    * Watch out for potential data type conversion issues in dynamic task mapping.

**[Need Advice: What to Do After Finishing My SSIS Solution for Final Year Project? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1lziopf/need_advice_what_to_do_after_finishing_my_ssis/)**
*  **Summary:** The thread seeks advice on what to do after completing an SSIS project. The main suggestions involve implementing logging, monitoring, restartability, and the ability to turn on/off parts of the job via a control table in a database.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    * Implement logging and monitoring.
    * Ensure restartability of the job.
    * Allow enabling/disabling parts of the job using a control table.

**[Is this ELT or ETL? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lztpb4/is_this_elt_or_etl/)**
*  **Summary:** The thread discusses whether a specific data transformation process should be classified as ELT or ETL. Several users argue that it is neither because there is no extraction or loading, as the transformation happens within the same database.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    * The process is ETL because it involves extracting, transforming, and loading (even within the same system).
    * The process is ELT because the transformation occurs within the target system.
    * The process is neither ETL nor ELT as there is no explicit extraction or loading from one system to another.

**[Are you guys managing to keep up? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lzwqiq/are_you_guys_managing_to_keep_up/)**
*  **Summary:** Users discuss the struggle to keep up with the ever-evolving landscape of data engineering technologies. Some are focusing on specific tools like Databricks, dbt, and PySpark, while others are refactoring workflows to use MS Fabric Notebooks. The general sentiment is that there is a lot of noise and it's important to focus on what's relevant.
*  **Emotion:** Neutral, with a hint of positive sentiment from those who are embracing new technologies.
*  **Top 3 Points of View:**
    * Focus on mastering specific tools relevant to your job.
    * Embrace new technologies like MS Fabric Notebooks.
    * Tune out the noise and focus on what's essential.

**[Data Extraction from Google Maps (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lzp0qn/data_extraction_from_google_maps/)**
*  **Summary:** The thread briefly discusses data extraction from Google Maps. The single suggestion is to check if scraping is allowed and then automate the process with a script if possible.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    * Check if scraping is allowed and then write an automated script.
