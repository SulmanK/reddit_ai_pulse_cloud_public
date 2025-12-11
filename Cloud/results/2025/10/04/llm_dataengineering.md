---
title: "Data Engineering Subreddit"
date: "2025-10-04"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "databases", "AI"]
---

# Overall Ranking and Top Discussions
1.  [[D] How to deal with messy database?](https://www.reddit.com/r/dataengineering/comments/1nxshi2/how_to_deal_with_messy_database/) (Score: 32)
    * Discusses challenges of undocumented databases and strategies for analyzing them.
2.  [Writing large PySpark dataframes as JSON](https://www.reddit.com/r/dataengineering/comments/1nxcpzo/writing_large_pyspark_dataframes_as_json/) (Score: 25)
    * Discusses the best way to write dataframes, suggesting alternative methods for writing large PySpark dataframes as JSON.
3.  [What do we think about this post - "Why AI will fail without engineering principles?"](https://www.reddit.com/r/dataengineering/comments/1nxp7t3/what_do_we_think_about_this_post_why_ai_will_fail/) (Score: 9)
    *  Discusses the importance of engineering principles for successful AI implementation, questioning the idea of letting AI handle data quality issues.
4.  [First time doing an integration (API to ERP). Any tips from veterans?](https://www.reddit.com/r/dataengineering/comments/1nxxj0q/first_time_doing_an_integration_api_to_erp_any/) (Score: 5)
    *  Asks for tips and advice for a first-time API to ERP integration project.
5.  [MySQL + Excel Automation: IDEs or Tools with Complex Export Scripting?](https://www.reddit.com/r/dataengineering/comments/1ny1e63/mysql_excel_automation_ides_or_tools_with_complex/) (Score: 1)
    *  Asks for recommendations for IDEs or tools with complex export scripting for MySQL and Excel automation.
6.  [best practices for storing data from on premise server to cloud storage](https://www.reddit.com/r/dataengineering/comments/1ny091v/best_practices_for_storing_data_from_on_premise/) (Score: 0)
    *  Seeks advice on best practices for storing data from on-premise servers to cloud storage.

# Detailed Analysis by Thread
**[[D] How to deal with messy database? (Score: 32)](https://www.reddit.com/r/dataengineering/comments/1nxshi2/how_to_deal_with_messy_database/)**
*   **Summary:**  The thread discusses the common challenges of dealing with messy, undocumented databases, especially in healthcare. Users share strategies like breaking down the problem, documenting findings, talking to system maintainers, using schema visualization tools, and leveraging DBA support for query analysis.
*   **Emotion:** The emotional tone is mostly neutral, with users sharing experiences and offering practical advice.
*   **Top 3 Points of View:**
    *   Messy, undocumented databases are common, especially in industries like healthcare.
    *   Talking to people who maintain the systems is crucial for understanding the database structure and purpose.
    *   Visualizing the database schema using tools like dbdiagram.io can be helpful.

**[Writing large PySpark dataframes as JSON (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1nxcpzo/writing_large_pyspark_dataframes_as_json/)**
*   **Summary:** The thread discusses the challenges of writing large PySpark dataframes as JSON files and explores alternative file formats and methods for data transfer to Snowflake.
*   **Emotion:** The emotional tone is predominantly neutral, with users providing technical suggestions and questioning the original approach. There is a hint of negativity towards the JSON format.
*   **Top 3 Points of View:**
    *   JSON might not be the best format for large dataframes due to size and complexity.
    *   Alternative file formats like Parquet or Iceberg are recommended for Snowflake.
    *   Using the PySpark connector for Snowflake might be a more efficient solution.

**[What do we think about this post - "Why AI will fail without engineering principles?" (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1nxp7t3/what_do_we_think_about_this_post_why_ai_will_fail/)**
*   **Summary:** This thread discusses the importance of engineering principles in AI, particularly regarding data quality. Users react to a statement suggesting that AI models can handle data quality issues on their own.
*   **Emotion:** The emotional tone is predominantly neutral with a hint of skepticism.
*   **Top 3 Points of View:**
    *   Engineering principles are essential for successful AI, especially in ensuring data quality.
    *   It is wild to suggest that AI models should handle data quality without prior engineering principles being considered.
    *   AI could help eliminate tedious tasks, and save on costs.

**[First time doing an integration (API to ERP). Any tips from veterans? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1nxxj0q/first_time_doing_an_integration_api_to_erp_any/)**
*   **Summary:** This thread is a request for advice on integrating an API with an ERP system. Veterans are asked to share their tips and experiences.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Create a detailed design document, questioning every assumption and planning for potential failures.
    *   A Python script in a VM can be a lightweight solution.
    *   Consider using established technologies like Airflow or Dagster.

**[MySQL + Excel Automation: IDEs or Tools with Complex Export Scripting? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ny1e63/mysql_excel_automation_ides_or_tools_with_complex/)**
*   **Summary:**  The thread asks for tool recommendations for automating MySQL data export to Excel with complex scripting capabilities.
*   **Emotion:**  The emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    *   Python and DuckDB are recommended.
    *   Use whatever you're most comfortable with, Python or VBA.
    *   Some view the question as a meme post.

**[best practices for storing data from on premise server to cloud storage (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ny091v/best_practices_for_storing_data_from_on_premise/)**
*   **Summary:** The thread seeks best practices for moving data from on-premise servers to cloud storage, covering various aspects like ETL tools, data transfer methods, and cloud service selection.
*   **Emotion:** The emotional tone is neutral, with users offering detailed and practical advice.
*   **Top 3 Points of View:**
    *   There aren't universal "best practices".
    *   Consider using SSIS if you have a SQL Server license.
    *   Dagster and DBT for scheduled updates and processing.
