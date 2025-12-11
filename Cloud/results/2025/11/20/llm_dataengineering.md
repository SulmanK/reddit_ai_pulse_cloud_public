---
title: "Data Engineering Subreddit"
date: "2025-11-20"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "AI", "metadata"]
---

# Overall Ranking and Top Discussions
1. [[D] Data engineers who are not building LLM to SQL](https://www.reddit.com/r/dataengineering/comments/1p1y34k/data_engineers_who_are_not_building_llm_to_sql/) (Score: 101)
    *   Data engineers are discussing the interesting projects they're working on that aren't related to LLM to SQL.
2. [Unpopular opinion (to investors) - this current zeitgeist of force AI into everything sucks](https://www.reddit.com/r/dataengineering/comments/1p21iem/unpopular_opinion_to_investors_this_current/) (Score: 93)
    *   Users are sharing their opinion of forcing AI into everything.
3.  [Anyone else dealing with metadata scattered across multiple catalogs? How are you handling it?](https://www.reddit.com/r/dataengineering/comments/1p2auyi/anyone_else_dealing_with_metadata_scattered/) (Score: 22)
    *   People are sharing how they are dealing with their metadata scattered across multiple catalogs.
4.  [Why TSV files are often better than other *SV Files (; , | )](https://www.reddit.com/r/dataengineering/comments/1p1v65k/why_tsv_files_are_often_better_than_other_sv_files/) (Score: 18)
    *   Users are debating the advantages and disadvantages of using TSV files versus other delimited file formats for data engineering tasks.
5.  [How to prep for a Data Platform Engineer system design in one week](https://www.reddit.com/r/dataengineering/comments/1p1vgsd/how_to_prep_for_a_data_platform_engineer_system/) (Score: 16)
    *   People are discussing the preparations required for a Data Platform Engineer system design interview.
6.  [First ever Data Pipeline project review](https://www.reddit.com/r/dataengineering/comments/1p20thm/first_ever_data_pipeline_project_review/) (Score: 9)
    *   A bot shared an open-source project showcase and a form for submitting a project.
7.  [Need advice for a lost intern](https://www.reddit.com/r/dataengineering/comments/1p1yfla/need_advice_for_a_lost_intern/) (Score: 5)
    *   People are giving advice to a data engineering intern who feels lost.
8.  [PASS Summit 2025](https://www.reddit.com/r/dataengineering/comments/1p1lb1w/pass_summit_2025/) (Score: 4)
    *   Someone commented that people from Reddit like to be anonymous.
9.  [How real time alerts are being sent in real time transaction monitoring](https://www.reddit.com/r/dataengineering/comments/1p2av0g/how_real_time_alerts_are_being_sent_in_real_time/) (Score: 2)
    *   Someone answered that it can be as simple as an http request.
10. [4 YoE - Specialize in Full-Stack vs Data vs ML/RAG?](https://www.reddit.com/r/dataengineering/comments/1p2bx3k/4_yoe_specialize_in_fullstack_vs_data_vs_mlrag/) (Score: 1)
    *   A bot shared a list of learning resources.
11. [Solo developer for a whole migration project](https://www.reddit.com/r/dataengineering/comments/1p1x8we/solo_developer_for_a_whole_migration_project/) (Score: 1)
    *   People are offering to help someone who is working on a solo migration project.
12. [Sharing my data platform tech stack](https://www.reddit.com/r/dataengineering/comments/1p29gpl/sharing_my_data_platform_tech_stack/) (Score: 0)
    *   A bot shared a list of learning resources.

# Detailed Analysis by Thread
**[[D] Data engineers who are not building LLM to SQL (Score: 101)](https://www.reddit.com/r/dataengineering/comments/1p1y34k/data_engineers_who_are_not_building_llm_to_sql/)**
*  **Summary:** Data engineers are discussing the interesting projects they're working on that aren't related to LLM to SQL. These include cleaning up schema evolution for pipeline stability, building internal tools for surfacing contract changes, resolving SQL to CSV parsing issues, migrating to Databricks, building column-level data lineage tools, creating dashboard builders for small datasets, and deploying computational biology models.
*  **Emotion:** The overall emotional tone is Neutral. Although there are some positive sentiment scores, the majority are neutral.
*  **Top 3 Points of View:**
    *   Some data engineers are focusing on improving data pipeline reliability by cleaning up schema evolution and building internal tools to manage contract changes.
    *   Others are working on foundational data engineering tasks such as resolving data parsing and encoding issues or migrating to new data platforms like Databricks.
    *   Several data engineers are building internal tools and solutions, such as dashboard builders and data lineage tools, to support data analysis and governance.

**[Unpopular opinion (to investors) - this current zeitgeist of force AI into everything sucks (Score: 93)](https://www.reddit.com/r/dataengineering/comments/1p21iem/unpopular_opinion_to_investors_this_current/)**
*  **Summary:** Users are sharing their opinion of forcing AI into everything. Many believe that the push to integrate AI into everything is driven by investors who don't understand the product and is largely marketing hype. Some find it frustrating and see limited legitimate use cases for LLMs beyond expert assistance and copywriting.
*  **Emotion:** The overall emotional tone is Negative. A lot of people are tired and frustrated seeing AI being forced into everything.
*  **Top 3 Points of View:**
    *   The push for AI integration is primarily driven by investor hype rather than practical applications or product understanding.
    *   LLMs have limited real-world use cases, and many applications are simply marketing ploys.
    *   There's a sentiment that the focus on AI distracts from other valuable data engineering tasks and can lead to inefficient or inappropriate solutions.

**[Anyone else dealing with metadata scattered across multiple catalogs? How are you handling it? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1p2auyi/anyone_else_dealing_with_metadata_scattered/)**
*  **Summary:** People are sharing how they are dealing with their metadata scattered across multiple catalogs. Solutions include building custom metadata sync tools, federating data through Unity Catalog, and considering Master Data Management systems.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Some organizations have built their own custom tools to sync metadata from various catalogs into a centralized repository, despite the challenges of maintaining these tools.
    *   Federating data through a unified catalog like Unity Catalog is seen as a way to centralize access and manage metadata across different data sources.
    *   Master Data Management (MDM) systems are suggested as a long-term solution for managing metadata, particularly as data volume and complexity grow.

**[Why TSV files are often better than other *SV Files (; , | ) (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1p1v65k/why_tsv_files_are_often_better_than_other_sv_files/)**
*  **Summary:** Users are debating the advantages and disadvantages of using TSV files versus other delimited file formats for data engineering tasks. The discussion covers topics such as the robustness of parsers, the use of quoting characters, and the suitability of different file formats (e.g., Avro, Parquet, JSON) for various data engineering scenarios.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The robustness of modern parsers makes the choice of delimiter less critical, with some arguing that using robust parsing techniques negates the need for TSV.
    *   For complex data engineering tasks, binary formats like Avro or Parquet are preferred over delimited text files.
    *   For quick communication of query results to non-technical users, CSV remains a practical choice, while JSON is favored for human readability and support for nested structures.

**[How to prep for a Data Platform Engineer system design in one week (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1p1vgsd/how_to_prep_for_a_data_platform_engineer_system/)**
*  **Summary:** People are discussing the preparations required for a Data Platform Engineer system design interview. Advice includes understanding fundamental concepts like CAP theorem, data modeling, and differences between database systems, as well as familiarity with event-based and batch processing, and tools like Spark, Kafka, and Flink.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   A strong understanding of fundamental data engineering concepts, such as the CAP theorem, data modeling, and the differences between various database systems (e.g., RDS, Postgres, Trino, Hive), is essential.
    *   Familiarity with event-based and batch processing paradigms, along with tools like Spark, Kafka, and Flink, is crucial for designing effective data platforms.
    *   Practical preparation using resources like blog posts from companies like Netflix and Uber, as well as system design frameworks like the one from Hello Interview, can be helpful.

**[First ever Data Pipeline project review (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1p20thm/first_ever_data_pipeline_project_review/)**
*  **Summary:** A bot shared an open-source project showcase and a form for submitting a project.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The linked dataengineering.wiki provides a platform for showcasing open-source data pipeline projects.
    *   There is an opportunity for community members to have their projects featured on the showcase by submitting them through the provided Airtable form.
    *   This can be a valuable resource for learning about and contributing to data engineering projects.

**[Need advice for a lost intern (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p1yfla/need_advice_for_a_lost_intern/)**
*  **Summary:** People are giving advice to a data engineering intern who feels lost. Suggestions include breaking down the problem into smaller steps, exploring different technology options (e.g., Microsoft Fabric, Snowflake, dbt, Fivetran), and focusing on learning and problem-solving skills.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Breaking down the overall task into smaller, manageable steps (e.g., database schema design, data migration, data transformation, reporting) can make the project less overwhelming.
    *   Exploring different data platform options, such as Microsoft Fabric, Snowflake, dbt, and Fivetran, can provide insights into potential solutions and trade-offs.
    *   The intern should focus on developing problem-solving skills, independent thinking, and clear communication, as these are valuable for demonstrating competence and making superiors happy.

**[PASS Summit 2025 (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p1lb1w/pass_summit_2025/)**
*  **Summary:** Someone commented that people from Reddit like to be anonymous.
*  **Emotion:** The overall emotional tone is Negative.
*  **Top 3 Points of View:**
    *   Reddit users may not be receptive to meeting in person due to a preference for anonymity.

**[How real time alerts are being sent in real time transaction monitoring (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p2av0g/how_real_time_alerts_are_being_sent_in_real_time/)**
*  **Summary:** Someone answered that it can be as simple as an http request.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Real-time alerts in transaction monitoring can be implemented with simple HTTP requests.

**[4 YoE - Specialize in Full-Stack vs Data vs ML/RAG? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p2bx3k/4_yoe_specialize_in_fullstack_vs_data_vs_mlrag/)**
*  **Summary:** A bot shared a list of learning resources.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The linked dataengineering.wiki provides a platform for learning resources

**[Solo developer for a whole migration project (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p1x8we/solo_developer_for_a_whole_migration_project/)**
*  **Summary:** People are offering to help someone who is working on a solo migration project.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The user sought support for a solo migration project

**[Sharing my data platform tech stack (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p29gpl/sharing_my_data_platform_tech_stack/)**
*  **Summary:** A bot shared a list of learning resources.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The user should use Apache Airflow and DBT for SQL models.
