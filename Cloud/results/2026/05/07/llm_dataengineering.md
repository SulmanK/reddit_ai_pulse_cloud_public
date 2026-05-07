---
title: "Data Engineering Subreddit"
date: "2026-05-07"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "subreddit analysis", "reddit"]
---

# Overall Ranking and Top Discussions
*   1. [[D] Is anyone migrating away from Databricks?](https://www.reddit.com/r/dataengineering/comments/1t6ch3j/is_anyone_migrating_away_from_databricks/) (Score: 129)
    *   This thread discusses the reasons and experiences of users migrating away from Databricks, with a focus on cost, alternatives, and the trade-offs involved.
*   2. [[D] Do you really need Spark?](https://www.reddit.com/r/dataengineering/comments/1t6f1lo/do_you_really_need_spark/) (Score: 31)
    *   This discussion explores whether Spark is truly necessary for data engineering tasks, considering data size, alternatives, and the platform's versatility.
*   3. [[ADHD] Data engineers](https://www.reddit.com/r/dataengineering/comments/1t6g4j1/adhd_data_engineers/) (Score: 16)
    *   This thread focuses on the experiences and strategies of data engineers who have ADHD, discussing how they manage their work and challenges.
*   4. [How are you guys handling Iceberg table maintenance in production?](https://www.reddit.com/r/dataengineering/comments/1t66thf/how_are_you_guys_handling_iceberg_table/) (Score: 12)
    *   Users share their methods and tools for maintaining Iceberg tables in production environments, including automation and best practices.
*   5. [Should i use fivetran](https://www.reddit.com/r/dataengineering/comments/1t5vlzc/should_i_use_fivetran/) (Score: 8)
    *   This thread delves into the pros and cons of using Fivetran for data ingestion, with discussions on cost, simplicity, and alternative tools.
*   6. [Hello folks,](https://www.reddit.com/r/dataengineering/comments/1t5zro8/hello_folks/) (Score: 6)
    *   This post is a request for learning resources in data engineering, with users recommending books and online materials.
*   7. [do you think cloud compute costs are quietly eating our entire department's budget ?](https://www.reddit.com/r/dataengineering/comments/1t6aue9/do_you_think_cloud_compute_costs_are_quietly/) (Score: 3)
    *   This discussion centers on the rising costs of cloud compute and strategies for optimizing expenses within data engineering departments.
*   8. [How we cut DQE testing from 4 days to 3 hours using config-driven SQL templates — wrote about it](https://www.reddit.com/r/dataengineering/comments/1t66m42/how_we_cut_dqe_testing_from_4_days_to_3_hours/) (Score: 3)
    *   A user shares their experience in significantly reducing DQE testing time through a specific methodology.
*   9. [Sub-second query on Iceberg data lakes using Apache Pinot's indexes](https://www.reddit.com/r/dataengineering/comments/1t6g1mr/subsecond_query_on_iceberg_data_lakes_using/) (Score: 2)
    *   This thread discusses the performance of Apache Pinot for querying Iceberg data lakes and comparisons with other technologies.
*   10. [How to make Nifi reusable/dynamic pipeline!?](https://www.reddit.com/r/dataengineering/comments/1t69xaj/how_to_make_nifi_reusabledynamic_pipeline/) (Score: 1)
    *   A user is seeking ways to make NiFi pipelines more reusable and dynamic.
*   11. [Data-Analytics-Essential-Course Completion CISCO](https://www.reddit.com/r/dataengineering/comments/1t6f5so/dataanalyticsessentialcourse_completion_cisco/) (Score: 0)
    *   This post appears to be about completing a Cisco Data Analytics course, with comments offering advice on practical application.

# Detailed Analysis by Thread
**[ Is anyone migrating away from Databricks? (Score: 129)](https://www.reddit.com/r/dataengineering/comments/1t6ch3j/is_anyone_migrating_away_from_databricks/)**
*   **Summary:** Users are discussing their reasons for migrating away from Databricks, with cost being a primary driver. Alternatives like AWS native services, S3+Parquet with Athena/DuckDB, and on-premises solutions are being considered. Some believe Databricks is for companies that prioritize platform convenience over employee expertise.
*   **Emotion:** Predominantly Neutral, with some undertones of concern regarding cost and a desire for more control or efficiency.
*   **Top 3 Points of View:**
    *   Migrating to AWS native services due to high bills, with Databricks seen as a premium for convenience.
    *   Using S3+Parquet with Athena or DuckDB for smaller, non-ML use cases.
    *   Databricks can be optimized for cost and performance with careful configuration, but it's generally more expensive and might be overkill for smaller operations.

**[ Do you really need Spark? (Score: 31)](https://www.reddit.com/r/dataengineering/comments/1t6f1lo/do_you_really_need_spark/)**
*   **Summary:** The discussion revolves around the necessity of Spark in data engineering. Participants share their experiences with Spark for various data sizes (from tens of TB to small datasets) and highlight its versatility as a data platform, while also acknowledging alternatives like DuckDB, Postgres, and Polars. The overhead of setting up Spark and the prevalence of AI-driven use cases are also mentioned.
*   **Emotion:** Mostly Neutral, with a slightly negative sentiment towards Spark being overused or unnecessarily implemented for smaller tasks.
*   **Top 3 Points of View:**
    *   Spark is a powerful and versatile data platform, suitable for large-scale data processing and offering flexibility due to its open-source nature.
    *   Spark may be overkill for smaller datasets or specific use cases, with alternatives like DuckDB, Postgres, and Polars being more efficient and cost-effective.
    *   Proper implementation of Spark, including partitioning, clustering, and optimization, can lead to low costs, but requires dedication and experienced personnel.

**[ ADHD data engineers (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1t6g4j1/adhd_data_engineers/)**
*   **Summary:** This thread offers advice and shared experiences from data engineers who have ADHD. Discussions cover treatment strategies, managing hyperfocus, structuring work, dealing with context switching, and adapting work environments.
*   **Emotion:** Primarily Neutral, with a supportive and empathetic tone as individuals share personal challenges and coping mechanisms. Some positive sentiment is present when discussing effective strategies.
*   **Top 3 Points of View:**
    *   Treating ADHD requires a multi-faceted approach including medication, therapy, and consistent behavioral routines (sleep, exercise, diet).
    *   ADHD can be managed by structuring tasks and environments to leverage hyperfocus and reduce distractions, rather than fighting against it.
    *   Finding a work environment that accommodates individual needs, such as smaller companies or roles with more autonomy, can be crucial for success.

**[ How are you guys handling Iceberg table maintenance in production? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1t66thf/how_are_you_guys_handling_iceberg_table/)**
*   **Summary:** Data engineers are sharing their strategies for maintaining Iceberg tables in production. This includes using automated Spark jobs triggered by cloud events, leveraging AWS services like Glue and Athena for optimization, and managing maintenance logic through separate Airflow DAGs for better organization.
*   **Emotion:** Mostly Neutral, with a touch of shared frustration about the "pleasures" of modern data engineering but also a sense of shared problem-solving.
*   **Top 3 Points of View:**
    *   Automation is key, with Spark jobs (often CDk-generated) and event triggers being used for maintenance tasks.
    *   Cloud provider services (AWS Glue, Athena) simplify maintenance by offering built-in optimization and cataloging features.
    *   Moving maintenance logic to dedicated orchestration tools like Airflow can help manage complexity compared to integrating it directly into Spark jobs.

**[ Should i use fivetran (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1t5vlzc/should_i_use_fivetran/)**
*   **Summary:** This thread discusses the merits and drawbacks of using Fivetran for data ingestion. The primary concerns are its cost, especially at scale, while its simplicity and ease of use for connecting to various sources are acknowledged as significant advantages. Alternatives like Airbyte are also suggested.
*   **Emotion:** Neutral, with a clear division between those who find Fivetran too expensive and those who value its simplicity. There's a notable "hate" for Fivetran expressed by some users.
*   **Top 3 Points of View:**
    *   Fivetran is expensive, particularly as data volume and the number of sources increase, leading many to seek cheaper alternatives like Airbyte.
    *   Fivetran offers significant simplicity and speed for data ingestion, making it a worthwhile trade-off for teams that prioritize ease of use and have the budget.
    *   The decision to use Fivetran depends on understanding its specific use case, limitations, and whether the cost justifies the simplicity compared to building and managing pipelines internally or with open-source tools.

**[ Hello folks, (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1t5zro8/hello_folks/)**
*   **Summary:** Users are seeking recommendations for data engineering learning resources. The discussion highlights a preference for books like "Designing Data-Intensive Applications" and "The Data Warehouse Toolkit," alongside practical study of open-source systems like Airflow, Spark, and Kafka.
*   **Emotion:** Neutral, with a sense of curiosity about learning methods and a collaborative sharing of valuable resources.
*   **Top 3 Points of View:**
    *   Foundational books such as "Designing Data-Intensive Applications" and "The Data Warehouse Toolkit" are highly recommended for a solid understanding of data engineering principles.
    *   Combining theoretical knowledge from books with practical experience from studying and working with real-world open-source systems (Airflow, Spark, Kafka) accelerates learning.
    *   Online resources, including community-submitted lists, are also valuable, but there's a distinct appreciation for the structured and in-depth knowledge offered by books.

**[ do you think cloud compute costs are quietly eating our entire department's budget ? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1t6aue9/do_you_think_cloud_compute_costs_are_quietly/)**
*   **Summary:** This thread addresses the growing concern of cloud compute costs impacting data engineering budgets. Participants offer various strategies for cost optimization, including analyzing usage, pre-purchasing compute, optimizing idle resources, and leveraging tools like `swmgpu` for spot pricing.
*   **Emotion:** Neutral, with a shared concern about rising costs and a focus on practical solutions and best practices for cost management.
*   **Top 3 Points of View:**
    *   Thorough analysis of compute usage is critical to identify cost-saving opportunities, such as optimizing idle instances, consolidating workflows, and turning down unnecessary latency.
    *   Leveraging cloud provider recommendations and features like reserved instances or spot pricing (e.g., with `swmgpu`) can lead to significant savings.
    *   Proactive cost management, including performance tuning, retiring unused processes, and implementing hard limits, is an integral part of data engineering.

**[ How we cut DQE testing from 4 days to 3 hours using config-driven SQL templates — wrote about it (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1t66m42/how_we_cut_dqe_testing_from_4_days_to_3_hours/)**
*   **Summary:** A user shares their experience of reducing Data Quality Engineering (DQE) testing time from four days to three hours by implementing config-driven SQL templates. The focus is on identifying weaknesses in shared assumptions between tests and the system.
*   **Emotion:** Positive, with the commenter highlighting the impressive achievement and the insightful architectural thinking behind the solution.
*   **Top 3 Points of View:**
    *   The significant reduction in testing time from 4 days to 3 hours is a notable accomplishment.
    *   Identifying and addressing weaknesses in shared assumptions between tests and the system is a key factor in creating robust solutions.
    *   The methodology used demonstrates strong architectural thinking, which leads to genuinely robust outcomes.

**[ Sub-second query on Iceberg data lakes using Apache Pinot's indexes (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1t6g1mr/subsecond_query_on_iceberg_data_lakes_using/)**
*   **Summary:** This thread discusses the performance of Apache Pinot for querying Iceberg data lakes, with users inquiring about comparisons to other systems like StarRocks, performance during data changes, metadata handling, and speeds relative to DuckDB. Cost considerations for Pinot are also raised.
*   **Emotion:** Neutral, with users posing technical questions and seeking comparative data on performance and cost.
*   **Top 3 Points of View:**
    *   Inquiries are made about comparative performance studies against systems like StarRocks.
    *   Questions are raised about how Pinot handles changes to underlying Iceberg tables, metadata storage, and performance with string columns.
    *   Comparisons to DuckDB's speeds and its direct conversion from Iceberg are sought, along with the cost implications of using Pinot.

**[ How to make Nifi reusable/dynamic pipeline!? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1t69xaj/how_to_make_nifi_reusabledynamic_pipeline/)**
*   **Summary:** A user is asking for advice on making NiFi pipelines more reusable and dynamic. A comment suggests considering the `dlt` (Data Load Tool) library as an alternative or complementary solution.
*   **Emotion:** Neutral, with the main post being a straightforward technical question and the comment offering an off-topic but relevant suggestion.
*   **Top 3 Points of View:**
    *   The user is seeking methods to enhance reusability and dynamism in NiFi pipelines.
    *   The `dlt` (Data Load Tool) is proposed as a potential solution or alternative to explore.
    *   The discussion touches upon the broader landscape of data ingestion and transformation tools.

**[ Data-Analytics-Essential-Course Completion CISCO (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1t6f5so/dataanalyticsessentialcourse_completion_cisco/)**
*   **Summary:** This post is about the completion of a Cisco Data Analytics course. Comments advise that practical project experience is more valuable than certifications alone, and links to general learning resources are shared.
*   **Emotion:** Neutral, with practical advice being offered to complement theoretical learning.
*   **Top 3 Points of View:**
    *   Completing courses and certifications is helpful, but executing projects is crucial to demonstrate practical skills.
    *   A shared resource list for data engineering learning is provided.
    *   The value of hands-on experience is emphasized over solely relying on course completion.
