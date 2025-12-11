---
title: "Data Engineering Subreddit"
date: "2025-10-11"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "big data", "cloud computing"]
---

# Overall Ranking and Top Discussions
1.  [What makes BigQuery “big“?](https://i.redd.it/dstpgghwqhuf1.jpeg) (Score: 275)
    *   The discussion revolves around the factors contributing to BigQuery's perceived "bigness," with users debating whether it's due to its capabilities, cost, or underlying architecture.
2.  [Small data engineering firms](https://www.reddit.com/r/dataengineering/comments/1o3lepw/small_data_engineering_firms/) (Score: 9)
    *   Users share insights and strategies employed by small data engineering firms, focusing on cloud-native architectures, scalability solutions, and talent management.
3.  [Polars read database and write database bottleneck](https://www.reddit.com/r/dataengineering/comments/1o3yz5o/polars_read_database_and_write_database_bottleneck/) (Score: 6)
    *   The thread discusses potential bottlenecks when using Polars to read from and write to databases, with suggestions for optimization and alternative tools.
4.  [Write to Fabric warehouse from Fabric Notebook](https://www.reddit.com/r/dataengineering/comments/1o3tb9l/write_to_fabric_warehouse_from_fabric_notebook/) (Score: 5)
    *   The conversation centers around challenges faced while writing to a Fabric warehouse from a Fabric notebook, with potential solutions involving permissions, managed identities, and alternative approaches using Lakehouse.
5.  [Is ProjectPro worth it to expand the stack and portfolio projects?](https://www.reddit.com/r/dataengineering/comments/1o3gani/is_projectpro_worth_it_to_expand_the_stack_and/) (Score: 3)
    *   This thread is about whether ProjectPro is worth it to expand the stack and portfolio projects.
6.  [Can I really become a data engineer without a CS degree or experience?](https://www.reddit.com/r/dataengineering/comments/1o447qa/can_i_really_become_a_data_engineer_without_a_cs/) (Score: 3)
    *   Users share their experiences and insights on transitioning into data engineering without a traditional computer science background, highlighting essential skills and potential career paths.
7.  [GUID or URN for business key](https://www.reddit.com/r/dataengineering/comments/1o3ccsr/guid_or_urn_for_business_key/) (Score: 1)
    *   The thread discusses the use of GUIDs versus URNs for business keys in data lakes or warehouses, with a preference for GUIDs to accommodate future system migrations.
8.  [Best tool to display tasks like Jira cards?](https://i.redd.it/lgiqf4ededuf1.jpeg) (Score: 0)
    *   The discussion revolves around finding the best tool to display tasks in a format similar to Jira cards, with suggestions including Jira itself, Power BI, and simpler solutions like Excel or custom HTML.
9.  [Need advice on designing a scalable vector pipeline for an AI chatbot (API-only data ~100GB JSON + PDFs)](https://www.reddit.com/r/dataengineering/comments/1o3otpf/need_advice_on_designing_a_scalable_vector/) (Score: 0)
    *   The thread seeks advice on designing a scalable vector pipeline for an AI chatbot, with a focus on metadata stores, content hashing, and workflow management.
10. [Can data engineers really work remotely from another country?](https://www.reddit.com/r/dataengineering/comments/1o43kba/can_data_engineers_really_work_remotely_from/) (Score: 0)
    *   The discussion explores the feasibility of data engineers working remotely from another country, considering factors like company policies, data regulations, and potential constraints.
11. [What should I specialize in as a data engineer learner?](https://www.reddit.com/r/dataengineering/comments/1o43tyt/what_should_i_specialize_in_as_a_data_engineer/) (Score: 0)
    *   The conversation offers guidance on specialization paths for aspiring data engineers, emphasizing the importance of SQL, pipelines, cloud, and emerging areas like big data or ML engineering.

# Detailed Analysis by Thread
**[What makes BigQuery “big“? (Score: 275)](https://i.redd.it/dstpgghwqhuf1.jpeg)**
*  **Summary:** The thread explores the reasons behind BigQuery's reputation, with contributors debating whether its size, cost, or underlying architecture contributes to its "bigness." Some users highlight the potential for high query costs if not properly optimized, while others argue that BigQuery can be cost-effective with appropriate partitioning and query design. The origin of the "Big" in BigQuery is also speculated upon, with some suggesting it's derived from Google's BigTable.
*  **Emotion:** The overall emotional tone is Neutral, with users presenting various perspectives and experiences regarding BigQuery's capabilities and costs.
*  **Top 3 Points of View:**
    *   BigQuery's high query costs are a major factor in its "bigness."
    *   BigQuery can be cost-effective if used correctly with proper optimization techniques.
    *   The "Big" in BigQuery likely refers to Google's BigTable distributed database.

**[Small data engineering firms (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1o3lepw/small_data_engineering_firms/)**
*  **Summary:**  The discussion centers around the strategies and tools utilized by small data engineering firms. Key themes include leveraging cloud-native architectures like serverless and containerization for flexibility, utilizing tools such as Airbyte, Prefect, and Airflow for data pipelines and orchestration, and addressing the challenges of scalability and talent management in small teams.
*  **Emotion:** The overall emotional tone is Neutral, with a mix of practical advice and experience sharing. Some comments lean towards Positive when describing successful patterns and tools.
*  **Top 3 Points of View:**
    *   Cloud-native architectures and containerization are essential for small teams.
    *   Tools like Airbyte, Prefect, and Airflow help manage data pipelines and scalability.
    *   Cross-training and talent management are crucial for handling workload variation.

**[Polars read database and write database bottleneck (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1o3yz5o/polars_read_database_and_write_database_bottleneck/)**
*  **Summary:** The thread discusses the challenges related to read and write performance when using Polars with databases. Users suggest potential solutions such as using Polars with ConnectorX for parallel data retrieval and mention the potential of turbodbc for improved performance, while also acknowledging its setup complexity.
*  **Emotion:** The overall emotional tone is Neutral. Users are primarily focused on providing technical advice and solutions to the performance bottleneck issue.
*  **Top 3 Points of View:**
    *   Polars alone may not significantly improve database operation speed.
    *   Using Polars with ConnectorX and specifying partition columns can speed up data retrieval through parallel connections.
    *   turbodbc can offer performance improvements but is difficult to set up.

**[Write to Fabric warehouse from Fabric Notebook (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1o3tb9l/write_to_fabric_warehouse_from_fabric_notebook/)**
*  **Summary:** The discussion revolves around the problem of writing data from a Fabric Notebook to a Fabric Warehouse, specifically encountering HTTP authentication errors. Suggestions include checking and granting explicit permissions to the managed identity (MI/SP), verifying Fabric tenant settings, and exploring alternative approaches like using a Lakehouse and triggering notebooks via pipelines.
*  **Emotion:** The overall emotional tone is Neutral, as users are trying to troubleshoot a technical problem and offer potential solutions.
*  **Top 3 Points of View:**
    *   Ensure the managed identity has the necessary permissions on the Fabric Warehouse and relevant workspaces.
    *   Consider using a Lakehouse instead of a Warehouse, as they are natively related to Spark Notebooks.
    *   Verify the ADF account is designated as a service principal and has the correct scopes granted.

**[Is ProjectPro worth it to expand the stack and portfolio projects? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o3gani/is_projectpro_worth_it_to_expand_the_stack_and/)**
*  **Summary:** The conversation is about whether or not ProjectPro is worth the cost of expanding a stack and portfolio projects. A bot shares a link to learning resources.
*  **Emotion:** The overall emotional tone is Neutral, as it is a simple question and the only answer is a link to resources.
*  **Top 3 Points of View:**
    *   A bot shares a link to learning resources.

**[Can I really become a data engineer without a CS degree or experience? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1o447qa/can_i_really_become_a_data_engineer_without_a_cs/)**
*  **Summary:** The thread explores the possibility of becoming a data engineer without a computer science degree or extensive experience. Contributors share personal experiences and provide guidance on essential skills, potential career paths, and the feasibility of working in different types of organizations.
*  **Emotion:** The overall emotional tone is Neutral, with users offering realistic perspectives and encouraging advice to those without traditional backgrounds.
*  **Top 3 Points of View:**
    *   A CS degree is not strictly necessary, but a strong grasp of essential skills like SQL and data modeling is crucial.
    *   Entry into FAANG companies might be difficult without a CS background, but opportunities exist in government or manufacturing.
    *   Curiosity, a willingness to learn, and putting in effort are key to acquiring new skills and succeeding as a data engineer.

**[GUID or URN for business key (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1o3ccsr/guid_or_urn_for_business_key/)**
*  **Summary:** The discussion focuses on choosing between GUIDs and URNs for business keys within a data lake or warehouse context. The recommended approach is to use GUIDs for both tables and link them with foreign key constraints or mapping tables to accommodate potential future migrations to different identification schemes.
*  **Emotion:** The overall emotional tone is Neutral, presenting a technical recommendation with a rationale based on adaptability and future-proofing.
*  **Top 3 Points of View:**
    *   GUIDs should be generated for both tables.
    *   Link tables using foreign key constraints or mapping tables.
    *   GUIDs are better for adaptability to new identification schemes.

**[Best tool to display tasks like Jira cards? (Score: 0)](https://i.redd.it/lgiqf4ededuf1.jpeg)**
*  **Summary:** The thread explores various tools that can be used to display tasks in a similar format to Jira cards. Suggestions range from using Jira itself to employing Power BI, Excel, or custom HTML solutions, depending on the specific requirements and resources available. The discussion also touches upon the potential complexity of using multiple task trackers.
*  **Emotion:** The overall emotional tone is Neutral, with users offering different suggestions based on varying needs and technical capabilities.
*  **Top 3 Points of View:**
    *   Jira is the most straightforward solution if it's already in use.
    *   Power BI can provide visually appealing dashboards and reporting capabilities.
    *   Excel or custom HTML solutions can be sufficient for simple, internal task displays.

**[Need advice on designing a scalable vector pipeline for an AI chatbot (API-only data ~100GB JSON + PDFs) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o3otpf/need_advice_on_designing_a_scalable_vector/)**
*  **Summary:** The thread seeks advice on designing a scalable vector pipeline for an AI chatbot. The recommended approach involves setting up a metadata store, utilizing content hashes to avoid full re-ingestion, and tracking various metadata fields. DynamoDB or Postgres are suggested for the metadata store, Temporal for workflow management, and Qdrant for vector storage.
*  **Emotion:** The overall emotional tone is Neutral, focusing on providing technical recommendations and best practices for designing a scalable data pipeline.
*  **Top 3 Points of View:**
    *   Set up a metadata store and use content hashes for efficient updates.
    *   Use DynamoDB or Postgres for metadata storage, Temporal for workflow management, and Qdrant for vector storage.
    *   Index payload fields in Qdrant and retire old vectors to manage updates.

**[Can data engineers really work remotely from another country? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o43kba/can_data_engineers_really_work_remotely_from/)**
*  **Summary:** The thread discusses the feasibility of data engineers working remotely from another country. Contributors highlight that it's generally possible unless restricted by data regulations, company policies, or territorial constraints. They also mention the increasing prevalence of distributed teams and the importance of considering tax and labor laws.
*  **Emotion:** The overall emotional tone is Neutral, with users providing realistic perspectives and addressing the various factors that can impact remote work arrangements.
*  **Top 3 Points of View:**
    *   Remote work is generally possible unless restricted by data regulations or company policies.
    *   Companies with distributed teams are more likely to support remote work from other countries.
    *   Tax and labor laws are significant considerations for companies allowing remote work from abroad.

**[What should I specialize in as a data engineer learner? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o43tyt/what_should_i_specialize_in_as_a_data_engineer/)**
*  **Summary:** The discussion centers around recommendations for specialization paths for aspiring data engineers. Common suggestions include focusing on SQL, data pipelines, cloud technologies, and emerging fields like big data or machine learning engineering. The importance of mastering foundational skills before moving to more advanced topics is also emphasized.
*  **Emotion:** The overall emotional tone is Neutral, offering practical guidance and advice to those seeking to specialize in data engineering.
*  **Top 3 Points of View:**
    *   Prioritize SQL, data pipelines, and cloud technologies as essential foundations.
    *   Consider specializing in big data or machine learning engineering after mastering the basics.
    *   SQL/Python, cloud ops and orchestration tools, and AI engineering are important specializations.
