---
title: "Data Engineering Subreddit"
date: "2025-08-12"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "LLMs", "career advice"]
---

# Overall Ranking and Top Discussions
1. [[D] The push for LLMs is making my data team's work worse](https://www.reddit.com/r/dataengineering/comments/1moanf4/the_push_for_llms_is_making_my_data_teams_work/) (Score: 101)
    * The discussion revolves around the increasing pressure to adopt LLMs for tasks where existing solutions are already effective, leading to concerns about data quality, accuracy, and overall team efficiency.
2.  [Accidentally became my company's unpaid data engineer. Need advice.](https://www.reddit.com/r/dataengineering/comments/1mo82xz/accidentally_became_my_companys_unpaid_data/) (Score: 65)
    * The user seeks advice on how to address the situation of performing data engineering tasks without proper compensation or recognition. Advice includes documenting work, calculating value, asking for a promotion, and looking for a job elsewhere.
3.  [When do you guys decide to denormalize your DB?](https://www.reddit.com/r/dataengineering/comments/1mo4ouk/when_do_you_guys_decide_to_denormalize_your_db/) (Score: 29)
    * The discussion covers strategies and situations for database denormalization, primarily for improving performance in OLAP systems.
4.  [Pandas vs SQL - doubt](https://www.reddit.com/r/dataengineering/comments/1mohowo/pandas_vs_sql_doubt/) (Score: 4)
    * This thread is about the preference between Pandas and SQL for data manipulation, with many users suggesting that SQL is better.
5.  [How do you guys create test data for a functional change?](https://www.reddit.com/r/dataengineering/comments/1moel28/how_do_you_guys_create_test_data_for_a_functional/) (Score: 3)
    * The post is a question of how to generate/create test data for functional changes.
6.  [Data warehouse for a small company](https://www.reddit.com/r/dataengineering/comments/1mogizo/data_warehouse_for_a_small_company/) (Score: 3)
    * This thread discusses whether a small company needs a dedicated data warehouse or if they can use analytical views in a transactional database.
7.  [No Cloud, No OOP - Can I Still Go for Fintech Roles?](https://www.reddit.com/r/dataengineering/comments/1moikon/no_cloud_no_oop_can_i_still_go_for_fintech_roles/) (Score: 2)
    * User wants to know if they still go for fintech roles without cloud and OOP.
8.  [Need advice using dagster with dbt where dbt models are updated frequently](https://www.reddit.com/r/dataengineering/comments/1mo64ly/need_advice_using_dagster_with_dbt_where_dbt/) (Score: 1)
    * User is seeking advice on how to use Dagster with dbt where dbt models are updated frequently.
9.  [Looking for guidance in cleaning data for a personal project.](https://www.reddit.com/r/dataengineering/comments/1moif7p/looking_for_guidance_in_cleaning_data_for_a/) (Score: 1)
    * User is looking for guidance in cleaning data for a personal project.
10. [Switch Datbricks to Palantir?](https://www.reddit.com/r/dataengineering/comments/1mog65z/switch_datbricks_to_palantir/) (Score: 0)
    * User is looking for suggestions on switching from Databricks to Palantir.

# Detailed Analysis by Thread
**[[D] The push for LLMs is making my data team's work worse (Score: 101)](https://www.reddit.com/r/dataengineering/comments/1moanf4/the_push_for_llms_is_making_my_data_teams_work/)**
*   **Summary:** The main point of discussion is the challenge of leadership pushing for LLM adoption even when existing, proven solutions are more effective. This leads to concerns about data quality, accuracy, increased costs, and reduced efficiency.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   LLMs are being pushed for the sake of appearing innovative, even if they provide worse results and higher costs.
    *   It's important to present data-driven evidence to leadership showing the negative impacts of LLMs on data quality and efficiency.
    *   Data quality metrics are essential to quantify the negative impacts of LLMs in terms of availability, cost, and engineering toil.

**[Accidentally became my company's unpaid data engineer. Need advice. (Score: 65)](https://www.reddit.com/r/dataengineering/comments/1mo82xz/accidentally_became_my_companys_unpaid_data/)**
*   **Summary:** The user is performing data engineering tasks without the proper title or compensation. The advice focuses on strategies to address this, including documenting contributions, assessing market rate, and potentially seeking external opportunities.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Document all contributions and quantify the value delivered to the company in business terms.
    *   Research the market rate for the work being performed and present this information to management.
    *   If internal efforts to get a promotion or raise fail, start interviewing for data engineering positions elsewhere.

**[When do you guys decide to denormalize your DB? (Score: 29)](https://www.reddit.com/r/dataengineering/comments/1mo4ouk/when_do_you_guys_decide_to_denormalize_your_db/)**
*   **Summary:** The thread discusses when to denormalize a database. The consensus is that denormalization is beneficial for OLAP (Online Analytical Processing) to improve query performance, whereas normalized models are preferred for OLTP (Online Transaction Processing) to maintain data integrity.
*   **Emotion:** The overall emotional tone is neutral. There's a single negative comment.
*   **Top 3 Points of View:**
    *   Denormalize for OLAP systems to improve query performance, especially in data warehouses or data marts.
    *   Normalize for OLTP systems to maintain data integrity and consistency.
    *   Consider Inmon vs. Kimball methodologies for data warehouse design, with Inmon favoring a 3NF model first and Kimball favoring star schema.

**[Pandas vs SQL - doubt (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1mohowo/pandas_vs_sql_doubt/)**
*   **Summary:** The post is a question about if Pandas is a useful tool to know, compared to SQL.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   SQL is simple and supreme don’t over engineering.
    *   The less you use pandas the better it is.
    *   Stay away from pandas as much as possible if you can.

**[How do you guys create test data for a functional change? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1moel28/how_do_you_guys_create_test_data_for_a_functional/)**
*   **Summary:** This thread discusses how to generate or create test data for functional changes in data pipelines.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 2 Points of View:**
    *   Copy some existing data into a separate environment or table and run it through both pipelines to compare results.
    *   Use Hypothesis to generate data.

**[Data warehouse for a small company (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mogizo/data_warehouse_for_a_small_company/)**
*   **Summary:** The discussion centers on whether a small company with a limited amount of data needs a dedicated data warehouse or if alternative solutions can be implemented.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 2 Points of View:**
    *   For a small amount of data, a dedicated data warehouse may not be necessary. Instead, analytical views within the transactional database, combined with a read replica for reporting, can be a cost-effective solution.
    *   If the dataset is small enough, a local Sqlite database with Superset for visualization might suffice, avoiding the need for cloud infrastructure.

**[No Cloud, No OOP - Can I Still Go for Fintech Roles? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1moikon/no_cloud_no_oop_can_i_still_go_for_fintech_roles/)**
*   **Summary:** This thread's about whether someone can get fintech roles without cloud and OOP experience.
*   **Emotion:** The overall emotional tone is neutral. There's one positive comment.
*   **Top 2 Points of View:**
    *   Lovely. Another AI post.
    *   Are you interested in transitioning into Data Engineering? Read our community guide: https://dataengineering.wiki/FAQ/How+can+I+transition+into+Data+Engineering

**[Need advice using dagster with dbt where dbt models are updated frequently (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mo64ly/need_advice_using_dagster_with_dbt_where_dbt/)**
*   **Summary:** This thread seeks advice on using Dagster with dbt where dbt models are updated frequently.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 1 Point of View:**
    *   The key is to trigger step 2 above any time your models change, treating the dbt manifest.json as a build artifact produced by the dbt repo.

**[Looking for guidance in cleaning data for a personal project. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1moif7p/looking_for_guidance_in_cleaning_data_for_a/)**
*   **Summary:** A user is looking for guidance on cleaning data for a personal project.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 2 Points of View:**
    *   I was told to use an AI agent from a friend, although I’ve never worked with AI before and it seems to be quite expensive.
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[Switch Datbricks to Palantir? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mog65z/switch_datbricks_to_palantir/)**
*   **Summary:** This thread discusses switching from Databricks to Palantir.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   No.
    *   Palantir itself is a terrible product, though it is useful for its niche.
    *   Palantir recently announced a partnership with Databricks where DBX can be used as the compute engine of PLTR, maybe you could suggest that.
