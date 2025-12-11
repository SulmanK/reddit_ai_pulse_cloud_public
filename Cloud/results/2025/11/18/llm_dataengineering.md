---
title: "Data Engineering Subreddit"
date: "2025-11-18"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ETL", "data pipelines"]
---

# Overall Ranking and Top Discussions
1.  [Data engineers: which workflows do you wish were event‑driven instead of batch?](https://www.reddit.com/r/dataengineering/comments/1ozu1qq/data_engineers_which_workflows_do_you_wish_were/) (Score: 20)
    *  The thread discusses which data engineering workflows would benefit from being event-driven instead of batch-oriented, with users sharing their experiences and perspectives on the advantages and disadvantages of each approach.

2.  [ETL Dev -> Data Engineer](https://www.reddit.com/r/dataengineering/comments/1p09bna/etl_dev_data_engineer/) (Score: 11)
    *  The discussion centers around the transition from an ETL Developer role to a Data Engineer role, with advice on skills to acquire and technologies to learn.

3.  [Data Engineering Discord](https://www.reddit.com/r/dataengineering/comments/1p070pl/data_engineering_discord/) (Score: 11)
    *  The thread provides a list of community-submitted learning resources.

4.  [How are you managing SQL inside Python](https://www.reddit.com/r/dataengineering/comments/1p0cz7o/how_are_you_managing_sql_inside_python/) (Score: 7)
    *  The conversation explores different methods of managing SQL queries within Python code, including the use of external files, multi-line strings, and templating engines.

5.  [Devs create tangible products, systems, websites, and apps that people can really use. I’m starting to think I’d like to transition into that kind of role.](https://www.reddit.com/r/dataengineering/comments/1p0ifcv/devs_create_tangible_products_systems_websites/) (Score: 5)
    *  The thread is about a data engineer considering a transition to a more traditional software development role, driven by a desire to create tangible products.

6.  [Are there any benefits of duplicating data?](https://www.reddit.com/r/dataengineering/comments/1p05nq4/are_there_any_benefits_of_duplicating_data/) (Score: 5)
    *  The discussion revolves around the benefits and drawbacks of duplicating data, with a focus on maintaining a single source of truth and using caching or CDC for read models.

7.  [How to automate the daily import of TXT files into SQL Server?](https://www.reddit.com/r/dataengineering/comments/1p06xol/how_to_automate_the_daily_import_of_txt_files/) (Score: 5)
    *  The thread discusses ways to automate the process of importing TXT files into SQL Server, including using Python scripts, SSIS packages, and SQL Server Agent.

8.  [Near realtime fraud detection system](https://www.reddit.com/r/dataengineering/comments/1p01h3l/near_realtime_fraud_detection_system/) (Score: 4)
    *  The thread discusses approaches and technologies for building a near real-time fraud detection system.

9.  [Evaluating real-time analytics solutions for streaming data](https://www.reddit.com/r/dataengineering/comments/1p0j209/evaluating_realtime_analytics_solutions_for/) (Score: 3)
    *  The thread is focused on evaluating different real-time analytics solutions for processing streaming data.

10. [Should I leave my job now or leave after completing 5 yrs?](https://www.reddit.com/r/dataengineering/comments/1p07k85/should_i_leave_my_job_now_or_leave_after/) (Score: 3)
    *  The discussion is centered around whether someone should leave their current job before or after reaching 5 years of employment, considering factors like gratuity and the current job market.

11. [Joe Reis - How to Sell Data Modeling](https://practicaldatamodeling.substack.com/p/how-to-sell-data-modeling) (Score: 2)
    * The discussion is centered around Joe Reis' substack post about how to sell data modeling and that it improves developer velocity, downstream ramp up, findability, and data trust.

12. [Bets way to ingest MSSQL data into Azure databricks](https://www.reddit.com/r/dataengineering/comments/1p0dejw/bets_way_to_ingest_mssql_data_into_azure/) (Score: 2)
    *  The conversation revolves around the best methods for ingesting data from MSSQL into Azure Databricks, with a focus on efficiency and minimizing overhead.

13. [Data Dependency](https://www.reddit.com/r/dataengineering/comments/1oztsoh/data_dependency/) (Score: 2)
    *  The thread explores how to manage data dependencies in data pipelines, particularly ensuring data freshness when joining data from different sources.

14. [Tips to reduce environmental impact](https://www.reddit.com/r/dataengineering/comments/1ozyj4s/tips_to_reduce_environmental_impact/) (Score: 1)
    *  The conversation focuses on tips for reducing the environmental impact of data engineering practices, such as optimizing cloud costs and using efficient technologies.

15. [An AI Agent that Builds a Data Warehouse End-to-End](https://www.reddit.com/r/dataengineering/comments/1p0dnv3/an_ai_agent_that_builds_a_data_warehouse_endtoend/) (Score: 0)
    *  This thread is centered around building a data warehouse end-to-end, using an AI Agent.

# Detailed Analysis by Thread
**[Data engineers: which workflows do you wish were event‑driven instead of batch? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1ozu1qq/data_engineers_which_workflows_do_you_wish_were/)**
*  **Summary:**  The thread discusses which data engineering workflows would benefit from being event-driven instead of batch-oriented, with users sharing their experiences and perspectives on the advantages and disadvantages of each approach.
*  **Emotion:** The emotional tone of the thread is neutral, with users providing objective insights and technical advice.
*  **Top 3 Points of View:**
    *   Some users wish for event-driven systems to manage file drops from remote SFTP servers, as it is more efficient than batch jobs checking for new files.
    *   Some users state that "Batch" and "Event Driven" pipelines are two different facets of pipelines. The alternative to a cron scheduler is a pub/sub architecture with events and rules on an aws event bus.
    *   Some users believe that event-driven analytics is a rare use case, and event-driven assumes that you are not batch processing your data.

**[ETL Dev -> Data Engineer (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1p09bna/etl_dev_data_engineer/)**
*  **Summary:**  The discussion centers around the transition from an ETL Developer role to a Data Engineer role, with advice on skills to acquire and technologies to learn.
*  **Emotion:** The overall emotional tone is positive, with users offering encouragement and helpful guidance.
*  **Top 3 Points of View:**
    *   Focus on learning data modeling.
    *   Learn distributed storage and compute, such as Snowflake and Databricks.
    *   Your biggest strength is SQL.

**[Data Engineering Discord (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1p070pl/data_engineering_discord/)**
*  **Summary:**  The thread provides a list of community-submitted learning resources.
*  **Emotion:** The emotional tone of the thread is neutral, with users providing objective insights and technical advice.
*  **Top 3 Points of View:**
    *   Find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources
    *   Remember a community called DataTalks Club.
    *   N/A

**[How are you managing SQL inside Python (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1p0cz7o/how_are_you_managing_sql_inside_python/)**
*  **Summary:**  The conversation explores different methods of managing SQL queries within Python code, including the use of external files, multi-line strings, and templating engines.
*  **Emotion:** The emotional tone of the thread is neutral, with users sharing their preferred methods and offering practical advice. There's a slight negative sentiment expressed toward multi-line strings.
*  **Top 3 Points of View:**
    *   Use SQL files in external files, loading the file and then running inline. Multi line strings are considered the worst.
    *   Use interpolated strings.
    *   Use jinja2 templates as SQL files for airflow/large queries.

**[Devs create tangible products, systems, websites, and apps that people can really use. I’m starting to think I’d like to transition into that kind of role. (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p0ifcv/devs_create_tangible_products_systems_websites/)**
*  **Summary:**  The thread is about a data engineer considering a transition to a more traditional software development role, driven by a desire to create tangible products.
*  **Emotion:** The emotional tone is mixed, with some users being sympathetic to the desire for more tangible results, while others highlight the value and impact of data engineering work.
*  **Top 3 Points of View:**
    *   Some users believe data engineering can be thankless, but it's generally seen as necessary.
    *   Some users who transitioned into building data intensive applications felt more rewarded.
    *   Some users enjoy the relationship with the people who consume the data they steward.

**[Are there any benefits of duplicating data? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p05nq4/are_there_any_benefits_of_duplicating_data/)**
*  **Summary:**  The discussion revolves around the benefits and drawbacks of duplicating data, with a focus on maintaining a single source of truth and using caching or CDC for read models.
*  **Emotion:** The emotional tone is neutral, with a focus on providing technical advice and best practices.
*  **Top 3 Points of View:**
    *   Keep the Django API as the source of truth and only duplicate as a cache or CDC-backed read model.
    *   A change in schema should take 30 minutes, not 2 weeks, even if the DB has a built-in transformation feature.
    *   Custom data structures are slower and worse than the ones built in.

**[How to automate the daily import of TXT files into SQL Server? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p06xol/how_to_automate_the_daily_import_of_txt_files/)**
*  **Summary:**  The thread discusses ways to automate the process of importing TXT files into SQL Server, including using Python scripts, SSIS packages, and SQL Server Agent.
*  **Emotion:** The emotional tone is mostly neutral, with some users expressing frustration at the question if a working solution already exists.
*  **Top 3 Points of View:**
    *   Stick with the existing Python script and use a scheduler to trigger it.
    *   Use SSIS plus SQL Server Agent for long-term reliability.
    *   SSIS is the best tool for the job.

**[Near realtime fraud detection system (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p01h3l/near_realtime_fraud_detection_system/)**
*  **Summary:**  The thread discusses approaches and technologies for building a near real-time fraud detection system.
*  **Emotion:** The emotional tone is neutral, with users providing technical recommendations.
*  **Top 3 Points of View:**
    *   Flink is the best solution for near-real-time data analysis.
    *   Spark and TImeplus/Proton are also good options.
    *   Deploy a model on a Google end point.

**[Evaluating real-time analytics solutions for streaming data (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p0j209/evaluating_realtime_analytics_solutions_for/)**
*  **Summary:**  The thread is focused on evaluating different real-time analytics solutions for processing streaming data.
*  **Emotion:** The emotional tone is neutral, with users offering technical suggestions based on their experience.
*  **Top 3 Points of View:**
    *   ClickHouse can easily handle the scale.
    *   Pinot is a bit more complex to manage.
    *   Use postgres notifications unless you expect this scale to continue indefinitely.

**[Should I leave my job now or leave after completing 5 yrs? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p07k85/should_i_leave_my_job_now_or_leave_after/)**
*  **Summary:**  The discussion is centered around whether someone should leave their current job before or after reaching 5 years of employment, considering factors like gratuity and the current job market.
*  **Emotion:** The emotional tone is negative, with users expressing concern about the current job market.
*  **Top 3 Points of View:**
    *   Do not quit unless you have a job lined up.
    *   The tech market has been *** for 2 years and is getting worse by the minute.
    *   Before quitting, calculate the amount of the gratuity.

**[Joe Reis - How to Sell Data Modeling (Score: 2)](https://practicaldatamodeling.substack.com/p/how-to-sell-data-modeling)**
*   **Summary:** The discussion is centered around Joe Reis' substack post about how to sell data modeling and that it improves developer velocity, downstream ramp up, findability, and data trust.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Just say it improves developer velocity, downstream ramp up, findability, and data trust.

**[Bets way to ingest MSSQL data into Azure databricks (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p0dejw/bets_way_to_ingest_mssql_data_into_azure/)**
*  **Summary:**  The conversation revolves around the best methods for ingesting data from MSSQL into Azure Databricks, with a focus on efficiency and minimizing overhead.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   In vendor-based software (like an ERP) use API first, direct query second.
    *   Put it all in the same domain, open up the appropriate port, and simply do SELECT ... INTO staging_layer ... FROM servername.dbname.schemaname.tablename, this uses Linked Server.
    *   Load to csv and send to Databricks, but it's quite slow

**[Data Dependency (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oztsoh/data_dependency/)**
*  **Summary:**  The thread explores how to manage data dependencies in data pipelines, particularly ensuring data freshness when joining data from different sources.
*  **Emotion:** The emotional tone is positive and neutral, with users sharing solutions.
*  **Top 3 Points of View:**
    *   Airflow or other orchestrators have the ability to use sensors to check if partitions of tables exist in warehouses or if new files have been uploaded to s3/sftp.
    *   ETL is wrong as a concept. ELT is what works.
    *   Glue + AWS Step Functions tech stack

**[Tips to reduce environmental impact (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ozyj4s/tips_to_reduce_environmental_impact/)**
*  **Summary:**  The conversation focuses on tips for reducing the environmental impact of data engineering practices, such as optimizing cloud costs and using efficient technologies.
*  **Emotion:** The emotional tone is neutral to positive.
*  **Top 3 Points of View:**
    *   Keep an eye on how much your cloud costs. Lower cloud bills mean less electricity and resources used.
    *   You’re a negligible amount of the issue. Don’t worry about it.
    *   Shift daily compute jobs that can be a little flexible to a time when the energy is likely renewable in your local data centre.

**[An AI Agent that Builds a Data Warehouse End-to-End (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p0dnv3/an_ai_agent_that_builds_a_data_warehouse_endtoend/)**
*   **Summary:** This thread is centered around building a data warehouse end-to-end, using an AI Agent.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   GitHub link or it didnt happen.
    *   ROFL
    *   N/A
