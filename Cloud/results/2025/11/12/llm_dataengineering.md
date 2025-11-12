---
title: "Data Engineering Subreddit"
date: "2025-11-12"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] If Spark is lazy, how does it infer schema without reading data — and is Spark only useful for multi-node memory?](https://www.reddit.com/r/dataengineering/comments/1ov19lh/if_spark_is_lazy_how_does_it_infer_schema_without/) (Score: 34)
    *   Users are discussing how Spark infers schema despite its lazy evaluation, and whether it's beneficial for single-machine use cases compared to Pandas.
2.  [Introducing Open Transformation Specification (OTS) – a portable, executable standard for data transformations](https://github.com/francescomucio/open-transformation-specification) (Score: 23)
    *   The thread introduces OTS and discusses its potential compared to existing tools like dbt.
3.  [Worth it to move to a different job for same pay from DE to Analytics Manager?](https://www.reddit.com/r/dataengineering/comments/1ov7fxk/worth_it_to_move_to_a_different_job_for_same_pay/) (Score: 7)
    *   The thread discusses the pros and cons of moving from a Data Engineering role to an Analytics Manager role for the same pay, considering factors like job security and future career prospects.
4.  [What’s your growth hack?](https://www.reddit.com/r/dataengineering/comments/1ovdd9k/whats_your_growth_hack/) (Score: 6)
    *   Users share their strategies for career growth in the field of data engineering.
5.  [Building and maintaining pyspark script](https://www.reddit.com/r/dataengineering/comments/1ouxsb8/building_and_maintaining_pyspark_script/) (Score: 5)
    *   The thread discusses best practices for building and maintaining PySpark scripts, including modularization, configuration management, and testing.
6.  [AWS Glue to Azure databricks/ADF](https://www.reddit.com/r/dataengineering/comments/1ov7pyc/aws_glue_to_azure_databricksadf/) (Score: 5)
    *   Users are seeking advice on migrating from AWS Glue to Azure Databricks and ADF.
7.  [2025 State of Data Quality survey results](https://26725328.fs1.hubspotusercontent-eu1.net/hubfs/26725328/SYNQs%202025%20State%20of%20Data%20Quality%20Survey.pdf) (Score: 5)
    *   The thread discusses the results of a 2025 Data Quality survey
8.  [Re-evaluating our data integration setup: Azure Container Apps vs orchestration tools](https://www.reddit.com/r/dataengineering/comments/1ouz5fq/reevaluating_our_data_integration_setup_azure/) (Score: 4)
    *   The thread is about re-evaluating data integration setup using Azure Container Apps versus orchestration tools.
9.  [Bitnami gone?](https://www.reddit.com/r/dataengineering/comments/1ov9muj/bitnami_gone/) (Score: 3)
    *   The thread discusses the future of Bitnami images in light of changes to their availability and pricing.
10. [Organizing a climate data + machine learning research project that grew out of control](https://www.reddit.com/r/dataengineering/comments/1ovb4ww/organizing_a_climate_data_machine_learning/) (Score: 3)
    *   The thread discusses strategies for organizing a climate data and machine learning project that has become unmanageable.

# Detailed Analysis by Thread
**[[D] If Spark is lazy, how does it infer schema without reading data — and is Spark only useful for multi-node memory? (Score: 34)](https://www.reddit.com/r/dataengineering/comments/1ov19lh/if_spark_is_lazy_how_does_it_infer_schema_without/)**
*  **Summary:** The discussion revolves around Spark's lazy evaluation and how it infers schema, as well as its usefulness for single-machine vs. multi-node environments.  Users discuss the various stages of execution in Spark and compare it to Pandas.
*  **Emotion:** The overall emotional tone is Neutral, with users providing technical explanations and comparisons.
*  **Top 3 Points of View:**
    *   Spark infers schema by sampling data or reading metadata headers, which is not a lazy operation.
    *   Spark's laziness applies to transformations, not schema inference.
    *   Spark is most beneficial for large, distributed datasets, while Pandas is often better for single-machine use cases.

**[Introducing Open Transformation Specification (OTS) – a portable, executable standard for data transformations (Score: 23)](https://github.com/francescomucio/open-transformation-specification)**
*  **Summary:** The thread introduces the Open Transformation Specification (OTS) and discusses its potential and drawbacks compared to existing solutions like dbt.
*  **Emotion:** The overall emotional tone is Neutral, with a hint of Positive sentiment, but also Negative sentiment, as some users are skeptical.
*  **Top 3 Points of View:**
    *   OTS is a vague attempt at a standard without clear benefits over existing tools.
    *   OTS might be a good approach to making an open source library of UDF's in different languages.
    *   The problem is that everyone already uses dbt and every tool already integrates dbt-core so I don't understand why I would use this.

**[Worth it to move to a different job for same pay from DE to Analytics Manager? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ov7fxk/worth_it_to_move_to_a_different_job_for_same_pay/)**
*  **Summary:** Users are debating the value of transitioning from a Data Engineering role to an Analytics Manager role for the same salary, considering factors like job security, career growth potential, and benefits like pensions.
*  **Emotion:** The overall emotional tone is Neutral, with users offering balanced perspectives.
*  **Top 3 Points of View:**
    *   The Analytics Manager role offers potential stability, especially in government jobs with pension benefits.
    *   There are not many jobs beyond "manager" on Analytics teams, this could be a terminal position.
    *   DE background before analytics can give you a leg up for director of data in the future.

**[What’s your growth hack? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1ovdd9k/whats_your_growth_hack/)**
*  **Summary:** The thread explores various strategies and "hacks" for career growth in the data engineering field.
*  **Emotion:** The overall emotional tone is Neutral with some comments that show Positive sentiment, reflecting users' enthusiasm for career advancement.
*  **Top 3 Points of View:**
    *   Continuously push the bounds of expectation and embrace lifelong learning.
    *   Regularly evaluate skills, learning opportunities, and job satisfaction to identify areas for growth.
    *   Switch roles/departments/companies once you've mastered 95% of a job or after 2 years.

**[Building and maintaining pyspark script (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ouxsb8/building_and_maintaining_pyspark_script/)**
*  **Summary:** This thread discusses best practices for constructing and maintaining PySpark scripts, emphasizing modularity, configuration, and leveraging Python's tooling capabilities.
*  **Emotion:** The overall tone is Neutral, focusing on providing practical advice and technical insights. Some users also express Negative sentiment when talking about the mistakes to avoid
*  **Top 3 Points of View:**
    *   Separate I/O and transformation logic for easier testing and maintenance.
    *   Modularize code into small functions and use config files for constants and paths.
    *   Consider using Databricks bundles + GH actions for configuration and monitoring.

**[AWS Glue to Azure databricks/ADF (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ov7pyc/aws_glue_to_azure_databricksadf/)**
*  **Summary:** The thread discusses options for migrating from AWS Glue to Azure services like Databricks and Azure Data Factory (ADF).
*  **Emotion:** The overall emotional tone is Neutral, offering practical suggestions.
*  **Top 3 Points of View:**
    *   Use ADF + Databricks for orchestration and ETL to Snowflake.
    *   Consider using SSIS for the project.

**[2025 State of Data Quality survey results (Score: 5)](https://26725328.fs1.hubspotusercontent-eu1.net/hubfs/26725328/SYNQs%202025%20State%20of%20Data%20Quality%20Survey.pdf)**
*  **Summary:** The thread is about the results of a 2025 Data Quality survey.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   How many people have participated?

**[Re-evaluating our data integration setup: Azure Container Apps vs orchestration tools (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ouz5fq/reevaluating_our_data_integration_setup_azure/)**
*  **Summary:** Users discuss whether to use Azure Container Apps directly or leverage orchestration tools like Airflow or Dagster for data integration.
*  **Emotion:** The overall emotional tone is Neutral, with some Positive sentiment.
*  **Top 3 Points of View:**
    *   Azure Data Factory is suitable for simple scheduling and monitoring tasks.
    *   Dagster and Airflow are schedulers that can be used with K8S.

**[Bitnami gone? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ov9muj/bitnami_gone/)**
*  **Summary:** Users are discussing the implications of Bitnami moving most of its public images to a legacy repo with no future updates.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Bitnami is moving most of its public images to a legacy repo with no future updates starting August 28, 2025.
    *   Broadcom ruins everything it touches, I would plan to get off bitnami images if you can.

**[Organizing a climate data + machine learning research project that grew out of control (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ovb4ww/organizing_a_climate_data_machine_learning/)**
*  **Summary:** The thread is about seeking advice on how to better organize climate data and machine learning research that has grown out of control.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Put everything in a relational database.
    *   A data lake seems reasonable for ML use case, but it's not clear what the possibilities are for netcdf and xarray formats.
    *   Recommend Duckdb with parquet.
