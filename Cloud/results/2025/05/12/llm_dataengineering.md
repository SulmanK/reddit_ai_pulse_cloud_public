---
title: "Data Engineering Subreddit"
date: "2025-05-12"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Polars in Rust vs golang custom implementation to replace Pandas real-time feature engineering](https://www.reddit.com/r/dataengineering/comments/1kkm5aw/polars_in_rust_vs_golang_custom_implementation_to/) (Score: 12)
    *   The discussion revolves around using Polars in Rust or a custom Go implementation to replace Pandas for real-time feature engineering.
2.  [How can I keep gaining experience through projects?](https://www.reddit.com/r/dataengineering/comments/1kkvjc8/how_can_i_keep_gaining_experience_through_projects/) (Score: 8)
    *   The thread is centered on ways to continuously build experience through data engineering projects.
3.  [SQL Certification](https://www.reddit.com/r/dataengineering/comments/1kkvpfz/sql_certification/) (Score: 7)
    *   People are discussing the value and different types of SQL certifications, with some preferring practical skills over certifications.
4.  [common database for metadata](https://www.reddit.com/r/dataengineering/comments/1kkmyj7/common_database_for_metadata/) (Score: 6)
    *   The conversation focuses on whether to use a common database for Airflow and OpenMetadata or separate instances, with a preference for isolation.
5.  [PyArrow+Narwhals vs. Polars: Opinions?](https://www.reddit.com/r/dataengineering/comments/1kkxpw5/pyarrownarwhals_vs_polars_opinions/) (Score: 6)
    *   Users are sharing their opinions on using PyArrow+Narwhals versus Polars for data engineering tasks.
6.  [Seeking Advice: Transitioning from Python Scripting to Building Data Pipelines](https://www.reddit.com/r/dataengineering/comments/1kkpf3o/seeking_advice_transitioning_from_python/) (Score: 5)
    *   The discussion centers around transitioning from Python scripting to building comprehensive data pipelines, including tool recommendations and architectural considerations.
7.  [Replication and/or ETL tools - what's the current pick based on pricing vs features around here?  When to buy vs build?](https://www.reddit.com/r/dataengineering/comments/1kkvi7j/replication_andor_etl_tools_whats_the_current/) (Score: 3)
    *   The thread explores the current preferred replication and ETL tools, considering the balance between pricing and features, as well as the build vs. buy decision.
8.  [Data Warehousing Dilemma: Base Fact Table + Specific Facts vs. Consolidated Fact - Which is Right?](https://www.reddit.com/r/dataengineering/comments/1kklrvr/data_warehousing_dilemma_base_fact_table_specific/) (Score: 2)
    *   The discussion focuses on the best approach to data warehousing: using a base fact table with specific facts or a consolidated fact table.
9.  [How to handle changing data in archived entitys?](https://www.reddit.com/r/dataengineering/comments/1kkqev7/how_to_handle_changing_data_in_archived_entitys/) (Score: 2)
    *   The thread discusses strategies for managing changes to data within archived entities.
10. [Maybe I'm the only one who has problems with "IT Recruiters on Matters Data Engineering" or something that's already common in Spain?](https://www.reddit.com/r/dataengineering/comments/1kksxcu/maybe_im_the_only_one_who_has_problems_with_it/) (Score: 2)
    *   The conversation focuses on the challenges of working with IT recruiters who may not fully understand data engineering concepts, particularly in Spain.
11. [Dataform](https://www.reddit.com/r/dataengineering/comments/1kkqcic/dataform/) (Score: 1)
    *   The thread discusses Dataform, the growing ubiquity of dbt and the transition to dbt.
12. [What is the name of this profession?](https://www.reddit.com/r/dataengineering/comments/1kktodn/what_is_the_name_of_this_profession/) (Score: 1)
    *   Users are trying to identify the profession that involves translating product requirements into technical specifications and considering business factors.
13. [Snowflake vs Databricks, beyond warehouse/lakehouse capabilities](https://www.reddit.com/r/dataengineering/comments/1kkylcb/snowflake_vs_databricks_beyond_warehouselakehouse/) (Score: 1)
    *   The discussion is about choosing between Snowflake and Databricks, considering factors beyond just warehouse/lakehouse capabilities.
14. [How LLMs Are Revolutionizing Database Queries Through Natural Language](https://www.queryhub.ai/blog/natural-language-to-sql-llm) (Score: 0)
    *   The discussion is centered around the feasibility of using LLMs to generate SQL from natural language.
15. [3NF before Kimball dimensional modeling](https://www.reddit.com/r/dataengineering/comments/1kkx037/3nf_before_kimball_dimensional_modeling/) (Score: 0)
    *   The thread discusses the value of applying 3NF normalization before implementing Kimball dimensional modeling.
16. [Feasibility of Big Data Analysis: Tracking Drug-Related Content Trends on Social Media (TikTok, YouTube, Instagram)](https://www.reddit.com/r/dataengineering/comments/1kkz2f8/feasibility_of_big_data_analysis_tracking/) (Score: 0)
    *   The thread discusses the feasibility of a big data analysis project focused on tracking drug-related content trends on social media platforms.
17. [Career: Onprem or Cloud?](https://www.reddit.com/r/dataengineering/comments/1kl073e/career_onprem_or_cloud/) (Score: 0)
    *   The discussion centers on the choice between on-premises and cloud-based career opportunities in data engineering.

# Detailed Analysis by Thread
**[[D] Polars in Rust vs golang custom implementation to replace Pandas real-time feature engineering (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1kkm5aw/polars_in_rust_vs_golang_custom_implementation_to/)**
*  **Summary:**  The thread discusses the pros and cons of using Polars in Rust versus implementing a custom solution in Go for real-time feature engineering, as an alternative to Pandas.
*  **Emotion:** The overall emotional tone is Neutral. The comments provide technical advice and information without strong emotional expression.
*  **Top 3 Points of View:**
    *   Polars in Python is recommended because it allows asynchronous collection of lazy frames in Rust without blocking the Python asyncio loop.
    *   If using Go, using DuckDB may be more stable than a non-official Polars binding.
    *   `groupby` and `rolling` operations should be easy to port over.

**[How can I keep gaining experience through projects? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1kkvjc8/how_can_i_keep_gaining_experience_through_projects/)**
*  **Summary:** The thread discusses how to keep gaining experience through projects by reading documentation of the listed tools.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Read the documentation of the listed tools.

**[SQL Certification (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kkvpfz/sql_certification/)**
*  **Summary:** The discussion centers around the value of SQL certifications versus practical skills and specific certifications like DP-300, Snowflake, and Databricks.
*  **Emotion:** The overall emotional tone is mixed, with both Neutral and Positive sentiments.
*  **Top 3 Points of View:**
    *   Practical SQL skills are more important than certifications for hiring.
    *   Certifications can help focus and understand required topics.
    *   DP-300 is good for in-depth SQL Server knowledge.

**[common database for metadata (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kkmyj7/common_database_for_metadata/)**
*  **Summary:**  The thread revolves around whether to use a shared Postgres instance for Airflow and OpenMetadata or to keep them separate.
*  **Emotion:** The overall emotional tone is mostly Neutral, with a few positive sentiments.
*  **Top 3 Points of View:**
    *   Separate databases are recommended to maintain isolation and easier maintenance.
    *   Sharing a database can create tight coupling and risk schema conflicts.
    *   Domain isolation is a good idea, even if it requires extra investment.

**[PyArrow+Narwhals vs. Polars: Opinions? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kkxpw5/pyarrownarwhals_vs_polars_opinions/)**
*  **Summary:** This thread discusses the pros and cons of using PyArrow+Narwhals vs. Polars for data engineering tasks.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Polars has more features and is generally sufficient for normal data engineering tasks.
    *   Narwhals is intended for systems that need to input different dataframes, like plotting libraries.
    *   Polars offers planning and optimizations, and can toggle into a batched streaming mode for out-of-core processing.

**[Seeking Advice: Transitioning from Python Scripting to Building Data Pipelines (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kkpf3o/seeking_advice_transitioning_from_python/)**
*  **Summary:** The discussion involves advice for someone transitioning from Python scripting to building full-fledged data pipelines.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Consider using a lightweight solution like DuckDB with dbt-core for a cost-effective proof of concept.
    *   Pitch the pipeline upgrade if the current Excel-based process is inefficient.
    *   DBT is just templatized SQL, so if you can achieve your ore processing through SQL, you can achieve that via DBT.

**[Replication and/or ETL tools - what's the current pick based on pricing vs features around here?  When to buy vs build? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kkvi7j/replication_andor_etl_tools_whats_the_current/)**
*  **Summary:** The thread discusses the trade-offs between buying ETL tools like Fivetran and Matillion versus building custom pipelines.
*  **Emotion:** The overall emotional tone is Neutral, with some positive sentiment towards SSIS.
*  **Top 3 Points of View:**
    *   Buying tools can be expensive but saves on development and maintenance costs.
    *   DIY solutions sound cheap upfront, but the total cost of ownership, including maintenance, debugging, and opportunity cost, must be considered.
    *   SSIS is recommended for ETL needs.

**[Data Warehousing Dilemma: Base Fact Table + Specific Facts vs. Consolidated Fact - Which is Right? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kklrvr/data_warehousing_dilemma_base_fact_table_specific/)**
*  **Summary:** The thread discusses the best approach to data warehousing design: using a base fact table with specific facts versus a consolidated fact table.
*  **Emotion:** The overall emotional tone is Neutral, with some negative sentiment expressing concerns about a single large table.
*  **Top 3 Points of View:**
    *   For analytics, denormalization is often better (consolidated fact table) to reduce joins.
    *   Design should be driven by reporting requirements; the answer could be "both."
    *   One big table is not good since you don’t have any shared dimensions.

**[How to handle changing data in archived entitys? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kkqev7/how_to_handle_changing_data_in_archived_entitys/)**
*  **Summary:**  The discussion is centered around how to manage changes to data in archived entities, specifically focusing on sales and product prices.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The sale should have the product's price at the time it was sold.
    *   A new record can be added to the product table every time the price changes.
    *   The current price of a product sold in LineItem can be stored.

**[Maybe I'm the only one who has problems with "IT Recruiters on Matters Data Engineering" or something that's already common in Spain? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kksxcu/maybe_im_the_only_one_who_has_problems_with_it/)**
*  **Summary:**  The conversation discusses the difficulties in dealing with IT recruiters who may lack a deep understanding of data engineering roles, especially in Spain.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Specialized recruiters at least get the key words and can map them to a job.
    *   Don't waste time with recruiters who aren't working for you.
    *    The right recruiter can be a good long term fruitful relationship.

**[Dataform (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kkqcic/dataform/)**
*  **Summary:**  The discussion focuses on Dataform, the growing ubiquity of dbt within the modern data stack, and potential transitions to dbt.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Transitioning to dbt is a good idea given its growing ubiquity.
    *   A growing number of dbt practitioners accelerate onboarding new hires.
    *   There are concerns that dbt-core is becoming a second priority to dbt-cloud.

**[What is the name of this profession? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kktodn/what_is_the_name_of_this_profession/)**
*  **Summary:** The thread seeks to identify the profession that involves translating product requirements into technical specifications, considering business factors.
*  **Emotion:** The overall emotional tone is Neutral to Positive.
*  **Top 3 Points of View:**
    *   The role aligns with a Business Analyst.
    *   It could be a Business System Analyst or Product Analyst.
    *   System Architect is another possible, though less common, title.

**[Snowflake vs Databricks, beyond warehouse/lakehouse capabilities (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kkylcb/snowflake_vs_databricks_beyond_warehouselakehouse/)**
*  **Summary:** The discussion centers around choosing between Snowflake and Databricks, taking into account factors beyond just warehouse/lakehouse capabilities.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   What is the amount of data you have to process daily?

**[How LLMs Are Revolutionizing Database Queries Through Natural Language (Score: 0)](https://www.queryhub.ai/blog/natural-language-to-sql-llm)**
*  **Summary:** The discussion is centered around the feasibility of using LLMs to generate SQL from natural language.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   They aren't.

**[3NF before Kimball dimensional modeling (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kkx037/3nf_before_kimball_dimensional_modeling/)**
*  **Summary:** The thread discusses the value of applying 3NF normalization before implementing Kimball dimensional modeling.
*  **Emotion:** The overall emotional tone is Neutral to Negative.
*  **Top 3 Points of View:**
    *   It will keep your dimension forming queried much simpler.
    *   Does creating 3nf break all your dimensions into the same level of granularity? If yes then sure.
    *   If the source systems are in 3NF then sure but otherwise I don't see the point in modelling the data twice.

**[Feasibility of Big Data Analysis: Tracking Drug-Related Content Trends on Social Media (TikTok, YouTube, Instagram) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kkz2f8/feasibility_of_big_data_analysis_tracking/)**
*  **Summary:** The thread discusses the feasibility of a big data analysis project focused on tracking drug-related content trends on social media platforms.
*  **Emotion:** The overall emotional tone is Neutral to Negative.
*  **Top 3 Points of View:**
    *   Hello there, I don’t consider myself an expert in the field, but I don’t think that you can collect social media data from the past 3-5 years.
    *   Anyways if you need some help consider contacting.
    *   I really didn't understand what you mean. In this case, what functionality would you use this data for?

**[Career: Onprem or Cloud? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kl073e/career_onprem_or_cloud/)**
*  **Summary:** The discussion centers on the choice between on-premises and cloud-based career opportunities in data engineering.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Cloud.
    *   I too would suggest the corporate one but for a slightly different reason.
    *   Job stability with a big corp is an illusion.
