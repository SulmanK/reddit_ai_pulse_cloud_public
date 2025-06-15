---
title: "Data Engineering Subreddit"
date: "2025-06-15"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Processing 50 Million Brazilian Companies: Lessons from Building an Open-Source Government Data Pipeline](https://www.reddit.com/r/dataengineering/comments/1lby55q/processing_50_million_brazilian_companies_lessons/) (Score: 121)
    *   The thread discusses the lessons learned from building an open-source data pipeline for processing a large dataset of Brazilian companies.
2.  [Roast my project: I created a data pipeline which matches all the rock climbing locations in England with hourly 7 day weather forecast. This is the backend](https://www.reddit.com/r/dataengineering/comments/1lbi0re/roast_my_project_i_created_a_data_pipeline_which/) (Score: 40)
    *   A user is seeking feedback on their data pipeline project which combines rock climbing locations with weather forecasts.
3.  [Tired of Spark overhead; built a Polars catalog on Delta Lake.](https://www.reddit.com/r/dataengineering/comments/1lc1ke2/tired_of_spark_overhead_built_a_polars_catalog_on/) (Score: 34)
    *   The thread discusses building a Polars catalog on Delta Lake as an alternative to Spark, addressing the overhead associated with Spark.
4.  [Free tier isn’t enough — how can I learn Azure Data Factory more effectively?](https://www.reddit.com/r/dataengineering/comments/1lbrhw6/free_tier_isnt_enough_how_can_i_learn_azure_data/) (Score: 27)
    *   The thread discusses how to learn Azure Data Factory effectively when the free tier is insufficient.
5.  [Structuring a dbt project for fact and dimension tables?](https://www.reddit.com/r/dataengineering/comments/1lbrlb0/structuring_a_dbt_project_for_fact_and_dimension/) (Score: 21)
    *   This thread discusses the best way to structure a dbt project for fact and dimension tables.
6.  [I've built my ETL Pipeline, should I focus on optimising my pipeline or should I focus on building an endpoint for my data?](https://www.reddit.com/r/dataengineering/comments/1lc2270/ive_built_my_etl_pipeline_should_i_focus_on/) (Score: 15)
    *   The poster is seeking advice on whether to focus on optimizing their ETL pipeline or building an endpoint for their data.
7.  [How will Cloudfare remove its GCP dependency?](https://www.reddit.com/r/dataengineering/comments/1lbvlrb/how_will_cloudfare_remove_its_gcp_dependency/) (Score: 11)
    *   The thread explores Cloudflare's plans to reduce its dependency on Google Cloud Platform (GCP).
8.  [Kafka and Airflow](https://www.reddit.com/r/dataengineering/comments/1lbvhtk/kafka_and_airflow/) (Score: 6)
    *   This thread discusses the integration of Kafka and Airflow in data engineering workflows.
9.  [Trying to extract structured info from 2k+ logs (free text) - NLP or regex?](https://www.reddit.com/r/dataengineering/comments/1lbybox/trying_to_extract_structured_info_from_2k_logs/) (Score: 6)
    *   The user is asking for advice on whether to use NLP or regex for extracting structured information from free-text logs.
10. [Seeking Feedback on User ID Unification with Spark/GraphX and Delta Lake](https://www.reddit.com/r/dataengineering/comments/1lc08vf/seeking_feedback_on_user_id_unification_with/) (Score: 6)
    *   The poster is seeking feedback on a user ID unification strategy using Spark/GraphX and Delta Lake.
11. [best way to implement data quality testing with clickhouse?](https://www.reddit.com/r/dataengineering/comments/1lbkgv0/best_way_to_implement_data_quality_testing_with/) (Score: 3)
    *   The thread discusses the best ways to implement data quality testing within a Clickhouse environment.
12. [Has anyone implemented auto-segmentation for unstructured text?](https://www.reddit.com/r/dataengineering/comments/1lc11fa/has_anyone_implemented_autosegmentation_for/) (Score: 2)
    *   The poster is looking for experiences and advice on implementing auto-segmentation for unstructured text data.
13. [I need help with data analysis](https://www.reddit.com/r/dataengineering/comments/1lbi4fh/i_need_help_with_data_analysis/) (Score: 0)
    *   A user is requesting assistance with data analysis tasks.
14. [What Should I do ? Please help !!](https://www.reddit.com/r/dataengineering/comments/1lbunhz/what_should_i_do_please_help/) (Score: 0)
    *   The thread is a cry for career advice.
15. [PageRank, simillars/alternatives and Search Engines](https://www.reddit.com/r/dataengineering/comments/1lbuv0p/pagerank_simillarsalternatives_and_search_engines/) (Score: 0)
    *   This thread seems to be about PageRank algorithm and search engine alternatives.
16. [Built a binary-structured database that writes and reads 1M records in 3s using <1.1GB RAM](https://www.reddit.com/r/dataengineering/comments/1lc234x/built_a_binarystructured_database_that_writes_and/) (Score: 0)
    *   A user presents a new database they built with claimed performance benefits.
17. [New to Data Science/Data Analysis— Which Enterprise Tool Should I Learn First?](https://www.reddit.com/r/dataengineering/comments/1lc2us0/new_to_data_sciencedata_analysis_which_enterprise/) (Score: 0)
    *   The user is seeking advice on which enterprise tool to learn first as a newcomer to Data Science/Data Analysis.
18. [Is there a cursor for us DATA folks?](https://www.reddit.com/r/dataengineering/comments/1lc9afx/is_there_a_cursor_for_us_data_folks/) (Score: 0)
    *   The thread is about the Cursor IDE.

# Detailed Analysis by Thread
**[[D] Processing 50 Million Brazilian Companies: Lessons from Building an Open-Source Government Data Pipeline (Score: 121)](https://www.reddit.com/r/dataengineering/comments/1lby55q/processing_50_million_brazilian_companies_lessons/)**
*  **Summary:** The thread discusses the lessons learned from building an open-source data pipeline for processing a large dataset of Brazilian companies. The discussion includes tool recommendations, optimization tips, and validation techniques.
*  **Emotion:** The overall emotional tone is positive and neutral. Many comments express admiration and provide constructive feedback.
*  **Top 3 Points of View:**
    *   Pandas and MySQL may not be the best tools for analyzing data of this size; Polars and DuckDB are better alternatives.
    *   Staging tables are useful for improving upsert performance in data pipelines.
    *   Using Polars' built-in chunking can improve file processing efficiency.

**[Roast my project: I created a data pipeline which matches all the rock climbing locations in England with hourly 7 day weather forecast. This is the backend (Score: 40)](https://www.reddit.com/r/dataengineering/comments/1lbi0re/roast_my_project_i_created_a_data_pipeline_which/)**
*  **Summary:** A user is seeking feedback on their data pipeline project which combines rock climbing locations with weather forecasts. Discussions include suggestions for alternative database technologies, data modeling approaches, and tools for schema validation and data loading.
*  **Emotion:** The overall emotional tone is positive, with users offering encouragement and constructive criticism.
*  **Top 3 Points of View:**
    *   Consider using PostgreSQL with PostGIS for better handling of geodata and transactional workloads.
    *   It may be helpful to create a fact/dim approach for the data model.
    *   Use DLT (https://dlthub.com/docs/reference/explainers/how-dlt-works) to load data into DWH and then perform all the transformations in DWH instead of Python

**[Tired of Spark overhead; built a Polars catalog on Delta Lake. (Score: 34)](https://www.reddit.com/r/dataengineering/comments/1lc1ke2/tired_of_spark_overhead_built_a_polars_catalog_on/)**
*  **Summary:** The thread discusses building a Polars catalog on Delta Lake as an alternative to Spark, addressing the overhead associated with Spark. Users are seeking clarification on the project's purpose and its comparison to existing solutions like Databricks.
*  **Emotion:** The overall emotional tone is neutral, with a mix of curiosity, skepticism, and shared pain regarding Spark overhead.
*  **Top 3 Points of View:**
    *   Spark has too much overhead.
    *   The Rust delta kernel should support all the bells and whistles to leverage Polars over Spark.
    *   Clarification is needed on what "Flint" is.

**[Free tier isn’t enough — how can I learn Azure Data Factory more effectively? (Score: 27)](https://www.reddit.com/r/dataengineering/comments/1lbrhw6/free_tier_isnt_enough_how_can_i_learn_azure_data/)**
*  **Summary:** The thread discusses how to learn Azure Data Factory effectively when the free tier is insufficient. Suggestions include courses, small projects, following influencers, and obtaining certifications.
*  **Emotion:** The overall emotional tone is neutral, with practical advice and suggestions.
*  **Top 3 Points of View:**
    *   ADF has no future. Learning SSIS is better.
    *   Get a free fabric trial capacity.
    *   Take courses, do projects, follow influencers, get certs.

**[Structuring a dbt project for fact and dimension tables? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1lbrlb0/structuring_a_dbt_project_for_fact_and_dimension/)**
*  **Summary:** This thread discusses the best way to structure a dbt project for fact and dimension tables.
*  **Emotion:** The overall emotional tone is neutral, with practical advice and suggestions.
*  **Top 3 Points of View:**
    *   Have three separate layers: staging > intermediate > marts (which will contain your facts and dimensions).
    *   Use at least 2 layers, 4 for most cases for landing, joining tables, business rules and Kimball modeling.
    *   https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/

**[I've built my ETL Pipeline, should I focus on optimising my pipeline or should I focus on building an endpoint for my data? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1lc2270/ive_built_my_etl_pipeline_should_i_focus_on/)**
*  **Summary:** The poster is seeking advice on whether to focus on optimizing their ETL pipeline or building an endpoint for their data.
*  **Emotion:** The overall emotional tone is neutral, with some positive sentiment.
*  **Top 3 Points of View:**
    *   Focus on building the endpoint first to make the project somewhat ready.
    *   Optimization is not needed most of the time. You just make something that works, and only improve it when it stops working.
    *   Learning DE is quite difficult, because its not useful on its own.

**[How will Cloudfare remove its GCP dependency? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1lbvlrb/how_will_cloudfare_remove_its_gcp_dependency/)**
*  **Summary:** The thread explores Cloudflare's plans to reduce its dependency on Google Cloud Platform (GCP).
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Cloudflare will most likely not remove their dependency on GCP.
    *   Cloudflare's blog post said they will add another provider or implement it themselves in case GCP is down, but not committing to removing GCP.
    *   N/A

**[Kafka and Airflow (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1lbvhtk/kafka_and_airflow/)**
*  **Summary:** This thread discusses the integration of Kafka and Airflow in data engineering workflows.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Debezium is the primary solution for postgres native replication. It's industry standard way to stream data from postgres to kafka.
    *   Manual offset management gets complicated quickly, just use a Kafka connector.
    *   N/A

**[Trying to extract structured info from 2k+ logs (free text) - NLP or regex? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1lbybox/trying_to_extract_structured_info_from_2k_logs/)**
*  **Summary:** The user is asking for advice on whether to use NLP or regex for extracting structured information from free-text logs.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Use an LLM, but the time and cost might not be worth it.
    *   Download a transformer model from hugging face and set up the prompts to output what you want.
    *   Bin the data in three and identify features that keep doing this sort of partitioning.

**[Seeking Feedback on User ID Unification with Spark/GraphX and Delta Lake (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1lc08vf/seeking_feedback_on_user_id_unification_with/)**
*  **Summary:** The poster is seeking feedback on a user ID unification strategy using Spark/GraphX and Delta Lake.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   GraphX is deprecated in Apache Spark 4.0. GraphFrames should be used instead.
    *   N/A
    *   N/A

**[best way to implement data quality testing with clickhouse? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lbkgv0/best_way_to_implement_data_quality_testing_with/)**
*  **Summary:** The thread discusses the best ways to implement data quality testing within a Clickhouse environment.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   DBT test are super easy to setup given your models also parsed using DBT
    *   You can make materialized view which would track everytime a new data comes in. Otherwise just make a view.
    *   N/A

**[Has anyone implemented auto-segmentation for unstructured text? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lc11fa/has_anyone_implemented_autosegmentation_for/)**
*  **Summary:** The poster is looking for experiences and advice on implementing auto-segmentation for unstructured text data.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   LLM is used in hospitality and QSR industry. It is a data model to store final data. It uses domain specific categories for the industry within the prompt.
    *   N/A
    *   N/A

**[I need help with data analysis (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lbi4fh/i_need_help_with_data_analysis/)**
*  **Summary:** A user is requesting assistance with data analysis tasks.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   You need to be able to code to do this. I would ask Chatgpt and you can probably get somewhere close even if your a novice if you can clearly explain what you want.
    *   Depending on structure Excel has an excellent pdf importer, but needs table structure
    *   Mightymerge is a free and paid app that merges all the tables found in the pdf file into one file.

**[What Should I do ? Please help !! (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lbunhz/what_should_i_do_please_help/)**
*  **Summary:** The thread is a cry for career advice.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   It will be hard for you to get a good public University. People go for masters to germany for data science roles not for data engineering courses. Try to learn by yourself and switch to data engineering.
    *   In this market, I would keep my job and learn DE in background (working on actual projects, building your git) and then try to switch to a junior DE/DA role.
    *   Try asking at r/developersIndia, you might find something great.

**[PageRank, simillars/alternatives and Search Engines (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lbuv0p/pagerank_simillarsalternatives_and_search_engines/)**
*  **Summary:** This thread seems to be about PageRank algorithm and search engine alternatives.
*  **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   N/A
    *   N/A
    *   N/A

**[Built a binary-structured database that writes and reads 1M records in 3s using <1.1GB RAM (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lc234x/built_a_binarystructured_database_that_writes_and/)**
*  **Summary:** A user presents a new database they built with claimed performance benefits.
*  **Emotion:** The overall emotional tone is negative.
*  **Top 3 Points of View:**
    *   Cool. How do you plan to scale up to trillions of rows. How do you plan to handle billions by billions of rows in a join?
    *   1)1M records is small dataset. 2)With fast storage and good CPU Postgres will be even faster. 3 seconds for 1.1 Gb  = 360mb/s disk write literally slower than single SATA ssd. 3)Ram usage sounds just wrong
    *   If you don’t index, how do you write deterministically? It sounds like the very act of writing is indexing in your scheme

**[New to Data Science/Data Analysis— Which Enterprise Tool Should I Learn First? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lc2us0/new_to_data_sciencedata_analysis_which_enterprise/)**
*  **Summary:** The user is seeking advice on which enterprise tool to learn first as a newcomer to Data Science/Data Analysis.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   N/A
    *   N/A
    *   N/A

**[Is there a cursor for us DATA folks? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lc9afx/is_there_a_cursor_for_us_data_folks/)**
*  **Summary:** The thread is about the Cursor IDE.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   We use cursor for our python and dbt code at my job and it seems fine.
    *   N/A
    *   N/A
