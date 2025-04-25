---
title: "Data Engineering Subreddit"
date: "2025-04-25"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Woken up by a mystery incident caused by an untracked SQL fix? 🌝 Hope you haven't been there ...](https://i.redd.it/zt5n3lcjcywe1.png) (Score: 172)
    *   Users share relatable experiences and express the challenges of dealing with untracked SQL fixes and the importance of documentation.
2.  [Best approach for reading partitioned Parquet data: Python (Pandas/Polars) vs AWS Athena?](https://www.reddit.com/r/dataengineering/comments/1k7lp9q/best_approach_for_reading_partitioned_parquet/) (Score: 15)
    *   Discussion about the optimal method for reading partitioned Parquet data, comparing Python libraries like Pandas and Polars with AWS Athena.
3.  [Data Architect podcast episode for systems integration and data solutions in payments and fintech](https://www.reddit.com/r/dataengineering/comments/1k7f6gx/data_architect_podcast_episode_for_systems/) (Score: 12)
    *   A user shares a podcast episode about data architecture in payments and fintech.
4.  [How Do You Track Column-Level Lineage Between dbt/SQLMesh and Power BI (with Snowflake)?](https://www.reddit.com/r/dataengineering/comments/1k7cj7i/how_do_you_track_columnlevel_lineage_between/) (Score: 11)
    *   Discussion on methods for tracking column-level lineage between dbt/SQLMesh and Power BI in Snowflake, with suggestions for using Snowflake metadata, OpenLineage, and OpenMetadata.
5.  [How do you guys deal with unexpected datatypes in ETL processes?](https://www.reddit.com/r/dataengineering/comments/1k7n4uc/how_do_you_guys_deal_with_unexpected_datatypes_in/) (Score: 7)
    *   Users discuss strategies for handling unexpected data types in ETL processes, including validation steps, data contracts, and defensive coding.
6.  [How does real world Acceptance criteria look like](https://www.reddit.com/r/dataengineering/comments/1k7ml97/how_does_real_world_acceptance_criteria_look_like/) (Score: 6)
    *   A discussion on what acceptance criteria look like in real-world data engineering projects.
7.  [Built a tool to collapse the CSV → analysis → shareable app pipeline into a single step](https://www.reddit.com/r/dataengineering/comments/1k7elh2/built_a_tool_to_collapse_the_csv_analysis/) (Score: 5)
    *   A user introduces a tool to simplify the CSV to analysis pipeline.
8.  [HIPAA compliance and Data Engineering](https://www.reddit.com/r/dataengineering/comments/1k7jrjr/hipaa_compliance_and_data_engineering/) (Score: 2)
    *   Discussion on HIPAA compliance in data engineering.
9.  [Delta Load Into an Enrichment Layer](https://www.reddit.com/r/dataengineering/comments/1k7hxii/delta_load_into_an_enrichment_layer/) (Score: 1)
    *   The proper SQL join is a full outer join.
10. [DWH - Migration to Cloud - Steps](https://www.reddit.com/r/dataengineering/comments/1k7tvq0/dwh_migration_to_cloud_steps/) (Score: 1)
    *   The discussion is about the steps involved in migrating a Data Warehouse (DWH) to the cloud
11. [Can AI replace data professionals yet?](https://medium.com/@prashant.tandan528/how-far-till-an-ai-replaces-data-scientists-and-engineers-c4efe8c508f7) (Score: 0)
    *   Discussion on the possibility of AI replacing data scientists and engineers.
12. [IICS Parent and Sub Orgs Resource Contetion](https://www.reddit.com/r/dataengineering/comments/1k7mvvt/iics_parent_and_sub_orgs_resource_contetion/) (Score: 0)
    *   A bot provides a link to community-submitted learning resources.

# Detailed Analysis by Thread
**[ Woken up by a mystery incident caused by an untracked SQL fix? 🌝 Hope you haven't been there ... (Score: 172)](https://i.redd.it/zt5n3lcjcywe1.png)**
*  **Summary:**  Users share relatable experiences and express the challenges of dealing with untracked SQL fixes and the importance of documentation.
*  **Emotion:** The overall emotional tone is predominantly neutral. There is a mix of negative sentiments related to the frustrations caused by untracked SQL fixes, and some positive sentiments from those who can relate.
*  **Top 3 Points of View:**
    *   The lack of documentation in SQL projects can lead to phobias and difficulties in maintenance.
    *   Proper documentation is crucial, but finding examples for huge SQL queries can be challenging.
    *   Experiencing incidents caused by untracked SQL fixes is a common and frustrating occurrence.

**[ Best approach for reading partitioned Parquet data: Python (Pandas/Polars) vs AWS Athena? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1k7lp9q/best_approach_for_reading_partitioned_parquet/)**
*  **Summary:** Discussion about the optimal method for reading partitioned Parquet data, comparing Python libraries like Pandas and Polars with AWS Athena.
*  **Emotion:** The overall emotional tone of the thread is neutral, focusing on technical considerations and advice rather than expressing strong emotions.
*  **Top 3 Points of View:**
    *   For ML tasks involving larger datasets, Polars or DuckDB are better choices than Athena due to Python integration and performance.
    *   Polars is significantly faster than DuckDB for reading Parquet files from S3, with predicate pushdown capabilities.
    *   Consider the frequency of data access, the size of the data, and the need for distributed processing when choosing between Python libraries and Athena.

**[ Data Architect podcast episode for systems integration and data solutions in payments and fintech (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1k7f6gx/data_architect_podcast_episode_for_systems/)**
*  **Summary:** A user shares a podcast episode about data architecture in payments and fintech.
*  **Emotion:** The overall emotion is positive, with some neutral sentiment, expressing appreciation for the content and interest in listening.
*  **Top 3 Points of View:**
    *   The podcast is appreciated and will be listened to.
    *   Inquiry about a non-Spotify version of the podcast.

**[ How Do You Track Column-Level Lineage Between dbt/SQLMesh and Power BI (with Snowflake)? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1k7cj7i/how_do_you_track_columnlevel_lineage_between/)**
*  **Summary:** Discussion on methods for tracking column-level lineage between dbt/SQLMesh and Power BI in Snowflake, with suggestions for using Snowflake metadata, OpenLineage, and OpenMetadata.
*  **Emotion:** The emotional tone is neutral, focusing on providing helpful information and suggestions.
*  **Top 3 Points of View:**
    *   Snowflake metadata can be used to track column lineage.
    *   OpenLineage is a good standard for lineage metadata.
    *   OpenMetadata supports column-level lineage for Snowflake/PowerBI/dbt.

**[ How do you guys deal with unexpected datatypes in ETL processes? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1k7n4uc/how_do_you_guys_deal_with_unexpected_datatypes_in/)**
*  **Summary:** Users discuss strategies for handling unexpected data types in ETL processes, including validation steps, data contracts, and defensive coding.
*  **Emotion:** The emotional tone is mixed. Some users express frustration, while others offer practical solutions, resulting in an overall neutral sentiment.
*  **Top 3 Points of View:**
    *   Establish data contracts with upstream sources to ensure data reliability.
    *   Implement validation steps in ETL processes to detect and handle bad data.
    *   Use defensive coding practices and early failure mechanisms to manage unexpected data types.

**[ How does real world Acceptance criteria look like (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k7ml97/how_does_real_world_acceptance_criteria_look_like/)**
*  **Summary:** A discussion on what acceptance criteria look like in real-world data engineering projects.
*  **Emotion:** The emotional tone is generally positive.
*  **Top 3 Points of View:**
    *   Acceptance criteria are not always formally defined and can be based on stakeholder satisfaction.
    *   Acceptance criteria can include statements that specify an ETL pipeline should load data from X to Y without errors or that data quality checks should flag anomalies that match business rules.
    *  Personal projects can have acceptance criteria based on outcomes like running without manual intervention.

**[ Built a tool to collapse the CSV → analysis → shareable app pipeline into a single step (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1k7elh2/built_a_tool_to_collapse_the_csv_analysis/)**
*  **Summary:** A user introduces a tool to simplify the CSV to analysis pipeline.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   A bot provides links to open-source projects and a submission form to be featured.

**[ HIPAA compliance and Data Engineering (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k7jrjr/hipaa_compliance_and_data_engineering/)**
*  **Summary:** Discussion on HIPAA compliance in data engineering.
*  **Emotion:** The emotional tone is neutral, focusing on providing informative and factual details.
*  **Top 3 Points of View:**
    *   HIPAA and PII are distinct concepts, with HIPAA specifically covering protected health information.
    *   Separating regular and sensitive data into different data lakes is a sensible approach for maintaining compliance.
    *   Having a dedicated sensitive development environment with controlled access is a solid practice.

**[ Delta Load Into an Enrichment Layer (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k7hxii/delta_load_into_an_enrichment_layer/)**
*  **Summary:** The proper SQL join is a full outer join.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   To return data from two joined tables regardless of whether one table has a record of the join, you need to use a full outer join.

**[ DWH - Migration to Cloud - Steps (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k7tvq0/dwh_migration_to_cloud_steps/)**
*  **Summary:** The discussion is about the steps involved in migrating a Data Warehouse (DWH) to the cloud.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Point your tool to the new DWH and keep the source settings the same.

**[ Can AI replace data professionals yet? (Score: 0)](https://medium.com/@prashant.tandan528/how-far-till-an-ai-replaces-data-scientists-and-engineers-c4efe8c508f7)**
*  **Summary:** Discussion on the possibility of AI replacing data scientists and engineers.
*  **Emotion:** The emotional tone is negative with some positive and neutral sentiments.
*  **Top 3 Points of View:**
    *   AI will never replace DE because source systems will always be full of user errors.
    *   The posters should be banned.
    *   Hope AI will not replace data professionals.

**[ IICS Parent and Sub Orgs Resource Contetion (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k7mvvt/iics_parent_and_sub_orgs_resource_contetion/)**
*  **Summary:** A bot provides a link to community-submitted learning resources.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   A bot provides links to learning resources.
