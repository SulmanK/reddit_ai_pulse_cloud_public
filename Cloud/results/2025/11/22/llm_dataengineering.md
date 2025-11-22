---
title: "Data Engineering Subreddit"
date: "2025-11-22"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "postgres", "dbt"]
---

# Overall Ranking and Top Discussions
1. [[D] Testing FaceSeek made me think about the data pipelines behind public image search](https://www.reddit.com/r/dataengineering/comments/1p3s6k6/testing_faceseek_made_me_think_about_the_data/) (Score: 76)
    * Discusses the data pipelines behind public image search after testing FaceSeek.
2. [Can Postgres handle these analytics requirements at 1TB+](https://www.reddit.com/r/dataengineering/comments/1p3cdzm/can_postgres_handle_these_analytics_requirements/) (Score: 51)
    *  Asks if Postgres can handle analytics requirements at 1TB+.
3. [What is the purpose of the book "fundamentals of data engineering "](https://www.reddit.com/r/dataengineering/comments/1p3l6t8/what_is_the_purpose_of_the_book_fundamentals_of/) (Score: 47)
    *  Asks about the purpose of the book "Fundamentals of Data Engineering."
4. [Am I on the right way to get my first job?](https://www.reddit.com/r/dataengineering/comments/1p3iqru/am_i_on_the_right_way_to_get_my_first_job/) (Score: 9)
    *  Asks for feedback on the best path to getting a first job in data engineering.
5. [Code Masking Tool](https://www.reddit.com/r/dataengineering/comments/1p3b9o9/code_masking_tool/) (Score: 6)
    *  Discusses code masking tools and using LLMs.
6. [Comparison of Microsoft Fabric CICD package vs Deployment Pipelines](https://www.reddit.com/r/dataengineering/comments/1p3sexq/comparison_of_microsoft_fabric_cicd_package_vs/) (Score: 6)
    *  A question about the comparison of Microsoft Fabric CICD package versus Deployment Pipelines.
7. [Onlymaps, a Python micro-ORM](https://www.reddit.com/r/dataengineering/comments/1p3v0c7/onlymaps_a_python_microorm/) (Score: 6)
    *  A discussion about the usefulness of Onlymaps, a Python micro-ORM.
8. [ADF incremental binary copy of files is missing files when executed too frequently](https://www.reddit.com/r/dataengineering/comments/1p3ifoa/adf_incremental_binary_copy_of_files_is_missing/) (Score: 1)
    * Question regarding a problem when ADF incremental binary copy of files is missing files when executed too frequently.
9. [dbt-core: where are the docs?](https://www.reddit.com/r/dataengineering/comments/1p3t6ct/dbtcore_where_are_the_docs/) (Score: 0)
    *  Asks where the documentation is for dbt-core.

# Detailed Analysis by Thread
**[[D] Testing FaceSeek made me think about the data pipelines behind public image search (Score: 76)](https://www.reddit.com/r/dataengineering/comments/1p3s6k6/testing_faceseek_made_me_think_about_the_data/)**
*   **Summary:** The post discusses the data pipelines behind public image search, prompted by testing FaceSeek.
*   **Emotion:** The emotional tone of the thread is neutral.
*   **Top 3 Points of View:**
    *   The post is considered a clear advertisement.

**[Can Postgres handle these analytics requirements at 1TB+ (Score: 51)](https://www.reddit.com/r/dataengineering/comments/1p3cdzm/can_postgres_handle_these_analytics_requirements/)**
*   **Summary:** The post questions whether Postgres can efficiently handle analytical requirements at a scale of 1TB or more, particularly when dealing with mixed transactional and analytical workloads.
*   **Emotion:** The emotional tone of the thread is neutral, but with a hint of negativity due to concerns about performance issues with Postgres at scale.
*   **Top 3 Points of View:**
    *   Postgres can handle it, but other databases like Clickhouse or Starrocks might be better depending on data structures and join sizes.
    *   Running transactional and analytical workloads on the same database is questioned.
    *   It depends on the query workload and context such as load schedule and whether the Postgres instance is also used for transactional data.

**[What is the purpose of the book "fundamentals of data engineering " (Score: 47)](https://www.reddit.com/r/dataengineering/comments/1p3l6t8/what_is_the_purpose_of_the_book_fundamentals_of/)**
*   **Summary:** The discussion revolves around the purpose and value of the book "Fundamentals of Data Engineering," particularly for newcomers to the field.
*   **Emotion:** The thread has a generally positive emotional tone.
*   **Top 3 Points of View:**
    *   The book is good for learning the fundamentals of data engineering, especially for those new to the field.
    *   The book is most useful for non-practitioners and those in management roles, but less useful for experienced data engineers.
    *   It's important to understand the concepts of data engineering because of the rapid improvement of AI tools.

**[Am I on the right way to get my first job? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1p3iqru/am_i_on_the_right_way_to_get_my_first_job/)**
*   **Summary:** The post is a query asking if the poster is on the right track to getting their first data engineering job.
*   **Emotion:** The overall emotional tone is positive and encouraging.
*   **Top 3 Points of View:**
    *   Focus on building one strong, end-to-end flagship project rather than many smaller ones.
    *   Emphasize what you learned, what went wrong, and how you would solve problems in your projects.
    *   Depth and real-world applicability of skills are more important than listing every tool you know.

**[Code Masking Tool (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p3b9o9/code_masking_tool/)**
*   **Summary:** The discussion focuses on using code masking tools and the use of LLMs with enterprise agreements.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   LLMs are used everywhere with enterprise versions and data retention agreements.

**[Comparison of Microsoft Fabric CICD package vs Deployment Pipelines (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p3sexq/comparison_of_microsoft_fabric_cicd_package_vs/)**
*   **Summary:** The post is a request for a comparison between Microsoft Fabric's CICD package and Deployment Pipelines.
*   **Emotion:** The emotional tone is positive, indicated by the upvote and interest in unit testing.
*   **Top 3 Points of View:**
    *   Unit testing in Fabric is a highly desired feature.

**[Onlymaps, a Python micro-ORM (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p3v0c7/onlymaps_a_python_microorm/)**
*   **Summary:** This post introduces "Onlymaps," a Python micro-ORM, and discusses its potential name and relevance to data engineering.
*   **Emotion:** The emotional tone is mostly neutral.
*   **Top 3 Points of View:**
    *   The name "Onlymaps" is problematic and should be changed.
    *   ORMs aren't typically used in data engineering.
    *   One user thought it was a geospatial tool.

**[ADF incremental binary copy of files is missing files when executed too frequently (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p3ifoa/adf_incremental_binary_copy_of_files_is_missing/)**
*   **Summary:** The post describes an issue where ADF incremental binary copy misses files when executed too frequently and seeks advice on how to resolve the problem.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Move files to an archive folder and rename them after processing for an idempotent pipeline.
    *   Do not delete files in source to keep files to rebuild if required.

**[dbt-core: where are the docs? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p3t6ct/dbtcore_where_are_the_docs/)**
*   **Summary:** The post questions where to find the documentation for dbt-core and expresses frustration with the available resources.
*   **Emotion:** The emotional tone is mixed, ranging from neutral to positive, with some frustration expressed by the original poster and some empathetic responses.
*   **Top 3 Points of View:**
    *   The dbt documentation is generally good but can be confusing due to the mix of dbt Core and dbt Cloud documentation.
    *   Start with dbt Core's quickstarts and example projects.
    *   The documentation is hard to follow when you don't know everything, therefore start with the Snowflake dbt setup and Kimball modelling in dbt docs.
