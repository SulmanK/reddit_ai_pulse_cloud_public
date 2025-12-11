---
title: "Data Engineering Subreddit"
date: "2025-10-10"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How much data engineers care about costs?](https://www.reddit.com/r/dataengineering/comments/1o33raz/how_much_data_engineers_care_about_costs/) (Score: 21)
    *   The discussion revolves around the importance of cost considerations for data engineers, especially in cloud environments, and the trade-offs between feature delivery and cost optimization.
2.  [How do you feel the Job market is at the moment?](https://www.reddit.com/r/dataengineering/comments/1o37d19/how_do_you_feel_the_job_market_is_at_the_moment/) (Score: 15)
    *   Users are sharing their experiences and perceptions of the current job market for data engineers, with varying perspectives based on location and seniority.
3.  [Looking for tuning advice for ClickHouse](https://www.reddit.com/r/dataengineering/comments/1o2vw26/looking_for_tuning_advice_for_clickhouse/) (Score: 12)
    *   The thread discusses tuning ClickHouse for optimal performance, comparison with other solutions like Exasol, and specific configurations to consider.
4.  [Need Airflow DAG monitoring tips](https://www.reddit.com/r/dataengineering/comments/1o2tgtq/need_airflow_dag_monitoring_tips/) (Score: 8)
    *   The discussion centers around different approaches to monitoring Airflow DAGs, including using a dedicated monitoring DAG, implementing failure alerts, and leveraging external tools.
5.  [How to model two fact tables with different levels of granularity according to Kimball?](https://www.reddit.com/r/dataengineering/comments/1o2yrhe/how_to_model_two_fact_tables_with_different/) (Score: 8)
    *   The thread discusses strategies for modeling fact tables with different granularities in a Kimball-style data warehouse, including using date dimensions, bridge tables, and aggregating data.
6.  [Built an API to query economic/demographic statistics without the CSV *** - looking for feedback **Affiliated**](https://www.reddit.com/r/dataengineering/comments/1o30rpr/built_an_api_to_query_economicdemographic/) (Score: 6)
    *   Users are providing feedback on an API built to query economic and demographic statistics, focusing on canonical schema, provenance, versioning and DSL.
7.  [AI use in Documentation](https://www.reddit.com/r/dataengineering/comments/1o385re/ai_use_in_documentation/) (Score: 6)
    *   The discussion revolves around using AI for documentation purposes, with the consensus that it can generate a good first draft but requires polishing.
8.  [A JSON validator that actually gets what you meant.](https://www.reddit.com/r/dataengineering/comments/1o36inq/a_json_validator_that_actually_gets_what_you_meant/) (Score: 4)
    *   Users are reacting to a JSON validator that attempts to understand the intent behind the data, with some expressing interest in trying it out.
9.  [Looking for a lightweight open-source metadata catalog (≤1 GB RAM) to pair with Marquez & Delta tables](https://www.reddit.com/r/dataengineering/comments/1o39o9b/looking_for_a_lightweight_opensource_metadata/) (Score: 4)
    *   The thread is a request for recommendations for a lightweight open-source metadata catalog.
10. [Tips on how to build our data pipeline](https://www.reddit.com/r/dataengineering/comments/1o2v24z/tips_on_how_to_build_our_data_pipeline/) (Score: 3)
    *   Users are providing advice on building data pipelines, suggesting tools like AWS Athena, declarative systems like Delta Live Tables, and Aiven for automation.
11. [How to handle data from different sources and formats?](https://www.reddit.com/r/dataengineering/comments/1o35mma/how_to_handle_data_from_different_sources_and/) (Score: 3)
    *   The discussion focuses on strategies for handling data from various sources and formats, emphasizing automation, data pipeline tools, and avoiding PDFs if possible.
12. [Shared paths with Python, dbt, and uv?](https://www.reddit.com/r/dataengineering/comments/1o2vmg0/shared_paths_with_python_dbt_and_uv/) (Score: 0)
    *   This thread seems to be seeking advice on configuration management with Python, dbt, and uv, suggesting the use of environment variables or CLI arguments.
13. [Junior analyst thrown into the deep end & needs help with job/ETL process](https://www.reddit.com/r/dataengineering/comments/1o38y09/junior_analyst_thrown_into_the_deep_end_needs/) (Score: 0)
    *   A junior analyst seeks advice on ETL processes. Recommendations include delivering business value, moving data to an analytical database, and integrating with the organization's existing solutions.

# Detailed Analysis by Thread
**[How much data engineers care about costs? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1o33raz/how_much_data_engineers_care_about_costs/)**
*  **Summary:** The thread discusses the importance of cost considerations for data engineers, especially in cloud environments. It covers topics like optimizing cloud platform costs, balancing feature delivery with cost, and managing budgets in data engineering projects.
*  **Emotion:** The overall emotional tone is neutral, with some positive sentiments related to delivering solutions and saving costs, and some negative sentiments about management prioritizing features over cost optimization.
*  **Top 3 Points of View:**
    *   Data engineers should be heavily focused on cost, given the consumption-based cost model of most cloud platforms.
    *   Management often prioritizes feature delivery over cost optimization, leading to increased costs and performance degradation.
    *   Cost concerns are inherent in data engineering, particularly when dealing with large datasets and limited budgets.

**[How do you feel the Job market is at the moment? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1o37d19/how_do_you_feel_the_job_market_is_at_the_moment/)**
*  **Summary:** The thread asks how people perceive the current job market for data engineers. There are differing views, with some indicating a tough market, especially in the EU, while others, particularly in NYC, find the market for senior engineers to be active.
*  **Emotion:** The emotional tone is primarily neutral, with some hints of positivity from those experiencing a good job market and some negative sentiment from those finding it difficult.
*  **Top 3 Points of View:**
    *   The job market is challenging in general.
    *   Analytics Engineering roles are more readily available than pure Data Engineering roles.
    *   The job market for senior engineers in NYC is strong.

**[Looking for tuning advice for ClickHouse (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1o2vw26/looking_for_tuning_advice_for_clickhouse/)**
*  **Summary:**  The thread is seeking advice on tuning ClickHouse for optimal performance. Discussions include comparisons with other solutions like Exasol and suggestions for specific configurations.
*  **Emotion:** The emotional tone is mostly neutral, with some negative sentiment regarding comparisons with enterprise solutions.
*  **Top 3 Points of View:**
    *   ClickHouse's strength lies in scalability, storage efficiency, and fast aggregations.
    *   Adjusting the `optimize_move_to_prewhere` setting and checking index usage can improve performance.
    *   ClickHouse is a good open-source alternative to industrial-strength enterprise solutions.

**[Need Airflow DAG monitoring tips (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1o2tgtq/need_airflow_dag_monitoring_tips/)**
*  **Summary:** The thread discusses various strategies for monitoring Airflow DAGs, including creating a dedicated monitoring DAG, implementing failure alerts, and using external monitoring tools.
*  **Emotion:** The emotional tone is neutral overall.
*  **Top 3 Points of View:**
    *   Create a dedicated DAG to monitor other DAGs by calling the Airflow API.
    *   Implement failure alerts (Slack or email) to notify of issues, rather than reporting successful statuses.
    *   Use an external SaaS tool to monitor DAGs and detect issues with Airflow itself.

**[How to model two fact tables with different levels of granularity according to Kimball? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1o2yrhe/how_to_model_two_fact_tables_with_different/)**
*  **Summary:** The thread explores strategies for modeling fact tables with different granularities in a Kimball-style data warehouse. It includes discussions on using date dimensions, bridge tables, and aggregating data.
*  **Emotion:** The emotional tone is mainly neutral, with some positive sentiment expressing agreement with the user's approach.
*  **Top 3 Points of View:**
    *   Never join 2 fact tables directly, you have to join them through a common dimension.
    *   Create one transaction type dimension and use a date in the target fact.
    *   Create a third fact table to compare business realities and target dimensions.

**[Built an API to query economic/demographic statistics without the CSV *** - looking for feedback **Affiliated** (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1o30rpr/built_an_api_to_query_economicdemographic/)**
*  **Summary:** The thread solicits feedback on an API built to query economic and demographic statistics. Discussions focus on the importance of a stable, versioned schema, rich metadata, performance optimization, and a compact DSL.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The main value lies in hiding CSV chaos behind a stable, versioned schema and a clear query surface.
    *   Lock down a canonical model with ISO country codes, metric taxonomy, unit, frequency, seasonal adjustment, currency/base year, and a concordance table.
    *   Store normalized series as Parquet, serve via DuckDB or ClickHouse, and cache popular slices behind a CDN with ETag-based revalidation for performance.

**[AI use in Documentation (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1o385re/ai_use_in_documentation/)**
*  **Summary:** The discussion centers on the use of AI in documentation. Users generally agree that AI can generate a good first draft, but it still requires human polishing.
*  **Emotion:** The emotional tone is mostly neutral, with slight positivity towards AI's usefulness.
*  **Top 3 Points of View:**
    *   AI can generate a good first draft for documentation.
    *   AI-generated documentation still needs to be polished by humans.
    *   AI can get you 60-80% of the way there.

**[A JSON validator that actually gets what you meant. (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o36inq/a_json_validator_that_actually_gets_what_you_meant/)**
*  **Summary:** The thread is a reaction to a JSON validator that attempts to understand the intent behind the data. Users express interest in trying it out.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The validator looks useful.
    *   Interest in trying the validator someday.

**[Looking for a lightweight open-source metadata catalog (≤1 GB RAM) to pair with Marquez & Delta tables (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o39o9b/looking_for_a_lightweight_opensource_metadata/)**
*  **Summary:** The thread is a request for recommendations for a lightweight open-source metadata catalog.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Recommendation to check a list of open-source data catalogs.

**[Tips on how to build our data pipeline (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o2v24z/tips_on_how_to_build_our_data_pipeline/)**
*  **Summary:** Users are providing advice on building data pipelines, suggesting tools like AWS Athena, declarative systems like Delta Live Tables, and Aiven for automation.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Avoid doing explicit orchestration and go with a declarative system.
    *   Use AWS Athena to process files in-place directly on S3.
    *   Aiven can simplify this setup by running Airflow to automate the data prep from S3 and PostgreSQL.

**[How to handle data from different sources and formats? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o35mma/how_to_handle_data_from_different_sources_and/)**
*  **Summary:** The discussion focuses on strategies for handling data from various sources and formats, emphasizing automation, data pipeline tools, and avoiding PDFs if possible.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Avoid PDFs if possible and try to get data in tabular formats like CSV or JSON.
    *   Use Databricks AutoLoader to load everything into a delta column as text.
    *   Automate data gathering from common sources into a central location.

**[Shared paths with Python, dbt, and uv? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o2vmg0/shared_paths_with_python_dbt_and_uv/)**
*  **Summary:** This thread seeks advice on configuration management with Python, dbt, and uv.
*  **Emotion:** The emotional tone is neutral.
*  **Top 2 Points of View:**
    *   The user is talking about configuration management.
    *   The least common denominator may be env vars or CLI arguments for the variables you set.

**[Junior analyst thrown into the deep end & needs help with job/ETL process (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o38y09/junior_analyst_thrown_into_the_deep_end_needs/)**
*  **Summary:** A junior analyst seeks advice on ETL processes.
*  **Emotion:** The emotional tone is slightly positive.
*  **Top 3 Points of View:**
    *   Focus on delivering business value using data.
    *   Move the data into an analytical database and do the processing there.
    *   Move towards whatever the rest of the organization is doing in the long term.
