---
title: "Data Engineering Subreddit"
date: "2025-10-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Struggling with separate Snowflake and Airflow environments for DEV/UAT/PROD - how do others handle this?](https://www.reddit.com/r/dataengineering/comments/1oajs0h/struggling_with_separate_snowflake_and_airflow/) (Score: 32)
    *   Users are discussing the best practices for managing Snowflake and Airflow environments across development, user acceptance testing (UAT), and production. The main question revolves around whether to use separate accounts or a single account with segregated databases.
2.  [Company is paying for my next DE cert. Which one to choose right now ?](https://www.reddit.com/r/dataengineering/comments/1oafuv2/company_is_paying_for_my_next_de_cert_which_one/) (Score: 25)
    *   Users are providing advice on which data engineering certifications are most valuable. Options mentioned include cloud-specific certifications, industry-neutral certifications, and vendor-specific certifications, with varying opinions on their usefulness.
3.  [handling sensitive pii data in modern lakehouse built with AWS stack](https://www.reddit.com/r/dataengineering/comments/1oagoef/handling_sensitive_pii_data_in_modern_lakehouse/) (Score: 7)
    *   This thread is about how to handle sensitive PII (Personally Identifiable Information) data in a modern lakehouse architecture built with the AWS stack.
4.  [Beginner Confused About Airflow Setup](https://www.reddit.com/r/dataengineering/comments/1oatq7o/beginner_confused_about_airflow_setup/) (Score: 4)
    *   Beginners are asking for help setting up Airflow for local development. Suggestions include using Docker, Astro CLI, and considering alternative tools like Dagster.
5.  [Evaluating my proposed approach](https://www.reddit.com/r/dataengineering/comments/1oaa9jv/evaluating_my_proposed_approach/) (Score: 3)
    *   Users are evaluating and suggesting improvements to a data engineering approach involving migrating from Alteryx and SQL Server to a modern data stack. Recommendations include Snowflake, dbt, BigQuery, Azure SQL, and Power BI.
6.  [Important analytical models/metrics you have made for social media and web analyst](https://www.reddit.com/r/dataengineering/comments/1oai1xu/important_analytical_modelsmetrics_you_have_made/) (Score: 2)
    *   Users are sharing analytical models and metrics they have created for social media and web analytics, such as conversation rate and attention score.
7.  [Is the data engineering job market good?](https://www.reddit.com/r/dataengineering/comments/1oa7fk5/is_the_data_engineering_job_market_good/) (Score: 0)
    *   Users are discussing the current state of the data engineering job market, with most agreeing that it is currently difficult due to high competition.

# Detailed Analysis by Thread
**[ [D] Struggling with separate Snowflake and Airflow environments for DEV/UAT/PROD - how do others handle this? (Score: 32)](https://www.reddit.com/r/dataengineering/comments/1oajs0h/struggling_with_separate_snowflake_and_airflow/)**
*   **Summary:** The thread discusses different approaches to managing Snowflake and Airflow environments for development, UAT, and production. Users are sharing their experiences and recommendations on whether to use separate accounts or a single account with segregated databases.
*   **Emotion:** The overall emotional tone of the thread is neutral, as users are primarily sharing technical advice and experiences in an objective manner.
*   **Top 3 Points of View:**
    *   **Single Snowflake Account with Separate Databases:** Many users recommend using a single Snowflake account with separate databases (and schemas) for each environment (DEV, UAT, PROD), leveraging RBAC (Role-Based Access Control) for security. This approach is considered easier to manage.
    *   **Separate Snowflake Accounts:** Some users have experience with separate Snowflake accounts for each environment, but generally find it more complex and costly to manage, although useful for testing security.
    *   **Airflow Deployment Considerations:** For Airflow, opinions vary, with some finding separate deployments a headache but more understandable than separate Snowflake accounts. Some suggest using local-first development environments with tools like dbt or bruin to minimize the need for separate Airflow environments.

**[Company is paying for my next DE cert. Which one to choose right now ? (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1oafuv2/company_is_paying_for_my_next_de_cert_which_one/)**
*   **Summary:** The thread revolves around which data engineering certification to pursue, with various users offering advice based on their experiences and the perceived value of different certifications in the job market.
*   **Emotion:** The emotional tone of the thread is mostly neutral, with users offering advice and opinions in an objective and informative way. There are slight variations depending on each users experience with a specific tool.
*   **Top 3 Points of View:**
    *   **Cloud-Specific Certifications (AWS, GCP, Databricks):** Some users recommend focusing on certifications related to specific cloud platforms (AWS, GCP) or tools like Databricks, as they are widely used and can open doors to better roles.
    *   **Industry-Neutral Certifications (CDMP, AI Governance):** Other users suggest pursuing industry-neutral certifications like CDMP Associate or AI Governance, as they provide broader knowledge and are applicable across different domains.
    *   **Vendor Certifications vs. Theoretical Knowledge:** A different point of view emphasizes strengthening theoretical knowledge (database design, data modeling) rather than focusing solely on vendor-specific certifications, arguing that understanding fundamental concepts is more valuable in the long term.

**[handling sensitive pii data in modern lakehouse built with AWS stack (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1oagoef/handling_sensitive_pii_data_in_modern_lakehouse/)**
*   **Summary:** The thread discusses how to handle sensitive PII (Personally Identifiable Information) data in a modern lakehouse architecture built with the AWS stack. The comment was removed.
*   **Emotion:** The emotional tone of the thread is neutral.
*   **Top 3 Points of View:** Since there is only one comment and it was removed. There is no data to extract any point of view.

**[Beginner Confused About Airflow Setup (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1oatq7o/beginner_confused_about_airflow_setup/)**
*   **Summary:** The thread is about a beginner's confusion regarding Airflow setup. Users are offering guidance on how to get started with Airflow, focusing on local development setups and suggesting tools like Docker and Astro CLI.
*   **Emotion:** The emotional tone is generally positive and helpful, as users are providing advice and resources to assist the beginner.
*   **Top 3 Points of View:**
    *   **Use Docker for Local Setup:** Many users recommend using Docker and Docker Compose for setting up Airflow locally, as it simplifies the process and provides a consistent environment.
    *   **Consider Astro CLI:** Astro CLI is suggested as a good starting point for beginners, as it provides a wrapper around Docker containers and simplifies Airflow setup.
    *   **Explore Alternatives like Dagster:** Some users suggest considering alternative orchestration tools like Dagster, which they believe are easier to set up and use for local development.

**[Evaluating my proposed approach (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1oaa9jv/evaluating_my_proposed_approach/)**
*   **Summary:** The thread is about evaluating a proposed data engineering approach, likely involving migrating from an existing setup (Alteryx and SQL Server) to a more modern data stack. Users are providing suggestions and alternatives based on their experiences.
*   **Emotion:** The emotional tone is mostly neutral and informative, as users are sharing their experiences and offering advice in an objective manner.
*   **Top 3 Points of View:**
    *   **Snowflake and dbt:** Several users suggest using Snowflake as a data warehouse and dbt for transformations, with Fivetran for data ingestion, highlighting the ease of use and manageability of this stack.
    *   **Azure SQL and ADF:** If the organization is already in the Microsoft ecosystem, using Azure SQL (managed SQL Server) and Azure Data Factory (ADF) pipelines is recommended as a cost-effective and integrated solution.
    *   **Google BigQuery:** BigQuery is suggested as a fully managed, scalable, and cost-effective data warehouse solution, especially for organizations with smaller data volumes.

**[Important analytical models/metrics you have made for social media and web analyst (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oai1xu/important_analytical_modelsmetrics_you_have_made/)**
*   **Summary:** The thread is about sharing analytical models and metrics for social media and web analytics.
*   **Emotion:** The emotional tone of the thread is neutral and informative.
*   **Top 3 Points of View:**
    *   The point of view built some around organic engagement too things like conversation rate (comments ÷ reach) and attention score that weights average watch time against total views also experimenting with a metric that tracks content decay over time to see how long posts keep driving clicks after day one

**[Is the data engineering job market good? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oa7fk5/is_the_data_engineering_job_market_good/)**
*   **Summary:** The thread discusses the current state of the data engineering job market.
*   **Emotion:** The emotional tone is negative.
*   **Top 3 Points of View:**
    *   The job market is not good and brutal right now. There are too many applicants and not enough positions.
