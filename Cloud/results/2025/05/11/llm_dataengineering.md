---
title: "Data Engineering Subreddit"
date: "2025-05-11"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "career", "tools"]
---

# Overall Ranking and Top Discussions
1.  [[D] Last 2 months I have been humbled by the data engineering landscape](https://www.reddit.com/r/dataengineering/comments/1kk0xxg/last_2_months_i_have_been_humbled_by_the_data/) (Score: 111)
    *   The poster expresses being overwhelmed by the current data engineering landscape. Commenters discuss the relevance of specific technologies, the routine nature of some DE jobs, and the difference between actual data engineering and what many perceive it to be.
2.  [What are your ETL data cleaning/standardisation rules?](https://www.reddit.com/r/dataengineering/comments/1kjo6uj/what_are_your_etl_data_cleaningstandardisation/) (Score: 65)
    *   Users are sharing their ETL data cleaning and standardization rules, including handling null values, validating data size, normalizing column names, and ensuring data consistency.
3.  [DBT full_refresh for Very Big Dataset in BigQuery](https://www.reddit.com/r/dataengineering/comments/1kjjo2u/dbt_full_refresh_for_very_big_dataset_in_bigquery/) (Score: 16)
    *   The discussion revolves around strategies for performing full refreshes of very large datasets in BigQuery using DBT, including manual incremental loads, pre-staging, append-only methods, and partition management.
4.  [Why is "Sort Merge Join" is preferred over "Shuffle Hash Join" in Spark?](https://www.reddit.com/r/dataengineering/comments/1kk5zup/why_is_sort_merge_join_is_preferred_over_shuffle/) (Score: 9)
    *   The thread explores the preference for Sort Merge Join over Shuffle Hash Join in Spark, particularly when dealing with large tables that may not fit in memory.
5.  [Single shot a streamlit and gradio app into existence](https://www.reddit.com/r/dataengineering/comments/1kjn1gu/single_shot_a_streamlit_and_gradio_app_into/) (Score: 6)
    *   A bot posted a link to an open-source project showcase. Another commenter thinks short-lived gradio/streamlit dashboards are a great usecase for AI.
6.  [Need help deciding- ML vs DE](https://www.reddit.com/r/dataengineering/comments/1kjx0a2/need_help_deciding_ml_vs_de/) (Score: 5)
    *   The discussion centers on choosing between a Machine Learning (ML) and Data Engineering (DE) internship. Commenters discuss the importance of the work's actual content, competition in ML, and the potential need for a Master's degree in ML.
7.  [New project advise](https://www.reddit.com/r/dataengineering/comments/1kjxa2i/new_project_advise/) (Score: 2)
    *   The thread discusses project advice, focusing on QC at source and dealing with business reluctance to make hard rules about QC.
8.  [Data governance tools](https://www.reddit.com/r/dataengineering/comments/1kjxv6l/data_governance_tools/) (Score: 2)
    *   Discussion about data governance tools, with a suggestion to look into Unity Catalog.
9.  [Need advice on freelancing](https://www.reddit.com/r/dataengineering/comments/1kk7y09/need_advice_on_freelancing/) (Score: 1)
    *   The thread discusses the challenges and opportunities in data engineering freelancing, including the importance of sales skills and the reluctance of established companies to hire freelancers.
10. [What data platform pain are you trying to solve most?](https://www.reddit.com/r/dataengineering/comments/1kjqn0b/what_data_platform_pain_are_you_trying_to_solve/) (Score: 0)
    *   The discussion centers around data platform pain points, particularly for SMBs, and the difficulty of use of existing platforms.
11. [Do People Actually Code as They Climb the Career Ladder?](https://www.reddit.com/r/dataengineering/comments/1kjuwnl/do_people_actually_code_as_they_climb_the_career/) (Score: 0)
    *   The discussion revolves around whether people code as they climb the career ladder.

# Detailed Analysis by Thread
**[[D] Last 2 months I have been humbled by the data engineering landscape (Score: 111)](https://www.reddit.com/r/dataengineering/comments/1kk0xxg/last_2_months_i_have_been_humbled_by_the_data/)**
*  **Summary:** The original poster expresses feeling overwhelmed by the data engineering landscape. Commenters discuss the rapidly changing tech stack, the routine nature of some data engineering roles, the debate of genuine DE vs SWE, and ways to keep up with the industry.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The data engineering tech stack changes rapidly, making it difficult to keep up.
    *   Some data engineering jobs are routine, despite inflated requirements.
    *   "Genuine" data engineering is a subset of software engineering.

**[What are your ETL data cleaning/standardisation rules? (Score: 65)](https://www.reddit.com/r/dataengineering/comments/1kjo6uj/what_are_your_etl_data_cleaningstandardisation/)**
*  **Summary:** Users share their ETL data cleaning and standardization rules, including handling null values, validating data size, normalizing column names, and ensuring data consistency.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Set empty strings to null, validate cell sizes, and validate not-null columns and unique keys.
    *   Snake case column names, replace null values, and add load timestamp and data source columns.
    *   Convert geospatial data to decimal degrees and validate longitude and latitude ranges.

**[DBT full_refresh for Very Big Dataset in BigQuery (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1kjjo2u/dbt_full_refresh_for_very_big_dataset_in_bigquery/)**
*  **Summary:** The discussion revolves around strategies for performing full refreshes of very large datasets in BigQuery using DBT, including manual incremental loads, pre-staging, append-only methods, and partition management.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Manual incremental loads can be used when doing full history on huge tables.
    *   Ingest historical data into a temp table as a pre-staging area, then merge into the DBT model.
    *   Incrementally load data using a small initial load script or airflow.

**[Why is "Sort Merge Join" is preferred over "Shuffle Hash Join" in Spark? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1kk5zup/why_is_sort_merge_join_is_preferred_over_shuffle/)**
*  **Summary:** The thread explores the preference for Sort Merge Join over Shuffle Hash Join in Spark, particularly when dealing with large tables that may not fit in memory.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Sort Merge Join is preferred when tables are large and don't fit into memory.
    *   Sorting makes read access more predictable.
    *   Smaller tables are preferred for hash joins.

**[Single shot a streamlit and gradio app into existence (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kjn1gu/single_shot_a_streamlit_and_gradio_app_into/)**
*  **Summary:** A bot posted a link to an open-source project showcase. Another commenter thinks short-lived gradio/streamlit dashboards are a great usecase for AI.
*  **Emotion:** The overall emotional tone is neutral with a hint of positivity.
*  **Top 3 Points of View:**
    *   Sharing of the link for open-source project showcase.
    *   Short-lived gradio/streamlit dashboards are a great usecase for AI.

**[Need help deciding- ML vs DE (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kjx0a2/need_help_deciding_ml_vs_de/)**
*  **Summary:** The discussion centers on choosing between a Machine Learning (ML) and Data Engineering (DE) internship. Commenters discuss the importance of the work's actual content, competition in ML, and the potential need for a Master's degree in ML.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   The actual work content of the internship is more important than the title.
    *   Competition in ML is intense, potentially making DE a better option for some.
    *   ML may require a Master's degree for future career advancement.

**[New project advise (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kjxa2i/new_project_advise/)**
*  **Summary:** The thread discusses project advice, focusing on QC at source and dealing with business reluctance to make hard rules about QC.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Start with focusing on QC at the source.
    *   Document everything, especially when the business is reluctant to make hard rules about QC.

**[Data governance tools (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kjxv6l/data_governance_tools/)**
*  **Summary:** Discussion about data governance tools, with a suggestion to look into Unity Catalog.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Check out Unity Catalog since it's also open sourced.

**[Need advice on freelancing (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kk7y09/need_advice_on_freelancing/)**
*  **Summary:** The thread discusses the challenges and opportunities in data engineering freelancing, including the importance of sales skills and the reluctance of established companies to hire freelancers.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Freelancing is 80% sales and 20% technical.
    *   Established companies are hesitant to bring in freelancers.
    *   Networking at tech meetups can help freelancers build connections.

**[What data platform pain are you trying to solve most? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kjqn0b/what_data_platform_pain_are_you_trying_to_solve/)**
*  **Summary:** The discussion centers around data platform pain points, particularly for SMBs, and the difficulty of use of existing platforms.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   It should become easier for SMBs to set up and have a dataplatform.
    *   Existing platforms are "too hard to use".
    *   Existing platforms don't have scalability.

**[Do People Actually Code as They Climb the Career Ladder? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kjuwnl/do_people_actually_code_as_they_climb_the_career/)**
*  **Summary:** The discussion revolves around whether people code as they climb the career ladder.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   As a manager, "doing the code" can vary from none to 80% of a week.
    *   Skills in PowerPoint have had more attention than anything else.
