---
title: "Data Engineering Subreddit"
date: "2025-04-18"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [You open an S3 bucket. It contains 200M objects named ‘export_final.json’…](https://i.redd.it/fxvf2n8pwlve1.png) (Score: 131)
    *   This thread discusses strategies for dealing with a large number of identically named files in an S3 bucket.
2.  [Diskless Kafka: 80% Cheaper, 100% Open](https://www.reddit.com/r/dataengineering/comments/1k21gd3/diskless_kafka_80_cheaper_100_open/) (Score: 41)
    *   This thread discusses a new approach to Kafka that eliminates the need for disks, potentially reducing costs.
3.  [Thinking of building a SaaS that scrapes data from other sources? Think twice. Read this.](https://www.reddit.com/r/dataengineering/comments/1k20v9p/thinking_of_building_a_saas_that_scrapes_data/) (Score: 31)
    *   This thread discusses the challenges and potential pitfalls of building a SaaS that relies on data scraping.
4.  [Just finished my end-to-end supply‑chain pipeline please be brutally honest!](https://www.reddit.com/r/dataengineering/comments/1k2099l/just_finished_my_endtoend_supplychain_pipeline/) (Score: 25)
    *   This thread is about feedback on an end-to-end supply chain pipeline.
5.  [We built a new open-source validation library for Polars: dataframely 🐻‍❄️](https://tech.quantco.com/blog/dataframely) (Score: 23)
    *   This thread introduces a new open-source validation library for the Polars data frame library.
6.  [[VIdeo] Freecodecamp/ Data talks club/ dltHub: Build like a senior](https://www.reddit.com/r/dataengineering/comments/1k23dh1/video_freecodecamp_data_talks_club_dlthub_build/) (Score: 19)
    *   This thread shares a video about building like a senior data engineer.
7.  [Are Data Analyst Roles Becoming Too Much Like Data Engineering?](https://www.reddit.com/r/dataengineering/comments/1k29a8t/are_data_analyst_roles_becoming_too_much_like/) (Score: 19)
    *   This thread discusses the blurring lines between data analyst and data engineering roles.
8.  [Use case for using DuckDB against a database data source?](https://www.reddit.com/r/dataengineering/comments/1k26p9z/use_case_for_using_duckdb_against_a_database_data/) (Score: 16)
    *   This thread explores use cases for using DuckDB in conjunction with existing databases.
9.  [Integration of AWS S3 Iceberg tables with Snowflake](https://www.reddit.com/r/dataengineering/comments/1k203kx/integration_of_aws_s3_iceberg_tables_with/) (Score: 10)
    *   This thread discusses the integration of AWS S3 Iceberg tables with Snowflake.
10. [xorq: open source composite data engine framework](https://www.reddit.com/r/dataengineering/comments/1k2cu9a/xorq_open_source_composite_data_engine_framework/) (Score: 4)
    *   This thread introduces xorq: open source composite data engine framework.
11. [Business analyst responsibilities on a data engineering team](https://www.reddit.com/r/dataengineering/comments/1k2b58i/business_analyst_responsibilities_on_a_data/) (Score: 3)
    *   This thread discusses the responsibilities of business analysts on a data engineering team.
12. [Current State (MySQL, SSIS, SSAS, EC2) => Cloud](https://www.reddit.com/r/dataengineering/comments/1k2dtku/current_state_mysql_ssis_ssas_ec2_cloud/) (Score: 1)
    *   This thread is about migrating current stack (MySQL, SSIS, SSAS, EC2) to the cloud.
13. [You don’t need a perfect pipeline to prove value](https://datagibberish.com/p/how-to-build-minimum-viable-data-products) (Score: 0)
    *   This thread discusses the importance of proving value with data products, even without a perfect pipeline.

# Detailed Analysis by Thread
**[You open an S3 bucket. It contains 200M objects named ‘export_final.json’… (Score: 131)](https://i.redd.it/fxvf2n8pwlve1.png)**
*   **Summary:** The thread discusses how to approach the problem of an S3 bucket containing a massive number of identically named files. Suggestions include checking file content, examining metadata, and consulting stakeholders.
*   **Emotion:** The emotional tone is mostly neutral, with a hint of negativity expressed regarding the situation.
*   **Top 3 Points of View:**
    *   Change bucket permissions to see who needs the data.
    *   Consultants would sell a time and materials contract for manual cleanup.
    *   Check file contents from different dates to determine if the data is worth examining.

**[Diskless Kafka: 80% Cheaper, 100% Open (Score: 41)](https://www.reddit.com/r/dataengineering/comments/1k21gd3/diskless_kafka_80_cheaper_100_open/)**
*   **Summary:** The thread discusses a new diskless Kafka solution and its potential benefits, including cost savings and open-source availability. Users are curious about its implementation, UX, and comparison to similar projects.
*   **Emotion:** The emotional tone is largely neutral, with some positive sentiment expressed regarding the interesting nature of the solution.
*   **Top 3 Points of View:**
    *   The solution offers good value, and users are interested in deploying it on GCP.
    *   The UX and backend handling of diskless Kafka are of interest.
    *   The solution is potentially inspired by bufstreams.

**[Thinking of building a SaaS that scrapes data from other sources? Think twice. Read this. (Score: 31)](https://www.reddit.com/r/dataengineering/comments/1k20v9p/thinking_of_building_a_saas_that_scrapes_data/)**
*   **Summary:** This thread focuses on the challenges of building a SaaS that scrapes data. It cautions readers to consider the legal risks, the fragility of the underlying data sources, and the potential for high costs.
*   **Emotion:** Predominantly positive, with users thanking the author for the informative article and finding it helpful. There's also some negative sentiment directed at the perceived spammy nature of the post.
*   **Top 3 Points of View:**
    *   Data scraping is more challenging than initially perceived, especially at scale.
    *   There are significant legal and business risks associated with relying on scraped data.
    *   Data brokers or APIs are a more reliable alternative to scraping.

**[Just finished my end-to-end supply‑chain pipeline please be brutally honest! (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1k2099l/just_finished_my_endtoend_supplychain_pipeline/)**
*   **Summary:** The thread is centered around a user seeking feedback on their completed end-to-end supply chain pipeline. Others inquire about the choices made in the architecture, such as using serverless Redshift over Athena and the data transformation process.
*   **Emotion:** The overall emotion is neutral, with users asking technical questions and offering constructive criticism.
*   **Top 3 Points of View:**
    *   Questioning the choice of serverless Redshift over Athena.
    *   Inquiring about the data transformation process between buckets and the use of DBT.
    *   Expressing admiration for the detailed setup.

**[We built a new open-source validation library for Polars: dataframely 🐻‍❄️ (Score: 23)](https://tech.quantco.com/blog/dataframely)**
*   **Summary:** A new open-source validation library for Polars called dataframely is introduced. Users inquire about its features, compare it to similar projects like patito, and discuss its capabilities for handling parameterized column names and adjusting logic based on data frequency.
*   **Emotion:** Mixed emotions with both excitement and skepticism, trending to Neutral.
*   **Top 3 Points of View:**
    *   The project seems awesome and fills a need.
    *   Questions about how it compares to similar projects like patito.
    *   Questions about handling parameterized column names and data frequency adjustments.

**[[VIdeo] Freecodecamp/ Data talks club/ dltHub: Build like a senior (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1k23dh1/video_freecodecamp_data_talks_club_dlthub_build/)**
*   **Summary:** This thread promotes a video from Freecodecamp/Data talks club/dltHub about building like a senior data engineer. One user expresses their appreciation and asks how it can be used with MCP.
*   **Emotion:** The overall tone is positive due to the appreciation expressed by a user.
*   **Top 2 Points of View:**
    *   A user loves the resource
    *   A user is wondering how to use it with MCP

**[Are Data Analyst Roles Becoming Too Much Like Data Engineering? (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1k29a8t/are_data_analyst_roles_becoming_too_much_like/)**
*   **Summary:** The discussion revolves around whether Data Analyst roles are increasingly overlapping with Data Engineering responsibilities. Various opinions are shared, with some believing that the roles are merging, while others maintain that they are still distinct.
*   **Emotion:** Mixed feelings ranging from positive to neutral, with a hint of negativity around job expectations.
*   **Top 3 Points of View:**
    *   DA roles are transitioning to DE roles.
    *   The roles are still separate, but there's a demand for more technical analysts.
    *   Having separate Engineering and Analysis teams is an organizational mistake and cost-ineffective.

**[Use case for using DuckDB against a database data source? (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1k26p9z/use_case_for_using_duckdb_against_a_database_data/)**
*   **Summary:** The thread explores potential use cases for using DuckDB in conjunction with a traditional database data source. It focuses on the benefits of DuckDB's ability to connect to multiple data sources, perform joins, and rapidly gain insights.
*   **Emotion:** Primarily neutral, with some positive sentiment.
*   **Top 3 Points of View:**
    *   DuckDB facilitates connecting to diverse data sources for rapid insights.
    *   DuckDB is used during the transformation stage.
    *   DuckDB is helpful for joining data between SQL databases and parquet files.

**[Integration of AWS S3 Iceberg tables with Snowflake (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1k203kx/integration_of_aws_s3_iceberg_tables_with/)**
*   **Summary:** Discussion centers around Snowflake's integration with AWS S3 Iceberg tables, focusing on how the race for vendor lock-in has shifted to catalogs. The new REST Catalog allows writing iceberg tables and is compared to AWS Glue.
*   **Emotion:** Predominantly Neutral.
*   **Top 2 Points of View:**
    *   The game around iceberg has switched to catalogs.
    *   REST Catalog allows writing iceberg tables.

**[xorq: open source composite data engine framework (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k2cu9a/xorq_open_source_composite_data_engine_framework/)**
*   **Summary:** Discussion about xorq: open source composite data engine framework.
*   **Emotion:** The emotional tone is neutral, expressing curiosity and questioning the production usability of the framework.
*   **Top 1 Point of View:**
    *   Expressing it's a lot of effort to avoid writing a cte with a window function because you don't have asof joins in Trino.

**[Business analyst responsibilities on a data engineering team (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k2b58i/business_analyst_responsibilities_on_a_data/)**
*   **Summary:** The thread discusses the responsibilities of business analysts on a data engineering team, touching on their role as a bridge between business requirements and engineering, and how Data Analysts are replacing them.
*   **Emotion:** The emotional tone is mostly positive and neutral.
*   **Top 3 Points of View:**
    *   BA roles are slowly going out of fashion.
    *   Non-tech roles will be targeted first when a downsizing happens.
    *   A business analyst learns the product and focuses on business requirements and business processes.

**[Current State (MySQL, SSIS, SSAS, EC2) => Cloud (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k2dtku/current_state_mysql_ssis_ssas_ec2_cloud/)**
*   **Summary:** The thread offers general advice for transitioning into data engineering and provides links to learning resources.
*   **Emotion:** Neutral.
*   **Top 2 Points of View:**
    *   Directing people to community-submitted learning resources.
    *   Pointing to the transition guide into data engineering.

**[You don’t need a perfect pipeline to prove value (Score: 0)](https://datagibberish.com/p/how-to-build-minimum-viable-data-products)**
*   **Summary:** This thread discusses the importance of proving value with data products, even without a perfect pipeline. Users discuss software engineering best practices.
*   **Emotion:** Positive
*   **Top 3 Points of View:**
    *   Sticking to software engineering best practices.
    *   Stakeholder can’t describe what they need until they see something.
    *   AI slop art. We'll never know if it's AI slop text too.
