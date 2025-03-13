---
title: "Data Engineering Subreddit"
date: "2025-03-13"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Thoughts on dbt](https://www.reddit.com/r/dataengineering/comments/1jafpb3/thoughts_on_dbt/) (Score: 27)
    * Discussing thoughts and opinions on the dbt (data build tool), with some comparing it to SQLMesh and Snowflake tasks.
2.  [Optimizing SQL Queries: Understanding Execution Order for Performance Gains](https://www.reddit.com/r/dataengineering/comments/1ja89yp/optimizing_sql_queries_understanding_execution/) (Score: 24)
    * A discussion about SQL query optimization, focusing on execution order and indexing.
3.  [What types of data structures are typically asked about in data engineering interviews?](https://www.reddit.com/r/dataengineering/comments/1jafhx5/what_types_of_data_structures_are_typically_asked/) (Score: 6)
    * People are discussing the types of data structures that are asked about in data engineering interviews.
4.  [What do I absolutely need to know before working on Databricks?](https://www.reddit.com/r/dataengineering/comments/1ja8nq8/what_do_i_absolutely_need_to_know_before_working/) (Score: 5)
    * A discussion about the essential concepts and skills needed to work on Databricks, especially for someone transitioning from Talend.
5.  [I'll soon inherit a bunch of questionable pipelines. Advice for a smooth transition?](https://www.reddit.com/r/dataengineering/comments/1jaag0v/ill_soon_inherit_a_bunch_of_questionable/) (Score: 3)
    * Seeking advice on how to handle the transition of inheriting potentially problematic data pipelines.
6.  [Kafka with python](https://www.reddit.com/r/dataengineering/comments/1jaa83l/kafka_with_python/) (Score: 2)
    * A question about using Kafka with Python, including resources and best practices.
7.  [Building a very small backend logic fetching couple of APIs - need advice](https://www.reddit.com/r/dataengineering/comments/1jaakga/building_a_very_small_backend_logic_fetching/) (Score: 2)
    * Advice is sought on how to build a small backend logic to fetch a couple of APIs, including caching strategies.
8.  [Any one working on GEN AI with Data Engineering](https://www.reddit.com/r/dataengineering/comments/1jadwso/any_one_working_on_gen_ai_with_data_engineering/) (Score: 2)
    * Discussing the application of GenAI in data engineering, specifically for address standardization.
9.  [When to move from Django to Airflow](https://www.reddit.com/r/dataengineering/comments/1jak2hy/when_to_move_from_django_to_airflow/) (Score: 2)
    * Discussing the transition from Django to Airflow for data processing tasks.
10. [I need some advice and please don't tell me I am ***.](https://www.reddit.com/r/dataengineering/comments/1jafk03/i_need_some_advice_and_please_dont_tell_me_i_am/) (Score: 1)
    * Requesting advice, with the initial comment focusing on getting back unpaid salary.
11. [CI/CD Best Practices for Silver Layer and Gold Layer?](https://www.reddit.com/r/dataengineering/comments/1jaj9u6/cicd_best_practices_for_silver_layer_and_gold/) (Score: 1)
    * Asking for best practices for CI/CD in the context of data engineering silver and gold layers.
12. [Move from NoSQL db to a relational db model?](https://www.reddit.com/r/dataengineering/comments/1jakzxz/move_from_nosql_db_to_a_relational_db_model/) (Score: 0)
    * Seeking guidance on how to transition from a NoSQL database to a relational database model.

# Detailed Analysis by Thread
**[[D] Thoughts on dbt (Score: 27)](https://www.reddit.com/r/dataengineering/comments/1jafpb3/thoughts_on_dbt/)**
*  **Summary:**  The thread discusses thoughts and opinions on dbt, with comparisons to SQLMesh and Snowflake tasks. Users discuss the pros and cons of dbt, its scalability, and alternative tools.
*  **Emotion:** The overall emotional tone of the thread is Neutral. There's some positive sentiment when users describe the benefits of dbt, and negative sentiment when users point out limitations, but most comments are informative and objective.
*  **Top 3 Points of View:**
    *   dbt is a useful tool that scales well for both small and large organizations, especially when using dbt Core.
    *   SQLMesh is a potential alternative that addresses some of dbt's pain points, such as compilation time and dev environment support.
    *   Snowflake tasks might not fully replace dbt due to dbt's additional features like testing suites, reusable macros, and environment management.

**[Optimizing SQL Queries: Understanding Execution Order for Performance Gains (Score: 24)](https://www.reddit.com/r/dataengineering/comments/1ja89yp/optimizing_sql_queries_understanding_execution/)**
*  **Summary:** The thread discusses SQL query optimization, focusing on the execution order and indexing. Some users question the validity of the presented optimizations, suggesting they might be implementation-dependent or not applicable to columnar databases.
*  **Emotion:** The overall emotional tone of the thread is Neutral. Users are actively questioning and debating the claims made in the original post, leading to a constructive discussion.
*  **Top 3 Points of View:**
    *   The effectiveness of SQL optimization techniques depends on the type of database (OLTP vs. columnar) and implementation.
    *   The logical execution order might not always correlate with the physical execution order that determines performance.
    *   The "optimized" queries presented might not be equivalent to the original queries and could produce different results.

**[What types of data structures are typically asked about in data engineering interviews? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1jafhx5/what_types_of_data_structures_are_typically_asked/)**
*  **Summary:** This thread discusses the types of data structures that are asked about in data engineering interviews. The discussion emphasizes practical application over theoretical knowledge.
*  **Emotion:** The overall emotional tone is Neutral. The comments provide helpful insights and guidance in an objective manner.
*  **Top 3 Points of View:**
    *   Interviews focus on practical data structures like strings, lists, sets, dictionaries, queues, and hash tables.
    *   Understanding how to apply these structures to solve real-world engineering challenges is crucial.
    *   Theoretical deep dives into advanced structures are rare; a high-level understanding of their use cases is beneficial.

**[What do I absolutely need to know before working on Databricks? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ja8nq8/what_do_i_absolutely_need_to_know_before_working/)**
*  **Summary:** This thread discusses the essential concepts and skills needed to work on Databricks, especially for someone transitioning from Talend.
*  **Emotion:** The overall emotional tone of the thread is Neutral. Users offer practical advice and resources to help the original poster prepare for their new role.
*  **Top 3 Points of View:**
    *   Familiarity with the medallion architecture (bronze/silver/gold layers), Delta Lake table optimizations, and Spark's distributed computing model are essential.
    *   Understanding how ADF pipelines trigger Databricks notebooks/jobs and the basic authentication flow between services is crucial for Azure integration.
    *   Focusing on Spark SQL and optimization techniques like repartitioning and caching is important.

**[I'll soon inherit a bunch of questionable pipelines. Advice for a smooth transition? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jaag0v/ill_soon_inherit_a_bunch_of_questionable/)**
*  **Summary:** This thread seeks advice on how to handle the transition of inheriting potentially problematic data pipelines.
*  **Emotion:** The overall emotional tone of the thread is Neutral. Users offer practical advice and cautionary tales based on their experiences.
*  **Top 3 Points of View:**
    *   Document everything wrong with the pipelines and estimate the costs to fix it early on to avoid taking responsibility for pre-existing problems.
    *   Implement unit tests, integration tests, and data profiling tests to understand the existing functionality and ensure safe refactoring.
    *   Rewrite everything if necessary, especially if the existing pipelines are built on outdated or unreliable technologies.

**[Kafka with python (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jaa83l/kafka_with_python/)**
*  **Summary:** A question about using Kafka with Python, including resources and best practices.
*  **Emotion:** Neutral. The comments are informative and aim to provide helpful resources and guidance.
*  **Top 3 Points of View:**
    *   Reading and writing to Kafka with Python is straightforward using libraries like Confluent Kafka.
    *   It is important to focus on hands-on tutorials that use the `confluent-kafka-python` library.
    *   Building and maintaining Kafka service is part of DevOps/Infrastructure.

**[Building a very small backend logic fetching couple of APIs - need advice (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jaakga/building_a_very_small_backend_logic_fetching/)**
*  **Summary:** Advice is sought on how to build a small backend logic to fetch a couple of APIs, including caching strategies.
*  **Emotion:** Neutral. The comments offer helpful advice on caching and API management.
*  **Top 3 Points of View:**
    *   The caching method depends on the framework being used, e.g., `@st.cache_data` in Streamlit.
    *   For Python backends without built-in caching, consider using packages like `cachetools` or `requests_cache`.
    *   Caching decisions depend on how frequently the API dimensions change.

**[Any one working on GEN AI with Data Engineering (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jadwso/any_one_working_on_gen_ai_with_data_engineering/)**
*  **Summary:** Discussing the application of GenAI in data engineering, specifically for address standardization.
*  **Emotion:** Neutral. The comments are informative and focused on a specific use case.
*  **Top 3 Points of View:**
    *   GenAI can be used for address standardization.
    *   It works better than libpostal.
    *   Cost optimization is still needed.

**[When to move from Django to Airflow (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jak2hy/when_to_move_from_django_to_airflow/)**
*  **Summary:** Discussing the transition from Django to Airflow for data processing tasks.
*  **Emotion:** Neutral. The responses highlight the differences between Django and Airflow.
*  **Top 3 Points of View:**
    *   Django and Airflow are different tools for different problems.
    *   If current Django-based data tasks become problematic, it's time to separate them from the Django application.
    *   For small, repetitive tasks, Airflow might be overkill; consider Temporal or even Cron.

**[I need some advice and please don't tell me I am *** (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jafk03/i_need_some_advice_and_please_dont_tell_me_i_am/)**
*  **Summary:** Requesting advice, with the initial comment focusing on getting back unpaid salary.
*  **Emotion:** Neutral. The comments offer simple advice.
*  **Top 3 Points of View:**
    *   Focus on getting the unpaid salary that is owed.

**[CI/CD Best Practices for Silver Layer and Gold Layer? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jaj9u6/cicd_best_practices_for_silver_layer_and_gold/)**
*  **Summary:** Asking for best practices for CI/CD in the context of data engineering silver and gold layers.
*  **Emotion:** Neutral. The comments refer to existing resources and ask for further clarification.
*  **Top 3 Points of View:**
    *   Any CI/CD tool should work, not just GitHub.
    *   Focus on compilation and builds, linting, and testing models.
    *   Specify what aspects of the layers CI/CD is being applied to (e.g. Models, notebooks, etc.).

**[Move from NoSQL db to a relational db model? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jakzxz/move_from_nosql_db_to_a_relational_db_model/)**
*  **Summary:** Seeking guidance on how to transition from a NoSQL database to a relational database model.
*  **Emotion:** Positive. The comment offers advice.
*  **Top 3 Points of View:**
    *   Study data normalization.

