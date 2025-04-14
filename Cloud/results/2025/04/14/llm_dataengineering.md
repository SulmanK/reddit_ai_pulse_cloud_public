---
title: "Data Engineering Subreddit"
date: "2025-04-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data", "engineering", "trends"]
---

# Overall Ranking and Top Discussions
1.  [ [video] What is Iceberg, and why is everyone talking about it?](https://www.youtube.com/watch?v=TsmhRZElPvM) (Score: 34)
    *   Discussing the history and adoption of Iceberg, a table format, including its origins at Netflix and its benefits for separating storage and compute.
2.  [Event Sourcing as a creative tool for developers](https://www.reddit.com/r/dataengineering/comments/1jyve41/event_sourcing_as_a_creative_tool_for_developers/) (Score: 12)
    *   Exploring the use of event sourcing as a method for data storage and manipulation, emphasizing its flexibility and adaptability to changing business needs.
3.  [ETL for Ingesting S3 files and converting to Iceberg](https://www.reddit.com/r/dataengineering/comments/1jyxdlb/etl_for_ingesting_s3_files_and_converting_to/) (Score: 8)
    *   Seeking advice on ETL processes for ingesting S3 files and converting them to Iceberg format, with suggestions including DynamoDB, Athena, and Glue.
4.  [Meta IC5 Team Matching and Offer Question](https://www.reddit.com/r/dataengineering/comments/1jz36d2/meta_ic5_team_matching_and_offer_question/) (Score: 5)
    *   A user asks for help with Meta IC5 team matching and offers.
5.  [Communication issue](https://www.reddit.com/r/dataengineering/comments/1jz4phr/communication_issue/) (Score: 4)
    *   A user seeks advice on dealing with a communication issue, with suggestions including exploring anxiety and learning how to use AI.
6.  [How do I document existing Pipelines?](https://www.reddit.com/r/dataengineering/comments/1jz0zet/how_do_i_document_existing_pipelines/) (Score: 3)
    *   Looking for recommendations on how to document existing pipelines, with suggestions including using an AI crawler and summarizing inputs, outputs, and operational considerations.
7.  [Databricks Pain Points?](https://www.reddit.com/r/dataengineering/comments/1jz6bu9/databricks_pain_points/) (Score: 2)
    *   A user asks about Databricks pain points, and the response suggests using dbt.
8.  [Can someone help me with this Oozie error?](https://i.redd.it/pckpeuxr4uue1.png) (Score: 1)
    *   Requesting help with an Oozie error, likely related to Kerberos configuration, but lacking sufficient information for a definitive diagnosis.
9.  [Recommendations for a new grad](https://www.reddit.com/r/dataengineering/comments/1jz026m/recommendations_for_a_new_grad/) (Score: 1)
    *   Seeking recommendations for a new grad, with suggestions including building a project and utilizing community learning resources.
10. [Databricks geographic coding on the cheap?](https://www.reddit.com/r/dataengineering/comments/1jz0clz/databricks_geographic_coding_on_the_cheap/) (Score: 1)
    *   Looking for recommendations on Databricks geographic coding on the cheap, with suggestions including using H3 on databricks.
11. [Any success story from Microsoft Feature Stores?](https://www.reddit.com/r/dataengineering/comments/1jz3810/any_success_story_from_microsoft_feature_stores/) (Score: 1)
    *   Asks if there are any success stories from Microsoft Feature Stores.
12. [doubt](https://www.reddit.com/r/dataengineering/comments/1jz3ls4/doubt/) (Score: 1)
    *   A user asks about which Data Engineer certification to pick.
13. [Files to be processed in sequence on S3 bucket.](https://www.reddit.com/r/dataengineering/comments/1jz3m2a/files_to_be_processed_in_sequence_on_s3_bucket/) (Score: 1)
    *   Asking how to process files in sequence on an S3 bucket, with suggestions including including date and time in the filename.
14. [Meta Data Engineering Full Stack coming up.](https://www.reddit.com/r/dataengineering/comments/1jz6yr0/meta_data_engineering_full_stack_coming_up/) (Score: 1)
    *   The discussion refers a list of learning resources.
15. [How do you improve Data Quality?](https://www.reddit.com/r/dataengineering/comments/1jyx7at/how_do_you_improve_data_quality/) (Score: 0)
    *   Discussing methods for improving data quality, including testing, feedback loops with data consumers, and applying SRE methodologies.
16. [NoSQL Database for Ticketing System](https://www.reddit.com/r/dataengineering/comments/1jz4fsw/nosql_database_for_ticketing_system/) (Score: 0)
    *   Seeking recommendations for a NoSQL database for a ticketing system, with suggestions including MongoDB, Redis, Cassandra, and Elasticsearch.
17. [How to install apache sparks](https://www.reddit.com/r/dataengineering/comments/1jz4qdr/how_to_install_apache_sparks/) (Score: 0)
    *   Asking how to install apache sparks, with suggestions including registering for community cluster on databricks.

# Detailed Analysis by Thread
**[[video] What is Iceberg, and why is everyone talking about it? (Score: 34)](https://www.youtube.com/watch?v=TsmhRZElPvM)**
*   **Summary:** Discussion about the history, benefits, and adoption of the Iceberg table format, particularly its development at Netflix for separating storage and compute on S3.
*   **Emotion:** The emotional tone of the thread is largely Neutral.
*   **Top 3 Points of View:**
    *   Netflix built Iceberg to address the challenges of storing unstructured data and to separate storage and compute.
    *   Iceberg adoption is driven by its ability to optimize storage and handle S3 eventual consistency.
    *   Iceberg provides a quick and nice summary for data.

**[Event Sourcing as a creative tool for developers (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1jyve41/event_sourcing_as_a_creative_tool_for_developers/)**
*   **Summary:** Exploring event sourcing as a method where data is stored in its raw form and data structures are derived from it. This allows for flexible data adaptation without migrations or ETL pipelines.
*   **Emotion:** The emotional tone of the thread is mostly Neutral, with a slight positive sentiment.
*   **Top 3 Points of View:**
    *   Event sourcing allows for easy data reshaping and adaptation to changing business needs.
    *   Raw event streams often lack semantic meaning and contextual intent, which can be a limitation.
    *   Adopting event sourcing requires support from legacy systems.

**[ETL for Ingesting S3 files and converting to Iceberg (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1jyxdlb/etl_for_ingesting_s3_files_and_converting_to/)**
*   **Summary:** Seeking advice on ETL processes for ingesting S3 files and converting them to Iceberg.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Use DynamoDB for file tracking in short intervals, along with Iceberg for version control.
    *   Utilize Athena to transform Parquet files to Iceberg and schedule the query with an orchestration tool.
    *   Glue can keep track of processed files with its bookmarks feature.

**[Meta IC5 Team Matching and Offer Question (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1jz36d2/meta_ic5_team_matching_and_offer_question/)**
*   **Summary:** A user asks for advice on team matching and offer-related questions for a Meta IC5 position.
*   **Emotion:** The emotional tone of the thread is Negative.
*   **Top 3 Points of View:**
    *   Another user requested to DM the original poster to ask about interview experience.

**[Communication issue (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1jz4phr/communication_issue/)**
*   **Summary:** A user is experiencing a communication issue and is looking for advice.
*   **Emotion:** The emotional tone of the thread is a mix of Neutral and Positive.
*   **Top 3 Points of View:**
    *   Explore anxiety and its potential impact on communication.
    *   Learn how to use AI to improve communication.
    *   Read books and engage in online discussions to improve communication skills.

**[How do I document existing Pipelines? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jz0zet/how_do_i_document_existing_pipelines/)**
*   **Summary:** This thread is about documenting existing pipelines.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Use an AI crawler to document the pipelines.
    *   Provide a brief summary of what the pipeline does, including input, output, and operational considerations.

**[Databricks Pain Points? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jz6bu9/databricks_pain_points/)**
*   **Summary:** A user inquires about the pain points of using Databricks.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Suggests using dbt (data build tool).

**[Can someone help me with this Oozie error? (Score: 1)](https://i.redd.it/pckpeuxr4uue1.png)**
*   **Summary:** A user is asking for help with an Oozie error.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   The error might be related to Kerberos authentication, specifically a missing kinit.

**[Recommendations for a new grad (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz026m/recommendations_for_a_new_grad/)**
*   **Summary:** The discussion provides advice for a new grad entering the field.
*   **Emotion:** The emotional tone of the thread is mixed, with both Neutral and Negative sentiments.
*   **Top 3 Points of View:**
    *   Provide list of community submitted learning resources.
    *   Build something to demonstrate knowledge and skills.
    *   Someone was called an "***".

**[Databricks geographic coding on the cheap? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz0clz/databricks_geographic_coding_on_the_cheap/)**
*   **Summary:** Seeking advice on cost-effective geographic coding in Databricks.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Suggests using H3 geospatial functions on Databricks.

**[Any success story from Microsoft Feature Stores? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz3810/any_success_story_from_microsoft_feature_stores/)**
*   **Summary:** A user asks about success stories from Microsoft Feature Stores.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Someone questions how the question relates to the data engineering group.

**[doubt (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz3ls4/doubt/)**
*   **Summary:** Asks about which Data Engineer certification to pick.
*   **Emotion:** The emotional tone of the thread is mixed, with Neutral and Positive sentiments.
*   **Top 3 Points of View:**
    *   Pick the one that fits your strengths.
    *   The Data Engineer Professional cert teaches you how to build full, real-world data systems.
    *   Take the AWS Punctuation Engineering course.

**[Files to be processed in sequence on S3 bucket. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz3m2a/files_to_be_processed_in_sequence_on_s3_bucket/)**
*   **Summary:** Asking how to process files in sequence on an S3 bucket.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Ask the people who export the files to include both the date and time in the file name.
    *   Use a simple python script, if this is going to be executed once.

**[Meta Data Engineering Full Stack coming up. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jz6yr0/meta_data_engineering_full_stack_coming_up/)**
*   **Summary:** Discussion provides link to community-submitted learning resources.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Provides link to learning resources.

**[How do you improve Data Quality? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jyx7at/how_do_you_improve_data_quality/)**
*   **Summary:** Discussing methods for improving data quality.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Different data sets and problems require different methods.
    *   Data engineers can address technical data quality, while functional data quality requires a feedback loop with data consumers.
    *   Treat data quality like a software problem and apply the google SRE methodologies.

**[NoSQL Database for Ticketing System (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jz4fsw/nosql_database_for_ticketing_system/)**
*   **Summary:** Seeking recommendations for a NoSQL database for a ticketing system.
*   **Emotion:** The emotional tone of the thread is mixed, with both Neutral and Positive sentiments.
*   **Top 3 Points of View:**
    *   MongoDB is a good choice.
    *   MongoDB, Redis, Cassandra and Elasticsearch are good choices for booking data.
    *   Cassandra and DynamoDB require a deeper understanding of data modeling.

**[How to install apache sparks (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jz4qdr/how_to_install_apache_sparks/)**
*   **Summary:** Asking how to install Apache Spark.
*   **Emotion:** The emotional tone of the thread is mixed, with both Neutral and Positive sentiments.
*   **Top 3 Points of View:**
    *   Register for community cluster on databricks it’s free.
