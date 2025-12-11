---
title: "Data Engineering Subreddit"
date: "2025-11-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ETL", "data pipelines"]
---

# Overall Ranking and Top Discussions
1.  [Streaming telemetry from 500+ factory machines to cloud in real time, lessons from 2 years running this setup](https://www.reddit.com/r/dataengineering/comments/1owsh0m/streaming_telemetry_from_500_factory_machines_to/) (Score: 56)
    *   Users discuss the challenges and solutions for streaming telemetry data from factory machines to the cloud.
2.  [Is the difference between ETL and ELT purely theoretical or is there some sort of objective way to determine in which category a pipeline falls?](https://www.reddit.com/r/dataengineering/comments/1owt21l/is_the_difference_between_etl_and_elt_purely/) (Score: 35)
    *   Users are debating the practical differences between ETL and ELT data pipelines.
3.  [Why is transforming data still so expensive](https://www.reddit.com/r/dataengineering/comments/1owxk6b/why_is_transforming_data_still_so_expensive/) (Score: 34)
    *   A discussion about the ongoing costs associated with data transformation processes.
4.  [Got an unfair end-of-year review after burning myself out](https://www.reddit.com/r/dataengineering/comments/1owzjys/got_an_unfair_endofyear_review_after_burning/) (Score: 33)
    *   A user shares their experience of receiving an unfair performance review after experiencing burnout and seeks advice.
5.  [Is Cloudera still Alive in US/EU?](https://www.reddit.com/r/dataengineering/comments/1owwdnx/is_cloudera_still_alive_in_useu/) (Score: 8)
    *   Users are discussing the current relevance and usage of Cloudera in the US and Europe.
6.  [What are your monthly costs?](https://www.reddit.com/r/dataengineering/comments/1ox2dhd/what_are_your_monthly_costs/) (Score: 7)
    *   Users are sharing their monthly costs associated with data engineering infrastructure and tools.
7.  [EDI in DE](https://www.reddit.com/r/dataengineering/comments/1owxx7s/edi_in_de/) (Score: 6)
    *   Discussion on the relevance and use of EDI (Electronic Data Interchange) in data engineering roles.
8.  [Rejected 3x senior DE, feel like fraud](https://www.reddit.com/r/dataengineering/comments/1ox75em/rejected_3x_senior_de_feel_like_fraud/) (Score: 5)
    *   A user expresses feelings of inadequacy after being rejected for multiple senior data engineering positions.
9.  [Sanity check: am I crazy for feeling like my "data engineering" position is a dead end?](https://www.reddit.com/r/dataengineering/comments/1ox84x9/sanity_check_am_i_crazy_for_feeling_like_my_data/) (Score: 4)
    *   A user questions whether their current data engineering role is a dead end.
10. [When does Spark justify itself for Postgres to S3 ETL using Iceberg format? Sorry, I'm noob here.](https://www.reddit.com/r/dataengineering/comments/1owy8wn/when_does_spark_justify_itself_for_postgres_to_s3/) (Score: 4)
    *   A user asks when it makes sense to use Spark for ETL from Postgres to S3 using Iceberg.
11. [Best way to store financial statements and do some timeseries / benchmark analyses](https://www.reddit.com/r/dataengineering/comments/1ox1s0b/best_way_to_store_financial_statements_and_do/) (Score: 4)
    *   Users are discussing the best ways to store financial statements for time series and benchmark analysis.
12. [CMU Intro to Database Systems](https://www.reddit.com/r/dataengineering/comments/1owx9ut/cmu_intro_to_database_systems/) (Score: 4)
    *   A user is seeking guidance on learning resources for database systems.
13. [Need tips on a hybrid architecture for both real-time BI and ML](https://www.reddit.com/r/dataengineering/comments/1ox4uvz/need_tips_on_a_hybrid_architecture_for_both/) (Score: 2)
    *   A user seeks tips on designing a hybrid architecture for real-time BI and ML.
14. [Is there a way to auto create data model from schemas of sources?](https://www.reddit.com/r/dataengineering/comments/1ox173p/is_there_a_way_to_auto_create_data_model_from/) (Score: 1)
    *   A discussion on automatically creating data models from source schemas.
15. [Would using Azure Data Factory in this Context be Overkill?](https://www.reddit.com/r/dataengineering/comments/1ox5kta/would_using_azure_data_factory_in_this_context_be/) (Score: 1)
    *   A user questions whether using Azure Data Factory would be overkill for their specific use case.
16. [GIS Consulting to Data Engineering Salary](https://www.reddit.com/r/dataengineering/comments/1ox5wiq/gis_consulting_to_data_engineering_salary/) (Score: 1)
    *   A discussion on salary expectations when transitioning from GIS consulting to data engineering.
17. [Is it not pointless to transfer Parquet data with Kafka?](https://www.reddit.com/r/dataengineering/comments/1ox1e9h/is_it_not_pointless_to_transfer_parquet_data_with/) (Score: 0)
    *   A user questions the practicality of transferring Parquet data with Kafka.

# Detailed Analysis by Thread
**[Streaming telemetry from 500+ factory machines to cloud in real time, lessons from 2 years running this setup (Score: 56)](https://www.reddit.com/r/dataengineering/comments/1owsh0m/streaming_telemetry_from_500_factory_machines_to/)**
*  **Summary:** The thread discusses the challenges and solutions implemented for streaming telemetry data from 500+ factory machines to the cloud in real-time. Users are requesting more details about the solution used, specifically the messaging framework and hardware setup.
*  **Emotion:** The overall emotional tone is neutral, with users expressing curiosity and seeking more information.
*  **Top 3 Points of View:**
    *   Users want to know the specific messaging framework used (e.g., MQTT, NATS).
    *   Users are interested in the hardware and software configurations at the edge.
    *   Some users believe the problem isn't complex enough to warrant significant scaling challenges given the data volume.

**[Is the difference between ETL and ELT purely theoretical or is there some sort of objective way to determine in which category a pipeline falls? (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1owt21l/is_the_difference_between_etl_and_elt_purely/)**
*  **Summary:** The thread explores the practical differences between ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) data pipelines, focusing on where the transformation process takes place.
*  **Emotion:** The overall emotional tone is neutral, focused on clarifying the definitions and practical implications.
*  **Top 3 Points of View:**
    *   ETL involves transforming data before loading it into the data warehouse.
    *   ELT involves loading data into the data warehouse first, then transforming it.
    *   The location of the "main transformations" is the defining factor, regardless of staging tables or extra steps.

**[Why is transforming data still so expensive (Score: 34)](https://www.reddit.com/r/dataengineering/comments/1owxk6b/why_is_transforming_data_still_so_expensive/)**
*  **Summary:** The thread discusses the reasons why data transformation remains a costly process, even with modern tools and technologies.
*  **Emotion:** The overall emotional tone is neutral, with elements of frustration and problem-solving.
*  **Top 3 Points of View:**
    *   Moving and normalizing data across systems is a non-trivial problem.
    *   Many companies suffer from "cluster fatigue" or tech debt that increases costs.
    *   Modern data platforms charge for convenience, leading to expensive locked-in compute and networking.

**[Got an unfair end-of-year review after burning myself out (Score: 33)](https://www.reddit.com/r/dataengineering/comments/1owzjys/got_an_unfair_endofyear_review_after_burning/)**
*  **Summary:** A user shares their experience of receiving a negative performance review despite working hard and experiencing burnout, seeking advice on how to proceed.
*  **Emotion:** The emotional tone is mixed, with elements of frustration, negativity, and some positivity from supportive responses.
*  **Top 3 Points of View:**
    *   Advise the user to look for a new job due to the bad manager.
    *   Question the user's perspective, suggesting they consider the manager's viewpoint and focus on results over effort.
    *   Suggest documenting contributions and involving HR if necessary, but with caution.

**[Is Cloudera still Alive in US/EU? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1owwdnx/is_cloudera_still_alive_in_useu/)**
*  **Summary:** The thread discusses the current prevalence and usage of Cloudera in the US and Europe, especially compared to cloud-based alternatives.
*  **Emotion:** The overall emotional tone is neutral, with some positive sentiment indicating Cloudera is still in use, but generally declining.
*  **Top 3 Points of View:**
    *   Cloudera is still used in some large European corporations and bureaucratic institutions, due to inertia and regulatory hurdles.
    *   Cloudera is on the decline in favor of cloud-based solutions like Databricks and Snowflake.
    *   Some banks in India are still using Cloudera because they don't want customer info on the cloud.

**[What are your monthly costs? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ox2dhd/what_are_your_monthly_costs/)**
*  **Summary:** Users are sharing the costs associated with data engineering infrastructure.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   For less than or equal to 100 GB daily, one user pays less than 5k per month.
    *   One user pays around 150k a month for Foundry, Snowflake, Fabric, little bit of Big Query, and Old ERP.
    *   Another user pays 300-400k per month for BigQuery and 100-150k for Databricks.

**[EDI in DE (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1owxx7s/edi_in_de/)**
*  **Summary:** This thread discusses the prevalence, challenges, and usefulness of EDI (Electronic Data Interchange) in data engineering.
*  **Emotion:** Overall, the tone is neutral, but with a hint of negativity towards EDI itself due to its complexity and lack of standardization.
*  **Top 3 Points of View:**
    *   EDI is still common in certain industries like finance, healthcare, and insurance.
    *   Working with EDI is generally a pain due to its lack of consistent standards.
    *   Using APIs for data transfers is preferable to EDI if possible.

**[Rejected 3x senior DE, feel like fraud (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1ox75em/rejected_3x_senior_de_feel_like_fraud/)**
*  **Summary:** A user shares their frustration and feelings of inadequacy after being rejected for multiple senior data engineering positions.
*  **Emotion:** The overall tone is negative, with the user feeling like a fraud. Some comments offer support and encouragement, adding some positive sentiment.
*  **Top 3 Points of View:**
    *   In a tough job market, aim for roles below your experience level.
    *   Focus on improving behavioral/culture interview skills.
    *   Apply for mid-level positions, focusing on the actual work rather than the title.

**[Sanity check: am I crazy for feeling like my "data engineering" position is a dead end? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ox84x9/sanity_check_am_i_crazy_for_feeling_like_my_data/)**
*  **Summary:** The user questions whether or not their data engineering position is a dead end.
*  **Emotion:** The overall emotional tone is neutral, but with a bit of negativity.
*  **Top 3 Points of View:**
    *   Sounds like a standard issue, but look at the experience you are getting.
    *   Push for a modern data engineering position, or look at another company.
    *   Consider whether the next step lies more with architecture or management.

**[When does Spark justify itself for Postgres to S3 ETL using Iceberg format? Sorry, I'm noob here. (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1owy8wn/when_does_spark_justify_itself_for_postgres_to_s3/)**
*  **Summary:** This thread seeks advice on when using Spark is justified for ETL from Postgres to S3 with Iceberg, given the user's current setup.
*  **Emotion:** The tone is mostly neutral, with a friendly and helpful atmosphere for the "noob" who asked the question.
*  **Top 3 Points of View:**
    *   Use Spark only when data is too big or slow to handle on one machine. If the current setup with Lambda + pyiceberg works, it's sufficient.
    *   Spark is useful for larger scale or complex transformations. Avoid overcomplicating if the current setup meets the needs.
    *   The current setup may be fine.

**[Best way to store financial statements and do some timeseries / benchmark analyses (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1ox1s0b/best_way_to_store_financial_statements_and_do/)**
*  **Summary:** The thread is about the best way to store financial statements and do some timeseries/benchmark analyses.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 2 Points of View:**
    *   Consider using a database like postgres. Easier to standardize, query, analyze.
    *   Have you tried using power query within excel? It can be pretty handy for routine stuff like that. You can break down your reports and standardize them into a local database that you can query off of pretty easily.

**[CMU Intro to Database Systems (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1owx9ut/cmu_intro_to_database_systems/)**
*  **Summary:** This thread is about what learning resources the user can use to learn database systems.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The AudoModerator's list is good enough, don't go anything fancy. Try to understand the concepts; each company has a unique stack anyway.
    *   go with the latest version, usually the most updated content. older ones might have outdated info, especially in fast-evolving fields like data engineering. good luck with your studies.

**[Need tips on a hybrid architecture for both real-time BI and ML (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ox4uvz/need_tips_on_a_hybrid_architecture_for_both/)**
*  **Summary:** A CTO of a small startup in South America is asking for tips for a hybrid architecture.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Point of View:**
    *   One user is being sarcastic, but the bot also sent a generic message saying You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources.

**[Is there a way to auto create data model from schemas of sources? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ox173p/is_there_a_way_to_auto_create_data_model_from/)**
*  **Summary:** A discussion on how to auto create data model from schemas of sources.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 2 Points of View:**
    *   Yes, you can partially automate it with a user-assisted approach. Column matching heuristics: match columns by name similarity, type compatibility, and low cardinality to suggest join keys. Statistical correlation: check overlapping values between columns across tables; high overlap indicates possible joins.
    *   Yes. Most DE tools guestimate the schema of files. Data models and relations can be guessed also, because often primary and foreign key relations follow standard patterns.

**[Would using Azure Data Factory in this Context be Overkill? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ox5kta/would_using_azure_data_factory_in_this_context_be/)**
*  **Summary:** The user is asking if using Azure Data Factory in their context be overkill.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 2 Points of View:**
    *   Data Factory is a better solution than a VM.
    *   Dasgter+ Astronomer and Prefect are better options for smaller workloads.

**[GIS Consulting to Data Engineering Salary (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ox5wiq/gis_consulting_to_data_engineering_salary/)**
*  **Summary:** The thread is on salary expectations when transitioning from GIS consulting to data engineering.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Points of View:**
    *   For any data roles, SQL is the key to survival followed by few other important skills as well.

**[Is it not pointless to transfer Parquet data with Kafka? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ox1e9h/is_it_not_pointless_to_transfer_parquet_data_with/)**
*  **Summary:** Is it not pointless to transfer Parquet data with Kafka?
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Kafka is not designed to pass that type of heavy data, it is designed to pass messages. You usually pass a reference to your data, like the URL of the parquet.
    *   Parquet with kafka doesn't optimize much. it's mainly marketing fluff. focus on other optimizations.
    *   These articles are single-mindedly focusing on the fact that Parquet is tiny. If you want to transform in flight, there are other formats you should use and then compress it into Parquet after the fact. Parquet should be used at rest not in motion.
