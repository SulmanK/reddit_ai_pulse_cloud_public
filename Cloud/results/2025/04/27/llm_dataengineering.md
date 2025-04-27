---
title: "Data Engineering Subreddit"
date: "2025-04-27"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Saved $30K+ in marketing ops budget by self-hosting Airbyte on Kubernetes: A real-world story](https://www.reddit.com/r/dataengineering/comments/1k92813/saved_30k_in_marketing_ops_budget_by_selfhosting/) (Score: 105)
    * The discussion revolves around the cost savings achieved by self-hosting Airbyte on Kubernetes for marketing operations.
2.  [How important is webscraping as a skill for Data Engineers?](https://www.reddit.com/r/dataengineering/comments/1k8ml01/how_important_is_webscraping_as_a_skill_for_data/) (Score: 35)
    * The conversation centers on the importance of web scraping as a skill for data engineers, with varying opinions on its relevance and alternatives.
3.  [Building Self-Optimizing ETL Pipelines, Has anyone tried real-time feedback loops?](https://www.reddit.com/r/dataengineering/comments/1k8ye1g/building_selfoptimizing_etl_pipelines_has_anyone/) (Score: 13)
    * The discussion is about building self-optimizing ETL pipelines and whether anyone has experience with real-time feedback loops.
4.  [General guidance - Docker/dagster/postgres ETL build](https://www.reddit.com/r/dataengineering/comments/1k93nf9/general_guidance_dockerdagsterpostgres_etl_build/) (Score: 12)
    * The conversation centers on building an ETL pipeline using Docker, Dagster, and Postgres, seeking general guidance and advice.
5.  [Backend table design of Dashboard](https://www.reddit.com/r/dataengineering/comments/1k9793r/backend_table_design_of_dashboard/) (Score: 9)
    * This thread discusses the backend table design considerations for creating dashboards.
6.  [How is data collected, processed, and stored to serve AI Agents and LLM-based applications? What does the typical data engineering stack look like?](https://www.reddit.com/r/dataengineering/comments/1k8xcjp/how_is_data_collected_processed_and_stored_to/) (Score: 8)
    * The thread explores the methods and technologies used for collecting, processing, and storing data to support AI agents and LLM-based applications.
7.  [Unit testing a function that creates a Delta table](https://www.reddit.com/r/dataengineering/comments/1k95pqd/unit_testing_a_function_that_creates_a_delta_table/) (Score: 5)
    * The discussion focuses on strategies and tools for unit testing functions that create Delta tables.
8.  [A New Reference Architecture for Change Data Capture (CDC)](https://estuary.dev/blog/new-reference-architecture-for-cdc/) (Score: 3)
    * This thread links to a blog post about CDC architecture, but receives criticism for being an SEO article lacking substance.
9.  [Does S3tables Catalog Support LF-Tags?](https://www.reddit.com/r/dataengineering/comments/1k9ahhp/does_s3tables_catalog_support_lftags/) (Score: 3)
    * This thread is asking whether S3tables Catalog Support LF-Tags.
10. [Looking for resources to learn real-world Data Engineering (SQL, PySpark, ETL, Glue, Redshift, etc.) - IK practice is the key](https://www.reddit.com/r/dataengineering/comments/1k9c8ul/looking_for_resources_to_learn_realworld_data/) (Score: 1)
    * The post is looking for resources for learning real world data engineering.
11. [I am developing AI Agent to replace ETL engineers and data model experts](https://www.reddit.com/r/dataengineering/comments/1k90562/i_am_developing_ai_agent_to_replace_etl_engineers/) (Score: 0)
    * This thread discusses the feasibility of using AI agents to replace ETL engineers and data model experts.

# Detailed Analysis by Thread
**[[D] Saved $30K+ in marketing ops budget by self-hosting Airbyte on Kubernetes: A real-world story (Score: 105)](https://www.reddit.com/r/dataengineering/comments/1k92813/saved_30k_in_marketing_ops_budget_by_selfhosting/)**
*  **Summary:** The original post highlights saving over $30,000 by self-hosting Airbyte on Kubernetes.  Commenters discuss their own Kubernetes implementations for ETL, the challenges of self-hosting, and the trend of cloud repatriation.
*  **Emotion:** Predominantly Positive. Many commenters express enthusiasm and interest in the cost-saving strategies presented, and offer congratulations. Some neutral sentiments expressed with people inquiring for tips.
*  **Top 3 Points of View:**
    * Self-hosting Airbyte on Kubernetes can lead to significant cost savings compared to managed services.
    * Kubernetes is a viable platform for deploying and managing ETL pipelines, though scaling may require tweaking.
    * Cloud repatriation is becoming more common as organizations seek to reduce costs and gain more control.

**[How important is webscraping as a skill for Data Engineers? (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1k8ml01/how_important_is_webscraping_as_a_skill_for_data/)**
*  **Summary:** The discussion centers on whether web scraping is a crucial skill for data engineers. Opinions vary, with some considering it an outdated practice while others find it necessary in specific industries or for personal projects. The use of APIs as a cleaner alternative is also mentioned.
*  **Emotion:** Mostly Neutral. The comments provide objective assessments of the relevance and challenges of web scraping.
*  **Top 3 Points of View:**
    * Web scraping is becoming less important as APIs and structured data sources become more prevalent.
    * Web scraping is essential in certain industries where accessing data requires it.
    * Accessing hidden or undocumented APIs is preferable to scraping whenever possible.

**[Building Self-Optimizing ETL Pipelines, Has anyone tried real-time feedback loops? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1k8ye1g/building_selfoptimizing_etl_pipelines_has_anyone/)**
*  **Summary:** This thread is about the challenges and benefits of implementing self-optimizing ETL pipelines using real-time feedback loops.  Commenters discuss the complexity of automated tuning and mention existing database features that offer similar optimization.
*  **Emotion:** Mostly Neutral. Comments give professional suggestions with an objective tone.
*  **Top 3 Points of View:**
    * Building self-optimizing ETL pipelines is complex because of high-dimensional state spaces and the difficulty of comparing results over time.
    * Automated tuning can be beneficial, particularly when applied across many pipelines.
    * Existing database systems already incorporate some level of real-time or adaptive optimization.

**[General guidance - Docker/dagster/postgres ETL build (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1k93nf9/general_guidance_dockerdagsterpostgres_etl_build/)**
*  **Summary:** The thread seeks guidance on building an ETL pipeline using Docker, Dagster, and Postgres. Commenters suggest alternatives like DuckDB, advise on security considerations, and recommend tools like Nginx for accessing the Dagster UI.
*  **Emotion:** Mostly Positive/Neutral. The overall tone is helpful and constructive, with commenters providing suggestions and advice.
*  **Top 3 Points of View:**
    * DuckDB can be a lighter-weight alternative to Postgres, especially for smaller data volumes.
    * Setting up a Docker/Dagster environment is worthwhile for its extensibility and maintainability.
    * Nginx should be added to the stack for security and UI access.

**[Backend table design of Dashboard (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1k9793r/backend_table_design_of_dashboard/)**
*  **Summary:** This thread discusses backend table design strategies for dashboards, recommending the use of multiple tables with different purposes (landing, fact & dim, mart, reporting).
*  **Emotion:** Mostly Neutral. The comments primarily focus on providing technical advice.
*  **Top 3 Points of View:**
    * Using multiple tables (landing, fact & dim, mart, reporting) is used to organize data with different purposes.

**[How is data collected, processed, and stored to serve AI Agents and LLM-based applications? What does the typical data engineering stack look like? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1k8xcjp/how_is_data_collected_processed_and_stored_to/)**
*  **Summary:** The thread discusses the data infrastructure needed to support AI Agents and LLM-based applications, emphasizing real-time data extraction, optimal data structures for retrieval (e.g., vector embeddings), and the use of tools like Postgres and Python for gluing everything together.
*  **Emotion:** Mostly Neutral. This thread mostly contains objective discussions.
*  **Top 3 Points of View:**
    * Data needs to be as close to real-time as possible to augment the context of LLMs.
    * The choice of tools and databases depends on the specific systems being connected, but OSS options like Postgres and Python are often sufficient.
    * Databricks provides a comprehensive set of tools, including delta lake and vector index tables.

**[Unit testing a function that creates a Delta table (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1k95pqd/unit_testing_a_function_that_creates_a_delta_table/)**
*  **Summary:** The discussion is about unit testing strategies for functions that create Delta tables, with suggestions including using pytest-mock, creating temporary catalogs and schemas for integration tests, and using PyTest fixtures.
*  **Emotion:** Mostly Neutral. The comments provide concrete, technical suggestions.
*  **Top 3 Points of View:**
    * Use pytest-mock for mocking dependencies.
    * Create temporary catalogs and schemas for integration testing.
    * Use PyTest fixtures to provide spark session objects.

**[A New Reference Architecture for Change Data Capture (CDC) (Score: 3)](https://estuary.dev/blog/new-reference-architecture-for-cdc/)**
*  **Summary:** This thread links to an article on CDC architecture, which received one comment saying the article has a misleading title.
*  **Emotion:** Mostly Negative. This thread contains a negative remark.
*  **Top 3 Points of View:**
    * This article has a misleading title.

**[Does S3tables Catalog Support LF-Tags? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k9ahhp/does_s3tables_catalog_support_lftags/)**
*  **Summary:** User is asking whether S3tables Catalog Support LF-Tags.
*  **Emotion:** Mostly Neutral. The response is a bot response with links.
*  **Top 3 Points of View:**
    * N/A (Only a bot response)

**[Looking for resources to learn real-world Data Engineering (SQL, PySpark, ETL, Glue, Redshift, etc.) - IK practice is the key (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k9c8ul/looking_for_resources_to_learn_realworld_data/)**
*  **Summary:** User is looking for resources to learn real world data engineering.
*  **Emotion:** Mostly Neutral. The responses are a bot response with links and a recommendation of Coursera.
*  **Top 3 Points of View:**
    * Take Data Engineering Specialization on Coursera.

**[I am developing AI Agent to replace ETL engineers and data model experts (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k90562/i_am_developing_ai_agent_to_replace_etl_engineers/)**
*  **Summary:** The thread discusses the feasibility of using AI agents to replace ETL engineers and data model experts. Most comments express skepticism, citing the complexity of real-world data engineering tasks.
*  **Emotion:** Mostly Neutral/Positive. While the initial post might be perceived as provocative, the comments are generally measured and constructive.
*  **Top 3 Points of View:**
    * AI may automate simple tasks, but can't handle changing requirements, ambiguous requirements, data quality issues.
    * It is premature to consider replacing ETL engineers with AI agents due to the complex, nuanced nature of the work.
    * Developing an AI agent to replace AI start up founders.
