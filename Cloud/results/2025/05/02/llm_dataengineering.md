---
title: "Data Engineering Subreddit"
date: "2025-05-02"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1. [[D] What do you use Spark for?](https://www.reddit.com/r/dataengineering/comments/1kcyesf/what_do_you_use_spark_for/) (Score: 33)
    * The discussion revolves around use cases for Apache Spark in data engineering, with comments on its strengths, weaknesses, and alternatives.
2.  [Is it common for companies to hire people for "data engineering" roles, but really the role is DevOps?](https://www.reddit.com/r/dataengineering/comments/1kd63d0/is_it_common_for_companies_to_hire_people_for/) (Score: 28)
    * Users discuss the overlap between Data Engineering and DevOps roles, with many sharing experiences of being hired as Data Engineers but spending significant time on DevOps tasks.
3.  [Laid-off Data Engineer Struggling to Transition – Need Career Advice](https://www.reddit.com/r/dataengineering/comments/1kct5lz/laidoff_data_engineer_struggling_to_transition/) (Score: 27)
    *  Laid-off data engineers seek career advice in transitioning to modern technologies and finding new opportunities in a saturated job market.
4.  [Data infrastructure for self-driving labs](https://www.reddit.com/r/dataengineering/comments/1kd34is/data_infrastructure_for_selfdriving_labs/) (Score: 7)
    *  This thread discusses the optimal data infrastructure for self-driving labs, with suggestions around Postgres, PostGIS, pgRouting, JSONB types, TimeScaleDB, DuckDB, and Crunchy Data's Postgres Playground.
5.  [is the CDVP2 (Certified Data vault practitioner) worth it?](https://www.reddit.com/r/dataengineering/comments/1kd1mfl/is_the_cdvp2_certified_data_vault_practitioner/) (Score: 5)
    *  The thread discusses the value of the CDVP2 (Certified Data Vault Practitioner) certification.
6.  [Need incremental data from lake](https://www.reddit.com/r/dataengineering/comments/1kcyxqa/need_incremental_data_from_lake/) (Score: 4)
    *  A discussion about how to extract incremental data from a data lake, particularly when timestamps are missing from the source data.
7.  [Have a non DE title and doesn’t help at all](https://www.reddit.com/r/dataengineering/comments/1kczly2/have_a_non_de_title_and_doesnt_help_at_all/) (Score: 4)
    *  Users are discussing whether having a non-Data Engineering title hinders job applications and career prospects.
8.  [How much is your org spending on ETL SaaS, and how hard would it be to internalize it?](https://www.reddit.com/r/dataengineering/comments/1kd6u3s/how_much_is_your_org_spending_on_etl_saas_and_how/) (Score: 4)
    *  The cost and feasibility of internalizing ETL SaaS solutions like Fivetran are debated among data engineers.
9.  [Not able to create compute cluster in Databricks.](https://www.reddit.com/r/dataengineering/comments/1kcxi1j/not_able_to_create_compute_cluster_in_databricks/) (Score: 3)
    *  Users are trying to troubleshoot issues when creating compute clusters in Databricks, with possible solutions like checking Azure quotas or VM availability.
10. [How to better prepare for an entry-level data engineer as a fresh grad?](https://www.reddit.com/r/dataengineering/comments/1kd2n6v/how_to_better_prepare_for_an_entrylevel_data/) (Score: 3)
    *  The discussion centers around providing advice on how fresh graduates can prepare for entry-level data engineering roles, focusing on essential skills and tools.
11. [Data Governance Analysts tasks and duties ?](https://www.reddit.com/r/dataengineering/comments/1kd781f/data_governance_analysts_tasks_and_duties/) (Score: 2)
    *  The discussion asks about data governance analyst tasks and duties.
12. [Need advice on tech stack for large table](https://www.reddit.com/r/dataengineering/comments/1kd9mju/need_advice_on_tech_stack_for_large_table/) (Score: 0)
    *  Users seek advice on tech stack recommendations for managing large tables, with suggestions around Snowflake, Redshift, and other data management tools.

# Detailed Analysis by Thread
**[[D] What do you use Spark for? (Score: 33)](https://www.reddit.com/r/dataengineering/comments/1kcyesf/what_do_you_use_spark_for/)**
*  **Summary:**  The discussion revolves around use cases for Apache Spark in data engineering, with comments on its strengths, weaknesses, and alternatives.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Spark is valuable for processing massive datasets, especially when tuning jobs for performance.
    *   Spark can be used for writing to iceberg tables due to its reference implementation.
    *   Spark use for ETL is coming to an end and is being replaced by a single-machine processing engine.

**[Is it common for companies to hire people for "data engineering" roles, but really the role is DevOps? (Score: 28)](https://www.reddit.com/r/dataengineering/comments/1kd63d0/is_it_common_for_companies_to_hire_people_for/)**
*  **Summary:** Users discuss the overlap between Data Engineering and DevOps roles, with many sharing experiences of being hired as Data Engineers but spending significant time on DevOps tasks.
*  **Emotion:** The overall emotional tone is Neutral, with some comments expressing frustration and others a positive sentiment.
*  **Top 3 Points of View:**
    *   It's common for Data Engineering roles to involve DevOps tasks like setting up infrastructure and CI/CD pipelines.
    *   DataOps and MLOps are related to Data Engineering, and Data Engineers should have some knowledge of infrastructure.
    *   The mismatch between job descriptions and actual responsibilities is an HR problem.

**[Laid-off Data Engineer Struggling to Transition – Need Career Advice (Score: 27)](https://www.reddit.com/r/dataengineering/comments/1kct5lz/laidoff_data_engineer_struggling_to_transition/)**
*  **Summary:** Laid-off data engineers seek career advice in transitioning to modern technologies and finding new opportunities in a saturated job market.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Focus on building end-to-end projects and showcasing them on GitHub to demonstrate modern skills.
    *   Upskilling in Python, Spark, SQL, and cloud technologies (AWS, Azure, GCP) is essential.
    *   Highlighting experience with legacy systems can be a unique selling point (USP) in the job market.

**[Data infrastructure for self-driving labs (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kd34is/data_infrastructure_for_selfdriving_labs/)**
*  **Summary:** This thread discusses the optimal data infrastructure for self-driving labs, with suggestions around Postgres, PostGIS, pgRouting, JSONB types, TimeScaleDB, DuckDB, and Crunchy Data's Postgres Playground.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Postgres and its extensions (PostGIS, pgRouting, TimeScaleDB) can be well-suited for self-driving data.
    *   The choice of infrastructure depends on the specific use case and context.
    *   There is a trade-off between using managed solutions from hyper scalers and maintaining control over hardware.

**[is the CDVP2 (Certified Data vault practitioner) worth it? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kd1mfl/is_the_cdvp2_certified_data_vault_practitioner/)**
*  **Summary:** The thread discusses the value of the CDVP2 (Certified Data Vault Practitioner) certification.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The CDVP2 certification may not be widely recognized or valued by many companies.
    *   It is only worth getting if consulting specifically for data vault solutions.
    *   A bot recommends checking learning resources in the community.

**[Need incremental data from lake (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1kcyxqa/need_incremental_data_from_lake/)**
*  **Summary:** A discussion about how to extract incremental data from a data lake, particularly when timestamps are missing from the source data.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    *   If the source data lacks timestamps, hashing the source data and storing the hash in the destination table is one method to identify updates.

**[Have a non DE title and doesn’t help at all (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1kczly2/have_a_non_de_title_and_doesnt_help_at_all/)**
*  **Summary:** Users are discussing whether having a non-Data Engineering title hinders job applications and career prospects.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The title is not the only issue and the OP needs to show their resume and portfolio.
    *   The issue isn't the title but the approach to applying for jobs.
    *   Just add DE to your resume and make up a title on LinkedIn.

**[How much is your org spending on ETL SaaS, and how hard would it be to internalize it? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1kd6u3s/how_much_is_your_org_spending_on_etl_saas_and_how/)**
*  **Summary:** The cost and feasibility of internalizing ETL SaaS solutions like Fivetran are debated among data engineers.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   For many businesses, writing and maintaining ETL pipelines is unfeasible and more expensive than using SaaS solutions like Fivetran.
    *   Fivetran is catering to VC-funded or enterprise organizations who don't need to integrate with more exotic data sources and are not price sensitive.
    *   There are connector tools on the market that provide similar functionality and cost less compared to Fivetran.

**[Not able to create compute cluster in Databricks. (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kcxi1j/not_able_to_create_compute_cluster_in_databricks/)**
*  **Summary:** Users are trying to troubleshoot issues when creating compute clusters in Databricks, with possible solutions like checking Azure quotas or VM availability.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Check the Azure quota for the VM class being used.
    *   The specific VM size might not be available in the chosen region.
    *   Using AI tools like ChatGPT might help in spotting typos in the config.

**[How to better prepare for an entry-level data engineer as a fresh grad? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kd2n6v/how_to_better_prepare_for_an_entrylevel_data/)**
*  **Summary:** The discussion centers around providing advice on how fresh graduates can prepare for entry-level data engineering roles, focusing on essential skills and tools.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Focus on SQL, ETL processes, and data warehousing basics.
    *   The organization is expected to shape entry-level hires.
    *   Know what the role focuses on and the skills it specifically uses.

**[Data Governance Analysts tasks and duties ? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kd781f/data_governance_analysts_tasks_and_duties/)**
*  **Summary:** The discussion asks about data governance analyst tasks and duties.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    *   Start by looking up what "governance" means.

**[Need advice on tech stack for large table (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kd9mju/need_advice_on_tech_stack_for_large_table/)**
*  **Summary:** Users seek advice on tech stack recommendations for managing large tables, with suggestions around Snowflake, Redshift, and other data management tools.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 1 Points of View:**
    *   Snowflake, Redshift, and DreamFactory are good options for data management.
