---
title: "Data Engineering Subreddit"
date: "2025-10-12"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Am I the only one who spends half their life fixing the same *** dataset every month?](https://www.reddit.com/r/dataengineering/comments/1o4f1x3/am_i_the_only_one_who_spends_half_their_life/) (Score: 80)
    * The post is about the frustration of spending a significant amount of time fixing the same dataset every month.
2.  [Week 3 of learning Pyspark](https://i.redd.it/4bdfi16eymuf1.jpeg) (Score: 58)
    * The post shows a learning resource for Pyspark and prompts discussion about learning resources and their effectiveness for data analysts.
3.  [When to normalize vs denormalize in database design?](https://www.reddit.com/r/dataengineering/comments/1o4clus/when_to_normalize_vs_denormalize_in_database/) (Score: 46)
    * The discussion revolves around the best practices for database normalization and denormalization, and when each approach is most appropriate.
4.  [Data clutter in SCD Type 2](https://www.reddit.com/r/dataengineering/comments/1o467qd/data_clutter_in_scd_type_2/) (Score: 19)
    * The discussion is about data clutter in Slowly Changing Dimension Type 2 tables, and the pros and cons of including end dates or current flags.
5.  [How do I actually "sell" data engineering/analytics?](https://www.reddit.com/r/dataengineering/comments/1o4kfc6/how_do_i_actually_sell_data_engineeringanalytics/) (Score: 13)
    * The discussion focuses on strategies for selling data engineering and analytics services, particularly to smaller businesses with limited budgets.
6.  [Fivetran pricing for small data](https://www.reddit.com/r/dataengineering/comments/1o4l57x/fivetran_pricing_for_small_data/) (Score: 13)
    * The discussion is about understanding Fivetran's pricing model for small data volumes and exploring alternative ETL tools for budget-conscious users.
7.  [How common is it to store historical snapshots of data?](https://www.reddit.com/r/dataengineering/comments/1o4sjaa/how_common_is_it_to_store_historical_snapshots_of/) (Score: 7)
    * The post inquires about the commonality and benefits of storing historical data snapshots, particularly within a data engineering context.
8.  [a lot of small files problem](https://www.reddit.com/r/dataengineering/comments/1o4mpyy/a_lot_of_small_files_problem/) (Score: 6)
    * The discussion centers around strategies for handling numerous small files, particularly focusing on compression techniques and tools like Dataflow and DuckDB.
9.  [What Editor Do You Use?](https://www.reddit.com/r/dataengineering/comments/1o4rf13/what_editor_do_you_use/) (Score: 5)
    * The discussion revolves around the preferred code editors used by data engineers, with mentions of VS Code, Vim, Sublime, and Emacs.
10. [Career path advice](https://www.reddit.com/r/dataengineering/comments/1o4678u/career_path_advice/) (Score: 4)
    * This post is automatically answered by a bot with a link to learning resources.
11. [Data Engineering Crash Course Style Videos?](https://www.reddit.com/r/dataengineering/comments/1o4g92c/data_engineering_crash_course_style_videos/) (Score: 4)
    * The discussion involves sharing YouTube channels that offer data engineering crash course style videos.
12. [Using Airflow XCom from a separate file](https://www.reddit.com/r/dataengineering/comments/1o4gb9p/using_airflow_xcom_from_a_separate_file/) (Score: 3)
    * The discussion revolves around how to use Airflow XCom from a separate file.
13. [Good Hive Metastore Image for Trino + Iceberg](https://www.reddit.com/r/dataengineering/comments/1o45jkl/good_hive_metastore_image_for_trino_iceberg/) (Score: 2)
    * The discussion involves sharing suggestions for a good Hive Metastore image for Trino + Iceberg.
14. [how to go from python scripting to working in a team](https://www.reddit.com/r/dataengineering/comments/1o4pdow/how_to_go_from_python_scripting_to_working_in_a/) (Score: 2)
    * The discussion centers around transitioning from individual Python scripting to collaborative work in a data engineering team, focusing on essential skills and practices.
15. [Did I make a mistake chasing the money instead of the tech stack?](https://www.reddit.com/r/dataengineering/comments/1o4z0vv/did_i_make_a_mistake_chasing_the_money_instead_of/) (Score: 1)
    * This post questions whether chasing a higher salary was a mistake, as opposed to focusing on a desired tech stack.

# Detailed Analysis by Thread
**[Am I the only one who spends half their life fixing the same *** dataset every month? (Score: 80)](https://www.reddit.com/r/dataengineering/comments/1o4f1x3/am_i_the_only_one_who_spends_half_their_life/)**
*  **Summary:**  The post is about the frustration of spending a significant amount of time fixing the same dataset every month.
*  **Emotion:** The emotional tone of the thread is predominantly Neutral, with various comments expressing shared frustrations and offering potential solutions. One comment does convey a slightly Negative sentiment, expressing frustration with vendors.
*  **Top 3 Points of View:**
    * Setting up a data contract with data providers can help version changes.
    * Implementing a zero-trust approach by identifying errors and adding tests can hold upstream sources accountable.
    * Developing a generic framework to fix data issues and delegating the task of cleaning data to someone other than a data engineer.

**[Week 3 of learning Pyspark (Score: 58)](https://i.redd.it/4bdfi16eymuf1.jpeg)**
*  **Summary:** The post shows a learning resource for Pyspark and prompts discussion about learning resources and their effectiveness for data analysts.
*  **Emotion:** The emotional tone is predominantly Neutral, with one comment showing a Positive sentiment.
*  **Top 3 Points of View:**
    * Asking where someone has learnt SPARK from.
    * Does completing this playlist equal most of the knowledge from pyspark perspective?
    * Questioning why ztm and not Udemy?

**[When to normalize vs denormalize in database design? (Score: 46)](https://www.reddit.com/r/dataengineering/comments/1o4clus/when_to_normalize_vs_denormalize_in_database/)**
*  **Summary:**  The discussion revolves around the best practices for database normalization and denormalization, and when each approach is most appropriate.
*  **Emotion:** The emotional tone is predominantly Neutral, with one comment showing a Negative sentiment.
*  **Top 3 Points of View:**
    * Normalize for OLTP to reduce redundancy, and denormalize for reporting performance.
    * Normalize until it hurts, then denormalize until it works.
    * Normalize for efficient writes/reads in production, and denormalize for easy reads in analysis.

**[Data clutter in SCD Type 2 (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1o467qd/data_clutter_in_scd_type_2/)**
*  **Summary:**  The discussion is about data clutter in Slowly Changing Dimension Type 2 tables, and the pros and cons of including end dates or current flags.
*  **Emotion:** The overall emotional tone is Positive and Neutral.
*  **Top 3 Points of View:**
    *  Having start and end times match is useful and also means you can get following/preceding rows with joins rather than window lead/lag functions, which can be nice.
    * End user queries work much harder (and use more resources) to join fact rows to the correct versions of the dimension without proper management.
    * Storage is way cheaper than compute.

**[How do I actually "sell" data engineering/analytics? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1o4kfc6/how_do_i_actually_sell_data_engineeringanalytics/)**
*  **Summary:**  The discussion focuses on strategies for selling data engineering and analytics services, particularly to smaller businesses with limited budgets.
*  **Emotion:** The emotional tone is generally Positive and Neutral.
*  **Top 3 Points of View:**
    * Those selling data engineering as a consultant should make sure they have the experience to know what they're doing.
    * Recommend learning power bi, since it is just google sheets then power query will be more than enough.
    * Google Colab allows for automated notebooks to run on a schedule.

**[Fivetran pricing for small data (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1o4l57x/fivetran_pricing_for_small_data/)**
*  **Summary:**  The discussion is about understanding Fivetran's pricing model for small data volumes and exploring alternative ETL tools for budget-conscious users.
*  **Emotion:** The emotional tone of this thread is predominantly Neutral, with some comments leaning towards Positive, particularly regarding the potential for using the free tier.
*  **Top 3 Points of View:**
    * Fivetran's pricing can be tricky and fees might creep up, consider sticking with python or explore other affordable etl tools.
    * Try dlt.
    * Fivetran squeezes people from free tier who will never go premium.

**[How common is it to store historical snapshots of data? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1o4sjaa/how_common_is_it_to_store_historical_snapshots_of/)**
*  **Summary:**  The post inquires about the commonality and benefits of storing historical data snapshots, particularly within a data engineering context.
*  **Emotion:** The overall emotional tone is Positive and Neutral.
*  **Top 3 Points of View:**
    * Data engineers need to drive the convo about historical data, and yes historical dimensional data and transactions in the Data Lake is very common, as is SCD Type 2 dimensions is your Gold layer and/or Data Warehouse.
    * Don't you have a date dimension? Sales data shouldn't change, it's transactional data not snapshot.
    * It's very common. Some people purge data after a time but probably keep some aggregated data perpetually.

**[a lot of small files problem (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1o4mpyy/a_lot_of_small_files_problem/)**
*  **Summary:**  The discussion centers around strategies for handling numerous small files, particularly focusing on compression techniques and tools like Dataflow and DuckDB.
*  **Emotion:** The overall emotional tone is Positive and Neutral.
*  **Top 3 Points of View:**
    * Dataflow
    * if the schema is defined then you can do this reliably and quickly using duckdb.
    * Snappy compression was also decent.

**[What Editor Do You Use? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1o4rf13/what_editor_do_you_use/)**
*  **Summary:**  The discussion revolves around the preferred code editors used by data engineers, with mentions of VS Code, Vim, Sublime, and Emacs.
*  **Emotion:** The overall emotional tone is Neutral with some Negative sentiment.
*  **Top 3 Points of View:**
    * VSCode with Vim bindings now because of the LLM chat integration.
    * I use Vim for non SQL workflows like Python, Go, etc.
    * Every company I’ve worked for uses VS Code.

**[Career path advice (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o4678u/career_path_advice/)**
*  **Summary:**  This post is automatically answered by a bot with a link to learning resources.
*  **Emotion:** The sentiment score and emotion are Neutral.
*  **Top 3 Points of View:**
    * N/A

**[Data Engineering Crash Course Style Videos? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o4g92c/data_engineering_crash_course_style_videos/)**
*  **Summary:**  The discussion involves sharing YouTube channels that offer data engineering crash course style videos.
*  **Emotion:** The sentiment score and emotion are Neutral.
*  **Top 3 Points of View:**
    * N/A

**[Using Airflow XCom from a separate file (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o4gb9p/using_airflow_xcom_from_a_separate_file/)**
*  **Summary:**  The discussion revolves around how to use Airflow XCom from a separate file.
*  **Emotion:** The sentiment score and emotion are Neutral.
*  **Top 3 Points of View:**
    * Those are two tasks within one DAG, so the later task can pull the xcom values from the first.

**[Good Hive Metastore Image for Trino + Iceberg (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o45jkl/good_hive_metastore_image_for_trino_iceberg/)**
*  **Summary:**  The discussion involves sharing suggestions for a good Hive Metastore image for Trino + Iceberg.
*  **Emotion:** The sentiment score and emotion are Neutral.
*  **Top 3 Points of View:**
    * N/A

**[how to go from python scripting to working in a team (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o4pdow/how_to_go_from_python_scripting_to_working_in_a/)**
*  **Summary:**  The discussion centers around transitioning from individual Python scripting to collaborative work in a data engineering team, focusing on essential skills and practices.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Consider contributing to open source projects to get a feel for team dynamics, code reviews, and collaborative coding.
    * What you did so far was scripting. What you are looking for is software development and engineering.
    * Why haven’t you done any OOP or logging?

**[Did I make a mistake chasing the money instead of the tech stack? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1o4z0vv/did_i_make_a_mistake_chasing_the_money_instead_of/)**
*  **Summary:**  This post questions whether chasing a higher salary was a mistake, as opposed to focusing on a desired tech stack.
*  **Emotion:** The sentiment score and emotion are Neutral, and Positive.
*  **Top 3 Points of View:**
    * all stacks will fade, money in your account will not.
    * It doesn't hurt, if anything at all will add a different experience. Start looking for new role while working in the current role.
