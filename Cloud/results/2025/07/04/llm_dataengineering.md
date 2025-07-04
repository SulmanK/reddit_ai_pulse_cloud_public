---
title: "Data Engineering Subreddit"
date: "2025-07-04"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ETL", "data stack"]
---

# Overall Ranking and Top Discussions
1.  [[D] 2025 Open Source Tech Stack](https://i.redd.it/0bwy1conkuaf1.png) (Score: 196)
    *   A visual representation of the 2025 open-source tech stack for data engineering, sparking discussion and critique regarding tool choices and omissions.
2.  [Which ETL tool makes sense if you want low maintenance but also decent control?](https://www.reddit.com/r/dataengineering/comments/1lrf8nb/which_etl_tool_makes_sense_if_you_want_low/) (Score: 28)
    *   Users are discussing which ETL tools offer a balance between low maintenance and decent control, with recommendations for various tools like Apache NiFi, Airbyte, and dlthub.com.
3.  [Strange first-round experience with a major bank for a DE role](https://www.reddit.com/r/dataengineering/comments/1lrhj95/strange_firstround_experience_with_a_major_bank/) (Score: 18)
    *   A user shares their experience with a disorganized and surface-level first-round interview for a Data Engineering role at a major bank, prompting discussion about the norms and red flags in banking interviews.
4.  [Please help, do modern BI systems need an analytics Database (DW etc.)](https://www.reddit.com/r/dataengineering/comments/1lrcx96/please_help_do_modern_bi_systems_need_an/) (Score: 12)
    *   A discussion about whether modern BI systems still require an analytics database (DW) or if they can directly query source systems, considering factors like scale, complexity, and performance.
5.  [Help a SWE get better at DE](https://www.reddit.com/r/dataengineering/comments/1lrhihi/help_a_swe_get_better_at_de/) (Score: 7)
    *   Discussion on how a Software Engineer can transition into Data Engineering, emphasizing SQL skills and practical experience in building data warehouses.
6.  [Graphical evaluation SQL database](https://www.reddit.com/r/dataengineering/comments/1lrgs7y/graphical_evaluation_sql_database/) (Score: 5)
    *   Users are discussing tools for graphical evaluation of SQL databases, with recommendations for DataGrip and Grafana for query building and time-series dashboards.
7.  [Anyone built parallel cloud and on-premise data platforms?](https://www.reddit.com/r/dataengineering/comments/1lrk6b4/anyone_built_parallel_cloud_and_onpremise_data/) (Score: 5)
    *   A question about building parallel data platforms in the cloud and on-premise, with a suggestion to decouple storage and compute using S3 and containerized solutions.
8.  [What’s the most annoying part of doing EDA for you?](https://www.reddit.com/r/dataengineering/comments/1lrpq9q/whats_the_most_annoying_part_of_doing_eda_for_you/) (Score: 4)
    *   Users are sharing their most annoying experiences during Exploratory Data Analysis (EDA), including dealing with high dimensionality, missing data, and lack of domain knowledge.
9.  [Industrial Controls/Automation Engineer to DE](https://www.reddit.com/r/dataengineering/comments/1lrk967/industrial_controlsautomation_engineer_to_de/) (Score: 3)
    *   A user shares their career transition from Industrial Controls/Automation Engineer to Data Engineering, describing their experience in building an IIoT system and automating analytics reports.
10. [Kafka stream through snowflake sink connector and batch load process parallelly on same snowflake table](https://www.reddit.com/r/dataengineering/comments/1lrmko8/kafka_stream_through_snowflake_sink_connector_and/) (Score: 3)
    *   A question regarding Kafka stream through Snowflake sink connector and batch load process parallelly on the same Snowflake table.
11. [Vertica DB MCP Server](https://www.reddit.com/r/dataengineering/comments/1lrdbjz/vertica_db_mcp_server/) (Score: 2)
    *   This post links to the dataengineering.wiki for open-source projects.
12. [How do you handle tiny schema drift in near real-time pipelines without overcomplicating everything?](https://www.reddit.com/r/dataengineering/comments/1lrl7k6/how_do_you_handle_tiny_schema_drift_in_near/) (Score: 2)
    *   A discussion about handling schema drift in near real-time data pipelines, with suggestions ranging from creating "corrected-data" topics to waiting until things break.
13. [How to switch to DE](https://www.reddit.com/r/dataengineering/comments/1lrm1t8/how_to_switch_to_de/) (Score: 2)
    *   A user is seeking advice on switching to data engineering from a sysadmin role.
14. [Help Needed for Exporting Data from IBM Access Client Solutions to Azure Blob Storage](https://www.reddit.com/r/dataengineering/comments/1lrjrzl/help_needed_for_exporting_data_from_ibm_access/) (Score: 1)
    *   A user needs help exporting data from IBM Access Client Solutions to Azure Blob Storage.
15. [Transition from SQL DBA to Data Engineering](https://www.reddit.com/r/dataengineering/comments/1lrr4yj/transition_from_sql_dba_to_data_engineering/) (Score: 1)
    *   This post links to the dataengineering.wiki for resources on transitioning into Data Engineering.
16. [AWS DE course for a Mid- Senior level engineer](https://www.reddit.com/r/dataengineering/comments/1lrrdbq/aws_de_course_for_a_mid_senior_level_engineer/) (Score: 1)
    *   This post links to the dataengineering.wiki for learning resources.
17. [AWS DMS "Out of Memory" Error During Full Load](https://www.reddit.com/r/dataengineering/comments/1lrril9/aws_dms_out_of_memory_error_during_full_load/) (Score: 1)
    *   A question about resolving "Out of Memory" errors with AWS DMS during a full load process.

# Detailed Analysis by Thread
**[[D] 2025 Open Source Tech Stack (Score: 196)](https://i.redd.it/0bwy1conkuaf1.png)**
*   **Summary:** A visual representation of the 2025 open-source tech stack for data engineering is shared, receiving critical feedback on specific tool choices and overall map quality. Users discuss the inclusion of tools like Docker and Sonnet 4, question the machine learning section's relevance, and suggest alternatives like FastAPI, sqlmesh, Ballista, DataFusion, and Redash.
*   **Emotion:** The overall emotional tone is Neutral, with some Negative comments expressing criticism towards the tech stack map and certain tool selections, and some Positive comments.
*   **Top 3 Points of View:**
    *   The map is inaccurate and poorly constructed.
    *   Docker is not open source, and should be replaced with podman.
    *   The machine learning section is confusing and includes irrelevant tools for learning machine learning.

**[Which ETL tool makes sense if you want low maintenance but also decent control? (Score: 28)](https://www.reddit.com/r/dataengineering/comments/1lrf8nb/which_etl_tool_makes_sense_if_you_want_low/)**
*   **Summary:** Users are seeking recommendations for ETL tools that offer a good balance between low maintenance and decent control. The discussion revolves around suggesting tools and architectures such as Apache Airflow with Polars, Apache NiFi, Airbyte, dlthub.com, starlake.ai, weld.app, slingdata.io, Coalesce.io, and Azure Data Factory, highlighting their features and benefits.
*   **Emotion:** The emotional tone is predominantly Neutral, with a hint of Positive sentiment in recommendations.
*   **Top 3 Points of View:**
    *   Apache NiFi is a good option due to its drag-and-drop UI and customizability.
    *   starlake.ai offers a code-free ingestion and low-code transformation approach.
    *   Azure Data Factory supplemented with Databricks notebooks can provide both low maintenance and customization.

**[Strange first-round experience with a major bank for a DE role (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1lrhj95/strange_firstround_experience_with_a_major_bank/)**
*   **Summary:** A user describes a disappointing first-round interview experience for a Data Engineering role at a major bank, characterized by surface-level questions and a lack of discussion about relevant topics. The discussion explores whether this experience is typical for tech roles at non-tech organizations, especially in banking, and advises the user to consider the experience as a reflection of the potential work environment.
*   **Emotion:** The emotional tone is Neutral, with some Positive comments expressing optimism.
*   **Top 3 Points of View:**
    *   The experience is normal for tech roles in banking.
    *   It's a red flag, but keep options open.
    *   Interviews are a two-way street, and this experience indicates a disorganized environment with outdated practices.

**[Please help, do modern BI systems need an analytics Database (DW etc.) (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1lrcx96/please_help_do_modern_bi_systems_need_an/)**
*   **Summary:** The thread discusses the necessity of an analytics database (DW) for modern BI systems. Opinions vary, with some arguing that a dedicated analytics layer is crucial for sustainable reporting and performance, especially when dealing with joins across systems and historical data. Others suggest that for smaller setups, querying ERP/CRM data directly might suffice. The discussion also addresses concerns about data duplication and the benefits of using tools like dbt or SQLmesh.
*   **Emotion:** The overall tone is Neutral, with the discussion focusing on technical considerations and trade-offs.
*   **Top 3 Points of View:**
    *   A dedicated analytics layer is essential for sustainable reporting and sane performance, especially with complex data transformations and historical analysis.
    *   For smaller setups, querying ERP/CRM data directly with a good BI tool can be sufficient.
    *   Data warehouses are not about duplication but about making data fit for questions the source app never had to answer.

**[Help a SWE get better at DE (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1lrhihi/help_a_swe_get_better_at_de/)**
*   **Summary:** The discussion focuses on how a Software Engineer (SWE) can effectively transition into Data Engineering (DE). SQL fluency is highlighted as a key skill, and practical experience in building a data warehouse is recommended.
*   **Emotion:** The emotional tone is Positive, offering advice and encouragement for the transition.
*   **Top 3 Points of View:**
    *   SQL fluency is key to getting better at DE.
    *   Building a tiny warehouse on Postgres is a great way to learn.
    *   Former SWEs can transition into data engineering with decent SQL skills.

**[Graphical evaluation SQL database (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1lrgs7y/graphical_evaluation_sql_database/)**
*   **Summary:**  This thread discusses tools for graphically evaluating SQL databases. The recommended solutions include DataGrip for query building and Grafana for time-series dashboards.
*   **Emotion:** The tone of the thread is Neutral, focusing on practical tool recommendations.
*   **Top 3 Points of View:**
    *   DataGrip is good for query building and inline result plotting.
    *   Grafana is useful for creating time-series dashboards.
    *   DreamFactory can be used to create REST endpoints for accessing the data.

**[Anyone built parallel cloud and on-premise data platforms? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1lrk6b4/anyone_built_parallel_cloud_and_onpremise_data/)**
*   **Summary:** This thread asks about experiences building parallel cloud and on-premise data platforms. The response suggests decoupling storage and compute using S3 and containerized solutions like Docker/Kubernetes.
*   **Emotion:** The thread maintains a Neutral tone, providing technical advice.
*   **Top 3 Points of View:**
    *   Decouple storage and compute.
    *   Use S3 for storage.
    *   Utilize Docker/Kubernetes for compute solutions.

**[What’s the most annoying part of doing EDA for you? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1lrpq9q/whats_the_most_annoying_part_of_doing_eda_for_you/)**
*   **Summary:** This thread discusses the most frustrating aspects of performing Exploratory Data Analysis (EDA). Key issues include the limitations of 2D/3D plotting for high-dimensional data, dealing with missing or malformed data, and a lack of semantic column names and domain knowledge.
*   **Emotion:** The overall tone is Neutral.
*   **Top 3 Points of View:**
    *   Limitations of 2D/3D plotting for high-dimensional data.
    *   Dealing with missing or malformed data.
    *   Lack of semantic column names and domain knowledge.

**[Industrial Controls/Automation Engineer to DE (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lrk967/industrial_controlsautomation_engineer_to_de/)**
*   **Summary:** A user shares their journey from an Industrial Controls/Automation Engineer to a Data Engineer. They describe building an Industrial Internet of Things (IIoT) system, streaming data with MQTT, and using tools like Mongo and PostgreSQL.
*   **Emotion:** The tone is Neutral, sharing a personal experience.
*   **Top 3 Points of View:**
    *   The user transitioned from industrial automation to software and data engineering.
    *   They have experience building data pipelines using MQTT, Mongo, and PostgreSQL.
    *   They automated analytics reporting and built operations dashboards.

**[Kafka stream through snowflake sink connector and batch load process parallelly on same snowflake table (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lrmko8/kafka_stream_through_snowflake_sink_connector_and/)**
*   **Summary:** A user is asking a question about Kafka stream through snowflake sink connector and batch load process parallelly on the same Snowflake table. This is a bot response providing a link to learning resources.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   N/A: This is a bot providing a link to learning resources.

**[Vertica DB MCP Server (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lrdbjz/vertica_db_mcp_server/)**
*   **Summary:** A user is asking a question about Vertica DB MCP Server. This is a bot response providing a link to open-source project showcase.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   N/A: This is a bot providing a link to learning resources.

**[How do you handle tiny schema drift in near real-time pipelines without overcomplicating everything? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lrl7k6/how_do_you_handle_tiny_schema_drift_in_near/)**
*   **Summary:**  This thread discusses strategies for handling schema drift in near real-time data pipelines. Suggestions include creating separate topics for corrected data and more involved processes.
*   **Emotion:** The tone varies from Neutral to Negative (waiting for things to break).
*   **Top 3 Points of View:**
    *   Create another topic called "corrected-data" and a subscriber that filters and modifies the "drifted-data".
    *   Wait till things break.
    *   Pi planning and formal handoff during UAT with simultaneous releases.

**[How to switch to DE (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lrm1t8/how_to_switch_to_de/)**
*   **Summary:** A sysadmin asks how to switch to DE, and the response is to learn Airflow and leverage system tuning skills.
*   **Emotion:** The tone is Neutral.
*   **Top 3 Points of View:**
    *   Sysadmin skills are transferable.
    *   Learn Airflow.
    *   System tuning is useful.

**[Help Needed for Exporting Data from IBM Access Client Solutions to Azure Blob Storage (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lrjrzl/help_needed_for_exporting_data_from_ibm_access/)**
*   **Summary:** A user needs assistance exporting data from IBM Access Client Solutions to Azure Blob Storage. A solution involving Python scripting is proposed.
*   **Emotion:** The tone is Neutral.
*   **Top 3 Points of View:**
    *   Use Python to export data.
    *   Install Azure SDK on IBM i.
    *   Schedule the Python script.

**[Transition from SQL DBA to Data Engineering (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lrr4yj/transition_from_sql_dba_to_data_engineering/)**
*   **Summary:**  This thread is a simple redirection provided by a bot, linking to dataengineering.wiki for resources on transitioning into data engineering.
*   **Emotion:** The tone is Neutral.
*   **Top 3 Points of View:**
    *   N/A: This is a bot providing a link to learning resources.

**[AWS DE course for a Mid- Senior level engineer (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lrrdbq/aws_de_course_for_a_mid_senior_level_engineer/)**
*   **Summary:**  This thread is a simple redirection provided by a bot, linking to dataengineering.wiki for learning resources.
*   **Emotion:** The tone is Neutral.
*   **Top 3 Points of View:**
    *   N/A: This is a bot providing a link to learning resources.

**[AWS DMS "Out of Memory" Error During Full Load (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lrril9/aws_dms_out_of_memory_error_during_full_load/)**
*   **Summary:** A user is encountering an "Out of Memory" error in AWS DMS during a full load. A solution is provided to increase replication instance size or use serverless with a maximum DCU.
*   **Emotion:** The tone is Neutral.
*   **Top 3 Points of View:**
    *   Increase replication instance size.
    *   Choose serverless with a maximum DCU.
