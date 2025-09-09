---
title: "Data Engineering Subreddit"
date: "2025-08-07"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] DuckDB is a weird beast](https://www.reddit.com/r/dataengineering/comments/1mjudxc/duckdb_is_a_weird_beast/) (Score: 103)
    *   Users are discussing the features, use cases, and benefits of DuckDB, comparing it to other databases like Snowflake and SQLite.
2.  [For anyone who has sat in on a Palantir sales pitch, what is it like?](https://www.reddit.com/r/dataengineering/comments/1mjo5ur/for_anyone_who_has_sat_in_on_a_palantir_sales/) (Score: 86)
    *   Redditors are sharing their experiences with Palantir sales pitches, highlighting the focus on "ontology" and the perceived lack of technical depth.
3.  [Snowflake is ending password only logins. What is your team switching to?](https://www.reddit.com/r/dataengineering/comments/1mjnv2z/snowflake_is_ending_password_only_logins_what_is/) (Score: 75)
    *   People are discussing the implications of Snowflake ending password-only logins and the alternative authentication methods their teams are adopting, such as SSO and key-pair authentication.
4.  [How we used DuckDB to save 79% on Snowflake BI spend](https://www.reddit.com/r/dataengineering/comments/1mk85dn/how_we_used_duckdb_to_save_79_on_snowflake_bi/) (Score: 45)
    *   This thread discusses how the poster used DuckDB to reduce costs associated with Snowflake BI, but other users request more detail regarding its implementation and the limitations of DuckDB.
5.  [How did you land your first Data Engineering job? MSCS student trying to break in within 6 months](https://www.reddit.com/r/dataengineering/comments/1mjte05/how_did_you_land_your_first_data_engineering_job/) (Score: 16)
    *   An MSCS student is seeking advice on how to land their first Data Engineering job. Users share tips on skills, certifications, and the job market.
6.  [Airflow users with a lot of DAGs how do you configure you schedules ?](https://www.reddit.com/r/dataengineering/comments/1mjojdk/airflow_users_with_a_lot_of_dags_how_do_you/) (Score: 9)
    *   The thread discusses strategies for managing and scheduling a large number of DAGs in Airflow, including event-based triggering and alternative scheduling tools.
7.  [Hedge-fund data engineer gigs in the EU: where are they hiding?](https://www.reddit.com/r/dataengineering/comments/1mjqthj/hedgefund_data_engineer_gigs_in_the_eu_where_are/) (Score: 9)
    *   A user is asking about the location of hedge-fund data engineer jobs in the EU.
8.  [Simple project / any suggestions?](https://www.reddit.com/r/dataengineering/comments/1mjn0rq/simple_project_any_suggestions/) (Score: 6)
    *   This post is a request for simple project suggestions, with a bot providing a link to community resources.
9.  [If a at least once system handles duplicates is it then deemed "exactly once"](https://www.reddit.com/r/dataengineering/comments/1mk3x2a/if_a_at_least_once_system_handles_duplicates_is/) (Score: 4)
    *   The question is whether deduplication in an "at least once" system makes it equivalent to "exactly once." The discussion revolves around message delivery semantics and data modeling.
10. [Hybrid KNN + BM25 Search in Elasticsearch: How can we optimize and improve latency? (Currently 7–10s response time)](https://www.reddit.com/r/dataengineering/comments/1mk4qzu/hybrid_knn_bm25_search_in_elasticsearch_how_can/) (Score: 3)
    *   This thread is about optimizing the latency of a hybrid KNN + BM25 search in Elasticsearch.
11. [Iceberg Tables + cross account + Glue ETL](https://www.reddit.com/r/dataengineering/comments/1mjwn5p/iceberg_tables_cross_account_glue_etl/) (Score: 2)
    *   The thread discusses the challenges and solutions for using Iceberg tables across AWS accounts with Glue ETL, focusing on permissions and metadata management.
12. [Seeking Advice: Handling Dynamic JSON outputs](https://www.reddit.com/r/dataengineering/comments/1mk45xj/seeking_advice_handling_dynamic_json_outputs/) (Score: 2)
    *   A user is seeking advice on how to handle dynamic JSON outputs.
13. [Need advice](https://www.reddit.com/r/dataengineering/comments/1mk8977/need_advice/) (Score: 2)
    *   This post is a general request for advice, with a bot providing a link to community resources.
14. [Rethinking Semantic Layers in the AI Era](https://www.reddit.com/r/dataengineering/comments/1mjvkan/rethinking_semantic_layers_in_the_ai_era/) (Score: 0)
    *   This thread explores the evolving role of semantic layers in the age of AI, with some arguing that AI is reducing the need for traditional semantic layers.
15. [Data camp premium subscription for DE certifications](https://www.reddit.com/r/dataengineering/comments/1mk9gsk/data_camp_premium_subscription_for_de/) (Score: 0)
    *   This post is about Data Camp premium subscription for DE certifications, with a bot providing a link to community resources.
16. [Should I stick to Data Engg or explore Backend Engg](https://www.reddit.com/r/dataengineering/comments/1mk9kmh/should_i_stick_to_data_engg_or_explore_backend/) (Score: 0)
    *   The user is asking for advice on whether to stick to Data Engineering or explore Backend Engineering.

# Detailed Analysis by Thread
**[[D] DuckDB is a weird beast (Score: 103)](https://www.reddit.com/r/dataengineering/comments/1mjudxc/duckdb_is_a_weird_beast/)**
*   **Summary:** This thread explores the capabilities and use cases of DuckDB, a columnar database, with comparisons to Snowflake and SQLite.
*   **Emotion:** Predominantly Neutral, with some Positive sentiment expressed when users discuss their positive experiences with DuckDB.
*   **Top 3 Points of View:**
    *   DuckDB is useful as a local data wrangler for transforming data.
    *   DuckDB can be used as a full-blown datalake and is cheaper and faster than Snowflake for certain workloads.
    *   DuckDB is an in-memory columnar database suitable for data scientists and engineers.

**[For anyone who has sat in on a Palantir sales pitch, what is it like? (Score: 86)](https://www.reddit.com/r/dataengineering/comments/1mjo5ur/for_anyone_who_has_sat_in_on_a_palantir_sales/)**
*   **Summary:** Users recount their experiences with Palantir sales pitches, often noting the heavy use of jargon ("ontology") and the lack of specific technical details.
*   **Emotion:** Mostly Neutral, with a hint of Negative sentiment from users who found the pitches confusing or underwhelming.
*   **Top 3 Points of View:**
    *   Palantir sells solutions using a platform and team of engineers, focusing on high-value solutions rather than specific data engineering tools.
    *   Palantir's "ontology" is considered cool in theory but expensive and difficult to use.
    *   Palantir's offerings are often redundant to what companies can build themselves, especially with existing analytics platforms like Databricks.

**[Snowflake is ending password only logins. What is your team switching to? (Score: 75)](https://www.reddit.com/r/dataengineering/comments/1mjnv2z/snowflake_is_ending_password_only_logins_what_is/)**
*   **Summary:** This thread discusses the transition away from password-only logins in Snowflake, with users sharing their team's chosen alternative authentication methods.
*   **Emotion:** Overwhelmingly Neutral, with some Positive sentiment related to increased security. Some Negative sentiment is expressed regarding the unexpected work required to update service accounts.
*   **Top 3 Points of View:**
    *   Many teams are switching to SSO (Single Sign-On) for standard users.
    *   Key-pair authentication is being used for programmatic access and Tableau.
    *   The change is seen as a positive step towards minimizing unintentional data access.

**[How we used DuckDB to save 79% on Snowflake BI spend (Score: 45)](https://www.reddit.com/r/dataengineering/comments/1mk85dn/how_we_used_duckdb_to_save_79_on_snowflake_bi/)**
*   **Summary:** This post details how DuckDB was used to drastically cut Snowflake BI costs, by implementing a Smart caching layer. However, other users are requesting more detail regarding its implementation and the limitations of DuckDB.
*   **Emotion:** Largely Neutral, with a mix of curiosity and skepticism. There's some Positive sentiment toward the cost savings, but also Negative sentiment questioning the necessity and limitations.
*   **Top 3 Points of View:**
    *   Implementing a caching layer using DuckDB can significantly reduce Snowflake BI costs.
    *   More details are needed to understand the specific implementation and limitations of this approach.
    *   If the majority of a Snowflake bill is BI queries, it may not be the optimal tool, suggesting other open-source solutions are better.

**[How did you land your first Data Engineering job? MSCS student trying to break in within 6 months (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1mjte05/how_did_you_land_your_first_data_engineering_job/)**
*   **Summary:** An MSCS student seeks advice on entering the field within 6 months, and the thread covers skills, resources, and job market realities.
*   **Emotion:** Mixed, with Positive encouragement alongside realistic and sometimes Negative assessments of the job market.
*   **Top 3 Points of View:**
    *   Focus on Python, SQL, Airflow, and AWS skills.
    *   Networking and personal projects are key to standing out.
    *   Breaking into the field in 6 months is considered challenging and potentially unrealistic.

**[Airflow users with a lot of DAGs how do you configure you schedules ? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1mjojdk/airflow_users_with_a_lot_of_dags_how_do_you/)**
*   **Summary:** This thread discusses best practices for scheduling and managing a large number of DAGs in Airflow.
*   **Emotion:** Neutral, with a focus on practical advice and solutions.
*   **Top 3 Points of View:**
    *   Event-based triggering is recommended for managing complex DAG dependencies.
    *   DAG dependencies should be well-defined within a directed analytic graph.
    *   Consider using a 3rd generation scheduler for better handling of complex dependencies.

**[Hedge-fund data engineer gigs in the EU: where are they hiding? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1mjqthj/hedgefund_data_engineer_gigs_in_the_eu_where_are/)**
*   **Summary:** A user is asking about the location of hedge-fund data engineer jobs in the EU.
*   **Emotion:** Mostly Neutral, with a hint of Positive sentiment from users who provide potential locations.
*   **Top 3 Points of View:**
    *   The largest funds are in the US, making DE jobs in EU rare.
    *   There are some open spots in Amsterdam/Rotterdam/Eindhoven.
    *   London is another potential location.

**[Simple project / any suggestions? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mjn0rq/simple_project_any_suggestions/)**
*   **Summary:** This post is a request for simple project suggestions, with a bot providing a link to community resources.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The thread serves to point users to community-submitted project resources.

**[If a at least once system handles duplicates is it then deemed "exactly once" (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1mk3x2a/if_a_at_least_once_system_handles_duplicates_is/)**
*   **Summary:** The discussion revolves around whether deduplication in an "at least once" system makes it equivalent to "exactly once."
*   **Emotion:** Primarily Neutral, focusing on technical definitions and distinctions. Some negative sentiment stems from addressing data modelling issues.
*   **Top 3 Points of View:**
    *   "At least once" and "exactly once" are terms for message delivery software, not entire systems.
    *   Deduplication alone doesn't transform an "at least once" system into an "exactly once" system.
    *   Data modeling perspective emphasizes business keys and SCD2 tables.

**[Hybrid KNN + BM25 Search in Elasticsearch: How can we optimize and improve latency? (Currently 7–10s response time) (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mk4qzu/hybrid_knn_bm25_search_in_elasticsearch_how_can/)**
*   **Summary:** This thread is about optimizing the latency of a hybrid KNN + BM25 search in Elasticsearch.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   More information is needed regarding the Elasticsearch setup.
    *   LanceDB is suggested as an alternative.

**[Iceberg Tables + cross account + Glue ETL (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mjwn5p/iceberg_tables_cross_account_glue_etl/)**
*   **Summary:** The thread discusses the challenges and solutions for using Iceberg tables across AWS accounts with Glue ETL.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Proper Lake Formation and Glue permissions are crucial for cross-account access.
    *   Glue catalog is useful for staying within the AWS native stack.
    *   Different operations require varying permission levels.

**[Seeking Advice: Handling Dynamic JSON outputs (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mk45xj/seeking_advice_handling_dynamic_json_outputs/)**
*   **Summary:** A user is seeking advice on how to handle dynamic JSON outputs
*   **Emotion:** Neutral, with some Positive feedback regarding potential solutions
*   **Top 3 Points of View:**
    *   Altering the database and pipeline for every change is overly rigid/coupled.
    *   Consider using a standard set of columns and a JSON field for additional data.
    *   DLT can handle schema migrations automatically.

**[Need advice (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mk8977/need_advice/)**
*   **Summary:** This post is a general request for advice, with a bot providing a link to community resources.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The thread serves to point users to community-submitted learning resources.

**[Rethinking Semantic Layers in the AI Era (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mjvkan/rethinking_semantic_layers_in_the_ai_era/)**
*   **Summary:** This thread explores the evolving role of semantic layers in the age of AI.
*   **Emotion:** Neutral to Negative, with differing opinions on the relevance of semantic layers.
*   **Top 3 Points of View:**
    *   Semantic layers enhance AI's ability to analyze data.
    *   AI is closing the gap on schema understanding without semantic layers, potentially making them irrelevant.
    *   It's about making data mart columns readable for LLMs to generate SQL.

**[Data camp premium subscription for DE certifications (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mk9gsk/data_camp_premium_subscription_for_de/)**
*   **Summary:** This post is about Data Camp premium subscription for DE certifications, with a bot providing a link to community resources.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The thread serves to point users to community-submitted learning resources.

**[Should I stick to Data Engg or explore Backend Engg (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mk9kmh/should_i_stick_to_data_engg_or_explore_backend/)**
*   **Summary:** The user is asking for advice on whether to stick to Data Engineering or explore Backend Engineering.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   DE is a growing field but entry-level roles are scarce.
