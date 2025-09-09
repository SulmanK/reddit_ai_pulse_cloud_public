---
title: "Data Engineering Subreddit"
date: "2025-07-13"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Do I have a good job?](https://www.reddit.com/r/dataengineering/comments/1lyav6g/do_i_have_a_good_job/) (Score: 13)
    * The thread discusses whether the poster has a good data engineering job, considering the salary, responsibilities, and market conditions.
2.  [How do you handle daily ingests in a Duck Lake / Delta Lake setup?](https://www.reddit.com/r/dataengineering/comments/1lyvrbz/how_do_you_handle_daily_ingests_in_a_duck_lake/) (Score: 13)
    * The thread discusses how to handle daily ingests in a Duck Lake/Delta Lake setup.
3.  [In Azure databricks, can you query a datalake storage gen2 table in a SQL notebook?](https://www.reddit.com/r/dataengineering/comments/1lybol9/in_azure_databricks_can_you_query_a_datalake/) (Score: 4)
    * The thread discusses whether it is possible to query a datalake storage gen2 table in a SQL notebook in Azure Databricks.
4.  [Dedicated Pools for Synapse DWH](https://www.reddit.com/r/dataengineering/comments/1lz0tn1/dedicated_pools_for_synapse_dwh/) (Score: 3)
    * The thread discusses dedicated pools for Synapse Data Warehouse, including data movement, orchestration, and comparisons with Snowflake and Databricks.
5.  [Airflow SMTP not supporting OAuth - what is the proper solution?](https://www.reddit.com/r/dataengineering/comments/1lz2059/airflow_smtp_not_supporting_oauth_what_is_the/) (Score: 1)
    * The thread is about the proper solution if Airflow SMTP does not support OAuth.

# Detailed Analysis by Thread
**[[D] Do I have a good job? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1lyav6g/do_i_have_a_good_job/)**
*   **Summary:** The thread is about whether the original poster has a good data engineering job, considering factors like salary, learning opportunities, and market conditions.
*   **Emotion:** The overall emotional tone of the thread is positive to neutral, with some negative sentiment regarding salary negotiation and job market difficulties.
*   **Top 3 Points of View:**
    *   The current job is a good stepping stone for gaining experience.
    *   It's important to develop skills that are valuable and strategic for future career growth.
    *   It might be difficult to get a new job in the current labor market.

**[How do you handle daily ingests in a Duck Lake / Delta Lake setup? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1lyvrbz/how_do_you_handle_daily_ingests_in_a_duck_lake/)**
*   **Summary:** The discussion focuses on various strategies for handling daily data ingestion into Duck Lake/Delta Lake environments, including using ETL vs ELT, directly copying data from sources, and implementing a medallion architecture (Raw, Bronze, Silver, Gold layers).
*   **Emotion:** The emotional tone is primarily neutral, focusing on technical advice and best practices.
*   **Top 3 Points of View:**
    *   Consider the source of data before focusing on the destination.
    *   Implement a medallion architecture (Raw, Bronze, Silver, Gold).
    *   Data management and governance are important.

**[In Azure databricks, can you query a datalake storage gen2 table in a SQL notebook? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1lybol9/in_azure_databricks_can_you_query_a_datalake/)**
*   **Summary:** The thread revolves around whether Azure Data Lake Storage Gen2 tables can be queried directly from SQL notebooks within Azure Databricks. The consensus is that while there's no direct way, workarounds exist, involving ADF, PySpark, or Pandas.
*   **Emotion:** The emotional tone is neutral, with a focus on providing technical solutions and clarifying misconceptions.
*   **Top 3 Points of View:**
    *   Directly querying Azure Table Storage (NoSQL) is not supported; instead, use ADF or Databricks to ingest the data.
    *   PySpark or Pandas can be used to read the data, which can then be registered as a temp view for SQL queries.
    *   ADLS gen2 is a fully supported storage option for Azure Databricks.

**[Dedicated Pools for Synapse DWH (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lz0tn1/dedicated_pools_for_synapse_dwh/)**
*   **Summary:** The thread discusses dedicated pools in Synapse DWH, best practices for data movement, the role of Spark, and alternatives like Snowflake and Databricks. There is also a warning about the future of Synapse PaaS.
*   **Emotion:** The emotional tone is mostly neutral, with some concern expressed about the direction of Microsoft's Synapse product.
*   **Top 3 Points of View:**
    *   Move data in meaningful batches for better performance.
    *   Spark is important for data movement and processing.
    *   Synapse Analytics Workspaces (PaaS) may be deprecated in favor of Fabric.

**[Airflow SMTP not supporting OAuth - what is the proper solution? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lz2059/airflow_smtp_not_supporting_oauth_what_is_the/)**
*   **Summary:** This thread appears to be a question about Airflow SMTP not supporting OAuth. However, the single comment is from a bot and is unrelated to the question, pointing to a resource for transitioning into Data Engineering.
*   **Emotion:** Neutral, as the single comment is an automated message.
*   **Top 3 Points of View:**
    *   N/A (Only a bot comment present)
