---
title: "Data Engineering Subreddit"
date: "2025-12-03"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "BI", "APIs"]
---

# Overall Ranking and Top Discussions
1.  [[D] 90% of BI pain points come from data quality, not visualization - do you agree?](https://www.reddit.com/r/dataengineering/comments/1pd9blm/90_of_bi_pain_points_come_from_data_quality_not/) (Score: 25)
    * The discussion centers around whether data quality or visualization is the primary cause of BI pain points.
2.  [What’s the most confusing API behavior you’ve ever run into while moving data?](https://www.reddit.com/r/dataengineering/comments/1pd2gbn/whats_the_most_confusing_api_behavior_youve_ever/) (Score: 11)
    *  Users share their experiences with confusing or unexpected API behaviors encountered while moving data.
3.  [Is DuckLake a Step Backward?](https://www.pracdata.io/p/is-ducklake-a-step-backward) (Score: 7)
    *  This post discusses the DuckLake database solution and whether it represents a step backward in database technology.
4.  [From dbt column lineage to impact analysis](https://www.reddit.com/r/dataengineering/comments/1pdboxt/from_dbt_column_lineage_to_impact_analysis/) (Score: 6)
    * This post provides a link to an open-source project showcase related to dbt column lineage and impact analysis.
5.  [Can I use ETL/ELT on my Data warehouse Or data lake ?](https://www.reddit.com/r/dataengineering/comments/1pcvlm2/can_i_use_etlelt_on_my_data_warehouse_or_data_lake/) (Score: 5)
    *  Users discuss the applicability and best practices of using ETL/ELT processes on data warehouses and data lakes.
6.  [What DuckDB API do you use (or would like to) with the Python client?](https://www.reddit.com/r/dataengineering/comments/1pd6oce/what_duckdb_api_do_you_use_or_would_like_to_with/) (Score: 5)
    * Users share what DuckDB APIs they use or would like to see implemented with the Python client.
7.  [Who should manage Airflow in small but growing company?](https://www.reddit.com/r/dataengineering/comments/1pdfkd0/who_should_manage_airflow_in_small_but_growing/) (Score: 4)
    *  The thread discusses the optimal role or team to manage Airflow within a small but growing company.
8.  [Is Data Engineering the next step for me?](https://www.reddit.com/r/dataengineering/comments/1pdb4ql/is_data_engineering_the_next_step_for_me/) (Score: 3)
    *  This post explores whether a career transition to data engineering is a suitable path for the original poster.
9.  [Architecture Critique: Enterprise Text-to-SQL RAG with Human-in-the-Loop](https://www.reddit.com/r/dataengineering/comments/1pctolf/architecture_critique_enterprise_texttosql_rag/) (Score: 3)
    *  This thread requests architectural critique for an enterprise text-to-SQL RAG (Retrieval-Augmented Generation) system that incorporates human review.
10. [how do you keep pipelines + infra from becoming chaotic?](https://www.reddit.com/r/dataengineering/comments/1pdesv7/how_do_you_keep_pipelines_infra_from_becoming/) (Score: 2)
    * This post seeks advice on how to prevent data pipelines and infrastructure from becoming unorganized and difficult to manage.
11. [Late-night Glue/Spark failures, broken Step Functions, and how I stabilized the pipeline](https://www.reddit.com/r/dataengineering/comments/1pcp3i9/latenight_gluespark_failures_broken_step/) (Score: 1)
    *  The author discusses their experiences with Glue/Spark failures and how they stabilized the pipeline.
12. [How to store large JSON columns](https://www.reddit.com/r/dataengineering/comments/1pd8p5o/how_to_store_large_json_columns/) (Score: 1)
    *  The discussion explores the best methods and technologies for storing large JSON columns in a database or data warehouse.
13. [Airbyte vs. Fivetran vs Hevo](https://www.reddit.com/r/dataengineering/comments/1pcw4d5/airbyte_vs_fivetran_vs_hevo/) (Score: 0)
    *  This post is a comparison of three data integration tools: Airbyte, Fivetran, and Hevo.
14. [Need Advice](https://www.reddit.com/r/dataengineering/comments/1pcz86g/need_advice/) (Score: 0)
    * The original poster is seeking general professional advice.

# Detailed Analysis by Thread
**[[D] 90% of BI pain points come from data quality, not visualization - do you agree? (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1pd9blm/90_of_bi_pain_points_come_from_data_quality_not/)**
*  **Summary:** The discussion revolves around whether data quality or visualization is the primary source of pain points in Business Intelligence (BI). Many participants agree that data quality issues significantly outweigh visualization problems, citing issues with upstream data collection, lack of standards, and the need for data transformation.
*  **Emotion:** The emotional tone is largely neutral, with some negative sentiment related to the frustrations caused by data quality issues and unreasonable stakeholder expectations. There is also some positive sentiment due to agreement on the importance of data quality.
*  **Top 3 Points of View:**
    *   Data quality is more important than visualization.
    *   Data quality issues often stem from poor planning and execution in upstream data collection processes.
    *   Unreasonable stakeholder expectations are also a significant pain point.

**[What’s the most confusing API behavior you’ve ever run into while moving data? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1pd2gbn/whats_the_most_confusing_api_behavior_youve_ever/)**
*  **Summary:**  The thread is a collection of anecdotes about confusing and unexpected API behaviors encountered by data engineers when moving data. These include undocumented changes, inverted logic, and inconsistent data formats.
*  **Emotion:** The overall emotional tone is neutral, with mild negative undertones reflecting the frustration and challenges faced when dealing with poorly designed or documented APIs.
*  **Top 3 Points of View:**
    *   APIs often have undocumented changes or behaviors.
    *   Inconsistent data formats and lack of schema enforcement are common problems.
    *   Some APIs return errors or unexpected results under specific conditions (e.g., empty lists, 404 errors).

**[Is DuckLake a Step Backward? (Score: 7)](https://www.pracdata.io/p/is-ducklake-a-step-backward)**
*   **Summary:** This thread discusses the merits and potential drawbacks of DuckLake, a database solution. Some argue that it may be a step backward due to its siloed nature and lack of seamless integration with other popular data lake formats. Others believe that its architecture is well-suited for most business needs.
*   **Emotion:** The emotional tone is mixed, ranging from positive (solid article) to negative (siloed database solution, potential backward step) to neutral (measured summary).
*   **Top 3 Points of View:**
    *   DuckLake is a siloed database solution that needs better integration with Delta Lake, Iceberg, etc.
    *   DuckLake's architecture is sufficient for most businesses, as they don't handle petabytes of data.
    *   Most development seems aimed at making MotherDuck profitable

**[From dbt column lineage to impact analysis (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1pdboxt/from_dbt_column_lineage_to_impact_analysis/)**
*   **Summary:** This thread simply shares a link to an open-source project showcase related to dbt column lineage and impact analysis. It also includes a link for users to submit their own projects.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   This is a bot posting information.

**[Can I use ETL/ELT on my Data warehouse Or data lake ? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1pcvlm2/can_i_use_etlelt_on_my_data_warehouse_or_data_lake/)**
*   **Summary:** The discussion centers around the feasibility and best practices of applying ETL/ELT processes to data warehouses and data lakes. Participants generally agree that it's acceptable, especially for reshaping data or creating curated layers, but caution against unnecessary cost and duplication.
*   **Emotion:** The overall sentiment is neutral, with a slightly positive leaning.
*   **Top 3 Points of View:**
    *   Using ETL/ELT on data warehouses and data lakes is acceptable for reshaping or curating data.
    *   Cost and data duplication should be carefully considered.
    *   Reverse ETL is commonly used for sending data back to other systems.

**[What DuckDB API do you use (or would like to) with the Python client? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1pd6oce/what_duckdb_api_do_you_use_or_would_like_to_with/)**
*   **Summary:** Users discuss their experiences with DuckDB APIs, particularly the `read_blob` function, and suggest improvements for the Python client. A common issue is the lack of incremental loading support for `read_blob`.
*   **Emotion:** The emotional tone is generally positive, expressing appreciation for DuckDB and suggesting improvements.
*   **Top 3 Points of View:**
    *   `read_blob` with hive partitioning is useful for loading blob assets without a database for metadata.
    *   Incremental result loading for `read_blob` is a desirable feature.

**[Who should manage Airflow in small but growing company? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1pdfkd0/who_should_manage_airflow_in_small_but_growing/)**
*   **Summary:** This thread discusses which team or role should be responsible for managing Airflow in a small but growing company. Suggestions range from data engineers to platform engineers, with an emphasis on the importance of defining data ownership.
*   **Emotion:** The overall emotional tone is neutral to positive.
*   **Top 3 Points of View:**
    *   Airflow should be managed by platform engineers.
    *   Pipelines should be owned by data engineers.
    *   Consider using a managed Apache Airflow service to avoid operational overhead.

**[Is Data Engineering the next step for me? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1pdb4ql/is_data_engineering_the_next_step_for_me/)**
*   **Summary:** The thread discusses whether transitioning to data engineering is a good career move for the original poster. Advice includes focusing on current role performance, learning Python/SQL, and understanding data modeling.
*   **Emotion:** The emotional tone is mostly positive.
*   **Top 3 Points of View:**
    *   Transitioning to data engineering is a logical step for someone in analytics.
    *   Focus on current role performance before branching out.
    *   Learning Python/SQL and data modeling is essential for data engineering.

**[Architecture Critique: Enterprise Text-to-SQL RAG with Human-in-the-Loop (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1pctolf/architecture_critique_enterprise_texttosql_rag/)**
*   **Summary:** The thread requests feedback on an architecture for an enterprise text-to-SQL RAG system with human review. Suggestions include using versioned business rule registries, Git-based review processes, and off-the-shelf text-to-SQL products.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Keep business rules in a versioned registry and use pointers.
    *   Use Git-based review processes for verification.
    *   Evaluate off-the-shelf text-to-SQL products.

**[how do you keep pipelines + infra from becoming chaotic? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1pdesv7/how_do_you_keep_pipelines_infra_from_becoming/)**
*   **Summary:** This is a single-response thread recommending that the team practice data governance.
*   **Emotion:** The emotional tone is positive.
*   **Top 3 Points of View:**
    *   Governance is a core discipline your team should be practicing.

**[Late-night Glue/Spark failures, broken Step Functions, and how I stabilized the pipeline (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1pcp3i9/latenight_gluespark_failures_broken_step/)**
*   **Summary:** The author offers to share details about stabilizing a pipeline after encountering failures with Glue/Spark and Step Functions.
*   **Emotion:** The emotional tone is positive.
*   **Top 3 Points of View:**
    *   The author is open to sharing details and code snippets.

**[How to store large JSON columns (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1pd8p5o/how_to_store_large_json_columns/)**
*   **Summary:** The thread explores various approaches to storing large JSON columns, including using Snowflake, ClickHouse, and BigQuery. Recommendations include parsing important fields and using semi-structured data support.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Use Snowflake for its semi-structured data support.
    *   Unpack important fields and store the rest in JSON using ClickHouse.
    *   Ingest raw data into BigQuery, then model the warehouse.

**[Airbyte vs. Fivetran vs Hevo (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1pcw4d5/airbyte_vs_fivetran_vs_hevo/)**
*   **Summary:** This thread contains a question regarding cloud-only solutions vs. on-premises solutions for data integration tools.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Consider whether you need a cloud-only or on-premises solution.

**[Need Advice (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1pcz86g/need_advice/)**
*   **Summary:** This thread provides advice on career choices. One respondent suggests building a small end-to-end project and keeping a current role while interviewing for a new one.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Build a small end-to-end project to enhance your portfolio.
    *   Keep interviewing for a Databricks/Fabric role while building a project.
    *   Consider the implications of job hopping on your resume.
