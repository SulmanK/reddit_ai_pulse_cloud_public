---
title: "Data Engineering Subreddit"
date: "2025-05-01"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Data governance, is it still worth learning it in 2025?](https://www.reddit.com/r/dataengineering/comments/1kc7n6p/data_governance_is_it_still_worth_learning_it_in/) (Score: 40)
    *   Users discussed the importance and relevance of data governance in 2025, with some highlighting its criticality in regulated environments and for AI decision-making.
2.  [2 questions](https://i.redd.it/vogasdqjj6ye1.png) (Score: 21)
    *   The thread revolves around advice for aspiring data engineers, the requirements of a DE job and LinkedIn posts.
3.  [Goodbye PyDeequ: A new take on data quality in Spark](https://www.reddit.com/r/dataengineering/comments/1kc5giw/goodbye_pydeequ_a_new_take_on_data_quality_in/) (Score: 20)
    *   Users are discussing a new approach to data quality in Spark, with some comparing it to existing tools like Deequ and Cuallee.
4.  [StatQL – live, approximate SQL for huge datasets and many tenants](https://v.redd.it/9mknlmvd77ye1) (Score: 7)
    *   A user shared what they thought was "Cool stuff."
5.  [Does it make sense to use DuckDB just as a pandas replacement?](https://www.reddit.com/r/dataengineering/comments/1kcdfg2/does_it_make_sense_to_use_duckdb_just_as_a_pandas/) (Score: 6)
    *   Users discuss the pros and cons of using DuckDB as a replacement for Pandas, touching on performance, coding style, and integration with tools like Dagster and DBT.
6.  [best ai model for polars?](https://www.reddit.com/r/dataengineering/comments/1kcc50e/best_ai_model_for_polars/) (Score: 4)
    *   Users are discussing the best AI models to use with Polars, a relatively new data manipulation library, and considering the limited training data available.
7.  [Convert bitemporal data to iceberg table preserving time travel?](https://www.reddit.com/r/dataengineering/comments/1kcbp2m/convert_bitemporal_data_to_iceberg_table/) (Score: 3)
    *   A user asked about time travel in Iceberg. It's suggested Z-Ordering can be used to index bitemporal data and XTDB is also designed to store such data.
8.  [Just launched a course on building a simple AI agent with Llama + Flask – free at the moment](https://www.reddit.com/r/dataengineering/comments/1kc9jd4/just_launched_a_course_on_building_a_simple_ai/) (Score: 2)
    *   A user shared a course on building an AI agent, and people thanked him and said that they'd check it out.
9.  [Senior Data Engineer role](https://www.reddit.com/r/dataengineering/comments/1kceit1/senior_data_engineer_role/) (Score: 2)
    *   A user suggested what type of question might be asked in an interview.
10. [Trying to build a full data pipeline - does this architecture make sense?](https://www.reddit.com/r/dataengineering/comments/1kcfjo6/trying_to_build_a_full_data_pipeline_does_this/) (Score: 2)
    *   Users discussed the architecture of a proposed data pipeline, with suggestions to use AWS Data Firehose instead of Spark Streaming.
11. [How difficult is DE and whats the future scope](https://www.reddit.com/r/dataengineering/comments/1kce1jv/how_difficult_is_de_and_whats_the_future_scope/) (Score: 1)
    *   A user shared their experience as a DE in different types of companies.
12. [Partitioning JSON Is this a mistake?](https://www.reddit.com/r/dataengineering/comments/1kcg2mo/partitioning_json_is_this_a_mistake/) (Score: 1)
    *   Users are discussing the implications of partitioning JSON files, asking for clarification on the specific problem and offering advice on data reconciliation.
13. [Looking to move from Data Analyst to Data Engineer – would love your advice!](https://www.reddit.com/r/dataengineering/comments/1kchyk5/looking_to_move_from_data_analyst_to_data/) (Score: 1)
    *   A bot shares links to community-submitted learning resources.
14. [Shopify GraphQL Data Ingestion](https://www.reddit.com/r/dataengineering/comments/1kc6nen/shopify_graphql_data_ingestion/) (Score: 0)
    *   A user provided advice on how to use GraphQL to extract Shopify data and suggested using Airflow for transformations.

# Detailed Analysis by Thread
**[Data governance, is it still worth learning it in 2025? (Score: 40)](https://www.reddit.com/r/dataengineering/comments/1kc7n6p/data_governance_is_it_still_worth_learning_it_in/)**
*  **Summary:** The thread discusses the importance and relevance of data governance in 2025. Users debate whether it's still a valuable skill, with some emphasizing its necessity in regulated industries and others questioning what "learning data governance" even means. There is a consensus that data governance is crucial for AI and decision-making.
*  **Emotion:** The overall emotional tone is Neutral, though there are snippets of positive sentiment when users emphasize the importance of data governance.
*  **Top 3 Points of View:**
    *   Data governance is increasingly important, especially in regulated sectors like finance and life sciences.
    *   Data governance is essential for organizations using AI for decision-making. Without it, AI is not possible.
    *   The meaning of "learning data governance" is ambiguous, and the field lacks a universally agreed-upon definition.

**[2 questions (Score: 21)](https://i.redd.it/vogasdqjj6ye1.png)**
*  **Summary:** This thread discusses advice for aspiring data engineers in a tough job market. Users debated whether DE is an entry-level position and how to stand out, recommending personal projects and focusing on core skills like SQL and Python. Some criticized LinkedIn posts with generic advice.
*  **Emotion:** The overall emotional tone is Neutral. There is a touch of negative sentiment regarding the difficulty of breaking into the field, but some positive comments offer encouragement.
*  **Top 3 Points of View:**
    *   Data engineering is generally not considered an entry-level position and requires prior experience in data-related roles.
    *   Building a portfolio with personal projects on platforms like GitHub is an effective way to demonstrate skills and stand out to recruiters.
    *   Generic advice found on platforms like LinkedIn should be taken with a grain of salt, and a focus on practical skills and experience is more valuable.

**[Goodbye PyDeequ: A new take on data quality in Spark (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1kc5giw/goodbye_pydeequ_a_new_take_on_data_quality_in/)**
*  **Summary:** The thread is centered around a new data quality tool for Spark, with users sharing their experiences with similar tools like Deequ and Cuallee. They appreciated the configurable element.
*  **Emotion:** The overall emotional tone is Positive, with users expressing interest and appreciation for the new tool.
*  **Top 3 Points of View:**
    *   The new data quality tool looks promising and addresses some limitations of existing tools like Deequ.
    *   Cuallee is a helpful alternative to PyDeequ, particularly for its dataframe-agnostic nature.
    *   Configurability with YAML is a desirable feature.

**[StatQL – live, approximate SQL for huge datasets and many tenants (Score: 7)](https://v.redd.it/9mknlmvd77ye1)**
*  **Summary:** The thread is very simple, with a user sharing a link and another simply responding "Cool stuff"
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   One user thought it was "Cool stuff."

**[Does it make sense to use DuckDB just as a pandas replacement? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kcdfg2/does_it_make_sense_to_use_duckdb_just_as_a_pandas/)**
*  **Summary:** This thread discusses the use of DuckDB as a Pandas replacement. The conversation covers the advantages and disadvantages of DuckDB, its integration with other tools like Dagster and DBT, and the choice between SQL and Pythonic coding styles.
*  **Emotion:** The emotional tone is mostly Neutral, with a mix of positive and negative aspects being discussed.
*  **Top 3 Points of View:**
    *   DuckDB is a good replacement for Pandas, especially when dealing with many csv/parquet files or complex SQL queries.
    *   The choice between DuckDB and Pandas depends on coding style preferences (SQL vs. Pythonic).
    *   For data filling, visualization, and machine learning, other tools like Polars or Pandas may be necessary.

**[best ai model for polars? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1kcc50e/best_ai_model_for_polars/)**
*  **Summary:** This thread discusses the best AI models for use with Polars. The limited availability of Polars-specific training data is a central concern.
*  **Emotion:** The emotional tone is mixed. Some positive comments suggest specific models, but negative comments point out the limited resources available to train AI on Polars.
*  **Top 3 Points of View:**
    *   Due to the limited amount of training data, no existing AI model does well on Polars.
    *   Gemini 2.5 is a potentially good option, especially when fed the Polars documentation.
    *   The deepseek v3 model is excellent at Polars.

**[Convert bitemporal data to iceberg table preserving time travel? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kcbp2m/convert_bitemporal_data_to_iceberg_table/)**
*  **Summary:** The thread discusses the feasibility of using Apache Iceberg to store bitemporal data and preserve time travel. It suggests z-ordering and XTDB.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Z-Ordering can be used to index bitemporal data.
    *   The native time-travel features in Iceberg are not particularly helpful for bitemporal data.
    *   XTDB is an alternative option for storing bitemporal data.

**[Just launched a course on building a simple AI agent with Llama + Flask – free at the moment (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kc9jd4/just_launched_a_course_on_building_a_simple_ai/)**
*  **Summary:** The thread discusses the launching of a new free course on building an AI agent.
*  **Emotion:** The overall emotional tone is very positive.
*  **Top 3 Points of View:**
    *   Thanks for sharing.
    *   Appreciation for sharing with the community.
    *   Grabbed the course and will walk through it.

**[Senior Data Engineer role (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kceit1/senior_data_engineer_role/)**
*  **Summary:** The thread discusses possible interview questions for a senior data engineer role.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Expect questions on window functions in Pyspark.

**[Trying to build a full data pipeline - does this architecture make sense? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kcfjo6/trying_to_build_a_full_data_pipeline_does_this/)**
*  **Summary:** This thread discusses the architecture of a data pipeline and asks for feedback.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The proposed architecture might be overkill depending on the amount of data expected.
    *   AWS Data Firehose is a good alternative to Spark Streaming.
    *   Apache Iceberg tables could be used for data landing.

**[How difficult is DE and whats the future scope (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kce1jv/how_difficult_is_de_and_whats_the_future_scope/)**
*  **Summary:** The user shares their experiences as a DE in different companies.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   The difficulty and stress of a DE role depend on the company culture and priorities.
    *   A company that values data and invests in best practices is a more rewarding place to work.
    *   Terabyte scale and real-time data require more robust infrastructure and a larger team.

**[Partitioning JSON Is this a mistake? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kcg2mo/partitioning_json_is_this_a_mistake/)**
*  **Summary:** The user is asking for opinions on whether partitioning JSON is a mistake.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Partitioning files can be a valid strategy for larger pipelines.
    *   It is important to ensure data reconciles at the end of the job.

**[Looking to move from Data Analyst to Data Engineer – would love your advice! (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kchyk5/looking_to_move_from_data_analyst_to_data/)**
*  **Summary:** Bot provided learning resources.
*  **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   The bot linked to learning resources.

**[Shopify GraphQL Data Ingestion (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kc6nen/shopify_graphql_data_ingestion/)**
*   **Summary:** The thread discusses the process of ingesting data from Shopify using GraphQL and provides advice on date filtering, pagination, and rate limiting.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Use `createdAt_gte` and `createdAt_lte` for date filtering in GraphQL queries.
    *   Properly handle cursor-based pagination by tracking the `endCursor` value.
    *   Implement backoff retry logic to manage Shopify API rate limits.
