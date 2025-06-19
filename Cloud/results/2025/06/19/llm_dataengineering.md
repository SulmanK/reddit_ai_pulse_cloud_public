---
title: "Data Engineering Subreddit"
date: "2025-06-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "spark", "etl"]
---

# Overall Ranking and Top Discussions
1.  [[D] Is Spark used outside of Databricks?](https://www.reddit.com/r/dataengineering/comments/1lfd1lv/is_spark_used_outside_of_databricks/) (Score: 36)
    * The discussion revolves around the usage of Spark in various cloud platforms and on-premise environments beyond Databricks.
2.  [Which ETL tool is most reliable for enterprise use, especially when cost is a critical factor?](https://www.reddit.com/r/dataengineering/comments/1lf9sj2/which_etl_tool_is_most_reliable_for_enterprise/) (Score: 21)
    *  Users discuss various ETL tools and their reliability and cost-effectiveness for enterprise use, with suggestions including Apache NiFi, Dagster, Hevo Data, SSIS, Duckdb, and Snowflake.
3.  [Which cloud DE platform (ADF, AWS, etc.) is free to use for small personal projects that I can put on my CV?](https://www.reddit.com/r/dataengineering/comments/1lf85o6/which_cloud_de_platform_adf_aws_etc_is_free_to/) (Score: 16)
    * The conversation centers on identifying free or low-cost cloud platforms (ADF, AWS, GCP) suitable for small data engineering projects for CV building.
4.  [Is Factorio really that good of a game for Data Engineers? Does it help to "think like a data engineer"?](https://www.reddit.com/r/dataengineering/comments/1lfj3uh/is_factorio_really_that_good_of_a_game_for_data/) (Score: 7)
    * The discussion explores if the game Factorio can help data engineers with their problem-solving skills.
5.  [[Databricks/PySpark] Getting Down to the JVM: How to Handle Atomic Commits & Advanced Ops in Python ETLs](https://www.reddit.com/r/dataengineering/comments/1lfc5eq/databrickspyspark_getting_down_to_the_jvm_how_to/) (Score: 5)
    * Discussion about how to handle atomic commits and advanced operations in Python ETLs using Databricks/PySpark.
6.  [First ETL Data pipeline](https://github.com/pucci800/ai_dc_energy_demand) (Score: 5)
    * A user shares their first ETL data pipeline and receives positive feedback.
7.  [How do you query large datasets?](https://www.reddit.com/r/dataengineering/comments/1lfb1c1/how_do_you_query_large_datasets/) (Score: 4)
    * Discussion about how to query large datasets.
8.  [What I learned from the book Designing Data-Intensive Applications?](https://newsletter.techworld-with-milan.com/p/what-i-learned-from-the-book-designing) (Score: 4)
    * Discussion about which books are up to date and on streaming topics.
9.  [Data Lineage + Airflow / Data pipelines in general](https://www.reddit.com/r/dataengineering/comments/1lfevqh/data_lineage_airflow_data_pipelines_in_general/) (Score: 2)
    * Discussion about data lineage, Airflow and data pipelines.
10. [How do you handle development/testing environments in data engineering to avoid impacting production systems?](https://www.reddit.com/r/dataengineering/comments/1lfg8ii/how_do_you_handle_developmenttesting_environments/) (Score: 2)
    * Discussion on how to handle development/testing environments to avoid impacting production systems.
11. [I want to create a frontend for my ETL pipeline, what do I need to know and what resources can I use?](https://www.reddit.com/r/dataengineering/comments/1lf84d3/i_want_to_create_a_frontend_for_my_etl_pipeline/) (Score: 1)
    *  A user is asking about how to create a frontend for their ETL pipeline.
12. [Can we setup kafka topic lifecycle?](https://www.reddit.com/r/dataengineering/comments/1lfar60/can_we_setup_kafka_topic_lifecycle/) (Score: 1)
    * A user is asking if it's possible to set up a Kafka topic lifecycle.
13. [Need help understanding the below job description](https://www.reddit.com/r/dataengineering/comments/1lfk4rw/need_help_understanding_the_below_job_description/) (Score: 1)
    * A user needs help understanding a job description.

# Detailed Analysis by Thread

**[[D] Is Spark used outside of Databricks? (Score: 36)](https://www.reddit.com/r/dataengineering/comments/1lfd1lv/is_spark_used_outside_of_databricks/)**
*  **Summary:**  The thread discusses where Spark is used outside of Databricks, primarily focusing on cloud platforms like AWS EMR, Azure Synapse, Microsoft Fabric, and GCP Dataproc. Some users also mention using it on-premise.
*  **Emotion:** The emotional tone of the thread is generally Neutral.
*  **Top 3 Points of View:**
    * Spark is extensively used on cloud platforms like AWS (Glue, EMR), Azure Synapse, and Microsoft Fabric.
    * While Spark is used in GCP, some prefer BigQuery.
    * Spark was a significant technology before Databricks gained prominence.

**[Which ETL tool is most reliable for enterprise use, especially when cost is a critical factor? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1lf9sj2/which_etl_tool_is_most_reliable_for_enterprise/)**
*  **Summary:**  The discussion centers on the best ETL tools for enterprise use, considering reliability and cost. Options include Apache NiFi, Dagster, Hevo Data, SSIS, Duckdb, and Snowflake, with considerations for data governance and support.
*  **Emotion:** The emotional tone of the thread is generally Neutral.
*  **Top 3 Points of View:**
    * Open-source options like Apache NiFi and Dagster offer cost-effectiveness but may require more in-house expertise.
    * Microsoft SSIS is an established platform with excellent support, despite potential software limitations.
    * Data governance is a crucial factor when selecting an ETL tool, and Microsoft Purview integrated with Databricks or Fabric is a good option.

**[Which cloud DE platform (ADF, AWS, etc.) is free to use for small personal projects that I can put on my CV? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1lf85o6/which_cloud_de_platform_adf_aws_etc_is_free_to/)**
*  **Summary:**  This thread discusses which cloud data engineering platforms offer free tiers suitable for personal projects. Options include AWS, Azure, GCP, and Databricks, with cautions about monitoring usage to avoid unexpected costs.
*  **Emotion:** The emotional tone of the thread is mixed, with a slightly Positive leaning.
*  **Top 3 Points of View:**
    * AWS offers a free tier and potentially low costs for small projects.
    * Azure, specifically Azure Data Factory, is commonly referenced in job descriptions and offers free services.
    * Databricks has a free tier for gaining experience with the platform.

**[Is Factorio really that good of a game for Data Engineers? Does it help to "think like a data engineer"? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1lfj3uh/is_factorio_really_that_good_of_a_game_for_data/)**
*  **Summary:**  This thread explores whether the game Factorio can help data engineers develop useful skills. The consensus is that it helps with logistics, pipeline building, and understanding bottlenecks in processes.
*  **Emotion:** The emotional tone of the thread is generally Positive.
*  **Top 3 Points of View:**
    * Factorio is similar to data engineering work, involving building pipelines and refactoring.
    * The game helps visualize how upstream processes can create bottlenecks and spaghetti code can bloat a process.
    * Factorio may be more about logistics than specific data engineering tasks.

**[[Databricks/PySpark] Getting Down to the JVM: How to Handle Atomic Commits & Advanced Ops in Python ETLs (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1lfc5eq/databrickspyspark_getting_down_to_the_jvm_how_to/)**
*  **Summary:**  The thread discusses how to handle atomic commits and advanced operations in Python ETLs within Databricks/PySpark, including the use of commit protocols.
*  **Emotion:** The emotional tone of the thread is generally Neutral.
*  **Top 3 Points of View:**
    * You can dig into various commit protocols and implement your own for the storage layer you are writing to, which will have specific characteristics.
    * HDFS allows you to rename files atomically, but s3 has no such functionality.
    * Learning resources are available on the dataengineering.wiki.

**[First ETL Data pipeline (Score: 5)](https://github.com/pucci800/ai_dc_energy_demand)**
*  **Summary:** A user shared their first ETL data pipeline and received a positive response encouraging them to add architecture diagrams.
*  **Emotion:** The emotional tone of the thread is Positive.
*  **Top 3 Points of View:**
    * The shared ETL pipeline is considered great.
    * Adding an architecture diagram would be a beneficial addition.

**[How do you query large datasets? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1lfb1c1/how_do_you_query_large_datasets/)**
*  **Summary:** This thread is about how to effectively query large datasets, with suggestions to increase cluster size and check query profiles for pruning.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Try increasing the cluster size for querying.
    * Consider querying the source data directly.
    * Analyze query profiles to check if pruning is occurring.

**[What I learned from the book Designing Data-Intensive Applications? (Score: 4)](https://newsletter.techworld-with-milan.com/p/what-i-learned-from-the-book-designing)**
*  **Summary:** This thread is about which books are up to date and on streaming topics.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *  A user is requesting suggestions for up-to-date books on streaming topics.

**[Data Lineage + Airflow / Data pipelines in general (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lfevqh/data_lineage_airflow_data_pipelines_in_general/)**
*  **Summary:** This thread is about data lineage, Airflow and data pipelines.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Consider using DBT/sqlmesh for data lineage.
    * Check the Apache Airflow documentation for OpenLineage integration.

**[How do you handle development/testing environments in data engineering to avoid impacting production systems? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lfg8ii/how_do_you_handle_developmenttesting_environments/)**
*  **Summary:** This thread is about how to handle development/testing environments to avoid impacting production systems.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Use multiple versions of every resource, including APIs and data lake, for dev, test, and prod environments in Azure.

**[I want to create a frontend for my ETL pipeline, what do I need to know and what resources can I use? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lf84d3/i_want_to_create_a_frontend_for_my_etl_pipeline/)**
*  **Summary:** The thread discusses how to create a frontend for an ETL pipeline, suggesting Streamlit, HTML, CSS, Javascript, or Flask.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Consider using Streamlit for creating the frontend.
    * Alternatively, use HTML, CSS, and Javascript.
    * Flask can be used if you want to stay in Python.

**[Can we setup kafka topic lifecycle? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lfar60/can_we_setup_kafka_topic_lifecycle/)**
*  **Summary:** This thread is about how to set up a Kafka topic lifecycle.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Build a simple clean-up script.
    * Set message TTL for topics and create a script to delete topics without data.

**[Need help understanding the below job description (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lfk4rw/need_help_understanding_the_below_job_description/)**
*  **Summary:** This thread is about a user who needs help understanding a job description.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * The community guide on dataengineering.wiki/Learning+Resources may be helpful.
