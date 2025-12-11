---
title: "Data Engineering Subreddit"
date: "2025-10-03"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "azure", "python"]
---

# Overall Ranking and Top Discussions
1.  [[D] Replace Data Factory with python?](https://www.reddit.com/r/dataengineering/comments/1nws1e8/replace_data_factory_with_python/) (Score: 29)
    * This thread discusses the possibility and methods of replacing Azure Data Factory with Python for data engineering tasks.

2.  [Explain Azure Data Engineering project in the real-life corporate world.](https://www.reddit.com/r/dataengineering/comments/1nwp1wp/explain_azure_data_engineering_project_in_the/) (Score: 22)
    *  The conversation centers around explaining Azure Data Engineering projects in a real-world corporate setting, focusing on the roles of ADF, Databricks, and Synapse.

3.  [Feeling stuck and at a cross road](https://www.reddit.com/r/dataengineering/comments/1nx34fr/feeling_stuck_and_at_a_cross_road/) (Score: 11)
    *  The thread discusses a Business Analyst's potential transition to a Data Engineer role.

4.  [Conversion to Fabric](https://www.reddit.com/r/dataengineering/comments/1nwm4fg/conversion_to_fabric/) (Score: 6)
    *  This thread explores the adoption of Microsoft Fabric, with discussions on its benefits and drawbacks compared to alternatives like Snowflake and Databricks.

5.  [Best GUI-based Cloud ETL/ELT](https://www.reddit.com/r/dataengineering/comments/1nx25u5/best_guibased_cloud_etlelt/) (Score: 5)
    *  The discussion revolves around recommending the best GUI-based Cloud ETL/ELT tools, with mentions of Azure Data Factory, Matillion, and others.

6.  [Continue as a tool based MDM Developer 3.5 YOE or Switch to core data engineering? Detailed post](https://www.reddit.com/r/dataengineering/comments/1nwf67i/continue_as_a_tool_based_mdm_developer_35_yoe_or/) (Score: 3)
    *  The thread seeks advice on whether to continue as a tool-based MDM developer or switch to core data engineering.

7.  [Feedback on self learning / project work](https://www.reddit.com/r/dataengineering/comments/1nwtxhz/feedback_on_self_learning_project_work/) (Score: 3)
    *   The user seeks feedback on self-learning projects and advice on how to improve their projects to be recognized by potential employers.

8.  [Rough DE day](https://www.reddit.com/r/dataengineering/comments/1nwp2l2/rough_de_day/) (Score: 2)
    *   The thread discusses issues related to database performance and optimization within a data engineering context.

9.  [Quick Q: How are you all using Fivetran History Mode](https://www.reddit.com/r/dataengineering/comments/1nx5fx1/quick_q_how_are_you_all_using_fivetran_history/) (Score: 2)
    *  The conversation focuses on how Fivetran users are utilizing its history mode for data tracking and versioning, with confirmation that it implements SCD Type 2.

10. [Need advice on career progression while juggling uni, moving to germany, wanting to to possobly start contract work/startup](https://www.reddit.com/r/dataengineering/comments/1nwu2oe/need_advice_on_career_progression_while_juggling/) (Score: 0)
    *   The thread seeks advice on career progression while juggling university, moving to Germany, and potential contract work/startup ventures, focusing on prioritization and avoiding burnout.

# Detailed Analysis by Thread
**[[D] Replace Data Factory with python? (Score: 29)](https://www.reddit.com/r/dataengineering/comments/1nws1e8/replace_data_factory_with_python/)**
*  **Summary:**  The thread discusses the possibility and methods of replacing Azure Data Factory with Python for data engineering tasks, with suggestions for tools like Dagster, dlt, and custom Python scripts.
*  **Emotion:** The overall emotional tone is neutral, with some positive sentiment expressed towards Python-based solutions. Some negative sentiment is seen towards ADF.
*  **Top 3 Points of View:**
    * Python, along with tools like Dagster and dlt, can be a good replacement for ADF.
    * Replacing ADF with Python requires more upfront work but offers more flexibility.
    * Data Factory is useful for native connectors, while Python scripts can handle specific tasks like ingestion and format changes.

**[Explain Azure Data Engineering project in the real-life corporate world. (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1nwp1wp/explain_azure_data_engineering_project_in_the/)**
*  **Summary:**  The conversation centers around explaining Azure Data Engineering projects in a real-world corporate setting, focusing on the roles of ADF, Databricks, and Synapse, and emphasizing the importance of data contracts and SLAs.
*  **Emotion:** Neutral overall, with a focus on practical advice and best practices.
*  **Top 3 Points of View:**
    * ADF orchestrates, Databricks transforms on Delta, and Synapse serves as the serving layer.
    * Building a small POC version of the platform is crucial for understanding how it all fits together.
    * Understanding reporting requirements helps in designing appropriate data models.

**[Feeling stuck and at a cross road (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1nx34fr/feeling_stuck_and_at_a_cross_road/)**
*  **Summary:**  The thread discusses a Business Analyst's potential transition to a Data Engineer role.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    * Business Analyst is ready for Data Engineer opportunities.
    * Should test the waters and look for a new job.

**[Conversion to Fabric (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1nwm4fg/conversion_to_fabric/)**
*  **Summary:**  This thread explores the adoption of Microsoft Fabric, with discussions on its benefits and drawbacks compared to alternatives like Snowflake and Databricks.
*  **Emotion:** Neutral, with some users expressing skepticism about Fabric while others find it suitable for specific use cases.
*  **Top 3 Points of View:**
    * Fabric is only suitable for confined business areas like reporting, not as a central data platform.
    * Fabric adoption is primarily driven by Power BI licensing savings and tighter governance.
    * Fabric is adequate if everything in the ms365 suite works fine.

**[Best GUI-based Cloud ETL/ELT (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1nx25u5/best_guibased_cloud_etlelt/)**
*  **Summary:**  The discussion revolves around recommending the best GUI-based Cloud ETL/ELT tools, with mentions of Azure Data Factory, Matillion, and others.
*  **Emotion:** Neutral, with a mix of opinions on the usefulness and limitations of GUI-based tools.
*  **Top 3 Points of View:**
    * GUI tools are generally terrible, especially for complex transformations, and are discouraged by some.
    * SQL-based frameworks like dbt/bruin are recommended for easier debugging and development.
    * Several GUI-based tools such as Azure Data Factory, Matillion, Coalesce.io, IICS, IBM Cloud Pak DataStage, and Apache Hop are suggested.

**[Continue as a tool based MDM Developer 3.5 YOE or Switch to core data engineering? Detailed post (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1nwf67i/continue_as_a_tool_based_mdm_developer_35_yoe_or/)**
*  **Summary:**  The thread seeks advice on whether to continue as a tool-based MDM developer or switch to core data engineering.
*  **Emotion:** Neutral overall.
*  **Top 3 Points of View:**
    * If you want to go into DE, go and try DE.

**[Feedback on self learning / project work (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1nwtxhz/feedback_on_self_learning_project_work/)**
*  **Summary:**  The user seeks feedback on self-learning projects and advice on how to improve their projects to be recognized by potential employers.
*  **Emotion:** Neutral overall.
*  **Top 3 Points of View:**
    * Focus on projects that interest you.
    * Speak to recruiters and build rapport.
    * Get experience before certifications.

**[Rough DE day (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1nwp2l2/rough_de_day/)**
*  **Summary:**  The thread discusses issues related to database performance and optimization within a data engineering context.
*  **Emotion:** Neutral overall, with a focus on problem-solving and technical advice.
*  **Top 3 Points of View:**
    * There is a problem with the way the SQZl in the view is written.
    * The view if failing was not coded correctly and needs to be rewritten.
    * Make it the DBA's problem if you are not a DBE or optimization specialist.

**[Quick Q: How are you all using Fivetran History Mode (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1nx5fx1/quick_q_how_are_you_all_using_fivetran_history/)**
*  **Summary:**  The conversation focuses on how Fivetran users are utilizing its history mode for data tracking and versioning, with confirmation that it implements SCD Type 2.
*  **Emotion:** Neutral and informative.
*  **Top 3 Points of View:**
    * Fivetran's history mode implements SCD Type 2.

**[Need advice on career progression while juggling uni, moving to germany, wanting to to possobly start contract work/startup (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nwu2oe/need_advice_on_career_progression_while_juggling/)**
*  **Summary:**  The thread seeks advice on career progression while juggling university, moving to Germany, and potential contract work/startup ventures, focusing on prioritization and avoiding burnout.
*  **Emotion:** Neutral, with an element of concern regarding the user's potential burnout.
*  **Top 3 Points of View:**
    * Prioritize finishing your degree.
    * Reduce the number of concurrent projects to avoid burnout.
    * Fluent German is important for most companies in Germany.
