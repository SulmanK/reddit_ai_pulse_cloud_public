---
title: "Data Engineering Subreddit"
date: "2025-09-22"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "spark", "etl"]
---

# Overall Ranking and Top Discussions
1.  [Why Don’t Data Engineers Unit Test Their Spark Jobs?](https://www.reddit.com/r/dataengineering/comments/1nnhtxt/why_dont_data_engineers_unit_test_their_spark_jobs/) (Score: 76)
    * This thread discusses why data engineers often don't unit test their Spark jobs, with various reasons ranging from time constraints and understaffing to the perceived difficulty and the nature of data transformations.
2.  [I made an open source node-based ETL repo that connects to embeddable dashboards](https://www.reddit.com/gallery/1nn7x1v) (Score: 18)
    * The discussion revolves around an open-source node-based ETL repository that connects to embeddable dashboards, focusing on its potential benefits for smaller businesses and the importance of GUI-based tools.
3.  [Design a Medallion architecture for 1TB/day of data with a 1hr SLA". How would you answer to get the job?](https://www.reddit.com/r/dataengineering/comments/1nnth0h/design_a_medallion_architecture_for_1tbday_of/) (Score: 16)
    * This thread explores how to approach a job interview question about designing a Medallion architecture for a large daily data volume with a strict SLA, questioning the practicality and necessary clarifications for such a task.
4.  [Advanced learning on AWS Redshift](https://www.reddit.com/r/dataengineering/comments/1nnt1ap/advanced_learning_on_aws_redshift/) (Score: 2)
    * This thread provides a link to community-submitted learning resources for AWS Redshift.
5.  [Data extraction - Salesforce into Excel](https://www.reddit.com/r/dataengineering/comments/1nnchyu/data_extraction_salesforce_into_excel/) (Score: 1)
    * The thread discusses different methods for extracting data from Salesforce into Excel, including using Salesforce APIs, Excel Power Query, and tools like Dataloader and Azure Data Factory.
6.  [How to convert Oracle Db queries to MySQL.](https://www.reddit.com/r/dataengineering/comments/1nnoy2g/how_to_convert_oracle_db_queries_to_mysql/) (Score: 0)
    * The thread provides recommendations for converting Oracle Db queries to MySQL.
7.  [question data conversion data mapping data migration](https://www.reddit.com/r/dataengineering/comments/1nnps2u/question_data_conversion_data_mapping_data/) (Score: 0)
    * This thread asks about how to handle XML data conversion, data mapping, and data migration.
8.  [Getting started with pipeline observability & monitoring](https://www.reddit.com/r/dataengineering/comments/1nnu2v7/getting_started_with_pipeline_observability/) (Score: 0)
    * This thread links to community-submitted learning resources for pipeline observability and monitoring.

# Detailed Analysis by Thread
**[Why Don’t Data Engineers Unit Test Their Spark Jobs? (Score: 76)](https://www.reddit.com/r/dataengineering/comments/1nnhtxt/why_dont_data_engineers_unit_test_their_spark_jobs/)**
*  **Summary:** This thread explores the reasons why data engineers often skip unit testing for their Spark jobs. The discussion points to factors such as time constraints, understaffing, the perceived difficulty of writing meaningful tests, and the nature of data transformations. Some argue that testing invariants is more practical than traditional unit tests.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   Unit testing is often skipped due to understaffing and time constraints.
    *   Writing effective unit tests for data transformations can be challenging and time-consuming.
    *   Testing invariants and using validation gates may be more practical approaches than traditional unit tests.

**[I made an open source node-based ETL repo that connects to embeddable dashboards (Score: 18)](https://www.reddit.com/gallery/1nn7x1v)**
*  **Summary:** The thread discusses an open-source, node-based ETL repository that connects to embeddable dashboards. The discussion highlights its potential value for smaller businesses due to its GUI-based approach. Suggestions are made to avoid fixed Docker requirements and to allow for different destination DB engines.
*  **Emotion:** The overall emotional tone of the thread is slightly Positive.
*  **Top 3 Points of View:**
    *   GUI-based ETL tools are particularly beneficial for smaller businesses and individual users.
    *   Avoiding fixed Docker requirements is crucial for wider adoption, especially among smaller teams.
    *   Supporting multiple destination DB engines is essential for flexibility and broader applicability.

**[Design a Medallion architecture for 1TB/day of data with a 1hr SLA". How would you answer to get the job? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1nnth0h/design_a_medallion_architecture_for_1tbday_of/)**
*  **Summary:** This thread discusses how to answer a job interview question about designing a Medallion architecture for processing 1TB of data daily with a 1-hour SLA. Participants emphasize the need to clarify the question's assumptions and requirements, such as data arrival patterns, schema details, and SLA consequences. Some suggest that the question is impractical or lacks sufficient information.
*  **Emotion:** The overall emotional tone of the thread is Neutral to slightly Negative.
*  **Top 3 Points of View:**
    *   It's crucial to clarify the specific requirements and assumptions before proposing a solution.
    *   The 1-hour SLA might be unrealistic or arbitrarily attached.
    *   Understanding the business context and consequences of missing the SLA is essential.

**[Advanced learning on AWS Redshift (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1nnt1ap/advanced_learning_on_aws_redshift/)**
*  **Summary:** This thread provides a link to a list of community-submitted learning resources for AWS Redshift.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   The thread provides a link to community-submitted learning resources for AWS Redshift.

**[Data extraction - Salesforce into Excel (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1nnchyu/data_extraction_salesforce_into_excel/)**
*  **Summary:** The thread discusses various methods for extracting data from Salesforce into Excel. Options include using the Salesforce API, Excel Power Query, Dataloader, and Azure Data Factory. The focus is on automating the data extraction process and avoiding manual data entry.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   Using Excel Power Query to connect to Salesforce Reports is an easy solution.
    *   Leveraging the Salesforce API for programmatic extraction is a flexible approach.
    *   Automating data extraction is preferred over manual data entry.

**[How to convert Oracle Db queries to MySQL. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nnoy2g/how_to_convert_oracle_db_queries_to_mysql/)**
*  **Summary:** The thread offers recommendations for converting Oracle Db queries to MySQL, suggesting tools like SQLGlot and AI models.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   SQLGlot is a recommended tool for SQL translation.
    *   AI models like Claude-4-sonnet and Gemini-2.5-pro can be used for query conversion.
    *   A pre-written prompt with examples can improve the AI's translation accuracy.

**[question data conversion data mapping data migration (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nnps2u/question_data_conversion_data_mapping_data/)**
*  **Summary:** The thread seeks advice on XML data conversion, mapping, and migration.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   Python and libraries like xmltodict or lxml can be used.

**[Getting started with pipeline observability & monitoring (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nnu2v7/getting_started_with_pipeline_observability/)**
*  **Summary:** This thread links to community-submitted learning resources for pipeline observability and monitoring.
*  **Emotion:** The overall emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   The thread provides a link to community-submitted learning resources for pipeline observability and monitoring.
