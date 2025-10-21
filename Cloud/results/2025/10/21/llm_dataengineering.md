---
title: "Data Engineering Subreddit"
date: "2025-10-21"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How do you decide when to move from batch jobs to real-time pipelines?](https://www.reddit.com/r/dataengineering/comments/1oc1w56/how_do_you_decide_when_to_move_from_batch_jobs_to/) (Score: 74)
    * This thread discusses the criteria for transitioning from batch processing to real-time data pipelines, with considerations for business needs and infrastructure costs.
2.  [Small company head of dept or team lead at a dominant global company?](https://www.reddit.com/r/dataengineering/comments/1obsrfm/small_company_head_of_dept_or_team_lead_at_a/) (Score: 18)
    * This thread discusses whether to choose a head of department position at a small company or a team lead position at a large global company.
3.  [IaC a prerequisite for DE?](https://www.reddit.com/r/dataengineering/comments/1oc3vf9/iac_a_prerequisite_for_de/) (Score: 18)
    * This thread discusses whether Infrastructure as Code (IaC) is a prerequisite for Data Engineering roles, especially with tools like Terraform.
4.  [Developing with production data: who and how?](https://www.reddit.com/r/dataengineering/comments/1occxjl/developing_with_production_data_who_and_how/) (Score: 13)
    * This thread discusses strategies and challenges of developing with production data, including security, compliance, and data isolation.
5.  [Quick dbt question, do you name your data marts schema 'marts'?](https://www.reddit.com/r/dataengineering/comments/1obzvv0/quick_dbt_question_do_you_name_your_data_marts/) (Score: 12)
    * This thread discusses the naming conventions for data mart schemas in dbt projects.
6.  [Azure Data Factory pipelines in Python](https://www.reddit.com/r/dataengineering/comments/1oc1c98/azure_data_factory_pipelines_in_python/) (Score: 5)
    * This thread discusses the use of Python in Azure Data Factory (ADF) pipelines and explores various methods like Azure Functions, Spark notebooks, and metadata-driven pipelines.
7.  [Thoughts on Using Synthetic Tabular data for DE projects ?](https://www.reddit.com/r/dataengineering/comments/1ocksmo/thoughts_on_using_synthetic_tabular_data_for_de/) (Score: 3)
    * This thread discusses the use of synthetic tabular data for Data Engineering projects.
8.  [Anyone else use AWS Redshift Zero-ETL in US-EAST-1?](https://www.reddit.com/r/dataengineering/comments/1ocery5/anyone_else_use_aws_redshift_zeroetl_in_useast1/) (Score: 3)
    * This thread references a megathread about an AWS outage affecting Redshift Zero-ETL in the US-EAST-1 region.
9.  [Help a noob: CI/CD pipelines with medallion architecture](https://www.reddit.com/r/dataengineering/comments/1oca4c7/help_a_noob_cicd_pipelines_with_medallion/) (Score: 2)
    * This thread explains the relationship between CI/CD pipelines and the medallion architecture (Bronze, Silver, Gold layers).
10. [DBT unit tests on Redshift](https://www.reddit.com/r/dataengineering/comments/1occmld/dbt_unit_tests_on_redshift/) (Score: 2)
    * This thread discusses how to use DBT unit tests on Redshift.
11. [Integrating sqlmesh models with Dagster](https://www.reddit.com/r/dataengineering/comments/1ocaik3/integrating_sqlmesh_models_with_dagster/) (Score: 1)
    * This thread discusses how to use SQLMesh models with Dagster.
12. [Is there a website like MDN for data engineers?](https://www.reddit.com/r/dataengineering/comments/1obtotd/is_there_a_website_like_mdn_for_data_engineers/) (Score: 1)
    * This thread discusses if a website like MDN exists for data engineers, or alternatives to learn more.
13. [Cannot determine primary keys in raw data as no column is unique and concatenation of columns too don’t provide uniqueness](https://www.reddit.com/r/dataengineering/comments/1oc6sq1/cannot_determine_primary_keys_in_raw_data_as_no/) (Score: 0)
    * This thread discusses the problem of not being able to determine the primary keys, and what options there are when no column is unique.

# Detailed Analysis by Thread
**[How do you decide when to move from batch jobs to real-time pipelines? (Score: 74)](https://www.reddit.com/r/dataengineering/comments/1oc1w56/how_do_you_decide_when_to_move_from_batch_jobs_to/)**
*  **Summary:**  The thread discusses criteria for transitioning from batch to real-time pipelines. Considerations include whether real-time updates truly change behavior, the actual need for real-time data versus perceived need, and the cost/complexity trade-offs. Many suggest micro-batching as a middle ground.
*  **Emotion:** The emotional tone is generally Neutral, with a hint of Positive sentiment. Most comments offer practical advice and considerations, without strong emotional expressions.
*  **Top 3 Points of View:**
    *   Real-time is often unnecessary; batch or micro-batch is sufficient for most use cases.
    *   If real-time is genuinely needed, it should be treated as an entirely new, complex project.
    *   Consider whether real-time data actually changes decision-making or behavior.

**[Small company head of dept or team lead at a dominant global company? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1obsrfm/small_company_head_of_dept_or_team_lead_at_a/)**
*  **Summary:** The thread discusses the pros and cons of taking a head of department role at a small company versus a team lead role at a large, global company, with advice focused on weighing growth opportunities and work-life balance.
*  **Emotion:** The emotional tone is primarily Positive and Neutral. The thread reflects thoughtful consideration of career choices.
*  **Top 3 Points of View:**
    *   Global companies offer more growth opportunities and resources despite potential comfort in smaller teams.
    *   Small companies offer better work-life balance and more hands-on experience.
    *   Aligning career goals with the type of work (managerial vs. hands-on) is critical.

**[IaC a prerequisite for DE? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1oc3vf9/iac_a_prerequisite_for_de/)**
*  **Summary:** The thread discusses if Infrastructure as Code (IaC) is a necessary skill for Data Engineers. The general consensus is that while it's not always a strict prerequisite, it's increasingly valuable, especially in smaller companies where engineers wear multiple hats.
*  **Emotion:** The overall emotional tone is Neutral, with a slight variance.
*  **Top 3 Points of View:**
    *   IaC skills (like Terraform) are highly desirable and often required, especially in today's job market.
    *   IaC importance increases in smaller companies where Data Engineers handle more DevOps tasks.
    *   While not always mandatory, DevOps knowledge enhances a Data Engineer's career and effectiveness.

**[Developing with production data: who and how? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1occxjl/developing_with_production_data_who_and_how/)**
*  **Summary:** The thread explores strategies and potential pitfalls of developing with production data. Topics covered include data isolation, compliance, security, the necessity of production-like data for accurate testing, and the importance of control and accountability.
*  **Emotion:** The overall emotional tone is Neutral, focusing on practical advice. A slight Positive sentiment is reflected in the emphasis on accountability and controlled access.
*  **Top 3 Points of View:**
    *   Controlled production access is acceptable, especially with auditing, recording, and restricted access for non-data-qualified individuals.
    *   Using cloned production data in stage environments is crucial for ensuring validity, scalability, and quality.
    *   Compliance requirements should be considered, and production data should not be on DEV infrastructure.

**[Quick dbt question, do you name your data marts schema 'marts'? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1obzvv0/quick_dbt_question_do_you_name_your_data_marts/)**
*  **Summary:** The thread explores different naming conventions for data mart schemas in dbt projects. Many prefer descriptive names over the generic "marts," while others use abbreviations or prefixes. The main takeaway is to be consistent within a company.
*  **Emotion:** Predominantly Neutral. The tone is conversational and focused on sharing practices. There are hints of positive sentiment in calls for clarity and consistency.
*  **Top 3 Points of View:**
    *   Consistency within a company or group is paramount.
    *   Descriptive names (e.g., 'recruitment') are preferred over generic names like "marts" for better clarity.
    *   Some prefer not using marts at all, opting for programmatic denormalization.

**[Azure Data Factory pipelines in Python (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1oc1c98/azure_data_factory_pipelines_in_python/)**
*  **Summary:** The thread discusses the use of Python within Azure Data Factory (ADF) pipelines. Alternatives to using Python directly in ADF are explored, such as Azure Functions, containerized Python jobs, and metadata-driven pipelines. Some users are moving to Airflow or Dagster for a more native Python experience.
*  **Emotion:** The overall tone is Neutral. The discussion revolves around technical solutions and experiences.
*  **Top 3 Points of View:**
    *   Metadata-driven ADF pipelines are often sufficient and avoid unnecessary complexity.
    *   Azure Functions provide a way to run Python scripts triggered by ADF.
    *   Alternatives like Airflow or Dagster offer a more native Python development experience, although with increased complexity.

**[Thoughts on Using Synthetic Tabular data for DE projects ? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ocksmo/thoughts_on_using_synthetic_tabular_data_for_de/)**
*  **Summary:** The thread discusses the use of synthetic tabular data for Data Engineering projects.
*  **Emotion:** Neutral sentiment.
*  **Top 2 Points of View:**
    *   No one cares.
    *   Bot post for resources.

**[Anyone else use AWS Redshift Zero-ETL in US-EAST-1? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ocery5/anyone_else_use_aws_redshift_zeroetl_in_useast1/)**
*  **Summary:** The thread references a megathread about an AWS outage affecting Redshift Zero-ETL in the US-EAST-1 region.
*  **Emotion:** Neutral sentiment.
*  **Top 1 Points of View:**
    *   Links to megathread, thread locked.

**[Help a noob: CI/CD pipelines with medallion architecture (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1oca4c7/help_a_noob_cicd_pipelines_with_medallion/)**
*  **Summary:** The thread explains the relationship between CI/CD pipelines and the medallion architecture (Bronze, Silver, Gold layers). Staging areas, environments, and the purpose of each data layer are discussed.
*  **Emotion:** High Neutral sentiment is prevalent, focused on explanation and information.
*  **Top 3 Points of View:**
    *   Staging is where raw data lands for ingestion, which can be an S3 bucket or a database.
    *   Bronze, Silver, and Gold layers are stages in the DWH representing data transformations.
    *   Different development environments isolate code, logic, and processes.

**[DBT unit tests on Redshift (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1occmld/dbt_unit_tests_on_redshift/)**
*  **Summary:** This thread discusses how to use DBT unit tests on Redshift.
*  **Emotion:** Neutral sentiment.
*  **Top 1 Points of View:**
    *   Wrapping in different quotes might solve the issue.

**[Integrating sqlmesh models with Dagster (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ocaik3/integrating_sqlmesh_models_with_dagster/)**
*  **Summary:** This thread discusses how to use SQLMesh models with Dagster.
*  **Emotion:** Neutral sentiment.
*  **Top 1 Points of View:**
    *   Use dg-sqlmesh.

**[Is there a website like MDN for data engineers? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1obtotd/is_there_a_website_like_mdn_for_data_engineers/)**
*  **Summary:** This thread discusses if a website like MDN exists for data engineers, or alternatives to learn more.
*  **Emotion:** Mix of neutral and positive sentiment.
*  **Top 2 Points of View:**
    *   No, the field is far too complex for one website to cover.
    *   Reading documentation from cloud providers like aws, azure, and gcp helps a lot. also, stack overflow is a decent resource.

**[Cannot determine primary keys in raw data as no column is unique and concatenation of columns too don’t provide uniqueness (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1oc6sq1/cannot_determine_primary_keys_in_raw_data_as_no/)**
*  **Summary:** This thread discusses the problem of not being able to determine the primary keys, and what options there are when no column is unique.
*  **Emotion:** Neutral sentiment.
*  **Top 3 Points of View:**
    *   Surrogate key ftw
    *   row number on the way in? then do concat followed by hash
    *   If there is no natural primary key you may have to consider making one that fits the needs of your customer. Speak to your customer.
