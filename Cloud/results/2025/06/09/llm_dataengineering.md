---
title: "Data Engineering Subreddit"
date: "2025-06-09"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Help with parsing a troublesome PDF format](https://i.redd.it/20vldtnguw5f1.jpeg) (Score: 24)
    *   The discussion revolves around the best ways to parse a troublesome PDF format, with suggestions including using LLMs, AWS Textract, Azure Form Intelligence, and Python libraries.
2.  Understanding DuckLake: A Table Format with a Modern Architecture (video)](https://www.youtube.com/watch?v=hrTjvvwhHEQ) (Score: 14)
    *   The discussion is about Understanding DuckLake: A Table Format with a Modern Architecture
3.  [Advice for a clueless soul](https://www.reddit.com/r/dataengineering/comments/1l6yk2v/advice_for_a_clueless_soul/) (Score: 11)
    *   The discussion focuses on providing advice for someone who needs to orchestrate scheduled pipelines, with recommendations for tools like Airflow, Prefect, and Windows Task Scheduler.
4.  [How are we helping our non-technical colleagues to edit data in the database?](https://www.reddit.com/r/dataengineering/comments/1l7at7h/how_are_we_helping_our_nontechnical_colleagues_to/) (Score: 10)
    *   The conversation explores strategies for allowing non-technical colleagues to edit data in the database, with cautions against direct write access and suggestions for using tools like Streamlit and SSIS or creating a process with guardrails.
5.  30 team healthcare company - no dedicated data engineers, need assistance on third party etl tools and cloud warehousing](https://www.reddit.com/r/dataengineering/comments/1l6y3xv/30_team_healthcare_company_no_dedicated_data/) (Score: 7)
    *   The discussion centers around a healthcare company with no dedicated data engineers seeking assistance with ETL tools and cloud warehousing, with suggestions including contracting out the work or hiring a data engineer.
6.  Apache Iceberg: how to SELECT on table "PARTITIONED BY Truncate(L, col)".](https://www.reddit.com/r/dataengineering/comments/1l6xmsr/apache_iceberg_how_to_select_on_table_partitioned/) (Score: 6)
    *   The discussion addresses how to select data on an Apache Iceberg table partitioned by a truncated column, with suggestions on how Spark and Athena handle the query and how to explicitly define the generated column name.
7.  Soda Data Quality Acquires AI Monitoring startup NannyML](https://siliconcanals.com/brussels-soda-acquires-nannyml/) (Score: 5)
    *   The discussion highlights the trend of consolidation in the VC-funded AI space, where companies either consolidate or get acquired.
8.  [Databricks+SQLMesh](https://www.reddit.com/r/dataengineering/comments/1l79z73/databrickssqlmesh/) (Score: 5)
    *   The discussion focuses on using Databricks with SQLMesh, with advice on using SQL warehouses instead of clusters with SQL, and using Databricks jobs to trigger SQL via SQL warehouses.
9.  [Is it premature to job hunt?](https://www.reddit.com/r/dataengineering/comments/1l6stze/is_it_premature_to_job_hunt/) (Score: 4)
    *   The advice given to someone who is asking "Is it premature to job hunt?" includes following a professional resume format, ensuring links are functional, adding titles, and cautioning against a specific company (Reventure).
10. [Future German Job Market ?](https://www.reddit.com/r/dataengineering/comments/1l70ccg/future_german_job_market/) (Score: 4)
    *   The discussion revolves around the future job market for Data Engineers in Germany, with varied opinions on whether it will improve or become oversaturated, and advice to focus on specific skills and consider internships.
11. [Behind every clean dataset is a data engineer turning chaos into order! 🛠️](https://i.redd.it/nzl56zh8ev5f1.png) (Score: 0)
    *   The discussion revolves around the meme and suggests the user is using the meme incorrectly.
12. [How to learn vertexAI and bqml?](https://www.reddit.com/r/dataengineering/comments/1l7037q/how_to_learn_vertexai_and_bqml/) (Score: 0)
    *   The discussion revolves around the best way to learn vertexAI and bqml with community suggestions.
13. [Best tool to load data from azure sql to GCP - transactional db with star schema](https://www.reddit.com/r/dataengineering/comments/1l7bhym/best_tool_to_load_data_from_azure_sql_to_gcp/) (Score: 0)
    *   The discussion involves the best tool to load data from azure sql to GCP with Cloud Functions for extraction, BigQuery and dbt for transformations, and Composer for orchestration and the use of CDC.
14. [How do I safely update my feature branch with the latest changes from development?](https://www.reddit.com/r/dataengineering/comments/1l7cjul/how_do_i_safely_update_my_feature_branch_with_the/) (Score: 0)
    *   The discussion explains how to safely update the user's feature branch with the latest changes from development.

# Detailed Analysis by Thread
**[Help with parsing a troublesome PDF format (Score: 24)](https://i.redd.it/20vldtnguw5f1.jpeg)**
*   **Summary:** The discussion revolves around the best ways to parse a troublesome PDF format, with various suggestions and approaches offered.
*   **Emotion:** The overall emotional tone is neutral, with a mix of suggestions and advice.
*   **Top 3 Points of View:**
    *   Use LLMs for parsing the PDF, even though it might require additional offerings for perfect results.
    *   Avoid OCR and use conversion instead, leveraging Python scripting for parsing without LLM calls.
    *   Consider using AWS Textract or Azure Form Intelligence as services for managing PDF files.

**[Understanding DuckLake: A Table Format with a Modern Architecture (video) (Score: 14)](https://www.youtube.com/watch?v=hrTjvvwhHEQ)**
*   **Summary:** The discussion asks the mod if a video flair should be added to the thread.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The mods should add a "video" flair.

**[Advice for a clueless soul (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1l6yk2v/advice_for_a_clueless_soul/)**
*   **Summary:** The discussion focuses on providing advice for someone who needs to orchestrate scheduled pipelines.
*   **Emotion:** The overall emotional tone is neutral, with a focus on providing helpful suggestions. The negative sentiment relates to Alteryx.
*   **Top 3 Points of View:**
    *   Airflow is the industry standard for orchestrating scheduled pipelines, and can be set up with Docker Compose.
    *   Consider using Airflow or Prefect 3 for the orchestration task.
    *   It's often easier to set up cloud services privately than to get a company to do it, with a suggestion to log script activities and use Windows Scheduler initially.

**[How are we helping our non-technical colleagues to edit data in the database? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1l7at7h/how_are_we_helping_our_nontechnical_colleagues_to/)**
*   **Summary:** The conversation explores strategies for allowing non-technical colleagues to edit data in the database, with a common theme of caution.
*   **Emotion:** The emotional tone is mixed, with neutral suggestions and negative sentiment against giving direct database write access.
*   **Top 3 Points of View:**
    *   Do not give non-technical colleagues direct write access to the database; create a process with guardrails.
    *   Consider using Streamlit in Snowflake, but acknowledge the potential challenges of managing an app development project.
    *   Edit data at the source system, ensuring pipelines work correctly with quality checks, and consider using the data editor component of Streamlit if needed.

**[30 team healthcare company - no dedicated data engineers, need assistance on third party etl tools and cloud warehousing (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1l6y3xv/30_team_healthcare_company_no_dedicated_data/)**
*   **Summary:** The discussion centers around a healthcare company with no dedicated data engineers seeking assistance with ETL tools and cloud warehousing.
*   **Emotion:** The overall emotional tone is positive, with a focus on providing solutions.
*   **Top 3 Points of View:**
    *   Contracting out the work is a good option to avoid potential failures from incorrect implementation.
    *   It's essential to determine the amount and cleanliness of data before recommending solutions.
    *   Consider owning your own data warehouse and using tools like Hevo with plug-and-play connectors.

**[Apache Iceberg: how to SELECT on table "PARTITIONED BY Truncate(L, col)". (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1l6xmsr/apache_iceberg_how_to_select_on_table_partitioned/)**
*   **Summary:** The discussion addresses how to select data on an Apache Iceberg table partitioned by a truncated column.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Spark might not recognize the automatically generated column name, so use the generated column name directly in the query (e.g., `WHERE requestedtime_trunc = '2025-05-30'`).
    *   The system has to read and convert all values in the table if you ask it to run the timestamp column through an expression.
    *   Convert the timestamp to a valid date.

**[Soda Data Quality Acquires AI Monitoring startup NannyML (Score: 5)](https://siliconcanals.com/brussels-soda-acquires-nannyml/)**
*   **Summary:** The discussion highlights the trend of consolidation in the VC-funded AI space.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Consolidate or be acquired.

**[Databricks+SQLMesh (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1l79z73/databrickssqlmesh/)**
*   **Summary:** The discussion focuses on using Databricks with SQLMesh.
*   **Emotion:** The emotional tone is mixed, with mostly neutral points.
*   **Top 3 Points of View:**
    *   Join the sqlmesh slack community and ask questions.
    *   Reach out to Databricks support since the service is already paid for.
    *   Use SQL warehouses instead of clusters with SQL, and use Databricks jobs to trigger SQL via SQL warehouses.

**[Is it premature to job hunt? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1l6stze/is_it_premature_to_job_hunt/)**
*   **Summary:** The advice given to someone who is asking "Is it premature to job hunt?"
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Please follow a professional resume format and titles.
    *   All your links are dead and fail on 403 redirect.
    *   Only apply to Reventure if you want to be a modern day.

**[Future German Job Market ? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1l70ccg/future_german_job_market/)**
*   **Summary:** The discussion revolves around the future job market for Data Engineers in Germany.
*   **Emotion:** The emotional tone is mixed, with neutral and negative points.
*   **Top 3 Points of View:**
    *   The job market might not improve in the next year or two, but it's still possible to find a job; internships are recommended.
    *   It's hard to predict the job market, so focus and apply for jobs.
    *   Improve German skills.

**[Behind every clean dataset is a data engineer turning chaos into order! 🛠️ (Score: 0)](https://i.redd.it/nzl56zh8ev5f1.png)**
*   **Summary:** The discussion revolves around the meme and suggests the user is using the meme incorrectly.
*   **Emotion:** The overall emotional tone is negative.
*   **Top 3 Points of View:**
    *   This is not how the meme is used.
    *   This is one of the worst abuses of this meme template I’ve ever seen.
    *   Ew no stop trying to make memes.

**[How to learn vertexAI and bqml? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1l7037q/how_to_learn_vertexai_and_bqml/)**
*   **Summary:** The discussion revolves around the best way to learn vertexAI and bqml with community suggestions.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   I don't know how cross platform they are given they're embedded GCP services but you can use cloud skillsboost and follow a machine learning engineer learning path.

**[Best tool to load data from azure sql to GCP - transactional db with star schema (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1l7bhym/best_tool_to_load_data_from_azure_sql_to_gcp/)**
*   **Summary:** The discussion involves the best tool to load data from azure sql to GCP with Cloud Functions for extraction, BigQuery and dbt for transformations, and Composer for orchestration and the use of CDC.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Beam is probably more than you need if your data is coming in batches.
    *   CDC is still a strong choice even if you’re not working with real-time data.

**[How do I safely update my feature branch with the latest changes from development? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1l7cjul/how_do_i_safely_update_my_feature_branch_with_the/)**
*   **Summary:** The discussion explains how to safely update the user's feature branch with the latest changes from development.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Ensure you’re in your feature branch with git checkout feature/streaming-pipelines, and then do git fetch origin/development to update your local tracking branches, followed by git merge origin/development to merge the remote changes into your feature branch.
    *   You should just be able to merge development to your feature branch.
    *   I would always recommend performing a rebase instead of merging.
