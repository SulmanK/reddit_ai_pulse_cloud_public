---
title: "Data Engineering Subreddit"
date: "2025-08-05"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How we solved ingesting spreadsheets](https://www.reddit.com/r/dataengineering/comments/1mi9e8f/how_we_solved_ingesting_spreadsheets/) (Score: 35)
    *   This thread discusses a new tool for ingesting spreadsheets, with some users expressing enthusiasm and others raising concerns about adoption and the tool's limitations compared to existing solutions.
2.  [successful deployment of ai agents for analytics requests](https://www.reddit.com/r/dataengineering/comments/1mia426/successful_deployment_of_ai_agents_for_analytics/) (Score: 13)
    *   This thread is about deploying AI agents for analytics requests, with people curious about experiences with this.
3.  [Sling vs dlt's SQL connector Benchmark](https://www.reddit.com/r/dataengineering/comments/1mi9w04/sling_vs_dlts_sql_connector_benchmark/) (Score: 6)
    *   This thread compares Sling and dlt's SQL connectors. One user reports that dlt was impossibly slow with MSSQL servers.
4.  [Custom visualizations for BI solution](https://www.reddit.com/r/dataengineering/comments/1miihny/custom_visualizations_for_bi_solution/) (Score: 3)
    *   This thread is about custom visualizations for BI solutions, with a recommendation for Google BigQuery and a wish for a Snowflake PowerBI replacement.
5.  [DLThub/Sling/Airbyte/etc users, do you let the apps create tables in target database, or use migrations (such as alembic)?](https://www.reddit.com/r/dataengineering/comments/1miisiy/dlthubslingairbyteetc_users_do_you_let_the_apps/) (Score: 3)
    *   The question is if users allow apps like DLThub/Sling/Airbyte create tables in target databases, or use migrations.
6.  [How do you validate the feeds before loading into staging?](https://www.reddit.com/r/dataengineering/comments/1miakw4/how_do_you_validate_the_feeds_before_loading_into/) (Score: 2)
    *   This thread asks about methods for validating data feeds before loading them into staging, with suggestions including Pydantic, Great Expectations, Pandera, and dlt.
7.  [How to migrate a complex BigQuery Scheduled Query into dbt?](https://www.reddit.com/r/dataengineering/comments/1miaxe9/how_to_migrate_a_complex_bigquery_scheduled_query/) (Score: 2)
    *   This thread discusses how to migrate a BigQuery scheduled query into dbt, with a suggestion to use an incremental model.
8.  [General consensus on Docker/Linux](https://www.reddit.com/r/dataengineering/comments/1mijpgx/general_consensus_on_dockerlinux/) (Score: 1)
    *   This thread is about the general consensus on Docker/Linux, with a comment about Docker on Windows being inefficient.
9.  [Looking for a reliable way to extract structured data from messy PDFs ?](https://v.redd.it/kkstvllws7hf1) (Score: 0)
    *   The thread asks about a reliable way to extract structured data from messy PDFs, with a comment suggesting it's a bot ad.
10. [Ask in English, get the SQL—built a generator and would love your thoughts](https://www.reddit.com/r/dataengineering/comments/1mi6u1u/ask_in_english_get_the_sqlbuilt_a_generator_and/) (Score: 0)
    *   This thread discusses a tool that generates SQL from English queries, but receives negative feedback regarding security, necessity, and competition from existing tools.
11. [Are there any sites specific for data engineers looking for some contract work?](https://www.reddit.com/r/dataengineering/comments/1mi7lwa/are_there_any_sites_specific_for_data_engineers/) (Score: 0)
    *   This is a question about sites specific for data engineers looking for contract work.
12. [New tool in data world](https://www.reddit.com/r/dataengineering/comments/1mi9rym/new_tool_in_data_world/) (Score: 0)
    *   This thread discusses Alteryx, with mixed opinions about its usefulness and relevance in the current data engineering landscape.
13. [Is it possible to become an Analytics Engineer without orchestration tools experience](https://www.reddit.com/r/dataengineering/comments/1mibg4c/is_it_possible_to_become_an_analytics_engineer/) (Score: 0)
    *   This thread asks if it's possible to become an Analytics Engineer without orchestration tools experience, with responses suggesting that solid modeling skills and stakeholder communication are more important.
14. [Should I switch to DE from DS?](https://www.reddit.com/r/dataengineering/comments/1mih7no/should_i_switch_to_de_from_ds/) (Score: 0)
    *   This thread is asking if someone should switch to Data Engineering from Data Science.

# Detailed Analysis by Thread
**[How we solved ingesting spreadsheets (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1mi9e8f/how_we_solved_ingesting_spreadsheets/)**
*   **Summary:**  This thread discusses a new tool for ingesting spreadsheets. Users provide feedback on the tool, including suggestions for improvement, concerns about stakeholder adoption, and questions about implementation details like referential integrity and testing. Some users express strong enthusiasm, while others are more skeptical.
*   **Emotion:** The overall emotional tone is mixed. While there's excitement and positive feedback ("This is awesome," "Great looking app") reflected in the positive sentiment scores, there's also skepticism and concerns about real-world applicability.  The dominant emotion appears to be Neutral, reflecting a balanced discussion and objective assessment of the tool.
*   **Top 3 Points of View:**
    *   The tool is a valuable solution to the common problem of ingesting and managing data from spreadsheets.
    *   Stakeholder adoption and integration with existing systems will be challenging.
    *   The tool should consider features like foreign key enforcement and regression testing to ensure data quality.

**[successful deployment of ai agents for analytics requests (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1mia426/successful_deployment_of_ai_agents_for_analytics/)**
*   **Summary:** The thread starter shares that they have deployed AI agents for analytics requests. Others are curious about their experiences with it.
*   **Emotion:** The overall emotional tone is Neutral, with a sentiment score of 0.90.
*   **Top 3 Points of View:**
    *   The main point of view is curiosity about the experience with deploying AI agents for analytics.

**[Sling vs dlt's SQL connector Benchmark (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mi9w04/sling_vs_dlts_sql_connector_benchmark/)**
*   **Summary:** This thread presents a benchmark of Sling versus dlt's SQL connector. One user reports that dlt was very slow with MSSQL. A bot also posted a link to learning resources.
*   **Emotion:** The emotional tone is mixed, with both Negative and Neutral sentiments expressed. The negative sentiment stems from the performance issues experienced with dlt, while the neutral sentiment is from the bot posting the link.
*   **Top 3 Points of View:**
    *   dlt's SQL connector is slow with MSSQL.
    *   Sling may be a faster alternative.
    *   Community learning resources are available for data engineering.

**[Custom visualizations for BI solution (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1miihny/custom_visualizations_for_bi_solution/)**
*   **Summary:**  This thread discusses custom visualizations for BI solutions. A BigQuery solution is suggested, and a user expresses a desire for a Snowflake alternative to PowerBI. Another user suggests using the mobile view in PowerBI.
*   **Emotion:** The emotional tone is mixed, with Neutral as a dominant emotion. Positive sentiment indicates there's a potential positive solution.
*   **Top 3 Points of View:**
    *   Google BigQuery is a potential solution.
    *   A Snowflake-based PowerBI replacement would be desirable.
    *   PowerBI's mobile view might offer an alternative approach.

**[DLThub/Sling/Airbyte/etc users, do you let the apps create tables in target database, or use migrations (such as alembic)? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1miisiy/dlthubslingairbyteetc_users_do_you_let_the_apps/)**
*   **Summary:** The thread is asking if users allow apps like DLThub/Sling/Airbyte create tables in target databases, or use migrations.
*   **Emotion:** The overall emotional tone is Neutral, with a sentiment score of 0.91.
*   **Top 3 Points of View:**
    *   Most of the time, users let the tool create the tables.

**[How do you validate the feeds before loading into staging? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1miakw4/how_do_you_validate_the_feeds_before_loading_into/)**
*   **Summary:** This thread discusses how to validate data feeds before loading into staging. Suggestions included using pydantic, Great Expectations, Pandera or dlt.
*   **Emotion:** The overall emotional tone is Neutral, with all comments having Neutral sentiment.
*   **Top 3 Points of View:**
    *   Use Pydantic for validation.
    *   Incorporate a validation step into Airflow DAGs using Great Expectations or Pandera.
    *   Use dlt for schema evolution and data contract enforcement.

**[How to migrate a complex BigQuery Scheduled Query into dbt? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1miaxe9/how_to_migrate_a_complex_bigquery_scheduled_query/)**
*   **Summary:**  The thread discusses how to migrate a complex BigQuery scheduled query into dbt. The suggested solution involves using an incremental model in dbt to pull new data based on a timestamp.
*   **Emotion:** The overall emotional tone is Neutral, with a high sentiment score.
*   **Top 3 Points of View:**
    *   Use a dbt incremental model to migrate the query.

**[General consensus on Docker/Linux (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mijpgx/general_consensus_on_dockerlinux/)**
*   **Summary:** This thread is about the general consensus on Docker/Linux.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Docker on Windows is inefficient with CPU overhead.

**[Looking for a reliable way to extract structured data from messy PDFs ? (Score: 0)](https://v.redd.it/kkstvllws7hf1)**
*   **Summary:**  The thread asks about a reliable way to extract structured data from messy PDFs. A commenter suspects that the post is a bot ad.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The post might be a bot advertisement.

**[Ask in English, get the SQL—built a generator and would love your thoughts (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mi6u1u/ask_in_english_get_the_sqlbuilt_a_generator_and/)**
*   **Summary:** This thread discusses a tool that translates English queries into SQL. Users raised concerns about security, the necessity of such a tool, and its competition with existing tools like ChatGPT and Langchain.
*   **Emotion:** The emotional tone is predominantly Neutral, but there is a considerable amount of Negative sentiment.
*   **Top 3 Points of View:**
    *   The tool poses potential security risks due to the need for a live database connection.
    *   The tool is unnecessary because existing tools like ChatGPT and Langchain can achieve similar results.
    *   Verifying the correctness of the generated SQL is the most time-consuming part of the process, not writing the query itself.

**[Are there any sites specific for data engineers looking for some contract work? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mi7lwa/are_there_any_sites_specific_for_data_engineers/)**
*   **Summary:** The thread asks about sites specific for data engineers looking for contract work.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *  A bot posted a link to the dataengineering.wiki learning resources page.

**[New tool in data world (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mi9rym/new_tool_in_data_world/)**
*   **Summary:** The thread discusses Alteryx. Some consider it a decent ETL platform, while others consider it *** and from the early 2000s.
*   **Emotion:** The overall emotional tone is Neutral, with a slight positivity regarding the tool being decent.
*   **Top 3 Points of View:**
    *   Alteryx is an ETL platform that has been around for a while.
    *   Alteryx is considered old/outdated.
    *   Alteryx is expensive.

**[Is it possible to become an Analytics Engineer without orchestration tools experience (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mibg4c/is_it_possible_to_become_an_analytics_engineer/)**
*   **Summary:**  The thread asks if it's possible to become an Analytics Engineer without orchestration tools experience. Some users suggest it's possible and that dimensional modeling understanding is more important, while others suggest trying out orchestration tools at home.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   It's possible to become an Analytics Engineer without orchestration experience.
    *   Strong modeling skills and stakeholder communication are more valuable than orchestration knowledge.
    *   Gain orchestration experience by trying tools like Airflow at home.

**[Should I switch to DE from DS? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mih7no/should_i_switch_to_de_from_ds/)**
*   **Summary:**  This thread is about a career switch from Data Science to Data Engineering.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Switching from Data Science to Data Engineering is easier than the reverse.

