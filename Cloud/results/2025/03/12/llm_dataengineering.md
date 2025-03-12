---
title: "Data Engineering Subreddit"
date: "2025-03-12"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [SQL Premier League : SQL Meets Sports](https://i.redd.it/3ghvwtl2y8oe1.png) (Score: 124)
    *   The creator built a website where users can learn and practice SQL by querying real-world sports data. They are looking for sponsors to cover server costs and further development.
2.  [Optimizing PySpark Performance: Key Best Practices](https://www.reddit.com/r/dataengineering/comments/1j9hqfy/optimizing_pyspark_performance_key_best_practices/) (Score: 80)
    *   A discussion on best practices for optimizing PySpark performance, including the use of SSDs for temporary storage, DataFrame usage, schema inference, and handling data skew.
3.  [DuckDB released a local UI](https://duckdb.org/2025/03/12/duckdb-ui.html) (Score: 72)
    *   Users are discussing the newly released local UI for DuckDB, with some expressing excitement and interest.
4.  [The Current Data Stack is Too Complex: 70% Data Leaders & Practitioners Agree](https://moderndata101.substack.com/p/the-current-data-stack-is-too-complex) (Score: 56)
    *   A discussion about the complexity of the current data stack, with some arguing it stems from reliance on tools over foundational expertise, while others point out the inherent complexity of the problem domain.
5.  [AWS Data Engineer trying to learn Azure](https://www.reddit.com/r/dataengineering/comments/1j9iabm/aws_data_engineer_trying_to_learn_azure/) (Score: 10)
    *   An AWS data engineer is looking for advice on learning Azure, with recommendations to start with Databricks and be aware of the upcoming Fabric DE certification.
6.  [Is salting almost useless in Spark?](https://www.reddit.com/r/dataengineering/comments/1j9k9tf/is_salting_almost_useless_in_spark/) (Score: 9)
    *   The thread discusses the usefulness of salting in Spark for handling data skew, with conflicting opinions on whether it helps or breaks joins.
7.  [Should I move our data pipelines toward Cloud native(AWS) or keep it more under control?](https://www.reddit.com/r/dataengineering/comments/1j9hauh/should_i_move_our_data_pipelines_toward_cloud/) (Score: 8)
    *   The poster is trying to decide if they should move data pipelines to the cloud or keep them under control.
8.  [What is the best way to build a data warehouse for small accounting & digital marketing businesses? Should I do an on-premises data warehouse &/ or use cloud platforms?](https://www.reddit.com/r/dataengineering/comments/1j9lyg8/what_is_the_best_way_to_build_a_data_warehouse/) (Score: 4)
    *   Discussion on the best approach to building a data warehouse for small businesses, with opinions favoring cloud solutions like BigQuery and Postgres due to lower maintenance and cost.
9.  [Website as a data delivery tool](https://www.reddit.com/r/dataengineering/comments/1j9srtw/website_as_a_data_delivery_tool/) (Score: 3)
    *   A discussion on using a website as a data delivery tool, weighing its advantages for non-technical users against alternatives like SharePoint and APIs.
10. [ZipNN - Lossless compression for AI Models/ Embedings/ KV-cache](https://www.reddit.com/r/dataengineering/comments/1j9hzht/zipnn_lossless_compression_for_ai_models/) (Score: 2)
    *   The thread provides a link to community-submitted learning resources.
11. [Data Analyst w Snowflake/Databricks Access](https://www.reddit.com/r/dataengineering/comments/1j9rbux/data_analyst_w_snowflakedatabricks_access/) (Score: 2)
    *   The thread provides advise to Data Analysts to learn SQL
12. [Is EDW + Data Marts scalable?](https://www.reddit.com/r/dataengineering/comments/1j9linb/is_edw_data_marts_scalable/) (Score: 1)
    *   A question on whether EDW (Enterprise Data Warehouse) + Data Marts is scalable
13. [Reading unstructured text file into delta table using spark](https://www.reddit.com/r/dataengineering/comments/1j9mi9k/reading_unstructured_text_file_into_delta_table/) (Score: 1)
    *   Help on reading an unstructured text file into delta table using spark
14. [I'm a Data Rookie](https://www.reddit.com/r/dataengineering/comments/1j9rhoi/im_a_data_rookie/) (Score: 0)
    *   An introductory post by a "Data Rookie"

# Detailed Analysis by Thread
**[SQL Premier League : SQL Meets Sports (Score: 124)](https://i.redd.it/3ghvwtl2y8oe1.png)**
*  **Summary:** A user created a website for learning SQL through real-world sports data and seeks feedback and sponsorship for server costs.
*  **Emotion:** The overall emotional tone is positive. Users express enthusiasm and appreciation for the website.
*  **Top 3 Points of View:**
    *   The website is a fantastic idea and a great way to learn SQL.
    *   The creator needs sponsorship for server costs to keep the site running.
    *   Some users have encountered technical issues like incorrect table query errors or SSL connection problems.

**[Optimizing PySpark Performance: Key Best Practices (Score: 80)](https://www.reddit.com/r/dataengineering/comments/1j9hqfy/optimizing_pyspark_performance_key_best_practices/)**
*  **Summary:** This is a discussion on optimizing PySpark performance. Topics include using SSD disks, the efficiency of DataFrames, issues with inferring schema, transforming columns with `select()`, and handling data skew in joins.
*  **Emotion:** The emotional tone is neutral, with a focus on technical correctness and clarification.
*  **Top 3 Points of View:**
    *   Attaching multiple SSD disks for temporary storage can significantly improve Spark performance.
    *   Using `inferSchema=True` is not recommended for production pipelines because it increases load times due to double processing the data.
    *   Salting may or may not resolve skews in joins by adding a randomized salt to a join condition, because then it will break the join.

**[DuckDB released a local UI (Score: 72)](https://duckdb.org/2025/03/12/duckdb-ui.html)**
*  **Summary:** Users react to the release of a local UI for DuckDB, with comments ranging from inquiries about the client code to expressions of excitement.
*  **Emotion:** The overall emotional tone is positive and curious.
*  **Top 3 Points of View:**
    *   Some users are impressed and "wowing" by the UI.
    *   Some users believe that it seems ridiculously cool
    *   Some users are curious about the location of the client code.

**[The Current Data Stack is Too Complex: 70% Data Leaders & Practitioners Agree (Score: 56)](https://moderndata101.substack.com/p/the-current-data-stack-is-too-complex)**
*  **Summary:** Users are discussing an article that highlights the complexity of the current data stack, with many agreeing that it is a significant issue.
*  **Emotion:** The overall emotional tone is neutral and contemplative, with a hint of skepticism.
*  **Top 3 Points of View:**
    *   Complexity arises from relying on tools instead of foundational expertise and analysis.
    *   The underlying problem domain and requirements are inherently complex.
    *   The claim that 70% of data leaders agree the stack is too complex may be misleading, as it's based on time spent coordinating tools, not necessarily an opinion on overall complexity.

**[AWS Data Engineer trying to learn Azure (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1j9iabm/aws_data_engineer_trying_to_learn_azure/)**
*  **Summary:** An AWS data engineer is seeking advice on learning Azure, with a suggestion to start with Databricks and information about the upcoming Fabric DE certification.
*  **Emotion:** The overall emotional tone is neutral and helpful.
*  **Top 3 Points of View:**
    *   Start with Databricks as Microsoft is transitioning to Fabric.
    *   The Azure DE certification is being retired and replaced with the Fabric DE cert.
    *   Community-submitted learning resources can be found at a provided link.

**[Is salting almost useless in Spark? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1j9k9tf/is_salting_almost_useless_in_spark/)**
*  **Summary:** This thread questions the usefulness of salting in Spark for addressing data skew.
*  **Emotion:** The overall emotional tone is neutral and inquisitive.
*  **Top 3 Points of View:**
    *   Salting helps with skew by spreading a highly repeated value across many executors.
    *   Adding a salt to the equijoin key breaks the join because it prevents the co-location of data with the same join values.
    *   By default Spark’s partitioning behavior is to hash the join condition, mod that to the number of partitions.

**[Should I move our data pipelines toward Cloud native(AWS) or keep it more under control? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1j9hauh/should_i_move_our_data_pipelines_toward_cloud/)**
*  **Summary:** The poster is trying to decide if they should move data pipelines to the cloud or keep them under control.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The cloud native solution is the most future proof architecture.
    *   Cloud native vs....? All your solutions are cloud based.
    *   The most future proof architecture is the one that doesn't raise billing flags with finance.

**[What is the best way to build a data warehouse for small accounting & digital marketing businesses? Should I do an on-premises data warehouse &/ or use cloud platforms? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1j9lyg8/what_is_the_best_way_to_build_a_data_warehouse/)**
*  **Summary:** The thread discusses the best way to build a data warehouse for small businesses.
*  **Emotion:** The overall emotional tone is neutral and helpful.
*  **Top 3 Points of View:**
    *   For small businesses, go with cloud as on-prem needs hardware investment + maintenance. AWS/GCP free tiers are decent to start.
    *   BigQuery is the best bet, nearly zero technical work to set up and maintain and it costs nothing until your usage gets pretty heavy.
    *   Simon Sinek has a good philosophy that translates to DW projects. Start with WHY, then WHAT, then HOW.

**[Website as a data delivery tool (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1j9srtw/website_as_a_data_delivery_tool/)**
*  **Summary:** A discussion on the pros and cons of using a website as a tool for delivering data, especially to non-technical users.
*  **Emotion:** The overall emotional tone is neutral and informative.
*  **Top 3 Points of View:**
    *   A website is accessible anywhere and easy to use for non-technical users.
    *   CSV export from the web is a common practice.
    *   Consider using a SharePoint site as an alternative to creating a custom website.

**[ZipNN - Lossless compression for AI Models/ Embedings/ KV-cache (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j9hzht/zipnn_lossless_compression_for_ai_models/)**
*  **Summary:** The thread provides a link to community-submitted learning resources.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   N/A, this post is just a bot.

**[Data Analyst w Snowflake/Databricks Access (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j9rbux/data_analyst_w_snowflakedatabricks_access/)**
*  **Summary:** The thread provides advise to Data Analysts to learn SQL
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   As an analyst, you should learn some basic SQL and recreate some basic report from the database.

**[Is EDW + Data Marts scalable? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1j9linb/is_edw_data_marts_scalable/)**
*  **Summary:** A question on whether EDW (Enterprise Data Warehouse) + Data Marts is scalable
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Kimball's design recipes are very much alive and scalable.

**[Reading unstructured text file into delta table using spark (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1j9mi9k/reading_unstructured_text_file_into_delta_table/)**
*  **Summary:** Help on reading an unstructured text file into delta table using spark
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   You can read it in dataframe and it has options for multiline character and setting your delimiter

**[I'm a Data Rookie (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1j9rhoi/im_a_data_rookie/)**
*  **Summary:** An introductory post by a "Data Rookie"
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   N/A
