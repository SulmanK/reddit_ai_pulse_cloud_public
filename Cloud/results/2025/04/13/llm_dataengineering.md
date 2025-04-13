---
title: "Data Engineering Subreddit"
date: "2025-04-13"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Is this take-home assignment too large and complex?](https://www.reddit.com/r/dataengineering/comments/1jy09o8/is_this_takehome_assignment_too_large_and_complex/) (Score: 71)
    *   Users are discussing whether a data engineering take-home assignment is too extensive and complex, with many suggesting it's an unreasonable request.
2.  [How do my fellow on-prem DEs keep their sanity...](https://www.reddit.com/r/dataengineering/comments/1jxtxqo/how_do_my_fellow_onprem_des_keep_their_sanity/) (Score: 43)
    *   Data engineers are sharing their experiences and solutions for dealing with challenges in on-premise data environments, particularly regarding ETL, DWH stacks and memory issues.
3.  [Data Inserts best practices with Iceberg](https://www.reddit.com/r/dataengineering/comments/1jxun0q/data_inserts_best_practices_with_iceberg/) (Score: 18)
    *   Users are discussing best practices for data insertion into Iceberg tables, including batching, compaction, and handling streaming data.
4.  [I'm struggling to evaluate job offer and would appreciate outside opinions](https://www.reddit.com/r/dataengineering/comments/1jxsce8/im_struggling_to_evaluate_job_offer_and_would/) (Score: 13)
    *   A user is seeking advice on whether to accept a new job offer, considering factors like salary, location, and the skills involved, especially in light of having to pay back tuition reimbursement.
5.  [is Microsoft fabric the right shortcut for a data analyst moving to data engineer ?](https://www.reddit.com/r/dataengineering/comments/1jy1n56/is_microsoft_fabric_the_right_shortcut_for_a_data/) (Score: 11)
    *   The discussion revolves around whether Microsoft Fabric is a suitable shortcut for data analysts transitioning to data engineering roles, with opinions varying on its utility and whether shortcuts are advisable.
6.  [Building a Real-Time Analytics Pipeline: Balancing Throughput and Latency](https://www.reddit.com/r/dataengineering/comments/1jy7sii/building_a_realtime_analytics_pipeline_balancing/) (Score: 7)
    *   This thread discusses the architecture of a real-time analytics pipeline and the necessity of an intermediate queue between Kafka and WebSockets.
7.  [We built a natural language search tool for finding U.S. government datasets](https://www.reddit.com/r/dataengineering/comments/1jydmqv/we_built_a_natural_language_search_tool_for/) (Score: 7)
    *   Users are discussing a newly developed natural language search tool designed to facilitate the discovery of U.S. government datasets.
8.  [Dilemma: SWE vs DE @ Big Tech](https://www.reddit.com/r/dataengineering/comments/1jxswyj/dilemma_swe_vs_de_big_tech/) (Score: 6)
    *   The discussion centers around the choice between Software Engineering (SWE) and Data Engineering (DE) roles at big tech companies, with considerations for career growth, job security, and personal interests.
9.  [I need assistance in optimizing this ADF workflow.](https://www.reddit.com/r/dataengineering/comments/1jy0zwo/i_need_assistance_in_optimizing_this_adf_workflow/) (Score: 5)
    *   Users are providing suggestions and solutions for optimizing an Azure Data Factory (ADF) workflow, particularly focusing on the placement of a delete activity within the workflow.
10. [Creating AWS Glue Connection for On-prem JDBC source](https://www.reddit.com/r/dataengineering/comments/1jy79rg/creating_aws_glue_connection_for_onprem_jdbc/) (Score: 3)
    *   The conversation is about creating AWS Glue connections to on-premise JDBC sources, with a suggested workaround involving Lambda functions, AWS PrivateLink, and JDBC connections via SQLAlchemy.
11. [Self-Healing Data Quality in DBT — Without Any Extra Tools](https://www.reddit.com/r/dataengineering/comments/1jyg4ps/selfhealing_data_quality_in_dbt_without_any_extra/) (Score: 3)
    *   A user is reacting to an article about self-healing data quality in DBT. User believes bad data should be detected and triaged, rather than automatically detected and fixed.
12. [Want opinion about Lambdas](https://www.reddit.com/r/dataengineering/comments/1jxy77l/want_opinion_about_lambdas/) (Score: 1)
    *   A user is seeking opinions about using AWS Lambdas.
13. [What to do and how to do???](https://i.redd.it/ttbzo15fbnue1.jpeg) (Score: 0)
    *   A user is asking for help on how to design a pipeline that can handle both incremental and historical loads.
14. [How to create changeStreams pipeline to bigquery](https://www.reddit.com/r/dataengineering/comments/1jxr3uh/how_to_create_changestreams_pipeline_to_bigquery/) (Score: 0)
    *   A user is discussing the creation of a change streams pipeline to BigQuery.
15. [Help](https://www.reddit.com/r/dataengineering/comments/1jxv28g/help/) (Score: 0)
    *   A user is asking for help and gets redirected to learning resources.

# Detailed Analysis by Thread
**[ [D] Is this take-home assignment too large and complex? (Score: 71)](https://www.reddit.com/r/dataengineering/comments/1jy09o8/is_this_takehome_assignment_too_large_and_complex/)**
*  **Summary:** The discussion revolves around a data engineering take-home assignment that many users believe is too extensive, complex, and time-consuming for an interview task. Several users advise the original poster (OP) to reject the assignment, seeing it as disrespectful and indicative of a potentially negative work environment.
*  **Emotion:** The overall emotional tone is negative, with a sentiment score of -0.03, reflecting frustration and disapproval towards the take-home assignment.
*  **Top 3 Points of View:**
    *   The assignment is unreasonable and disrespectful of the candidate's time.
    *   Completing the assignment is akin to doing free work for the company.
    *   The scope of the assignment suggests that the company may not understand the role of a data engineer.

**[How do my fellow on-prem DEs keep their sanity... (Score: 43)](https://www.reddit.com/r/dataengineering/comments/1jxtxqo/how_do_my_fellow_onprem_des_keep_their_sanity/)**
*  **Summary:** This thread focuses on the challenges faced by on-premise data engineers and how they maintain their sanity. The discussion covers topics like ETL and DWH stack design, memory issues with Pydantic schema validation, and the limitations of pods as a processing platform in Kubernetes.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.69, indicating an informative and problem-solving discussion rather than strong positive or negative emotions.
*  **Top 3 Points of View:**
    *   Kubernetes (K8s) can be a limiting factor in on-prem environments, especially with regards to pods.
    *   Batching and chunking data can alleviate memory issues during Pydantic schema validation.
    *   Airflow should be used for orchestration, not for ETL/processing jobs.

**[Data Inserts best practices with Iceberg (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1jxun0q/data_inserts_best_practices_with_iceberg/)**
*  **Summary:** The discussion centers on best practices for inserting data into Apache Iceberg tables. Users discuss the importance of batching writes, avoiding merge operations, and periodically compacting files. They also mention the use of tools like Spark with structured streaming to handle checkpointing and file updates.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.72, indicating a practical and technical discussion.
*  **Top 3 Points of View:**
    *   Batching larger writes is more optimal, especially with small files.
    *   Using Spark with structured streaming can help with file updates.
    *   Compaction jobs are useful for merging small files and reducing overhead.

**[I'm struggling to evaluate job offer and would appreciate outside opinions (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1jxsce8/im_struggling_to_evaluate_job_offer_and_would/)**
*  **Summary:** A user is seeking advice on whether to accept a new job offer, considering factors like salary, location, and the skills involved, especially in light of having to pay back tuition reimbursement.
*  **Emotion:** The overall emotional tone is slightly negative, with a sentiment score of 0.67, reflecting the user's dilemma and concerns about the financial implications of the job change.
*  **Top 3 Points of View:**
    *   The new offer is not worth the move, especially considering the financial loss from tuition payback.
    *   The new job's skills are more in demand.
    *   Negotiate with the new company to cover the tuition payback or increase salary.

**[is Microsoft fabric the right shortcut for a data analyst moving to data engineer ? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1jy1n56/is_microsoft_fabric_the_right_shortcut_for_a_data/)**
*  **Summary:** The thread explores whether Microsoft Fabric is a suitable shortcut for data analysts transitioning to data engineering. Opinions vary, with some suggesting it might be a useful tool given Microsoft's presence in many Fortune 500 companies, while others argue that there are no shortcuts and that focusing on fundamental skills and technologies like Snowflake and Databricks is more beneficial.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.69, indicating a balanced discussion with mixed opinions.
*  **Top 3 Points of View:**
    *   There are no shortcuts.
    *   Microsoft Fabric might be a viable option due to Microsoft's strong presence in the industry.
    *   Snowflake and Databricks are better platforms for learning data engineering.

**[Building a Real-Time Analytics Pipeline: Balancing Throughput and Latency (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jy7sii/building_a_realtime_analytics_pipeline_balancing/)**
*  **Summary:** This thread discusses the architecture of a real-time analytics pipeline. A user questions the need for an intermediate queue between Kafka and WebSockets, suggesting that Kafka's message retention capabilities might make it unnecessary.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.42, suggesting a technical discussion aimed at optimizing a system.
*  **Top 3 Points of View:**
    *   The necessity of the intermediate queue is questioned.
    *   Kafka's message retention abilities are highlighted as a potential alternative.

**[We built a natural language search tool for finding U.S. government datasets (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1jydmqv/we_built_a_natural_language_search_tool_for/)**
*  **Summary:** Users are discussing a newly developed natural language search tool designed to facilitate the discovery of U.S. government datasets.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.78, reflecting interest and appreciation for the tool.
*  **Top 3 Points of View:**
    *   Interest in the technology used.
    *   A bot recommends submitting the project to an open-source project showcase.

**[Dilemma: SWE vs DE @ Big Tech (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1jxswyj/dilemma_swe_vs_de_big_tech/)**
*  **Summary:** The discussion centers around the choice between Software Engineering (SWE) and Data Engineering (DE) roles at big tech companies, with considerations for career growth, job security, and personal interests.
*  **Emotion:** The emotional tone is slightly positive, with a sentiment score of 0.66, reflecting a discussion about career choices and opportunities.
*  **Top 3 Points of View:**
    *   SWE is drying up. Go for DE.
    *   Whatever pays more and you’re happy in.
    *   Be careful with team matching, since you may not work on a data team in the SWE role.

**[I need assistance in optimizing this ADF workflow. (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jy0zwo/i_need_assistance_in_optimizing_this_adf_workflow/)**
*  **Summary:** Users are providing suggestions and solutions for optimizing an Azure Data Factory (ADF) workflow, particularly focusing on the placement of a delete activity within the workflow.
*  **Emotion:** The emotional tone is positive, with a sentiment score of 0.92, indicating a helpful and solution-oriented discussion.
*  **Top 3 Points of View:**
    *   The delete activity should be inside the If condition.
    *   You don't need to use all 3 connections (skip, success, fail) when it's in a linear chain.

**[Creating AWS Glue Connection for On-prem JDBC source (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jy79rg/creating_aws_glue_connection_for_onprem_jdbc/)**
*  **Summary:** The conversation is about creating AWS Glue connections to on-premise JDBC sources, with a suggested workaround involving Lambda functions, AWS PrivateLink, and JDBC connections via SQLAlchemy.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.61, reflecting a technical discussion with practical advice.
*  **Top 3 Points of View:**
    *   Using Lambda functions with AWS PrivateLink can help connect Snowflake to on-prem Oracle DB.
    *   JDBC and SQLAlchemy are useful for connecting to the database.

**[Self-Healing Data Quality in DBT — Without Any Extra Tools (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jyg4ps/selfhealing_data_quality_in_dbt_without_any_extra/)**
*  **Summary:** A user is reacting to an article about self-healing data quality in DBT. User believes bad data should be detected and triaged, rather than automatically detected and fixed.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.64, indicating a balanced opinion.
*  **Top 3 Points of View:**
    *   The approach of automatically fixing data issues is not agreeable because of the risk of picking the wrong rows.
    *   It's better to detect and triage rather than detect and fix.
    *   Fixing bad data downstream is more expensive to fix and revert everything back.

**[Want opinion about Lambdas (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jxy77l/want_opinion_about_lambdas/)**
*  **Summary:** A user is seeking opinions about using AWS Lambdas.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.97, indicating a factual statement.
*  **Top 3 Points of View:**
    *   Lambdas are equivalent to gifting Amazon part of your margin.

**[What to do and how to do??? (Score: 0)](https://i.redd.it/ttbzo15fbnue1.jpeg)**
*  **Summary:** A user is asking for help on how to design a pipeline that can handle both incremental and historical loads.
*  **Emotion:** The emotional tone is slightly positive, with a sentiment score of 0.48, reflecting helpful advice.
*  **Top 3 Points of View:**
    *   Design a pipeline that can handle both incremental and historical loads, it's simpler to maintain a single solution.

**[How to create changeStreams pipeline to bigquery (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jxr3uh/how_to_create_changestreams_pipeline_to_bigquery/)**
*  **Summary:** A user is discussing the creation of a change streams pipeline to BigQuery.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.71, reflecting a neutral observation.
*  **Top 3 Points of View:**
    *   Pubsub being a bottleneck is weird.

**[Help (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jxv28g/help/)**
*  **Summary:** A user is asking for help and gets redirected to learning resources.
*  **Emotion:** The emotional tone is neutral, with a sentiment score of 0.86, reflecting a neutral redirection to resources.
*  **Top 3 Points of View:**
    *   The user is directed to community-submitted learning resources.
