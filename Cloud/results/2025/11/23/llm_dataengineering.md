---
title: "Data Engineering Subreddit"
date: "2025-11-23"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] B-Trees: Why Every Database Uses Them](https://www.reddit.com/r/dataengineering/comments/1p4iptk/btrees_why_every_database_uses_them/) (Score: 40)
    * Discusses the usage of B-Trees in databases.
2.  [Any recommendations for starting with system design?](https://www.reddit.com/r/dataengineering/comments/1p4h49s/any_recommendations_for_starting_with_system/) (Score: 11)
    * Seeks recommendations for resources to learn system design.
3.  [Strategies for DQ check at scale](https://www.reddit.com/r/dataengineering/comments/1p4bhgu/strategies_for_dq_check_at_scale/) (Score: 8)
    * Discusses strategies for data quality checks at scale, specifically profiling/drift detection with sampling instead of traditional DQ checks.
4.  [Data Observability Question](https://www.reddit.com/r/dataengineering/comments/1p4dkph/data_observability_question/) (Score: 5)
    * Asks about data observability and how to test for stale data.
5.  [Book / Resource recommendations for Modern Data Platform Architectures](https://www.reddit.com/r/dataengineering/comments/1p4827x/book_resource_recommendations_for_modern_data/) (Score: 4)
    * Seeks recommendations for books and resources on modern data platform architectures.
6.  [Biotech DE Help](https://www.reddit.com/r/dataengineering/comments/1p4cq23/biotech_de_help/) (Score: 4)
    *  Asks for help with building a biotech data pipeline.
7.  [A Behavioral Health Analytics Stack: Secure, Scalable, and Under $1000 Annually](https://www.reddit.com/r/dataengineering/comments/1p4cxmh/a_behavioral_health_analytics_stack_secure/) (Score: 4)
    * Presents a behavioral health analytics stack that is secure, scalable, and under $1000 annually.
8.  [When do you think job market will get better?](https://www.reddit.com/r/dataengineering/comments/1p4s2x4/when_do_you_think_job_market_will_get_better/) (Score: 3)
    * Discusses the current state of the job market for data engineers and when it might improve.
9.  [Need advice reg. Ingestion setup](https://www.reddit.com/r/dataengineering/comments/1p47jfc/need_advice_reg_ingestion_setup/) (Score: 2)
    * Seeks advice on setting up a data ingestion pipeline.
10. [How to speed up AWS Glue Spark job processing ~20k Parquet files across multiple patterns?](https://www.reddit.com/r/dataengineering/comments/1p4wj45/how_to_speed_up_aws_glue_spark_job_processing_20k/) (Score: 2)
    *  Asks for advice on speeding up an AWS Glue Spark job processing a large number of Parquet files.
11. [Dagster Partitioning for Hierarchical Data](https://www.reddit.com/r/dataengineering/comments/1p49fl5/dagster_partitioning_for_hierarchical_data/) (Score: 1)
    * Discusses Dagster partitioning strategies for hierarchical data.
12. [Feedback for experiment on HTAP database architecture with zarr like chunks](https://www.reddit.com/r/dataengineering/comments/1p4mp28/feedback_for_experiment_on_htap_database/) (Score: 1)
    * Seeks feedback on an experiment with an HTAP database architecture using Zarr-like chunks.
13. [Spark rapids reviews](https://www.reddit.com/r/dataengineering/comments/1p44fyv/spark_rapids_reviews/) (Score: 0)
    * Asks for reviews of Spark Rapids.
14. [AI assistants for data work](https://www.reddit.com/r/dataengineering/comments/1p4qki5/ai_assistants_for_data_work/) (Score: 0)
    * Discusses the use of AI assistants for data engineering tasks.
15. [Seeking advice: Join EXL/Inductis (analytics role) or wait for a proper Data Engineering job?](https://www.reddit.com/r/dataengineering/comments/1p4wpq2/seeking_advice_join_exlinductis_analytics_role_or/) (Score: 0)
    * Seeks advice on whether to accept an analytics role or wait for a data engineering job.

# Detailed Analysis by Thread
**[[D] B-Trees: Why Every Database Uses Them (Score: 40)](https://www.reddit.com/r/dataengineering/comments/1p4iptk/btrees_why_every_database_uses_them/)**
*  **Summary:** The thread discusses an article about why B-trees are used in every database.
*  **Emotion:** The overall emotional tone is Neutral, with some positive sentiment expressing appreciation for the article.
*  **Top 3 Points of View:**
    * Appreciation for the article.
    * Sharing of an ELI5 explanation video about b-trees.
    * Acknowledgement of a "dead internet" comment (likely a spam or low-effort remark).

**[Any recommendations for starting with system design? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1p4h49s/any_recommendations_for_starting_with_system/)**
*  **Summary:** The thread is a request for recommendations for learning system design, with suggestions provided.
*  **Emotion:** The overall emotional tone is Positive, due to the helpful suggestions offered.
*  **Top 3 Points of View:**
    * Recommendation of the book "Designing Data Intensive Applications" by Martin Kleppmann.
    * Suggestion to check a list of community-submitted learning resources on dataengineering.wiki.

**[Strategies for DQ check at scale (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1p4bhgu/strategies_for_dq_check_at_scale/)**
*  **Summary:**  The thread discusses using profiling/drift detection with sampling instead of traditional data quality (DQ) checks at scale.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Suggestion to use profiling/drift detection with sampling instead of traditional DQ checks.
    * Recommendation to use Trino's TABLESAMPLE for queries or Spark's .sample().
    * Advice on frequency of lightweight profiling (schema, basic stats) on every run and save detailed stats for a few runs per day.

**[Data Observability Question (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p4dkph/data_observability_question/)**
*  **Summary:** The thread asks about how to test for stale data in data observability.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Suggestion to use Grafana to connect directly to the database and run queries to test for stale data.
    * Suggestion to use Dagster and its asset freshness policies.

**[Book / Resource recommendations for Modern Data Platform Architectures (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p4827x/book_resource_recommendations_for_modern_data/)**
*  **Summary:** The thread is a request for book and resource recommendations on modern data platform architectures.
*  **Emotion:** The overall emotional tone is Neutral to Positive, with recommendations and anticipation for upcoming books.
*  **Top 3 Points of View:**
    * Recommendation of the book "Deciphering Data Architectures (2024)" by James Serra.
    * Mention of Joe Reis writing a book on data modeling.
    * Suggestion to check a list of community-submitted learning resources on dataengineering.wiki.

**[Biotech DE Help (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p4cq23/biotech_de_help/)**
*  **Summary:** The thread requests help with building a data engineering pipeline for biotech data.
*  **Emotion:** The overall emotional tone is Neutral, providing helpful advice.
*  **Top 3 Points of View:**
    * Suggestion to build one end-to-end biotech data pipeline like production, using tools like AWS/GCP, Prefect/Airflow, Snowflake/BigQuery, and dbt.
    * Suggestion to check out the github "local-data-stack" and a learning data engineering blog post.
    * Suggestion to check a list of community-submitted learning resources on dataengineering.wiki.

**[A Behavioral Health Analytics Stack: Secure, Scalable, and Under $1000 Annually (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p4cxmh/a_behavioral_health_analytics_stack_secure/)**
*  **Summary:** The thread presents an analytics stack for behavioral health that is secure, scalable, and inexpensive.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Asking which EHR is being used by the clinic.
    * Question about where to find SQL Server for $500.

**[When do you think job market will get better? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p4s2x4/when_do_you_think_job_market_will_get_better/)**
*  **Summary:** The thread discusses when the job market for data engineers is expected to improve.
*  **Emotion:** The overall emotional tone is mixed, leaning towards Neutral with some Positive sentiment, reflecting optimism alongside the concerns about the job market.
*  **Top 3 Points of View:**
    * Suggestion to get any job to pay bills while looking for a better opportunity.
    * The job market will improve in Q1 2026 or when the AI bubble pops.
    * Leverage past internship and co-op experience from Northeastern University.
    * If no internship before graduation, the job seeker is "cooked".

**[Need advice reg. Ingestion setup (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p47jfc/need_advice_reg_ingestion_setup/)**
*  **Summary:** The thread requests advice on setting up a data ingestion pipeline.
*  **Emotion:** The overall emotional tone is Neutral, providing helpful advice.
*  **Top 3 Points of View:**
    * Suggestion on how data life cycle management happening.
    * Suggestion to setup event grid notifications on new file creation.

**[How to speed up AWS Glue Spark job processing ~20k Parquet files across multiple patterns? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p4wj45/how_to_speed_up_aws_glue_spark_job_processing_20k/)**
*  **Summary:** The thread asks about speeding up an AWS Glue Spark job.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Asking if longer time taking while reading or writing or files are located in S3

**[Dagster Partitioning for Hierarchical Data (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p49fl5/dagster_partitioning_for_hierarchical_data/)**
*  **Summary:** The thread discusses Dagster partitioning strategies for hierarchical data.
*  **Emotion:** The overall emotional tone is Neutral, providing helpful advice and thoughts.
*  **Top 3 Points of View:**
    * Partitions might not be the right fit for that much volume.
    * Process at the lowest granularity you need for reprocessing.
    * Partition by ingestion batch rather than by the hierarchical data structure.

**[Feedback for experiment on HTAP database architecture with zarr like chunks (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p4mp28/feedback_for_experiment_on_htap_database/)**
*  **Summary:** The thread seeks feedback on an experiment with an HTAP database architecture.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Asking if the user mean pax aka parquet

**[Spark rapids reviews (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p44fyv/spark_rapids_reviews/)**
*   **Summary:** The thread is a request for reviews of Spark Rapids.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Questioning the need for speedups and suggesting Photon as an alternative.
    *   Reasons why it is not more widespread.
    *   Use for Large-scale aggregations across billions of rows

**[AI assistants for data work (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p4qki5/ai_assistants_for_data_work/)**
*  **Summary:** The thread discusses the use of AI assistants for data engineering tasks.
*  **Emotion:** The overall emotional tone is mixed, ranging from Positive (excitement about automation) to Negative (concerns about reliability), but generally leans Neutral.
*  **Top 3 Points of View:**
    * AI is great for automating grunt work but lacks knowledge about data schemas.
    * AI assistants are useful in daily tasks.
    * LLMs are useless for tasks that have to be right.

**[Seeking advice: Join EXL/Inductis (analytics role) or wait for a proper Data Engineering job? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p4wpq2/seeking_advice_join_exlinductis_analytics_role_or/)**
*  **Summary:** The thread seeks advice on whether to accept an analytics role or wait for a data engineering job.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *  How do you know it’s going to be a short employment gap?
