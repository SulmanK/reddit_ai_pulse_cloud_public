---
title: "Data Engineering Subreddit"
date: "2025-07-16"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] System design books for Data Engineer](https://www.reddit.com/r/dataengineering/comments/1m16g4x/system_design_books_for_data_engineer/) (Score: 26)
    *   Discussion about recommended system design books for data engineers.
2.  [How can be Fivetran so much faster than Airbyte?](https://www.reddit.com/r/dataengineering/comments/1m1hj09/how_can_be_fivetran_so_much_faster_than_airbyte/) (Score: 7)
    *   Inquiry into the performance differences between Fivetran and Airbyte, with potential causes and solutions discussed.
3.  [Can a DE team educate an Engineering team?](https://www.reddit.com/r/dataengineering/comments/1m1hotq/can_a_de_team_educate_an_engineering_team/) (Score: 5)
    *   Discussion on the role of a Data Engineering (DE) team in educating a broader Engineering team on data quality and best practices.
4.  [Workaround for Databricks AI/BI Genie manual setup?](https://www.reddit.com/r/dataengineering/comments/1m18f3x/workaround_for_databricks_aibi_genie_manual_setup/) (Score: 4)
    *   Exploration of potential workarounds for the manual setup of Databricks AI/BI Genie.
5.  [Alteryx ETL vs Airbyte->DW->DBT: Convincing my boss](https://www.reddit.com/r/dataengineering/comments/1m1b0b3/alteryx_etl_vs_airbytedwdbt_convincing_my_boss/) (Score: 4)
    *   Discussion about the pros and cons of using Alteryx ETL versus Airbyte->DW->DBT, focusing on how to convince a boss to adopt the latter.
6.  [Swapped legacy schedulers and flat files with real-time pipelines on Azure - Here’s what broke and what worked](https://www.reddit.com/r/dataengineering/comments/1m1bwjf/swapped_legacy_schedulers_and_flat_files_with/) (Score: 3)
    *   Discussion about switching to real-time data pipelines on Azure.
7.  [We read 1000+ API docs so you don't have to. Here's the result](https://www.reddit.com/r/dataengineering/comments/1m1frmq/we_read_1000_api_docs_so_you_dont_have_to_heres/) (Score: 3)
    *   Discussion about an effort to simplify data pipeline construction.
8.  [Is there a way to efficiently convert PyArrow Lists and Structs to json strings?](https://www.reddit.com/r/dataengineering/comments/1m1bgvk/is_there_a_way_to_efficiently_convert_pyarrow/) (Score: 3)
    *   Inquiry about efficient methods for converting PyArrow Lists and Structs to JSON strings.
9.  [Is there any way to automatically export my database from phpMyAdmin to my own MySQL server?](https://www.reddit.com/r/dataengineering/comments/1m1a6b0/is_there_any_way_to_automatically_export_my/) (Score: 2)
    *   Question about automating database export from phpMyAdmin to a personal MySQL server.
10. [Need advice starting in a new company](https://www.reddit.com/r/dataengineering/comments/1m1aoac/need_advice_starting_in_a_new_company/) (Score: 2)
    *   Advice sought by a new data engineer who relies heavily on AI and faces challenges meeting expectations.
11. [What aspects of data engineering are more LLM resistant?](https://www.reddit.com/r/dataengineering/comments/1m1bjtd/what_aspects_of_data_engineering_are_more_llm/) (Score: 2)
    *   Exploration of data engineering tasks less susceptible to automation or replacement by Large Language Models (LLMs).
12. [Why do all of these MDS orchestration SaaS tools charge per transformation/materialization?](https://www.reddit.com/r/dataengineering/comments/1m1en12/why_do_all_of_these_mds_orchestration_saas_tools/) (Score: 2)
    *   Question regarding the pricing model of MDS orchestration SaaS tools.
13. [Stories about open source vs in-house](https://www.reddit.com/r/dataengineering/comments/1m1ihb6/stories_about_open_source_vs_inhouse/) (Score: 2)
    *   Discussion about the pros and cons of using open-source versus in-house solutions for data engineering tasks.
14. [Open Source Boilerplate for a small Data Platform](https://www.reddit.com/r/dataengineering/comments/1m1erzc/open_source_boilerplate_for_a_small_data_platform/) (Score: 1)
    *   Discussion around finding an open source boilerplate.
15. [Can you work as a data engineer with an economics science degree?](https://www.reddit.com/r/dataengineering/comments/1m1agoc/can_you_work_as_a_data_engineer_with_an_economics/) (Score: 0)
    *   Question about the feasibility of working as a data engineer with an economics degree.

# Detailed Analysis by Thread
**[[D] System design books for Data Engineer (Score: 26)](https://www.reddit.com/r/dataengineering/comments/1m16g4x/system_design_books_for_data_engineer/)**
*  **Summary:** The thread discusses recommended system design books for data engineers, including "DDIA" (Designing Data-Intensive Applications), "Pocket Reference," and "Data Engineering Design Patterns."
*  **Emotion:** The overall emotional tone of the thread is Neutral, with a sentiment score of 0.7396.
*  **Top 3 Points of View:**
    *   DDIA is getting a new edition, so it might be worth waiting.
    *   Pocket Reference is a good resource for common DE patterns.
    *   Data Engineering Design Patterns seems to cover DE project design.

**[How can be Fivetran so much faster than Airbyte? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m1hj09/how_can_be_fivetran_so_much_faster_than_airbyte/)**
*  **Summary:**  This thread investigates why Fivetran might be faster than Airbyte, focusing on potential issues with Airbyte's configuration, connector choices, and resource usage. Suggestions include checking pod size, RAM usage, deselecting slow streams, and considering "Direct Load" for BigQuery.
*  **Emotion:** The overall emotional tone of the thread is Neutral. Sentiment scores range from 0.4157 to 0.9387, with most comments expressing a neutral stance.
*  **Top 3 Points of View:**
    *   Airbyte's performance can be affected by pod size and RAM usage in k8s deployments.
    *   Slow Hubspot connectors can significantly impact Airbyte's overall sync speed.
    *   Airbyte's "Direct Load" feature for BigQuery can improve destination performance.

**[Can a DE team educate an Engineering team? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1m1hotq/can_a_de_team_educate_an_engineering_team/)**
*  **Summary:** The discussion revolves around whether a Data Engineering (DE) team can educate a broader Engineering team, emphasizing that willingness to learn is crucial. It also highlights the importance of understanding stakeholder incentives and establishing data contracts between producers and consumers.
*  **Emotion:** The overall emotional tone of the thread is Neutral, with sentiment scores ranging from 0.5031 to 0.6548.
*  **Top 3 Points of View:**
    *   A DE team can educate an Engineering team, but only if the latter is willing to learn.
    *   Data quality is a shared responsibility requiring buy-in at a leadership level.
    *   It is important to consider stakeholder incentives, QA processes, integration testing, and regression tests.

**[Workaround for Databricks AI/BI Genie manual setup? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1m18f3x/workaround_for_databricks_aibi_genie_manual_setup/)**
*  **Summary:** This thread explores potential workarounds for the manual setup of Databricks AI/BI Genie, including the use of AI to generate field descriptions and the possibility of AI-generated semantic layers in tools like dbt, Thoughtspot, and Connecty.
*  **Emotion:** The emotional tone of the thread is mixed, with both positive and neutral sentiments. Scores range from 0.4073 to 0.9648.
*  **Top 3 Points of View:**
    *   AI can generate field descriptions, which helps.
    *   dbt might offer an AI-generated semantic layer.
    *   Tools like Thoughtspot and Connecty claim to have AI-generated and managed semantic layers.

**[Alteryx ETL vs Airbyte->DW->DBT: Convincing my boss (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1m1b0b3/alteryx_etl_vs_airbytedwdbt_convincing_my_boss/)**
*  **Summary:** The discussion compares Alteryx ETL with Airbyte->DW->DBT, focusing on the pros and cons of each and how to convince a boss to adopt the latter. Points include the cost-effectiveness of Python-based solutions, the limitations of Alteryx, and the potential for over-engineering.
*  **Emotion:** The thread maintains a Neutral emotional tone, with sentiment scores ranging from 0.6281 to 0.8526.
*  **Top 3 Points of View:**
    *   Alteryx is better suited for analysis that can do things Excel can't, but it doesn't produce code.
    *   A cost benefit analysis (CBA) should be provided instead of technical benefits.
    *   What's being suggested (Airbyte->DW->DBT) is grossly over-engineered.

**[Swapped legacy schedulers and flat files with real-time pipelines on Azure - Here’s what broke and what worked (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m1bwjf/swapped_legacy_schedulers_and_flat_files_with/)**
*  **Summary:** The content provides links to open-source projects and a submission form for featuring projects, indicating a discussion around migrating to real-time pipelines on Azure.
*  **Emotion:** The emotional tone of the thread is Neutral, with a sentiment score of 0.8865.
*  **Top 3 Points of View:**
    *   The thread seems to be promoting dataengineering.wiki.
    *   The thread also promotes airtable.com.
    *   The overall discussion revolves around transitioning to real-time pipelines on Azure.

**[We read 1000+ API docs so you don't have to. Here's the result (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m1frmq/we_read_1000_api_docs_so_you_dont_have_to_heres/)**
*  **Summary:** This thread seems to be discussing the implications of a tool that aims to simplify data pipeline construction for Python developers. Some comments express skepticism, suggesting it might be an attempt to replace data engineers.
*  **Emotion:** The emotional tone is primarily Neutral, with sentiment scores ranging from 0.5130 to 0.9657.
*  **Top 3 Points of View:**
    *   Some users believe the tool is intended to replace data engineers.
    *   Others question whether it would be end-to-end or extraction only, requiring dbt for transformation.
    *   Some think that the product is intellisense for APIs.

**[Is there a way to efficiently convert PyArrow Lists and Structs to json strings? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m1bgvk/is_there_a_way_to_efficiently_convert_pyarrow/)**
*  **Summary:** The discussion revolves around efficient methods for converting PyArrow Lists and Structs to JSON strings, with suggestions including using `to_pylist()` followed by `json.dumps()`, or `to_pandas()` followed by `to_json()`, and considering the use of `orjson`.
*  **Emotion:** The emotional tone is Neutral, with sentiment scores ranging from 0.5367 to 0.8815.
*  **Top 3 Points of View:**
    *   Pyarrow doesn't have a way to generate an in-memory JSON string representation.
    *   Try using `to_pylist()` and then `json.dumps()`.
    *   Using `to_pandas()` and then `to_json()` could be faster.

**[Is there any way to automatically export my database from phpMyAdmin to my own MySQL server? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m1a6b0/is_there_any_way_to_automatically_export_my/)**
*  **Summary:** The thread discusses methods to automate database export from phpMyAdmin to a personal MySQL server. Suggestions include using browser inspection to write Python code with libraries like httpx/requests or playwright.
*  **Emotion:** The overall emotional tone is Neutral, with sentiment scores ranging from 0.7330 to 0.8562.
*  **Top 3 Points of View:**
    *   Backup and then Restore.
    *   Inspect the network in the browser and write python code to automate the process.
    *   Clarification is needed on whether it needs to be done once or scheduled.

**[Need advice starting in a new company (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m1aoac/need_advice_starting_in_a_new_company/)**
*  **Summary:** This thread is about a new data engineer seeking advice on how to progress in their role. The poster depends on AI to create a python script to execute data comparison, ETL, and so on and is facing challenges meeting expectations.
*  **Emotion:** The overall emotional tone is somewhat Negative, with sentiment scores ranging from 0.3757 to 0.8467.
*  **Top 3 Points of View:**
    *   People yell at the poster like a child.
    *   Focus on improving without AI one day a week.
    *   There is a huge technical deficit which is being filled by AI.

**[What aspects of data engineering are more LLM resistant? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m1bjtd/what_aspects_of_data_engineering_are_more_llm/)**
*  **Summary:** This thread explores which aspects of data engineering are less likely to be automated or replaced by Large Language Models (LLMs). The discussion points to tasks requiring deep domain knowledge, understanding business requirements, and handling information silos.
*  **Emotion:** The overall emotional tone is Neutral, with sentiment scores ranging from 0.6218 to 0.9674.
*  **Top 3 Points of View:**
    *   Deep domain knowledge of the core model is more LLM resistant.
    *   Deciphering the actual requirements from the business is more LLM resistant.
    *   Information silos are more LLM resistant.

**[Why do all of these MDS orchestration SaaS tools charge per transformation/materialization? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m1en12/why_do_all_of_these_mds_orchestration_saas_tools/)**
*  **Summary:** The thread discusses the pricing model of MDS orchestration SaaS tools, particularly the practice of charging per transformation or materialization. Reasons include the cost of running services, maintaining availability, and the underlying business model of these companies.
*  **Emotion:** The thread's emotional tone is Neutral, with sentiment scores ranging from 0.7633 to 0.9479.
*  **Top 3 Points of View:**
    *   Self-hosting is a good idea, since the compute for the transformation happens in the database.
    *   There’s also a flat cost for running all those services on their side.
    *   That's what these companies are banking on.

**[Stories about open source vs in-house (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m1ihb6/stories_about_open_source_vs_inhouse/)**
*  **Summary:** The discussion revolves around the pros and cons of using open-source versus in-house solutions for data engineering tasks. It emphasizes the importance of considering long-term maintenance, scalability, and the true cost of in-house development.
*  **Emotion:** The thread has a slightly Positive emotional tone overall, with sentiment scores ranging from 0.5909 to 0.8743.
*  **Top 3 Points of View:**
    *   It’s not reasonable to expect an out of the box solution to outperform something bespoke.
    *   It’s not really meaningful to bring open or closed source into it.
    *   What's the point of coding your own integrations if you already have a superior ETL platform like SSIS?

**[Open Source Boilerplate for a small Data Platform (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1m1erzc/open_source_boilerplate_for_a_small_data_platform/)**
*  **Summary:** The comment provides a link to local-data-stack.
*  **Emotion:** The overall emotional tone of the thread is Neutral with a sentiment score of 0.8010.
*  **Top 3 Points of View:**
    *   Recommend you stub the SSO piece.

**[Can you work as a data engineer with an economics science degree? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1m1agoc/can_you_work_as_a_data_engineer_with_an_economics/)**
*  **Summary:** The thread addresses the possibility of working as a data engineer with an economics degree, with most responders indicating that it is possible.
*  **Emotion:** The overall emotional tone is Neutral, with sentiment scores ranging from 0.5007 to 0.9636.
*  **Top 3 Points of View:**
    *   Yes, it's possible; self-study and experience are key.
    *   Economics is a good start, it's as common as computer science.
    *   Starting as a data analyst and transitioning is a good option.
