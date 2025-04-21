---
title: "Data Engineering Subreddit"
date: "2025-04-21"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "apache iceberg", "CDC"]
---

# Overall Ranking and Top Discussions
1.  [[D] What's the best tool for loading data into Apache Iceberg?](https://www.reddit.com/r/dataengineering/comments/1k4e9ja/whats_the_best_tool_for_loading_data_into_apache/) (Score: 25)
    *   The discussion revolves around identifying the most effective tools for loading data into Apache Iceberg, with mentions of Spark streaming, Estuary Flow, Daft and Flink.
2.  [How can I capture deletes in CDC if I can't modify the source system?](https://www.reddit.com/r/dataengineering/comments/1k46wz7/how_can_i_capture_deletes_in_cdc_if_i_cant_modify/) (Score: 15)
    *   The thread discusses strategies for capturing deletes in Change Data Capture (CDC) scenarios where the source system cannot be modified. It covers topics like brute force hash comparison, log-based replication, and full extract with diffing.
3.  [Can I become a Junior DE as a middle aged person?](https://www.reddit.com/r/dataengineering/comments/1k4hki6/can_i_become_a_junior_de_as_a_middle_aged_person/) (Score: 9)
    *   The conversation explores the possibility of a middle-aged person transitioning into a junior data engineering role. Participants share personal experiences, offer advice on standing out, and discuss the current job market.
4.  [Should I learn Scala?](https://www.reddit.com/r/dataengineering/comments/1k4hzeq/should_i_learn_scala/) (Score: 8)
    *   The discussion centers on whether learning Scala is beneficial for data engineering, with many suggesting focusing on Python/PySpark instead due to Scala's perceived decline.
5.  [Six Months with ClickHouse at CloudQuery (The Good, The Bad, and the Unexpected)](https://www.cloudquery.io/blog/six-months-with-clickhouse-at-cloudquery) (Score: 7)
    *   This thread discusses an article about experiences using ClickHouse at CloudQuery, focusing on valuable lessons learned during the implementation process.
6.  [DBT Logging, debugging and observability overall is a challenge. Discuss.](https://www.reddit.com/r/dataengineering/comments/1k48izz/dbt_logging_debugging_and_observability_overall/) (Score: 6)
    *   The thread discusses the challenges of logging, debugging, and observability when using DBT (Data Build Tool), and what solutions there are.
7.  [Will WSL Perform Better Than a VM on My Low-End Laptop?](https://www.reddit.com/r/dataengineering/comments/1k4aa0z/will_wsl_perform_better_than_a_vm_on_my_lowend/) (Score: 6)
    *   The discussion compares the performance of Windows Subsystem for Linux (WSL) versus a virtual machine (VM) on a low-end laptop.
8.  [Moving from Software Engineer to Data Engineer](https://www.reddit.com/r/dataengineering/comments/1k4eyv2/moving_from_software_engineer_to_data_engineer/) (Score: 5)
    *   This thread provides advice and insights for software engineers transitioning into data engineering roles, focusing on knowledge gaps and essential skills.
9.  [Anyone attending the Databricks Field Lab in London on April 29?](https://www.reddit.com/r/dataengineering/comments/1k45ujt/anyone_attending_the_databricks_field_lab_in/) (Score: 4)
    *   This is a simple question asking if anyone is attending a specific Databricks event.
10. [How can I speed up the Stream Buffering in BigQuery?](https://www.reddit.com/r/dataengineering/comments/1k471tz/how_can_i_speed_up_the_stream_buffering_in/) (Score: 4)
    *   This thread explores ways to optimize stream buffering in BigQuery, discussing querying the streaming buffer and handling delays.
11. [Sync data from snowflake to postgres](https://www.reddit.com/r/dataengineering/comments/1k4e0go/sync_data_from_snowflake_to_postgres/) (Score: 4)
    *   The thread discusses methods for syncing data from Snowflake to Postgres, questioning the constraints around using CDC (Change Data Capture).
12. [What’s the best way to upload a Parquet file to an Iceberg table in S3?](https://www.reddit.com/r/dataengineering/comments/1k4fz5s/whats_the_best_way_to_upload_a_parquet_file_to_an/) (Score: 4)
    *   The conversation focuses on the most efficient methods for uploading a Parquet file to an Iceberg table in S3.
13. [Thoughts on Prophecy?](https://www.reddit.com/r/dataengineering/comments/1k4gzcn/thoughts_on_prophecy/) (Score: 2)
    *   This thread discusses opinions on the Prophecy data engineering tool, with some skepticism towards low-code solutions.
14. [Thoughts on TOGAF vs CDMP certification](https://www.reddit.com/r/dataengineering/comments/1k4hl3x/thoughts_on_togaf_vs_cdmp_certification/) (Score: 2)
    *   This thread discusses the relevance and value of TOGAF and CDMP certifications in the field of data engineering.
15. [What does a data collective officer do?](https://www.reddit.com/r/dataengineering/comments/1k4fhg4/what_does_a_data_collective_officer_do/) (Score: 1)
    *   The discussion revolves around the unfamiliar role of a "data collective officer," with users speculating on the responsibilities.

# Detailed Analysis by Thread
**[[D] What's the best tool for loading data into Apache Iceberg? (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1k4e9ja/whats_the_best_tool_for_loading_data_into_apache/)**
*  **Summary:**  The discussion revolves around identifying the most effective tools for loading data into Apache Iceberg. Suggestions include Spark streaming, Estuary Flow, Daft, and Flink. Users are looking for lightweight options, especially for CDC data.
*  **Emotion:** The dominant emotion is Neutral, with some elements of Positive sentiment, as users share their experiences and suggest helpful tools.
*  **Top 3 Points of View:**
    *   Spark streaming is a viable option, but the OP is seeking more lightweight alternatives.
    *   Estuary Flow is presented as a real-time data movement tool specifically designed for Iceberg, handling CDC and schema evolution.
    *   Flink, in combination with Kafka, is suggested, though the commenter hasn't used the Flink Iceberg connector themselves.

**[How can I capture deletes in CDC if I can't modify the source system? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1k46wz7/how_can_i_capture_deletes_in_cdc_if_i_cant_modify/)**
*  **Summary:** The thread explores strategies for capturing deletes in Change Data Capture (CDC) scenarios where the source system cannot be modified. It covers topics like brute force hash comparison, log-based replication via tools like Airbyte, and full extract with diffing, especially handling SCD2 for dim-like tables.
*  **Emotion:** The overall emotional tone is Neutral, with users focusing on practical solutions and technical considerations.
*  **Top 3 Points of View:**
    *   Brute force hash comparison is one approach to detect deletes.
    *   Log-based replication using tools like Airbyte can capture deletes but depends on the database source and target.
    *   For dim-like tables needing delete tracking, a full extract and SCD2 handling might be better than CDC.

**[Can I become a Junior DE as a middle aged person? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1k4hki6/can_i_become_a_junior_de_as_a_middle_aged_person/)**
*  **Summary:** The conversation explores the possibility of a middle-aged person transitioning into a junior data engineering role. Participants share personal experiences, offer advice on standing out, and discuss the current job market.
*  **Emotion:** The emotional tone is mixed, with both Positive and Neutral sentiments. There's encouragement and sharing of success stories, but also realistic assessments of job market competitiveness.
*  **Top 3 Points of View:**
    *   It is possible to transition to a junior DE role as a middle-aged person, with transferable skills from previous experiences being valuable.
    *   The junior data engineering job market is competitive, requiring dedicated effort and potentially a focus on internships.
    *   Emphasizing soft skills and unique experiences can help a middle-aged candidate stand out from younger applicants.

**[Should I learn Scala? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1k4hzeq/should_i_learn_scala/)**
*  **Summary:** The discussion centers on whether learning Scala is beneficial for data engineering. The consensus leans towards focusing on Python/PySpark instead, due to Scala's perceived decline in popularity and the growing dominance of PySpark in the field.
*  **Emotion:** The overall emotional tone is Neutral, with a slight Negative undertone regarding Scala's future relevance.
*  **Top 3 Points of View:**
    *   Scala is becoming niche, and PySpark is the more relevant technology to focus on.
    *   Learning Python/PySpark is easier and more practical than Scala for most data engineering tasks.
    *   If choosing a secondary language, Java or Go might be more useful than Scala.

**[Six Months with ClickHouse at CloudQuery (The Good, The Bad, and the Unexpected) (Score: 7)](https://www.cloudquery.io/blog/six-months-with-clickhouse-at-cloudquery)**
*  **Summary:** This thread discusses an article about experiences using ClickHouse at CloudQuery, focusing on valuable lessons learned during the implementation process, with users sharing their own experiences with migrating to ClickHouse.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   ClickHouse can be cost-efficient, but there's a learning curve to maximizing its power.
    *   Some issues should have been anticipated earlier when considering ClickHouse.
    *   The article contains valuable lessons.

**[DBT Logging, debugging and observability overall is a challenge. Discuss. (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k48izz/dbt_logging_debugging_and_observability_overall/)**
*  **Summary:** The thread discusses the challenges of logging, debugging, and observability when using DBT (Data Build Tool), and what solutions there are.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   DBT isn't an observability tool.
    *   There are integrations for data quality and observability.
    *   The poster is asking about specific problems being experienced with DBT.

**[Will WSL Perform Better Than a VM on My Low-End Laptop? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k4aa0z/will_wsl_perform_better_than_a_vm_on_my_lowend/)**
*  **Summary:** The discussion compares the performance of Windows Subsystem for Linux (WSL) versus a virtual machine (VM) on a low-end laptop.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   WSL performance is similar to a VM since it's managed by Hyper-V.
    *   Dual booting Ubuntu might be a better option for performance.
    *   Insufficient memory can be a limiting factor for running both the host OS and a VM.

**[Moving from Software Engineer to Data Engineer (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1k4eyv2/moving_from_software_engineer_to_data_engineer/)**
*  **Summary:** This thread provides advice and insights for software engineers transitioning into data engineering roles, focusing on knowledge gaps and essential skills.
*  **Emotion:** The overall emotional tone is Neutral, with some element of Positive encouragement.
*  **Top 3 Points of View:**
    *   DevOps knowledge is a key area for software engineers to develop when moving into data engineering.
    *   Understanding tabular data concepts and business needs is crucial.
    *   Once the core concepts of a data pipeline click, software engineers should be fine.

**[Anyone attending the Databricks Field Lab in London on April 29? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k45ujt/anyone_attending_the_databricks_field_lab_in/)**
*  **Summary:** This is a simple question asking if anyone is attending a specific Databricks event.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The comments simply offers links to resources from the /dataengineering community.

**[How can I speed up the Stream Buffering in BigQuery? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k471tz/how_can_i_speed_up_the_stream_buffering_in/)**
*  **Summary:** This thread explores ways to optimize stream buffering in BigQuery, discussing querying the streaming buffer and handling delays.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The data is ready to query when it's in the buffer, but direct updates or deletions aren't possible.
    *   It is or has been possible to query the streaming buffer.
    *   The poster is asked if they are new to BigQuery and directed to the documentation.

**[Sync data from snowflake to postgres (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k4e0go/sync_data_from_snowflake_to_postgres/)**
*  **Summary:** The thread discusses methods for syncing data from Snowflake to Postgres, questioning the constraints around using CDC (Change Data Capture).
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  The size of the data and the timing requirements are important factors to consider.
    *  CDC might not be overkill, especially with managed services like Estuary available.
    *  Why CDC is considered overkill is being questioned by other engineers.

**[What’s the best way to upload a Parquet file to an Iceberg table in S3? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k4fz5s/whats_the_best_way_to_upload_a_parquet_file_to_an/)**
*  **Summary:** The conversation focuses on the most efficient methods for uploading a Parquet file to an Iceberg table in S3.
*  **Emotion:** The overall emotional tone is Neutral with some Positive sentiment around recommended solutions.
*  **Top 3 Points of View:**
    *   DuckDB can handle this.
    *   Use Glue to run pyspark code.
    *   Try spark with Iceberg integration to write directly to the Iceberg table.

**[Thoughts on Prophecy? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k4gzcn/thoughts_on_prophecy/)**
*  **Summary:** This thread discusses opinions on the Prophecy data engineering tool, with some skepticism towards low-code solutions.
*  **Emotion:** The overall emotional tone is slightly Negative.
*  **Top 3 Points of View:**
    *   Low-code solutions often create technical debt and lock-in issues.
    *   Code-first approaches work better long-term.
    *   Prophecy is like "Dreamweaver" for pyspark/Scala, the generated code is frustrating to update by hand.

**[Thoughts on TOGAF vs CDMP certification (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k4hl3x/thoughts_on_togaf_vs_cdmp_certification/)**
*  **Summary:** This thread discusses the relevance and value of TOGAF and CDMP certifications in the field of data engineering.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   TOGAF is a pretty good place to start.
    *   The only certifications talked about are platform, tool, or cloud.
    *   Platform certificates are just advanced marketing programs.

**[What does a data collective officer do? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k4fhg4/what_does_a_data_collective_officer_do/)**
*  **Summary:** The discussion revolves around the unfamiliar role of a "data collective officer," with users speculating on the responsibilities.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   It seems like a fancy title for collecting data.
    *   The role is unfamiliar, users recommend Google for information.
    *   Someone jokingly questions its validity.
