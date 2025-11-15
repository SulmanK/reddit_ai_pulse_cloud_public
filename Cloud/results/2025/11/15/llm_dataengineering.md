---
title: "Data Engineering Subreddit"
date: "2025-11-15"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] How Much of Data Engineering Is Actually Taught in Engineering or MCA Courses?](https://www.reddit.com/r/dataengineering/comments/1oxspqy/how_much_of_data_engineering_is_actually_taught/) (Score: 31)
    * Discussing how much of data engineering principles are taught in formal education, like engineering or MCA courses.
2.  [Need to scale feature engineering, only Python and SQL (SQL Server & SSIS) available as tools (no dbt etc.)](https://www.reddit.com/r/dataengineering/comments/1oxggmk/need_to_scale_feature_engineering_only_python_and/) (Score: 15)
    * Discussing strategies for scaling feature engineering using only Python and SQL, without tools like dbt.
3.  [Experimenting with DLT and DuckDb](https://www.reddit.com/r/dataengineering/comments/1oxu38x/experimenting_with_dlt_and_duckdb/) (Score: 13)
    * Users are sharing their experiences and insights on using DLT (presumably Data Loading Tool) with DuckDB.
4.  [Good free tools for API ingestion? How do they actually run in production?](https://www.reddit.com/r/dataengineering/comments/1oxoqj9/good_free_tools_for_api_ingestion_how_do_they/) (Score: 11)
    * The conversation is about good free tools for API ingestion and how those tools are being run in production.
5.  [Writing PySpark partitions to one file each in parallel?](https://www.reddit.com/r/dataengineering/comments/1oxf79l/writing_pyspark_partitions_to_one_file_each_in/) (Score: 10)
    * Discussing ways to write PySpark partitions to one file each in parallel, and the challenges and approaches involved.
6.  [Monitoring: Where do I start?](https://www.reddit.com/r/dataengineering/comments/1oxamdy/monitoring_where_do_i_start/) (Score: 7)
    * Discussing where to begin with monitoring data pipelines and systems.
7.  [Eye care](https://www.reddit.com/r/dataengineering/comments/1oxf3fk/eye_care/) (Score: 6)
    * Discussing techniques and tools for eye care, relevant to those who spend long hours in front of screens.
8.  [How to setup budget real-time pipelines?](https://www.reddit.com/r/dataengineering/comments/1oxto9o/how_to_setup_budget_realtime_pipelines/) (Score: 1)
    * Discussing how to set up real-time data pipelines on a limited budget.
9.  [Suggestions on what to spend $700 professional development stipend before EOY?](https://www.reddit.com/r/dataengineering/comments/1oxubz8/suggestions_on_what_to_spend_700_professional/) (Score: 0)
    * Asking for suggestions on how to best utilize a $700 professional development stipend before the end of the year.
10. [how common is it to find remote jobs in DE?](https://www.reddit.com/r/dataengineering/comments/1oxyssl/how_common_is_it_to_find_remote_jobs_in_de/) (Score: 0)
    * Discussing the frequency and feasibility of finding remote data engineering jobs.

# Detailed Analysis by Thread
**[[D] How Much of Data Engineering Is Actually Taught in Engineering or MCA Courses? (Score: 31)](https://www.reddit.com/r/dataengineering/comments/1oxspqy/how_much_of_data_engineering_is_actually_taught/)**
*  **Summary:**  The thread discusses the extent to which data engineering principles are covered in engineering and MCA courses. Many users report that while basic SQL and sometimes big data tools like Hadoop, Spark, and Kafka are taught, crucial topics like data modeling, ETL, pipeline design, and cloud DevOps are often missing.
*  **Emotion:** Predominantly Neutral. Though some comments express frustration (Negative Emotion) about the lack of comprehensive data engineering education, most responses are factual and informative.
*  **Top 3 Points of View:**
    *   Some universities have started incorporating big data classes, covering technologies like Hadoop, Spark, and Kafka, but these are recent additions.
    *   Traditional database courses cover relational databases and concepts like B-trees, which are interesting but not always directly helpful for modern data engineering.
    *   Essential data engineering skills like data modeling, Airflow, and pipeline design patterns are often self-taught.

**[Need to scale feature engineering, only Python and SQL (SQL Server & SSIS) available as tools (no dbt etc.) (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1oxggmk/need_to_scale_feature_engineering_only_python_and/)**
*  **Summary:** The thread is about strategies for scaling feature engineering with limited tools (Python and SQL Server/SSIS, excluding dbt). It covers query optimization, data modeling, and alternative tools like Apache Hamilton and Narwhals.
*  **Emotion:** Mostly Neutral with some Positive comments. The positive comments express gratitude and confirmation of correct steps, while the neutral comments focus on providing advice and suggestions.
*  **Top 3 Points of View:**
    *   Optimize SQL queries by analyzing the query plan, simplifying logic, and minimizing processed data. Consider using windowing functions.
    *   Improve the data warehouse structure, possibly separating business metrics and context using a star schema or similar data modeling techniques.
    *   Utilize Python to generate and parameterize SQL, or consider using the dbt Python SDK.

**[Experimenting with DLT and DuckDb (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1oxu38x/experimenting_with_dlt_and_duckdb/)**
*  **Summary:** This thread discusses experiences and tips for using DLT (Data Loading Tool) with DuckDB.
*  **Emotion:** Predominantly Positive, with users sharing favorable opinions and suggesting optimizations.
*  **Top 3 Points of View:**
    *   DLT is a great tool.
    *   Using Lambda with EventBridge to run Python code can make setup cheaper.
    *   Knowing how to deploy DLT on Lambda is beneficial.

**[Good free tools for API ingestion? How do they actually run in production? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1oxoqj9/good_free_tools_for_api_ingestion_how_do_they/)**
*  **Summary:** The thread focuses on recommending free tools for API ingestion and discussing how these tools are implemented and maintained in production environments.
*  **Emotion:** Predominantly Neutral, with a mix of informative and inquisitive comments.
*  **Top 3 Points of View:**
    *   Airbyte OSS is a good free option, but API changes can cause issues.
    *   Reliability depends on handling rate limits, schema drift, and retries effectively, not just the tool itself.
    *   Apache NiFi is a rock-solid, open-source option, particularly useful for handling API timeouts with its retry mechanisms.

**[Writing PySpark partitions to one file each in parallel? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1oxf79l/writing_pyspark_partitions_to_one_file_each_in/)**
*  **Summary:** This thread explores techniques for writing PySpark partitions to individual files in parallel, addressing challenges in managing Spark's default writing behavior.
*  **Emotion:** Predominantly Neutral, focusing on technical advice and problem-solving.
*  **Top 3 Points of View:**
    *   Repetitioning the data by the partition keys can enable parallel writing of all partitions.
    *   Using `coalesce` or `repartition` reduces parallelism by forcing Spark to write a single file, which goes against the goal of parallel writing.
    *   Consider changing the downstream pipeline to handle parquet tables correctly instead of trying to force Spark to output single files.

**[Monitoring: Where do I start? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1oxamdy/monitoring_where_do_i_start/)**
*  **Summary:** The thread discusses starting points for monitoring data pipelines, with suggestions ranging from anomaly detection to observability.
*  **Emotion:** Neutral, providing informational and resource-based recommendations.
*  **Top 3 Points of View:**
    *   Start with anomaly detection algorithms and time-series analysis.
    *   Consider leveraging AI for monitoring purposes.
    *   Explore observability as a concept that goes beyond simple metric collection.

**[Eye care (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1oxf3fk/eye_care/)**
*  **Summary:** This thread is dedicated to eye care tips and solutions for those who spend long hours in front of screens, which is particularly relevant to data engineers.
*  **Emotion:** Mostly Neutral, with a blend of personal experiences and practical suggestions. One comment has a positive emotion toward using eye spray.
*  **Top 3 Points of View:**
    *   Follow the 20-20-20 rule: look away from the screen every 20 minutes for 20 seconds at something 20 feet away.
    *   Ensure your eyes are not dry, and consider using eye drops or eye spray.
    *   Invest in a good flicker-free monitor with low blue light.

**[How to setup budget real-time pipelines? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1oxto9o/how_to_setup_budget_realtime_pipelines/)**
*  **Summary:** The discussion revolves around setting up cost-effective real-time data pipelines.
*  **Emotion:** Neutral, with an emphasis on practical advice.
*  **Top 2 Points of View:**
    *   Streaming 2GB per day using Kafka and Databricks might be over-engineered; consider using batch processing instead.
    *   Identify the sources of cost within your current setup.

**[Suggestions on what to spend $700 professional development stipend before EOY? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oxubz8/suggestions_on_what_to_spend_700_professional/)**
*  **Summary:** This thread is asking for recommendations on how to use a $700 professional development stipend before the end of the year.
*  **Emotion:** Neutral.
*  **Top 1 Point of View:**
    *   Consider using community-submitted learning resources from the dataengineering.wiki

**[how common is it to find remote jobs in DE? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oxyssl/how_common_is_it_to_find_remote_jobs_in_de/)**
*  **Summary:** The thread discusses the prevalence and challenges of finding remote data engineering jobs, particularly regarding compensation.
*  **Emotion:** Neutral, with a mix of personal experiences and realistic advice.
*  **Top 3 Points of View:**
    *   Remote data engineering jobs are possible, but the market is competitive.
    *   Getting a high cost of living (HCOL) salary while living in a low cost of living (LCOL) area is uncommon.
    *   One approach is to first secure a job in a high-paying location like NYC, become indispensable, then move and maintain the salary while working remotely.
