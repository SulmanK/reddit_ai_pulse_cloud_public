---
title: "Data Engineering Subreddit"
date: "2025-02-07"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "trends", "discussions"]
---

# Overall Ranking and Top Discussions
1.  [How do companies with hundreds of databases document them effectively?](https://www.reddit.com/r/dataengineering/comments/1ijukwe/how_do_companies_with_hundreds_of_databases/) (Score: 76)
    *   The discussion revolves around how organizations manage and document their numerous databases, with many users expressing that proper documentation is often lacking, and others discussing solutions like data catalogs and dedicated DBA teams.
2.  [Why dagster instead airflow?](https://www.reddit.com/r/dataengineering/comments/1ijtt2b/why_dagster_instead_airflow/) (Score: 52)
    *   The discussion centers on the reasons to choose Dagster over Airflow, with a focus on Dagster's asset-based approach, better developer experience, and easier local development.
3.  [Data Modeling trends](https://www.reddit.com/r/dataengineering/comments/1ijpn7p/data_modeling_trends/) (Score: 33)
    *   This discussion covers current trends in data modeling, including the use of Data Vault, dimensional modeling, medallion architectures, and feature stores, with some skepticism towards reinventing the wheel.
4.  [Can I Pursue Data Engineering Without Liking Data Analysis?](https://www.reddit.com/r/dataengineering/comments/1ijo8pe/can_i_pursue_data_engineering_without_liking_data/) (Score: 21)
    *   The thread debates whether it's feasible to pursue a career in data engineering without enjoying data analysis, with varying opinions on the necessity and overlap between the two.
5.  [DBT vs SqlMesh?](https://www.reddit.com/r/dataengineering/comments/1ik3i6e/dbt_vs_sqlmesh/) (Score: 13)
    *   A user requested a reminder to check the thread in 3 days, indicating a desire to follow the discussion.
6.  [What data lineage tools do you use, and what makes them your go-to choice?](https://www.reddit.com/r/dataengineering/comments/1ijr4jd/what_data_lineage_tools_do_you_use_and_what_makes/) (Score: 10)
    *   The discussion centers on data lineage tools, with users mentioning Purview and OpenLineage, and discussing their pros and cons.
7.  [advice for an intern](https://www.reddit.com/r/dataengineering/comments/1ijrw50/advice_for_an_intern/) (Score: 5)
    *   Users are providing advice to a data engineering intern, focusing on DevOps skills, CI/CD pipelines, and tools like Terraform.
8.  [Understanding Athena Scanned Data](https://www.reddit.com/r/dataengineering/comments/1ijqtci/understanding_athena_scanned_data/) (Score: 4)
    *   The thread discusses how to optimize Athena queries to reduce the amount of data scanned.
9.  [TAM vs De](https://www.reddit.com/r/dataengineering/comments/1ik0zz5/tam_vs_de/) (Score: 3)
    *   The discussion revolves around the differences and overlaps between the roles of Technical Account Manager (TAM) and Data Engineer (DE).
10. [In-memory ETF (Transform) Workload to Reduce Load on Main Database](https://www.reddit.com/r/dataengineering/comments/1ijt9xv/inmemory_etf_transform_workload_to_reduce_load_on/) (Score: 2)
    *   A bot provided a link to community-submitted learning resources.
11. [What to put down as my exact role?](https://www.reddit.com/r/dataengineering/comments/1ijxym7/what_to_put_down_as_my_exact_role/) (Score: 2)
    *   The thread discusses the implications of accurately representing one's job title and responsibilities during background checks and interviews.
12. [Anybody has used both TablePlus and DbVisualizer?](https://www.reddit.com/r/dataengineering/comments/1ijoxhc/anybody_has_used_both_tableplus_and_dbvisualizer/) (Score: 1)
    *   Users share their experiences with TablePlus and DbVisualizer, discussing UI preferences and limitations of each tool.
13. [Anyone have any idea on who this company might be?](https://i.redd.it/e9plwgiglrhe1.jpeg) (Score: 0)
    *   Users speculate about the identity of a company based on a picture, with suggestions including Accenture, Deloitte, and Indian-based contractor firms.
14. [stuck in career data science in UK](https://www.reddit.com/r/dataengineering/comments/1ijrcch/stuck_in_career_data_science_in_uk/) (Score: 0)
    *   The discussion centers around advice for someone stuck in a data science career in the UK, with suggestions to transition into data engineering.
15. [How to scrap data?](https://www.reddit.com/r/dataengineering/comments/1ijvis2/how_to_scrap_data/) (Score: 0)
    *   The discussion revolves around how to scrape data from websites, with users recommending tools like `wget`, selenium, and cautioning about the legality of scraping.
16. [AI JSON preprocessing](https://www.reddit.com/r/dataengineering/comments/1ijxi4k/ai_json_preprocessing/) (Score: 0)
    *   The thread discusses the use of AI, particularly ChatGPT, for preprocessing JSON data.

# Detailed Analysis by Thread
**[How do companies with hundreds of databases document them effectively? (Score: 76)](https://www.reddit.com/r/dataengineering/comments/1ijukwe/how_do_companies_with_hundreds_of_databases/)**
*  **Summary:**  This thread discusses how companies document hundreds of databases. A common sentiment is that they often don't. Data catalogs, dedicated DBA teams, and AI-powered knowledge bases are suggested as potential solutions.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Most companies don't document their databases effectively.
    *   Data catalogs are a viable solution for documenting databases.
    *   Dedicated DBA teams are responsible for documentation, but tool usage is unclear.

**[Why dagster instead airflow? (Score: 52)](https://www.reddit.com/r/dataengineering/comments/1ijtt2b/why_dagster_instead_airflow/)**
*  **Summary:**  This thread explores the reasons for choosing Dagster over Airflow. Key points include Dagster's asset-based approach, superior developer experience, and easier local development and testing. Some users still prefer Airflow's workflow orchestration model.
*  **Emotion:** The overall emotional tone is Neutral, with a hint of negativity regarding Airflow's development experience.
*  **Top 3 Points of View:**
    *   Dagster's asset-based approach and developer experience are superior to Airflow.
    *   Airflow's workflow orchestration model is preferred by some.
    *   Local development and testing are much easier with Dagster.

**[Data Modeling trends (Score: 33)](https://www.reddit.com/r/dataengineering/comments/1ijpn7p/data_modeling_trends/)**
*  **Summary:**  The discussion covers various data modeling trends, including Data Vault (DV), dimensional modeling, medallion architectures, and feature stores. There's a debate about whether to stick with tried-and-true methods like Kimball and Inmon or adopt newer approaches.
*  **Emotion:** The overall emotional tone is Neutral, with a mix of positive and negative sentiments towards different modeling techniques.
*  **Top 3 Points of View:**
    *   Data Vault is suitable for a niche set of use cases, but requires trained personnel.
    *   Dimensional modeling (Kimball, Inmon) remains relevant and effective.
    *   Medallion architectures are becoming more standard due to lower storage and compute costs.

**[Can I Pursue Data Engineering Without Liking Data Analysis? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1ijo8pe/can_i_pursue_data_engineering_without_liking_data/)**
*  **Summary:**  This thread debates the feasibility of a data engineering career without enjoying data analysis. Some argue that data analysis is integral to many DE roles, while others suggest focusing on areas like system design and infrastructure.
*  **Emotion:** The overall emotional tone is mixed, with both Positive and Negative sentiment.
*  **Top 3 Points of View:**
    *   Data analysis is a necessary component of most data engineering roles.
    *   It's possible to focus on other areas like system design, infrastructure, and DevOps.
    *   Understanding data is crucial for growth in data engineering.

**[DBT vs SqlMesh? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1ik3i6e/dbt_vs_sqlmesh/)**
*  **Summary:** A user set a reminder for 3 days, implying interest in the discussion to follow.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   N/A - This thread only contains a reminder.

**[What data lineage tools do you use, and what makes them your go-to choice? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1ijr4jd/what_data_lineage_tools_do_you_use_and_what_makes/)**
*  **Summary:** The discussion focuses on data lineage tools, with Purview and OpenLineage being mentioned. Users discuss their integration capabilities and community support.
*  **Emotion:** The overall emotional tone is Neutral, with some positive sentiment towards OpenLineage.
*  **Top 3 Points of View:**
    *   Purview is preferred for its broad integration capabilities and business glossary.
    *   OpenLineage is liked for being an open standard with a great community and open PRs.

**[advice for an intern (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ijrw50/advice_for_an_intern/)**
*  **Summary:** Advice for a data engineering intern focusing on DevOps skills, CI/CD pipelines, and tools like Terraform.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Interns should focus on learning CI/CD pipelines and using .yml files for deployment.
    *   Exposure to Terraform is valuable.
    *   Collaborating with dev and ops teams can broaden the perspective on end-to-end processes.

**[Understanding Athena Scanned Data (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ijqtci/understanding_athena_scanned_data/)**
*  **Summary:** This thread discusses how to optimize Athena queries to minimize scanned data by using `select distinct` or `where` clauses.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   To avoid scanning all rows, use "select distinct" to get a single value, or "where" clause.

**[TAM vs De (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ik0zz5/tam_vs_de/)**
*  **Summary:** This discussion explains that the TAM role varies among different organizations.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The TAM role can include support, sales, and solutions architecture.
    *   The TAM role might be solely support and account management.
    *   The meaning of a TAM role can vary from organization to organization.

**[In-memory ETF (Transform) Workload to Reduce Load on Main Database (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ijt9xv/inmemory_etf_transform_workload_to_reduce_load_on/)**
*  **Summary:** This is a bot response linking to learning resources.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   N/A - This is a bot response.

**[What to put down as my exact role? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ijxym7/what_to_put_down_as_my_exact_role/)**
*  **Summary:** The thread discusses implications of accurately representing job titles and responsibilities during background checks and interviews.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Listing an inaccurate job title can be flagged during background checks.
    *   Performing analyst responsibilities while interviewing for DE roles will be noticeable.

**[Anybody has used both TablePlus and DbVisualizer? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ijoxhc/anybody_has_used_both_tableplus_and_dbvisualizer/)**
*  **Summary:** This discusses user experiences with TablePlus and DbVisualizer.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   TablePlus has a great UI, even with limitations on connections.
    *   DbVisualizer is not significantly different, but has different limitations.
    *  Snowsight is heavily used when working with snowflake.

**[Anyone have any idea on who this company might be? (Score: 0)](https://i.redd.it/e9plwgiglrhe1.jpeg)**
*  **Summary:** Users speculate on the identity of a company from a photo, suggesting Accenture, Deloitte, and Indian firms.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Could be a large or small system integrator with RSUs.
    *   Could be an India-based contractor firm.
    *   Not related to data engineering.

**[stuck in career data science in UK (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ijrcch/stuck_in_career_data_science_in_uk/)**
*  **Summary:** Advice for someone stuck in a data science career in the UK, with a recommendation to transition into data engineering.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Focus on the data engineering part of the work.
    *   Data engineering has better job prospects than data science.
    *   It's important to set boundaries.

**[How to scrap data? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ijvis2/how_to_scrap_data/)**
*  **Summary:** This thread discusses how to scrape data, recommending tools like `wget` and selenium, and warning about legality.
*  **Emotion:** The overall emotional tone is Neutral, with some positive sentiment towards the challenge.
*  **Top 3 Points of View:**
    *   `wget -m` can be used for basic scraping, but isn't 100% effective.
    *   Selenium can be used if wget is not enough.
    *   Web scraping may be illegal.

**[AI JSON preprocessing (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ijxi4k/ai_json_preprocessing/)**
*  **Summary:** The thread is about using AI, specifically ChatGPT, for JSON preprocessing.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   ChatGPT can be used to parse JSON or give the code to do so.
    *   The user is requesting to use a specific SaaS which is a ChatGPT wrapper.
    *   Using AI for easier JSON parsing or table creation would be an awesome idea.
