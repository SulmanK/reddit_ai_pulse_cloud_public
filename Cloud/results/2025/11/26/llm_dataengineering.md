---
title: "Data Engineering Subreddit"
date: "2025-11-26"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] A small FaceSeek insight made me reconsider lightweight data flows](https://www.reddit.com/r/dataengineering/comments/1p784k1/a_small_faceseek_insight_made_me_reconsider/) (Score: 84)
    *   Discusses reconsidering lightweight data flows based on a FaceSeek insight.
2.  ["Are we there yet?" — Achieving the Ideal Data Science Hierarchy](https://www.reddit.com/r/dataengineering/comments/1p70jbm/are_we_there_yet_achieving_the_ideal_data_science/) (Score: 22)
    *   Explores the ideal data science hierarchy and whether it's realistically achievable in most organizations.
3.  [How many of you feel like the data engineers in your organization have too much work to keep up with?](https://www.reddit.com/r/dataengineering/comments/1p7fkop/how_many_of_you_feel_like_the_data_engineers_in/) (Score: 10)
    *   Addresses the workload and resource challenges faced by data engineers in various organizations.
4.  [Snowflake cortex agent MCP server](https://www.reddit.com/r/dataengineering/comments/1p6u7ir/snowflake_cortex_agent_mcp_server/) (Score: 10)
    *   Discusses the implementation and challenges of using Snowflake's Cortex agent MCP server.
5.  [Is it worth fine-tuning AI on internal company data?](https://www.reddit.com/r/dataengineering/comments/1p7607a/is_it_worth_finetuning_ai_on_internal_company_data/) (Score: 7)
    *   Debates the value and best practices for fine-tuning AI models using internal company data.
6.  [What's your favorite Iceberg Catalog?](https://www.reddit.com/r/dataengineering/comments/1p77i81/whats_your_favorite_iceberg_catalog/) (Score: 5)
    *   Asks for people's opinions and experiences with different Iceberg catalog implementations.
7.  [Aspiring Data Engineer – should I learn Go now or just stick to Python/PySpark? How do people actually learn the “data side” of Go?](https://www.reddit.com/r/dataengineering/comments/1p7ho3k/aspiring_data_engineer_should_i_learn_go_now_or/) (Score: 4)
    *   Discusses whether aspiring data engineers should learn Go, or focus on Python and PySpark.
8.  [Looking for a solution to dynamically copy all tables from Lakehouse to Warehouse](https://www.reddit.com/r/dataengineering/comments/1p6y5u1/looking_for_a_solution_to_dynamically_copy_all/) (Score: 3)
    *   Seeks advice on dynamically copying tables from a Lakehouse to a Warehouse, considering automation and schema changes.
9.  [Forcibly Alter Spark Plan](https://www.reddit.com/r/dataengineering/comments/1p790c0/forcibly_alter_spark_plan/) (Score: 3)
    *   Addresses methods to forcibly alter or simplify Spark execution plans.
10. [Sharepoint to Tableau Live](https://www.reddit.com/r/dataengineering/comments/1p6vnn5/sharepoint_to_tableau_live/) (Score: 2)
    *   Discusses methods to connect Sharepoint data to Tableau for live analysis.
11. [Considering an offer for DE II role, would love perspectives from DE/SWE folks](https://www.reddit.com/r/dataengineering/comments/1p6p35x/considering_an_offer_for_de_ii_role_would_love/) (Score: 1)
    *   Asks for advice on a data engineering job offer, weighing the pros and cons and potential career path.
12. [Structuring data analyses in academic projects](https://www.reddit.com/r/dataengineering/comments/1p7c4n4/structuring_data_analyses_in_academic_projects/) (Score: 1)
    *   Discusses how to structure data analyses in academic projects.
13. [How much data should I validate for “confidence”?](https://www.reddit.com/r/dataengineering/comments/1p7ht86/how_much_data_should_i_validate_for_confidence/) (Score: 0)
    *   Addresses the question of how much data should be validated to achieve a sufficient level of confidence.

# Detailed Analysis by Thread
**[[D] A small FaceSeek insight made me reconsider lightweight data flows (Score: 84)](https://www.reddit.com/r/dataengineering/comments/1p784k1/a_small_faceseek_insight_made_me_reconsider/)**
*  **Summary:** The thread discusses reconsidering lightweight data flows based on an insight from FaceSeek. It also includes a link to community-submitted learning resources for data engineering.
*  **Emotion:** The overall emotional tone is neutral, with sentiment scores around 0.53-0.86.
*  **Top 3 Points of View:**
    *   A minimal orchestration layer is preferred, splitting data pulling from the transformation layer unless complex normalization is needed.
    *   For simple data, delegate insights extraction to modeling tools like dbt and use pipelines only for data pulling.
    *   Avoid early optimization and focus on keeping the data flow simple, readable, and maintainable.

**[ "Are we there yet?" — Achieving the Ideal Data Science Hierarchy (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1p70jbm/are_we_there_yet_achieving_the_ideal_data_science/)**
*  **Summary:** The thread discusses the feasibility of achieving an ideal data science hierarchy in organizations, the overlapping roles of data engineers and data scientists, and whether data science is the primary consumer of data engineering.
*  **Emotion:** The overall emotional tone is neutral to slightly negative, with sentiment scores around 0.57-0.89.
*  **Top 3 Points of View:**
    *   The ideal data science hierarchy is not realistic because data engineers often lack the context to deliver useful datasets to data scientists.
    *   Most teams are far from the ideal pyramid, with data scientists often needing to do foundational data cleaning and stitching.
    *   The setup depends on the size of the company; larger companies are more likely to have specialized roles.

**[How many of you feel like the data engineers in your organization have too much work to keep up with? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1p7fkop/how_many_of_you_feel_like_the_data_engineers_in/)**
*  **Summary:** This thread discusses the challenges faced by data engineers who often have too much work to keep up with, and the reasons behind it, such as a lack of understanding of the value of data engineering and inadequate project oversight.
*  **Emotion:** The overall emotional tone is negative to neutral, with sentiment scores ranging from 0.50 to 0.95.
*  **Top 3 Points of View:**
    *   Data engineering teams are often swamped with work due to a lack of understanding of their value and insufficient resources.
    *   A common issue is the lack of project oversight, inadequate scoping, and late engagement with technical teams.
    *   It's often a feast or famine situation, where the workload is cyclical.

**[Snowflake cortex agent MCP server (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1p6u7ir/snowflake_cortex_agent_mcp_server/)**
*  **Summary:** The thread discusses experiences and best practices for using Snowflake's Cortex agent MCP server, focusing on making queries, ensuring data quality, and securing access.
*  **Emotion:** The overall emotional tone is positive to neutral, with sentiment scores ranging from 0.59 to 0.83.
*  **Top 3 Points of View:**
    *   Verified queries and incremental adjustments to the YAML file are crucial for getting correct results.
    *   The real challenge is building trust in the system and ensuring that text-to-SQL doesn't drift when the data gets messy.
    *   It's essential to design for safe, verifiable answers by keeping the agent on curated views, allowlisting schemas, and enforcing row/mask policies.

**[Is it worth fine-tuning AI on internal company data? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1p7607a/is_it_worth_finetuning_ai_on_internal_company_data/)**
*  **Summary:** This thread explores whether it's beneficial to fine-tune AI models on internal company data, considering factors like data privacy, accuracy, and the availability of large context windows in models.
*  **Emotion:** The overall emotional tone is neutral, with sentiment scores ranging from 0.53 to 0.94.
*  **Top 3 Points of View:**
    *   Skip full fine-tuning unless RAG (Retrieval-Augmented Generation) with strict governance can't meet your KPIs.
    *   If using a platform like Movai, you can fine-tune and train AI agents directly inside Snowflake or Databricks.
    *   Using a model with a large context window and loading the context from external files is a good alternative to fine-tuning.

**[What's your favorite Iceberg Catalog? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p77i81/whats_your_favorite_iceberg_catalog/)**
*  **Summary:** The thread asks users about their preferred Iceberg catalog implementations and discusses their experiences with different options.
*  **Emotion:** The emotional tone is mixed with a bit of negativity, with sentiment scores from 0.38 to 0.97
*  **Top 3 Points of View:**
    *   "Boring Catalog" is favored for ease of use and no server installation requirement.
    *   Project Nessie is an open-source transactional catalog that gives Git-like version control over tables and metadata.
    *   The Hadoop catalog (just files) is suitable for testing things out even at scale.

**[Aspiring Data Engineer – should I learn Go now or just stick to Python/PySpark? How do people actually learn the “data side” of Go? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p7ho3k/aspiring_data_engineer_should_i_learn_go_now_or/)**
*  **Summary:** The thread discusses whether aspiring data engineers should prioritize learning Go or stick to Python and PySpark, and how to learn the data side of Go.
*  **Emotion:** The emotional tone is mixed, with a lot of neutral and some negative sentiments. Sentiment scores range from 0.24 to 0.91.
*  **Top 3 Points of View:**
    *   Mastering Python, PySpark, and SQL is more than enough to be a good Data Engineer.
    *   Learning problem domains and building useful things is more important than just learning languages.
    *   Unless you plan to be a DE at Google, don't waste time on Go.

**[Looking for a solution to dynamically copy all tables from Lakehouse to Warehouse (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p6y5u1/looking_for_a_solution_to_dynamically_copy_all/)**
*  **Summary:** The thread discusses solutions for dynamically copying all tables from a Lakehouse to a Warehouse, focusing on automation, schema changes, and tools like Fabric, Airbyte, and Fivetran.
*  **Emotion:** The emotional tone is neutral, with sentiment scores ranging from 0.79 to 0.96.
*  **Top 3 Points of View:**
    *   Use Fabric's data movement primitives plus an automated control loop, or avoid copying entirely and materialize only what you need.
    *   Building a solution with Airbyte or subscribing to a service like Qlik or Fivetran are the two main options.
    *   Orchestrate with Fabric Data Pipelines and T-SQL scripts, using a metadata-driven pattern to auto-generate CREATE/ALTER + COPY INTO statements.

**[Forcibly Alter Spark Plan (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p790c0/forcibly_alter_spark_plan/)**
*  **Summary:** Discusses how to forcibly alter a Spark execution plan.
*  **Emotion:** The emotional tone is neutral, with sentiment scores ranging from 0.70.
*  **Top 1 Points of View:**
    *   Separate the operation into a new dataframe and join the data back to the main dataframe.

**[Sharepoint to Tableau Live (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p6vnn5/sharepoint_to_tableau_live/)**
*  **Summary:** Discusses ways to connect Sharepoint to Tableau for live analysis.
*  **Emotion:** The emotional tone is neutral, with sentiment scores ranging from 0.92 to 0.95.
*  **Top 3 Points of View:**
    *   Use Microsoft Graph API to pull the file wherever you need it.
    *   If you have SQL Server license, you can explore using SSIS for the ETL.
    *   Capture Forms responses straight into a database and point Tableau at that for live, skipping Excel entirely.

**[Considering an offer for DE II role, would love perspectives from DE/SWE folks (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p6p35x/considering_an_offer_for_de_ii_role_would_love/)**
*  **Summary:** Discusses the pros and cons of taking a Data Engineering II role.
*  **Emotion:** The emotional tone is neutral to negative, with sentiment scores ranging from 0.28 to 0.86.
*  **Top 3 Points of View:**
    *   If you want to be a SWE (Software Engineer), DE is not the right path. It might pigeonhole you.
    *   This is a good stack if you want to be a DE. DE is just a subsection of SWE.
    *   The pay cut might not be worth it, even if it's a good stack.

**[Structuring data analyses in academic projects (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p7c4n4/structuring_data_analyses_in_academic_projects/)**
*  **Summary:** The thread is about how to organize and structure data analyses within academic projects, with an emphasis on utility for its users
*  **Emotion:** The emotional tone is neutral, with sentiment scores around 0.82.
*  **Top 1 Points of View:**
    *   Store files in the cloud, or a shared drive, and keep a catalog of the files and versions in a relational database.

**[How much data should I validate for “confidence”? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p7ht86/how_much_data_should_i_validate_for_confidence/)**
*  **Summary:** This thread discusses how much data should be validated for confidence.
*  **Emotion:** The emotional tone is neutral, with sentiment scores ranging from 0.64 to 0.94.
*  **Top 3 Points of View:**
    *   The context and the specific requirements are crucial in determining this.
    *   Statistical significance and confidence intervals have nothing to do with data validation.
    *   Statistics can help you take a smaller sample and estimate the real percentage.
