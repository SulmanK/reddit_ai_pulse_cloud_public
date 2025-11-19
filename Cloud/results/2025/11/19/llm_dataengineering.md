---
title: "Data Engineering Subreddit"
date: "2025-11-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1. [[D] Apache Iceberg and Databricks Delta Lake - benchmarked](https://www.reddit.com/r/dataengineering/comments/1p10z2v/apache_iceberg_and_databricks_delta_lake/) (Score: 47)
    * The discussion is centered around the benchmarking of Apache Iceberg and Databricks Delta Lake, comparing their performance and interoperability, especially within the Databricks environment.
2.  [Seeing every Spark job and fixing the right things first. ANY SUGGESTIONS?](https://www.reddit.com/r/dataengineering/comments/1p135h9/seeing_every_spark_job_and_fixing_the_right/) (Score: 18)
    * This thread is about suggestions on how to gain visibility into Spark jobs, identify performance bottlenecks, and prioritize optimization efforts within a company.
3.  [Unpopular opinion: Most "Data Governance Frameworks" are just bureaucracy. Here is a model that might actually work (federated/active)](https://www.reddit.com/r/dataengineering/comments/1p18o83/unpopular_opinion_most_data_governance_frameworks/) (Score: 12)
    * The post discusses the ineffectiveness of traditional data governance frameworks and proposes an alternative federated/active model.
4.  [Documentation Standards for Data pipelines](https://www.reddit.com/r/dataengineering/comments/1p16h5h/documentation_standards_for_data_pipelines/) (Score: 8)
    * The discussion focuses on documentation standards for data pipelines, with specific reference to DBTs yaml specs for Sources, materializations and exposures.
5.  [BigQuery vs Snowflake](https://www.reddit.com/r/dataengineering/comments/1p19klu/bigquery_vs_snowflake/) (Score: 8)
    * This thread compares BigQuery and Snowflake, focusing on migration considerations, cost savings, performance, and user experience.
6.  [Fabric Workspaces](https://www.reddit.com/r/dataengineering/comments/1p14kj1/fabric_workspaces/) (Score: 7)
    * Discussion about using single production workspaces for all data layers, while promoting feature workspaces as required and use feature branches in your repo.
7.  [Reality Vs Expectation: Data Engineering as my first job](https://www.reddit.com/r/dataengineering/comments/1p1bxzu/reality_vs_expectation_data_engineering_as_my/) (Score: 6)
    * This thread explores the gap between the expectations and reality of a first job in data engineering, covering topics like documentation quality, company culture, and workload stress.
8.  [It's a bad practice doing lot joins in a gold layer table from silver tables? (+10 joins)](https://www.reddit.com/r/dataengineering/comments/1p18fwe/its_a_bad_practice_doing_lot_joins_in_a_gold/) (Score: 2)
    * Discussion on the practice of performing multiple joins in a gold layer table, questioning whether it is advisable or indicative of a flawed data modeling approach.
9.  [Is Devart SQL Tools actually better for daily SQL Server work than using SSMS alone?](https://www.reddit.com/r/dataengineering/comments/1p18eq4/is_devart_sql_tools_actually_better_for_daily_sql/) (Score: 2)
    * This thread discusses the comparison between Devart SQL Tools and SSMS for daily SQL Server work.
10. [How do you Postgres CDC into vector database](https://www.reddit.com/r/dataengineering/comments/1p1ek48/how_do_you_postgres_cdc_into_vector_database/) (Score: 2)
    * This thread is about Change Data Capture (CDC) from Postgres into a vector database, covering DIY approaches and managed solutions.
11. [OOP with Python](https://www.reddit.com/r/dataengineering/comments/1p1j82e/oop_with_python/) (Score: 2)
    * This post discusses the use of Object-Oriented Programming (OOP) with Python in data engineering contexts, where functional programming is more effective.
12. [Need help with database schema for a twitter like social media app](https://www.reddit.com/r/dataengineering/comments/1p17wag/need_help_with_database_schema_for_a_twitter_like/) (Score: 1)
    * This thread seeks help with the design of a database schema for a social media application.
13. [Need recommendations for solid profile and content review. DE Manager +  Architect, potential layoff coming.](https://www.reddit.com/r/dataengineering/comments/1p1dx1y/need_recommendations_for_solid_profile_and/) (Score: 1)
    * This post is asking for recommendations for profile and content review services, specifically for a Data Engineering Manager/Architect facing a potential layoff.
14. [Ex-Data Engineer (SAP BODS) - How do i get back into this?](https://www.reddit.com/r/dataengineering/comments/1p1hkaj/exdata_engineer_sap_bods_how_do_i_get_back_into/) (Score: 1)
    * This thread asks for guidance on how an ex-Data Engineer with SAP BODS experience can re-enter the field.

# Detailed Analysis by Thread
**[[D] Apache Iceberg and Databricks Delta Lake - benchmarked (Score: 47)](https://www.reddit.com/r/dataengineering/comments/1p10z2v/apache_iceberg_and_databricks_delta_lake/)**
*   **Summary:** The discussion revolves around benchmarking Apache Iceberg and Databricks Delta Lake. Key points include questioning the objectivity of the benchmarks, emphasizing the native interoperability of both technologies within Databricks, and debating the automatic Spark tuning capabilities of Databricks. Comparisons with DuckDB are also mentioned.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral, with comments primarily focused on technical analysis and comparison.
*   **Top 3 Points of View:**
    *   The benchmark may be biased.
    *   Iceberg and Delta Lake work natively on Databricks with full interoperability.
    *   The claim of automatic Spark tuning in Databricks is questionable.

**[Seeing every Spark job and fixing the right things first. ANY SUGGESTIONS? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1p135h9/seeing_every_spark_job_and_fixing_the_right/)**
*   **Summary:**  The thread is seeking suggestions for gaining visibility into Spark jobs and prioritizing optimization. Recommendations include focusing on the heaviest stages, combining Spark's built-in metrics with external tracking, and prioritizing the 20% of stages causing 80% of the cost. Open-source tools like Dataflint are also mentioned.
*   **Emotion:** The emotional tone of the thread is Neutral, mainly focusing on providing practical advice.
*   **Top 3 Points of View:**
    *   Focus on pruning noise and the heaviest stages first.
    *   Combine Spark's built-in metrics with external tracking for cost visibility.
    *   Prioritize the 20% of stages causing 80% of the cost.

**[Unpopular opinion: Most "Data Governance Frameworks" are just bureaucracy. Here is a model that might actually work (federated/active) (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1p18o83/unpopular_opinion_most_data_governance_frameworks/)**
*   **Summary:**  The discussion is centered on the ineffectiveness of traditional data governance frameworks. Points raised include the need for executive sponsorship, clear policies, integrating compliance into measurable goals and the importance of hands-on governance teams. It touches on the importance of programmatic embedding of governance into pipelines and relationship building.
*   **Emotion:** The emotional tone is mixed, with Neutral and Positive sentiments. Some comments express frustration with current frameworks while others support alternative approaches.
*   **Top 3 Points of View:**
    *   Traditional data governance is often bureaucratic and ineffective.
    *   A federated/active model with executive sponsorship and measurable goals might be more effective.
    *   Data governance needs to be programmatic and embedded into pipelines, not just a technical problem.

**[Documentation Standards for Data pipelines (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1p16h5h/documentation_standards_for_data_pipelines/)**
*   **Summary:**  This thread discusses documentation standards for data pipelines, referencing DBT's YAML specs and proposing a phased approach for gathering the "full chain" of documentation. It emphasizes the value of understanding data and using tools accepted everywhere for data portability.
*   **Emotion:** The emotional tone is Neutral, primarily informative and advice-oriented.
*   **Top 3 Points of View:**
    *   Use a phased approach to gather the "full chain" of documentation.
    *   Utilize DBT YAML specs for sources, materializations, and exposures.
    *   Work towards "impact reports" to show the value of documentation.

**[BigQuery vs Snowflake (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1p19klu/bigquery_vs_snowflake/)**
*   **Summary:**  The discussion compares BigQuery and Snowflake, covering migration costs, Google's discount offers, database IDEs, analytics integration, and the benefits of proof-of-concept migrations. The consensus is that both products have their advantages and drawbacks and it is important to pick the right choice for the team's requirements.
*   **Emotion:** The emotional tone is mixed with Neutral and Positive sentiments, with users sharing both positive and negative experiences with both platforms.
*   **Top 3 Points of View:**
    *   Consider the opportunity costs and efforts when migrating from Snowflake to BigQuery
    *   BigQuery can be more cost-efficient with proper training and data modeling.
    *   Snowflake has a better UI/UX and a better ecosystem around, but BigQuery has advantages for Google Analytics integration.

**[Fabric Workspaces (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1p14kj1/fabric_workspaces/)**
*   **Summary:** Discussion about using single production workspaces for all data layers, while promoting feature workspaces as required and use feature branches in your repo.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Use one prod workspace for all data layers, with folders and subfolders.
    *   Don't use static dev/test workspaces.
    *   Spin up feature workspaces as required and use feature branches in your repo.

**[Reality Vs Expectation: Data Engineering as my first job (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p1bxzu/reality_vs_expectation_data_engineering_as_my/)**
*   **Summary:** This thread explores the gap between the expectations and reality of a first job in data engineering. Common issues include poor documentation, a hit or miss company culture, and high workload. However it is considered a normal and typical entry level experience.
*   **Emotion:** Negative
*   **Top 3 Points of View:**
    *   The work is typical for an entry level Data Engineer.
    *   Poor documentation is common in data engineering.
    *   Work is work. It might be good, it might be bad, and you never know where it is going to take you.

**[It's a bad practice doing lot joins in a gold layer table from silver tables? (+10 joins) (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p18fwe/its_a_bad_practice_doing_lot_joins_in_a_gold/)**
*   **Summary:** Discussion on whether it's a bad practice to do many joins in a gold layer table from silver tables.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The practice isn't necessarily bad if the gold layer table is business facing.
    *   Bronze is raw, gold is what the consumers want, silver is building blocks.
    *   Modeling practices are crucial.

**[Is Devart SQL Tools actually better for daily SQL Server work than using SSMS alone? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p18eq4/is_devart_sql_tools_actually_better_for_daily_sql/)**
*   **Summary:** Comparison of Devart SQL Tools and SSMS for daily SQL Server work.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   SSMS is sufficient for daily work, especially with SSMS 21.
    *   Try DataGrip.

**[How do you Postgres CDC into vector database (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p1ek48/how_do_you_postgres_cdc_into_vector_database/)**
*   **Summary:** This thread covers methods for Change Data Capture (CDC) from Postgres into a vector database.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Use Debezium and Kafka.
    *   DIY pattern involves logical replication, a queue, and a worker service.
    *   Managed solutions like Estuary handle ordering, retries, and replication.

**[OOP with Python (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p1j82e/oop_with_python/)**
*   **Summary:** Discussion on the use of Object-Oriented Programming (OOP) with Python in data engineering.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Data engineering is primarily functional programming, not OOP.

**[Need help with database schema for a twitter like social media app (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p17wag/need_help_with_database_schema_for_a_twitter_like/)**
*   **Summary:** Seeking assistance with designing a database schema for a social media app.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Keep the schema simple for easy maintenance.

**[Need recommendations for solid profile and content review. DE Manager +  Architect, potential layoff coming. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p1dx1y/need_recommendations_for_solid_profile_and/)**
*   **Summary:** Asking for recommendations for profile and content review services due to a potential layoff.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Use LinkedIn.

**[Ex-Data Engineer (SAP BODS) - How do i get back into this? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p1hkaj/exdata_engineer_sap_bods_how_do_i_get_back_into/)**
*   **Summary:** Seeking guidance on re-entering the data engineering field after working with SAP BODS.
*   **Emotion:** Positive
*   **Top 3 Points of View:**
    *   Focus on picking up skills through self-learning and hands-on experience.
