---
title: "Data Engineering Subreddit"
date: "2025-06-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Dealing with being burnt out](https://www.reddit.com/r/dataengineering/comments/1ldnhzm/dealing_with_being_burnt_out/) (Score: 11)
    * Discussing strategies for coping with burnout in the field of data engineering.
2.  ["Start right. Shift left." Is that just another marketing gimmick in data engineering?](https://www.reddit.com/r/dataengineering/comments/1ldtqzt/start_right_shift_left_is_that_just_another/) (Score: 9)
    * Discussing "Start Right, Shift Left" approach.
3.  [What's your fail-safe for raw ingested data?](https://www.reddit.com/r/dataengineering/comments/1ldoodt/whats_your_failsafe_for_raw_ingested_data/) (Score: 7)
    *  Discussing different fail-safe mechanisms for raw ingested data.
4.  [Blog: You Can't Have an AI Strategy Without a Data Strategy](https://www.reddit.com/r/dataengineering/comments/1ldpc65/blog_you_cant_have_an_ai_strategy_without_a_data/) (Score: 7)
    * Discussion about the blog post which highlights the importance of data strategy in AI implementation.
5.  [Fun resources for getting better at the basics](https://www.reddit.com/r/dataengineering/comments/1ldp6p7/fun_resources_for_getting_better_at_the_basics/) (Score: 4)
    *  Users share fun resources for improving data engineering fundamentals.
6.  [Is an Azure-Focused BI Developer Role a Good Stepping Stone to Data Engineering?](https://www.reddit.com/r/dataengineering/comments/1ldslel/is_an_azurefocused_bi_developer_role_a_good/) (Score: 3)
    * Discussing the transition from Azure BI Developer to Data Engineering.
7.  [A simple toy RDBMS in Rust (for Learning)](https://www.reddit.com/r/dataengineering/comments/1ldtkg3/a_simple_toy_rdbms_in_rust_for_learning/) (Score: 3)
    * Discussing a simple relational database management system (RDBMS) built in Rust for learning purposes.
8.  [Efficient data transfer between systems is critical for modern applications. Dragonfly and Airbyte](https://www.dragonflydb.io/blog/syncing-data-from-postgresql-to-dragonfly-using-airbyte) (Score: 2)
    *  Data transfer between systems is critical for modern applications.
9.  [csv data export mapping to own data structure using AI/LLM](https://www.reddit.com/r/dataengineering/comments/1ldo7sf/csv_data_export_mapping_to_own_data_structure/) (Score: 2)
    *  Discussing using AI/LLM for mapping CSV data exports to custom data structures.
10. [Microsoft Certified Azure Fundamentals-Is it worth getting?](https://www.reddit.com/r/dataengineering/comments/1ldt7ai/microsoft_certified_azure_fundamentalsis_it_worth/) (Score: 2)
    * Discussing the value of the Microsoft Certified Azure Fundamentals certification.
11. [your view on testing data pipelines?](https://www.reddit.com/r/dataengineering/comments/1ldwbhd/your_view_on_testing_data_pipelines/) (Score: 2)
    * Discussing strategies and approaches for testing data pipelines.
12. [Im building a Scalable Analytics Dashboard for 28M+ Rows, Is ADX a good option?](https://www.reddit.com/r/dataengineering/comments/1lds0hi/im_building_a_scalable_analytics_dashboard_for/) (Score: 1)
    * Discussing the suitability of Azure Data Explorer (ADX) for building a scalable analytics dashboard.
13. [Courses and certifications for a Data Engineering and BI team?](https://www.reddit.com/r/dataengineering/comments/1ldw7nm/courses_and_certifications_for_a_data_engineering/) (Score: 1)
    * Users requesting recommendations for courses and certifications for a data engineering and BI team.
14. [Masters needed?](https://www.reddit.com/r/dataengineering/comments/1ldpjtw/masters_needed/) (Score: 0)
    *  Discussing whether a master's degree is necessary to advance in data engineering.
15. [Helping analysts automate pipelines without giving them Docker, Python, or Airbyte](https://www.reddit.com/r/dataengineering/comments/1ldvqst/helping_analysts_automate_pipelines_without/) (Score: 0)
    *  Discussing methods for analysts to automate data pipelines without using Docker, Python, or Airbyte.
16. [Advice for MSc AI Graduate Looking to Break Into Data Engineering — What Pathways or Skills Should I Focus On?](https://www.reddit.com/r/dataengineering/comments/1ldw4pj/advice_for_msc_ai_graduate_looking_to_break_into/) (Score: 0)
    *  Seeking advice for transitioning from an MSc in AI to a career in data engineering.

# Detailed Analysis by Thread
**[Dealing with being burnt out (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1ldnhzm/dealing_with_being_burnt_out/)**
*  **Summary:**  Users discuss strategies for coping with burnout in the field of data engineering, including therapy, company changes, and self-optimization.
*  **Emotion:** The thread has mixed emotions, with neutral dominating, and some expressions of positive reinforcement regarding potential solutions.
*  **Top 3 Points of View:**
    * Getting therapy to address internal battles causing burnout.
    *  Changing companies to find a better environment.
    * Focus on self-optimization and improvement rather than comparing oneself to others.

**["Start right. Shift left." Is that just another marketing gimmick in data engineering? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1ldtqzt/start_right_shift_left_is_that_just_another/)**
*  **Summary:** The thread discusses the concept of "Start Right, Shift Left" in data engineering, debating whether it's a useful approach or just a marketing gimmick. The consensus is that it emphasizes early problem discovery and resolution to minimize downstream impact.
*  **Emotion:** The emotional tone of the thread is predominantly neutral, with users rationally discussing the concept.
*  **Top 3 Points of View:**
    * "Start Right, Shift Left" is not a gimmick but a practical approach to solve problems early in the development cycle.
    * It's about shifting bits for scale and growth.
    *  It's an ideal that is rarely executed correctly in real-world data teams due to immediate needs and workarounds.

**[What's your fail-safe for raw ingested data? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ldoodt/whats_your_failsafe_for_raw_ingested_data/)**
*  **Summary:** Users share their strategies for ensuring data durability and recoverability, including using data lakes, versioning, and monitoring tools.
*  **Emotion:** The emotional tone is neutral, with users matter-of-factly describing their fail-safe mechanisms.
*  **Top 3 Points of View:**
    * Employing a data lake with raw data stored in S3, triggering events to load data into a landing zone.
    * Utilizing Snowflake Time Travel for data history and rollback capabilities.
    * Implementing monitoring tools like Monte Carlo to detect unexpected data modifications or drops.

**[Blog: You Can't Have an AI Strategy Without a Data Strategy (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ldpc65/blog_you_cant_have_an_ai_strategy_without_a_data/)**
*  **Summary:**  The thread discusses a blog post about the necessity of a data strategy for AI implementation. Commenters find the content high-level and lacking in-depth analysis.
*  **Emotion:** The thread has a positive emotional tone, but there is disappointment with the blog's depth and practicality.
*  **Top 3 Points of View:**
    * The blog post is too high-level and lacks substantial content.
    *  A data strategy must connect business outcomes to the technology being used.
    *  The blog focuses more on IT aspects than on comprehensive data strategy components like data governance, business alignment, and security.

**[Fun resources for getting better at the basics (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ldp6p7/fun_resources_for_getting_better_at_the_basics/)**
*  **Summary:**  This thread is a pointer to community submitted learning resources.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * Pointing users to a wiki for learning resources.

**[Is an Azure-Focused BI Developer Role a Good Stepping Stone to Data Engineering? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ldslel/is_an_azurefocused_bi_developer_role_a_good/)**
*  **Summary:** The thread discusses the transition from an Azure BI Developer role to a Data Engineering role.
*  **Emotion:** The thread has neutral and positive emotional tone.
*  **Top 3 Points of View:**
    * Titles don't matter, pursue the tech and experience.
    * Pointing users to a guide on transitioning to Data Engineering.

**[A simple toy RDBMS in Rust (for Learning) (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1ldtkg3/a_simple_toy_rdbms_in_rust_for_learning/)**
*  **Summary:** Discussing a simple relational database management system (RDBMS) built in Rust for learning purposes.
*  **Emotion:** The thread has positive and neutral emotional tone.
*  **Top 3 Points of View:**
    * ResortApprehensive72 shared his project with Sadservers.com.
    * Pointing users to an open-source project showcase.

**[Efficient data transfer between systems is critical for modern applications. Dragonfly and Airbyte (Score: 2)](https://www.dragonflydb.io/blog/syncing-data-from-postgresql-to-dragonfly-using-airbyte)**
*  **Summary:** Airbyte’s connector game is strong. This setup beats wrangling custom scripts any day.
*  **Emotion:** The thread has a positive emotional tone.
*  **Top 3 Points of View:**
    * Airbyte’s connector game is strong.

**[csv data export mapping to own data structure using AI/LLM (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ldo7sf/csv_data_export_mapping_to_own_data_structure/)**
*  **Summary:** In 80% of the cases, the mapping of variable names to their description was done with LLM.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * In 80% of the cases, the mapping of variable names to their description was done with LLM.

**[Microsoft Certified Azure Fundamentals-Is it worth getting? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ldt7ai/microsoft_certified_azure_fundamentalsis_it_worth/)**
*  **Summary:** Discussing the value of the Microsoft Certified Azure Fundamentals certification.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * AZ-900 is very easy and given to Azure new comers as a required course in the first month.
    * Technically, It’s useless but some employers like seeing certificates.

**[your view on testing data pipelines? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ldwbhd/your_view_on_testing_data_pipelines/)**
*  **Summary:** Discussing strategies and approaches for testing data pipelines.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * why are you testing with large data? if it’s a e2e test, it should write where the destination is, otherwise integration test should be subset and unit test should be mock data

**[Im building a Scalable Analytics Dashboard for 28M+ Rows, Is ADX a good option? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lds0hi/im_building_a_scalable_analytics_dashboard_for/)**
*  **Summary:** Discussing the suitability of Azure Data Explorer (ADX) for building a scalable analytics dashboard.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * You can process 28million records with a standard relational database. Probably Azure SQL Server will be enough for your needs.

**[Courses and certifications for a Data Engineering and BI team? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ldw7nm/courses_and_certifications_for_a_data_engineering/)**
*  **Summary:** Users requesting recommendations for courses and certifications for a data engineering and BI team.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * Pointing users to a wiki for learning resources.

**[Masters needed? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ldpjtw/masters_needed/)**
*  **Summary:** Discussing whether a master's degree is necessary to advance in data engineering.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * Masters are not needed. Corporate certification, such as from AWS or Microsoft is a must.

**[Helping analysts automate pipelines without giving them Docker, Python, or Airbyte (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ldvqst/helping_analysts_automate_pipelines_without/)**
*  **Summary:** Discussing methods for analysts to automate data pipelines without using Docker, Python, or Airbyte.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * How is that good if you are locked to the Google Sheets service?

**[Advice for MSc AI Graduate Looking to Break Into Data Engineering — What Pathways or Skills Should I Focus On? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ldw4pj/advice_for_msc_ai_graduate_looking_to_break_into/)**
*  **Summary:** Seeking advice for transitioning from an MSc in AI to a career in data engineering.
*  **Emotion:** The thread has a neutral emotional tone.
*  **Top 3 Points of View:**
    * Pointing users to a guide on transitioning to Data Engineering.
