---
title: "Data Engineering Subreddit"
date: "2026-05-08"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
*   1. [[D] Linkedin Influencer posting in support of offshoring data engineering jobs](https://www.reddit.com/gallery/1t6qdas) (Score: 67)
    *   This thread discusses a LinkedIn influencer's post advocating for offshoring data engineering jobs, with users debating the cost-effectiveness and implications of such practices.
*   2. [[D] How are you centralizing knowledge/context from AI agents (like Claude Code)?](https://www.reddit.com/r/dataengineering/comments/1t6ttuz/how_are_you_centralizing_knowledgecontext_from_ai/) (Score: 30)
    *   Users share strategies and tools for organizing and centralizing knowledge and context from AI agents, focusing on practical implementations for teams.
*   3. [[D] Help …](https://www.reddit.com/r/dataengineering/comments/1t6uy3u/help/) (Score: 25)
    *   This discussion revolves around advice for aspiring data engineers, emphasizing the importance of fundamentals, learning core concepts, and not getting overwhelmed by the vast array of tools.
*   4. [[D] Where to see enterprise grade Airflow data pipeline?](https://www.reddit.com/r/dataengineering/comments/1t7581v/where_to_see_enterprise_grade_airflow_data/) (Score: 24)
    *   The thread focuses on the structure and best practices for enterprise-grade Airflow data pipelines, with users sharing their team's setups and advice on maintainability.
*   5. [[D] Leetcode for Data Engineering?](https://www.reddit.com/r/dataengineering/comments/1t7hqel/leetcode_for_data_engineering/) (Score: 11)
    *   This discussion provides recommendations for platforms and resources that offer Leetcode-style problems tailored for data engineering interviews.
*   6. [[D] PostgreSQL query on 60M-row JSONB table is slow - should I add expression indexes or move to a structured table?](https://www.reddit.com/r/dataengineering/comments/1t6zmee/postgresql_query_on_60mrow_jsonb_table_is_slow/) (Score: 6)
    *   Users are discussing performance issues with a large JSONB table in PostgreSQL and seeking advice on whether to use expression indexes or restructure the table.
*   7. [[D] What’s the most challenging part of maintaining data pipelines in production?](https://www.reddit.com/r/dataengineering/comments/1t743of/whats_the_most_challenging_part_of_maintaining/) (Score: 6)
    *   This thread delves into the difficulties of maintaining data pipelines in production, with participants highlighting challenges like documentation, naming, reliability, and silent failures.
*   8. [[D] Migrating from oracle to fabric](https://www.reddit.com/r/dataengineering/comments/1t6s7s8/migrating_from_oracle_to_fabric/) (Score: 5)
    *   The discussion centers on the decision-making process and potential implications of migrating from Oracle to Fabric, with users questioning the business case and offering cautionary advice.
*   9. [[D] Autonomous Iceberg Table Maintenance for Data Lakes](https://lakeops.dev/blog/autonomous-iceberg-table-maintenance) (Score: 4)
    *   This thread briefly touches upon the benefits of automated table maintenance for data lakes, referencing a blog post about autonomous Iceberg table maintenance.
*   10. [[D] Is there any way to limit loop iterations during Airflow DAG file parsing — not during task execution?](https://www.reddit.com/r/dataengineering/comments/1t7g5wr/is_there_any_way_to_limit_loop_iterations_during/) (Score: 4)
    *   Users are discussing ways to manage loop iterations during Airflow DAG file parsing to avoid performance issues, with suggestions ranging from using DagBundle to adjusting parsing times.
*   11. [[D] Simulating real-time flow from data sources](https://www.reddit.com/r/dataengineering/comments/1t6n1kt/simulating_realtime_flow_from_data_sources/) (Score: 2)
    *   The thread explores methods for simulating real-time data flow for testing and validation purposes, with suggestions on creating and injecting fake data.
*   12. [[D] Preserve your Claude, Codex, and Cursor sessions as high-value data assets](https://i.redd.it/9n2jk0939xzg1.png) (Score: 2)
    *   This post suggests treating AI sessions as valuable data assets for future AI agents.
*   13. [[D] Databricks managed tables and raw files](https://www.reddit.com/r/dataengineering/comments/1t7igzq/databricks_managed_tables_and_raw_files/) (Score: 2)
    *   The discussion clarifies the relationship between Databricks managed tables and raw files, explaining how underlying storage is structured and how to persist pre-delta raw files.
*   14. [[D] Salesforce plugin in GCP data fusion](https://www.reddit.com/r/dataengineering/comments/1t6ztoy/salesforce_plugin_in_gcp_data_fusion/) (Score: 1)
    *   Users are discussing challenges with a Salesforce plugin in GCP Data Fusion, particularly concerning API changes and authentication deprecations, and potential alternative solutions.
*   15. [[D] Does anyone have any experience automating data exports from a Chase business bank account?](https://www.reddit.com/r/dataengineering/comments/1t6oomx/does_anyone_have_any_experience_automating_data/) (Score: 1)
    *   This thread seeks advice on automating data exports from a Chase business bank account, with a suggestion to consider connecting to client accounting platforms instead of banking APIs.

# Detailed Analysis by Thread
**[ Linkedin Influencer posting in support of offshoring data engineering jobs (Score: 67)](https://www.reddit.com/gallery/1t6qdas)**
*   **Summary:** A LinkedIn influencer's post advocating for offshoring data engineering jobs has sparked a discussion about the cost implications, salary expectations for senior engineers in different regions, and the overall effectiveness and potential downsides of such strategies.
*   **Emotion:** The emotional tone is predominantly Neutral, with some tinges of skepticism and slight negativity expressed regarding the perceived quality and value of offshoring.
*   **Top 3 Points of View:**
    *   Some users question the claimed cost savings, stating that senior engineers in regions like Poland can command higher salaries than suggested.
    *   There's a sentiment that offshoring, while sometimes pursued by executives for perceived achievements and business trips, rarely works out "great" in practice.
    *   A perspective is offered by an "offshore data engineer" highlighting the complexities of the arrangement, including the role of middlemen, the importance of time zone overlap, and the reality that "you get what you pay for" often holds true, though they also express positive aspects of their experience.

**[ How are you centralizing knowledge/context from AI agents (like Claude Code)? (Score: 30)](https://www.reddit.com/r/dataengineering/comments/1t6ttuz/how_are_you_centralizing_knowledgecontext_from_ai/)**
*   **Summary:** This thread discusses various methods and tools for centralizing knowledge and context from AI agents like Claude Code, focusing on creating organized and accessible information for teams.
*   **Emotion:** The overall emotional tone is Neutral, with a practical and problem-solving focus. There are some Positive sentiments regarding successful implementations.
*   **Top 3 Points of View:**
    *   Several users suggest using personal knowledge management tools like Obsidian, often in conjunction with shared drives or Git repositories, to create a "llm-wiki" pattern.
    *   Strategies involving organizing knowledge into specific files like `SKILL.md` and `CLAUDE.md` within dedicated repositories are proposed to standardize AI behavior and store project architecture details.
    *   A key theme is the challenge of retrieval versus storage, with suggestions to use techniques like indexed headers or a centralized "ai-docs" repository with on-demand symlinking to manage context effectively.

**[ Help … (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1t6uy3u/help/)**
*   **Summary:** This discussion provides advice to individuals seeking guidance on becoming a data engineer, emphasizing foundational knowledge, practical application, and managing the perception of complexity.
*   **Emotion:** The emotional tone is largely Neutral, with elements of reassurance and encouragement. One comment expresses a Negative sentiment about feeling like a fraud, but frames it as a sign of professional growth.
*   **Top 3 Points of View:**
    *   A strong emphasis is placed on learning the fundamentals (Python, SQL) and core concepts (data warehousing, ETL/ELT, stream processing) rather than trying to master every tool.
    *   It's suggested that understanding the general purpose of different tool categories (orchestration, data modeling) and how to optimize SQL queries is more crucial than deep expertise in every single tool.
    *   The idea that "everyone feels like a fraud" and that embracing challenges and not knowing everything is a sign of professional growth and learning is shared.

**[ Where to see enterprise grade Airflow data pipeline? (Score: 24)](https://www.reddit.com/r/dataengineering/comments/1t7581v/where_to_see_enterprise_grade_airflow_data/)**
*   **Summary:** This thread discusses the structure and maintainability of enterprise-grade Airflow data pipelines, with participants sharing their team's repository structures and best practices for organization, consistency, and maintainability.
*   **Emotion:** The emotional tone is primarily Neutral, with a practical and informative exchange of ideas. Some comments express mild frustration or skepticism about what constitutes "enterprise grade."
*   **Top 3 Points of View:**
    *   A common approach shared is a structured repository organization, often involving `dags/`, `include/`, `plugins/`, and `tests/` directories, with variations in how DAGs are organized by domain or business unit.
    *   There's a strong consensus that maintainability is the biggest challenge in Airflow at scale, emphasizing consistency, clear ownership, separating business logic from DAG files, and robust logging, monitoring, and error handling.
    *   Several users recommend using tools like the Astro CLI for initial project setup and suggest defining clear standards and good internal documentation as being more important than strictly copying a specific GitHub repo structure.

**[ Leetcode for Data Engineering? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1t7hqel/leetcode_for_data_engineering/)**
*   **Summary:** This discussion offers recommendations for platforms and resources that provide practice problems similar to Leetcode but are more tailored to the types of questions encountered in data engineering interviews.
*   **Emotion:** The emotional tone is predominantly Neutral, with a helpful and informative exchange. There are some Positive sentiments towards the suggested resources.
*   **Top 3 Points of View:**
    *   DataLemur is recommended as a platform offering Leetcode-style problems specifically designed for data engineering interviews.
    *   Stratascratch is mentioned as a good resource with curated problem sets for data engineering practice.
    *   SQL-specific learning resources, like "SQL *** Mystery," are highlighted for making SQL learning more engaging and investigative.

**[ PostgreSQL query on 60M-row JSONB table is slow - should I add expression indexes or move to a structured table? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1t6zmee/postgresql_query_on_60mrow_jsonb_table_is_slow/)**
*   **Summary:** Users are discussing performance issues with a large JSONB table in PostgreSQL and seeking advice on optimizing queries, with a debate between using expression indexes versus migrating to a structured table.
*   **Emotion:** The emotional tone is Neutral, focused on technical problem-solving. Some comments express a cautionary tone about the anti-patterns of querying JSONB at scale.
*   **Top 3 Points of View:**
    *   The primary recommendation is to use expression indexes on frequently filtered JSONB paths to improve query performance without immediate restructuring.
    *   Several users suggest that for large data volumes, it's generally better to extract frequently queried fields into regular, indexed columns while keeping the JSONB blob for less accessed data.
    *   A recurring sentiment is that while JSONB can be queried, it's not ideal for heavily queried fields at scale, and a structured table or even a NoSQL solution might be more appropriate if a coherent, scalable model cannot be built with JSONB.

**[ What’s the most challenging part of maintaining data pipelines in production? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1t743of/whats_the_most_challenging_part_of_maintaining/)**
*   **Summary:** This thread explores the most challenging aspects of maintaining data pipelines in production, with participants highlighting issues beyond initial engineering, such as documentation, consistency, reliability, and dealing with evolving source systems.
*   **Emotion:** The emotional tone is Neutral, reflecting a shared understanding of the complexities of data pipeline maintenance. There are some Negative undertones related to the difficulties encountered.
*   **Top 3 Points of View:**
    *   Documentation is frequently cited as a major challenge, with its absence or poor quality significantly hindering maintenance.
    *   Maintaining reliability and consistency is crucial, especially ensuring data is correctly transformed and loaded after retries, often achieved through idempotent and stateless processes.
    *   Silent failures, where pipelines run without errors but produce incorrect data, are identified as a particularly insidious and difficult problem to monitor and resolve.

**[ Migrating from oracle to fabric (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1t6s7s8/migrating_from_oracle_to_fabric/)**
*   **Summary:** This discussion centers on the decision for companies to migrate from Oracle to cloud-native platforms like Fabric, with users questioning the business case and offering cautionary advice about the complexity and potential downsides.
*   **Emotion:** The emotional tone is mixed, with Neutral sentiments discussing the decision point, but also Negative sentiments expressed about the potential move being "from bad to worse."
*   **Top 3 Points of View:**
    *   Many companies are at a crossroads where Oracle's reliability is contrasted with its licensing costs, operational overhead, and ecosystem fragmentation, leading to pressure for cloud-native solutions.
    *   Some users express concern about the migration itself, with one comment directly stating, "From bad to worse," implying skepticism about Fabric as a superior alternative.
    *   Questions are raised about the fundamental impetus and business case driving such a migration, suggesting that careful consideration is needed before undertaking the process.

**[ Autonomous Iceberg Table Maintenance for Data Lakes (Score: 4)](https://lakeops.dev/blog/autonomous-iceberg-table-maintenance)**
*   **Summary:** This thread briefly discusses the benefits of automated table maintenance for data lakes, referencing a blog post and sharing personal experiences with manual compaction scripts being a "nightmare."
*   **Emotion:** The emotional tone is Neutral, with a shared sentiment against manual, burdensome maintenance tasks.
*   **Top 3 Points of View:**
    *   Manual compaction scripts are described as a "total nightmare" and something users do not want to "babysit forever."
    *   Automated maintenance is seen as the preferable approach if the overhead is not prohibitive.
    *   A question is posed about encountering "weird edge cases with partition evolution" when using automated maintenance.

**[ Is there any way to limit loop iterations during Airflow DAG file parsing — not during task execution? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1t7g5wr/is_there_any_way_to_limit_loop_iterations_during/)**
*   **Summary:** This thread discusses methods to limit loop iterations during the Airflow DAG file parsing phase, rather than during task execution, to prevent performance issues.
*   **Emotion:** The emotional tone is Neutral, focused on technical problem-solving and Airflow's design.
*   **Top 3 Points of View:**
    *   A suggestion is made to explore `DagBundle` and the possibility of writing custom `DagBundle` or `DagBag` in Airflow 2.
    *   One user suggests that the parsing behavior is by design and that unless it causes performance issues, users shouldn't worry too much, advising to adjust the parsing time if instant DAG updates aren't necessary.
    *   The idea of raising the default 30-second parsing timeout to a couple of minutes is offered as a way to avoid seeing DAG changes instantly after releases, especially if the number of DAGs is manageable.

**[ Simulating real-time flow from data sources (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1t6n1kt/simulating_realtime_flow_from_data_sources/)**
*   **Summary:** This discussion explores methods for simulating real-time data flow for testing, demos, and monitoring validation, with participants suggesting approaches like manually creating and injecting fake data.
*   **Emotion:** The emotional tone is mixed, with Neutral sentiments about the technical challenge and Positive sentiments about the interest and utility of realistic streaming simulation.
*   **Top 3 Points of View:**
    *   A practical approach suggested is to manually create fake data and push it through the pipeline at maximum expected throughput plus a buffer.
    *   The complexity of building synthetic flows that accurately preserve temporal behavior is acknowledged as a significant challenge for many teams.
    *   The idea of realistic streaming simulation is seen as an interesting and valuable concept for various use cases, including testing, demos, and monitoring validation.

**[ Preserve your Claude, Codex, and Cursor sessions as high-value data assets (Score: 2)](https://i.redd.it/9n2jk0939xzg1.png)**
*   **Summary:** This post suggests treating AI sessions with tools like Claude, Codex, and Cursor as valuable data assets, akin to a personal "ImageNet" for future AI agents.
*   **Emotion:** The emotional tone is Neutral, presenting an idea rather than a debate.
*   **Top 3 Points of View:**
    *   The core idea is to value and preserve AI interaction sessions as data.
    *   These preserved sessions are seen as a form of personal "ImageNet," implying a dataset for training or informing future AI models.
    *   The implication is that these sessions hold valuable context or knowledge that can be leveraged by AI agents.

**[ Databricks managed tables and raw files (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1t7igzq/databricks_managed_tables_and_raw_files/)**
*   **Summary:** This thread clarifies the distinction between Databricks managed tables and raw files, explaining how managed tables are structured and how to persist pre-delta raw files for auditing or consumption.
*   **Emotion:** The emotional tone is Neutral, providing technical explanations and clarifications.
*   **Top 3 Points of View:**
    *   Raw files are distinct from the files materialized into a managed Delta table, with Databricks structuring the underlying storage by linking Delta files and folders to UC schema and table GUIDs.
    *   Auditing managed Delta table files at a file level is generally not necessary as audits can typically be done via Databricks SQL and UC operations.
    *   To persist pre-delta raw files, they should be stored upstream in ADLS, and a UC volume can be created to link to this storage location for governable access within Databricks.

**[ Salesforce plugin in GCP data fusion (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1t6ztoy/salesforce_plugin_in_gcp_data_fusion/)**
*   **Summary:** This discussion addresses issues arising from a Salesforce plugin in GCP Data Fusion, particularly concerning API changes and authentication deprecations, with users suggesting alternative solutions and highlighting the operational impact of such changes.
*   **Emotion:** The emotional tone is predominantly Neutral, with a leaning towards caution and problem-solving. One comment expresses a Neutral sentiment about the seriousness of authentication deprecations.
*   **Top 3 Points of View:**
    *   It's suggested that the Salesforce plugin likely changed to use the API, and users may need to move to a Data Transfer Service (DTS) if the plugin is no longer compatible.
    *   Users advise finding alternative plugins that work with newer Salesforce APIs, with Fivetran mentioned as a potential connector provider, especially for smaller data volumes.
    *   A strong point is made that authentication deprecations in enterprise integrations can quickly become massive operational problems, and teams often underestimate the tight coupling of plugins until vendors change authentication requirements.

**[ Does anyone have any experience automating data exports from a Chase business bank account? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1t6oomx/does_anyone_have_any_experience_automating_data/)**
*   **Summary:** This thread seeks advice on automating data exports from a Chase business bank account, with a suggestion to consider connecting to client accounting platforms as a more streamlined and secure alternative to banking APIs.
*   **Emotion:** The emotional tone is Neutral, focusing on providing practical advice and alternative solutions.
*   **Top 3 Points of View:**
    *   A suggestion is made to connect to the clients' accounting platforms rather than attempting to use a banking system API.
    *   This approach is seen as potentially more streamlined and also avoids the need to pass authentication to sensitive source systems like bank accounts.
    *   The alternative of using accounting platform integrations is presented as a way to manage data exports more efficiently and securely.
