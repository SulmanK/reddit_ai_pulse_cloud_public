---
title: "Data Engineering Subreddit"
date: "2025-04-24"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] *** that guy just wrote a database in 2 lines of bash](https://i.redd.it/nqcgrkcm0twe1.png) (Score: 270)
    * The thread discusses an implementation of a database in 2 lines of bash script.

2.  [Does your company expect data engineers to understand enterprise architecture?](https://www.reddit.com/r/dataengineering/comments/1k6wi8y/does_your_company_expect_data_engineers_to/) (Score: 7)
    * The thread discusses whether data engineers are expected to understand enterprise architecture in their companies.

3.  [Query runs longer than your AWS bill. How do I improve it](https://www.reddit.com/r/dataengineering/comments/1k6xfby/query_runs_longer_than_your_aws_bill_how_do_i/) (Score: 6)
    * The thread discusses how to improve a query that is running longer than the AWS bill.

4.  [Icebird: I wrote an Apache Iceberg reader from scratch in JavaScript](https://github.com/hyparam/icebird) (Score: 6)
    * The thread discusses an Apache Iceberg reader written in JavaScript.

5.  [How do you manage versioning when both raw and transformed data shift?](https://www.reddit.com/r/dataengineering/comments/1k6sth5/how_do_you_manage_versioning_when_both_raw_and/) (Score: 5)
    * The thread discusses how to manage versioning when both raw and transformed data change.

6.  [Where do you publish your PowerBI dashboards?](https://www.reddit.com/r/dataengineering/comments/1k6p9uv/where_do_you_publish_your_powerbi_dashboards/) (Score: 4)
    * The thread is about where people publish their PowerBI dashboards.

7.  [Best approach to warehousing flats](https://www.reddit.com/r/dataengineering/comments/1k6zbhh/best_approach_to_warehousing_flats/) (Score: 3)
    * The thread discusses the best approach to warehousing flats.

8.  [AirByte: How to transform data before sync to destination](https://www.reddit.com/r/dataengineering/comments/1k6vlwr/airbyte_how_to_transform_data_before_sync_to/) (Score: 2)
    * The thread discusses how to transform data before syncing to the destination using Airbyte.

9.  [How do you handle real-time data access (<100ms) while keeping bulk ingestion efficient and stable?](https://www.reddit.com/r/dataengineering/comments/1k6p7x9/how_do_you_handle_realtime_data_access_100ms/) (Score: 1)
    * The thread discusses how to handle real-time data access with low latency while maintaining efficient and stable bulk ingestion.

10. [Looking for insights from current Solution Architects or Senior Solution Architects at Databricks (or similar tech organizations) — what are the key differences in roles and responsibilities between the two positions?](https://www.reddit.com/r/dataengineering/comments/1k6r1by/looking_for_insights_from_current_solution/) (Score: 1)
    * The thread seeks insights into the key differences between Solution Architects and Senior Solution Architects at Databricks or similar companies.

11. [Data Analyst/Engineer](https://www.reddit.com/r/dataengineering/comments/1k6w80r/data_analystengineer/) (Score: 1)
    * The thread discusses the roles and responsibilities of a Data Analyst/Engineer.

12. [Iceberg CDC and Cron](https://www.reddit.com/r/dataengineering/comments/1k71cqf/iceberg_cdc_and_cron/) (Score: 1)
    * The thread is about Iceberg CDC and Cron

13. [Need career advise ??](https://www.reddit.com/r/dataengineering/comments/1k71y9n/need_career_advise/) (Score: 1)
    * The thread is asking for career advice.

14. [Just realized that I don't fully understand how Snowflake decouples storage and compute. What happens behind the scenes from when I submit a query to when I see the results?](https://www.reddit.com/r/dataengineering/comments/1k6ugw8/just_realized_that_i_dont_fully_understand_how/) (Score: 0)
    * The thread is asking for Snowflake decoupling knowledge.

# Detailed Analysis by Thread
**[[D] *** that guy just wrote a database in 2 lines of bash (Score: 270)](https://i.redd.it/nqcgrkcm0twe1.png)**
*  **Summary:** The thread discusses an implementation of a database in 2 lines of bash script, comparing it to other database solutions and discussing its limitations and potential use cases.
*  **Emotion:** The overall emotional tone of the thread is neutral with some positive comments.
*  **Top 3 Points of View:**
    *   The bash script can be considered a simple key-value store.
    *   CSV files can be considered databases for those who don't mind the drawbacks.
    *   It's a demonstration of a concept.

**[Does your company expect data engineers to understand enterprise architecture? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1k6wi8y/does_your_company_expect_data_engineers_to/)**
*  **Summary:** The thread discusses whether data engineers are expected to understand enterprise architecture in their companies, with some arguing that it's not always necessary but can be helpful for communication and compliance, while others feel it's an unreasonable expectation.
*  **Emotion:** The overall emotional tone of the thread is neutral. There's a hint of negativity from a user ranting about excessive expectations.
*  **Top 3 Points of View:**
    *   Data engineers are not always required to understand EA frameworks like TOGAF.
    *   Understanding EA can help data engineers liaise more effectively with the EA function.
    *   Companies may have unreasonable expectations of data engineers, including understanding architecture and various other tasks.

**[Query runs longer than your AWS bill. How do I improve it (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k6xfby/query_runs_longer_than_your_aws_bill_how_do_i/)**
*  **Summary:** The thread discusses how to improve a query that is running longer than the AWS bill, with suggestions including using CTEs, checking the planner, caching results, and considering the underlying data store.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Using CTE logic to filter data before ranking can improve performance.
    *   Caching previous day's results and applying today's changes can reduce computation time.
    *   The choice of underlying data store (e.g., Postgres, Redshift) matters for performance.

**[Icebird: I wrote an Apache Iceberg reader from scratch in JavaScript (Score: 6)](https://github.com/hyparam/icebird)**
*  **Summary:** The thread discusses an Apache Iceberg reader written in JavaScript, with questions about its implementation and performance compared to other solutions.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Pushing Iceberg + Parquet into the browser is interesting.
    *   The implementation details, such as manifest filtering and page-level stats, are important for performance.
    *   Benchmarking against duckdb-wasm or Arrow JS would be useful.

**[How do you manage versioning when both raw and transformed data shift? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1k6sth5/how_do_you_manage_versioning_when_both_raw_and/)**
*  **Summary:** The thread discusses how to manage versioning when both raw and transformed data change, with suggestions including using idempotent pipelines and tools like DBmaestro and dbt.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Using idempotent pipelines can solve the versioning problem in batch pipelines.
    *   DBmaestro helps with schema versioning and data lineage tracking.
    *   dbt can be used for managing versioning.

**[Where do you publish your PowerBI dashboards? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k6p9uv/where_do_you_publish_your_powerbi_dashboards/)**
*  **Summary:** The thread is about where people publish their PowerBI dashboards, with Power BI Report Server being mentioned.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Power BI Report Server

**[Best approach to warehousing flats (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k6zbhh/best_approach_to_warehousing_flats/)**
*  **Summary:** The thread discusses the best approach to warehousing flats, with suggestions including using SQL Server Integration Services (SSIS) and data catalogs like Glue Catalog or Hive Metastore.
*  **Emotion:** The overall emotional tone of the thread is neutral with one positive comment.
*  **Top 3 Points of View:**
    *   SQL Server Integration Services (SSIS) is an enterprise ETL platform.
    *   Data catalog, such as Glue Catalog or Hive Metastore, can be used.
    *   The recommended approach depends on the available tools and deployment setup.

**[AirByte: How to transform data before sync to destination (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k6vlwr/airbyte_how_to_transform_data_before_sync_to/)**
*  **Summary:** The thread discusses how to transform data before syncing to the destination using Airbyte, noting that Airbyte is primarily for EL and transformations are typically done elsewhere, with some enterprise features and workarounds available.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Airbyte is primarily used for EL (Extract and Load), not transformation.
    *   Airbyte offers mapping as an enterprise feature.
    *   Workarounds include creating views in the source or using PyAirbyte.

**[How do you handle real-time data access (<100ms) while keeping bulk ingestion efficient and stable? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k6p7x9/how_do_you_handle_realtime_data_access_100ms/)**
*  **Summary:** The thread discusses how to handle real-time data access with low latency while maintaining efficient and stable bulk ingestion, suggesting alternatives to ClickHouse like SingleStore, QuestDB, TimescaleDB, Cassandra, and Scylla.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   SingleStore is a good option for handling real-time ingestion and low-latency access.
    *   QuestDB and TimescaleDB are alternatives for low-latency requirements.
    *   Consider using different databases like Cassandra or Scylla.

**[Looking for insights from current Solution Architects or Senior Solution Architects at Databricks (or similar tech organizations) — what are the key differences in roles and responsibilities between the two positions? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k6r1by/looking_for_insights_from_current_solution/)**
*  **Summary:** The thread seeks insights into the key differences between Solution Architects and Senior Solution Architects at Databricks or similar companies, with one response highlighting the varied branding and focus of solution architect roles.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Solution Architect branding can vary, focusing on products or domain.
    *   Solution Architects bridge the gap between vendor lock-ins and desired technology.
    *   Deeper dive solutions are prefered with technical teams to discuss the implementation of the solution.

**[Data Analyst/Engineer (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k6w80r/data_analystengineer/)**
*  **Summary:** The thread discusses the roles and responsibilities of a Data Analyst/Engineer and transitioning into those roles.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   Data analyst would be much higher up the value chain.
    *   The line between data analysts and data engineers will keep getting fuzzier.
    *   Transitioning from analyst to analytics engineer is feasible.

**[Iceberg CDC and Cron (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k71cqf/iceberg_cdc_and_cron/)**
*  **Summary:** The thread is about Iceberg CDC and Cron, and recommends the community-submitted learning resources.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   The thread recommends checking the data engineering wiki for learning resources.

**[Need career advise ?? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k71y9n/need_career_advise/)**
*  **Summary:** The thread is asking for career advice, and recommends the community-submitted learning resources.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *   The thread recommends checking the data engineering wiki for learning resources.

**[Just realized that I don't fully understand how Snowflake decouples storage and compute. What happens behind the scenes from when I submit a query to when I see the results? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k6ugw8/just_realized_that_i_dont_fully_understand_how/)**
*  **Summary:** The thread is asking for Snowflake decoupling knowledge, and recommends the Snowflake whitepaper.
*  **Emotion:** The overall emotional tone of the thread is positive and neutral.
*  **Top 3 Points of View:**
    *   Reading the Snowflake whitepaper for a deeper understanding.
    *   Backend storage and its potential challenges.
    *   A simpler case of using S3 with pandas and turning off your computer does not affect the S3 storage.

