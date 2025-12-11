---
title: "Data Engineering Subreddit"
date: "2025-10-31"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Why do ml teams keep treating infrastructure like an afterthought?](https://www.reddit.com/r/dataengineering/comments/1okq7tm/why_do_ml_teams_keep_treating_infrastructure_like/) (Score: 112)
    * Discussing why machine learning teams often neglect infrastructure considerations.
2.  [Interesting Links in Data Engineering - October 2025](https://www.reddit.com/r/dataengineering/comments/1okxs7r/interesting_links_in_data_engineering_october_2025/) (Score: 20)
    *  Sharing and appreciating interesting links related to data engineering.
3.  [Handling Semi-Structured Data at Scale: What’s Worked for You?](https://www.reddit.com/r/dataengineering/comments/1okq6mu/handling_semistructured_data_at_scale_whats/) (Score: 11)
    *  Discussing approaches to handling semi-structured data at scale, including using Postgres, Parquet, BigQuery, and Snowflake.
4.  [Database Design for Beginners: How not to overthink?](https://www.reddit.com/r/dataengineering/comments/1oksihc/database_design_for_beginners_how_not_to_overthink/) (Score: 7)
    *  Offering advice for beginners on database design, focusing on avoiding over-complication.
5.  [What is your best metaphor for DE?](https://www.reddit.com/r/dataengineering/comments/1okshm9/what_is_your_best_metaphor_for_de/) (Score: 7)
    * Sharing metaphors for the role of a data engineer.
6.  [Data catalog that also acts as metadata catalog](https://www.reddit.com/r/dataengineering/comments/1okvhyc/data_catalog_that_also_acts_as_metadata_catalog/) (Score: 7)
    * Discussing data catalogs that can also function as metadata catalogs, highlighting features and options.
7. [How do you define, Raw - Silver - Gold](https://www.reddit.com/r/dataengineering/comments/1ol22zz/how_do_you_define_raw_silver_gold/) (Score: 5)
    * Discussing the definitions of Raw, Silver, and Gold data layers in data architecture.
8. [Adding shards to increase (speed up) query performance | Clickhouse.](https://www.reddit.com/r/dataengineering/comments/1okdu9q/adding_shards_to_increase_speed_up_query/) (Score: 4)
    * Seeking advice on using sharding in ClickHouse to improve query performance.
9. [Onprem data lakes: Who's engineering on them?](https://www.reddit.com/r/dataengineering/comments/1okuvgs/onprem_data_lakes_whos_engineering_on_them/) (Score: 2)
    * Discussing experiences with on-premises data lakes, including the reasons for choosing them and the challenges involved.
10. [Pasting SQL code into Chat GPT](https://www.reddit.com/r/dataengineering/comments/1ol4c9i/pasting_sql_code_into_chat_gpt/) (Score: 1)
    * Discussing the implications and potential risks of pasting SQL code into tools like ChatGPT.
11. [Transitioning from Coalesce.io to DBT](https://www.reddit.com/r/dataengineering/comments/1okarpo/transitioning_from_coalesceio_to_dbt/) (Score: 1)
    * Discussing the transition from Coalesce.io to DBT
12. [Noob question](https://www.reddit.com/r/dataengineering/comments/1okamkz/noob_question/) (Score: 1)
    * Asking a question regarding SSMS integration with databases.
13. [Would you use an open-source tool that gave "human-readable RCA" for pipeline failures?](https://www.reddit.com/r/dataengineering/comments/1oknspw/would_you_use_an_opensource_tool_that_gave/) (Score: 0)
    *  Considering the utility of an open-source tool that provides human-readable root cause analysis for pipeline failures.
14. [Need suggestions](https://www.reddit.com/r/dataengineering/comments/1okj885/need_suggestions/) (Score: 0)
    * Requesting advice on database setup and modeling for dashboards.
15. [Docker for Data Engineers](https://pipeline2insights.substack.com/p/docker-for-data-engineers) (Score: 0)
    * Sharing thoughts on docker setup.

# Detailed Analysis by Thread
**[[D] Why do ml teams keep treating infrastructure like an afterthought? (Score: 112)](https://www.reddit.com/r/dataengineering/comments/1okq7tm/why_do_ml_teams_keep_treating_infrastructure_like/)**
*  **Summary:**  The discussion revolves around the common issue of machine learning teams neglecting infrastructure. Many data scientists don't have formal training in software engineering best practices, leading to challenges in deploying and maintaining ML models. Solutions proposed include better communication, collaboration between data science and data engineering teams, and the adoption of MLOps practices. Management support in enforcing processes and standards is also emphasized.
*  **Emotion:** The overall emotional tone is Neutral. There are elements of frustration but the comments are mostly informative.
*  **Top 3 Points of View:**
    *   ML teams often lack software engineering skills and training in production infrastructure.
    *   Management should enforce processes that require data science teams to do proper pre-work and handovers.
    *   Positions like ML Engineer have emerged to bridge the gap between data science and infrastructure.

**[Interesting Links in Data Engineering - October 2025 (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1okxs7r/interesting_links_in_data_engineering_october_2025/)**
*  **Summary:**  This thread is a collection of interesting links related to data engineering, with users expressing gratitude and appreciation for the shared resources.
*  **Emotion:** The overall emotional tone is Positive, with users expressing thanks and finding the links helpful.
*  **Top 3 Points of View:**
    *   Shared links are appreciated.
    *   The links are interesting and useful.
    *   Users are thankful for the resources.

**[Handling Semi-Structured Data at Scale: What’s Worked for You? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1okq6mu/handling_semistructured_data_at_scale_whats/)**
*  **Summary:**  The discussion centers on the best approaches for handling semi-structured data at scale. The use of JSONB in Postgres, Parquet in data lakes, BigQuery, Snowflake, and columnar storage solutions are discussed. There's a focus on balancing flexibility with performance and cost.
*  **Emotion:** The overall emotional tone is Neutral. Users are sharing their experiences and offering technical solutions.
*  **Top 3 Points of View:**
    *   Postgres and Parquet are suitable for operational and analytical queries, respectively.
    *   BigQuery and Snowflake are convenient options for storing raw data as JSON or Variant.
    *   Columnar storage in a lakehouse is a scalable solution for semi-structured data.

**[Database Design for Beginners: How not to overthink? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1oksihc/database_design_for_beginners_how_not_to_overthink/)**
*  **Summary:**  This thread focuses on providing advice to beginners on database design, emphasizing simplicity and avoiding over-complication. Suggestions include starting with basic normalization, using version control, and understanding that designs can evolve.
*  **Emotion:** The overall emotional tone is Neutral, with helpful and informative advice being shared.
*  **Top 3 Points of View:**
    *   Start with simple designs and normalize up to 3NF.
    *   Use version control for schema evolution.
    *   Avoid trying to make the database perfect from the start; iterate based on real usage.

**[What is your best metaphor for DE? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1okshm9/what_is_your_best_metaphor_for_de/)**
*  **Summary:** Users share various metaphors for the role of a data engineer, including subway sandwich artist, scapegoat, janitor, librarian, plumber, firefighter, factories and Sisyphus.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Data engineers are like librarians, organizing and providing access to data.
    *   Data engineers are like janitors or garbage collectors, cleaning and managing data.
    *   Data engineers are like factories, turning raw data into useful products.

**[Data catalog that also acts as metadata catalog (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1okvhyc/data_catalog_that_also_acts_as_metadata_catalog/)**
*  **Summary:**  The discussion revolves around data catalogs that can also function as metadata catalogs. Open-source DataHub is mentioned as a potential solution.
*  **Emotion:** The overall emotional tone is Neutral, with a focus on technical details and potential solutions.
*  **Top 3 Points of View:**
    *   Having a data catalog that also acts as a metadata catalog is not common.
    *   Open-source DataHub is a possible solution.
    *   Integration of catalogs is also an option.

**[How do you define, Raw - Silver - Gold (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ol22zz/how_do_you_define_raw_silver_gold/)**
*  **Summary:** The discussion revolves around the definitions of Raw, Silver, and Gold data layers in the Medallion architecture.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Raw data should be append only and apply transformations only if absolutely necessary to get the data into the system.
    * Silver data should be transformed to get the data into a usable state in your platform.
    * Gold data is whatever you need to do to make the data available to customers or partners.

**[Adding shards to increase (speed up) query performance | Clickhouse. (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1okdu9q/adding_shards_to_increase_speed_up_query/)**
*  **Summary:** The discussion revolves around using sharding to increase query performance in ClickHouse.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * For time series queries, a single shard with more replicas would be best.
    * A single node performs better with double the resources compared to adding another node to the cluster with these resources.
    * For sharding you'll need a more complicated strategy.

**[Onprem data lakes: Who's engineering on them? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1okuvgs/onprem_data_lakes_whos_engineering_on_them/)**
*  **Summary:** The discussion revolves around on-premises data lakes and why some companies choose them over cloud solutions.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Legal and security reasons prevent some companies from using the cloud for data storage.
    * On-prem solutions can be cheaper and offer better performance than cloud solutions.
    * Some consider cloud is not as cheap or as reliable as your onprem can be.

**[Pasting SQL code into Chat GPT (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ol4c9i/pasting_sql_code_into_chat_gpt/)**
*  **Summary:** The discussion revolves around the implications and potential risks of pasting SQL code into tools like ChatGPT, particularly concerning data sensitivity and company policies.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Table and column names can be considered sensitive data, depending on the company's policies.
    * It's essential to check with managers and understand company AI policies before pasting code into public tools.
    * One can obfuscate sensitive data by replacing actual data with *** data while providing table structures to the LLM.

**[Transitioning from Coalesce.io to DBT (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1okarpo/transitioning_from_coalesceio_to_dbt/)**
*  **Summary:** The discussion is about how to transition from Coalesce.io to DBT.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Whatever you have in Coalesce, it wil not port to DBT, but you can do the same stuff using DBT and an orchestration platform.

**[Noob question (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1okamkz/noob_question/)**
*  **Summary:** The discussion is about SSMS integration with databases.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * You don't need SSMS to run queries programmatically.
    * SSMS is outdated and you should upgrade to SSMS 21.
    * You have to use SSIS and one of the available third-party extensions to get the data from different APIs.

**[Would you use an open-source tool that gave "human-readable RCA" for pipeline failures? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oknspw/would_you_use_an_opensource_tool_that_gave/)**
*  **Summary:** The discussion is about the utility of an open-source tool that provides human-readable root cause analysis for pipeline failures.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * You need to "shift left" — address issues in script, not in the logs.
    * Implementing an observability stack with central log collection, anomaly detection and automated problem analysis workflows will take hundreds of hours and requires a lot of infrastructure.
    * Is it working.

**[Need suggestions (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1okj885/need_suggestions/)**
*  **Summary:** The discussion is about database setup and modeling for dashboards.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * SharePoint folder plus power bi plus a ribbon chart.
    * You need to create a database table for grant type, a grant header table with all grants and a grant detail table for timestamped grants. Add tables to track Financials, End of Period, Beginning of Period stuff.

**[Docker for Data Engineers (Score: 0)](https://pipeline2insights.substack.com/p/docker-for-data-engineers)**
*  **Summary:** The discussion is about thoughts on docker setup.
*  **Emotion:** The overall emotional tone is Neutral, with some Positive.
*  **Top 3 Points of View:**
    * That is actually a pretty tight docker setup for out of the box dbt.
    *  Who the *** doesn’t know about Docker?

