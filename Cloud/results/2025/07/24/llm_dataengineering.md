---
title: "Data Engineering Subreddit"
date: "2025-07-24"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Squashing down duplicate rows due to business rules on a code base with little data quality checks](https://i.redd.it/1uk8g6p6ztef1.jpeg) (Score: 52)
    * Discusses challenges and solutions for handling duplicate rows arising from business rules in a codebase with poor data quality checks.
2.  [Anyone running lightweight ad ETL pipelines without Airbyte or Fivetran?](https://www.reddit.com/r/dataengineering/comments/1m82tna/anyone_running_lightweight_ad_etl_pipelines/) (Score: 20)
    *  Users share their experiences and preferred tools for running lightweight ad ETL pipelines without using Airbyte or Fivetran, including custom scripts and SaaS solutions.
3.  [Re-learning Data Engineering](https://www.reddit.com/r/dataengineering/comments/1m7vjht/relearning_data_engineering/) (Score: 15)
    * Users share learning resources for data engineering, including community guides and YouTube channels.
4.  [ETL Unit Tests - how do you do it?](https://www.reddit.com/r/dataengineering/comments/1m84o0c/etl_unit_tests_how_do_you_do_it/) (Score: 12)
    *  Users discuss their approaches to ETL unit testing, covering topics like development environments, failure types, and testing frameworks.
5.  [Tool for interactive pipeline diagrams](https://v.redd.it/b2sqt6o0rtef1) (Score: 10)
    *  A user is available to answer questions about their tool for creating interactive pipeline diagrams.
6.  [Sample Data Warehouse for Testing](https://www.reddit.com/r/dataengineering/comments/1m82gsw/sample_data_warehouse_for_testing/) (Score: 9)
    *  A user shares a link to Microsoft's AdventureWorks sample data warehouse for testing purposes.
7.  [Liquibase best practices](https://www.reddit.com/r/dataengineering/comments/1m81i0v/liquibase_best_practices/) (Score: 7)
    *  Users discuss best practices for using Liquibase for database schema management, focusing on changeset structure and rollback strategies.
8.  [Modeling a Duplicate/Cojoined Dimension](https://www.reddit.com/r/dataengineering/comments/1m87w61/modeling_a_duplicatecojoined_dimension/) (Score: 6)
    *  Users discuss modeling a duplicate/cojoined dimension, with a focus on using surrogate keys and dimensional modeling benefits.
9.  [Hyparquet: The Quest for Instant Data](https://blog.hyperparam.app/2025/07/24/quest-for-instant-data/) (Score: 5)
    * A user shares their open-source library, Hyparquet, which is a Javascript Parquet loader.
10. [Holding Microsoft Accountable](https://www.trevornestor.com/post/microsoft-wants-me-to-be-afraid) (Score: 5)
    *  A user suggests contacting Amazon employees to find more people who feel similarly about Microsoft.
11. [RBAC and Alembic](https://www.reddit.com/r/dataengineering/comments/1m7x4xb/rbac_and_alembic/) (Score: 3)
    *  Users discuss how to manage RBAC changes using Alembic migration files.
12. [Connect dbt Semantic layer with Excel](https://www.reddit.com/r/dataengineering/comments/1m88jyz/connect_dbt_semantic_layer_with_excel/) (Score: 3)
    * A user recommends using Power BI and its "analyze in excel" button instead of trying to connect dbt Semantic Layer with Excel.
13. [Is it worth pursuing a second degree as a backup plan?](https://www.reddit.com/r/dataengineering/comments/1m88pvf/is_it_worth_pursuing_a_second_degree_as_a_backup/) (Score: 3)
    *  Users debate the value of pursuing a second degree as a backup plan in the data engineering field, considering opportunity cost and the value of practical experience.
14. [AI-Powered Data Engineering: My Stack for Faster, Smarter Analytics](https://estuary.dev/blog/ai-assisted-analytics-engineering/) (Score: 2)
    *  A user asks about the data size, CDC, and bottlenecks during the AI-powered data engineering process.
15. [What are the biggest challenges data engineers face when building pipelines on Snowflake?](https://www.reddit.com/r/dataengineering/comments/1m7tozt/what_are_the_biggest_challenges_data_engineers/) (Score: 2)
    *  Users discuss the challenges of building data pipelines on Snowflake, primarily focusing on cost management and data layout optimization.
16. [Any free game/wisdom?](https://www.reddit.com/r/dataengineering/comments/1m7yro7/any_free_gamewisdom/) (Score: 1)
    *  Users discuss the importance of business knowledge and holistic solutions for data engineers in certain companies.
17. [Data Simulating/Obfuscating For a Project](https://www.reddit.com/r/dataengineering/comments/1m7wg24/data_simulatingobfuscating_for_a_project/) (Score: 0)
    *  Users discuss creating datasets that mirror the structure of their real data, and the importance of generating realistic fake data to validate analysis logic and app performance.
18. [Live Report & Dashboard Generator - No Code, in less than 2 minutes](https://www.reddit.com/r/dataengineering/comments/1m8136d/live_report_dashboard_generator_no_code_in_less/) (Score: 0)
    *  Users discuss the need for specific information to provide actionable dashboards and the possibility of reinventing existing solutions.

# Detailed Analysis by Thread
**[Squashing down duplicate rows due to business rules on a code base with little data quality checks (Score: 52)](https://i.redd.it/1uk8g6p6ztef1.jpeg)**
*  **Summary:** The discussion revolves around the problem of handling duplicate rows resulting from business rules in a codebase that lacks data quality checks.
*  **Emotion:** The overall emotional tone is mostly Neutral, although some comments contain blunt or critical language.
*  **Top 3 Points of View:**
    *   The problem could stem from a lack of understanding of surrogate and business keys.
    *   This situation is a typical challenge in data engineering, requiring the ability to recreate incorrect values to match legacy reports.
    *   The issue might be a modeling problem, potentially requiring a redesign of the data warehouse.

**[Anyone running lightweight ad ETL pipelines without Airbyte or Fivetran? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1m82tna/anyone_running_lightweight_ad_etl_pipelines/)**
*  **Summary:** Users are sharing their experiences with setting up lightweight ad ETL pipelines without using tools like Airbyte or Fivetran, discussing various approaches and tools they have found effective.
*  **Emotion:** The overall emotional tone is Positive, with users sharing helpful suggestions and offering advice.
*  **Top 3 Points of View:**
    *   Writing custom Python scripts is a common approach, although keeping up with API changes can be challenging.
    *   Simpler SaaS solutions are preferred over Airbyte when orchestration isn't needed.
    *   Combinations of Python, cron, and cloud functions (like AWS Lambda) are popular choices for lightweight ETL.

**[Re-learning Data Engineering (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1m7vjht/relearning_data_engineering/)**
*  **Summary:** This thread focuses on resources for re-learning data engineering, with users and bots providing links to helpful guides and learning materials.
*  **Emotion:** The overall emotional tone is Neutral, with the focus on sharing informative links.
*  **Top 3 Points of View:**
    *   Data Engineering Wiki provides community-submitted learning resources.
    *   Ease with Data YouTube channel offers helpful content.
    *   There is a community guide available for transitioning into Data Engineering.

**[ETL Unit Tests - how do you do it? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1m84o0c/etl_unit_tests_how_do_you_do_it/)**
*  **Summary:** This thread asks about different methods for performing unit tests on ETL processes, and users share a few ways that they approach this.
*  **Emotion:** The overall emotional tone is Neutral, as people are simply sharing information.
*  **Top 3 Points of View:**
    *   Consider Write-Audit-Publish patterns for testing.
    *   Using a CI/CD pipeline and pytest can help.
    *   DBT can be used to add tests to sources.

**[Tool for interactive pipeline diagrams (Score: 10)](https://v.redd.it/b2sqt6o0rtef1)**
*  **Summary:** The post is advertising a tool for interactive pipeline diagrams, with the creator offering to answer questions.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The creator is open to answering any questions about the tool.

**[Sample Data Warehouse for Testing (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1m82gsw/sample_data_warehouse_for_testing/)**
*  **Summary:** A user is sharing a link to a sample data warehouse for testing purposes.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   AdventureWorks is a sample database developed by Microsoft that might be helpful.

**[Liquibase best practices (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m81i0v/liquibase_best_practices/)**
*  **Summary:** Users are asking and answering about Liquibase Best Practices.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Keep one change per changeset.
    *   createTable and createIndex should not be considered a single operation.
    *   Add a rollback for the trigger.

**[Modeling a Duplicate/Cojoined Dimension (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1m87w61/modeling_a_duplicatecojoined_dimension/)**
*  **Summary:** The post is asking for advice on how to model a duplicate dimension.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Surrogate keys that don't contribute to the grain of a fact are normal.
    *   The first option is likely the way to go.

**[Hyparquet: The Quest for Instant Data (Score: 5)](https://blog.hyperparam.app/2025/07/24/quest-for-instant-data/)**
*  **Summary:** The post is about a user's open-source library, Hyparquet, which is a Javascript Parquet loader.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Hyparquet is a faster Parquet loader in Javascript.

**[Holding Microsoft Accountable (Score: 5)](https://www.trevornestor.com/post/microsoft-wants-me-to-be-afraid)**
*  **Summary:** The post is about holding Microsoft accountable.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Contact Amazon employees.

**[RBAC and Alembic (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m7x4xb/rbac_and_alembic/)**
*  **Summary:** This is about RBAC and Alembic migrations.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   A good approach would be to create separate Alembic migration files specifically for RBAC changes.

**[Connect dbt Semantic layer with Excel (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m88jyz/connect_dbt_semantic_layer_with_excel/)**
*  **Summary:** A question is being asked about how to connect the dbt Semantic Layer to Excel, with the advice being to avoid using Excel in this instance.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Use PowerBI instead.

**[Is it worth pursuing a second degree as a backup plan? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m88pvf/is_it_worth_pursuing_a_second_degree_as_a_backup/)**
*  **Summary:** This thread is about whether or not pursuing a second degree as a backup plan is worth it.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Upskill on the job and use it, eventually segment in your career.
    *   Never have a backup plan, burn the boats 😤
    *   No unless a company paid for it. Too much opportunity + financial cost. You can’t plan for everything that’s just life.

**[AI-Powered Data Engineering: My Stack for Faster, Smarter Analytics (Score: 2)](https://estuary.dev/blog/ai-assisted-analytics-engineering/)**
*  **Summary:** A user is asking about the data size, CDC, and bottlenecks during the AI-powered data engineering process.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The person asking the question is curious.

**[What are the biggest challenges data engineers face when building pipelines on Snowflake? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m7tozt/what_are_the_biggest_challenges_data_engineers/)**
*  **Summary:** Users are discussing the biggest challenges of Snowflake.
*  **Emotion:** The overall emotional tone is slightly Positive, with users sharing helpful suggestions and offering advice.
*  **Top 3 Points of View:**
    *   Cost
    *   Cost management.
    *   Tuning Snowflake pipelines often means rethinking data layouts.

**[Any free game/wisdom? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1m7yro7/any_free_gamewisdom/)**
*  **Summary:** Users are discussing some of the biggest challenges facing Data Engineers.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Be prepared to learn a lot of business knowledge.
    *   Technical stuff is good
    *   Have a holistic approach

**[Data Simulating/Obfuscating For a Project (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1m7wg24/data_simulatingobfuscating_for_a_project/)**
*  **Summary:** Users are discussing the best practices for data simulation.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   They create a dataset that mirrors the structure of their real data.

**[Live Report & Dashboard Generator - No Code, in less than 2 minutes (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1m8136d/live_report_dashboard_generator_no_code_in_less/)**
*  **Summary:** Users are discussing the need for visibility in CRMs.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   There are people that have put all the effort into a working CRM that don’t already have visibility into the metrics they need to track.

