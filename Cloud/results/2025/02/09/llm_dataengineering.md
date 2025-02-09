---
title: "Data Engineering Subreddit"
date: "2025-02-09"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Why do engineers break each metric into a separate CTE?](https://www.reddit.com/r/dataengineering/comments/1iln487/why_do_engineers_break_each_metric_into_a/) (Score: 17)
    *   The discussion revolves around the common practice of breaking down metrics into separate Common Table Expressions (CTEs) in data engineering and the reasons behind it.

2.  [What level of System Design knowledge is required for a data engineer?](https://www.reddit.com/r/dataengineering/comments/1ilcvr1/what_level_of_system_design_knowledge_is_required/) (Score: 16)
    *   The thread explores the extent of system design knowledge required for data engineers, with varying opinions on how deep one needs to delve into concepts like load balancing, automation, and scalability.

3.  [DevOps to Data Engineering: Am I Escaping a Sinking Ship or Jumping Into a Bigger Fire?](https://www.reddit.com/r/dataengineering/comments/1ilauju/devops_to_data_engineering_am_i_escaping_a/) (Score: 15)
    *   This discussion weighs the pros and cons of transitioning from a DevOps role to data engineering, considering factors like demand, pay, responsibilities, and future career prospects.

4.  [How does your company's data architecture looks like?](https://www.reddit.com/r/dataengineering/comments/1ilhvg5/how_does_your_companys_data_architecture_looks/) (Score: 15)
    *   Users share and describe the data architecture of their respective companies, including the technologies and platforms used, such as Databricks, Azure, Snowflake, and the Medallion architecture.

5.  [Is it possible to change Source of a adf pipeline dynamically?(eg from azure to sap )](https://www.reddit.com/r/dataengineering/comments/1il7pcl/is_it_possible_to_change_source_of_a_adf_pipeline/) (Score: 10)
    *   The discussion revolves around the possibility of dynamically changing the source of an Azure Data Factory (ADF) pipeline and potential approaches to achieve this, along with the pros and cons of using ADF for advanced tasks.

6.  [Fellow engineers in Finance, what extra knowledge is helpful to get better roles/pay in Finance data domain](https://www.reddit.com/r/dataengineering/comments/1ile71k/fellow_engineers_in_finance_what_extra_knowledge/) (Score: 10)
    *   Data engineers working in finance share insights on the extra knowledge and skills that can improve career prospects and compensation in the finance data domain, such as financial mathematics, automation, and financial accounting fundamentals.

7.  [Career Growth and Reflections of a Data Development Engineer](https://www.reddit.com/r/dataengineering/comments/1il55kf/career_growth_and_reflections_of_a_data/) (Score: 5)
    *   This thread provides a list of community-submitted learning resources.

8.  [Discover the Power of Spark Structured Streaming in Databricks](https://www.reddit.com/r/dataengineering/comments/1ilfhl0/discover_the_power_of_spark_structured_streaming/) (Score: 5)
    *   This thread discusses Spark Structured Streaming and its integration with Databricks, with a suggestion to explore its integration with AWS services.

9.  [Why do small files in big data engines cause performance issues?](https://www.reddit.com/r/dataengineering/comments/1ilfmi2/why_do_small_files_in_big_data_engines_cause/) (Score: 5)
    *   The discussion addresses the performance issues caused by small files in big data engines and offers solutions like automating file size optimization during ETL processes, and also mentions the increased cloud storage costs due to more partitions.

10. [How Do You Organize and Visualize Complex Data Processing Tasks?](https://www.reddit.com/r/dataengineering/comments/1ilb8gs/how_do_you_organize_and_visualize_complex_data/) (Score: 3)
    *   The thread discusses ways to organize and visualize complex data processing tasks, and the use of tools like dbt and Delta Live Tables for observability and lineage.

11. [How do you deal with uncertainty in planning?](https://www.reddit.com/r/dataengineering/comments/1ilm7io/how_do_you_deal_with_uncertainty_in_planning/) (Score: 3)
    *   The discussion is centered around how to handle uncertainty in planning. Suggestions include providing estimates with ranges, regular checkpoints, and honest communication.

12. [Transitioning from Data Engineering to Data Science or AI](https://www.reddit.com/r/dataengineering/comments/1ilohuo/transitioning_from_data_engineering_to_data/) (Score: 3)
    *   This thread provides a link to a community guide on transitioning to Data Engineering.

13. [Need advice on coding approach.](https://www.reddit.com/r/dataengineering/comments/1ilj0kl/need_advice_on_coding_approach/) (Score: 2)
    *   The thread discusses coding approaches for data engineering tasks, including the use of Python classes for ETL processes and mini-frameworks for outbound jobs.

14. [Career advice for a 21yo undergrad student](https://www.reddit.com/r/dataengineering/comments/1ilndjc/career_advice_for_a_21yo_undergrad_student/) (Score: 2)
    *   This thread provides links to learning resources and a community guide on transitioning to Data Engineering.

15. [Tiered data storage architecture advice needed](https://www.reddit.com/r/dataengineering/comments/1ilibel/tiered_data_storage_architecture_advice_needed/) (Score: 1)
    *   This thread simply has one user stating "Following".

16. [Need to design a data pipeline for audio for machine learning](https://www.reddit.com/r/dataengineering/comments/1ilkz54/need_to_design_a_data_pipeline_for_audio_for/) (Score: 1)
    *   This thread provides a link to learning resources and points out that for data pipelines, audio is just a file.

17. [How to use Optimize Tenser flow on Intel system for Intel?](https://www.reddit.com/r/dataengineering/comments/1il22aa/how_to_use_optimize_tenser_flow_on_intel_system/) (Score: 0)
    *   The thread discusses Intel-specific optimizations for TensorFlow and suggests reviewing the documentation.

18. [Data Processing](https://www.reddit.com/r/dataengineering/comments/1ilcngp/data_processing/) (Score: 0)
    *   The thread suggests using PySpark for data processing, even in Hadoop setups.

# Detailed Analysis by Thread
**[[D] Why do engineers break each metric into a separate CTE? (Score: 17)](https://www.reddit.com/r/dataengineering/comments/1iln487/why_do_engineers_break_each_metric_into_a/)**
*  **Summary:** The thread discusses the reasons behind breaking down metrics into separate CTEs (Common Table Expressions) in data engineering for readability, maintainability, and performance.
*  **Emotion:** The overall emotional tone of the thread is neutral, with most comments expressing objective viewpoints on the topic.
*  **Top 3 Points of View:**
    *   Breaking metrics into separate CTEs improves readability and maintainability of code.
    *   Separate CTEs make it easier to validate and test individual steps in the data model.
    *   Using separate CTEs supports the DRY (Don't Repeat Yourself) principle, especially when adding new metrics.

**[What level of System Design knowledge is required for a data engineer? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1ilcvr1/what_level_of_system_design_knowledge_is_required/)**
*  **Summary:** The thread discusses the necessary level of system design knowledge for data engineers, highlighting the balance between understanding key concepts and practical application.
*  **Emotion:** The emotional tone is generally positive and neutral, with users sharing their experiences and insights.
*  **Top 3 Points of View:**
    *   Basic understanding of system design concepts like load balancing is helpful.
    *   Focusing on automation and scalability yields better results.
    *   The required knowledge depends on the specific role and company.

**[DevOps to Data Engineering: Am I Escaping a Sinking Ship or Jumping Into a Bigger Fire? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1ilauju/devops_to_data_engineering_am_i_escaping_a/)**
*  **Summary:** This thread evaluates the pros and cons of moving from DevOps to Data Engineering, considering demand, pay, responsibilities, and career advancement.
*  **Emotion:** The emotional tone is mixed, with positive sentiment towards making the move, but some negative and neutral sentiments regarding the potential challenges.
*  **Top 3 Points of View:**
    *   Data Engineering can pay more but may involve being a "one-person army."
    *   DevOps and Data Engineering are both in demand.
    *   Learning the business domain is crucial for long-term success in Data Engineering.

**[How does your company's data architecture looks like? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1ilhvg5/how_does_your_companys_data_architecture_looks/)**
*  **Summary:** The thread describes various companies' data architectures, focusing on the technologies and patterns used.
*  **Emotion:** The tone is mostly neutral, with objective descriptions of the data architectures.
*  **Top 3 Points of View:**
    *   Many companies use a combination of Databricks, Azure, and Snowflake.
    *   The Medallion architecture is a common pattern.
    *   Architectures vary based on client needs and project requirements.

**[Is it possible to change Source of a adf pipeline dynamically?(eg from azure to sap ) (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1il7pcl/is_it_possible_to_change_source_of_a_adf_pipeline/)**
*  **Summary:** This thread discusses methods for dynamically changing the source of an ADF pipeline, with opinions on ADF's limitations.
*  **Emotion:** The thread's emotion is mostly neutral with some negative feelings about using ADF.
*  **Top 3 Points of View:**
    *   Create separate pipelines for each source and use a main pipeline to trigger the appropriate one.
    *   Use a config file with a source variable to determine the logic and connection.
    *   ADF can become a mess when trying to do advanced dynamic tasks.

**[Fellow engineers in Finance, what extra knowledge is helpful to get better roles/pay in Finance data domain (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1ile71k/fellow_engineers_in_finance_what_extra_knowledge/)**
*  **Summary:** The discussion revolves around the additional knowledge and skills that can improve career prospects for data engineers in the finance sector.
*  **Emotion:** The overall emotional tone is neutral, with a focus on providing informative advice.
*  **Top 3 Points of View:**
    *   A strong grasp of financial mathematics is beneficial.
    *   Knowledge of financial accounting fundamentals is valuable.
    *   Presentation, networking, and professional appearance are crucial.

**[Career Growth and Reflections of a Data Development Engineer (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1il55kf/career_growth_and_reflections_of_a_data/)**
*  **Summary:** The thread provides a list of community-submitted learning resources.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   (No specific points of view provided, as the comments are focused on linking to resources.)

**[Discover the Power of Spark Structured Streaming in Databricks (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ilfhl0/discover_the_power_of_spark_structured_streaming/)**
*  **Summary:** Discussion focuses on Spark Structured Streaming in Databricks, with a recommendation to investigate AWS integrations.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Spark Structured Streaming is a solid intro.
    *   Consider how it integrates with AWS services.

**[Why do small files in big data engines cause performance issues? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ilfmi2/why_do_small_files_in_big_data_engines_cause/)**
*  **Summary:** The thread explains the performance degradation caused by small files and suggests optimization strategies.
*  **Emotion:** Positive and Neutral
*  **Top 3 Points of View:**
    *   Small files degrade performance and increase storage costs.
    *   Automate file size optimization during ETL.
    *   This problem happens when other teams are in charge of partitioning the data and create small files.

**[How Do You Organize and Visualize Complex Data Processing Tasks? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ilb8gs/how_do_you_organize_and_visualize_complex_data/)**
*  **Summary:** Discusses methods to organize and visualize complex data processing, suggesting tools like dbt and Delta Live Tables.
*  **Emotion:** Neutral to Positive.
*  **Top 3 Points of View:**
    *   Use tools like dbt to solve the problem.
    *   Delta Live Tables are helpful for granular observability in Databricks.
    *   Unity Catalog is great for overall lineage.

**[How do you deal with uncertainty in planning? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ilm7io/how_do_you_deal_with_uncertainty_in_planning/)**
*  **Summary:** The conversation discusses techniques for dealing with uncertainty during planning, such as providing estimates with ranges.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Provide estimates with ranges.
    *   Include regular check points and force regular communication.
    *   Draw best and worst case scenarios for the managers to do the estimations.

**[Transitioning from Data Engineering to Data Science or AI (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ilohuo/transitioning_from_data_engineering_to_data/)**
*  **Summary:** This thread provides a link to a community guide on transitioning to Data Engineering.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   (No specific points of view provided, as the comments are focused on linking to resources.)

**[Need advice on coding approach. (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ilj0kl/need_advice_on_coding_approach/)**
*  **Summary:** This thread is about coding approaches for data engineering tasks, including the use of Python classes for ETL processes and mini-frameworks for outbound jobs.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Create Python classes for specific ETL processes.
    *   Dynamic approaches are the way to go!
    *   Create a "mini framework" for outbound jobs, and use asset bundles to orchestrate everything.

**[Career advice for a 21yo undergrad student (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ilndjc/career_advice_for_a_21yo_undergrad_student/)**
*  **Summary:** This thread provides links to learning resources and a community guide on transitioning to Data Engineering.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   (No specific points of view provided, as the comments are focused on linking to resources.)

**[Tiered data storage architecture advice needed (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ilibel/tiered_data_storage_architecture_advice_needed/)**
*  **Summary:** This thread simply has one user stating "Following".
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   (None, single comment indicates interest in the topic without providing a viewpoint.)

**[Need to design a data pipeline for audio for machine learning (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ilkz54/need_to_design_a_data_pipeline_for_audio_for/)**
*  **Summary:** This thread provides a link to learning resources and points out that for data pipelines, audio is just a file.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   For a data pipeline, audio is treated as a file, similar to xls.
    *   (Other comments are focused on linking to resources.)

**[How to use Optimize Tenser flow on Intel system for Intel? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1il22aa/how_to_use_optimize_tenser_flow_on_intel_system/)**
*  **Summary:** The thread discusses Intel-specific optimizations for TensorFlow and suggests reviewing the documentation.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    *   Intel-specific optimizations can be tricky.

**[Data Processing (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ilcngp/data_processing/)**
*  **Summary:** The thread suggests using PySpark for data processing, even in Hadoop setups.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   PySpark is suitable for data processing, even with Hadoop.
