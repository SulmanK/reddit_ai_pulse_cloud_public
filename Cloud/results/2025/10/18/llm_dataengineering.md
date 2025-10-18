---
title: "Data Engineering Subreddit"
date: "2025-10-18"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Best approach to large joins](https://www.reddit.com/r/dataengineering/comments/1oa0bi3/best_approach_to_large_joins/) (Score: 21)
    *   Discussion revolves around the optimal strategies for performing large joins on tables containing billions of rows, with suggestions including distributed SQL engines, broadcast joins, and pre-aggregation techniques.

2.  [Late data arrival partitioning best practices](https://www.reddit.com/r/dataengineering/comments/1o9gfu5/late_data_arrival_partitioning_best_practices/) (Score: 18)
    *   The thread explores best practices for partitioning data when dealing with late data arrivals, emphasizing read patterns, data distribution, and the use of lakehouse formats like Iceberg for updates and merges.

3.  [Data Factory extraction techniques](https://www.reddit.com/r/dataengineering/comments/1o9q246/data_factory_extraction_techniques/) (Score: 11)
    *   Discussion on extraction techniques using Data Factory, particularly around the use of metadata tables, version control, and alternative metadata management tools.

4.  [Thoughts on databricks genie](https://www.reddit.com/r/dataengineering/comments/1o9x20y/thoughts_on_databricks_genie/) (Score: 7)
    *   Users share their thoughts on Databricks Genie, with opinions ranging from it being one of the worst Databricks products at launch to being solid with proper instructions and well-defined data.

5.  [Courses for dim and fact modelling](https://www.reddit.com/r/dataengineering/comments/1o9gtyi/courses_for_dim_and_fact_modelling/) (Score: 5)
    *   The thread discusses resources and courses for dimensional and fact modeling, with recommendations for the Kimball book, IBM Redbook, and discussions on industry certifications like DAMA-DMBOK.

6.  [How to convince my boss that table is the way to go](https://www.reddit.com/r/dataengineering/comments/1o9uqkv/how_to_convince_my_boss_that_table_is_the_way_to/) (Score: 5)
    *   The discussion centers on how to convince a boss that a table-based approach is better than creating custom metadata files, with suggestions including running a pilot project, inviting external experts, and demonstrating performance improvements.

7.  [How to deploy airflow project on EC2 instance using Terraform.](https://www.reddit.com/r/dataengineering/comments/1o9xi5u/how_to_deploy_airflow_project_on_ec2_instance/) (Score: 2)
    *   The post is about deploying an Airflow project on an EC2 instance using Terraform, with suggestions including using CI pipelines, Docker, and alternatives like AWS MWAA.

8.  [What is the right tool for running adhoc scripts (with some visibility)](https://www.reddit.com/r/dataengineering/comments/1oa26wu/what_is_the_right_tool_for_running_adhoc_scripts/) (Score: 2)
    *   This thread explores the best tools for running ad-hoc scripts with visibility, suggesting Dagster, Airflow, or a migrations repository with tracking in a database/S3.

# Detailed Analysis by Thread
**[Best approach to large joins (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1oa0bi3/best_approach_to_large_joins/)**
*  **Summary:** The thread discusses the best strategies for performing large joins on tables with 20 billion rows. Suggestions include using distributed SQL engines like Spark or Presto, employing broadcast joins in Trino, and pre-aggregating data before joining.
*  **Emotion:** The overall emotional tone is neutral, with a few comments leaning towards positive. The discussion is generally informative and solution-oriented.
*  **Top 3 Points of View:**
    *   Use a distributed SQL engine like Apache Spark or Presto.
    *   Utilize a broadcast join in Trino with correct partitioning.
    *   Aggregate each dataset as much as possible before joining.

**[Late data arrival partitioning best practices (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1o9gfu5/late_data_arrival_partitioning_best_practices/)**
*  **Summary:** The thread is about the best practices for partitioning data when dealing with late data arrivals. It emphasizes read patterns, data distribution, and considering deployment/compute sizing. The use of lakehouse formats like Iceberg for updates and merges is also discussed.
*  **Emotion:** The overall emotional tone is neutral. The discussion is focused on providing practical advice and best practices.
*  **Top 3 Points of View:**
    *   Partitioning should be approached with a focus on read patterns and data distribution.
    *   Use a lakehouse format like Iceberg for updates and merges if immutable bronze data is not required.
    *   Partition by reception date, then repartition by event date, and finally handle versioning.

**[Data Factory extraction techniques (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1o9q246/data_factory_extraction_techniques/)**
*  **Summary:** The discussion is about extraction techniques using Data Factory, particularly the use of metadata tables. Concerns about the risks of using metadata tables in SQL, especially if not version-controlled, are raised. Alternative metadata management tools are suggested.
*  **Emotion:** The overall emotional tone is neutral. The discussion is focused on identifying risks and offering alternative solutions.
*  **Top 3 Points of View:**
    *   Metadata tables in SQL can be risky if not version-controlled.
    *   Consider using a more robust metadata management tool.
    *   Copy the table as a file which contains all the metadata you need.

**[Thoughts on databricks genie (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1o9x20y/thoughts_on_databricks_genie/)**
*  **Summary:** The thread discusses users' opinions on Databricks Genie. Some users consider it one of the worst Databricks products at launch, while others find it solid with proper instructions and well-defined data. The issue of GenAI hallucination is also mentioned.
*  **Emotion:** The overall emotional tone is mixed, with some comments being positive and others being critical.
*  **Top 3 Points of View:**
    *   Databricks Genie is one of the worst Databricks products at launch.
    *   Databricks Genie is solid with proper instructions and well-defined data.
    *   GenAI hallucination is a real issue that needs to be checked.

**[Courses for dim and fact modelling (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1o9gtyi/courses_for_dim_and_fact_modelling/)**
*  **Summary:** The thread discusses resources and courses for dimensional and fact modeling. The Kimball book and the IBM Redbook are recommended. There is also a discussion on industry certifications like DAMA-DMBOK.
*  **Emotion:** The overall emotional tone is neutral to positive, with people sharing helpful resources.
*  **Top 3 Points of View:**
    *   Read the Kimball book.
    *   The IBM Redbook on Dimensional Modeling is good.
    *   Consider Inmon in addition to Kimball for data warehousing.

**[How to convince my boss that table is the way to go (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1o9uqkv/how_to_convince_my_boss_that_table_is_the_way_to/)**
*  **Summary:** The discussion is about how to convince a boss that a table-based approach is better than creating custom metadata files. Suggestions include running a pilot project, inviting external experts, and demonstrating performance improvements.
*  **Emotion:** The overall emotional tone is neutral, with a hint of frustration in some comments related to dealing with the boss.
*  **Top 3 Points of View:**
    *   Run a pilot project to compare both approaches.
    *   Invite external experts to provide an unbiased opinion.
    *   Demonstrate performance improvements with the table-based solution.

**[How to deploy airflow project on EC2 instance using Terraform. (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1o9xi5u/how_to_deploy_airflow_project_on_ec2_instance/)**
*  **Summary:** The post seeks advice on deploying an Airflow project on an EC2 instance using Terraform. Suggestions include using CI pipelines, Docker, and alternatives like AWS MWAA.
*  **Emotion:** The overall emotional tone is neutral, with helpful suggestions and resources.
*  **Top 3 Points of View:**
    *   Use CI pipelines, Docker, and ECR for deployment.
    *   Use a user-data script to download and install the project on EC2 during startup.
    *   Consider using AWS MWAA instead.

**[What is the right tool for running adhoc scripts (with some visibility) (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oa26wu/what_is_the_right_tool_for_running_adhoc_scripts/)**
*  **Summary:** This thread explores the best tools for running ad-hoc scripts with visibility, suggesting Dagster, Airflow, or a migrations repository with tracking in a database/S3.
*  **Emotion:** The overall emotional tone is neutral and informative.
*  **Top 3 Points of View:**
    *   Dagster could work, providing good visibility and logging.
    *   Use a migrations repo and track execution in database/S3.
    *   Consider Airflow or Glue, but they may be overkill for adhoc tasks.
