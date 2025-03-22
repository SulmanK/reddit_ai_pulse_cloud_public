---
title: "Data Engineering Subreddit"
date: "2025-03-22"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Starting to see why monolithic services appeal to execs](https://www.reddit.com/r/dataengineering/comments/1jgwdo6/starting_to_see_why_monolithic_services_appeal_to/) (Score: 40)
    * This thread discusses the reasons why executives might prefer monolithic services over microservices in data engineering, touching on risk, benefit, speed of delivery, and the impact of non-technical management.
2.  [Optimising for spark job which is processing about 6.7 TB of raw data.](https://www.reddit.com/r/dataengineering/comments/1jh0mbq/optimising_for_spark_job_which_is_processing/) (Score: 20)
    * This thread focuses on optimizing a Spark job processing a large volume of raw data. The discussion involves partitioning strategies, memory allocation, data formats, and incremental processing techniques.
3.  [Waning Data Engineer](https://www.reddit.com/r/dataengineering/comments/1jh844y/waning_data_engineer/) (Score: 13)
    * The discussion revolves around the challenges of career progression for a data engineer, particularly in achieving a "senior" title. It explores the subjective nature of job titles, the importance of soft skills, and strategies for negotiating promotions or finding new opportunities.
4.  [Iceberg data catalogs differences](https://www.reddit.com/r/dataengineering/comments/1jh6lie/iceberg_data_catalogs_differences/) (Score: 9)
    * This thread discusses the differences between iceberg data catalogs. The conversation touches on using iceberg tables as external tables in snowflake and using Polaris to help with efficiently running SQL queries.
5.  [Data quality checks](https://www.reddit.com/r/dataengineering/comments/1jh636z/data_quality_checks/) (Score: 7)
    * This thread discusses the importance of creating reconciliation scripts/reports that ensure accurate row counts, validates at least some percentage of source data, traces/tests for completeness, ensures key consistency, tests for duplicate records, and then any use case/industry-specific testing
6.  [Helping my cousin land her first data engineering job](https://www.reddit.com/r/dataengineering/comments/1jgyxik/helping_my_cousin_land_her_first_data_engineering/) (Score: 4)
    * This thread shares a valuable resource for learning data engineering.
7.  [Integration testing DAGs in an on premise environment](https://www.reddit.com/r/dataengineering/comments/1jh2dxa/integration_testing_dags_in_an_on_premise/) (Score: 3)
    * This thread discusses integration testing DAGs in an on-premise environment, recommending Dagster for simplifying DAG testing.
8.  [Old database migration to a new ERP](https://www.reddit.com/r/dataengineering/comments/1jhbzuy/old_database_migration_to_a_new_erp/) (Score: 2)
    * This thread discusses the complexities of migrating an old database to a new ERP system, emphasizing the importance of understanding the data model and its dependencies.
9.  [automated wordpress blogs](https://www.reddit.com/r/dataengineering/comments/1jhdi7z/automated_wordpress_blogs/) (Score: 2)
    * This thread provides a link to the community open-source project showcase
10. [Which tool would you recommend for this task?](https://www.reddit.com/r/dataengineering/comments/1jh8igl/which_tool_would_you_recommend_for_this_task/) (Score: 2)
    * This thread asks for information regarding the amount of data needed to be processed and if the user is running on-premises or in the cloud
11. [[Discussion] New ETL platform](https://www.reddit.com/r/dataengineering/comments/1jhfy9d/discussion_new_etl_platform/) (Score: 1)
    * This thread provides a link to the community open-source project showcase and a gif of someone shaking their head.
12. [Need feedbacks: Guepard, The turbocharged-Git for Databases 🐆](https://www.reddit.com/r/dataengineering/comments/1jgv6vo/need_feedbacks_guepard_the_turbochargedgit_for/) (Score: 0)
    * This thread provides a link to the community open-source project showcase
13. [🚀 Building the Perfect Data Stack: Complexity vs. Simplicity](https://www.reddit.com/r/dataengineering/comments/1jh96k6/building_the_perfect_data_stack_complexity_vs/) (Score: 0)
    * This thread discusses the balance between complexity and simplicity when building a data stack.
14. [Have You Heard of This Powerful Alternative to Requests in Python?](https://www.reddit.com/r/dataengineering/comments/1jhazl0/have_you_heard_of_this_powerful_alternative_to/) (Score: 0)
    * This thread discusses a powerful alternative to request in Python.
15. ["vibe coding" how do we feel about that as data engineers](https://www.reddit.com/r/dataengineering/comments/1jhc3fk/vibe_coding_how_do_we_feel_about_that_as_data/) (Score: 0)
    * This thread explores the concept of "vibe coding" (using AI to generate code) and its implications for data engineers.

# Detailed Analysis by Thread
**[Starting to see why monolithic services appeal to execs (Score: 40)](https://www.reddit.com/r/dataengineering/comments/1jgwdo6/starting_to_see_why_monolithic_services_appeal_to/)**
*  **Summary:** The thread discusses why executives often prefer monolithic services due to the perceived lower risk, faster delivery, and immediate cost benefits compared to microservices. The conversation also touches on the challenges of managing rapidly changing technologies and the importance of having technical expertise in leadership roles.
*  **Emotion:** The emotional tone is mostly Neutral, with some Positive and Negative sentiments mixed in.
*  **Top 3 Points of View:**
    * Executives prefer monolithic services because they prioritize immediate gains and perceived lower risks, driven by a "pay right now and get it fast" mentality.
    * Frequent adoption of new technologies without fully implementing previous ones leads to wasted time and money, often driven by non-technical middle management.
    * Engineers should be involved in tech stack decisions, and they should focus on making flexible choices rather than striving for perfection.

**[Optimising for spark job which is processing about 6.7 TB of raw data. (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1jh0mbq/optimising_for_spark_job_which_is_processing/)**
*  **Summary:** This thread revolves around optimizing a Spark job that processes a significant amount of raw data. The discussion points cover clarifying reprocessing needs, optimizing partition sizes and executor configurations, utilizing data partitioning and pushdown optimizations, choosing appropriate file formats (like Parquet), and considering incremental processing strategies. The thread also mentions using delta tables and Change Data Feed (CDF) where applicable.
*  **Emotion:** The overall emotional tone is Neutral, indicating a focus on technical advice and problem-solving.
*  **Top 3 Points of View:**
    * Clarify whether the data processing involves historical data and whether incremental processing is possible.
    * Optimize Spark configuration by adjusting executor memory, cores, and the number of instances.
    * Ensure the data is stored in an optimal format (e.g., Parquet) and consider using delta tables with Change Data Feed (CDF) for incremental updates.

**[Waning Data Engineer (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1jh844y/waning_data_engineer/)**
*  **Summary:** The thread discusses the challenges a data engineer faces in getting promoted to a senior role, despite having significant experience. It touches on the subjectivity of job titles, the importance of soft skills and leadership qualities, and the value of seeking external job offers to leverage internal promotions.
*  **Emotion:** The emotional tone is largely Neutral, with some instances of Positive sentiment related to encouragement and offering solutions.
*  **Top 3 Points of View:**
    * The definition of "senior" varies from company to company, and sometimes companies avoid giving the title to avoid higher pay.
    * Soft skills, leadership abilities, and the ability to influence others are just as important as technical skills for senior roles.
    * Seeking external job offers can be a powerful way to negotiate promotions and salary increases with the current employer.

**[Iceberg data catalogs differences (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1jh6lie/iceberg_data_catalogs_differences/)**
*  **Summary:** The thread discusses building iceberg and putting data in it, using iceberg tables as external tables in snowflake, and using Polaris to help with efficiently running SQL queries.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Use iceberg tables as external tables in snowflake
    * Save cost by only provisioning for end users.
    * Polaris is deployed on top of iceberg to help with efficiently running SQL queries.

**[Data quality checks (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jh636z/data_quality_checks/)**
*  **Summary:** The thread discusses the importance of creating reconciliation scripts/reports that ensures accurate row counts, validates at least some percentage of source data, traces/tests for completeness, ensures key consistency, tests for duplicate records, and then any use case/industry-specific testing
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    * Create a reconciliation script/report that ensures accurate row counts
    * Validate at least some percentage of source data
    * Tests for duplicate records

**[Helping my cousin land her first data engineering job (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1jgyxik/helping_my_cousin_land_her_first_data_engineering/)**
*  **Summary:** The thread shares a valuable resource for learning data engineering.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * Share a valuable resource for learning data engineering.

**[Integration testing DAGs in an on premise environment (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jh2dxa/integration_testing_dags_in_an_on_premise/)**
*  **Summary:** The thread discusses integration testing DAGs in an on-premise environment, recommending Dagster for simplifying DAG testing.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * Using something like dagster makes your dag testing much simpler

**[Old database migration to a new ERP (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jhbzuy/old_database_migration_to_a_new_erp/)**
*  **Summary:** This thread discusses the complexities of migrating an old database to a new ERP system, emphasizing the importance of understanding the data model and its dependencies.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    * Attempting to integrate with an outdated ERP is inherently risky.
    * The most important step is to start understanding the datamodel and it's dependencies.
    * Dump, transform, upload, done.

**[automated wordpress blogs (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jhdi7z/automated_wordpress_blogs/)**
*  **Summary:** This thread provides a link to the community open-source project showcase
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * You can find our open-source project showcase here: https://dataengineering.wiki/Community/Projects

**[Which tool would you recommend for this task? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jh8igl/which_tool_would_you_recommend_for_this_task/)**
*  **Summary:** This thread asks for information regarding the amount of data needed to be processed and if the user is running on-premises or in the cloud
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * What is the amount of data you need to process? Are you running on-premises or in the cloud?

**[[Discussion] New ETL platform (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jhfy9d/discussion_new_etl_platform/)**
*  **Summary:** This thread provides a link to the community open-source project showcase and a gif of someone shaking their head.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    * You can find our open-source project showcase here: https://dataengineering.wiki/Community/Projects
    * GUI and C#?

**[Need feedbacks: Guepard, The turbocharged-Git for Databases 🐆 (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jgv6vo/need_feedbacks_guepard_the_turbochargedgit_for/)**
*  **Summary:** This thread provides a link to the community open-source project showcase
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * You can find our open-source project showcase here: https://dataengineering.wiki/Community/Projects

**[🚀 Building the Perfect Data Stack: Complexity vs. Simplicity (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jh96k6/building_the_perfect_data_stack_complexity_vs/)**
*  **Summary:** This thread discusses the balance between complexity and simplicity when building a data stack.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Consider budget when building a data stack.
    * Most companies don’t need complicated realtime Kubernetes pipelines with petabyte scalability. Airbyte, DBT, and S3/Postgres are more than sufficient for most use cases.
    * What does PowerBI fetch?

**[Have You Heard of This Powerful Alternative to Requests in Python? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jhazl0/have_you_heard_of_this_powerful_alternative_to/)**
*  **Summary:** This thread discusses a powerful alternative to request in Python.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    * I'm not clicking some random blog, but I hope the powerful alternative to requests is called demands
    * Can we ban blog posts to medium specifically?
    * I've been using httpx for years.

**["vibe coding" how do we feel about that as data engineers (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jhc3fk/vibe_coding_how_do_we_feel_about_that_as_data/)**
*  **Summary:** This thread explores the concept of "vibe coding" (using AI to generate code) and its implications for data engineers.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    * "Vibe coding" is bad. After reviewing an LLM's output, a person should not copy and paste code until it meets some functional requirement.
    * The biggest advantage of vibe coding is the pace at which I am able to now learn new frameworks.
    * I believe vibe coding refers to people who have no idea what they're doing, asking LLM for stuff, and pasting code until it eventually meets some functional requirement. It is, generally a bad/*** thing to do.

