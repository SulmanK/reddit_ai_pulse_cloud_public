---
title: "Data Engineering Subreddit"
date: "2025-02-25"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Why we're building for on-prem](https://www.reddit.com/r/dataengineering/comments/1ixvltu/why_were_building_for_onprem/) (Score: 38)
    * Discusses the reasons for choosing on-premise solutions, specifically focusing on Clickhouse's performance, challenges with cloud services like EBS, and legacy system integration.
2.  [Our Journey with LLMs and Data Warehousing: Practical Insights and Lessons Learned](https://www.reddit.com/r/dataengineering/comments/1ixwoz2/our_journey_with_llms_and_data_warehousing/) (Score: 9)
    *  Discusses the application of Large Language Models (LLMs) in data warehousing, including their use in replacing QA functions for junior engineers and their helpfulness with data dictionaries and cataloging.
3.  [Semantic layer - what’s automated vs user specified?](https://www.reddit.com/r/dataengineering/comments/1iy0bhz/semantic_layer_whats_automated_vs_user_specified/) (Score: 9)
    * Discusses the role of a semantic layer in data management, including the balance between automation and user specification.
4.  [Lost job in layoffs](https://www.reddit.com/r/dataengineering/comments/1iy3efc/lost_job_in_layoffs/) (Score: 8)
    *  Users discuss job searching after layoffs, suggesting strategies like applying directly on company websites, and asking about the job market and years of experience.
5.  [Install Apache Ranger on Kubernetes](https://www.reddit.com/r/dataengineering/comments/1iy2urh/install_apache_ranger_on_kubernetes/) (Score: 6)
    * Discusses the installation of Apache Ranger on Kubernetes, including the use of Helm charts, backend database setup, and configuration management.
6.  [Udemy Best DE Course(s) or Instructor(s)](https://www.reddit.com/r/dataengineering/comments/1ixxj14/udemy_best_de_courses_or_instructors/) (Score: 3)
    * Seeking recommendations for the best Udemy courses or instructors for data engineering.
7.  [Self-learning and collaboration shortage](https://www.reddit.com/r/dataengineering/comments/1iy4otf/selflearning_and_collaboration_shortage/) (Score: 3)
    * Discusses challenges and resources related to self-learning and collaboration in data engineering.
8.  [Apache Airflow for DevOps and IaC?](https://www.reddit.com/r/dataengineering/comments/1iy4rya/apache_airflow_for_devops_and_iac/) (Score: 3)
    * Discusses using Apache Airflow for DevOps and Infrastructure as Code (IaC).
9.  [Help with Airbyte Google BigQuery destination.](https://www.reddit.com/r/dataengineering/comments/1ixx534/help_with_airbyte_google_bigquery_destination/) (Score: 1)
    *  Asks for help with configuring Airbyte to work with Google BigQuery, specifically related to the destination setup.
10. [Courses about data transformations](https://www.reddit.com/r/dataengineering/comments/1ixyhkd/courses_about_data_transformations/) (Score: 1)
    *  Asks for course recommendations on the topic of data transformations.
11. [Fastest way to pivot large dataset on many columns dynamically?](https://www.reddit.com/r/dataengineering/comments/1iy2bmc/fastest_way_to_pivot_large_dataset_on_many/) (Score: 1)
    *  Seeks advice on the most efficient method to pivot a large dataset dynamically across multiple columns.
12. [Can anyone tell me what tool was used to produced this architecture diagram?](https://www.reddit.com/r/dataengineering/comments/1iy3z19/can_anyone_tell_me_what_tool_was_used_to_produced/) (Score: 1)
    *  Asks for identification of the tool used to create a specific architecture diagram.
13. [Miscrosoft Fabric or Snowflake. Choosing the Right Solution](https://www.reddit.com/r/dataengineering/comments/1iy4eeg/miscrosoft_fabric_or_snowflake_choosing_the_right/) (Score: 1)
    *  Discusses and compares Microsoft Fabric and Snowflake to determine which is the right solution for a given use case.

# Detailed Analysis by Thread
**[Why we're building for on-prem (Score: 38)](https://www.reddit.com/r/dataengineering/comments/1ixvltu/why_were_building_for_onprem/)**
*  **Summary:** This thread discusses the rationale behind choosing on-premise data solutions over cloud-based alternatives. It highlights the performance of Clickhouse, challenges faced with cloud services like EBS, and considerations for integrating with legacy systems.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Clickhouse is performant for scaling and query performance.
    * Cloud services (specifically EBS) can have data loss issues and logging complexities.
    * Lakehouse architecture on-premise, using open table formats like Apache Iceberg, is a viable alternative.

**[Our Journey with LLMs and Data Warehousing: Practical Insights and Lessons Learned (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1ixwoz2/our_journey_with_llms_and_data_warehousing/)**
*  **Summary:** This thread explores the use of Large Language Models (LLMs) in data warehousing, including their application in replacing QA functions and enhancing data dictionaries.
*  **Emotion:** Neutral, with a hint of Positive
*  **Top 3 Points of View:**
    * LLMs can be helpful in replacing QA functions, especially for junior engineers.
    * LLMs are beneficial for data dictionaries and cataloging.
    * The thread links to external learning resources for data engineering.

**[Semantic layer - what’s automated vs user specified? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1iy0bhz/semantic_layer_whats_automated_vs_user_specified/)**
*  **Summary:** This thread explores the concept of a semantic layer in data management, focusing on the balance between automated processes and user-defined specifications.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * A semantic layer translates agnostic data calls into SQL queries based on user-defined metadata.
    * AI can assist in defining metadata, but human oversight is necessary.
    * The semantic layer is closely tied to business needs and requires proper access control.

**[Lost job in layoffs (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1iy3efc/lost_job_in_layoffs/)**
*  **Summary:** Users discuss job searching after layoffs, suggesting strategies and asking about the job market.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Apply directly on company websites instead of relying on job boards.
    * Inquire about the job market in specific locations (e.g., US).
    * Years of experience is a relevant factor in job searching.

**[Install Apache Ranger on Kubernetes (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1iy2urh/install_apache_ranger_on_kubernetes/)**
*  **Summary:** Discusses the setup of Apache Ranger on Kubernetes, including the use of Helm charts and database configuration.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Helm charts are a good starting point for installing Apache Ranger on Kubernetes.
    * PostgreSQL is a suitable backend database.
    * Open Policy Agent (OPA) is another option to consider.

**[Udemy Best DE Course(s) or Instructor(s) (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ixxj14/udemy_best_de_courses_or_instructors/)**
*  **Summary:** The thread is seeking recommendations for Udemy courses or instructors. It also gives you a link to a list of data engineering learning resources.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Thread provides a link to a community-submitted data engineering learning resources.

**[Self-learning and collaboration shortage (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1iy4otf/selflearning_and_collaboration_shortage/)**
*  **Summary:** This thread discusses issues with self-learning and collaboration, specifically noting potential shortages in these areas within the data engineering field.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Thread provides a link to a community-submitted data engineering learning resources.

**[Apache Airflow for DevOps and IaC? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1iy4rya/apache_airflow_for_devops_and_iac/)**
*  **Summary:** The thread is seeking to discuss the possibility of using Apache Airflow for DevOps and IaC.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Thread provides a link to a community-submitted data engineering learning resources.

**[Help with Airbyte Google BigQuery destination. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ixx534/help_with_airbyte_google_bigquery_destination/)**
*  **Summary:** The thread is a question regarding help with Google BigQuery destination.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Check raw_data_dataset config is set to "raw_data".
    * Thread provides a link to a community-submitted data engineering learning resources.

**[Courses about data transformations (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ixyhkd/courses_about_data_transformations/)**
*  **Summary:** Thread asking for course recommendations for data transformations
*  **Emotion:** Neutral, with a hint of Positive
*  **Top 3 Points of View:**
    * People recommend Fundamentals of Data Engineering: Plan and Build Robust Data Systems course and Data Engineer Learning Path from interviewquery.com
    * This thread also have link to Fakespot reviews analysis bot
    * Thread provides a link to a community-submitted data engineering learning resources.

**[Fastest way to pivot large dataset on many columns dynamically? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iy2bmc/fastest_way_to_pivot_large_dataset_on_many/)**
*  **Summary:** Thread asking how to pivot large dataset on many columns dynamically.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Find out what is the reporting purpose and the goal.
    * Use SQL cmd that creates a materialized view of that table each day for your reporting.
    * PIVOT operator is an expensive operation.

**[Can anyone tell me what tool was used to produced this architecture diagram? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iy3z19/can_anyone_tell_me_what_tool_was_used_to_produced/)**
*  **Summary:** Thread asking what tool was used to produce a diagram.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Lucid chart.
    * Miro.
    * Figma.

**[Miscrosoft Fabric or Snowflake. Choosing the Right Solution (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iy4eeg/miscrosoft_fabric_or_snowflake_choosing_the_right/)**
*  **Summary:** Thread asking if one should use Snowflake or Miscrosoft Fabric.
*  **Emotion:** Neutral, Negative
*  **Top 3 Points of View:**
    * Snowflake.
    * Snowflake or Databricks.
    * Fabric is problematic and MS is going to take a while to get it up to parity.
