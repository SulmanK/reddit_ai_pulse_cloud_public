---
title: "Data Engineering Subreddit"
date: "2025-08-15"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "snowflake", "career"]
---

# Overall Ranking and Top Discussions
1.  [Medallion layers in Snowflake](https://www.reddit.com/r/dataengineering/comments/1mqk0ja/medallion_layers_in_snowflake/) (Score: 20)
    *   The thread discusses the implementation of medallion layers in Snowflake, focusing on database and schema setup, role-based access controls, and potential issues with access permissions.
2.  [A deep dive into what an ORM for OLAP databases (like ClickHouse) could look like.](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm) (Score: 17)
    *   The thread is about the need for ORMs (Object-Relational Mappers) in OLAP (Online Analytical Processing) databases like ClickHouse.
3.  [How to Get Started](https://www.reddit.com/r/dataengineering/comments/1mqymkf/how_to_get_started/) (Score: 15)
    *   The thread discusses ways for individuals to transition into data engineering roles, including building a portfolio, leveraging existing positions, and exploring learning resources.
4.  [How do you implement data governance in your pipelines?, what measures do you take to ensure data governance is in place?](https://www.reddit.com/r/dataengineering/comments/1mqmxt1/how_do_you_implement_data_governance_in_your/) (Score: 10)
    *   The discussion focuses on implementing data governance in data pipelines, including measures such as PI (Personally Identifiable Information) checks, data lineage, metadata-driven models, naming conventions, and role-based access control.
5.  [Experience - Data Analyst technical round](https://www.reddit.com/r/dataengineering/comments/1mqre6h/experience_data_analyst_technical_round/) (Score: 8)
    *   The thread discusses experiences in data analyst technical interviews, focusing on SQL problems, interview skills, and resources for preparation.
6.  [The "dilemma" in the cost centre vs. profit centre separation](https://www.reddit.com/r/dataengineering/comments/1mqvctx/the_dilemma_in_the_cost_centre_vs_profit_centre/) (Score: 7)
    *   The thread discusses the differences between cost centers and profit centers, especially in the context of data engineering, and how these designations impact budget allocations, job security, and business value.
7.  [Why does transactional date serve as a good delta value for an incremental load?](https://www.reddit.com/r/dataengineering/comments/1mqx9qs/why_does_transactional_date_serve_as_a_good_delta/) (Score: 7)
    *   The discussion explains the use of transactional date as a delta value for incremental loads in data pipelines, emphasizing its reliability and the handling of change data capture (CDC) records.
8.  [Custom numeric type in PostgreSQL](https://www.reddit.com/r/dataengineering/comments/1mr4hsf/custom_numeric_type_in_postgresql/) (Score: 3)
    *   The thread explores different solutions to approach custom numeric types in PostgreSQL such as leveraging stored procedures.
9.  [Starting AWS Associate Data Engineer Course](https://www.reddit.com/r/dataengineering/comments/1mr77m0/starting_aws_associate_data_engineer_course/) (Score: 3)
    *   The thread is about starting AWS Associate Data Engineer Course. The advice is to check out community learning resources.
10. [Questions about career path](https://www.reddit.com/r/dataengineering/comments/1mqmwjm/questions_about_career_path/) (Score: 2)
    *   The thread discusses strategies for advancing a data engineering career, including building personal projects, pursuing a master's degree, and showcasing skills in specific technologies.
11. [How would experienced engineers approach this business problem?](https://www.reddit.com/r/dataengineering/comments/1mqtkrf/how_would_experienced_engineers_approach_this/) (Score: 2)
    *   The discussion focuses on how experienced data engineers would approach a business problem related to tracking costs and inventory in a small business, with suggestions ranging from basic inventory systems to more advanced data analysis tools.
12. [MCP for third-party data integration - anyone tried it?](https://www.reddit.com/r/dataengineering/comments/1mqui5z/mcp_for_thirdparty_data_integration_anyone_tried/) (Score: 2)
    *   The thread explores the use of MCP (likely referring to a specific tool or method) for third-party data integration, with recommendations against direct database connections and suggestions for alternative approaches such as using APIs and data sharing platforms.
13. [Which of these SQLite / SQLCipher pain points would you want solved?](https://www.reddit.com/r/dataengineering/comments/1mqrrcn/which_of_these_sqlite_sqlcipher_pain_points_would/) (Score: 1)
    *   The thread discusses pain points related to using SQLite and SQLCipher, and questions whether data engineering is being performed correctly.
14. [Good Text-To-SQL solutions?](https://www.reddit.com/r/dataengineering/comments/1mr31nz/good_texttosql_solutions/) (Score: 1)
    *   The thread discusses GraphRAG and Snowflake investments in building text-to-sql offering. It also covers tools for communicating data structures to the LLM.
15. [How to build a pipeline that supports extraction of so many different data types from data source?](https://www.reddit.com/r/dataengineering/comments/1mr7kg8/how_to_build_a_pipeline_that_supports_extraction/) (Score: 1)
    *   The thread discusses how to build a data pipeline that supports extraction from various data sources and types, with the general consensus being to process the data in common data structures such as Pandas, Polars, or PySpark and storing it in common data storage formats such as Delta Tables, SQLite, or Postgres.
16. [New Tech Stack to Pair with Snowflake - What would you choose?](https://www.reddit.com/r/dataengineering/comments/1mr7yvq/new_tech_stack_to_pair_with_snowflake_what_would/) (Score: 1)
    *   The thread discusses using Openflow, Fivetran/dbt or Airbyte with Snowflake.
17. [Conformed Dimensions Explained in 3 Minutes (For Busy Engineers)**](https://youtu.be/DFuVkLmNoQA?si=CGpqjDV9bs_xybEd) (Score: 1)
    *   The thread is about conformed dimensions and star schema.
18. [Seeking Opportunity: Aspiring Data Engineer/Analyst Looking to Take on Tasks](https://www.reddit.com/r/dataengineering/comments/1mqxz0a/seeking_opportunity_aspiring_data_engineeranalyst/) (Score: 0)
    *   The thread is about someone seeking opportunity. The responses mention security is a concern to allow someone take a look at actual company data and that working on projects has more positives than actual work.

# Detailed Analysis by Thread
**[Medallion layers in Snowflake (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1mqk0ja/medallion_layers_in_snowflake/)**
*   **Summary:** The thread discusses the implementation of medallion layers in Snowflake, focusing on database and schema setup, role-based access controls, and potential issues with access permissions.
*   **Emotion:** The overall emotional tone is neutral, with some positive comments.
*   **Top 3 Points of View:**
    *   There may be an issue with role-based access controls.
    *   It could be an issue with role based access controls.
    *   Medallion layers implementation with a separate DB for each environment.

**[A deep dive into what an ORM for OLAP databases (like ClickHouse) could look like. (Score: 17)](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm)**
*   **Summary:** The thread is about the need for ORMs (Object-Relational Mappers) in OLAP (Online Analytical Processing) databases like ClickHouse.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   ORMs are great

**[How to Get Started (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1mqymkf/how_to_get_started/)**
*   **Summary:** The thread discusses ways for individuals to transition into data engineering roles, including building a portfolio, leveraging existing positions, and exploring learning resources.
*   **Emotion:** The overall emotional tone is neutral and positive.
*   **Top 3 Points of View:**
    *   Try to lean your current position into data engineering projects if you have such freedom.
    *   Create a portfolio by ingesting data from reddit API into S3.
    *   Start applying and test the market.

**[How do you implement data governance in your pipelines?, what measures do you take to ensure data governance is in place? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1mqmxt1/how_do_you_implement_data_governance_in_your/)**
*   **Summary:** The discussion focuses on implementing data governance in data pipelines, including measures such as PI (Personally Identifiable Information) checks, data lineage, metadata-driven models, naming conventions, and role-based access control.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Apply data governance at the data model level with PI checks and data lineage.
    *   PI data should be checked from the model level and during DML.
    *   Need to create a document on AD groups, what roles, which tables access to be given to who and fields that need to be encrypted.

**[Experience - Data Analyst technical round (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1mqre6h/experience_data_analyst_technical_round/)**
*   **Summary:** The thread discusses experiences in data analyst technical interviews, focusing on SQL problems, interview skills, and resources for preparation.
*   **Emotion:** The overall emotional tone is positive and neutral.
*   **Top 3 Points of View:**
    *   Interviewing is a skill and the more you do it the better you become at it.
    *   Use roleraise.com

**[The "dilemma" in the cost centre vs. profit centre separation (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1mqvctx/the_dilemma_in_the_cost_centre_vs_profit_centre/)**
*   **Summary:** The thread discusses the differences between cost centers and profit centers, especially in the context of data engineering, and how these designations impact budget allocations, job security, and business value.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Data engineering teams almost never bring money directly into the business.
    *   If you’re not directly bringing in money, then you’re a cost.
    *   If the business unit you work in brings in more money than it costs, you are a profit centre.

**[Why does transactional date serve as a good delta value for an incremental load? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1mqx9qs/why_does_transactional_date_serve_as_a_good_delta/)**
*   **Summary:** The discussion explains the use of transactional date as a delta value for incremental loads in data pipelines, emphasizing its reliability and the handling of change data capture (CDC) records.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   There is a definite start and stop point for each batch.
    *   There is only one change record per row in the source database.

**[Custom numeric type in PostgreSQL (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mr4hsf/custom_numeric_type_in_postgresql/)**
*   **Summary:** The thread explores different solutions to approach custom numeric types in PostgreSQL such as leveraging stored procedures.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   You can just denote them as an int for an amount of a scale/currency pair.
    *   Create stored procedures to parse these types.

**[Starting AWS Associate Data Engineer Course (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mr77m0/starting_aws_associate_data_engineer_course/)**
*   **Summary:** The thread is about starting AWS Associate Data Engineer Course. The advice is to check out community learning resources.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Check out community learning resources

**[Questions about career path (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mqmwjm/questions_about_career_path/)**
*   **Summary:** The thread discusses strategies for advancing a data engineering career, including building personal projects, pursuing a master's degree, and showcasing skills in specific technologies.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   Learn fast at work.
    *   Pursue a master's degree.

**[How would experienced engineers approach this business problem? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mqtkrf/how_would_experienced_engineers_approach_this/)**
*   **Summary:** The discussion focuses on how experienced data engineers would approach a business problem related to tracking costs and inventory in a small business, with suggestions ranging from basic inventory systems to more advanced data analysis tools.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Data engineering is gathering data from disparate sources and turning it into something useful.
    *   Implement a basic inventory system or ERP, or logging things in Excel.
    *   Basic data analysis could be enabled through Power BI or Excel charts.

**[MCP for third-party data integration - anyone tried it? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mqui5z/mcp_for_thirdparty_data_integration_anyone_tried/)**
*   **Summary:** The thread explores the use of MCP (likely referring to a specific tool or method) for third-party data integration, with recommendations against direct database connections and suggestions for alternative approaches such as using APIs and data sharing platforms.
*   **Emotion:** The overall emotional tone is neutral and negative.
*   **Top 3 Points of View:**
    *   MCP has zero relevance to this task
    *   Direct database connection is not a good idea because of isolation between operational and analytical systems.
    *   MCP is a way to connect a LLM with python functions that can do things.

**[Which of these SQLite / SQLCipher pain points would you want solved? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mqrrcn/which_of_these_sqlite_sqlcipher_pain_points_would/)**
*   **Summary:** The thread discusses pain points related to using SQLite and SQLCipher, and questions whether data engineering is being performed correctly.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Solve less bloat

**[Good Text-To-SQL solutions? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mr31nz/good_texttosql_solutions/)**
*   **Summary:** The thread discusses GraphRAG and Snowflake investments in building text-to-sql offering. It also covers tools for communicating data structures to the LLM.
*   **Emotion:** The overall emotional tone is positive and neutral.
*   **Top 3 Points of View:**
    *   GraphRAG is a graph query engine that can sit on top of your relational databases.
    *   Snowflake invested alot of time in building their text-to-sql offering
    *   Semantic models provide a framework to communicate the data structure and describe the data to the LLM

**[How to build a pipeline that supports extraction of so many different data types from data source? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mr7kg8/how_to_build_a_pipeline_that_supports_extraction/)**
*   **Summary:** The thread discusses how to build a data pipeline that supports extraction from various data sources and types, with the general consensus being to process the data in common data structures such as Pandas, Polars, or PySpark and storing it in common data storage formats such as Delta Tables, SQLite, or Postgres.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Process data in common data structures such as Pandas, Polars, or PySpark
    *   Store data in common data storage formats such as Delta Tables, SQLite, or Postgres.

**[New Tech Stack to Pair with Snowflake - What would you choose? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mr7yvq/new_tech_stack_to_pair_with_snowflake_what_would/)**
*   **Summary:** The thread discusses using Openflow, Fivetran/dbt or Airbyte with Snowflake.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Openflow?
    *   Fivetran/dbt.

**[Conformed Dimensions Explained in 3 Minutes (For Busy Engineers)** (Score: 1)](https://youtu.be/DFuVkLmNoQA?si=CGpqjDV9bs_xybEd)**
*   **Summary:** The thread is about conformed dimensions and star schema.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   It's still a denormalized star Schema, so it's not a snowflake.

**[Seeking Opportunity: Aspiring Data Engineer/Analyst Looking to Take on Tasks (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mqxz0a/seeking_opportunity_aspiring_data_engineeranalyst/)**
*   **Summary:** The thread is about someone seeking opportunity. The responses mention security is a concern to allow someone take a look at actual company data and that working on projects has more positives than actual work.
*   **Emotion:** The overall emotional tone is negative and neutral.
*   **Top 3 Points of View:**
    *   Security is a concern to allow someone take a look at actual company data.
    *   Working on projects has more positives than actual work.
