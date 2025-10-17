---
title: "Data Engineering Subreddit"
date: "2025-10-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data", "engineering", "trends"]
---

# Overall Ranking and Top Discussions
1.  [[D] Data infrastructure so "open" that there's only 1 box that isn't Fivetran...](https://i.redd.it/2w1fkqef2pvf1.png) (Score: 116)
    *   The image shows a data infrastructure diagram where almost all the boxes are labeled "Fivetran", implying a lack of true openness in the data infrastructure.
2.  [Anyone feel like too much is expected of DEs (at small companies)](https://www.reddit.com/r/dataengineering/comments/1o97xkg/anyone_feel_like_too_much_is_expected_of_des_at/) (Score: 31)
    *   Data Engineers at small companies are often expected to be "full stack" and handle a wide range of tasks due to smaller team sizes and cost-center perceptions.
3.  [If you could work as a DE anywhere, what company or industry would it be - and why?](https://www.reddit.com/r/dataengineering/comments/1o96rrn/if_you_could_work_as_a_de_anywhere_what_company/) (Score: 25)
    *   People are discussing where they would ideally work as data engineers, considering factors like compensation, work-life balance, challenging problems, and enjoyable team dynamics.
4.  [Engineers modifying DB columns without informing others](https://www.reddit.com/r/dataengineering/comments/1o9335d/engineers_modifying_db_columns_without_informing/) (Score: 23)
    *   The post discusses the importance of change management processes and proper database access controls to prevent engineers from making unauthorized changes to database schemas.
5.  [What are some other underrated books in the field of data?](https://i.redd.it/4fg8jirasmvf1.jpeg) (Score: 16)
    *   A user shares an image of a textbook and jokes about the difficulty of understanding it, sparking a discussion about underrated data books.
6.  [Iceberg support in Apache Fluss - first demo](https://youtu.be/a6MG4f0Ko_g) (Score: 6)
    *   This post is about the introduction of Iceberg support in Apache Fluss and its potential for real-time data processing.
7.  [Embracing data engineering as a hobby](https://www.reddit.com/r/dataengineering/comments/1o98a9f/embracing_data_engineering_as_a_hobby/) (Score: 5)
    *   Users discuss using data engineering as a hobby and list their side-projects.
8.  [How do you architect your boilerplate code over projects.](https://www.reddit.com/r/dataengineering/comments/1o8yjpe/how_do_you_architect_your_boilerplate_code_over/) (Score: 3)
    *   Discussion on how to organize and structure boilerplate code across different data engineering projects.
9.  [ClickHouse Date and DateTime types](https://www.reddit.com/r/dataengineering/comments/1o8td28/clickhouse_date_and_datetime_types/) (Score: 3)
    *   The post discusses the limitations of ClickHouse's Date and DateTime types, particularly for dates before 1970, and suggests alternative storage and handling methods.
10. [Power BI + Azure Synapse to Fabric migration](https://www.reddit.com/r/dataengineering/comments/1o93iwl/power_bi_azure_synapse_to_fabric_migration/) (Score: 2)
    *   Discussing the migration process from Power BI and Azure Synapse to Fabric, including concerns about compute limits and costs.
11. [Any experiences with Marks and Spencer UK Digital (Data Engineer role)?](https://www.reddit.com/r/dataengineering/comments/1o8yia8/any_experiences_with_marks_and_spencer_uk_digital/) (Score: 2)
    *   The discussion is about the experiences of people working for Marks and Spencer UK Digital as Data Engineers.
12. [Using modal for transformation of a huge dataset](https://www.reddit.com/r/dataengineering/comments/1o8luf7/using_modal_for_transformation_of_a_huge_dataset/) (Score: 2)
    *   Users discuss the suitability of using Modal for large-scale ETL, with some suggesting Spark as a better alternative.
13. [How am i supposed to set up an environment with Airflow and Spark?](https://www.reddit.com/r/dataengineering/comments/1o8qtsx/how_am_i_supposed_to_set_up_an_environment_with/) (Score: 1)
    *   The post is about setting up an environment with Airflow and Spark, with a suggestion to use bitnami legacy instead of bitnami.
14. [I built a tool- csv/parquet to API in 30 seconds?](https://v.redd.it/posk8rjrwpvf1) (Score: 1)
    *   A user shares a tool they built for converting CSV/Parquet files to APIs quickly.
15. [Compare and update two different databases](https://www.reddit.com/r/dataengineering/comments/1o96izv/compare_and_update_two_different_databases/) (Score: 1)
    *   The post discusses how to compare and update two different databases, with suggestions on using 'lastModified' timestamp columns.
16. [Ai-based specsheet data extraction tool for products.](https://www.reddit.com/r/dataengineering/comments/1o8whgl/aibased_specsheet_data_extraction_tool_for/) (Score: 0)
    *   A user shares an AI-based tool for extracting data from product spec sheets.
17. [Elusion v7.9.0 has additional DASHBOARD features](https://www.reddit.com/r/dataengineering/comments/1o8tf72/elusion_v790_has_additional_dashboard_features/) (Score: 0)
    *   A post about new dashboard features in Elusion v7.9.0, specifically cross-filtering for interactive data exploration.
18. [Lakehouse Catalog Feature Dream List](https://www.reddit.com/r/dataengineering/comments/1o93vum/lakehouse_catalog_feature_dream_list/) (Score: 0)
    *   Users are brainstorming features for a Lakehouse catalog, including RBAC, lineage, support for various engines, and metadata discovery.

# Detailed Analysis by Thread
**[[D] Data infrastructure so "open" that there's only 1 box that isn't Fivetran... (Score: 116)](https://i.redd.it/2w1fkqef2pvf1.png)**
*   **Summary:** The image depicts a data infrastructure overwhelmingly dominated by Fivetran, questioning the true openness of the system.
*   **Emotion:** The emotional tone is mostly neutral with some negativity.
*   **Top 3 Points of View:**
    *   The diagram highlights the potential over-reliance on a single vendor (Fivetran).
    *   Some recognize the marketing effectiveness of promoting "open standards" over "open source".
    *   Developers are sometimes blamed for selling out their projects.

**[Anyone feel like too much is expected of DEs (at small companies) (Score: 31)](https://www.reddit.com/r/dataengineering/comments/1o97xkg/anyone_feel_like_too_much_is_expected_of_des_at/)**
*   **Summary:** Data engineers at small companies are often expected to handle a wide range of responsibilities, leading to them being "full-stack".
*   **Emotion:** The emotional tone is mixed, with neutral sentiments mixed with some positive opinions.
*   **Top 3 Points of View:**
    *   Data teams are often seen as cost centers and are therefore understaffed, requiring data engineers to be more versatile.
    *   Some data engineers enjoy the variety of tasks and would be bored doing the same thing every day.
    *   The workload can be extreme, with expectations to solve all data issues quickly, leading some to consider returning to larger companies with more structure.

**[If you could work as a DE anywhere, what company or industry would it be - and why? (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1o96rrn/if_you_could_work_as_a_de_anywhere_what_company/)**
*   **Summary:** People are discussing their ideal workplaces as data engineers, with considerations ranging from compensation and work-life balance to challenging problems and enjoyable team dynamics.
*   **Emotion:** The emotional tone is generally positive and neutral.
*   **Top 3 Points of View:**
    *   Some prioritize compensation and the ability to retire early.
    *   Others value working in industries that contribute to health, well-being, and the environment.
    *   Many seek a balance of challenging work, good compensation, and a positive team environment.

**[Engineers modifying DB columns without informing others (Score: 23)](https://www.reddit.com/r/dataengineering/comments/1o9335d/engineers_modifying_db_columns_without_informing/)**
*   **Summary:** The post discusses the problem of engineers modifying database columns without informing others, and the importance of proper processes and access control.
*   **Emotion:** The emotional tone is mostly neutral.
*   **Top 3 Points of View:**
    *   Engineers should not have the permission to modify database schemas directly.
    *   Implementing a change management process with version control and schema migration tools is essential.
    *   A data contract logic for source validation before running pipelines is needed.

**[What are some other underrated books in the field of data? (Score: 16)](https://i.redd.it/4fg8jirasmvf1.jpeg)**
*   **Summary:** A user shares an image of a textbook and jokes about the difficulty of understanding it.
*   **Emotion:** The overall tone is positive, with a humorous perspective.
*   **Top 3 Points of View:**
    *   Textbooks are sometimes difficult to understand despite being comprehensive.

**[Iceberg support in Apache Fluss - first demo (Score: 6)](https://youtu.be/a6MG4f0Ko_g)**
*   **Summary:** The post introduces Iceberg support in Apache Fluss and its potential for real-time data processing.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   The new support is promising for real-time data processing.

**[Embracing data engineering as a hobby (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1o98a9f/embracing_data_engineering_as_a_hobby/)**
*   **Summary:** Users discuss using data engineering as a hobby and list their side-projects.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   Some projects use AWS services, Dagster, dbt, Python, SQL, Supabase, and Soda.
    *   Some are going full GCP and deep diving into Dagster.
    *   Some users express interest in collaborating on data engineering projects.

**[How do you architect your boilerplate code over projects. (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o8yjpe/how_do_you_architect_your_boilerplate_code_over/)**
*   **Summary:** Discussion on how to organize and structure boilerplate code across different data engineering projects.
*   **Emotion:** The overall tone is neutral.
*   **Top 3 Points of View:**
    *   Using a consistent folder structure (e.g., data, log, core, config, util, service) as a baseline is helpful.
    *   Make code callable, especially in Python/Airflow, by importing it as a variable.
    *   Avoid template files, as they can lead to unmaintained and unoptimized code.

**[ClickHouse Date and DateTime types (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o8td28/clickhouse_date_and_datetime_types/)**
*   **Summary:** The post discusses the limitations of ClickHouse's Date and DateTime types, particularly for dates before 1970, and suggests alternative storage and handling methods.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   ClickHouse's Date type only supports dates from 1970-01-01 to 2105-12-31.
    *   For older dates, store them as DateTime64, String, or keep your Decimal(8,0) format and convert only when needed.
    *   Consider using a different platform or rounding dates to the minimum if precise dates are not essential.

**[Power BI + Azure Synapse to Fabric migration (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o93iwl/power_bi_azure_synapse_to_fabric_migration/)**
*   **Summary:** Discussing the migration process from Power BI and Azure Synapse to Fabric, including concerns about compute limits and costs.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Fabric F64 may not be sufficient for larger organizations with many workspaces and clients, leading to throttling issues.
    *   You can still use Power BI licences for a workspace with models and reports, this won't use your Fabric capacity
    *   Evaluate consumption before changing licenses in the workspace

**[Any experiences with Marks and Spencer UK Digital (Data Engineer role)? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o8yia8/any_experiences_with_marks_and_spencer_uk_digital/)**
*   **Summary:** The discussion is about the experiences of people working for Marks and Spencer UK Digital as Data Engineers.
*   **Emotion:** Mixed, with some negative opinions.
*   **Top 3 Points of View:**
    *   The company is boring, stable, and a large corporation with a performative culture.
    *   Someone joked that they leaked the keys which lead to the hack
    *   Experiences were unfavorable.

**[Using modal for transformation of a huge dataset (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o8luf7/using_modal_for_transformation_of_a_huge_dataset/)**
*   **Summary:** Users discuss the suitability of using Modal for large-scale ETL, with some suggesting Spark as a better alternative.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Modal seems more for dev experiments, not large-scale etl.
    *   Spark is better for large-scale etl.

**[How am i supposed to set up an environment with Airflow and Spark? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1o8qtsx/how_am_i_supposed_to_set_up_an_environment_with/)**
*   **Summary:** The post is about setting up an environment with Airflow and Spark, with a suggestion to use bitnami legacy instead of bitnami.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Use bitnami legacy instead of bitnami.
    *   Use ssh or sparkoperator in airflow to submit spark job

**[I built a tool- csv/parquet to API in 30 seconds? (Score: 1)](https://v.redd.it/posk8rjrwpvf1)**
*   **Summary:** A user shares a tool they built for converting CSV/Parquet files to APIs quickly.
*   **Emotion:** The tone is positive.
*   **Top 3 Points of View:**
    *   The tool is very cool.

**[Compare and update two different databases (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1o96izv/compare_and_update_two_different_databases/)**
*   **Summary:** The post discusses how to compare and update two different databases, with suggestions on using 'lastModified' timestamp columns.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Add 'lastModified' timestamp column and clean and import just batched data into your db.
    *   Export the whole table and replace it in Postgres every night (truncate and then insert) after it goes through ETL.
    *   The problem would normally be solved with update_at column in the source, so you can store a "high water mark" and know which new records to import

**[Ai-based specsheet data extraction tool for products. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o8whgl/aibased_specsheet_data_extraction_tool_for/)**
*   **Summary:** A user shares an AI-based tool for extracting data from product spec sheets.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   The tool sounds like a solid timesaver.
    *   Interested in how well it handles diverse formats

**[Elusion v7.9.0 has additional DASHBOARD features (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o8tf72/elusion_v790_has_additional_dashboard_features/)**
*   **Summary:** A post about new dashboard features in Elusion v7.9.0, specifically cross-filtering for interactive data exploration.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Cross-filtering is useful for interactive data exploration.
    *   Enhances clarity

**[Lakehouse Catalog Feature Dream List (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o93vum/lakehouse_catalog_feature_dream_list/)**
*   **Summary:** Users are brainstorming features for a Lakehouse catalog, including RBAC, lineage, support for various engines, and metadata discovery.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Proper working fgac that works on hive, spark, impala, trino and any other sql engine.
    *   RBAC
    *   Lineage
