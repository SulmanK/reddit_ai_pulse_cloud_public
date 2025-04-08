---
title: "Data Engineering Subreddit"
date: "2025-04-08"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Jira: Is it still helping teams... or just slowing them down?](https://www.reddit.com/r/dataengineering/comments/1ju81cr/jira_is_it_still_helping_teams_or_just_slowing/) (Score: 56)
    *   This thread discusses the usefulness of Jira for data engineering teams, with varied opinions on its effectiveness and potential drawbacks.
2.  [Ingesting a billion small .csv files from blob?](https://www.reddit.com/r/dataengineering/comments/1ju6uoo/ingesting_a_billion_small_csv_files_from_blob/) (Score: 16)
    *   This thread explores strategies for efficiently ingesting a large number of small CSV files from a blob storage, with a focus on parallel processing and leveraging tools like Snowflake and Iceberg.
3.  [Why do you dislike MS Fabric?](https://www.reddit.com/r/dataengineering/comments/1jukwsu/why_do_you_dislike_ms_fabric/) (Score: 16)
    *   Users discuss the downsides of using MS Fabric. Most users agree that it is too expensive, buggy, and is an unfinished product.
4.  [How did you start your data engineering journey?](https://www.reddit.com/r/dataengineering/comments/1ju9kqo/how_did_you_start_your_data_engineering_journey/) (Score: 11)
    *   This thread shares personal anecdotes about how different individuals transitioned into data engineering roles, highlighting diverse backgrounds and career paths.
5.  [What are the Python Data Engineering approaches every data scientist should know?](https://www.reddit.com/r/dataengineering/comments/1jugab3/what_are_the_python_data_engineering_approaches/) (Score: 5)
    *   This thread discusses recommended Python-related practices and approaches for data scientists transitioning into or collaborating with data engineering.
6.  [Clean architecture for Data Engineering](https://www.reddit.com/r/dataengineering/comments/1jukena/clean_architecture_for_data_engineering/) (Score: 3)
    *   A user asked for a reminder about a clean architecture for data engineering.
7.  [Help: Looking to set up a decent data architecture (data lake and/or warehouse)](https://www.reddit.com/r/dataengineering/comments/1juhrrs/help_looking_to_set_up_a_decent_data_architecture/) (Score: 2)
    *   This thread requests guidance on setting up a data architecture with a data lake and/or data warehouse, and provides links to learning resources.
8.  [What is the best way to reflect data in clickhouse from MySQL other than the MySQL engine?](https://www.reddit.com/r/dataengineering/comments/1ju7cmf/what_is_the_best_way_to_reflect_data_in/) (Score: 1)
    *   The thread seeks alternative methods for reflecting data from MySQL to ClickHouse, exploring CDC, binlog parsing, and replica setups.
9.  [How do you group your tables into pipelines?](https://www.reddit.com/r/dataengineering/comments/1jub08u/how_do_you_group_your_tables_into_pipelines/) (Score: 1)
    *   The thread discusses strategies for organizing tables into data pipelines, focusing on source-level ingestion, domain-level transformations, and addressing scheduling challenges.
10. [Is there any tool you use to keep track on the dates you need to reset API keys?](https://www.reddit.com/r/dataengineering/comments/1jucavs/is_there_any_tool_you_use_to_keep_track_on_the/) (Score: 1)
    *   This thread discusses tools and methods for tracking API key reset dates, with suggestions ranging from simple notepad reminders to secret managers and Airflow.
11. [GizmoSQL: Power your Enterprise analytics with Arrow Flight SQL and DuckDB](https://www.reddit.com/r/dataengineering/comments/1judm9f/gizmosql_power_your_enterprise_analytics_with/) (Score: 1)
    *   A bot posted an open-source project showcase for GizmoSQL.
12. [Question around migrating to dbt](https://www.reddit.com/r/dataengineering/comments/1jufvpe/question_around_migrating_to_dbt/) (Score: 1)
    *   This thread discusses reasons and considerations for migrating to dbt (data build tool) from existing ETL systems.
13. [Beginning Data Scientist in Azure needing some help (iot)](https://www.reddit.com/r/dataengineering/comments/1juj0x6/beginning_data_scientist_in_azure_needing_some/) (Score: 1)
    *   A user is seeking help with Azure IoT and is asking about who/what is pushing the sensor data.
14. [Lessons from optimizing dashboard performance on Looker Studio with BigQuery data](https://www.reddit.com/r/dataengineering/comments/1jujn9j/lessons_from_optimizing_dashboard_performance_on/) (Score: 1)
    *   This thread discusses strategies for optimizing dashboard performance in Looker Studio with BigQuery, including moving calculations to BigQuery queries and reducing data transfers.
15. [Experienced data engineer looking to expand to devops](https://www.reddit.com/r/dataengineering/comments/1ju693k/experienced_data_engineer_looking_to_expand_to/) (Score: 0)
    *   This thread seeks advice for an experienced data engineer transitioning to DevOps, focusing on understanding existing infrastructure and learning resources.
16. [Mirror snowflake to PG](https://www.reddit.com/r/dataengineering/comments/1jui1dg/mirror_snowflake_to_pg/) (Score: 0)
    *   This thread explores methods for mirroring data from Snowflake to PostgreSQL, including Snowflake Streams and Change Data Capture (CDC).
17. [Hot Take: You shouldn't be a data engineer if you've never been a data analyst](https://www.reddit.com/r/dataengineering/comments/1jukctt/hot_take_you_shouldnt_be_a_data_engineer_if_youve/) (Score: 0)
    *   A user shares their opinion that you shouldn't be a data engineer if you've never been a data analyst. Other users argue that software engineering skills are more important.

# Detailed Analysis by Thread
**[[D] Jira: Is it still helping teams... or just slowing them down? (Score: 56)](https://www.reddit.com/r/dataengineering/comments/1ju81cr/jira_is_it_still_helping_teams_or_just_slowing/)**
*   **Summary:** The thread revolves around the perceived benefits and drawbacks of using Jira for data engineering teams. Some users find it useful for feature and task tracking, while others see it as a hindrance that slows down development and is often misused by management.
*   **Emotion:** The overall emotional tone is neutral, with a mix of negative sentiment towards Jira's misuse and positive sentiment towards its potential for task tracking.
*   **Top 3 Points of View:**
    *   Jira is useful for feature/task tracking and documenting requirements.
    *   Jira becomes a problem when companies misuse it for ritualistic scrum or employee monitoring.
    *   Simpler tools like Monday and Trello can be better alternatives, but may lack complexity.

**[Ingesting a billion small .csv files from blob? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1ju6uoo/ingesting_a_billion_small_csv_files_from_blob/)**
*   **Summary:** The discussion centers on strategies for efficiently ingesting a billion small CSV files from a blob storage into a data warehouse, particularly Snowflake. The suggestions include using event-based triggers, parallel processing, and an intermediary lakehouse.
*   **Emotion:** The overall emotional tone is neutral, focusing on technical solutions.
*   **Top 3 Points of View:**
    *   Use an event-based trigger to ingest data via a cloud function.
    *   Utilize an intermediary lakehouse like Iceberg with proper partitioning before loading into Snowflake.
    *   Read the files in parallel to speed up processing.

**[Why do you dislike MS Fabric? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1jukwsu/why_do_you_dislike_ms_fabric/)**
*   **Summary:** This thread explores the reasons why data engineers dislike MS Fabric. Common complaints include it being too expensive, buggy, an unfinished product, and having a slimmed-down toolset compared to the 'proper' Azure tools.
*   **Emotion:** The overall emotional tone is negative, with users expressing frustration and disappointment with MS Fabric.
*   **Top 3 Points of View:**
    *   MS Fabric is too expensive for what it offers.
    *   It's a buggy and unfinished product, with a front-end that is a mess.
    *   It is a slimmed-down version of the 'proper' Azure tools without much cost saving.

**[How did you start your data engineering journey? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1ju9kqo/how_did_you_start_your_data_engineering_journey/)**
*   **Summary:** This thread is a collection of personal stories about how people began their careers in data engineering, highlighting different educational backgrounds, career transitions, and motivations.
*   **Emotion:** The overall emotional tone is neutral, with individuals sharing their experiences and journeys.
*   **Top 3 Points of View:**
    *   Transitioning from other fields like systems analysis or chemical engineering after recognizing the need for data infrastructure.
    *   Starting with programming or data science and then pivoting to data engineering due to interest or job opportunities.
    *   Being "forced" into data engineering due to the company's needs to shift to DL, despite lack of resources/pipeline.

**[What are the Python Data Engineering approaches every data scientist should know? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jugab3/what_are_the_python_data_engineering_approaches/)**
*   **Summary:** The discussion is about essential Python-related skills and practices that data scientists should be aware of when working in data engineering contexts, including version control, testing, code structure, and collaboration.
*   **Emotion:** The overall emotional tone is neutral, with users providing advice and recommendations.
*   **Top 3 Points of View:**
    *   Data scientists should use version control (git) and write unit/end-to-end tests.
    *   Data scientists should write testable code with well-defined, short functions.
    *    Data scientists should learn type annotations and use them.

**[Clean architecture for Data Engineering (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jukena/clean_architecture_for_data_engineering/)**
*   **Summary:** A user asked for a reminder about a clean architecture for data engineering.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    * N/A

**[Help: Looking to set up a decent data architecture (data lake and/or warehouse) (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1juhrrs/help_looking_to_set_up_a_decent_data_architecture/)**
*   **Summary:** This thread seeks guidance on setting up a data architecture with a data lake and/or data warehouse, and provides links to learning resources.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    * N/A

**[What is the best way to reflect data in clickhouse from MySQL other than the MySQL engine? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ju7cmf/what_is_the_best_way_to_reflect_data_in/)**
*   **Summary:** The thread seeks alternative methods for reflecting data from MySQL to ClickHouse, exploring CDC, binlog parsing, and replica setups.
*   **Emotion:** The overall emotional tone is positive, with users providing recommendations and resources.
*   **Top 3 Points of View:**
    *   Use Debezium with Kafka for reliable Change Data Capture (CDC).
    *   Parse MySQL's binlog to stream CDC events to ClickHouse.
    *   Create a MySQL replica to read data from it.

**[How do you group your tables into pipelines? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jub08u/how_do_you_group_your_tables_into_pipelines/)**
*   **Summary:** The thread discusses strategies for organizing tables into data pipelines, focusing on source-level ingestion, domain-level transformations, and addressing scheduling challenges.
*   **Emotion:** The overall emotional tone is neutral, with users discussing best practices and seeking advice.
*   **Top 3 Points of View:**
    *   Structure pipelines at the data source level and decouple ingestion from transformation.
    *   Group tables by domain and schedule domains one after the other.
    *   Use a proper orchestration tool with individual refresh logic for each table.

**[Is there any tool you use to keep track on the dates you need to reset API keys? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jucavs/is_there_any_tool_you_use_to_keep_track_on_the/)**
*   **Summary:** This thread discusses tools and methods for tracking API key reset dates, with suggestions ranging from simple notepad reminders to secret managers and Airflow.
*   **Emotion:** The overall emotional tone is neutral, with users sharing practical solutions.
*   **Top 3 Points of View:**
    *   Use a simple method like a notepad.
    *   Store secrets with expiration dates in secret managers or parameter stores and set up a notification process.
    *   Use Airflow to trigger reminders when secrets expire.

**[GizmoSQL: Power your Enterprise analytics with Arrow Flight SQL and DuckDB (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1judm9f/gizmosql_power_your_enterprise_analytics_with/)**
*   **Summary:** A bot posted an open-source project showcase for GizmoSQL.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   N/A

**[Question around migrating to dbt (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jufvpe/question_around_migrating_to_dbt/)**
*   **Summary:** This thread discusses reasons and considerations for migrating to dbt (data build tool) from existing ETL systems.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   N/A

**[Beginning Data Scientist in Azure needing some help (iot) (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1juj0x6/beginning_data_scientist_in_azure_needing_some/)**
*   **Summary:** A user is seeking help with Azure IoT and is asking about who/what is pushing the sensor data.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   N/A

**[Lessons from optimizing dashboard performance on Looker Studio with BigQuery data (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jujn9j/lessons_from_optimizing_dashboard_performance_on/)**
*   **Summary:** This thread discusses strategies for optimizing dashboard performance in Looker Studio with BigQuery, including moving calculations to BigQuery queries and reducing data transfers.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   N/A

**[Experienced data engineer looking to expand to devops (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ju693k/experienced_data_engineer_looking_to_expand_to/)**
*   **Summary:** This thread seeks advice for an experienced data engineer transitioning to DevOps, focusing on understanding existing infrastructure and learning resources.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   Learn everything about your existing infrastructure repository.
    *   Terraform is a cleaner way to interact with APIs.

**[Mirror snowflake to PG (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jui1dg/mirror_snowflake_to_pg/)**
*   **Summary:** This thread explores methods for mirroring data from Snowflake to PostgreSQL, including Snowflake Streams and Change Data Capture (CDC).
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Use Snowflake Streams (CDC).
    *   Use Change Data Capture (CDC).
    *   Any ETL tool can do this.

**[Hot Take: You shouldn't be a data engineer if you've never been a data analyst (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jukctt/hot_take_you_shouldnt_be_a_data_engineer_if_youve/)**
*   **Summary:** A user shares their opinion that you shouldn't be a data engineer if you've never been a data analyst. Other users argue that software engineering skills are more important.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Software engineering skills are much more important.
    *   Having analyst experience depends on the shop, roles and responsibilities.
    *   Learn proper software engineering pattern beats analyst.
