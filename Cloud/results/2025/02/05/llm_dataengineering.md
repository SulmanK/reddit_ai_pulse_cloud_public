---
title: "Data Engineering Subreddit"
date: "2025-02-05"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ETL", "data warehouse"]
---

# Overall Ranking and Top Discussions
1.  [[D] IT hiring and salary trends in Europe (18'000 jobs, 68'000 surveys)](https://www.reddit.com/r/dataengineering/comments/1iib0r8/it_hiring_and_salary_trends_in_europe_18000_jobs/) (Score: 67)
    *   Discussing IT hiring and salary trends in Europe based on a survey of 18,000 jobs and 68,000 surveys.
2.  [When your company shifted away from AWS Glue, which ETL tools did you shift to?](https://www.reddit.com/r/dataengineering/comments/1iie373/when_your_company_shifted_away_from_aws_glue/) (Score: 22)
    *   Discussing alternative ETL tools to AWS Glue and the limitations encountered with Glue.
3.  [Incrementally replicate hundreds of tables from MySQL and SQL Server into Snwoflake.](https://www.reddit.com/r/dataengineering/comments/1ii8bze/incrementally_replicate_hundreds_of_tables_from/) (Score: 17)
    *   Discussing strategies and tools for incrementally replicating hundreds of tables from MySQL and SQL Server into Snowflake.
4.  [How do you deal with heavy workload?](https://www.reddit.com/r/dataengineering/comments/1ii7c9z/how_do_you_deal_with_heavy_workload/) (Score: 14)
    *   Discussing strategies and approaches for managing heavy workloads in data engineering roles.
5.  [How to Gain Hands-on Experience in DE Without High Cloud Costs?](https://www.reddit.com/r/dataengineering/comments/1iidu03/how_to_gain_handson_experience_in_de_without_high/) (Score: 12)
    *   Discussing ways to gain practical data engineering experience without incurring high costs on cloud platforms.
6.  [What Data Warehouse & ETL Stack Would You Use for a 600-Employee Company?](https://www.reddit.com/r/dataengineering/comments/1iigqxk/what_data_warehouse_etl_stack_would_you_use_for_a/) (Score: 12)
    *   Discussing suitable data warehouse and ETL stacks for a company with 600 employees.
7.  [Data Lakes For Complete Noobs: What They Are and Why The *** You Need Them](https://datagibberish.com/p/what-are-data-lakes-and-why-you-need-them) (Score: 10)
    *   A noob says that they really enjoyed the reading. Thank you!
8.  [Fivetran: from AWS Postgres to GCP Snowflake - Slow!](https://www.reddit.com/r/dataengineering/comments/1iibzlp/fivetran_from_aws_postgres_to_gcp_snowflake_slow/) (Score: 5)
    *   Discussing performance issues with Fivetran when moving data from AWS Postgres to GCP Snowflake.
9.  [Incrementally replicate hundreds of tables from MySQL and SQL Server into Snwoflake.](https://www.reddit.com/r/dataengineering/comments/1ii8byy/incrementally_replicate_hundreds_of_tables_from/) (Score: 4)
    *   Discussing strategies and tools for incrementally replicating hundreds of tables from MySQL and SQL Server into Snowflake.
10. [We built a free Databricks System Tables Queries and Dashboard to help users manage and optimize Databricks costs - feedback welcome!](https://www.reddit.com/r/dataengineering/comments/1iiclek/we_built_a_free_databricks_system_tables_queries/) (Score: 4)
    *   A bot says you can find community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources
11. [Strategies to reduce re-sync times from database to data warehouse?](https://www.reddit.com/r/dataengineering/comments/1iij2jt/strategies_to_reduce_resync_times_from_database/) (Score: 4)
    *   A discussion about strategies to reduce re-sync times from database to data warehouse.
12. [I built RepoTEN, a user-friendly simple data management platform for data analysts](https://www.reddit.com/r/dataengineering/comments/1iidaqk/i_built_repoten_a_userfriendly_simple_data/) (Score: 3)
    *   A discussion about a user-friendly simple data management platform for data analysts.
13. [Resources to learn differences between different types of databases and their use cases](https://www.reddit.com/r/dataengineering/comments/1iiataz/resources_to_learn_differences_between_different/) (Score: 2)
    *   A discussion about resources to learn differences between different types of databases and their use cases.
14. [I am studying data science engineering](https://www.reddit.com/r/dataengineering/comments/1iihy50/i_am_studying_data_science_engineering/) (Score: 1)
    *   Just clarifying that data science and data engineering aren’t the same thing.

# Detailed Analysis by Thread
**[[D] IT hiring and salary trends in Europe (18'000 jobs, 68'000 surveys)](https://www.reddit.com/r/dataengineering/comments/1iib0r8/it_hiring_and_salary_trends_in_europe_18000_jobs/) (Score: 67)**
*   **Summary:** The thread discusses IT hiring and salary trends in Europe, based on a report analyzing 18,000 jobs and 68,000 surveys. Users question specific data points, such as Belfast's high ranking in the UK, the absence of Italy in the report, and whether the jobs listed offer visa sponsorships. There is also discussion around the salary differences between Europe and the US.
*   **Emotion:** The overall emotional tone is Neutral, with users primarily seeking clarification and offering explanations related to the presented data.
*   **Top 3 Points of View:**
    *   The report's data on specific regions (e.g., Belfast) might be skewed.
    *   The exclusion of certain countries (e.g., Italy) from the report raises questions about the study's scope.
    *   European IT salaries are lower than US salaries, prompting curiosity about the reasons and general satisfaction with these salaries.

**[When your company shifted away from AWS Glue, which ETL tools did you shift to?](https://www.reddit.com/r/dataengineering/comments/1iie373/when_your_company_shifted_away_from_aws_glue/) (Score: 22)**
*   **Summary:** Users are discussing their experiences with migrating away from AWS Glue for ETL processes, exploring alternative tools and the reasons for their choice. Recommendations include Databricks, Dagster+Trino, Apache Hop, and Fabric’s version of ADF, while some suggest rethinking architecture before moving away from Glue. There is also a comment strongly advising against moving to Foundry.
*   **Emotion:** The emotional tone is mixed, with both Positive (recommendations, success stories) and Negative (disagreement, strong discouragement of certain solutions) signals, but overall it leans Neutral as the conversation focuses on technical aspects.
*   **Top 3 Points of View:**
    *   Databricks is a viable alternative to AWS Glue.
    *   Apache Hop is a good open-source drag-and-drop ETL tool.
    *   Moving to Foundry is strongly discouraged.

**[Incrementally replicate hundreds of tables from MySQL and SQL Server into Snwoflake.](https://www.reddit.com/r/dataengineering/comments/1ii8bze/incrementally_replicate_hundreds_of_tables_from/) (Score: 17)**
*   **Summary:** The thread discusses methods and tools for incrementally replicating data from MySQL and SQL Server databases into Snowflake. Suggestions include using Debezium, Apache Iceberg, AWS DMS, Apache NiFi, Snowflake sink connector, and Estuary.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Debezium and Apache Iceberg can be used for the replication process.
    *   AWS DMS is a viable option.
    *   Estuary offers no-code connectors for the replication.

**[How do you deal with heavy workload?](https://www.reddit.com/r/dataengineering/comments/1ii7c9z/how_do_you_deal_with_heavy_workload/) (Score: 14)**
*   **Summary:** The thread discusses strategies for dealing with heavy workloads, particularly in data engineering. Suggestions include prioritizing tasks with a manager's input, setting realistic timescales, creating visual project boards, saying "no" to new work, analyzing workload to justify hiring needs, and focusing on minimum viable products to avoid scope creep.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Prioritize tasks and get sign-off from your manager.
    *   Communicate workload and resource constraints to stakeholders.
    *   Deliver minimum viable products to avoid scope creep.

**[How to Gain Hands-on Experience in DE Without High Cloud Costs?](https://www.reddit.com/r/dataengineering/comments/1iidu03/how_to_gain_handson_experience_in_de_without_high/) (Score: 12)**
*   **Summary:** The discussion revolves around gaining practical experience in data engineering without incurring significant cloud costs. The recommendations include abusing free tiers, using open-source tools like Apache Spark and Postgres on local machines, using Databricks Community Edition, and creating a full stack DE setup in a low-cost server. There is an emphasis on learning fundamentals (Python, SQL, DBT) and building small projects.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Utilize free tiers offered by cloud providers.
    *   Focus on open-source tools and local setups.
    *   Learn Python, SQL, and DBT.

**[What Data Warehouse & ETL Stack Would You Use for a 600-Employee Company?](https://www.reddit.com/r/dataengineering/comments/1iigqxk/what_data_warehouse_etl_stack_would_you_use_for_a/) (Score: 12)**
*   **Summary:** The thread discusses suitable data warehouse and ETL stacks for a 600-employee company, considering factors like cost-effectiveness, current skills, and data volume. Options mentioned include Databricks, Snowflake, BigQuery, Firebolt, DuckDB, Redshift, and tools like Airflow, dbt, Dagster, Collibra, and Alation. Users also emphasize the importance of understanding the company's specific needs and skills before making a recommendation.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Databricks is a solid choice but may require specialized skills.
    *   BigQuery is cost-effective and light on administration.
    *   Airflow can be used to orchestrate dbt jobs.

**[Data Lakes For Complete Noobs: What They Are and Why The *** You Need Them](https://datagibberish.com/p/what-are-data-lakes-and-why-you-need-them) (Score: 10)**
*   **Summary:** A user enjoyed reading a post called "Data Lakes For Complete Noobs: What They Are and Why The *** You Need Them".
*   **Emotion:** The emotional tone is Positive.
*   **Top 3 Points of View:**
    *   The post was found helpful for data lake beginners.

**[Fivetran: from AWS Postgres to GCP Snowflake - Slow!](https://www.reddit.com/r/dataengineering/comments/1iibzlp/fivetran_from_aws_postgres_to_gcp_snowflake_slow/) (Score: 5)**
*   **Summary:** Users discuss performance issues with Fivetran when moving data from AWS Postgres to GCP Snowflake. The discussion covers CDC-based tools and logical replication methods.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Switch to alternatives if Fivetran is not helping.
    *   Use logical replication method.
    *   Use CDC-based tools to follow changes.

**[Incrementally replicate hundreds of tables from MySQL and SQL Server into Snwoflake.](https://www.reddit.com/r/dataengineering/comments/1ii8byy/incrementally_replicate_hundreds_of_tables_from/) (Score: 4)**
*   **Summary:** Users discuss the process of incrementally replicating hundreds of tables from MySQL and SQL Server into Snowflake.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Check native Snowflake MySQL connector.

**[We built a free Databricks System Tables Queries and Dashboard to help users manage and optimize Databricks costs - feedback welcome!](https://www.reddit.com/r/dataengineering/comments/1iiclek/we_built_a_free_databricks_system_tables_queries/) (Score: 4)**
*   **Summary:** A bot shared a link to community-submitted learning resources.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   There are community-submitted learning resources available at https://dataengineering.wiki/Learning+Resources.

**[Strategies to reduce re-sync times from database to data warehouse?](https://www.reddit.com/r/dataengineering/comments/1iij2jt/strategies_to_reduce_resync_times_from_database/) (Score: 4)**
*   **Summary:** Strategies to reduce re-sync times from database to data warehouse.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Implementing Change Data Capture (CDC) can help reduce the need for full reloads.

**[I built RepoTEN, a user-friendly simple data management platform for data analysts](https://www.reddit.com/r/dataengineering/comments/1iidaqk/i_built_repoten_a_userfriendly_simple_data/) (Score: 3)**
*   **Summary:** Discussion about a data management platform for data analysts.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   RepoTen may be a solid solution for teams dealing with dataset chaos
    *   Users asked if it was a catalog

**[Resources to learn differences between different types of databases and their use cases](https://www.reddit.com/r/dataengineering/comments/1iiataz/resources_to_learn_differences_between_different/) (Score: 2)**
*   **Summary:** Users are asking for resources to learn about different types of databases.
*   **Emotion:** The emotional tone is Positive.
*   **Top 3 Points of View:**
    *   Check out the Community Learning Resources https://dataengineering.wiki/Learning+Resources
    *   DDIA is a good book for system design

**[I am studying data science engineering](https://www.reddit.com/r/dataengineering/comments/1iihy50/i_am_studying_data_science_engineering/) (Score: 1)**
*   **Summary:** A discussion clarifying data science and data engineering.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Data science and data engineering are not the same thing.
