---
title: "Data Engineering Subreddit"
date: "2025-03-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "SQL", "Spark"]
---

# Overall Ranking and Top Discussions
1.  [[D] Whats the most difficult SQL code you had to write for your data engineering role?](https://www.reddit.com/r/dataengineering/comments/1jevvff/whats_the_most_difficult_sql_code_you_had_to/) (Score: 45)
    * This thread discusses the most challenging SQL code data engineers have encountered in their roles, with contributors sharing experiences and specific scenarios.
2.  [Best practice for import pyspark.sql.functions](https://www.reddit.com/r/dataengineering/comments/1jewn8f/best_practice_for_import_pysparksqlfunctions/) (Score: 28)
    *  The thread discusses best practices for importing `pyspark.sql.functions`, specifically focusing on aliasing conventions like `F` vs. `sf`.
3.  [Scaling Iceberg Writes with Confidence: A Conflict-Free Distributed Architecture for Fast, Concurrent, Consistent Append-Only Writes](https://www.e6data.com/blog/iceberg-distributed-architecture-fast-concurrent-append-writes) (Score: 14)
    *  This thread discusses a conflict-free concurrent writes are a game changer for scaling ingestion workloads.
4.  [How do I document an old, janky, spaghetti-code ETL?](https://www.reddit.com/r/dataengineering/comments/1jeyfxx/how_do_i_document_an_old_janky_spaghetticode_etl/) (Score: 10)
    *   The thread focuses on strategies for documenting complex, undocumented ETL systems, including the use of sequence diagrams and ERDs.
5.  [Did You Become a Data Engineer by Accident or Passion ? Seeking Insights!](https://www.reddit.com/r/dataengineering/comments/1jf1e5d/did_you_become_a_data_engineer_by_accident_or/) (Score: 9)
    *   This thread explores the different paths people have taken to becoming data engineers, whether by accident or by actively pursuing it.
6.  [Is it okay to cache(disk) Spark DataFrames and use them for ad-hoc queries from users?](https://www.reddit.com/r/dataengineering/comments/1jevafb/is_it_okay_to_cachedisk_spark_dataframes_and_use/) (Score: 9)
    *   The discussion revolves around the suitability of caching Spark DataFrames on disk for ad-hoc user queries, considering factors like performance and data staleness.
7.  [A multi-engine Iceberg pipeline with Athena & Redshift](https://www.reddit.com/r/dataengineering/comments/1jevozf/a_multiengine_iceberg_pipeline_with_athena/) (Score: 8)
    *   This thread discusses leveraging multiple processing engines.
8.  [How can I become better with 5 yoe](https://www.reddit.com/r/dataengineering/comments/1jew753/how_can_i_become_better_with_5_yoe/) (Score: 5)
    *   Advice on how to improve as a data engineer.
9.  [Elasticsearch indexer for Open Library dump files](https://www.reddit.com/r/dataengineering/comments/1jeva3s/elasticsearch_indexer_for_open_library_dump_files/) (Score: 3)
    *   This thread is about Elasticsearch indexer for Open Library dump files.
10. [dbt_core -- excluding dbt_project_evaluator most of the time](https://www.reddit.com/r/dataengineering/comments/1jf43ry/dbt_core_excluding_dbt_project_evaluator_most_of/) (Score: 2)
    *   Discussion on excluding dbt_project_evaluator
11. [Suggestion on DE books](https://www.reddit.com/r/dataengineering/comments/1jf0eyg/suggestion_on_de_books/) (Score: 2)
    *   This thread provides suggestions on data engineering books.
12. [Delta lake or Iceberg on local file system or AWS EBS?](https://www.reddit.com/r/dataengineering/comments/1jezem8/delta_lake_or_iceberg_on_local_file_system_or_aws/) (Score: 2)
    *   This thread explores writing to local file systems.
13. [Would you (or have you) go/gone from Director to Senior Architect role? What was/is your reason?](https://www.reddit.com/r/dataengineering/comments/1jf27oe/would_you_or_have_you_gogone_from_director_to/) (Score: 1)
    *   This thread discusses career changes from Director to Senior Architect.
14. [choose Clod for Data Enginering and Analysis || Required suggestion and advise](https://www.reddit.com/r/dataengineering/comments/1jezkmn/choose_clod_for_data_enginering_and_analysis/) (Score: 1)
    *   Advise for choosing a cloud.
15. [currently an intern, question about long term career prospects](https://www.reddit.com/r/dataengineering/comments/1jf3qyw/currently_an_intern_question_about_long_term/) (Score: 0)
    *   Advice for interns and their career.

# Detailed Analysis by Thread
**[[D] Whats the most difficult SQL code you had to write for your data engineering role? (Score: 45)](https://www.reddit.com/r/dataengineering/comments/1jevvff/whats_the_most_difficult_sql_code_you_had_to/)**
*  **Summary:** Users share their experiences with complex SQL queries they've had to write for their data engineering roles, including challenges like nested procedures, anomaly detection, and performance optimization.
*  **Emotion:** The overall emotional tone is Neutral, with a mix of experiences being shared without strong emotional expressions. Some comments contain positive emotions, expressing accomplishment for optimizing and fixing complex queries, but there's also a hint of negative emotion towards the difficulty and frustration of dealing with poorly written or extremely large SQL code.
*  **Top 3 Points of View:**
    *   Complex SQL, such as recursive CTEs and window functions, is challenging but manageable.
    *   Debugging and modifying long, poorly written stored procedures is often more difficult than writing SQL from scratch.
    *   Sometimes it's better to move to other coding languages.

**[Best practice for import pyspark.sql.functions (Score: 28)](https://www.reddit.com/r/dataengineering/comments/1jewn8f/best_practice_for_import_pysparksqlfunctions/)**
*  **Summary:** The thread is about best practices when importing `pyspark.sql.functions`, discussing conventions such as using `F` or `sf` as aliases. The consensus is that consistency within a codebase is more important than adhering strictly to one particular convention. Some caution against star imports to avoid overwriting Python's built-in functions.
*  **Emotion:** The overall tone is Neutral. Some express positive sentiments about the simplicity and convenience of shorter aliases like "f," while others neutrally discuss coding standards and potential conflicts.
*  **Top 3 Points of View:**
    *   Consistency in aliasing (`F` or `sf`) within a codebase is crucial.
    *   Avoid star imports (`from pyspark.sql.functions import *`) to prevent overwriting Python's built-in functions.
    *   There's no universally correct alias; personal preference or team convention dictates the choice.

**[Scaling Iceberg Writes with Confidence: A Conflict-Free Distributed Architecture for Fast, Concurrent, Consistent Append-Only Writes (Score: 14)](https://www.e6data.com/blog/iceberg-distributed-architecture-fast-concurrent-append-writes)**
*  **Summary:** Solid write-up! Conflict-free concurrent writes are a game changer for scaling ingestion workloads.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Conflict-free concurrent writes are a game changer.

**[How do I document an old, janky, spaghetti-code ETL? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1jeyfxx/how_do_i_document_an_old_janky_spaghetticode_etl/)**
*  **Summary:**  The thread focuses on strategies for documenting complex, undocumented ETL systems. Suggestions include using sequence diagrams and ERDs, figuring out what's relied on by your highest priority XFN partners and documenting how that works, and using process mapping with subprocess maps.
*  **Emotion:** The overall emotional tone is Neutral, revolving around problem-solving and information sharing.
*  **Top 3 Points of View:**
    *   Sequence diagrams and ERDs can be unwieldy but helpful for visualizing data flow.
    *   Prioritize documenting the most critical processes first.
    *   Consider process mapping with subprocess maps.

**[Did You Become a Data Engineer by Accident or Passion ? Seeking Insights! (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1jf1e5d/did_you_become_a_data_engineer_by_accident_or/)**
*  **Summary:** The thread explores the different paths people have taken to becoming data engineers. Most describe how they stumbled into the role, often after starting in related fields like data analysis, BI, or even web development.
*  **Emotion:** The overall emotional tone is generally Positive.
*  **Top 3 Points of View:**
    *   Many data engineers initially aimed for other roles (e.g., data scientist) but found data engineering more appealing.
    *   Data engineering roles offer diverse challenges.
    *   A background in other tech fields can be helpful.

**[Is it okay to cache(disk) Spark DataFrames and use them for ad-hoc queries from users? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1jevafb/is_it_okay_to_cachedisk_spark_dataframes_and_use/)**
*  **Summary:** The discussion revolves around the suitability of caching Spark DataFrames on disk for ad-hoc user queries, considering factors like performance and data staleness.
*  **Emotion:** The overall emotional tone is Neutral, with a mix of practicality and caution.
*  **Top 3 Points of View:**
    *   Caching Spark DataFrames depends on user tolerance for stale data.
    *   Spark's scalability for serving multiple users concurrently should be considered.
    *   Consider parquet files.

**[A multi-engine Iceberg pipeline with Athena & Redshift (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1jevozf/a_multiengine_iceberg_pipeline_with_athena/)**
*  **Summary:** Iceberg lets you have up to 3 copies of the data in the database.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   Iceberg is good.

**[How can I become better with 5 yoe (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jew753/how_can_i_become_better_with_5_yoe/)**
*  **Summary:** Advice on how to improve as a data engineer.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Read the data warehouse toolkit.
    *   1% daily is 365% improvement YoY
    *   Adding some SQL and data modeling skills could really boost your resume.

**[Elasticsearch indexer for Open Library dump files (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jeva3s/elasticsearch_indexer_for_open_library_dump_files/)**
*  **Summary:** This thread is about Elasticsearch indexer for Open Library dump files.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Open-source projects can be featured.

**[dbt_core -- excluding dbt_project_evaluator most of the time (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jf43ry/dbt_core_excluding_dbt_project_evaluator_most_of/)**
*  **Summary:** To disable the package, you need to write a macro to fetch the current target environment and configure your project yaml.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Write a macro to fetch the current target environment and configure your project yaml.

**[Suggestion on DE books (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jf0eyg/suggestion_on_de_books/)**
*  **Summary:** The Data Warehouse Toolkit is pretty essential reading to understand or design dimensional models.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Read The Data Warehouse Toolkit

**[Delta lake or Iceberg on local file system or AWS EBS? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jezem8/delta_lake_or_iceberg_on_local_file_system_or_aws/)**
*  **Summary:** Writing both to filesystem (local or bucket)
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Set warehouse root as file:///directory.
    *   Support writing to filesystem (local or bucket)

**[Would you (or have you) go/gone from Director to Senior Architect role? What was/is your reason? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jf27oe/would_you_or_have_you_gogone_from_director_to/)**
*  **Summary:** This thread discusses career changes from Director to Senior Architect.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   As a manager, I feel I would be more replaceable.
    *   Pivot back to doing the things you enjoy.
    *   Companies are recognizing that management is different from engineering.

**[choose Clod for Data Enginering and Analysis || Required suggestion and advise (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jezkmn/choose_clod_for_data_enginering_and_analysis/)**
*  **Summary:** Advise for choosing a cloud.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Learning resources are listed in dataengineering.wiki
    *   Cloud adoption depends on your local area.

**[currently an intern, question about long term career prospects (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jf3qyw/currently_an_intern_question_about_long_term/)**
*  **Summary:** Advice for interns and their career.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Becoming a CTO isn't just about a career path.
