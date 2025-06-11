---
title: "Data Engineering Subreddit"
date: "2025-04-10"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Tried to roll out Microsoft Fabric… ended up rolling straight into a $20K/month wall](https://www.reddit.com/r/dataengineering/comments/1jvwwcy/tried_to_roll_out_microsoft_fabric_ended_up/) (Score: 386)
    *   The discussion revolves around unexpected high costs incurred while implementing Microsoft Fabric, with users sharing advice and concerns about AI-driven pipelines.
2.  [Data analytics system (s3, duckdb, iceberg, glue) ko](https://i.redd.it/swk8caawryte1.jpeg) (Score: 41)
    *   Users are discussing different data analytics system architectures, including S3, DuckDB, Iceberg, and Glue, and considering factors like cost, performance, and lock-in.
3.  [Is the Data Engineer Role Still Relevant in the Era of Multi-Skilled Data Teams?](https://www.reddit.com/r/dataengineering/comments/1jvs8f1/is_the_data_engineer_role_still_relevant_in_the/) (Score: 20)
    *   The thread explores the relevance of the data engineer role in the context of multi-skilled data teams and the rise of AI, with varying opinions on its future.
4.  [Can I learn AWS Data Engineering on localstack?](https://www.reddit.com/r/dataengineering/comments/1jvu3af/can_i_learn_aws_data_engineering_on_localstack/) (Score: 21)
    *   The post asks about the feasibility of learning AWS Data Engineering on LocalStack, with users suggesting alternatives like SQL Server Developer Edition and free AWS trials.
5.  [Sql to pyspark](https://www.reddit.com/r/dataengineering/comments/1jvr8my/sql_to_pyspark/) (Score: 9)
    *   The discussion focuses on translating SQL code to PySpark, with users sharing tips, tools, and strategies for dealing with complex SQL procedures and views.
6.  [Staging Layer Close to Source - is it a right approach](https://www.reddit.com/r/dataengineering/comments/1jvuwgm/staging_layer_close_to_source_is_it_a_right/) (Score: 7)
    *   The thread discusses the benefits of having a staging layer close to the data source for debugging and reprocessing data, with general agreement on its value.
7.  [What job profile fits someone whose majority time goes in reverse engineering SQL queries?](https://www.reddit.com/r/dataengineering/comments/1jvxw0v/what_job_profile_fits_someone_whose_majority_time/) (Score: 7)
    *   Users are exploring different job profiles that involve reverse engineering SQL queries, including database administrator, data engineer, business intelligence developer, and data analyst.
8.  [Databases supporting set of vectors on disk?](https://www.reddit.com/r/dataengineering/comments/1jvsr6u/databases_supporting_set_of_vectors_on_disk/) (Score: 5)
    *   The post asks about databases that support sets of vectors on disk, with a suggestion to use pgvector, a Postgres extension.
9.  [Have I Overengineered My Analytics Backend? (Detailed Architecture and Feedback Request)](https://www.reddit.com/r/dataengineering/comments/1jvuiqx/have_i_overengineered_my_analytics_backend/) (Score: 3)
    *   The user is requesting feedback on their analytics backend architecture, with suggestions to consider dbt, Python for calculations, and ClickHouse for performance.
10. [CloudFlare R2 Data Catalog: Managed Apache Iceberg tables with zero egress fees](https://blog.cloudflare.com/r2-data-catalog-public-beta/) (Score: 2)
    *   The post discusses the CloudFlare R2 Data Catalog, with a comment about the need for lightweight data catalogs and its pricing.
11. [Trying to move from Data Analysis to DE. Would PowerCenter be a bad move?](https://www.reddit.com/r/dataengineering/comments/1jvskco/trying_to_move_from_data_analysis_to_de_would/) (Score: 2)
    *   The user is asking about the value of learning PowerCenter for a career transition from data analysis to data engineering, with suggestions to focus on Python, SQL, and modern cloud tools instead.
12. [Polars mapping](https://www.reddit.com/r/dataengineering/comments/1jvtlcc/polars_mapping/) (Score: 1)
    *   The post is about Polars mapping, with a suggestion to use `.replace_strict()`.
13. [A cost effective way to use Google Labs to learn DE](https://www.reddit.com/r/dataengineering/comments/1jvysa4/a_cost_effective_way_to_use_google_labs_to_learn/) (Score: 1)
    *   The post is about learning data engineering with google labs. The bot recommends the dataengineering.wiki
14. [Any way to optimize XML transformation in Snowflake](https://www.reddit.com/r/dataengineering/comments/1jw1vsu/any_way_to_optimize_xml_transformation_in/) (Score: 1)
    *   The post is about optimizing XML transformations. The bot recommends the dataengineering.wiki
15. [Monitoring Data Volume Metrics?](https://www.reddit.com/r/dataengineering/comments/1jw2tqa/monitoring_data_volume_metrics/) (Score: 1)
    *   The post is about monitoring data volume metrics. There is a suggestion to use a DBT package.
16. [Advice on Data Deduplication](https://www.reddit.com/r/dataengineering/comments/1jw6m8p/advice_on_data_deduplication/) (Score: 1)
    *   The post is about data deduplication, with suggestions to use SSIS or the Splink Python library.

# Detailed Analysis by Thread
**[[D] Tried to roll out Microsoft Fabric… ended up rolling straight into a $20K/month wall (Score: 386)](https://www.reddit.com/r/dataengineering/comments/1jvwwcy/tried_to_roll_out_microsoft_fabric_ended_up/)**
*  **Summary:** The thread discusses a costly Microsoft Fabric implementation, with users sharing concerns about AI-driven pipelines and offering advice.
*  **Emotion:** The overall emotional tone is neutral, with some concern about costs and inexperienced implementations.
*  **Top 3 Points of View:**
    *   ChatGPT-powered pipelines are a potential nightmare.
    *   Unexpected high costs may be due to running F64 without a reservation and lacking surge protection.
    *   Inexperienced and rushed implementation is to blame, particularly allowing AI to write pipelines.

**[Data analytics system (s3, duckdb, iceberg, glue) ko (Score: 41)](https://i.redd.it/swk8caawryte1.jpeg)**
*  **Summary:** Users discuss various data analytics system architectures using S3, DuckDB, Iceberg, and Glue, considering factors like cost, performance, and lock-in.
*  **Emotion:** The overall emotional tone is neutral, focused on technical considerations. One comment displays a slightly positive sentiment.
*  **Top 3 Points of View:**
    *   For 500GB of data, simplicity is key, and using Postgres with dbt is a viable option.
    *   Querying vast amounts of data in Postgres can be costly; Redshift or Snowflake with dbt-core and MWAA are alternatives.
    *   Consider avoiding lock-in or prioritizing fast queries when selecting a solution, and evaluate AWS, Starbucks, Snowflake, or a combination of dlthub, Lakekeeper, dbt, and DuckDB.

**[Is the Data Engineer Role Still Relevant in the Era of Multi-Skilled Data Teams? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1jvs8f1/is_the_data_engineer_role_still_relevant_in_the/)**
*  **Summary:** The thread explores the relevance of the data engineer role amidst multi-skilled teams and AI advancements, with divided opinions.
*  **Emotion:** The overall emotional tone is neutral, with some negative sentiment regarding the increasing workload and the potential threat of AI. Some comments display a slightly positive sentiment.
*  **Top 3 Points of View:**
    *   Data engineers are still necessary, especially in larger companies, and a data engineering background is valuable.
    *   Software engineers are increasingly taking on data engineering work, potentially reducing the need for dedicated data engineers.
    *   Data analysts/scientists may be more threatened by AI than data engineers, as AI may enhance data engineers' capabilities to create BI modules.

**[Can I learn AWS Data Engineering on localstack? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1jvu3af/can_i_learn_aws_data_engineering_on_localstack/)**
*  **Summary:** The post asks if it's possible to learn AWS Data Engineering on LocalStack, with suggestions of using SQL Server Developer Edition.
*  **Emotion:** The emotional tone is overall positive and helpful.
*  **Top 3 Points of View:**
    *   If the AWS DE services are available in localstack, then it is possible to learn AWS DE.
    *   You can install SQL Server Developer Edition completely free and practice your data engineering skills in SSIS.
    *   Isn't it easier to get a new credit card and register new free trial with $300 USD?

**[Sql to pyspark (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1jvr8my/sql_to_pyspark/)**
*  **Summary:** The discussion revolves around translating SQL code to PySpark, offering advice, tools, and strategies for dealing with complex SQL procedures and views.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Try parsing it with sqlglot first.
    *   Use Spark SQL instead.
    *   Use an LLM tool, such as Copilot, as a starting point for translation.

**[Staging Layer Close to Source - is it a right approach (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jvuwgm/staging_layer_close_to_source_is_it_a_right/)**
*  **Summary:** The thread discusses the benefits of having a staging layer close to the data source for debugging and reprocessing data.
*  **Emotion:** The emotional tone is overall positive, as people agree on the value of the approach.
*  **Top 3 Points of View:**
    *   Having that first staging layer is actually pretty solid. It gives you a safety net for when things go wrong (and they will).
    *   Having a replica of the prod backend DB would mean that we might possibly have missed things over time.
    *   Incremental changes from the source systems should be written as insert-only to your landing stage tables.

**[What job profile fits someone whose majority time goes in reverse engineering SQL queries? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jvxw0v/what_job_profile_fits_someone_whose_majority_time/)**
*  **Summary:** Users are exploring different job profiles that involve reverse engineering SQL queries.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   Business intelligence dev
    *   Data engineer
    *    Data analyst or business analyst

**[Databases supporting set of vectors on disk? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jvsr6u/databases_supporting_set_of_vectors_on_disk/)**
*  **Summary:** The post asks about databases that support sets of vectors on disk.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   Use [pgvector](https://github.com/pgvector/pgvector).

**[Have I Overengineered My Analytics Backend? (Detailed Architecture and Feedback Request) (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jvuiqx/have_i_overengineered_my_analytics_backend/)**
*  **Summary:** The user is requesting feedback on their analytics backend architecture.
*  **Emotion:** The emotional tone is overall positive.
*  **Top 3 Points of View:**
    *   The original poster should have looked at DBT for dependecies and DAGs.
    *   Avoid recalculation.
    *   SQL is better than Python.

**[CloudFlare R2 Data Catalog: Managed Apache Iceberg tables with zero egress fees (Score: 2)](https://blog.cloudflare.com/r2-data-catalog-public-beta/)**
*  **Summary:** The post discusses the CloudFlare R2 Data Catalog.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   Need for lightweight data catalogs.

**[Trying to move from Data Analysis to DE. Would PowerCenter be a bad move? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jvskco/trying_to_move_from_data_analysis_to_de_would/)**
*  **Summary:** The user is asking about the value of learning PowerCenter for a career transition from data analysis to data engineering.
*  **Emotion:** The emotional tone is overall positive.
*  **Top 3 Points of View:**
    *   PowerCenter knowledge alone won't cut it in today's market.
    *   Learn the basics of data analysis before starting a project.
    *   PowerCenter is a good ETL platform but expensive. SSIS is an enterprise ETl platform included with every SQL Server license.

**[Polars mapping (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jvtlcc/polars_mapping/)**
*  **Summary:** The post is about Polars mapping, with a suggestion to use `.replace_strict()`.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   Use [`.replace_strict()`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.replace_strict.html#polars.Expr.replace_strict)

**[A cost effective way to use Google Labs to learn DE (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jvysa4/a_cost_effective_way_to_use_google_labs_to_learn/)**
*  **Summary:** The post is about learning data engineering with google labs.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   The dataengineering.wiki has a list of learning resources.

**[Any way to optimize XML transformation in Snowflake (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jw1vsu/any_way_to_optimize_xml_transformation_in/)**
*  **Summary:** The post is about optimizing XML transformations.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   The dataengineering.wiki has a list of learning resources.

**[Monitoring Data Volume Metrics? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jw2tqa/monitoring_data_volume_metrics/)**
*  **Summary:** The post is about monitoring data volume metrics.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   There is a suggestion to use a DBT package.

**[Advice on Data Deduplication (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jw6m8p/advice_on_data_deduplication/)**
*  **Summary:** The post is about data deduplication.
*  **Emotion:** The emotional tone is overall neutral.
*  **Top 3 Points of View:**
    *   There are suggestions to use SSIS or the Splink Python library.
