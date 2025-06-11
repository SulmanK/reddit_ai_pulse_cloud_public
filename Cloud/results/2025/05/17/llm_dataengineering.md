---
title: "Data Engineering Subreddit"
date: "2025-05-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1. [[D] What are the major transformations done in the Gold layer of the Medallion Architecture?](https://www.reddit.com/r/dataengineering/comments/1kopm00/what_are_the_major_transformations_done_in_the/) (Score: 40)
    * Discussing the transformations performed in the Gold layer of the Medallion Architecture.

2. [What do “good requirements” look like?](https://www.reddit.com/r/dataengineering/s/qOqSmbFi9O) (Score: 22)
    *  Discussing the characteristics of good requirements in data engineering projects.

3. [Traditional ETL dev to data engineer](https://www.reddit.com/r/dataengineering/comments/1koqyra/traditional_etl_dev_to_data_engineer/) (Score: 14)
    * Discussing the transition from traditional ETL development to data engineering.

4. [Advice on Data Pipeline that Requires Individual API Calls](https://www.reddit.com/r/dataengineering/comments/1kotr7w/advice_on_data_pipeline_that_requires_individual/) (Score: 12)
    * Seeking advice on designing a data pipeline that requires individual API calls for each record.

5. [How do experienced data engineers handle unreliable manual data entry in source systems?](https://www.reddit.com/r/dataengineering/comments/1kouhgg/how_do_experienced_data_engineers_handle/) (Score: 12)
    * Discussing strategies for handling unreliable manual data entry in source systems.

6. [What are the newest technologies/libraries/methods in ETL Pipelines?](https://www.reddit.com/r/dataengineering/comments/1kozikh/what_are_the_newest_technologieslibrariesmethods/) (Score: 8)
    * Discussing new technologies, libraries, and methods in ETL pipelines.

7. [insert-tools — Python CLI for type-safe bulk data insertion into ClickHouse](https://github.com/castengine/insert-tools) (Score: 7)
    * A question about if you can insert data from Postgres to Clickhouse.

8. [What is the best strategy for using Duckdb in a read-simultaneous scenario?](https://www.reddit.com/r/dataengineering/comments/1kowycp/what_is_the_best_strategy_for_using_duckdb_in_a/) (Score: 7)
    * Asking for the best strategy for using DuckDB in a read-simultaneous scenario.

9. [Looking for someone to review Dagster-Dbt-Dlt-DuckDb Project](https://www.reddit.com/r/dataengineering/comments/1konlpi/looking_for_someone_to_review_dagsterdbtdltduckdb/) (Score: 5)
    * Seeking someone to review a project using Dagster, DBT, DLT, and DuckDB.

10. [Update existing facts?](https://www.reddit.com/r/dataengineering/comments/1kok80s/update_existing_facts/) (Score: 4)
    * Discussing strategies for updating existing facts in a data warehouse.

11. [Seeking Focused Learning Resources for Microsoft SQL Server Aligned with Azure Data Engineer Role](https://www.reddit.com/r/dataengineering/comments/1kolkci/seeking_focused_learning_resources_for_microsoft/) (Score: 1)
    * Asking for learning resources for Microsoft SQL Server.

12. [Demand for Talend](https://www.reddit.com/r/dataengineering/comments/1kopot4/demand_for_talend/) (Score: 1)
    * Discussing the demand for the Talend data integration tool.

13. [I made an RAG job matching website for tech jobs (Canada + US)](https://www.reddit.com/r/dataengineering/comments/1kovtwa/i_made_an_rag_job_matching_website_for_tech_jobs/) (Score: 1)
    * Sharing a RAG job matching website for tech jobs.

14. [Skills required for DE vs SWE?](https://www.reddit.com/r/dataengineering/comments/1koim5p/skills_required_for_de_vs_swe/) (Score: 0)
    * Discussing the skills required for a Data Engineer vs a Software Engineer.

15. [Question about pipelines](https://www.reddit.com/r/dataengineering/comments/1koywvx/question_about_pipelines/) (Score: 0)
    * A question about what a pipeline is.

16. [I feel so hopeless.](https://www.reddit.com/r/dataengineering/comments/1kp1ngh/i_feel_so_hopeless/) (Score: 0)
    * Someone expressing feeling hopeless.

# Detailed Analysis by Thread
**[ [D] What are the major transformations done in the Gold layer of the Medallion Architecture? (Score: 40)](https://www.reddit.com/r/dataengineering/comments/1kopm00/what_are_the_major_transformations_done_in_the/)**
*  **Summary:** The thread discusses the transformations performed in the Gold layer of the Medallion Architecture, including modeling data into star schema facts and dimensions tables, applying domain-specific business logic, creating facts, dimensions, aggregates, and denormalized reporting tables.
*  **Emotion:** The overall emotional tone is Neutral, with high sentiment scores indicating informative and objective discussions.
*  **Top 3 Points of View:**
    * The Gold layer involves modeling data into star schema facts and dimensions tables.
    * The Gold layer applies domain-specific business logic.
    * The Gold layer is the deliverable itself or directly feeds into it, focusing on business requirements.

**[What do “good requirements” look like? (Score: 22)](https://www.reddit.com/r/dataengineering/s/qOqSmbFi9O)**
*  **Summary:** The thread explores the characteristics of good requirements in data engineering, emphasizing clarity, essential outcomes, data contracts, and engagement with operations customers.
*  **Emotion:** The emotional tone is predominantly Neutral, with some comments expressing positive sentiment towards the importance of clear and well-defined requirements.
*  **Top 3 Points of View:**
    * Good requirements involve clarity of thinking around the actual problem to solve.
    * Good requirements involve clarity of thinking in terms of essential outcomes to target.
    * The data contract is the best document for communicating the requirement.

**[Traditional ETL dev to data engineer (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1koqyra/traditional_etl_dev_to_data_engineer/)**
*  **Summary:** This thread discusses the transition from traditional ETL development to data engineering, highlighting the importance of SQL skills and adaptability to new cloud technologies.
*  **Emotion:** The overall emotional tone is positive, with high sentiment scores reflecting encouragement and confidence in transitioning from ETL to data engineering.
*  **Top 3 Points of View:**
    *  Strong SQL skills are more valuable than experience with specific tools like DBT.
    * Data engineering is essentially the new name for ETL development.
    * Cloud knowledge is a bonus, but strong SQL and general data engineering knowledge are more important.

**[Advice on Data Pipeline that Requires Individual API Calls (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1kotr7w/advice_on_data_pipeline_that_requires_individual/)**
*  **Summary:** The thread seeks advice on designing a data pipeline that requires individual API calls for each of 20k records, discussing optimization strategies and considerations for API rate limits and error handling.
*  **Emotion:** The emotional tone is Neutral, providing practical advice and considerations for designing the data pipeline.
*  **Top 3 Points of View:**
    * Prioritize meeting SLAs and ensure API calls are free before optimizing for efficiency.
    * Consider parallelizing the API calls in multiple threads.
    * Filter each load to only retrieve new or updated rows.

**[How do experienced data engineers handle unreliable manual data entry in source systems? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1kouhgg/how_do_experienced_data_engineers_handle/)**
*  **Summary:** This thread discusses strategies for handling unreliable manual data entry in source systems, including upstream fixes, data cleaning, and stakeholder engagement.
*  **Emotion:** The emotional tone is Neutral, offering practical advice and emphasizing the importance of data quality and stakeholder collaboration.
*  **Top 3 Points of View:**
    * The best long-term solution is to improve data entry upstream by engaging with stakeholders.
    * Use the transform layer for light cleaning and quarantine malformed rows.
    * Data producers should own data quality.

**[What are the newest technologies/libraries/methods in ETL Pipelines? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1kozikh/what_are_the_newest_technologieslibrariesmethods/)**
*  **Summary:** The thread discusses new technologies, libraries, and methods in ETL pipelines, including Airbyte, Datastream, DataFlow, Dataform, Composer, Databricks delta lake, DuckDB, and connectorx.
*  **Emotion:** The emotional tone is Neutral, showcasing a range of technologies and tools used in modern ETL pipelines.
*  **Top 3 Points of View:**
    * Airbyte, Datastream, DataFlow, Dataform, and Composer are popular choices for ETL pipelines.
    * Databricks delta lake is gaining traction in many organizations.
    * DuckDB and connectorx are useful tools for local development and fast data connections.

**[insert-tools — Python CLI for type-safe bulk data insertion into ClickHouse (Score: 7)](https://github.com/castengine/insert-tools)**
*  **Summary:** The thread is about a python tool for bulk data insertion into ClickHouse.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A

**[What is the best strategy for using Duckdb in a read-simultaneous scenario? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kowycp/what_is_the_best_strategy_for_using_duckdb_in_a/)**
*  **Summary:** This thread asks for the best strategy for using DuckDB in a read-simultaneous scenario.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A

**[Looking for someone to review Dagster-Dbt-Dlt-DuckDb Project (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1konlpi/looking_for_someone_to_review_dagsterdbtdltduckdb/)**
*  **Summary:** Seeking someone to review a project using Dagster, DBT, DLT, and DuckDB.
*  **Emotion:** The emotional tone is Positive, with users expressing interest and willingness to help review the project.
*  **Top 3 Points of View:**
    * Many users are interested in reviewing the project and providing feedback.
    * Reviewers have extensive experience with GCP, DBT, and DLT.
    * Some reviewers lack experience with Dagster but are still willing to help.

**[Update existing facts? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1kok80s/update_existing_facts/)**
*  **Summary:** Discussing strategies for updating existing facts in a data warehouse.
*  **Emotion:** The emotional tone is Positive, with users providing solutions and suggestions.
*  **Top 3 Points of View:**
    * Use "delete + insert" for updating facts.
    * Implement Slowly Changing Dimension (SCD) Type II for historical tracking.
    * Consider using Delta/Iceberg for time travel capabilities.

**[Seeking Focused Learning Resources for Microsoft SQL Server Aligned with Azure Data Engineer Role (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kolkci/seeking_focused_learning_resources_for_microsoft/)**
*  **Summary:** Asking for learning resources for Microsoft SQL Server.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A

**[Demand for Talend (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kopot4/demand_for_talend/)**
*  **Summary:** Discussing the demand for the Talend data integration tool.
*  **Emotion:** The emotional tone is Positive, with users giving encouragement to still taking the job.
*  **Top 3 Points of View:**
    * Talend is an outdated product.
    * The tool doesn't matter as much as understanding the concepts.
    * Demand for Talend is low.

**[I made an RAG job matching website for tech jobs (Canada + US) (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kovtwa/i_made_an_rag_job_matching_website_for_tech_jobs/)**
*  **Summary:** Sharing a RAG job matching website for tech jobs.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A

**[Skills required for DE vs SWE? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1koim5p/skills_required_for_de_vs_swe/)**
*  **Summary:** Discussing the skills required for a Data Engineer vs a Software Engineer.
*  **Emotion:** The emotional tone is Positive.
*  **Top 3 Points of View:**
    * Software Engineer Data and Data Engineer are two different types of roles.
    * Software Engineer Data is more on the front end and focuses on business data needs.
    * Data Engineer is purely business focus thinking about the models that can be built around existing tables or data structures.

**[Question about pipelines (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1koywvx/question_about_pipelines/)**
*  **Summary:** A question about what a pipeline is.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A

**[I feel so hopeless. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kp1ngh/i_feel_so_hopeless/)**
*  **Summary:** Someone expressing feeling hopeless.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * N/A
