---
title: "Data Engineering Subreddit"
date: "2025-03-26"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "kafka", "snowflake"]
---

# Overall Ranking and Top Discussions
1. [[D] What is the point of learning Kafka if I don't work with Microservices?](https://www.reddit.com/r/dataengineering/comments/1jkb38n/what_is_the_point_of_learning_kafka_if_i_dont/) (Score: 22)
    * This thread discusses the value of learning Kafka for data engineers who don't work with microservices, with various opinions on its necessity and use cases.
2. [Big tech companies using snowflake, dbt and airflow?](https://www.reddit.com/r/dataengineering/comments/1jkha69/big_tech_companies_using_snowflake_dbt_and_airflow/) (Score: 20)
    * This thread explores whether big tech companies utilize tools like Snowflake, DBT, and Airflow, considering their capacity to build in-house solutions.
3. [Medallion Architecture for Spatial Data](https://www.reddit.com/r/dataengineering/comments/1jkdbwc/medallion_architecture_for_spatial_data/) (Score: 11)
    * This thread is about Medallion architecture for spatial data
4. [Looking for intermediate/advanced blogs on optimizing sql queries](https://www.reddit.com/r/dataengineering/comments/1jkg5z4/looking_for_intermediateadvanced_blogs_on/) (Score: 11)
    * A user is looking for resources about SQL query optimization.
5. [Is it normal to do interviews without job searching?](https://www.reddit.com/r/dataengineering/comments/1jkbs8o/is_it_normal_to_do_interviews_without_job/) (Score: 10)
    *  The discussion revolves around the practice of interviewing for jobs even when not actively seeking a new position.
6. [BigQuery vs. BigQuery External Tables (Apache Iceberg) for Complex Queries – Which is Better?](https://www.reddit.com/r/dataengineering/comments/1jka8r3/bigquery_vs_bigquery_external_tables_apache/) (Score: 8)
    *  This thread compares the performance and cost-effectiveness of using native BigQuery versus BigQuery External Tables with Apache Iceberg for complex queries on large datasets.
7. [Need to Solidify My Self-Taught Data Engineering Skills - $2000 Budget, What's Your Top Pick?](https://www.reddit.com/r/dataengineering/comments/1jk82z1/need_to_solidify_my_selftaught_data_engineering/) (Score: 7)
    * A self-taught data engineer is seeking advice on how to best use a $2000 budget to improve their skills.
8. [Informatica ETL lineage/logic harvester](https://www.reddit.com/r/dataengineering/comments/1jke6if/informatica_etl_lineagelogic_harvester/) (Score: 3)
    * This thread is about Informatica ETL lineage/logic harvester
9. [Data Consolidation and Visualization](https://www.reddit.com/r/dataengineering/comments/1jkew8w/data_consolidation_and_visualization/) (Score: 3)
    * This thread discusses data consolidation and visualization.
10. [BigQuery Stored Procedure v.s. Dataform](https://www.reddit.com/r/dataengineering/comments/1jkckbb/bigquery_stored_procedure_vs_dataform/) (Score: 2)
    * A user asks when to use BigQuery Stored Procedures instead of Dataform
11. [Best Cloud Certifications for a Beginner (AWS, GCP, or Azure) to Help Land My First Job in the USA or Europe?](https://www.reddit.com/r/dataengineering/comments/1jkjcxs/best_cloud_certifications_for_a_beginner_aws_gcp/) (Score: 2)
    * A beginner is asking for advice about which cloud certifications would be best for them to get a job.
12. [Autoscaling of systems for data engineering](https://www.reddit.com/r/dataengineering/comments/1jkju0e/autoscaling_of_systems_for_data_engineering/) (Score: 2)
    * This thread discusses autoscaling of systems for data engineering.
13. [Data Engineering Project with free tools](https://www.reddit.com/r/dataengineering/comments/1jkgajq/data_engineering_project_with_free_tools/) (Score: 1)
    * A user is asking about free tools to use for a data engineering project.
14. [Scheduled SQL code best practice question](https://www.reddit.com/r/dataengineering/comments/1jkhno1/scheduled_sql_code_best_practice_question/) (Score: 1)
    *  This thread discusses best practices for scheduling SQL code execution.
15. [Stuck After 2 Years as a Contract Consultant – No PF, No Docs, Fired for Speaking Up. Help!](https://www.reddit.com/r/dataengineering/comments/1jkhsi7/stuck_after_2_years_as_a_contract_consultant_no/) (Score: 0)
    * A user is asking for help after being fired for speaking up.

# Detailed Analysis by Thread
**[[D] What is the point of learning Kafka if I don't work with Microservices? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1jkb38n/what_is_the_point_of_learning_kafka_if_i_dont/)**
*  **Summary:** The discussion revolves around the value of learning Kafka for data engineers who don't work with microservices.  Some argue Kafka is overhyped for many applications, while others point out its utility in tracking events, ETL/ELT processes, and as an "unbounded table."  The relevance of Kafka Connect and Debezium is also mentioned.
*  **Emotion:** The overall emotional tone is Neutral, with most comments having a neutral sentiment.
*  **Top 3 Points of View:**
    * Kafka is not always necessary and can be overkill for many pipelines, especially outside of large tech companies.
    *  Kafka is valuable for tracking events and can be useful even without microservices, particularly in the context of Kappa architecture and ETL/ELT processes.
    *  The depth of Kafka knowledge required depends on the role; some engineers only need a basic understanding for interacting with it, while others require deeper expertise for deployment and maintenance.

**[Big tech companies using snowflake, dbt and airflow? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1jkha69/big_tech_companies_using_snowflake_dbt_and_airflow/)**
*  **Summary:** This thread explores whether big tech companies utilize tools like Snowflake, DBT, and Airflow, considering their capacity to build in-house solutions.  The discussion includes confirmations of some big tech companies using Snowflake, mentions of in-house tools mirroring open-source architectures, and debates on the cost-effectiveness of using SaaS solutions versus building internal tools.
*  **Emotion:** The overall emotional tone is primarily Neutral, though there are also positive sentiments expressed regarding the usefulness and adoption of these technologies.
*  **Top 3 Points of View:**
    * Big tech companies often leverage a mix of in-house built tools and SaaS/PaaS solutions like Snowflake, DBT, and Airflow, using them for specific parts of their infrastructure.
    * While many large companies have the resources to build internal tools, using open-source or commercial products can be more cost-effective, particularly for data warehousing.
    *  In-house tools in big tech companies often mirror open-source architectures in spirit, and teams may prototype using open-source tools before scaling in-house.

**[Medallion Architecture for Spatial Data (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1jkdbwc/medallion_architecture_for_spatial_data/)**
*  **Summary:** The discussion centers around the application of the Medallion Architecture (also known as the 3-layer model) to spatial data. It involves clarification of the layers - staging, core (silver), and semantic (gold) - with emphasis on where transformation and processing should occur (between layers) versus the contents of each layer (deduped data with surrogate keys in core, data products in semantic).
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  "Medallion architecture" is a marketing term for the 3 layer model. The layers are: staging, core and semantic. The semantic layer is where the majority of data consumption happens.
    *  Core (silver) layer should contain deduped data with surrogate keys, not the processing steps themselves.
    *  The architecture can have more than one layer per level.

**[Looking for intermediate/advanced blogs on optimizing sql queries (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1jkg5z4/looking_for_intermediateadvanced_blogs_on/)**
*  **Summary:** A user is looking for resources about SQL query optimization. The advice given centers around understanding the specific database being used, testing different optimization approaches, and knowing the query planner.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Focus on optimization best practices for the specific database being used.
    * Test different optimization approaches and examine the query profile.
    * Become familiar with the database's query planner.

**[Is it normal to do interviews without job searching? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1jkbs8o/is_it_normal_to_do_interviews_without_job/)**
*  **Summary:** The discussion revolves around the practice of interviewing for jobs even when not actively seeking a new position. The main points cover the benefits of such practice for skill enhancement, market awareness, and potential unexpected opportunities, while also cautioning about the risk of burning bridges with recruiters.
*  **Emotion:** The overall emotional tone is slightly Positive, with users highlighting the advantages of the practice.
*  **Top 3 Points of View:**
    * Interviewing without actively job searching is a good way to practice interview skills, build confidence, and assess one's market value.
    *  It can lead to unexpected job opportunities even when not actively looking.
    *  There's a risk of burning bridges with recruiters if one is perceived as insincere.

**[BigQuery vs. BigQuery External Tables (Apache Iceberg) for Complex Queries – Which is Better? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1jka8r3/bigquery_vs_bigquery_external_tables_apache/)**
*  **Summary:**  This thread compares the performance and cost-effectiveness of using native BigQuery versus BigQuery External Tables with Apache Iceberg for complex queries on large datasets. It highlights BigQuery's optimized analytical workloads and performance tricks, while Iceberg offers cost efficiency and schema evolution capabilities. The conclusion emphasizes that the choice depends on specific use cases and query patterns.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  Native BigQuery is optimized for complex analytics and performs better for frequently queried data.
    *  BigQuery External Tables with Iceberg are more cost-effective for large datasets not frequently queried and offer schema flexibility.
    *  The ideal choice depends on the specific use case and query patterns.

**[Need to Solidify My Self-Taught Data Engineering Skills - $2000 Budget, What's Your Top Pick? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jk82z1/need_to_solidify_my_selftaught_data_engineering/)**
*  **Summary:** A self-taught data engineer is seeking advice on how to best use a $2000 budget to improve their skills. The suggestions include enrolling in a DE bootcamp, focusing on data modeling, earning cloud certifications, and exploring community-submitted learning resources.
*  **Emotion:** The overall emotional tone is Neutral to Positive, reflecting helpful and encouraging advice.
*  **Top 3 Points of View:**
    * Investing in a structured program such as a DE bootcamp.
    * Focusing on foundational knowledge like data modeling.
    *  Pursuing relevant cloud certifications.

**[Informatica ETL lineage/logic harvester (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jke6if/informatica_etl_lineagelogic_harvester/)**
*  **Summary:** This thread is about Informatica ETL lineage/logic harvester. Users suggest utilizing Informatica's own lineage tool or metadata API.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Use Informatica's lineage tool.
    * Use Informatica's own metadata API.
    * There are no open source tools that can do Informatica's ETL solutions.

**[Data Consolidation and Visualization (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jkew8w/data_consolidation_and_visualization/)**
*  **Summary:** This thread discusses data consolidation and visualization.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Point of View:**
    * You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[BigQuery Stored Procedure v.s. Dataform (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jkckbb/bigquery_stored_procedure_vs_dataform/)**
*  **Summary:** A user asks when to use BigQuery Stored Procedures instead of Dataform. Users suggest that if Airflow and GitLab are already handling orchestration and versioning, stored procedures are sufficient.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    * Stored Procedures are sufficient if Airflow/GitLab handle orchestration/versioning.
    * Dataform's extras are redundant in a setup where Airflow and GitLab are already in use.

**[Best Cloud Certifications for a Beginner (AWS, GCP, or Azure) to Help Land My First Job in the USA or Europe? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jkjcxs/best_cloud_certifications_for_a_beginner_aws_gcp/)**
*  **Summary:** A beginner is asking for advice about which cloud certifications would be best for them to get a job.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Point of View:**
    * Choose Azure or AWS and aim for foundational or entry-friendly certs.

**[Autoscaling of systems for data engineering (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jkju0e/autoscaling_of_systems_for_data_engineering/)**
*  **Summary:** This thread discusses autoscaling of systems for data engineering.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Point of View:**
    * You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[Data Engineering Project with free tools (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jkgajq/data_engineering_project_with_free_tools/)**
*  **Summary:** A user is asking about free tools to use for a data engineering project.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 1 Point of View:**
    * Use SQL Server with the SSIS module

**[Scheduled SQL code best practice question (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jkhno1/scheduled_sql_code_best_practice_question/)**
*  **Summary:**  This thread discusses best practices for scheduling SQL code execution.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    *  It's an elegant solution to a workflow problem or sequence of SQLs to be executed
    *  It's a crazy hack to make an RDBMS do the job of Airflow.

**[Stuck After 2 Years as a Contract Consultant – No PF, No Docs, Fired for Speaking Up. Help! (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jkhsi7/stuck_after_2_years_as_a_contract_consultant_no/)**
*   **Summary:** A user is asking for help after being fired for speaking up.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 2 Points of View:**
    *  PF is not a normal term
    * this sounds like something specific to your country (india?) or at least not how US jobs work.
