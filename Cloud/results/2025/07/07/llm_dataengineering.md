---
title: "Data Engineering Subreddit"
date: "2025-07-07"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Why Realtime Analytics Feels Like a Myth (and What You Can Actually Expect)](https://www.reddit.com/r/dataengineering/comments/1ltg0pt/why_realtime_analytics_feels_like_a_myth_and_what/) (Score: 32)
    *   The discussion centers on the challenges and realities of achieving real-time analytics, with many participants highlighting the trade-offs between latency, cost, and complexity.
2.  [What would be your dream architecture?](https://www.reddit.com/r/dataengineering/comments/1ltwttw/what_would_be_your_dream_architecture/) (Score: 25)
    *   Users share their preferred data architectures, often mentioning tools like Python, Airflow, dbt, Snowflake, BigQuery and Dagster.
3.  [Is there such a thing as  "embedded Airflow"](https://www.reddit.com/r/dataengineering/comments/1ltpaxq/is_there_such_a_thing_as_embedded_airflow/) (Score: 17)
    *   The thread discusses the possibility of "embedded Airflow" and explores alternative solutions for lightweight workflow orchestration, such as Prefect, Dagster, and Celery.
4.  [I built an open-source JSON visualizer that runs locally](https://www.reddit.com/r/dataengineering/comments/1lto3h0/i_built_an_opensource_json_visualizer_that_runs/) (Score: 17)
    *   A user introduces their open-source JSON visualizer tool, aiming to facilitate faster and more intuitive JSON data handling.
5.  [What is the term used for devices/programs that have access to internal metadata?](https://www.reddit.com/r/dataengineering/comments/1ltlf6n/what_is_the_term_used_for_devicesprograms_that/) (Score: 10)
    *   The discussion revolves around identifying the correct terminology for devices or programs that can access internal metadata, with suggestions including "telemetry," "instrumentation," "data catalog," and "metrics."
6.  [Our Snowflake pipeline became monster, so we tried Dynamic Tables - here's what happened](https://dataengineeringtoolkit.substack.com/p/dynamic-tables-snowflake) (Score: 9)
    *   The post discusses the user's experience with using Dynamic Tables in Snowflake to manage a complex pipeline.
7.  [Data Lakehouse Project](https://www.reddit.com/r/dataengineering/comments/1ltlkat/data_lakehouse_project/) (Score: 7)
    *   This thread is a general discussion about data lakehouse projects, with a bot providing a link to an open-source project showcase.
8.  [Designing reliable queueing system with Postgres for scale, common challenges and solution](https://www.reddit.com/gallery/1ltk5ov) (Score: 5)
    *   The post outlines the design of a reliable queueing system using Postgres, addressing challenges related to disk operations, wasted space, and status updates.
9.  [Looking for a study partner to prepare for Data Engineer or Data Analyst roles](https://www.reddit.com/r/dataengineering/comments/1ltzef6/looking_for_a_study_partner_to_prepare_for_data/) (Score: 5)
    *   A user is seeking a study partner to prepare for Data Engineer or Data Analyst roles.
10. [Star schema - flatten dimensional hierarchy?](https://www.reddit.com/r/dataengineering/comments/1ltsbjn/star_schema_flatten_dimensional_hierarchy/) (Score: 4)
    *   The discussion explores strategies for flattening dimensional hierarchies within a star schema, weighing the benefits and drawbacks of different approaches for simplification and performance.
11. [Best way to handle high volume Ethereum keypair storage?](https://www.reddit.com/r/dataengineering/comments/1ltt5rb/best_way_to_handle_high_volume_ethereum_keypair/) (Score: 3)
    *   The thread seeks advice on the best methods for managing high-volume Ethereum keypair storage.
12. [Best data modeling technique for silver layer in medallion architecure](https://www.reddit.com/r/dataengineering/comments/1lu3rhx/best_data_modeling_technique_for_silver_layer_in/) (Score: 2)
    *   The thread seeks advice on best data modeling techniques.
13. [Agentic Tool to push Excel files to Datalakes](https://www.reddit.com/r/dataengineering/comments/1ltmo46/agentic_tool_to_push_excel_files_to_datalakes/) (Score: 1)
    *   The discussion revolves around using an "agentic" tool to push Excel files to data lakes, and the complexities involved.
14. [Planning to switch back to Informatica powercenter developer domain from VLSI Physical Design.](https://www.reddit.com/r/dataengineering/comments/1ltqk4q/planning_to_switch_back_to_informatica/) (Score: 1)
    *   A user discusses switching back to Informatica.
15. [Stepping into Event Streaming with Microsoft Fabric](https://datanrg.blogspot.com/2025/07/stepping-into-event-streaming-with.html) (Score: 0)
    *   This thread expresses a lack of interest in Microsoft Fabric.
16. [A timeless guide to BigQuery partitioning and clustering still trending in 2025](https://www.reddit.com/r/dataengineering/comments/1ltwiq3/a_timeless_guide_to_bigquery_partitioning_and/) (Score: 0)
    *   This thread links to a guide about BigQuery partitioning and clustering.
17. [Key requirements for Data architects in the UK and EU](https://www.reddit.com/r/dataengineering/comments/1lu2csg/key_requirements_for_data_architects_in_the_uk/) (Score: 0)
    *   The thread is about the key requirements for Data architects in the UK and EU.

# Detailed Analysis by Thread
**[[D] Why Realtime Analytics Feels Like a Myth (and What You Can Actually Expect)](https://www.reddit.com/r/dataengineering/comments/1ltg0pt/why_realtime_analytics_feels_like_a_myth_and_what/) (Score: 32)**
*  **Summary:** The thread discusses the challenges and realities of achieving real-time analytics, with many participants highlighting the trade-offs between latency, cost, and complexity.
*  **Emotion:** The overall emotional tone is neutral. While some comments express positive sentiment about the possibilities of real-time analytics, most remain objective in assessing its limitations.
*  **Top 3 Points of View:**
    *   Real-time analytics has been overhyped, and its benefits depend heavily on the specific use case. For many reporting and dashboarding applications, near real-time (2-5 minutes) is sufficient.
    *   Achieving true real-time analytics (sub-second latency) is possible but often comes with significantly increased costs and complexity, particularly at scale.
    *   The definition of "real-time" varies depending on the context and the needs of the organization. It's crucial to align expectations and understand the trade-offs involved.

**[What would be your dream architecture?](https://www.reddit.com/r/dataengineering/comments/1ltwttw/what_would_be_your_dream_architecture/) (Score: 25)**
*  **Summary:** Users share their preferred data architectures, often mentioning tools like Python, Airflow, dbt, Snowflake, BigQuery and Dagster.
*  **Emotion:** The overall emotional tone is neutral, with a hint of positive sentiment as users express enthusiasm for their favorite tools and architectures.
*  **Top 3 Points of View:**
    *   A common dream architecture includes Python for general-purpose tasks, Airflow for orchestration, dbt for transformations, and Snowflake or BigQuery for data warehousing.
    *   Some users prefer open-source solutions like Dagster on Kubernetes with Podman, Postgres for storage, and dbt for data quality checks.
    *   The ideal architecture depends heavily on the specific data and the needs of the organization, with cost and expertise being major considerations.

**[Is there such a thing as  "embedded Airflow"](https://www.reddit.com/r/dataengineering/comments/1ltpaxq/is_there_such_a_thing_as_embedded_airflow/) (Score: 17)**
*  **Summary:** The thread discusses the possibility of "embedded Airflow" and explores alternative solutions for lightweight workflow orchestration, such as Prefect, Dagster, and Celery.
*  **Emotion:** The overall emotional tone is neutral, with some users expressing positive sentiment towards specific alternatives to Airflow.
*  **Top 3 Points of View:**
    *   Airflow can be overkill for small jobs, and lighter tools like Prefect and Dagster are better suited for "embedded" scenarios.
    *   Celery can be a sufficient task queue for simpler use cases, offering a more lightweight alternative to full-fledged orchestrators.
    *   Managed Airflow solutions like GCP Composer, AWS MWAA, and Astronomer can reduce the maintenance burden for small teams.

**[I built an open-source JSON visualizer that runs locally](https://www.reddit.com/r/dataengineering/comments/1lto3h0/i_built_an_opensource_json_visualizer_that_runs/) (Score: 17)**
*  **Summary:** A user introduces their open-source JSON visualizer tool, aiming to facilitate faster and more intuitive JSON data handling.
*  **Emotion:** The overall emotional tone is positive, with users expressing interest in the tool and its potential benefits.
*  **Top 3 Points of View:**
    *   The tool could potentially help users work faster with JSON data by providing a better way to visualize its structure.
    *   (From a bot) Open-source projects can be showcased on dataengineering.wiki.
    *   N/A (Not enough distinct viewpoints for 3)

**[What is the term used for devices/programs that have access to internal metadata?](https://www.reddit.com/r/dataengineering/comments/1ltlf6n/what_is_the_term_used_for_devicesprograms_that/) (Score: 10)**
*  **Summary:** The discussion revolves around identifying the correct terminology for devices or programs that can access internal metadata, with suggestions including "telemetry," "instrumentation," "data catalog," and "metrics."
*  **Emotion:** The overall emotional tone is neutral. The discussion is largely informative and seeking clarification.
*  **Top 3 Points of View:**
    *   "Telemetry" refers to systems that collect internal metadata, performance metrics, and user behavior.
    *   "Instrumentation" is the process of embedding data collection into an application, service, or device.
    *   "Data catalog" and "metrics" are also relevant terms for describing access to internal metadata.

**[Our Snowflake pipeline became monster, so we tried Dynamic Tables - here's what happened](https://dataengineeringtoolkit.substack.com/p/dynamic-tables-snowflake) (Score: 9)**
*  **Summary:** The post discusses the user's experience with using Dynamic Tables in Snowflake to manage a complex pipeline.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Dynamic tables are similar to materialised views with refresh logic.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Data Lakehouse Project](https://www.reddit.com/r/dataengineering/comments/1ltlkat/data_lakehouse_project/) (Score: 7)**
*   **Summary:** This thread is a general discussion about data lakehouse projects, with a bot providing a link to an open-source project showcase.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   (From a bot) Open-source projects can be showcased on dataengineering.wiki.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Designing reliable queueing system with Postgres for scale, common challenges and solution](https://www.reddit.com/gallery/1ltk5ov) (Score: 5)**
*   **Summary:** The post outlines the design of a reliable queueing system using Postgres, addressing challenges related to disk operations, wasted space, and status updates.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Batch events into large groups in memory before writing them to disk.
    *   Run a periodic "compaction" job that copies any remaining unprocessed events into a new block.
    *   Write all status updates to a separate, dedicated status queue as a simple log.

**[Looking for a study partner to prepare for Data Engineer or Data Analyst roles](https://www.reddit.com/r/dataengineering/comments/1ltzef6/looking_for_a_study_partner_to_prepare_for_data/) (Score: 5)**
*   **Summary:** A user is seeking a study partner to prepare for Data Engineer or Data Analyst roles.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Interested individuals are offering to be study partners.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Star schema - flatten dimensional hierarchy?](https://www.reddit.com/r/dataengineering/comments/1ltsbjn/star_schema_flatten_dimensional_hierarchy/) (Score: 4)**
*   **Summary:** The discussion explores strategies for flattening dimensional hierarchies within a star schema, weighing the benefits and drawbacks of different approaches for simplification and performance.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Flatten natural hierarchies and use surrogate keys for each level.
    *   Flatten the hierarchy and keep it simple, using business IDs as attributes.
    *   Consider the consuming applications to help inform the structure.

**[Best way to handle high volume Ethereum keypair storage?](https://www.reddit.com/r/dataengineering/comments/1ltt5rb/best_way_to_handle_high_volume_ethereum_keypair/) (Score: 3)**
*   **Summary:** The thread seeks advice on the best methods for managing high-volume Ethereum keypair storage.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The solution depends on the available resources (CPU, RAM) and whether cloud resources are being used.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Best data modeling technique for silver layer in medallion architecure](https://www.reddit.com/r/dataengineering/comments/1lu3rhx/best_data_modeling_technique_for_silver_layer_in/) (Score: 2)**
*   **Summary:** The thread seeks advice on best data modeling techniques.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Use data vault followed by dimensional layer.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Agentic Tool to push Excel files to Datalakes](https://www.reddit.com/r/dataengineering/comments/1ltmo46/agentic_tool_to_push_excel_files_to_datalakes/) (Score: 1)**
*   **Summary:** The discussion revolves around using an "agentic" tool to push Excel files to data lakes, and the complexities involved.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   It used to be a simple lambda function.
    *   One solution is to use parallel calls, solid evals, and long-term memory, along with a sandbox environment like Docker.
    *   Why not simply write code to push excel files to Datalakes?

**[Planning to switch back to Informatica powercenter developer domain from VLSI Physical Design.](https://www.reddit.com/r/dataengineering/comments/1ltqk4q/planning_to_switch_back_to_informatica/) (Score: 1)**
*   **Summary:** A user discusses switching back to Informatica.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Instead of Informatica Powercenter, consider Informatica Cloud Data Integration and Informatica Cloud Application Integration.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Stepping into Event Streaming with Microsoft Fabric](https://datanrg.blogspot.com/2025/07/stepping-into-event-streaming-with.html) (Score: 0)**
*   **Summary:** This thread expresses a lack of interest in Microsoft Fabric.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   No interest in Microsoft Fabric.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[A timeless guide to BigQuery partitioning and clustering still trending in 2025](https://www.reddit.com/r/dataengineering/comments/1ltwiq3/a_timeless_guide_to_bigquery_partitioning_and/) (Score: 0)**
*   **Summary:** This thread links to a guide about BigQuery partitioning and clustering.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   (From a bot) Open-source projects can be showcased on dataengineering.wiki.
    *   N/A (Not enough distinct viewpoints for 3)
    *   N/A (Not enough distinct viewpoints for 3)

**[Key requirements for Data architects in the UK and EU](https://www.reddit.com/r/dataengineering/comments/1lu2csg/key_requirements_for_data_architects_in_the_uk/) (Score: 0)**
*   **Summary:** The thread is about the key requirements for Data architects in the UK and EU.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Gain theoretical knowledge and certifications to "be the boss".
    *   Focus on practical skills and learn by doing, working as a data engineer.
    *   N/A (Not enough distinct viewpoints for 3)
