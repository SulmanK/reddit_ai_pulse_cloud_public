---
title: "Data Engineering Subreddit"
date: "2025-06-03"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How do non-technical teams handle Salesforce to BigQuery syncing?](https://www.reddit.com/r/dataengineering/comments/1l2bgux/how_do_nontechnical_teams_handle_salesforce_to/) (Score: 20)
    *   This thread discusses various tools and approaches for syncing data from Salesforce to BigQuery, specifically for teams without strong technical expertise.
2.  [How do I improve my problem reading when it comes to SQL coding?](https://www.reddit.com/r/dataengineering/comments/1l2hjeq/how_do_i_improve_my_problem_reading_when_it_comes/) (Score: 15)
    *   Users are discussing strategies for improving SQL coding skills, particularly in the context of understanding and interpreting problem statements during technical interviews.
3.  [Breaking in as a new grad DE](https://www.reddit.com/r/dataengineering/comments/1l2brc4/breaking_in_as_a_new_grad_de/) (Score: 10)
    *   This thread focuses on advice and strategies for new graduates looking to enter the data engineering field, including the importance of niche skills, projects, and potentially starting as a data analyst.
4.  [Do you use dbt? How do you use it?](https://www.reddit.com/r/dataengineering/comments/1l2dblv/do_you_use_dbt_how_do_you_use_it/) (Score: 10)
    *   The discussion revolves around the use of dbt (data build tool) in data engineering projects, including its complexity, organization, and the challenges users face, such as Jinja templating.
5.  [All I want is for DuckDB to allow 2 connections](https://www.reddit.com/r/dataengineering/comments/1l2ec28/all_i_want_is_for_duckdb_to_allow_2_connections/) (Score: 10)
    *   Users are exploring workarounds and solutions to the limitation of DuckDB allowing only one connection, such as using DuckLake or creating a microservice.
6.  [How do you rate your regex skills?](https://www.reddit.com/r/dataengineering/comments/1l2lsp5/how_do_you_rate_your_regex_skills/) (Score: 1)
    *   This is about rating RegEx skills and whether or not you need to know it offhand.
7.  [Fabric:Need to query the lake house table](https://i.redd.it/tzi4m8eh8r4f1.jpeg) (Score: 0)
    *   This thread discusses how to query a lakehouse table in Fabric, suggesting the use of lookup to query the SQL endpoint.
8.  [Redefining Data Engineering with Nova (It's Conversational)](https://www.reddit.com/r/dataengineering/comments/1l2bliv/redefining_data_engineering_with_nova_its/) (Score: 0)
    *   This thread is about using Nova, which uses a natural language pipeline for data engineering, and a user is wishing them luck.
9.  [Best resources to become Azure Data Engineer?](https://www.reddit.com/r/dataengineering/comments/1l2esdx/best_resources_to_become_azure_data_engineer/) (Score: 0)
    *   This thread is asking for resources to become an Azure Data Engineer. Users are linked to learning resources.

# Detailed Analysis by Thread
**[How do non-technical teams handle Salesforce to BigQuery syncing? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1l2bgux/how_do_nontechnical_teams_handle_salesforce_to/)**
*   **Summary:** The thread explores various tools and approaches for syncing data from Salesforce to BigQuery, catering to non-technical teams. Solutions mentioned include Fivetran, Airbyte, Stitch, Dlthub, Informatica, HevoData, custom code, SnapLogic, Boomi, and Nova Agent. Some users also shared their experience about the ROI of salesforce integration.
*   **Emotion:** The overall emotional tone is neutral. The sentiment scores for all comments are high, indicating a factual and informative discussion.
*   **Top 3 Points of View:**
    *   **Use pre-built tools:** Tools like Fivetran, Airbyte, and Stitch are recommended for their ease of use and ability to be managed by non-technical teams.
    *   **Consider cost:** Some users suggest Airbyte hosted on Google Compute Engine or HevoData as cheaper alternatives to Fivetran.
    *   **Custom solutions have a place:** Some users implement custom Python scripts or suggest tools like Nova Agent to abstract complexities.

**[How do I improve my problem reading when it comes to SQL coding? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1l2hjeq/how_do_i_improve_my_problem_reading_when_it_comes/)**
*   **Summary:** The thread discusses strategies for improving SQL coding skills, specifically focusing on understanding problem statements during technical interviews. Users shared advice on communication, breaking down problems, and managing interview nerves.
*   **Emotion:** The overall emotional tone is positive, with users offering encouragement and constructive advice.
*   **Top 3 Points of View:**
    *   **Communicate during interviews:** Interviewees should communicate their thought process with the interviewer to get feedback and collaborate.
    *   **Break down problems:** Approach SQL problems step-by-step, focusing on the order of execution and individual components.
    *   **Reflect on past experiences:** Learn from past interview mistakes and reflect on how to handle similar situations in the future.

**[Breaking in as a new grad DE (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1l2brc4/breaking_in_as_a_new_grad_de/)**
*   **Summary:** This discussion provides advice for new graduates aiming to enter the data engineering field. It covers the importance of niche skills, building relevant projects, and alternative career paths.
*   **Emotion:** The emotional tone is mixed, with some positive and some neutral comments. There is a general sense of realism about the challenges of entering the field.
*   **Top 3 Points of View:**
    *   **Develop a niche:** Having expertise in a specific area like GIS can significantly improve job prospects.
    *   **Build real-world projects:** Focus on creating applications with actual users rather than simply copying projects.
    *   **Consider starting as a data analyst:** Gaining experience as a data analyst can provide a stepping stone to data engineering roles.

**[Do you use dbt? How do you use it? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1l2dblv/do_you_use_dbt_how_do_you_use_it/)**
*   **Summary:** The thread explores the use of dbt in data engineering projects. Users discuss its complexity, project organization, and the pros and cons of its features, as well as opinions on Jinja.
*   **Emotion:** The emotional tone is mixed, with both positive and negative sentiments. Some find dbt easy to use, while others criticize its complexity and developer experience.
*   **Top 3 Points of View:**
    *   **DBT Requires Careful Architecting:** DBT is easy, but things go messy very quickly if you aren't careful enough while architecting your project.
    *   **Organization is Key:** Managing DBT's complexity requires good organization.
    *   **Jinja is Difficult:** The developer experience of Jinja, a templating language used in dbt, is considered poor.

**[All I want is for DuckDB to allow 2 connections (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1l2ec28/all_i_want_is_for_duckdb_to_allow_2_connections/)**
*   **Summary:** This thread discusses workarounds for DuckDB's limitation of only allowing one connection, including suggestions for using DuckLake or creating a microservice.
*   **Emotion:** The emotional tone is neutral, with users providing technical solutions to a specific problem.
*   **Top 3 Points of View:**
    *   **Use DuckLake:** DuckLake is suggested as a way to manage multiple connections.
    *   **Create multiple connections on separate threads:** Open multiple connections to the same file on separate CPU threads.
    *   **Implement a microservice:** Run DuckDB behind a microservice to allow multiple connections via a server/proxy.

**[How do you rate your regex skills? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1l2lsp5/how_do_you_rate_your_regex_skills/)**
*   **Summary:** This thread asks users to rate their Regex skills and users answer with some saying it's not useful.
*   **Emotion:** The emotional tone is negative, with some users answering it's not a very useful skill to have.
*   **Top 3 Points of View:**
    *   **Not Very Useful:** Regex isn't a very useful skill to have.
    *   **Research It:** If needed, research Regex to find the answer.
    *   **Low Score:** Regex skills rated as very low.

**[Fabric:Need to query the lake house table (Score: 0)](https://i.redd.it/tzi4m8eh8r4f1.jpeg)**
*   **Summary:** This thread suggests using lookup to query the SQL endpoint, which is on top of lakehouse.
*   **Emotion:** The emotional tone is positive, due to the fact that the sentiment score is positive.
*   **Top 3 Points of View:**
    *   **Lookup to Query SQL endpoint:** Lookup to Query SQL endpoint

**[Redefining Data Engineering with Nova (It's Conversational) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1l2bliv/redefining_data_engineering_with_nova_its/)**
*   **Summary:** This thread is about using Nova, which uses a natural language pipeline for data engineering, and a user is wishing them luck.
*   **Emotion:** The emotional tone is positive, due to the fact that the sentiment score is positive.
*   **Top 3 Points of View:**
    *   **Natural Language Pipeline:** Nova uses a natural language pipeline for data engineering.
    *   **Wish you luck:** User is wishing them luck

**[Best resources to become Azure Data Engineer? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1l2esdx/best_resources_to_become_azure_data_engineer/)**
*   **Summary:** This thread is asking for resources to become an Azure Data Engineer. Users are linked to learning resources.
*   **Emotion:** The emotional tone is neutral, due to the fact that the sentiment score is neutral.
*   **Top 3 Points of View:**
    *   **Learning Resources:** Users are being linked to learning resources.
