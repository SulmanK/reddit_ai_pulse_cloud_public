---
title: "Data Engineering Subreddit"
date: "2025-08-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "BI tools", "ELT"]
---

# Overall Ranking and Top Discussions
1.  [Why are BI tools getting worse?](https://www.reddit.com/r/dataengineering/comments/1mpy4pt/why_are_bi_tools_getting_worse/) (Score: 83)
    *   A discussion on whether BI tools are improving or declining, with various perspectives on specific tools like Power BI, Tableau, Qlik, and newer options like Hex and Metabase.
2.  [Airbyte vs Fivetran for our ELT stack? Any other alternatives?](https://www.reddit.com/r/dataengineering/comments/1mpsjqt/airbyte_vs_fivetran_for_our_elt_stack_any_other/) (Score: 30)
    *   A thread comparing Airbyte and Fivetran for ELT stacks, with alternative tools and approaches also being suggested, particularly regarding PII masking, SCD2 implementation, and API reliability.
3.  [Coding agent on top of BigQuery](https://i.redd.it/1676o831b0jf1.png) (Score: 11)
    *   A post about a coding agent built on top of BigQuery. Users discuss the potential risks and benefits, including cost concerns and the need for clean data.
4.  [What do you think about Apache piont?](https://www.reddit.com/r/dataengineering/comments/1mpogru/what_do_you_think_about_apache_piont/) (Score: 7)
    *   A discussion on Apache Pinot, its suitability for low-latency analytics at scale, and the challenges associated with its configuration and deployment.
5.  [Settle a bet for me — which integration method would you pick?](https://www.reddit.com/r/dataengineering/comments/1mq6a6f/settle_a_bet_for_me_which_integration_method/) (Score: 5)
    *   A debate on various data integration methods, with strong opinions against directly exposing the database and preferences for API-driven or S3-based approaches.
6.  [Advice for a Junior DE](https://www.reddit.com/r/dataengineering/comments/1mq7gmg/advice_for_a_junior_de/) (Score: 5)
    *   A thread seeking advice for junior data engineers, with responses focusing on documentation, continuous learning, and proactive problem-solving.
7.  [Need help to transfer a large table with Airflow](https://www.reddit.com/r/dataengineering/comments/1mpvtx5/need_help_to_transfer_a_large_table_with_airflow/) (Score: 3)
    *   A question about transferring a large table with Airflow, and people are commenting about the efficiency of using Airflow for processing large datasets.
8.  [The Role of Data Contracts in Modern Metadata Management](https://www.reddit.com/r/dataengineering/comments/1mq03ld/the_role_of_data_contracts_in_modern_metadata/) (Score: 3)
    *   A discussion on implementing data contracts in dbt for better tracking of downstream changes and ensuring data quality.
9.  [Did I do this system design question correct? had a technical round with dev lead, architect and Engineering manager](https://www.reddit.com/r/dataengineering/comments/1mq8tyh/did_i_do_this_system_design_question_correct_had/) (Score: 3)
    *   A user asks whether they did a system design question correctly during a technical interview.
10. [DE ZoomCamp](https://www.reddit.com/r/dataengineering/comments/1mq3xxp/de_zoomcamp/) (Score: 1)
    *   Brief comments regarding the intensity of the DE ZoomCamp.
11. [Major changes in the company, boss is quitting. Updated my CV just in case, can you critique?](https://i.redd.it/zcz0evn5h1jf1.png) (Score: 0)
    *   A user requests feedback on their updated CV due to company changes.
12. [MS options help](https://www.reddit.com/r/dataengineering/comments/1mpp75w/ms_options_help/) (Score: 0)
    *   A person asks for help deciding on what Master's degree they should pursue.
13. [Settle a bet for me — which would you pick?](https://www.reddit.com/r/dataengineering/comments/1mq3cpf/settle_a_bet_for_me_which_would_you_pick/) (Score: 0)
    *   A similar question to another post on integration methods, with a focus on data layer access and potential problems.
14. [Anyone else feel like DEs are just background NPCs now that everything’s “AI-driven”?](https://www.reddit.com/r/dataengineering/comments/1mq54lf/anyone_else_feel_like_des_are_just_background/) (Score: 0)
    *   A user expresses concern that data engineers are becoming less visible due to the focus on AI.

# Detailed Analysis by Thread
**[ Why are BI tools getting worse? (Score: 83)](https://www.reddit.com/r/dataengineering/comments/1mpy4pt/why_are_bi_tools_getting_worse/)**
*  **Summary:** The thread discusses the perceived decline or stagnation of BI tools. Commenters share experiences with different tools, including Power BI, Tableau, Qlik, Hex, and Metabase. There's a sentiment that newer tools are focusing too much on AI integration and neglecting core improvements and user experience. Some also discuss the challenges of self-service BI due to data complexity.
*  **Emotion:** The overall emotional tone is neutral, with a mix of opinions and experiences. There is some negative sentiment towards specific tools and the direction of BI development, but also positive experiences shared with newer tools.
*  **Top 3 Points of View:**
    * BI tools are getting worse because they are overly focused on AI and not enough on core functionality and user experience.
    * Power BI is becoming harder to use due to the increasing number of options and settings.
    * Hex and Metabase are promising alternatives that offer more flexibility and easier chart creation.

**[ Airbyte vs Fivetran for our ELT stack? Any other alternatives? (Score: 30)](https://www.reddit.com/r/dataengineering/comments/1mpsjqt/airbyte_vs_fivetran_for_our_elt_stack_any_other/)**
*  **Summary:** The thread compares Airbyte and Fivetran as ELT solutions, exploring alternatives, particularly regarding PII masking, SCD2 implementation, API limits and retry logic. Some people suggest custom python script or NiFi.
*  **Emotion:** The overall emotional tone is neutral. People discuss and analyze tools in a calm and objective fashion.
*  **Top 3 Points of View:**
    * Fivetran is good, but doesn't support mutable data, requiring dbt for SCD2, which adds complexity.
    * Airbyte is DIY.
    * Some suggest Stacksync as an alternative that is built for two-way sync, with full CRUD operations.

**[ Coding agent on top of BigQuery (Score: 11)](https://i.redd.it/1676o831b0jf1.png)**
*  **Summary:** The thread discusses the implications of using a coding agent on top of BigQuery. Concerns are raised about potential cost overruns and the need for clean data.
*  **Emotion:** The emotional tone is mixed, with elements of positivity (for creating something cool) and negativity (due to cost concerns and security risks).
*  **Top 3 Points of View:**
    * The agent could lead to unexpected and high costs due to poorly optimized queries.
    * The tool could be effective if the data is very clean.
    * Connecting unknown software to BigQuery carries security risks.

**[ What do you think about Apache piont? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1mpogru/what_do_you_think_about_apache_piont/)**
*  **Summary:** The thread discusses Apache Pinot, its suitability for low-latency analytics at scale, and the challenges associated with its configuration and deployment.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Apache Pinot is ideal for low-latency analytics at scale.
    *   The tricky parts are ingestion config, schema evolution, and resource tuning.
    *   It shouldn't be expected to be a general-purpose warehouse.

**[ Settle a bet for me — which integration method would you pick? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1mq6a6f/settle_a_bet_for_me_which_integration_method/)**
*  **Summary:** The thread debates on data integration methods. Many people are against directly exposing the database and prefer API-driven or S3-based approaches.
*  **Emotion:** The emotional tone is mostly negative towards option 2.
*  **Top 3 Points of View:**
    * Option 2 is the worst.
    * Option 3 is the best.
    * Building your own API in front of a DB, not exposing it directly.

**[ Advice for a Junior DE (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1mq7gmg/advice_for_a_junior_de/)**
*  **Summary:** The thread is about seeking advice for junior data engineers, with responses focusing on documentation, continuous learning, and proactive problem-solving.
*  **Emotion:** The overall tone is helpful and supportive.
*  **Top 3 Points of View:**
    *   Make a habit of documenting everything.
    *   Read others' code and browse through infrastructure.
    *   Ask questions and be curious.

**[ Need help to transfer a large table with Airflow (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mpvtx5/need_help_to_transfer_a_large_table_with_airflow/)**
*  **Summary:** The thread is a question about transferring a large table with Airflow, and people are commenting about the efficiency of using Airflow for processing large datasets.
*  **Emotion:** The overall tone is technical and neutral.
*  **Top 3 Points of View:**
    *   Using airflow for processing or integration will have problems.
    *   Use Polars to move the data and write to parquet for more memory efficiency.
    *   Best practice is to only use airflow for orchestration and use an ETL tool like spark to process data.

**[ The Role of Data Contracts in Modern Metadata Management (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mq03ld/the_role_of_data_contracts_in_modern_metadata/)**
*  **Summary:** A discussion on implementing data contracts in dbt for better tracking of downstream changes and ensuring data quality.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Implementing data contracts in dbt.
    *   The main reason is to better track how it'll affect downstream changes.
    *   If the contact is breached then it fails to build.

**[ Did I do this system design question correct? had a technical round with dev lead, architect and Engineering manager (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mq8tyh/did_i_do_this_system_design_question_correct_had/)**
*  **Summary:** A user asks whether they did a system design question correctly during a technical interview.
*  **Emotion:** The overall tone is helpful and supportive.
*  **Top 3 Points of View:**
    *   The job posting could be fake.
    *   They have someone already but need to do 3 interviews or a certain minimum to satisfy HR.
    *   There are also services like AWS SES that store raw email objetcs directly in S3.

**[ DE ZoomCamp (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mq3xxp/de_zoomcamp/)**
*  **Summary:** The thread has brief comments regarding the intensity of the DE ZoomCamp.
*  **Emotion:** The overall tone is positive.
*  **Top 3 Points of View:**
    *   Just start.
    *   From what I've heard its quite intense, I'm planning on joining the next cohort.

**[ Major changes in the company, boss is quitting. Updated my CV just in case, can you critique? (Score: 0)](https://i.redd.it/zcz0evn5h1jf1.png)**
*  **Summary:** The thread is a user requests feedback on their updated CV due to company changes.
*  **Emotion:** The overall tone is helpful and supportive.
*  **Top 3 Points of View:**
    *   What did you accomplish in the four years covered on your resume? Lead with the impact of your accomplishments.
    *   Never seen a resume with a small experience section and a large skills section before.
    *   Detail and expand on your work history. Incorporate how you used your skill on your job history and add some quantitative info is possible. Also throw in some ATS keywords as well.

**[ MS options help (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mpp75w/ms_options_help/)**
*  **Summary:** The thread is where a person asks for help deciding on what Master's degree they should pursue.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   Go for Masters in Math/Stats, other degrees you listed aren't useful or helpful for industry unless a ML degree is completely Math heavy.
    *   Your MS plan seems to be a tad bit astray from your overall goal. You could get some real-life experience as a data engineer/scientist. If your heart is confused, go for a safe option like data science.
    *   Don't get a masters unless it's paid for / from a top school.  Don't take on debt.  No one will care.  If you must, at least get one in CS/Math/Stats.

**[ Settle a bet for me — which would you pick? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mq3cpf/settle_a_bet_for_me_which_would_you_pick/)**
*  **Summary:** Similar to the other thread with a similar question. The consensus still remains that there should always be a layer of separation between the consumer of data and the database.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   1 and only 1: 2/3 leads to you not being able to change the data layer underneath.
    *   tbh in my company its a big problem.
    *   I work for a pharma company and they have super tight control over what can be connected to our sources, so we'll probably need to host or smth

**[ Anyone else feel like DEs are just background NPCs now that everything’s “AI-driven”? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mq54lf/anyone_else_feel_like_des_are_just_background/)**
*  **Summary:** A user expresses concern that data engineers are becoming less visible due to the focus on AI.
*  **Emotion:** The thread has a mix of tones.
*  **Top 3 Points of View:**
    *   Our roles exist to develop and manage infrastructure, ultimately to enable the business. We are behind the scenes workers and that's okay. Practice working out loud more and partnering with downstream business units to improve data products.
    *   go touch the grass a little - infrastructure related jobs are only noticed when they are not working.
    *   DE work is and always has been similar to plumbing for tech.
