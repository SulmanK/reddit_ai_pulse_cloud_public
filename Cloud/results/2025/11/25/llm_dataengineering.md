---
title: "Data Engineering Subreddit"
date: "2025-11-25"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Are data engineers being asked to build customer-facing AI “chat with data” features?](https://www.reddit.com/r/dataengineering/comments/1p6csl9/are_data_engineers_being_asked_to_build/) (Score: 36)
    * The discussion revolves around whether data engineers are increasingly tasked with creating AI-powered "chat with data" features for customers, with many sharing their experiences and perspectives on the challenges and approaches involved.
2.  [Spark doesn’t respect distribution of cached data](https://www.reddit.com/r/dataengineering/comments/1p67d7u/spark_doesnt_respect_distribution_of_cached_data/) (Score: 14)
    * The thread discusses the problem of Spark not respecting the distribution of cached data.
3.  [I'm tired](https://www.reddit.com/r/dataengineering/comments/1p61zft/im_tired/) (Score: 12)
    * A user expresses their tiredness, prompting supportive and humorous responses, along with resource links from a bot.
4.  [Which is best CDC top to end pipeline?](https://www.reddit.com/r/dataengineering/comments/1p6c95f/which_is_best_cdc_top_to_end_pipeline/) (Score: 10)
    * The discussion centers on the best approaches for building a Change Data Capture (CDC) pipeline, with various solutions and architectures being proposed.
5.  [How to control agents accessing sensitive customer data in internal databases](https://www.reddit.com/r/dataengineering/comments/1p67c7k/how_to_control_agents_accessing_sensitive/) (Score: 8)
    * This thread focuses on methods for controlling agent access to sensitive customer data within internal databases, emphasizing security and policy enforcement.
6.  [How do you test?](https://www.reddit.com/r/dataengineering/comments/1p5x8ah/how_do_you_test/) (Score: 7)
    * This thread asked community how they test their work.
7.  [If I cannot use InfluxDB nor TimescaleDB, is there something faster than Parquet? (e.g. stored at Amazon S3)](https://www.reddit.com/r/dataengineering/comments/1p69hz5/if_i_cannot_use_influxdb_nor_timescaledb_is_there/) (Score: 7)
    * The discussion focuses on finding faster alternatives to Parquet for time-series data storage in Amazon S3, when InfluxDB and TimescaleDB are not options.
8.  [Evaluating AWS DMS vs Estuary Flow](https://www.reddit.com/r/dataengineering/comments/1p6fpt5/evaluating_aws_dms_vs_estuary_flow/) (Score: 6)
    * Users are comparing and contrasting AWS DMS and Estuary Flow for data integration and Change Data Capture (CDC) purposes.
9.  [We wrote our first case study as a blend of technical how to and customer story on Snowflake optimization. Wdyt?](https://blog.greybeam.ai/headset-snowflake-playbook/) (Score: 5)
    * Users discuss a case study on Snowflake optimization, particularly focusing on serving queries to a large number of users.
10. [Handling data quality issues that are a tiny percentage?](https://www.reddit.com/r/dataengineering/comments/1p6fmpt/handling_data_quality_issues_that_are_a_tiny/) (Score: 4)
    * The discussion centers on how to handle data quality issues that affect only a small percentage of data.
11. [Is it realistic to replicate a 3000 line Oracle view in Snowflake (any suggestions would help)](https://www.reddit.com/r/dataengineering/comments/1p6n53i/is_it_realistic_to_replicate_a_3000_line_oracle/) (Score: 4)
    * The thread discusses the feasibility of replicating a complex Oracle view in Snowflake.
12. [Thoughts on WhereScape RED as a DWH tool.](https://www.reddit.com/r/dataengineering/comments/1p5z2rb/thoughts_on_wherescape_red_as_a_dwh_tool/) (Score: 3)
    * This thread asks for community thoughts on WhereScape RED as a DWH tool.
13. [Best way to count distinct values](https://www.reddit.com/r/dataengineering/comments/1p6k23x/best_way_to_count_distinct_values/) (Score: 3)
    * The thread explores different methods for efficiently counting distinct values in large datasets.
14. [Do Data Engineers Benefit from a Master’s Degree, or Is Experience Enough?](https://www.reddit.com/r/dataengineering/comments/1p6nt4g/do_data_engineers_benefit_from_a_masters_degree/) (Score: 2)
    * The discussion revolves around whether a master's degree is beneficial for data engineers, or if experience is sufficient.
15. [Row level security in Snowflake unsecure?](https://www.reddit.com/r/dataengineering/comments/1p6l0ps/row_level_security_in_snowflake_unsecure/) (Score: 1)
    * The thread is about whether row-level security is secure in Snowflake.

# Detailed Analysis by Thread
**[[D] Are data engineers being asked to build customer-facing AI “chat with data” features? (Score: 36)](https://www.reddit.com/r/dataengineering/comments/1p6csl9/are_data_engineers_being_asked_to_build/)**
*  **Summary:** The thread explores the increasing demand for data engineers to build customer-facing AI "chat with data" features. Participants discuss their experiences, the technologies involved, and the challenges of implementing such features effectively.
*  **Emotion:** The overall emotional tone is neutral, with a focus on practical discussions and information sharing.
*  **Top 3 Points of View:**
    *   Data engineers are indeed being asked to build these features, often involving API and React integration.
    *   Some believe that current AI models are not adequate for exploring the vast amount of enterprise data, making the ask somewhat unrealistic.
    *   Others are successfully building agentic data layers and using tools like Cursor to accelerate development.

**[Spark doesn’t respect distribution of cached data (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1p67d7u/spark_doesnt_respect_distribution_of_cached_data/)**
*  **Summary:** The thread discusses the problem of Spark not respecting the distribution of cached data, and how this can lead to performance bottlenecks.
*  **Emotion:** Neutral, focusing on technical problem-solving.
*  **Top 3 Points of View:**
    *   The issue is that Spark exchanges data to read from the cache, which is surprising as it should be a narrow transformation.
    *   It's questioned why the cached repartitioned data is expected to end up on the same disk.
    *   The user seems to be encountering a bottleneck due to data exchange when reading from the cache in Spark.

**[I'm tired (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1p61zft/im_tired/)**
*  **Summary:** A user expresses feeling tired, leading to supportive comments and humorous encouragement, along with a bot posting links to open-source projects.
*  **Emotion:** The overall emotional tone is positive, with elements of humor and encouragement.
*  **Top 3 Points of View:**
    *   General support and encouragement for the user.
    *   Humorous comparison to the "conference speaker experience."
    *   Sharing of relevant open-source project resources.

**[Which is best CDC top to end pipeline? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1p6c95f/which_is_best_cdc_top_to_end_pipeline/)**
*  **Summary:** The thread explores different approaches to building Change Data Capture (CDC) pipelines, with different architectures proposed.
*  **Emotion:** The overall emotional tone is mixed, reflecting the complexity of the topic and varying opinions.
*  **Top 3 Points of View:**
    *   Using Kafka with Oracle Goldengate and Debezium to capture data, then piping it to ClickHouse.
    *   Avoiding CDC altogether and instead consuming events created by an outbox pattern.
    *   Landing data in native JSON in bronze and then pushing it to delta for silver.

**[How to control agents accessing sensitive customer data in internal databases (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1p67c7k/how_to_control_agents_accessing_sensitive/)**
*  **Summary:** This thread discusses how to control agent access to sensitive customer data in internal databases, emphasizing security and policy enforcement.
*  **Emotion:** The overall emotional tone is neutral, focusing on security and best practices.
*  **Top 3 Points of View:**
    *   Do not let agents directly access SQL; use a strict API/policy layer instead.
    *   Implement row-level access control instead of views for easier maintenance.
    *   Use an MCP (Management Control Plane) as an abstraction layer for agentic workflows.

**[How do you test? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1p5x8ah/how_do_you_test/)**
*  **Summary:** A bot posts a link to community-submitted learning resources regarding testing.
*  **Emotion:** Neutral, informational.
*  **Top 3 Points of View:**
    *   This thread only contains a bot posting a link to community resources.

**[If I cannot use InfluxDB nor TimescaleDB, is there something faster than Parquet? (e.g. stored at Amazon S3) (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1p69hz5/if_i_cannot_use_influxdb_nor_timescaledb_is_there/)**
*  **Summary:** The thread discusses alternatives to Parquet for storing time-series data in S3 when InfluxDB and TimescaleDB aren't suitable.
*  **Emotion:** Neutral, focused on finding technical solutions.
*  **Top 3 Points of View:**
    *   ClickHouse is suggested as a potential alternative.
    *   Firebolt with Iceberg on top of Parquet files might be faster.
    *   Starrocks with S3 storage is another option to consider.

**[Evaluating AWS DMS vs Estuary Flow (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p6fpt5/evaluating_aws_dms_vs_estuary_flow/)**
*  **Summary:** The thread discusses the pros and cons of AWS DMS and Estuary Flow for data integration and CDC.
*  **Emotion:** The emotional tone is neutral to slightly positive due to discussion around different products with positive and negative attributes.
*  **Top 3 Points of View:**
    *   DMS is good for one-time replication, but has issues with CDC.
    *   Estuary Flow is favored by some for its ease of use and cost model, while others dislike its UI.
    *   Debezium on MSK Connect is another viable option.

**[We wrote our first case study as a blend of technical how to and customer story on Snowflake optimization. Wdyt? (Score: 5)](https://blog.greybeam.ai/headset-snowflake-playbook/)**
*  **Summary:** Users discuss a case study on Snowflake optimization and intelligent routing.
*  **Emotion:** Neutral, focusing on sales strategy and technical challenges.
*  **Top 3 Points of View:**
    *   "Intelligent routing" is more saleable than simply telling a customer to dump the product.
    *   What was the biggest challenge with serving Snowflake data with DuckDB?
    *   Snowflake is excellent for many things, but it was never designed to affordably serve queries to over 2500 users with sporadic usage patterns.

**[Handling data quality issues that are a tiny percentage? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p6fmpt/handling_data_quality_issues_that_are_a_tiny/)**
*  **Summary:** The thread explores the challenges and impact of data quality issues, even when they affect a small percentage of the data.
*  **Emotion:** Neutral, with a slight concern about the potential impact of data quality problems.
*  **Top 3 Points of View:**
    *   It is difficult to determine the impact of errors, even if they are rare.
    *   Data quality issues should be driven down to zero.
    *   Why are those records with invalid values being inserted in the first place?

**[Is it realistic to replicate a 3000 line Oracle view in Snowflake (any suggestions would help) (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p6n53i/is_it_realistic_to_replicate_a_3000_line_oracle/)**
*  **Summary:** The discussion revolves around the feasibility of replicating a complex, 3000-line Oracle view in Snowflake.
*  **Emotion:** Neutral, leaning towards skeptical about the project's feasibility.
*  **Top 3 Points of View:**
    *   Replicating such a complex view would require a full rewrite from the base tables up.
    *   Extracting data from the view as files and copying them into Snowflake daily is a temporary workaround.
    *   Clarification is needed on the type of packages the view calls.

**[Thoughts on WhereScape RED as a DWH tool. (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p5z2rb/thoughts_on_wherescape_red_as_a_dwh_tool/)**
*  **Summary:** This thread asks for thoughts on WhereScape RED as a DWH tool.
*  **Emotion:** Neutral, leaning towards negative, as there are better alternatives.
*  **Top 3 Points of View:**
    *   It's pretty much a very old lowcode tool similar to Informatica, which lacks flexibility.
    *   Some of the principals in Coalesce.IO came from Wherescape.
    *   There are many other tools out there with better backing and features.

**[Best way to count distinct values (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p6k23x/best_way_to_count_distinct_values/)**
*  **Summary:** The thread explores different methods for efficiently counting distinct values in large datasets.
*  **Emotion:** Neutral, with a focus on technical solutions and questioning the necessity of precise counts.
*  **Top 3 Points of View:**
    *   Consider partitioning, data formats, and approximation functions.
    *   Why is the count needed?
    *   Using approx_distinct with an epsilon standard error argument.

**[Do Data Engineers Benefit from a Master’s Degree, or Is Experience Enough? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p6nt4g/do_data_engineers_benefit_from_a_masters_degree/)**
*  **Summary:** The thread explores whether a master's degree is beneficial for data engineers, or if experience is sufficient.
*  **Emotion:** Neutral, leaning towards valuing experience more than education.
*  **Top 3 Points of View:**
    *   Experience is the only metric that matters.
    *   Experience matters more.

**[Row level security in Snowflake unsecure? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p6l0ps/row_level_security_in_snowflake_unsecure/)**
*  **Summary:** The thread discusses whether row-level security in Snowflake is unsecure.
*  **Emotion:** Neutral, seeking clarification and troubleshooting.
*  **Top 3 Points of View:**
    *   The example provided proves nothing without the RLS policy code.
    *   It would be useful to include some sample rows of data.
    *   It seems like it's working as intended.
