---
title: "Data Engineering Subreddit"
date: "2025-06-27"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Which sites, platforms or blogs do you regularly check to stay up to date, find insights, and satisfy your curiosity?](https://www.reddit.com/r/dataengineering/comments/1llee72/which_sites_platforms_or_blogs_do_you_regularly/) (Score: 42)
    *   People shared resources they use to stay informed about data engineering, including RSS feeds, blogs, and YouTube channels.
2.  [Do you use CDC? If yes, how does it benefit you?](https://www.reddit.com/r/dataengineering/comments/1llt6y9/do_you_use_cdc_if_yes_how_does_it_benefit_you/) (Score: 41)
    *   Users discussed the use of Change Data Capture (CDC) and its benefits, such as efficiency, cost savings, and capturing the evolution of data.
3.  [Would you take a $27K pay cut to land your first DE role?](https://www.reddit.com/r/dataengineering/comments/1llvqzs/would_you_take_a_27k_pay_cut_to_land_your_first/) (Score: 16)
    *   The discussion centered around whether it's worth taking a pay cut to enter the data engineering field, considering factors like career goals, current financial situation, and the potential for future growth.
4.  [Data Engineer or Software Engineer - Data](https://www.reddit.com/r/dataengineering/comments/1llv0oe/data_engineer_or_software_engineer_data/) (Score: 15)
    *   Users debated the nuances between the titles "Data Engineer" and "Software Engineer - Data," with many suggesting the distinction is minor and depends on the specific role and individual preferences.
5.  [How to debug dbt SQL?](https://www.reddit.com/r/dataengineering/comments/1llngh8/how_to_debug_dbt_sql/) (Score: 8)
    *   People shared tips and techniques for debugging dbt SQL, including inspecting compiled SQL, using logging functions, and checking query history in data warehouses.
6.  [Where do you store static element you need to?](https://www.reddit.com/r/dataengineering/comments/1llrd1d/where_do_you_store_static_element_you_need_to/) (Score: 8)
    *   The thread explored options for storing static data elements, with recommendations including relational databases, Airtable, and other tools that allow for easy editing and API access.
7.  [What problems did you solve as part of data engineering](https://www.reddit.com/r/dataengineering/comments/1llldd0/what_problems_did_you_solve_as_part_of_data/) (Score: 4)
    *   Users shared examples of problems they've solved in data engineering, such as allocating sales revenue to shipments and using Python and SQL for data movement.
8.  [Turning DBT snapshots into SCD2 Silver tables](https://www.reddit.com/r/dataengineering/comments/1llu6yc/turning_dbt_snapshots_into_scd2_silver_tables/) (Score: 2)
    *   The discussion focused on strategies for transforming dbt snapshots into SCD2 silver tables within a medallion architecture.
9.  [I built a multimodal document workflow system using VLMs - processes complex docs end-to-end](https://www.reddit.com/r/dataengineering/comments/1lllraf/i_built_a_multimodal_document_workflow_system/) (Score: 1)
    *   This post was a showcase of open-source projects related to data engineering.
10. [Opportunity to join start up I’m not politically aligned with](https://www.reddit.com/r/dataengineering/comments/1llcjy2/opportunity_to_join_start_up_im_not_politically/) (Score: 0)
    *   The thread discussed the ethical considerations of working for a startup whose political alignment differs from one's own.
11. [SQLite questions](https://www.reddit.com/r/dataengineering/comments/1llq8jw/sqlite_questions/) (Score: 0)
    *   The discussion centered around questions related to SQLite, specifically connecting SQLite to SQL Server.
12. [Biggest Pains in Current Tooling?](https://www.reddit.com/r/dataengineering/comments/1llvs04/biggest_pains_in_current_tooling/) (Score: 0)
    *   Users shared their biggest frustrations with current tooling, including the lack of OSS tools for versioning OLTP databases and the challenges of dealing with tech debt.

# Detailed Analysis by Thread
**[ [D] Which sites, platforms or blogs do you regularly check to stay up to date, find insights, and satisfy your curiosity? (Score: 42)](https://www.reddit.com/r/dataengineering/comments/1llee72/which_sites_platforms_or_blogs_do_you_regularly/)**
*   **Summary:**  Users share their go-to resources for staying up-to-date in the data engineering field, focusing on RSS feeds, specific blogs (Polars, DuckDB, Cloudflare), YouTube channels (Seattle Data Guy, Data with Zach), and even Reddit itself. The thread highlights the diverse range of sources data engineers use to learn and stay informed.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   RSS feeds are a less distracting way to consume news.
    *   YouTube channels and Databricks summit presentations are good for learning about real-world use cases.
    *   Tracking job positions can reveal current industry demands and new technologies.

**[Do you use CDC? If yes, how does it benefit you? (Score: 41)](https://www.reddit.com/r/dataengineering/comments/1llt6y9/do_you_use_cdc_if_yes_how_does_it_benefit_you/)**
*   **Summary:**  This thread explores the use of Change Data Capture (CDC) in data engineering. Contributors highlight its advantages over traditional snapshot methods, especially for large databases.  CDC is praised for its efficiency in capturing data changes, reducing costs, and providing a complete event lifecycle.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   CDC is more efficient than daily snapshots for large databases, saving time and resources.
    *   CDC captures the full evolution of data, unlike snapshots which only show point-in-time states.
    *   Tools like Debezium and Kafka Connect simplify CDC implementation.

**[Would you take a $27K pay cut to land your first DE role? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1llvqzs/would_you_take_a_27k_pay_cut_to_land_your_first/)**
*   **Summary:**  The core question is whether a $27,000 pay cut is justified to enter the Data Engineering field.  The discussion covers the job market, potential for future earnings, career goals, and personal financial situations.  Some argue that getting a foot in the door is crucial, while others advise against accepting a significant pay reduction.
*   **Emotion:** The overall emotional tone of the thread is Positive.
*   **Top 3 Points of View:**
    *   Taking a pay cut to enter data engineering is worthwhile if you're set on the career and can afford it, as it opens doors to higher future earnings.
    *   A $27k pay cut is significant and should be carefully considered based on current responsibilities, cost of living, and alternative opportunities within the current role.
    *   Negotiate with the potential employer to avoid a pay cut, emphasizing current salary and value.

**[Data Engineer or Software Engineer - Data (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1llv0oe/data_engineer_or_software_engineer_data/)**
*   **Summary:** The thread explores the distinction between the job titles "Data Engineer" and "Software Engineer - Data".  Most contributors believe the difference is negligible, with the specific responsibilities and the company culture being more important than the exact title.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   The distinction between "Data Engineer" and "Software Engineer - Data" is insignificant and doesn't matter much in practice.
    *   "Data Engineer" is more universally recognized for job searches.
    *   "Software Engineer - Data" might be preferable for those who want to emphasize their coding skills.

**[How to debug dbt SQL? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1llngh8/how_to_debug_dbt_sql/)**
*   **Summary:** This thread provides guidance on debugging dbt SQL code.  Suggestions include inspecting compiled SQL in the target folder, using the `dbt compile` command, leveraging logging functions within macros, and checking query history in the data warehouse.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Inspect the compiled SQL code in the `target` folder to see the final SQL being executed.
    *   Use `dbt compile` and logging functions within macros to understand the intermediate steps.
    *   Check the query history in the data warehouse to identify errors and performance issues.

**[Where do you store static element you need to? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1llrd1d/where_do_you_store_static_element_you_need_to/)**
*   **Summary:** The discussion revolves around the best practices for storing static data elements needed for data engineering tasks. The original poster is dealing with a scenario where data transformations require lookups based on country and region, and their current CSV-based solution is becoming too complex. Recommendations include using relational databases, Airtable, and other solutions that offer both a user-friendly interface and API access.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Using a relational database is a good approach when the static data becomes relational and too complicated for simple CSV files.
    *   Airtable is a user-friendly solution for storing and managing static data, providing a spreadsheet-like interface and a built-in REST API.
    *   A layer of SQL logic (using CASE statements) is needed to apply the static data to the input data and output the enhanced data to a second table/view.

**[What problems did you solve as part of data engineering (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1llldd0/what_problems_did_you_solve_as_part_of_data/)**
*   **Summary:** Users share examples of problems they have solved as data engineers. One example involves allocating sales revenue at a detailed level using shipment data, requiring handling numerous edge cases within Azure SQL Warehouses and ADF. The thread also touches on defining data engineering as a trade that uses tools like Python and SQL to move data around.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    * Data engineering can involve complex data allocation problems requiring creative solutions
    * Python and SQL are tools used in data engineering
    * One user admitted to not solving any problems after three months in their role.

**[Turning DBT snapshots into SCD2 Silver tables (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1llu6yc/turning_dbt_snapshots_into_scd2_silver_tables/)**
*   **Summary:** The thread discusses techniques for turning DBT snapshots into SCD2 silver tables. A user asks for advice on how to create a macro and if people have a better way of doing it.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    * It may be helpful if the original poster included the macro they created
    * It's not clear if the poster has a grasp on SCD2
    * Another user is curious if others have a better way of turning DBT snapshots into SCD2 silver tables.

**[I built a multimodal document workflow system using VLMs - processes complex docs end-to-end (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lllraf/i_built_a_multimodal_document_workflow_system/)**
*   **Summary:** This post references the community's open-source project showcase and encourages the user to submit their project.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    * N/A (Bot post)

**[Opportunity to join start up I’m not politically aligned with (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1llcjy2/opportunity_to_join_start_up_im_not_politically/)**
*   **Summary:**  The discussion centers on the ethical and practical considerations of accepting a job at a startup whose political views differ from the employee's. Opinions range from prioritizing personal values and avoiding such companies to separating personal beliefs from professional work and focusing on career advancement.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Personal values and ethical considerations should outweigh career opportunities, leading to a rejection of the job offer.
    *   Separate personal political beliefs from professional responsibilities, focusing on the work and career benefits.
    *   The current job market is tough, and it may be worthwhile to take the job temporarily while continuing to search for a better fit.

**[SQLite questions (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1llq8jw/sqlite_questions/)**
*   **Summary:** This thread discusses how to connect SQLite to SQL Server
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    * This is a bot post linking to community resources
    * Check ODBC driver version and connection string
    * Install a native SQLite ODBC driver, set up a System DSN that points at your .db file, and then in SQL Server create a Linked Server using the MSDASQL provider.

**[Biggest Pains in Current Tooling? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1llvs04/biggest_pains_in_current_tooling/)**
*   **Summary:** This post discusses the biggest issues in current tooling.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    * still almost no OSS tools to version and develop the insides of OLTP databases that are good, including stored procs etc
    * A different data type in the source data
    * Mine is less related to tooling and more about the absolute refusal to plan long term and/or address the ever growing tech debt.
