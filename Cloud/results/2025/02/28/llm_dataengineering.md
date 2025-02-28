---
title: "Data Engineering Subreddit"
date: "2025-02-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [What are the biggest problems in our field today?](https://www.reddit.com/r/dataengineering/comments/1j0elsz/what_are_the_biggest_problems_in_our_field_today/) (Score: 9)
    *   Discussing the prevalent issues in the data engineering field, including lack of domain knowledge, interview processes, tool proliferation, and vendor-driven architecture.
2.  [Self healing Data (ETL) pipelines! Does it exists already or could be a very good choice for MSc research project? Please guide.](https://www.reddit.com/r/dataengineering/comments/1j04guo/self_healing_data_etl_pipelines_does_it_exists/) (Score: 7)
    *   Exploring the concept of self-healing ETL pipelines, whether they currently exist, and their suitability as a research project.
3.  [Handling thousands of files?](https://www.reddit.com/r/dataengineering/comments/1j0btjb/handling_thousands_of_files/) (Score: 5)
    *   Seeking advice on effectively managing and processing large quantities of files, with suggestions including using Athena, Lambda, ClickHouse, S3 Glacier, and compaction strategies.
4.  [Dimensional model implementation in Power BI](https://www.reddit.com/r/dataengineering/comments/1j044ze/dimensional_model_implementation_in_power_bi/) (Score: 3)
    *   Discussing the feasibility and best practices for implementing dimensional models in Power BI, with recommendations for where data transformation should occur.
5.  [Multiple data in 1 fact](https://www.reddit.com/r/dataengineering/comments/1j06vl9/multiple_data_in_1_fact/) (Score: 3)
    *   Discussing if having multiple data points in one fact table is good, and detailing the use of the practice in documentation.
6.  [Is it worth getting a Data Engineering Master's if I already have a Computer Engineering degree and want to switch to Data Engineering?](https://www.reddit.com/r/dataengineering/comments/1j0f75w/is_it_worth_getting_a_data_engineering_masters_if/) (Score: 3)
    *   Debating the value of a Data Engineering Master's degree for someone with a Computer Engineering background, with arguments for practical experience and self-study.
7.  [Building a Data Pipeline for Scientific Instruments – SDMS vs Internal Storage(Data lakes/Data Warehouse, SQL/Blob storage) ?](https://www.reddit.com/r/dataengineering/comments/1j048rb/building_a_data_pipeline_for_scientific/) (Score: 2)
    *   Comparing SDMS solutions with internal storage options (data lakes, warehouses, SQL/Blob storage) for building data pipelines for scientific instruments.
8.  [Advice for our stack](https://www.reddit.com/r/dataengineering/comments/1j07xxd/advice_for_our_stack/) (Score: 2)
    *   Seeking recommendations on the best data stack, with suggestions ranging from Snowflake to local DuckDB and custom Python code.
9.  [I created a unit testing framework for Dataform](https://www.reddit.com/r/dataengineering/comments/1j0bi23/i_created_a_unit_testing_framework_for_dataform/) (Score: 2)
    *   Sharing a newly created unit testing framework for Dataform.
10. [Complexity in data integration / ETL solutions?](https://www.reddit.com/r/dataengineering/comments/1j0dl14/complexity_in_data_integration_etl_solutions/) (Score: 2)
    *   Discussing the complexity of ETL solutions.
11. [Which path should I choose?](https://www.reddit.com/r/dataengineering/comments/1j0gfaf/which_path_should_i_choose/) (Score: 2)
    *   Questioning what path to choose for a career.
12. [How Have Your Data Engineering Skills Helped Outside Work?](https://www.reddit.com/r/dataengineering/comments/1j0gxd0/how_have_your_data_engineering_skills_helped/) (Score: 2)
    *   Sharing an example where DE skills have helped set up a movie server outside of work.
13. [Struggling with flink](https://www.reddit.com/r/dataengineering/comments/1j06dxo/struggling_with_flink/) (Score: 1)
    *   Discussing struggles with Flink
14. [Data engineering end of study internship](https://www.reddit.com/r/dataengineering/comments/1j07wy5/data_engineering_end_of_study_internship/) (Score: 1)
    *   Discussing a data engineering end of study internship and to get hands on with visualization tools.
15. [dumb question about SQL dbs](https://www.reddit.com/r/dataengineering/comments/1j0hhau/dumb_question_about_sql_dbs/) (Score: 1)
    *   Questioning SQL dbs usage for small datasets.

# Detailed Analysis by Thread
**[What are the biggest problems in our field today? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1j0elsz/what_are_the_biggest_problems_in_our_field_today/)**
*   **Summary:** This thread discusses the main challenges in the data engineering field. It highlights issues such as the lack of domain knowledge among data engineers, the impracticality of LeetCode-style interviews, the overwhelming number of tools and technologies to learn, marketing exaggerating tool capabilities, the lack of standardization in tooling, and the difficulty in defining specialized roles within data engineering.
*   **Emotion:** The emotional tone is predominantly neutral, reflecting informative and objective commentary on the state of the field. A slight negative sentiment is noticeable due to the problems being discussed.
*   **Top 3 Points of View:**
    *   The lack of domain knowledge is a significant hurdle for data engineers.
    *   The current interview process is flawed, with an over-reliance on LeetCode-style questions.
    *   The sheer number of tools and the aggressive marketing of new technologies create confusion and hinder progress.

**[Self healing Data (ETL) pipelines! Does it exists already or could be a very good choice for MSc research project? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1j04guo/self_healing_data_etl_pipelines_does_it_exists/)**
*   **Summary:** This thread explores the concept of "self-healing" data pipelines, questioning if they exist and their feasibility as an MSc research project. It touches on the use of ML for filling missing values, anomaly detection, and error recovery, with skepticism about modifying authoritative data with non-authoritative values.
*   **Emotion:** The emotional tone is mainly neutral and inquisitive, but there's also some skepticism and caution regarding the implementation of self-healing mechanisms, particularly the use of ML to fill missing values.
*   **Top 3 Points of View:**
    *   Using machine learning to fill missing values in data could compromise data integrity.
    *   Anomaly detection should be performed separately from ETL pipelines.
    *   Robust infrastructure is essential but can be achieved without Kubernetes.

**[Handling thousands of files? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1j0btjb/handling_thousands_of_files/)**
*   **Summary:** The thread discusses strategies for handling thousands of files, particularly in a data engineering context. Suggestions include using Athena or Lambda to bundle files, importing to ClickHouse, and employing compaction strategies. Other suggestions were to move files to Glacier or delete old files.
*   **Emotion:** The emotional tone is neutral, providing practical and technical advice on data management.
*   **Top 3 Points of View:**
    *   Compacting smaller files into larger ones periodically is an effective strategy.
    *   Using Athena or Lambda to bundle files into larger parquet files.
    *   Moving older, unneeded files to S3 Glacier cold storage.

**[Dimensional model implementation in Power BI (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1j044ze/dimensional_model_implementation_in_power_bi/)**
*   **Summary:** This thread analyzes how to implement a dimensional model in Power BI and suggests that data should be transformed as far upstream as possible. It explores several options and considers the advantages and disadvantages of using DAX, Power Query, SQL, or creating fact & dim views on the server.
*   **Emotion:** The emotional tone is neutral with a hint of negative based on recommendations to not use DAX.
*   **Top 3 Points of View:**
    *   Transform data as far upstream as possible.
    *   Avoid using DAX for data transformation in Power BI.
    *   Consider Power BI Dataflows Gen2 for data transformations.

**[Multiple data in 1 fact (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1j06vl9/multiple_data_in_1_fact/)**
*   **Summary:** The main point of this thread is to say having multiple data points in a single fact table is an acceptable practice, as long as the practice is detailed in any accompanying documentation.
*   **Emotion:** The emotional tone is neutral and informative.
*   **Top 3 Points of View:**
    *   Having multiple data in 1 fact is acceptable
    *   Having the practice detailed in the accompanying documentation is important

**[Is it worth getting a Data Engineering Master's if I already have a Computer Engineering degree and want to switch to Data Engineering? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1j0f75w/is_it_worth_getting_a_data_engineering_masters_if/)**
*   **Summary:** The central debate revolves around whether a Data Engineering Master's is beneficial for someone already holding a Computer Engineering degree. The consensus leans toward gaining practical experience and self-study over formal education.
*   **Emotion:** The emotional tone is mixed, with some positive sentiment towards practical experience and self-study, and negative sentiment suggesting formal education is not always necessary.
*   **Top 3 Points of View:**
    *   Practical experience and self-study are more valuable than a Master's degree.
    *   A Computer Engineering degree is often sufficient for a Data Engineering role.
    *   Job interviews can help map the field.

**[Building a Data Pipeline for Scientific Instruments – SDMS vs Internal Storage(Data lakes/Data Warehouse, SQL/Blob storage) ? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j048rb/building_a_data_pipeline_for_scientific/)**
*   **Summary:** The thread discusses whether to use an out-of-the-box SDMS solution or build an internal storage solution for scientific instrument data, with a focus on value, flexibility, and transparency.
*   **Emotion:** The emotional tone is generally positive and informative, with a slight caution regarding vendor solutions.
*   **Top 3 Points of View:**
    *   If an out-of-the-box solution meets all needs and allows easy data extraction, it's often worthwhile for simplicity.
    *   Building an internal solution provides more flexibility and transparency but requires technical expertise and support.
    *   Vendors should be questioned if their product allows access to ALL of the data

**[Advice for our stack (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j07xxd/advice_for_our_stack/)**
*   **Summary:** Users seek advice on their data stack. Responses ranged from recommending Snowflake to suggesting local DuckDB and custom python code.
*   **Emotion:** The emotional tone is generally positive and informative.
*   **Top 3 Points of View:**
    *   Airbyte has issues
    *   For small datasets, local duckdb, pandas and custom python code are cheap and will work
    *   Snowflake is recommended

**[I created a unit testing framework for Dataform (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j0bi23/i_created_a_unit_testing_framework_for_dataform/)**
*   **Summary:** A user shares a unit testing framework.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Sharing an open source project

**[Complexity in data integration / ETL solutions? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j0dl14/complexity_in_data_integration_etl_solutions/)**
*   **Summary:** A user offers a user-interface suggestion for ETL solutions.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Text annotation would be useful for the UI

**[Which path should I choose? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j0gfaf/which_path_should_i_choose/)**
*   **Summary:** The user inquires on what path they should take.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The developer role will make more money.
    *   The modeling role will make more impact.

**[How Have Your Data Engineering Skills Helped Outside Work? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1j0gxd0/how_have_your_data_engineering_skills_helped/)**
*   **Summary:** A user's data engineering skills helped set up a movie server.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   DE skills can help automate setting up a movie server.

**[Struggling with flink (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1j06dxo/struggling_with_flink/)**
*   **Summary:** A user struggles with flink, so other users ask if flink is needed.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Is flink a requirement?

**[Data engineering end of study internship (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1j07wy5/data_engineering_end_of_study_internship/)**
*   **Summary:** Users were recommended to get hands on visualization tool like Tableau or PBI.
*   **Emotion:** The emotional tone is positive.
*   **Top 3 Points of View:**
    *   Try get hands on visualization tool like Tableau or PBI.
    *   Work on data storytelling for stakeholders.

**[dumb question about SQL dbs (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1j0hhau/dumb_question_about_sql_dbs/)**
*   **Summary:** SQL database is not recommended for small datasets.
*   **Emotion:** The emotional tone is positive.
*   **Top 3 Points of View:**
    *   Parquet files are recommended for datasets 500 rows or less
