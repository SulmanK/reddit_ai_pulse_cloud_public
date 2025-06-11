---
title: "Data Engineering Subreddit"
date: "2025-05-15"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Is it really necessary to ingest all raw data into the bronze layer?](https://www.reddit.com/r/dataengineering/comments/1kmq1ew/is_it_really_necessary_to_ingest_all_raw_data/) (Score: 145)
    * Discusses the necessity of ingesting all raw data into the bronze layer for future-proofing and problem diagnosis.
2.  [Perhaps the best transition: DS > DE](https://www.reddit.com/r/dataengineering/comments/1kn2cgq/perhaps_the_best_transition_ds_de/) (Score: 43)
    * Discusses the transition from Data Science to Data Engineering, including its benefits and impact on earnings.
3.  [Help me solve a classic DE problem](https://i.redd.it/qg1g6l7zkv0f1.jpeg) (Score: 18)
    * Seeks advice on extracting fields from JSON data, especially in the context of Amazon's financial events data.
4.  [Query slow on x2idn.16xlarge EC2 – 10min On-Prem Job Takes 6 Hours in AWS](https://www.reddit.com/r/dataengineering/comments/1kn12s8/query_slow_on_x2idn16xlarge_ec2_10min_onprem_job/) (Score: 9)
    * Troubleshoots a slow query performance issue on AWS compared to on-premise, focusing on storage and configuration.
5.  [Is there a book to teach you data engineering by examples or use cases?](https://www.reddit.com/r/dataengineering/comments/1knh5ex/is_there_a_book_to_teach_you_data_engineering_by/) (Score: 9)
    * Asks about books that teach data engineering through examples or use cases.
6.  [Anyone using a object storage for DE/DS other than the big 3](https://www.reddit.com/r/dataengineering/comments/1kn36yk/anyone_using_a_object_storage_for_deds_other_than/) (Score: 6)
    * Inquires about object storage solutions for Data Engineering and Data Science beyond the major cloud providers.
7.  [Too early to change jobs?](https://www.reddit.com/r/dataengineering/comments/1kn6f9x/too_early_to_change_jobs/) (Score: 5)
    * Asks whether it's too early to change jobs due to a dysfunctional work environment and unclear role.
8.  [Best practices for Kafka partitions?](https://www.reddit.com/r/dataengineering/comments/1kmttx5/best_practices_for_kafka_partitions/) (Score: 3)
    * Asks for best practices for Kafka partitions.
9.  [Is what I’m (thinking) of building actually useful?](https://www.reddit.com/r/dataengineering/comments/1kndvqd/is_what_im_thinking_of_building_actually_useful/) (Score: 3)
    * Asks about the usefulness of building an internal documentation tool.
10. [What tool is used to generate diagrams like this one](https://www.reddit.com/r/dataengineering/comments/1kmxtwz/what_tool_is_used_to_generate_diagrams_like_this/) (Score: 2)
    * Asks about the usefulness of building an internal documentation tool.
11. [Parquet doesn’t seem to support parallel reads?](https://www.reddit.com/r/dataengineering/comments/1knfpan/parquet_doesnt_seem_to_support_parallel_reads/) (Score: 1)
    * Asks about the usefulness of building an internal documentation tool.

# Detailed Analysis by Thread
**[Is it really necessary to ingest all raw data into the bronze layer? (Score: 145)](https://www.reddit.com/r/dataengineering/comments/1kmq1ew/is_it_really_necessary_to_ingest_all_raw_data/)**
*   **Summary:**  The thread discusses the pros and cons of ingesting all raw data into a bronze layer in data engineering pipelines.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Ingesting all raw data provides future-proofing and allows for easier debugging of data issues.
    *   Storing raw data acts as a cache, allowing for easier rebuilding or rollback of data layers without hitting source APIs repeatedly.
    *   Automated changes to schemas can break queries, exports and BI / analytic applications.

**[Perhaps the best transition: DS > DE (Score: 43)](https://www.reddit.com/r/dataengineering/comments/1kn2cgq/perhaps_the_best_transition_ds_de/)**
*   **Summary:** The thread discusses the transition from Data Science to Data Engineering, with users sharing their experiences, reasons for switching, and advice for others considering the move.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Data Engineering provides a sense of "solidity" and control over data, while Data Science can be frustrating due to client disagreements.
    *   Switching to Data Engineering can lead to better career prospects and easier promotions compared to Data Science.
    *   A CS background may not be necessary for transitioning into DE.

**[Help me solve a classic DE problem (Score: 18)](https://i.redd.it/qg1g6l7zkv0f1.jpeg)**
*   **Summary:** The thread discusses approaches to handling complex, unstructured JSON data, specifically from Amazon's financial events API.
*   **Emotion:** The overall emotional tone is neutral, with touches of positive sentiments from those offering solutions.
*   **Top 3 Points of View:**
    *   Use tools like dltHub to handle schema evolution for unstructured JSON files.
    *   Leverage ChatGPT to dynamically extract fields from the JSON data.
    *   Detect schema patterns based on keys (e.g., ShipmentEventList) and process events separately based on their type.

**[Query slow on x2idn.16xlarge EC2 – 10min On-Prem Job Takes 6 Hours in AWS (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1kn12s8/query_slow_on_x2idn16xlarge_ec2_10min_onprem_job/)**
*   **Summary:** The thread discusses why a query that runs quickly on-premise takes significantly longer on AWS, focusing on potential bottlenecks like storage configuration and instance size.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The target RDS r6i.2xlarge has a limitation of 312 MB sec throughput
    *   The performance of the EBS volume is the problem
    *   Target instance is undersized.

**[Is there a book to teach you data engineering by examples or use cases? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1knh5ex/is_there_a_book_to_teach_you_data_engineering_by/)**
*   **Summary:** A user asks for recommendations for books that teach data engineering through practical examples and use cases. The main response is a bot pointing to a community-maintained list of learning resources.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    * N/A (Only bot response)

**[Anyone using a object storage for DE/DS other than the big 3 (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kn36yk/anyone_using_a_object_storage_for_deds_other_than/)**
*   **Summary:** Users discuss alternatives to the major cloud providers (AWS, Azure, GCP) for object storage in data engineering and data science contexts.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Network cost is expensive, if you use services outside your deployment
    *   MinIO can be used for prototypes
    *   Anything else will normally be S3-compatible

**[Too early to change jobs? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kn6f9x/too_early_to_change_jobs/)**
*   **Summary:** The poster is considering leaving a new job due to a dysfunctional team and an unclear role that combines data engineering and product ownership. Advice focuses on strategies for navigating the situation.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Focus on DE, and really understanding the setup, capabilities, and limitations of what you've got.
    *   Is there any way you can focus on either the DE or PO aspects of your role while you are learning?
    * N/A (Only bot response)

**[Best practices for Kafka partitions? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kmttx5/best_practices_for_kafka_partitions/)**
*   **Summary:** The poster is asking about best practices for Kafka partitions.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Switching to use the customer ID
    *   You can mitigate this to some extent by using more partitions

**[Is what I’m (thinking) of building actually useful? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kndvqd/is_what_im_thinking_of_building_actually_useful/)**
*   **Summary:** The poster is asking about the usefulness of building an internal documentation tool.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The idea Sounds like Databricks' Unity Catalog
    *   You just clone our DevOps wiki as a git repo and search it via Vs code
    *   Sounds like a liability and an endless headache. Why don’t you just make a wiki, ask people to contribute and go from there?

**[What tool is used to generate diagrams like this one (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kmxtwz/what_tool_is_used_to_generate_diagrams_like_this/)**
*   **Summary:** The poster is asking about what tool is used to generate diagrams.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   draw.io aka diagrams.net
    *   Excalidraw

**[Parquet doesn’t seem to support parallel reads? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1knfpan/parquet_doesnt_seem_to_support_parallel_reads/)**
*   **Summary:** The poster is asking about if Parquet supports parallel reads.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    * N/A (Only bot response)
