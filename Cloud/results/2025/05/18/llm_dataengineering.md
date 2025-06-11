---
title: "Data Engineering Subreddit"
date: "2025-05-18"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [How does Reddit / Instagram / Facebook count the number of comments / likes on posts? Isn't it a VERY expensive OP?](https://www.reddit.com/r/dataengineering/comments/1kpf00c/how_does_reddit_instagram_facebook_count_the/) (Score: 87)
    *   The discussion revolves around efficient methods for counting comments and likes on social media platforms, considering the scale of operations.
2.  [Do data engineers need to memorize programming syntax and granular steps, or do you just memorize conceptual knowledge of SQL, Python, the terminal, etc.](https://www.reddit.com/r/dataengineering/comments/1kpm7yv/do_data_engineers_need_to_memorize_programming/) (Score: 44)
    *   This thread explores whether data engineers need to memorize programming syntax or if conceptual knowledge is more important.
3.  [Starting My First Senior Analytics Engineer Role Soon. What Do You Wish You Knew When You Started?](https://www.reddit.com/r/dataengineering/comments/1kphk95/starting_my_first_senior_analytics_engineer_role/) (Score: 18)
    *   Users share advice for someone starting a senior analytics engineer role.
4.  [Kimball vs Inmon vs Dehghani](https://www.reddit.com/r/dataengineering/comments/1kpm88w/kimball_vs_inmon_vs_dehghani/) (Score: 15)
    *   The thread discusses different data modeling methodologies: Kimball, Inmon, and Dehghani (Data Mesh).
5.  [Batch Data Processing Stack](https://www.reddit.com/r/dataengineering/comments/1kpjqt0/batch_data_processing_stack/) (Score: 7)
    *   Discussion about batch data processing stack.
6.  [Postgres CDC Showdown: Conduit Crushes Kafka Connect](https://meroxa.com/blog/postgres-cdc-showdown-conduit-crushes-kafka-connect/) (Score: 5)
    *   Users are discussing a blog post comparing CDC tools.
7.  [The Open Table Format Revolution: Why Hyperscalers Are Betting on Managed Iceberg](http://rilldata.com/blog/the-open-table-format-revolution-why-hyperscalers-are-betting-on-managed-iceberg) (Score: 3)
    *   The thread discusses the open table format revolution
8.  [Small file problem in delta lake](https://www.reddit.com/r/dataengineering/comments/1kpe2hp/small_file_problem_in_delta_lake/) (Score: 3)
    *   Users are discussing the small file problem in Delta Lake
9.  [Sqoop alternative for on-prem infra to replace HDP](https://www.reddit.com/r/dataengineering/comments/1kph7d6/sqoop_alternative_for_onprem_infra_to_replace_hdp/) (Score: 3)
    *   Users are discussing Sqoop alternatives for on-premise infrastructure to replace HDP
10. [Technology Trends](https://www.reddit.com/r/dataengineering/comments/1kpq8bn/technology_trends/) (Score: 3)
    *   Users are discussing technology trends
11. [What are some common Python questions you’ve been asked a lot in live coding interviews?](https://www.reddit.com/r/dataengineering/comments/1kpprz8/what_are_some_common_python_questions_youve_been/) (Score: 2)
    *   Users discuss commonly asked python questions in interviews
12. [Must know hack/trick or just tips that can make a difference to how one can access data](https://www.reddit.com/r/dataengineering/comments/1kpgwz4/must_know_hacktrick_or_just_tips_that_can_make_a/) (Score: 1)
    *   Users are sharing data access tips and tricks.
13. [Excel for DEs?](https://www.reddit.com/r/dataengineering/comments/1kps5o8/excel_for_des/) (Score: 1)
    *   Users are discussing if data engineers need excel.
14. [I've tried many SQL AI tools — here's what I learned (and why I built Vaame)](https://i.redd.it/mxgeo5064l1f1.png) (Score: 0)
    *   Users are discussing SQL AI tools.
15. [Should I take DE Academy's $4K internship-prep course or Meta’s iOS Developer certificate from Coursera?](https://www.reddit.com/r/dataengineering/comments/1kpj5xb/should_i_take_de_academys_4k_internshipprep/) (Score: 0)
    *   Users are discussing DE Academy's courses.
16. [Building and Managing ETL Pipelines with Apache Airflow – A Complete Guide (2025 Edition)](https://www.reddit.com/r/dataengineering/comments/1kpm6f5/building_and_managing_etl_pipelines_with_apache/) (Score: 0)
    *   Users are discussing Building and Managing ETL Pipelines with Apache Airflow.
17. [How do I prepare for my summer internship?](https://www.reddit.com/r/dataengineering/comments/1kpsdvg/how_do_i_prepare_for_my_summer_internship/) (Score: 0)
    *   Users are discussing how to prepare for summer internship.
18. [AI + natural language for querying databases](https://www.reddit.com/r/dataengineering/comments/1kpse1k/ai_natural_language_for_querying_databases/) (Score: 0)
    *   Users are discussing AI + natural language for querying databases.

# Detailed Analysis by Thread
**[How does Reddit / Instagram / Facebook count the number of comments / likes on posts? Isn't it a VERY expensive OP? (Score: 87)](https://www.reddit.com/r/dataengineering/comments/1kpf00c/how_does_reddit_instagram_facebook_count_the/)**
*  **Summary:**  The discussion focuses on various methods used by social media platforms to efficiently count comments and likes on posts, including denormalized counters, sharded counters, in-memory caching, and probabilistic data structures.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Storing post counts as a separate value that increments with each new post.
    * Using denormalized counters within the post record for small-scale operations, and sharded counters for mid-scale.
    * Utilizing in-memory caching systems like Redis or Memcached to maintain current counts for low-latency reads.

**[Do data engineers need to memorize programming syntax and granular steps, or do you just memorize conceptual knowledge of SQL, Python, the terminal, etc. (Score: 44)](https://www.reddit.com/r/dataengineering/comments/1kpm7yv/do_data_engineers_need_to_memorize_programming/)**
*  **Summary:**  This thread discusses whether data engineers need to memorize programming syntax or if conceptual understanding and the ability to find information are more important.
*  **Emotion:** The overall emotional tone of the thread is Neutral, with a mix of informative and experience-based comments.
*  **Top 3 Points of View:**
    * Memorization of syntax is not crucial; conceptual understanding and the ability to use documentation are more important.
    * Focus on foundations and standards, memorizing what is frequently used.
    * Some interviewers may expect memorized syntax, but generally, it's not a requirement.

**[Starting My First Senior Analytics Engineer Role Soon. What Do You Wish You Knew When You Started? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1kphk95/starting_my_first_senior_analytics_engineer_role/)**
*  **Summary:**  Users share advice for someone starting a senior analytics engineer role, emphasizing asking questions, documenting processes, understanding existing systems, and proactive communication with stakeholders.
*  **Emotion:** The emotional tone of the thread is largely Neutral with hints of Positive.
*  **Top 3 Points of View:**
    * Ask questions and document everything.
    * Proactively set up meetings with key stakeholders.
    * Focus on project management and politics as a senior engineer.

**[Kimball vs Inmon vs Dehghani (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1kpm88w/kimball_vs_inmon_vs_dehghani/)**
*  **Summary:**  The thread compares different data modeling approaches, namely Kimball, Inmon, and Dehghani (Data Mesh). Data Mesh is more about the operating model, while Inmon focuses on overall system design, and Kimball focuses on modeling itself.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Data Mesh is an operating model, while Kimball and Inmon are modeling methodologies.
    * Inmon is upstream of Kimball, with Inmon suggesting Kimball marts downstream.
    * Data Vault modeling is a well-thought-out superset of other popular models.

**[Batch Data Processing Stack (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kpjqt0/batch_data_processing_stack/)**
*  **Summary:** The discussion involves possible tools for batch data processing stack.
*  **Emotion:** The overall emotional tone of the thread is Positive.
*  **Top 3 Points of View:**
    *  SSIS can be used for everything and it is the best ETL platform on the market.
    *  Should consider using SQLMesh.

**[Postgres CDC Showdown: Conduit Crushes Kafka Connect (Score: 5)](https://meroxa.com/blog/postgres-cdc-showdown-conduit-crushes-kafka-connect/)**
*  **Summary:** The discussion revolves around how Conduit compares to Kafka Connect.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   How does Conduit compares to PeerDB?

**[The Open Table Format Revolution: Why Hyperscalers Are Betting on Managed Iceberg (Score: 3)](http://rilldata.com/blog/the-open-table-format-revolution-why-hyperscalers-are-betting-on-managed-iceberg)**
*  **Summary:**  Discussion about why hyperscalers are betting on managed iceberg.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * The blog post was surprisingly a better read than I expected.

**[Small file problem in delta lake (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kpe2hp/small_file_problem_in_delta_lake/)**
*  **Summary:**  The discussion focuses on compaction and small files problem.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Delta compacts iteratively on each partition.
    * Small files problem would happen if you do a lot of small inserts.

**[Sqoop alternative for on-prem infra to replace HDP (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kph7d6/sqoop_alternative_for_onprem_infra_to_replace_hdp/)**
*  **Summary:**  The discussion focuses on different technologies for achieving the same functionality, with emphasis on considering all use cases.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * Using oracledb and pyarrow in Python could achieve the same functionality.
    * Spark is a heavier alternative.
    * The data size matters.

**[Technology Trends (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kpq8bn/technology_trends/)**
*  **Summary:**  The discussion focuses on different resources to keep track of technology trends.
*  **Emotion:** The overall emotional tone of the thread is Positive.
*  **Top 3 Points of View:**
    *  Suggest using daily.dev or bytebytego
    *  Suggest using youtube channel: Fireship.io

**[What are some common Python questions you’ve been asked a lot in live coding interviews? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kpprz8/what_are_some_common_python_questions_youve_been/)**
*  **Summary:** The discussion revolves around different Python questions asked during live coding interviews.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * List vs tuple
    * Dict comprehension
    * Sort a list of strings by the string length.

**[Must know hack/trick or just tips that can make a difference to how one can access data (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kpgwz4/must_know_hacktrick_or_just_tips_that_can_make_a/)**
*  **Summary:** Users are sharing data access tips and tricks.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * RemindMe 2 days

**[Excel for DEs? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kps5o8/excel_for_des/)**
*  **Summary:** Users are discussing if data engineers need excel.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[I've tried many SQL AI tools — here's what I learned (and why I built Vaame) (Score: 0)](https://i.redd.it/mxgeo5064l1f1.png)**
*  **Summary:** Users are discussing SQL AI tools.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * I would rather use GPT to write the query.

**[Should I take DE Academy's $4K internship-prep course or Meta’s iOS Developer certificate from Coursera? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kpj5xb/should_i_take_de_academys_4k_internshipprep/)**
*  **Summary:** Users are discussing DE Academy's courses.
*  **Emotion:** The overall emotional tone of the thread is Negative.
*  **Top 3 Points of View:**
    * DE and SE positions are different.
    * Do not pay 4 or 10 thousand dollars for job training.
    * These are completely different career paths which means this is not a serious question.

**[Building and Managing ETL Pipelines with Apache Airflow – A Complete Guide (2025 Edition) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kpm6f5/building_and_managing_etl_pipelines_with_apache/)**
*  **Summary:** Users are discussing Building and Managing ETL Pipelines with Apache Airflow.
*  **Emotion:** The overall emotional tone of the thread is Negative.
*  **Top 3 Points of View:**
    * Not only is this horrible AI text but also wrong and outdated.
    * More AI slop woohoo

**[How do I prepare for my summer internship? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kpsdvg/how_do_i_prepare_for_my_summer_internship/)**
*  **Summary:** Users are discussing how to prepare for summer internship.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    * You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[AI + natural language for querying databases (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kpse1k/ai_natural_language_for_querying_databases/)**
*  **Summary:** Users are discussing AI + natural language for querying databases.
*  **Emotion:** The overall emotional tone of the thread is Negative.
*  **Top 3 Points of View:**
    * I hate to be the bearer of the bad news but...
    * You can find our open-source project showcase here: https://dataengineering.wiki/Community/Projects
