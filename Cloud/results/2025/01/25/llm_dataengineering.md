---
title: "Data Engineering Subreddit"
date: "2025-01-25"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "airflow", "etl"]
---

# Overall Ranking and Top Discussions
1.  [HOLD UP!! Airflow's secret weapon to slash AWS costs that nobody talks about!](https://www.reddit.com/r/dataengineering/comments/1i9k5ah/hold_up_airflows_secret_weapon_to_slash_aws_costs/) (Score: 113)
    *   Users discussed how to optimize Airflow to reduce AWS costs, focusing on fetching secrets within tasks instead of DAG processor.
2.  [How to approach data engineering systems design](https://www.reddit.com/r/dataengineering/comments/1i9o5hn/how_to_approach_data_engineering_systems_design/) (Score: 27)
    *   Users shared and thanked the poster for sharing tips and ideas on data engineering systems design.
3.  [Which industries view data engineering as a revenue driver rather than just a compliance expense?](https://www.reddit.com/r/dataengineering/comments/1i9o4y3/which_industries_view_data_engineering_as_a/) (Score: 17)
    *   Users discussed which industries value data engineering as a revenue driver, such as tech, e-commerce and finance.
4.  [Second Programming Language for Data Engineer](https://www.reddit.com/r/dataengineering/comments/1i9th33/second_programming_language_for_data_engineer/) (Score: 11)
    *   Users debated the best second programming language for data engineers, recommending Go, JavaScript, Java, and SQL and discussing the pros and cons of each.
5.  [DLT vs Meltano?](https://www.reddit.com/r/dataengineering/comments/1i9frvb/dlt_vs_meltano/) (Score: 9)
    *   Users compared DLT and Meltano, concluding that DLT is generally preferred due to better support and maintenance.
6.  [Built an Open-Source ETL Tool to Simplify Data Migrations. Would Love Your Feedback!](https://www.reddit.com/r/dataengineering/comments/1i9ls1p/built_an_opensource_etl_tool_to_simplify_data/) (Score: 8)
    *   Users provided feedback on a newly built open-source ETL tool, comparing it to similar tools and discussing its value.
7.  [Streaming data](https://www.reddit.com/r/dataengineering/comments/1i9qzg6/streaming_data/) (Score: 4)
    *   Users discussed the challenges of streaming data, raising questions about data sources, consumption methods, and transformations.
8.  [Sharing of my recent writings & projects](https://www.reddit.com/r/dataengineering/comments/1i9g7ja/sharing_of_my_recent_writings_projects/) (Score: 3)
    *   The bot suggests the user refer to the community resources for learning.
9.  [Template and Walkthrough for Deploying Airflow to GCP using Terraform and a user-script](https://www.reddit.com/r/dataengineering/comments/1i9vq4h/template_and_walkthrough_for_deploying_airflow_to/) (Score: 3)
    *  The bot suggests the user refer to the community resources for learning. Also, the bot suggests the user submits their project to the community project showcase.
10. [An alternative method for building data pipelines with a blend of no-code and python. Looking for testers with no cost and no pressure - DM me if you'd like to help.](https://v.redd.it/4ff6gnc3t6fe1) (Score: 2)
    *  Users questioned the need for this tool, given the existence of Jupyter notebooks, and expressed a dislike for no-code solutions.
11.  [How to improve Jupyter notebook work flow in VS Code?](https://www.reddit.com/r/dataengineering/comments/1i9r9sf/how_to_improve_jupyter_notebook_work_flow_in_vs/) (Score: 2)
     * Users discuss how to improve Jupyter Notebook workflow by extracting reusable code and automating data steps.
12. [Am I overengineering my ETL process? (Java + Python)](https://www.reddit.com/r/dataengineering/comments/1i9tqho/am_i_overengineering_my_etl_process_java_python/) (Score: 1)
    *  Users discuss different options to handle ETL process using Python, Spark, Polars, Streamlit, etc.
13. [Online Master Degree - Employer Paying](https://www.reddit.com/r/dataengineering/comments/1i9g8pk/online_master_degree_employer_paying/) (Score: 0)
    *   Users discuss different options to do a Master's degree related to data engineering. The bot shares a link to a community guide on transitioning into data engineering.
14. [If a company is still using Hadoop (they do not use cloud), should it be a redflag for an interviewing candidate?](https://www.reddit.com/r/dataengineering/comments/1i9ucr2/if_a_company_is_still_using_hadoop_they_do_not/) (Score: 0)
    *   Users debate whether companies using Hadoop on-prem are a red flag, discussing its relevance and different setups within the Hadoop ecosystem.
15.  [Passed the GCP Professional Data Engineer exam, AMA](https://www.reddit.com/r/dataengineering/comments/1i9qgwl/passed_the_gcp_professional_data_engineer_exam_ama/) (Score: 0)
    *   Users ask how the GCP Professional Data Engineer exam compared to others and what the person's egg preferences are.

# Detailed Analysis by Thread
**[HOLD UP!! Airflow's secret weapon to slash AWS costs that nobody talks about! (Score: 113)](https://www.reddit.com/r/dataengineering/comments/1i9k5ah/hold_up_airflows_secret_weapon_to_slash_aws_costs/)**
*  **Summary:** This thread discusses a method to reduce AWS costs by fetching secrets within Airflow tasks instead of at the DAG processor level.
*  **Emotion:** The overall emotional tone of the thread is neutral, with some negative sentiment towards Airflow's design.
*  **Top 3 Points of View:**
    *   Fetching secrets within tasks reduces calls to the secrets manager and speeds up DAG processing.
    *   Airflow's design for frequent secret calls is considered bad practice.
    *   Writing DAGs without top-level code execution during parsing is a better practice.

**[How to approach data engineering systems design (Score: 27)](https://www.reddit.com/r/dataengineering/comments/1i9o5hn/how_to_approach_data_engineering_systems_design/)**
*   **Summary:** This thread involves users sharing and appreciating a resource on how to approach data engineering systems design.
*   **Emotion:** The overall emotion is positive, with users expressing gratitude and interest in the shared information.
*   **Top 3 Points of View:**
    *   Users express thanks for sharing the information.
    *   Data analysts are looking to expand their data engineering skills.
    *   Data Quality checks are essential for growing pipelines.

**[Which industries view data engineering as a revenue driver rather than just a compliance expense? (Score: 17)](https://www.reddit.com/r/dataengineering/comments/1i9o4y3/which_industries_view_data_engineering_as_a/)**
*   **Summary:** This thread explores which industries recognize data engineering as a revenue driver rather than just a cost center for compliance.
*  **Emotion:** The overall emotional tone is neutral, with users sharing their experiences and perspectives.
*  **Top 3 Points of View:**
    *   Industries like tech, e-commerce, and finance tend to view data engineering as a revenue driver.
    *   Organizational culture and leadership buy-in are crucial for data engineering to be seen as valuable.
    *   Some industries, like healthcare, are still behind in leveraging data engineering for revenue generation.

**[Second Programming Language for Data Engineer (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1i9th33/second_programming_language_for_data_engineer/)**
*  **Summary:** This thread discusses what second programming language data engineers should learn after mastering Python and SQL, and the reasons for choosing them.
*  **Emotion:** The overall tone is mixed, with some positive sentiments towards certain languages and negative ones towards others.
*  **Top 3 Points of View:**
    *   Some recommend Go due to its ability to create self-contained binaries,
    *   Others suggest Java, or Scala due to its relevance in big data technologies like Spark and Flink.
    *   Some recommend Javascript for full stack capabilities. Other recommend sticking to Python and SQL.

**[DLT vs Meltano? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1i9frvb/dlt_vs_meltano/)**
*   **Summary:** This thread compares DLT and Meltano for data integration, with users sharing their experiences and preferences.
*   **Emotion:** The emotional tone is neutral, with users providing reasoned arguments for their choices.
*  **Top 3 Points of View:**
    *   DLT is generally preferred due to better maintain sources and targets.
    *   Meltano connectors are mostly community-maintained and may have inconsistent support.
    *   Neither DLT, Meltano nor Airbyte are production ready, with Debezium being the only working solution.

**[Built an Open-Source ETL Tool to Simplify Data Migrations. Would Love Your Feedback! (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1i9ls1p/built_an_opensource_etl_tool_to_simplify_data/)**
*   **Summary:** This thread features feedback on a newly built open-source ETL tool, with users sharing opinions and comparisons.
*  **Emotion:** The overall tone is neutral, with some users expressing skepticism and concerns.
*  **Top 3 Points of View:**
    *   The tool's UI resembles Airbyte.
    *   Users are concerned about the long-term maintenance of new open-source projects.
    *   Some users see potential for the tool in mid-tier companies for simplified data migrations.

**[Streaming data (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1i9qzg6/streaming_data/)**
*   **Summary:** This thread discusses challenges related to streaming data.
*  **Emotion:** The overall tone is neutral and inquisitive.
*  **Top 3 Points of View:**
    *   The bot refers to the project showcase
    *   Questions about the source of the data (streaming source or static files) are posed.
    *  Questions are raised about data transformations before feeding the data to the applications.

**[Sharing of my recent writings & projects (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1i9g7ja/sharing_of_my_recent_writings_projects/)**
*   **Summary:** This thread is just a post with bot response.
*   **Emotion:** The emotion is neutral.
*   **Top 3 Points of View:**
    *   The bot refers to the community submitted learning resources.

**[Template and Walkthrough for Deploying Airflow to GCP using Terraform and a user-script (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1i9vq4h/template_and_walkthrough_for_deploying_airflow_to/)**
*   **Summary:** This thread is just a post with bot response.
*   **Emotion:** The emotion is neutral.
*   **Top 3 Points of View:**
    *    The bot refers to the community submitted learning resources.
    *   The bot refers to the open-source project showcase.

**[An alternative method for building data pipelines with a blend of no-code and python. Looking for testers with no cost and no pressure - DM me if you'd like to help. (Score: 2)](https://v.redd.it/4ff6gnc3t6fe1)**
*   **Summary:** This thread discusses a proposed new tool with a mix of no-code and Python.
*   **Emotion:** The overall emotional tone is negative, with users expressing skepticism about no-code solutions.
*   **Top 3 Points of View:**
    *   Some users question the need for the tool compared to using Jupyter notebooks.
    *   Some users express a strong dislike for no-code solutions in data engineering.

**[How to improve Jupyter notebook work flow in VS Code? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1i9r9sf/how_to_improve_jupyter_notebook_work_flow_in_vs/)**
*   **Summary:** This thread discusses ways to improve Jupyter notebook workflow within VS Code.
*  **Emotion:** The overall emotional tone is neutral and helpful, with constructive advice.
*  **Top 3 Points of View:**
     *   Users recommend separating reusable code into Python packages for import.
     *   Users recommend making clear cuts in the data flow and creating separate scripts.
     *   Users recommend putting the automated bits out of a notebook into pure python and version control.

**[Am I overengineering my ETL process? (Java + Python) (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1i9tqho/am_i_overengineering_my_etl_process_java_python/)**
*   **Summary:** This thread seeks advice on a possible over-engineered ETL process using Java and Python.
*  **Emotion:** The emotional tone is generally positive, with users providing encouragement and alternative suggestions.
*  **Top 3 Points of View:**
    *   Users recommend not to over think it and have fun.
    *   Some users recommend using Polars and Streamlit.
    *   Other users suggest using Scala and Spark.

**[Online Master Degree - Employer Paying (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1i9g8pk/online_master_degree_employer_paying/)**
*   **Summary:** This thread is about online Master's degrees with employer funding.
*  **Emotion:** The overall emotional tone is neutral, with users sharing information and experiences.
*  **Top 3 Points of View:**
    *   The bot refers the user to a community guide on transitioning into DE.
    *   Some users shared their experiences with Boston University's CIS program.
    *   Users also suggested to pursue an MS in CS with focus on analytics.

**[If a company is still using Hadoop (they do not use cloud), should it be a redflag for an interviewing candidate? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1i9ucr2/if_a_company_is_still_using_hadoop_they_do_not/)**
*  **Summary:** This thread discusses if using Hadoop on-prem is a red flag for potential employees.
*  **Emotion:** The emotional tone is varied, from neutral to some negative opinions towards Hadoop.
*  **Top 3 Points of View:**
    *   Some users consider it a red flag, comparing it to old technologies like COBOL.
    *   Others think it depends on the company and the specific tools used within the Hadoop ecosystem (e.g., Spark, HDFS).
    *   Some users believe it doesn't matter because the skill developed as a DE is the same and companies might be transitioning to new tech.

**[Passed the GCP Professional Data Engineer exam, AMA (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1i9qgwl/passed_the_gcp_professional_data_engineer_exam_ama/)**
*   **Summary:** This thread is an "Ask Me Anything" from someone who passed the GCP Data Engineer exam.
*   **Emotion:** The emotional tone is neutral, with users asking questions out of curiosity.
*   **Top 3 Points of View:**
    *   A user asked a question about the person's egg preference.
    *   A user asked about the comparison of the GCP exam with others.
    *   The user questions the focus on service-specific details, rather than the fundamentals of data engineering.
