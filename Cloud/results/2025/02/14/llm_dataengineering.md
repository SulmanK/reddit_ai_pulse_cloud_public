---
title: "Data Engineering Subreddit"
date: "2025-02-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [What is that one DE project, that you liked the most?](https://www.reddit.com/r/dataengineering/comments/1ip6l0x/what_is_that_one_de_project_that_you_liked_the/) (Score: 58)
    *   Users discuss their favorite data engineering projects, ranging from building data pipelines for cruise lines to ingesting and analyzing healthcare insurance data and heavy machinery telematics.
2.  [Apache Iceberg Create Duplicate Parquet Files on Subsequent Runs](https://www.reddit.com/r/dataengineering/comments/1ip53hr/apache_iceberg_create_duplicate_parquet_files_on/) (Score: 15)
    *   Users discuss the issue of duplicate Parquet files being created in Apache Iceberg and potential solutions, including compaction, maintenance, and merge strategies.
3.  [Embedded ELT in the Orchestrator](https://dagster.io/blog/dagster-embedded-elt) (Score: 14)
    *   A user questions whether the linked blog post from October 2023 is the latest release from Dagster
4.  [What’s your biggest pain point with data reconciliation?](https://www.reddit.com/r/dataengineering/comments/1ip8d1k/whats_your_biggest_pain_point_with_data/) (Score: 8)
    *   Users share their biggest challenges in data reconciliation, including obtaining meaningful requirements from users and comparing on-prem and cloud data without a unified platform.
5.  [Moving from software developer to data engineer role](https://www.reddit.com/r/dataengineering/comments/1ip6ysf/moving_from_software_developer_to_data_engineer/) (Score: 6)
    *   Users share their experiences and advice for software developers transitioning to data engineering roles, discussing required skills, career paths, and the differences between the two fields.
6.  [Helping Junior Engineers upskill in Python?](https://www.reddit.com/r/dataengineering/comments/1ip6ed4/helping_junior_engineers_upskill_in_python/) (Score: 5)
    *   Users discuss effective methods for helping junior engineers improve their Python skills, including recommending courses and suggesting practical application.
7.  [Most effective way to join data in SAS/SQL](https://www.reddit.com/r/dataengineering/comments/1ipf8xc/most_effective_way_to_join_data_in_sassql/) (Score: 5)
    *   Users discuss the most efficient ways to join data in SAS/SQL environments, focusing on minimizing joins between SQL and SAS tables and potentially migrating away from SAS.
8.  [Opinion between these 2 job offers](https://www.reddit.com/r/dataengineering/comments/1ipd1s4/opinion_between_these_2_job_offers/) (Score: 4)
    *   Users offer opinions and advice on choosing between two job offers, considering factors like career trajectory, salary, and work environment.
9.  [What to spend learning budget on?](https://www.reddit.com/r/dataengineering/comments/1ip53vw/what_to_spend_learning_budget_on/) (Score: 3)
    *   Users recommend how to best utilize a learning budget, suggesting free learning materials, cloud provider resources, and academic courses over certifications.
10. [AI + synthetic data: How to smartly generate data sets with appropriate relationships?](https://www.reddit.com/r/dataengineering/comments/1ip9qcy/ai_synthetic_data_how_to_smartly_generate_data/) (Score: 3)
    *   Users discuss methods and tools for generating synthetic data using AI, including Synthetic Data Vault (SDV) and Snowflake's synthetic data generation feature.
11. [pt.2 start-up stock exchange data platform architecture](https://www.reddit.com/r/dataengineering/comments/1ipb3qm/pt2_startup_stock_exchange_data_platform/) (Score: 2)
    *   A user suggests using the Snowflake Connector for PostgreSQL for loading data from PostgreSQL to Snowflake instead of storing data in S3.
12. [MS SQL: Remove partition from partition scheme](https://www.reddit.com/r/dataengineering/comments/1ipcjkw/ms_sql_remove_partition_from_partition_scheme/) (Score: 2)
    *   Users discuss methods for removing a partition from an MS SQL partition scheme, including merging partitions, setting partitions as read-only, and dropping the partition.
13. [Advice for Better Airflow-DBT Orchestration](https://www.reddit.com/r/dataengineering/comments/1ip8fhh/advice_for_better_airflowdbt_orchestration/) (Score: 1)
    *   Users provide advice on improving Airflow-DBT orchestration, focusing on traceability, metadata logging, dependency trees, and tools like astronomer-cosmos.
14. [Data Quality Tools Options](https://www.reddit.com/r/dataengineering/comments/1ipd5pg/data_quality_tools_options/) (Score: 1)
    *   Users discuss options for data quality tools, recommending dbt and the elementary dbt package for testing and generating dashboards.
15. [Hahahaha... can't believe these guys for Vday!](https://www.reddit.com/r/dataengineering/comments/1ipbx7g/hahahaha_cant_believe_these_guys_for_vday/) (Score: 0)
    *   Users react to a marketing campaign, with some finding it cringeworthy and others suggesting it could be organic marketing.

# Detailed Analysis by Thread
**[What is that one DE project, that you liked the most? (Score: 58)](https://www.reddit.com/r/dataengineering/comments/1ip6l0x/what_is_that_one_de_project_that_you_liked_the/)**
*   **Summary:** Users describe various Data Engineering projects that they enjoyed working on. These projects involve building data pipelines, analyzing healthcare data, ingesting heavy machinery telematics, and implementing custom ELT solutions.
*   **Emotion:** The overall emotional tone of the thread is neutral, with individual comments expressing satisfaction, pride, or frustration depending on the project being discussed.
*   **Top 3 Points of View:**
    *   Building data pipelines to improve business outcomes (e.g., cruise line revenue, customer experience) is rewarding.
    *   Analyzing data to identify trends and solve problems (e.g., healthcare insurance trends, component failures in machinery) is fulfilling.
    *   Creating custom solutions to replace expensive or inefficient tools can be a significant accomplishment.

**[Apache Iceberg Create Duplicate Parquet Files on Subsequent Runs (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1ip53hr/apache_iceberg_create_duplicate_parquet_files_on/)**
*   **Summary:** Users discuss the issue of duplicate Parquet files being created in Apache Iceberg when performing repeated merge operations. They suggest solutions like compaction, maintenance, and creating hash rows to track changes.
*   **Emotion:** The emotional tone of the thread is primarily neutral, focusing on technical problem-solving. Some comments express a critical viewpoint of the user's approach.
*   **Top 3 Points of View:**
    *   Duplicate Parquet files are a normal part of how lakehouses like Iceberg operate.
    *   Compaction and maintenance are necessary to manage duplicate files.
    *   Relying on repeated merge operations can be a bad practice.

**[Embedded ELT in the Orchestrator (Score: 14)](https://dagster.io/blog/dagster-embedded-elt)**
*   **Summary:** A user questions whether the linked blog post from October 2023 is the latest release from Dagster
*   **Emotion:** The emotional tone of the thread is primarily neutral.
*   **Top 3 Points of View:**
    *   User is looking for the newest releases of Dagster products.

**[What’s your biggest pain point with data reconciliation? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1ip8d1k/whats_your_biggest_pain_point_with_data/)**
*   **Summary:** Users share their biggest challenges in data reconciliation.
*   **Emotion:** The emotional tone of the thread is primarily neutral.
*   **Top 3 Points of View:**
    *   Obtaining meaningful requirements from users is a major pain point.
    *   Comparing on-prem and cloud data without a unified platform is difficult.

**[Moving from software developer to data engineer role (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1ip6ysf/moving_from_software_developer_to_data_engineer/)**
*   **Summary:** Users share their experiences and advice for software developers transitioning to data engineering roles.
*   **Emotion:** The emotional tone of the thread is mixed, ranging from positive encouragement to negative warnings about the differences between the roles.
*   **Top 3 Points of View:**
    *   Data engineering is a subset of general software engineering.
    *   Strong SQL skills are essential for data engineers.
    *   Career paths in data engineering are similar to those in software engineering.

**[Helping Junior Engineers upskill in Python? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ip6ed4/helping_junior_engineers_upskill_in_python/)**
*   **Summary:** Users discuss effective methods for helping junior engineers improve their Python skills.
*   **Emotion:** The emotional tone of the thread is positive and helpful.
*   **Top 3 Points of View:**
    *   Practical application is the best way to learn Python.
    *   Specific courses like boot.dev can be beneficial.

**[Most effective way to join data in SAS/SQL (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ipf8xc/most_effective_way_to_join_data_in_sassql/)**
*   **Summary:** Users discuss the most efficient ways to join data in SAS/SQL environments.
*   **Emotion:** The emotional tone is primarily neutral, with some negative sentiment towards SAS.
*   **Top 3 Points of View:**
    *   Minimize joins between SQL and SAS tables.
    *   Migrating away from SAS is recommended.
    *   Joining workspace SAS data with server data will be a disaster.

**[Opinion between these 2 job offers (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ipd1s4/opinion_between_these_2_job_offers/)**
*   **Summary:** Users offer opinions and advice on choosing between two job offers.
*   **Emotion:** The emotional tone is neutral to positive, focusing on providing helpful advice.
*   **Top 3 Points of View:**
    *   Choose the job that best fits your career trajectory.
    *   Consider the currency when evaluating salary proposals.
    *   Remote or hybrid work arrangements can be subject to change.

**[What to spend learning budget on? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ip53vw/what_to_spend_learning_budget_on/)**
*   **Summary:** Users recommend how to best utilize a learning budget.
*   **Emotion:** The emotional tone is neutral and practical.
*   **Top 3 Points of View:**
    *   Prioritize free learning materials.
    *   Invest in cloud provider resources for practical experience.
    *   Consider academic courses over certifications.

**[AI + synthetic data: How to smartly generate data sets with appropriate relationships? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ip9qcy/ai_synthetic_data_how_to_smartly_generate_data/)**
*   **Summary:** Users discuss methods and tools for generating synthetic data using AI.
*   **Emotion:** The emotional tone is neutral and informative.
*   **Top 3 Points of View:**
    *   Synthetic Data Vault (SDV) is a potential solution.
    *   Snowflake offers synthetic data generation capabilities.

**[pt.2 start-up stock exchange data platform architecture (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ipb3qm/pt2_startup_stock_exchange_data_platform/)**
*   **Summary:** A user suggests using the Snowflake Connector for PostgreSQL.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The Snowflake Connector for PostgreSQL is a free and effective solution for loading data from PostgreSQL to Snowflake.

**[MS SQL: Remove partition from partition scheme (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ipcjkw/ms_sql_remove_partition_from_partition_scheme/)**
*   **Summary:** Users discuss methods for removing a partition from an MS SQL partition scheme.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Consider merging the partition into another.
    *   Set the partition as read-only.
    *   Dropping the partition might require dropping the scheme and index.

**[Advice for Better Airflow-DBT Orchestration (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ip8fhh/advice_for_better_airflowdbt_orchestration/)**
*   **Summary:** Users provide advice on improving Airflow-DBT orchestration.
*   **Emotion:** The emotional tone is positive and helpful.
*   **Top 3 Points of View:**
    *   Traceability and metadata logging are beneficial.
    *   Parsing the DBT manifest is necessary.
    *   astronomer-cosmos can help solve orchestration challenges.

**[Data Quality Tools Options (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ipd5pg/data_quality_tools_options/)**
*   **Summary:** Users discuss options for data quality tools.
*   **Emotion:** The emotional tone is neutral and informative.
*   **Top 3 Points of View:**
    *   Dbt is great for working with big query and testing.
    *   The elementary dbt package can help with storing test results and generating dashboards.

**[Hahahaha... can't believe these guys for Vday! (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ipbx7g/hahahaha_cant_believe_these_guys_for_vday/)**
*   **Summary:** Users react to a marketing campaign.
*   **Emotion:** The emotional tone is mixed, ranging from amusement to criticism.
*   **Top 3 Points of View:**
    *   The campaign is potentially an attempt at organic marketing.
    *   The campaign is cringeworthy and potentially inappropriate.
