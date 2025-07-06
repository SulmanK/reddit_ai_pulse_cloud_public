---
title: "Data Engineering Subreddit"
date: "2025-07-06"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions

1.  [[D] difference between writing SQL queries or writing DataFrame code [in SPARK]](https://www.reddit.com/r/dataengineering/comments/1lsxg99/difference_between_writing_sql_queries_or_writing/) (Score: 35)
    *   Discussion on whether to use SQL queries or DataFrame code within Spark, focusing on performance, maintainability, and convenience.
2.  [dbt cloud is brainless and useless](https://www.reddit.com/r/dataengineering/comments/1lt6d2y/dbt_cloud_is_brainless_and_useless/) (Score: 35)
    *   Users debate the value of dbt Cloud versus open-source alternatives with custom orchestration.
3.  [Good documentation practices](https://www.reddit.com/r/dataengineering/comments/1lsr9gl/good_documentation_practices/) (Score: 20)
    *   Debate regarding documentation practices, with some arguing that universal documentation is a waste of time, and others focus on automated lineage and target documentation.
4.  [Using Prefect instead of Airflow](https://www.reddit.com/r/dataengineering/comments/1lskxb9/using_prefect_instead_of_airflow/) (Score: 16)
    *   Users discuss the pros and cons of using Prefect versus Airflow, with a focus on job prospects and the complexity of Airflow setup.
5.  [Fabric: translytical task flows. Does this sound *** to anyone?](https://www.reddit.com/r/dataengineering/comments/1lsj9x9/fabric_translytical_task_flows_does_this_sound/) (Score: 11)
    *   Discussion on translytical task flows in Microsoft Fabric, with some expressing concerns about users modifying cleaned-up data and others highlighting potential use cases.
6.  [Does this open-source BI stack make sense? NiFi + PostgreSQL + Superset](https://www.reddit.com/r/dataengineering/comments/1lt18rx/does_this_opensource_bi_stack_make_sense_nifi/) (Score: 10)
    *   Users discuss the pros and cons of using NiFi, PostgreSQL, and Superset as an open-source BI stack.
7.  [Knowledge Graphs - thoughts?](https://www.reddit.com/r/dataengineering/comments/1lt9wlb/knowledge_graphs_thoughts/) (Score: 2)
    *   Users share their thoughts on Knowledge Graphs.
8.  [I’ve built a Jupyter-based data pipeline that’s grown with one stakeholder’s needs. How should I scale it to handle multiple stakeholders, each with their own folders and requirements?](https://www.reddit.com/r/dataengineering/comments/1lsj3ot/ive_built_a_jupyterbased_data_pipeline_thats/) (Score: 0)
    *   Users discuss the challenges of scaling a Jupyter-based pipeline for multiple stakeholders.
9.  [Doubts about de](https://www.reddit.com/r/dataengineering/comments/1lsv7xt/doubts_about_de/) (Score: 0)
    *   Users discuss the importance of learning data engineering tools before relying on AI.

# Detailed Analysis by Thread

**[[D] difference between writing SQL queries or writing DataFrame code [in SPARK] (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1lsxg99/difference_between_writing_sql_queries_or_writing/)**
*   **Summary:**  The discussion revolves around the performance differences and advantages of using SQL queries versus DataFrame code in Apache Spark. Users share their experiences, highlighting factors like the Catalyst Optimizer, maintainability, and convenience in schema evolution.
*   **Emotion:** The overall emotional tone is generally neutral, with a mix of positive sentiments expressing preferences for DataFrames due to modularity and clarity.
*   **Top 3 Points of View:**
    *   There is no true performance difference due to Spark's Catalyst Optimizer.
    *   DataFrame is more modular and clearer for defining data pipelines.
    *   SQL can be more performant in specific situations like broadcast and CTE usage.

**[dbt cloud is brainless and useless (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1lt6d2y/dbt_cloud_is_brainless_and_useless/)**
*   **Summary:**  This thread discusses the utility of dbt Cloud, with some users finding it lacking in control and flexibility, while others, particularly solo data practitioners, find it convenient and worth the cost. The conversation also touches on alternatives like dbt core, Airflow, and other orchestration tools.
*   **Emotion:** The overall emotion is mixed. It is generally neutral, with some negativity toward dbt cloud due to a perceived lack of control.
*   **Top 3 Points of View:**
    *   dbt Cloud is convenient for solo data practitioners.
    *   A dedicated orchestrator provides more control than dbt Cloud.
    *   dbt open-source combined with other tools like Airflow is a viable alternative.

**[Good documentation practices (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1lsr9gl/good_documentation_practices/)**
*   **Summary:** The thread explores different approaches to documentation in data engineering. Some argue against extensive documentation, considering it a waste of time, while others emphasize automated lineage, data asset catalogs, and target documentation.
*   **Emotion:** The emotional tone is primarily neutral, with a slight leaning towards skepticism about the value of extensive documentation.
*   **Top 3 Points of View:**
    *   Universal documentation is often a waste of time.
    *   Automated lineage and a catalog of data assets are more valuable.
    *   Focus on documenting the target and requirements.

**[Using Prefect instead of Airflow (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1lskxb9/using_prefect_instead_of_airflow/)**
*   **Summary:**  The discussion compares Prefect and Airflow for workflow orchestration. Users advise sticking with Airflow for better job prospects and discuss the learning curve associated with both tools. Setup difficulties are also addressed.
*   **Emotion:** The emotional tone is generally neutral, with a slight negativity towards the user struggling to set up Airflow.
*   **Top 3 Points of View:**
    *   Airflow is more widely used and better for job prospects.
    *   Setting up and managing Airflow can be complex.
    *   Hosted Airflow solutions on AWS or GCP can simplify the setup.

**[Fabric: translytical task flows. Does this sound *** to anyone? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1lsj9x9/fabric_translytical_task_flows_does_this_sound/)**
*   **Summary:** Users discuss the concept of translytical task flows in Microsoft Fabric. Some are skeptical about allowing end-users to modify data, while others see potential use cases like writeback for forecasts and insight-to-action scenarios.
*   **Emotion:** The overall tone is skeptical and negative.
*   **Top 3 Points of View:**
    *   Allowing end-users to modify data is a terrible idea in most cases.
    *   Translytical flows are useful for scenarios like writeback and triggering actions.
    *   The system should only trigger "Fix these ones" for the team responsible for the data.

**[Does this open-source BI stack make sense? NiFi + PostgreSQL + Superset (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1lt18rx/does_this_opensource_bi_stack_make_sense_nifi/)**
*   **Summary:**  The thread discusses the viability of using NiFi, PostgreSQL, and Superset as an open-source BI stack. Some users advise against NiFi due to operational overhead, while others find it useful. Alternatives like Airflow, Airbyte, and Dagster are mentioned.
*   **Emotion:** The emotional tone is mixed with positivity and neutrality. Some users had good experiences with Nifi while others had negative sentiments.
*   **Top 3 Points of View:**
    *   NiFi can be more operations work than necessary.
    *   Airflow, Airbyte or Dagster are lighter alternatives.
    *   Postgres and Superset are generally considered good choices.

**[Knowledge Graphs - thoughts? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lt9wlb/knowledge_graphs_thoughts/)**
*   **Summary:**  This thread has limited engagement. Users shares their thoughts about Knowledge Graphs.
*   **Emotion:** Negative, with posters saying that the technology doesn't live up to the hype.
*   **Top 3 Points of View:**
    *  Knowledge graphs don't live up to the hype.
    *  RDF/Ontology dreams are not the best version of FOL for most use cases imo.

**[I’ve built a Jupyter-based data pipeline that’s grown with one stakeholder’s needs. How should I scale it to handle multiple stakeholders, each with their own folders and requirements? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lsj3ot/ive_built_a_jupyterbased_data_pipeline_thats/)**
*   **Summary:** This thread has limited engagement. Users share their thoughts regarding data pipeline.
*   **Emotion:** The overall tone is neutral.
*   **Top 3 Points of View:**
    *   Jupyter-based pipelines are hard to scale.
    *   Multiple notebooks can be a stopgap solution.

**[Doubts about de (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lsv7xt/doubts_about_de/)**
*   **Summary:** This thread has limited engagement. It stresses the need to learn your tools before relying on AI.
*   **Emotion:** The overall tone is neutral.
*   **Top 3 Points of View:**
    *   Learn your tools before using AI to churn out pipelines.
