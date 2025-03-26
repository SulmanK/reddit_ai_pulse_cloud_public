---
title: "Data Engineering Subreddit"
date: "2025-03-26"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "spark", "data pipelines"]
---

# Overall Ranking and Top Discussions
1.  [Why is my bronze table 400x larger than silver in Databricks?](https://www.reddit.com/r/dataengineering/comments/1jk0wjd/why_is_my_bronze_table_400x_larger_than_silver_in/) (Score: 18)
    * The discussion revolves around a user's issue where their bronze table in Databricks is significantly larger than their silver table.
2.  [Breaking down Spark execution times](https://www.reddit.com/r/dataengineering/comments/1jjxwii/breaking_down_spark_execution_times/) (Score: 8)
    * The thread discusses methods and tools for analyzing and optimizing Spark execution times, particularly identifying bottlenecks.
3.  [Need help optimizing 35TB PySpark Job on Ray Cluster (Using RayDP)](https://www.reddit.com/r/dataengineering/comments/1jjzl1u/need_help_optimizing_35tb_pyspark_job_on_ray/) (Score: 5)
    * This thread focuses on optimizing a large PySpark job running on a Ray cluster, specifically addressing Out Of Memory (OOM) errors and performance bottlenecks.
4.  [Need advice and/or resources for modern data pipelines](https://www.reddit.com/r/dataengineering/comments/1jju5c2/need_advice_andor_resources_for_modern_data/) (Score: 2)
    * The thread seeks advice and resources for building modern data pipelines, addressing issues like limited compute and workflow orchestration.
5.  [I am working on a usecase which requires data to move from Google Bigquery to MongoDB. Need suggestions on how to upsert data instead of insert](https://www.reddit.com/r/dataengineering/comments/1jjvkzs/i_am_working_on_a_usecase_which_requires_data_to/) (Score: 1)
    * A user is looking for suggestions on how to upsert data from Google Bigquery to MongoDB, rather than simply inserting it.
6.  [Duplicate rows](https://www.reddit.com/r/dataengineering/comments/1jjyz3r/duplicate_rows/) (Score: 1)
    * The thread is about identifying and removing duplicate rows in a dataset.
7.  [Guidewire datahub](https://www.reddit.com/r/dataengineering/comments/1jk3fzb/guidewire_datahub/) (Score: 1)
    * A user is asking about Guidewire Datahub.
8. [Need some clarity in choosing the right course](https://www.reddit.com/r/dataengineering/comments/1jk1mzf/need_some_clarity_in_choosing_the_right_course/) (Score: 0)
    * The user is asking for some clarity in choosing the right course

# Detailed Analysis by Thread
**[Why is my bronze table 400x larger than silver in Databricks? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1jk0wjd/why_is_my_bronze_table_400x_larger_than_silver_in/)**
*   **Summary:** The user is experiencing a size discrepancy between their bronze and silver tables in Databricks, with the bronze table being significantly larger.  Possible causes discussed include schema differences, data types, SCD2 implementation, appending all rows regardless of changes, and small files.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The difference could be due to schema differences, specifically the dropping of columns between bronze and silver.
    *   If the bronze table is using SCD2, then it would naturally contain more rows than the silver table which only stores the most recent version.
    *   The bronze table might be appending every single row, regardless of whether there is a change, while the silver table is performing merges.

**[Breaking down Spark execution times (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1jjxwii/breaking_down_spark_execution_times/)**
*   **Summary:** The discussion is about identifying bottlenecks in Spark execution times.  Suggestions include parsing logs, examining shuffle partitions, checking for many-to-many joins, data skew, and using the Spark UI's stages tab to sort stages by duration.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Shuffles are often a bottleneck in Spark jobs, but optimizing other parts of the job can save time.
    *   Examine the Spark UI's stages tab to identify which stages are taking the longest.
    *   Parsing the logs yourself can help to get a more detailed breakdown of task execution times.

**[Need help optimizing 35TB PySpark Job on Ray Cluster (Using RayDP) (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jjzl1u/need_help_optimizing_35tb_pyspark_job_on_ray/)**
*   **Summary:** The user needs help optimizing a 35TB PySpark job on a Ray cluster, specifically dealing with Out Of Memory errors. Suggestions include addressing broadcast join limits, reducing executor count, and filtering the large data folders instead of joining.
*   **Emotion:** The overall emotional tone is primarily Neutral with a hint of negativity.
*   **Top 3 Points of View:**
    *   The default broadcast join limit in Spark might be too low for the user's small dataframe.
    *   The user's executor count might be too high, leading to overhead issues.
    *   Consider filtering the large data folders instead of joining to avoid reading all the big dataset.

**[Need advice and/or resources for modern data pipelines (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jju5c2/need_advice_andor_resources_for_modern_data/)**
*   **Summary:** The user is seeking advice and resources for modern data pipelines to address compute limitations and workflow orchestration challenges.  Suggestions include exploring platforms like Snowflake, Databricks, Azure Synapse/Glue, AWS, GCP. Reducing the MySQL database size will give you breathing room to plan for your next steps.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The user's main issues are a lack of dedicated compute and workflow orchestration.
    *   Modern platforms like Snowflake and Databricks can address the compute requirements.
    *   Pruning the MySQL database can reduce the database size.

**[I am working on a usecase which requires data to move from Google Bigquery to MongoDB. Need suggestions on how to upsert data instead of insert (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jjvkzs/i_am_working_on_a_usecase_which_requires_data_to/)**
*   **Summary:** The user is seeking advice on how to upsert data from Google Bigquery to MongoDB.  Questions are raised about the deployment environment of MongoDB and whether data changes in both BigQuery and MongoDB.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Where is the destination MongoDB deployed?
    *   Does data just change in BQ, or does mongo change too?
    *   Was it the user's decision to move from BigQuery to MongoDB?

**[Duplicate rows (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jjyz3r/duplicate_rows/)**
*   **Summary:** The thread discusses methods for identifying and removing duplicate rows.
*   **Emotion:** The overall emotional tone is positive and neutral.
*   **Top 3 Points of View:**
    *   Use what works. DISTINCT is fine if it does the job.
    *   Where is the data stored?
    *   Snowflake allows GROUP BY ALL.

**[Guidewire datahub (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jk3fzb/guidewire_datahub/)**
*   **Summary:** The user is asking about Guidewire Datahub.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The thread links to community submitted learning resources.

**[Need some clarity in choosing the right course (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jk1mzf/need_some_clarity_in_choosing_the_right_course/)**
*   **Summary:** The user is seeking clarity in choosing the right course.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The thread links to community submitted learning resources.
