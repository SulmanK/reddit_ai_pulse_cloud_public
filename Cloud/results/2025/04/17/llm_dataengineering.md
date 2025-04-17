---
title: "Data Engineering Subreddit"
date: "2025-04-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] LLMs, ML and Observability mess](https://www.reddit.com/r/dataengineering/comments/1k1fvsy/llms_ml_and_observability_mess/) (Score: 69)
    *   Discusses the need for monitoring LLMs like any other software pipeline and recommends tools like LangSmith and Langfuse.
2.  [What are the best open-source alternatives to SQL Server, SSAS, SSIS, Power BI, and Informatica?](https://www.reddit.com/r/dataengineering/comments/1k1b8on/what_are_the_best_opensource_alternatives_to_sql/) (Score: 50)
    *   Explores open-source alternatives to the Microsoft data stack, including tools for ETL, data warehousing, and BI.
3.  [Learning Spark (book recommendations?)](https://www.reddit.com/r/dataengineering/comments/1k14jny/learning_spark_book_recommendations/) (Score: 17)
    *   Asks for book recommendations for learning Spark and suggests practical approaches like doing hands-on projects and using Databricks community edition.
4.  [Star schema implementation in Glue + Redshift.](https://www.reddit.com/r/dataengineering/comments/1k1c0cc/star_schema_implementation_in_glue_redshift/) (Score: 8)
    *   Links to community learning resources for implementing star schema.
5.  [Best storage option for high-frequency time-series data (100 Hz, multiple producers)?](https://www.reddit.com/r/dataengineering/comments/1k1etqr/best_storage_option_for_highfrequency_timeseries/) (Score: 7)
    *   Seeks advice on the best storage options for high-frequency time-series data, with suggestions including BigTable, ClickHouse, and Kafka-based stream processing.
6.  [What is Data Architecture?](https://www.veritis.com/blog/what-is-data-architecture/) (Score: 6)
    *   Discusses data architecture, with comments noting consulting insights.
7.  [A hybrid on prem and cloud based architecture?](https://www.reddit.com/r/dataengineering/comments/1k1752f/a_hybrid_on_prem_and_cloud_based_architecture/) (Score: 5)
    *   Explores hybrid on-prem and cloud-based architecture approaches, including using MinIO for sensitive storage and Trino/Presto for data virtualization.
8.  [Exploring a DAAS Business Opportunity in Geospatial Data—Where to Start?](https://www.reddit.com/r/dataengineering/comments/1k1d5st/exploring_a_daas_business_opportunity_in/) (Score: 4)
    *   Discusses exploring a DAAS business opportunity and suggests learning data engineering and finding a co-founder with tech skills.
9.  [How to run a long Python script on an Azure VM from ADF and get execution status?](https://www.reddit.com/r/dataengineering/comments/1k1f0sa/how_to_run_a_long_python_script_on_an_azure_vm/) (Score: 3)
    *   Asks about running long Python scripts on Azure VMs and suggests turning it into a durable function in Azure Functions or implementing a polling strategy.
10. [Spark for beginners](https://www.reddit.com/r/dataengineering/comments/1k1gwfy/spark_for_beginners/) (Score: 2)
    *   Gives advice for beginners with Spark, including using Pyspark with AWS Glue or Scala.
11. [error handling with sql constraints?](https://www.reddit.com/r/dataengineering/comments/1k0ztio/error_handling_with_sql_constraints/) (Score: 1)
    *   Discusses error handling with SQL constraints and suggests checking the metadata on the table and converting constraints to python before using to_sql.
12. [How do you track LLM billing across multiple platforms? Looking for team management solutions](https://www.reddit.com/r/dataengineering/comments/1k103i8/how_do_you_track_llm_billing_across_multiple/) (Score: 1)
    *   Explores how to track LLM billing across multiple platforms and recommends requesting multiple OpenAI resources in Azure.
13. [How I can switch to development role in data engineering?](https://www.reddit.com/r/dataengineering/comments/1k1k27w/how_i_can_switch_to_development_role_in_data/) (Score: 1)
    *   Expresses frustration with the retirement of DP-203 for Fabric and reluctance to recommend or use Fabric.
14. [DataPig - RIP spark](https://www.reddit.com/r/dataengineering/comments/1k16dv7/datapig_rip_spark/) (Score: 0)
    *   Shares a link to DataPig cloud, a data SaaS, with mixed reactions from users.
15. [How Dirty Is Your Data?](https://www.reddit.com/r/dataengineering/comments/1k1je39/how_dirty_is_your_data/) (Score: 0)
    *   Asks about the cleanliness of data, with users sharing their experiences and ratings.
16. [MS ACCESS, no clickbait, kinda long](https://www.reddit.com/r/dataengineering/comments/1k1l7vo/ms_access_no_clickbait_kinda_long/) (Score: 0)
    *   Suggests migrating MS Access to a .NET application with SQL Server or becoming a full-stack software engineer.
17. [Would you as data engineer appreciate to have AI writing you the ETL pipelines to take data and sink it to a target place in a step by step approach?](https://www.reddit.com/r/dataengineering/comments/1k1lfi2/would_you_as_data_engineer_appreciate_to_have_ai/) (Score: 0)
    *   Discusses the potential of AI writing ETL pipelines, with some users questioning its usefulness for experienced data engineers.

# Detailed Analysis by Thread
**[[D] LLMs, ML and Observability mess (Score: 69)](https://www.reddit.com/r/dataengineering/comments/1k1fvsy/llms_ml_and_observability_mess/)**
*  **Summary:**  The thread discusses the need for monitoring Large Language Models (LLMs) like any other software or pipeline. It recommends LangSmith and Langfuse as good places to start for monitoring agents and tracing LLM frameworks.
*  **Emotion:** The overall emotional tone is positive and neutral, reflecting helpful and informative discussion about practical tools and approaches.
*  **Top 3 Points of View:**
    *   LLMs require monitoring similar to other software pipelines.
    *   LangSmith is a good starting point for monitoring LLM agents.
    *   Langfuse can be self-hosted and configured with most LLM frameworks for tracing and observability.

**[What are the best open-source alternatives to SQL Server, SSAS, SSIS, Power BI, and Informatica? (Score: 50)](https://www.reddit.com/r/dataengineering/comments/1k1b8on/what_are_the_best_opensource_alternatives_to_sql/)**
*  **Summary:**  The discussion revolves around finding open-source alternatives to the Microsoft data stack. Users suggest various tools for ETL, data warehousing, visualization, and orchestration, including Dbt, Airflow, Dagster, Superset, Metabase, Lightdash, Postgres, and DuckDB. The thread also discusses challenges in moving away from the Microsoft stack and emphasizes the importance of a well-defined data model for vendor lock-in.
*  **Emotion:** The overall emotional tone is neutral and slightly positive, as users are providing helpful suggestions and sharing their experiences with different tools. There's a hint of negativity regarding the difficulty of replacing SSIS.
*  **Top 3 Points of View:**
    *   Dbt, Airflow, Dagster, Superset, Metabase and Lightdash are some of the open source tools that can be used for data analysis. Postgres and Duckdb are suitable for local workloads as concurrency is an issue.
    *   Moving away from the Microsoft stack is difficult, especially replacing SSIS for free.
    *   A well-defined data warehouse and business-facing data model is important to avoid vendor lock-in.

**[Learning Spark (book recommendations?) (Score: 17)](https://www.reddit.com/r/dataengineering/comments/1k14jny/learning_spark_book_recommendations/)**
*  **Summary:** The thread asks for book recommendations for learning Apache Spark. Users suggest practical approaches like hands-on projects, using Databricks community edition, and courses on Udemy. The consensus is that practical experience is more valuable than just reading books.
*  **Emotion:** The overall emotional tone is neutral to positive, with an emphasis on practical learning and encouragement for beginners.
*  **Top 3 Points of View:**
    *   Hands-on experience and practical projects are the best way to learn Spark.
    *   Databricks Community Edition is a good platform for experimentation.
    *   Courses on Udemy and resources like sparkbyexamples can be helpful.

**[Star schema implementation in Glue + Redshift. (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1k1c0cc/star_schema_implementation_in_glue_redshift/)**
*  **Summary:** The thread directs users to a community-submitted learning resource for implementing star schema in Glue + Redshift.
*  **Emotion:** The emotional tone is neutral, providing helpful learning resources.
*  **Top 3 Points of View:**
    *   Links to community learning resources.

**[Best storage option for high-frequency time-series data (100 Hz, multiple producers)? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1k1etqr/best_storage_option_for_highfrequency_timeseries/)**
*  **Summary:** The discussion centers around choosing the best storage option for high-frequency time-series data. Suggestions include BigTable, ClickHouse, and a Kafka-based stream processing solution. The importance of considering the usage patterns and querying needs is also emphasized.
*  **Emotion:** The emotional tone is mostly neutral and positive, with users offering practical advice and sharing their experiences.
*  **Top 3 Points of View:**
    *   BigQuery wouldn't be very efficient for Time Series Database. Looking at BigTable instead.
    *   Using a Kafka-based stream processing solution for high/low watermark detection
    *   ClickHouse is a good option.

**[What is Data Architecture? (Score: 6)](https://www.veritis.com/blog/what-is-data-architecture/)**
*  **Summary:** The thread discusses data architecture.
*  **Emotion:** Positive and Neutral.
*  **Top 3 Points of View:**
    * Great insights
    * Ah yes consulting

**[A hybrid on prem and cloud based architecture? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1k1752f/a_hybrid_on_prem_and_cloud_based_architecture/)**
*  **Summary:** The thread explores hybrid on-prem and cloud-based architecture approaches. Users suggest using MinIO for sensitive storage, Sentra/Cyera for data governance, and Trino/Presto for data virtualization. The importance of securing data movement and synchronization across environments is highlighted.
*  **Emotion:** The overall tone is mostly positive, with helpful suggestions. There is a negative comment on using spark for small datasets.
*  **Top 3 Points of View:**
    *   MinIO is a good option for sensitive storage on-prem.
    *   Data virtualization layers like Trino/Presto can create a unified access across hybrid environments.
    *   Spark and Databricks should not be used if data volume is not large.

**[Exploring a DAAS Business Opportunity in Geospatial Data—Where to Start? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k1d5st/exploring_a_daas_business_opportunity_in/)**
*  **Summary:** The thread is about exploring a DAAS business opportunity in geospatial data. Suggestions include learning data engineering and seeking a co-founder with technical skills.
*  **Emotion:** The overall tone is positive and encouraging.
*  **Top 3 Points of View:**
    *   For the data aspects, consider learning data engineering.
    *   Find a co-founder or learn some tech skills on your own.
    *   Local Data Stack and George Heiler post may be valuable.

**[How to run a long Python script on an Azure VM from ADF and get execution status? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k1f0sa/how_to_run_a_long_python_script_on_an_azure_vm/)**
*  **Summary:** This thread discusses how to run long Python scripts on Azure VMs from ADF and get execution status.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   Turn it into a durable function in Azure Functions or implement your own polling strategy.

**[Spark for beginners (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k1gwfy/spark_for_beginners/)**
*  **Summary:** The thread offers advice for beginners learning Spark. Suggestions include using Pyspark with AWS Glue or Scala.
*  **Emotion:** The overall emotional tone is neutral and helpful.
*  **Top 3 Points of View:**
    *   If you already have experience working in AWS you can try glue with Pyspark but if you want to be unique go for Scala.
    *   If you like python go with pyspark, if you prefer scala use scala.
    *   Run Spark locally with standalone downloads with Hadoop preconfigured to avoid cloud costs.

**[error handling with sql constraints? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k0ztio/error_handling_with_sql_constraints/)**
*  **Summary:** The thread discusses error handling with SQL constraints.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Check the metadata on the table to get all of the constraints first then convert these constraints to python and do the data checking against the pandas data frame before using to_sql.

**[How do you track LLM billing across multiple platforms? Looking for team management solutions (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k103i8/how_do_you_track_llm_billing_across_multiple/)**
*  **Summary:** The thread explores tracking LLM billing and suggests requesting multiple OpenAI resources in Azure.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   The company requested multiple OpenAI resources in azure to track costs.

**[How I can switch to development role in data engineering? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k1k27w/how_i_can_switch_to_development_role_in_data/)**
*  **Summary:** The thread expresses frustration with the retirement of DP-203 for Fabric.
*  **Emotion:** Negative.
*  **Top 3 Points of View:**
    *   i hate that they retired dp-203 for fabric. i don't want to recommend fabric to anyone nor use it.

**[DataPig - RIP spark (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k16dv7/datapig_rip_spark/)**
*  **Summary:** Shares a link to DataPig cloud, a data SaaS, with mixed reactions from users.
*  **Emotion:** Neutral to positive.
*  **Top 3 Points of View:**
    *   Just another data SaaS with many promises but no technical info about what it is and how it works. Just have a demo.

**[How Dirty Is Your Data? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k1je39/how_dirty_is_your_data/)**
*  **Summary:** Asks about the cleanliness of data, with users sharing their experiences and ratings.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   All clients have data in excel. Cant get any dirtier than these dirt bags.
    *   We have datalake house medallion architecture. And so for each layer i would rate -10 😂😂😂. We are in the process of cleaning.
    *   Red flags all the way down.

**[MS ACCESS, no clickbait, kinda long (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k1l7vo/ms_access_no_clickbait_kinda_long/)**
*  **Summary:** The thread suggests migrating MS Access to a .NET application with SQL Server or becoming a full-stack software engineer.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Typically that would be a .NET application with SQL Server backed.
    *   Sounds like this monstrosity should’ve become a full-stack custom software app a long time ago, but probably didn’t.
    *   Links to community learning resources.

**[Would you as data engineer appreciate to have AI writing you the ETL pipelines to take data and sink it to a target place in a step by step approach? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k1lfi2/would_you_as_data_engineer_appreciate_to_have_ai/)**
*  **Summary:** Discusses the potential of AI writing ETL pipelines, with some users questioning its usefulness for experienced data engineers.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   This tool might reduce the cost to write but it's not helpful for a small team like ours.
    *   Why would a data engineer need natural language AI tools to do the things we can do in our sleep?
