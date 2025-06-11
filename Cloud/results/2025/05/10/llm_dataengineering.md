---
title: "Data Engineering Subreddit"
date: "2025-05-10"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Debezium without Kafka: Digging into the Debezium Server and Debezium Engine run times no one talks about](https://www.reddit.com/r/dataengineering/comments/1kita4e/debezium_without_kafka_digging_into_the_debezium/) (Score: 16)
    *   Discussion about using Debezium Server and Debezium Engine without Kafka.
2.  [I have a hive tables with 1millon rows of data and its really taking time to run join](https://www.reddit.com/r/dataengineering/comments/1kjcssq/i_have_a_hive_tables_with_1millon_rows_of_data/) (Score: 12)
    *   Users discuss reasons why a Hive table join is taking a long time and provide potential solutions.
3.  [What Platform Do You Use for Interviewing Candidates?](https://www.reddit.com/r/dataengineering/comments/1kjfl2n/what_platform_do_you_use_for_interviewing/) (Score: 10)
    *   A discussion about the platforms used for interviewing data engineering candidates and the best way to assess candidates.
4.  [How We Handle Billion-Row ClickHouse Inserts With UUID Range Bucketing](https://www.cloudquery.io/blog/how-we-handle-billion-row-clickhouse-inserts-with-uuid-range-bucketing) (Score: 8)
    *   A discussion about techniques for handling large ClickHouse inserts, specifically using UUID range bucketing.
5.  [How Do Companies Securely Store PCI and PII Data on the Cloud?](https://www.reddit.com/r/dataengineering/comments/1kj2vjq/how_do_companies_securely_store_pci_and_pii_data/) (Score: 6)
    *   A discussion about best practices for securely storing PCI and PII data in the cloud, focusing on access control, encryption, and data minimization.
6.  [Storage vs Compute : The Decoupling That Changed Cloud Warehousing (Explained with Chefs & a Pantry)](https://www.reddit.com/r/dataengineering/comments/1kisq21/storage_vs_compute_the_decoupling_that_changed/) (Score: 2)
    *   A discussion about the decoupling of storage and compute in cloud warehousing and the future of storage+compute bundling.
7.  [Looking for advise](https://www.reddit.com/r/dataengineering/comments/1kj0nuf/looking_for_advise/) (Score: 0)
    *   A user seeking advice, with responses suggesting focusing on Python and cloud technologies.
8.  [AWS Cost Optimization](https://www.reddit.com/r/dataengineering/comments/1kj499m/aws_cost_optimization/) (Score: 0)
    *   A discussion about strategies for optimizing AWS costs, including instance reservations, self-hosting services, and analyzing billing data.

# Detailed Analysis by Thread
**[Debezium without Kafka: Digging into the Debezium Server and Debezium Engine run times no one talks about (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1kita4e/debezium_without_kafka_digging_into_the_debezium/)**
*   **Summary:** Discussion about using Debezium Server and Debezium Engine without Kafka.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral.
*   **Top 3 Points of View:**
    *   Debezium engine is the only way to control the CDC engine directly, running in python with a JNI-python bridge.
    *   Debezium server can send directly to an S3 compatible destination.
    *   Delivery guarantees are at least once by default, but can be exactly once with connector configurations.

**[I have a hive tables with 1millon rows of data and its really taking time to run join (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1kjcssq/i_have_a_hive_tables_with_1millon_rows_of_data/)**
*   **Summary:** Users discuss reasons why a Hive table join is taking a long time and provide potential solutions.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral.
*   **Top 3 Points of View:**
    *   Check for a many-to-many join.
    *   The compute resource needs to be bigger.
    *   The bottleneck is either on ingestion or on the join (shuffle exchange). If it is the join, the issue is skewed keys, and the solution is to increase shuffle partitions.

**[What Platform Do You Use for Interviewing Candidates? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1kjfl2n/what_platform_do_you_use_for_interviewing/)**
*   **Summary:** A discussion about the platforms used for interviewing data engineering candidates and the best way to assess candidates.
*   **Emotion:** The thread's emotional tone is mixed, with some Neutral comments, but also Negative comments expressing frustration with current interview processes.
*   **Top 3 Points of View:**
    *   The process should focus on abstract ideas and how things work, not on syntax.
    *   Current interview processes can be terrible and dehumanizing.
    *   Interviews just need a whiteboard to discuss ideas and concepts.

**[How We Handle Billion-Row ClickHouse Inserts With UUID Range Bucketing (Score: 8)](https://www.cloudquery.io/blog/how-we-handle-billion-row-clickhouse-inserts-with-uuid-range-bucketing)**
*   **Summary:** A discussion about techniques for handling large ClickHouse inserts, specifically using UUID range bucketing.
*   **Emotion:** The overall emotional tone is Positive, with users finding the techniques and concepts useful.
*   **Top 3 Points of View:**
    *   The general techniques and concepts discussed here are good to know for anyone that works with distributed systems.
    *   Loading 20+ billion rows via parquet loading is possible.
    *   Partitioning/bucketing approaches can help in all sorts of scenarios where you need to reduce chunk size, or do horizontal scaling.

**[How Do Companies Securely Store PCI and PII Data on the Cloud? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kj2vjq/how_do_companies_securely_store_pci_and_pii_data/)**
*   **Summary:** A discussion about best practices for securely storing PCI and PII data in the cloud, focusing on access control, encryption, and data minimization.
*   **Emotion:** The emotional tone is predominantly Neutral, with users offering advice and expressing interest.
*   **Top 3 Points of View:**
    *   Apply the principle of least privilege.
    *   Keep all networking private in your VPC/VNet.
    *   Create synthetic data generators and datasets for dev/local work.

**[Storage vs Compute : The Decoupling That Changed Cloud Warehousing (Explained with Chefs & a Pantry) (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kisq21/storage_vs_compute_the_decoupling_that_changed/)**
*   **Summary:** A discussion about the decoupling of storage and compute in cloud warehousing and the future of storage+compute bundling.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral.
*   **Top 3 Points of View:**
    *   Separation of storage and computing is old news. The future is storage+compute bundling.

**[Looking for advise (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kj0nuf/looking_for_advise/)**
*   **Summary:** A user seeking advice, with responses suggesting focusing on Python and cloud technologies.
*   **Emotion:** The emotional tone of the thread is Positive, with users offering help and direction.
*   **Top 3 Points of View:**
    *   Brush up on python and cloud technologies as you start to interview.

**[AWS Cost Optimization (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kj499m/aws_cost_optimization/)**
*   **Summary:** A discussion about strategies for optimizing AWS costs, including instance reservations, self-hosting services, and analyzing billing data.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral.
*   **Top 3 Points of View:**
    *   Standard optimizations are 1y or 3y instance reservations for ec2, rds, redshift and self-hosting services like kafka-connect.
    *   ReCost.io is an S3 cost optimization tool.
    *   Automated turning off your dev environments at night is a start.
