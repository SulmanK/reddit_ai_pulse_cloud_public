---
title: "Data Engineering Subreddit"
date: "2025-07-01"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Is there a downside to adding an index at the start of a pipeline and removing it at the end?](https://www.reddit.com/r/dataengineering/comments/1lp130e/is_there_a_downside_to_adding_an_index_at_the/) (Score: 17)
    *   Users discuss the pros and cons of adding and removing indexes in a data pipeline, including performance considerations and potential blocking issues.
2.  [Has db-engine gone out of business? They haven't replied to my emails.](https://www.reddit.com/r/dataengineering/comments/1lovmfb/has_dbengine_gone_out_of_business_they_havent/) (Score: 15)
    *   Users discuss the status of db-engine, with some suggesting they might have been acquired by Redgate or are simply busy.
3.  [Would getting a masters in data science/engineering be worth it?](https://www.reddit.com/r/dataengineering/comments/1lopsgu/would_getting_a_masters_in_data/) (Score: 13)
    *   Users share their opinions and experiences regarding the value of a master's degree in data science or data engineering, with some questioning its immediate impact on job readiness.
4.  [Do any organizations block 100% Excel exports that contain PII data from Data Lake / Databricks / DWH? How do you balance investigation needs vs. data leakage risk?”](https://www.reddit.com/r/dataengineering/comments/1lot8t1/do_any_organizations_block_100_excel_exports_that/) (Score: 13)
    *   Users discuss strategies for preventing data leakage of PII from data lakes and warehouses, including blocking Excel exports and implementing secure environments.
5.  [High School Intern - Advice please](https://www.reddit.com/r/dataengineering/comments/1los4xa/high_school_intern_advice_please/) (Score: 5)
    *   Users offer advice to a high school intern in a data engineering role, focusing on networking, learning business fundamentals, and understanding the real-world work environment.
6.  [new SQL parameters syntax Databricks](https://www.reddit.com/r/dataengineering/comments/1lp01n3/new_sql_parameters_syntax_databricks/) (Score: 2)
    *   Users discuss new SQL parameter syntax in Databricks, sharing their experiences and preferred methods.
7.  [Anyone using PgDuckdb in Production?](https://www.reddit.com/r/dataengineering/comments/1lp5p2k/anyone_using_pgduckdb_in_production/) (Score: 2)
    *   A user asks if anyone is using PgDuckdb in production, and another user advises against it due to past stability issues.
8.  [Need Help: Building a "ChatGPT with My Data" System - Getting Limited Results](https://www.reddit.com/r/dataengineering/comments/1losykt/need_help_building_a_chatgpt_with_my_data_system/) (Score: 0)
    *   Users provide advice on building a "ChatGPT with My Data" system, suggesting approaches like using DuckDB for data retrieval and API wrappers for cost management.
9.  [Two offers of Europe and Abu Dhabi](https://www.reddit.com/r/dataengineering/comments/1lp53vp/two_offers_of_europe_and_abu_dhabi/) (Score: 0)
    *   Users discuss the pros and cons of job offers in Europe (specifically Ireland) and Abu Dhabi, considering factors like salary, passport requirements, and work culture.
10. [Missed the Microsoft Fabric certification DP 700 voucher any way to still get it?](https://www.reddit.com/r/dataengineering/comments/1lp8890/missed_the_microsoft_fabric_certification_dp_700/) (Score: 0)
    *   A user asks about obtaining a Microsoft Fabric certification voucher, and another user suggests cross-posting the question to related communities.
11. [Looking for learning buddy](https://www.reddit.com/r/dataengineering/comments/1lpbbha/looking_for_learning_buddy/) (Score: 0)
    *   A user is looking for a learning buddy, and another user expresses interest in collaborating, despite being a data analyst rather than a data engineer.

# Detailed Analysis by Thread
**[Is there a downside to adding an index at the start of a pipeline and removing it at the end? (Score: 17)](https://www.reddit.com/r/dataengineering/comments/1lp130e/is_there_a_downside_to_adding_an_index_at_the/)**
*  **Summary:**  The thread discusses the trade-offs of adding and removing indexes within a data pipeline. Concerns raised include the overhead of index creation/deletion, potential blocking of concurrent operations, and alternative solutions like temporary tables or leaving indexes in place.
*  **Emotion:** The emotional tone is primarily Neutral, with some Negative sentiments expressed regarding the potential downsides of index manipulation.
*  **Top 3 Points of View:**
    * Creating and deleting indexes can be time-consuming and might negate any performance gains.
    * Adding and dropping an index is a DDL operation that could block or be blocked by concurrent operations running on the table.
    * Consider using temporary tables with appropriate indexes instead of repeatedly creating and deleting indexes.

**[Has db-engine gone out of business? They haven't replied to my emails. (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1lovmfb/has_dbengine_gone_out_of_business_they_havent/)**
*  **Summary:** The thread revolves around the uncertainty regarding the status of db-engine, with users speculating on potential acquisition or internal issues.
*  **Emotion:** The emotional tone is predominantly Neutral, reflecting curiosity and uncertainty.
*  **Top 3 Points of View:**
    * db-engine might have been acquired by Redgate.
    * They could be undergoing an Oracle upgrade.
    * The unanswered emails could be a sign of inactivity or change.

**[Would getting a masters in data science/engineering be worth it? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1lopsgu/would_getting_a_masters_in_data/)**
*  **Summary:**  The thread explores the value of a master's degree in data science or data engineering. Some users share their experiences and opinions, with some questioning its immediate impact on job readiness.
*  **Emotion:** The emotional tone is mostly Neutral, with some Negative sentiments expressing doubts about the immediate value of the degree. There are a few positive sentiments.
*  **Top 3 Points of View:**
    * A master's degree can open doors and is seen as equivalent to 1-3 years of experience.
    * Many master's programs are cash cows and don't teach real-world skills.
    * Practical experience and self-learning are crucial regardless of having a degree.

**[Do any organizations block 100% Excel exports that contain PII data from Data Lake / Databricks / DWH? How do you balance investigation needs vs. data leakage risk?” (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1lot8t1/do_any_organizations_block_100_excel_exports_that/)**
*  **Summary:** The thread discusses ways to balance the need for fraud investigation with the risk of data leakage when PII is involved. The safest move is to leave Excel in place but run it inside a locked-down workspace.
*  **Emotion:** The emotional tone is primarily Neutral, focusing on practical solutions and risk mitigation. There are a few positive sentiments.
*  **Top 3 Points of View:**
    * Block downloads to OneDrive or local drives to prevent PII leakage.
    * Create secure environments, such as Citrix VDI, to run Excel and access data without exporting.
    * Implement strict data governance policies, including data masking, access controls, and monitoring of file sharing.

**[High School Intern - Advice please (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1los4xa/high_school_intern_advice_please/)**
*  **Summary:** Users offer advice to a high school intern in a data engineering role, focusing on networking, learning business fundamentals, and understanding the real-world work environment.
*  **Emotion:** The emotional tone is generally Positive, offering encouragement and practical suggestions.
*  **Top 3 Points of View:**
    * Networking is crucial for future internship and job opportunities.
    * Focus on understanding the business and processes rather than just the tools.
    * Don't worry about making mistakes, and be willing to learn and adapt.

**[new SQL parameters syntax Databricks (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lp01n3/new_sql_parameters_syntax_databricks/)**
*  **Summary:** Users discuss new SQL parameter syntax in Databricks, sharing their experiences and preferred methods.
*  **Emotion:** The emotional tone is primarily Neutral, with a hint of Positive sentiment in the shared blog post.
*  **Top 3 Points of View:**
    * Some users are using IDENTIFIER(:my_table_name).
    * Some users are using ||.
    * One user wrote a blog post about the challenges of using the syntax.

**[Anyone using PgDuckdb in Production? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lp5p2k/anyone_using_pgduckdb_in_production/)**
*  **Summary:**  A user asks if anyone is using PgDuckdb in production, and another user advises against it due to past stability issues.
*  **Emotion:** The emotional tone is Neutral overall, with a touch of Negative sentiment in the cautionary response.
*  **Top 3 Points of View:**
    * One user advises against using DuckDB in production.

**[Need Help: Building a "ChatGPT with My Data" System - Getting Limited Results (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1losykt/need_help_building_a_chatgpt_with_my_data_system/)**
*  **Summary:**  Users provide advice on building a "ChatGPT with My Data" system, suggesting approaches like using DuckDB for data retrieval and API wrappers for cost management.
*  **Emotion:** The emotional tone is Neutral, with some Negative sentiments concerning feasibility,
*  **Top 3 Points of View:**
    * It is not feasible to building a ChatGpt with your data system currently.
    * Don't cram the full CSV into one prompt and treat the LLM as a stateless analysis layer that pulls targeted slices on demand.
    * Move the data into duckdb, and have the agent run queries.

**[Two offers of Europe and Abu Dhabi (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lp53vp/two_offers_of_europe_and_abu_dhabi/)**
*  **Summary:**  Users discuss the pros and cons of job offers in Europe (specifically Ireland) and Abu Dhabi, considering factors like salary, passport requirements, and work culture.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Getting a western passport like Ireland, results in a much higher salary in the Middle East because many companies pay based on passport.
    * Stories from skilled foreign workers in the UAE would push towards Ireland.

**[Missed the Microsoft Fabric certification DP 700 voucher any way to still get it? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lp8890/missed_the_microsoft_fabric_certification_dp_700/)**
*  **Summary:**  A user asks about obtaining a Microsoft Fabric certification voucher, and another user suggests cross-posting the question to related communities.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Try cross-posting to other communities to increase the likelihood of getting help.

**[Looking for learning buddy (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1lpbbha/looking_for_learning_buddy/)**
*  **Summary:**  A user is looking for a learning buddy, and another user expresses interest in collaborating, despite being a data analyst rather than a data engineer.
*  **Emotion:** The emotional tone is Positive.
*  **Top 3 Points of View:**
    * A data analyst working on getting my feet into data engineering is up for building something if they don’t mind my level of expertise.
