---
title: "Data Engineering Subreddit"
date: "2026-03-07"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "data_platforms", "career_advice", "ai", "sql"]
---

# Overall Ranking and Top Discussions
1.  [Client wants <1s query time on OLAP scale. Wat do](https://www.reddit.com/r/dataengineering/comments/1rmrmxk/client_wants_1s_query_time_on_olap_scale_wat_do/) (Score: 271)
    *   Users discussed strategies for meeting a client's demanding request for sub-second query times on OLAP-scale data, ranging from managing client expectations and clarifying actual business needs to suggesting specific technical solutions like ClickHouse or optimized indexing.

2.  [Is it standard for data engineers to work blind without front end access, or is this what happens when a business leans on one person’s tribal knowledge for years?](https://www.reddit.com/r/dataengineering/comments/1rnbmtv/is_it_standard_for_data_engineers_to_work_blind/) (Score: 35)
    *   The thread explores whether data engineers commonly lack front-end access, attributing this issue to data governance gaps and over-reliance on individual expertise, and highlighting the importance of access for data validation and understanding.

3.  [We open-sourced a small AST-based Go tool for catching risky SQL in CI(no ai)](https://www.reddit.com/r/dataengineering/comments/1rmyz39/we_opensourced_a_small_astbased_go_tool_for/) (Score: 14)
    *   This thread introduces an open-source Go tool designed to detect risky SQL queries in CI pipelines using Abstract Syntax Trees, without AI, with a discussion point on handling dynamically generated SQL.

4.  [Help needed in dataform js and sqlx scripting](https://www.reddit.com/r/dataengineering/comments/1rmy9az/help_needed_in_dataform_js_and_sqlx_scripting/) (Score: 5)
    *   A user sought assistance with Dataform.js and SQLX scripting, receiving advice focused on correctly passing context (`ctx`) within nested functions to avoid issues.

5.  [Ai and side projects](https://www.reddit.com/r/dataengineering/comments/1rmtv40/ai_and_side_projects/) (Score: 4)
    *   The discussion centers on the use of AI tools like Claude Code for side projects, with advice ranging from leveraging AI for speed while still understanding underlying code to warnings against "black-box" coding without foundational knowledge.

6.  [Query](https://www.reddit.com/r/dataengineering/comments/1rn74st/query/) (Score: 4)
    *   This post provides career advice for data engineers with SQL and PySpark backgrounds, focusing on learning a single cloud stack (e.g., Azure), mastering core tools, and building practical end-to-end projects.

7.  [Api in deltalake](https://www.reddit.com/r/dataengineering/comments/1rmx702/api_in_deltalake/) (Score: 3)
    *   Users discussed solutions for building an API service to access data stored in Delta Lake, addressing performance challenges with large, frequently updated datasets and suggesting separate serving layers or specific Databricks features like Lakebase.

8.  [MWAA Cost](https://www.reddit.com/r/dataengineering/comments/1rnb0l9/mwaa_cost/) (Score: 3)
    *   The thread discusses the costs and performance of AWS Managed Workflows for Apache Airflow (MWAA), including scaling instances for concurrent DAGs, optimizing Airflow usage, and considering serverless options.

9.  [Best Data Pipeline Connector to move data from an Excel Online to BigQuery for Looker Studio Visualization](https://www.reddit.com/r/dataengineering/comments/1rmvqfl/best_data_pipeline_connector_to_move_data_from_an/) (Score: 2)
    *   Users sought and offered solutions for moving data from Excel Online to Google BigQuery for Looker Studio, suggesting leveraging Google Sheets as an intermediary, manual CSV loads, or Python scripts.

10. [DQ Monitoring with scaling problems](https://www.reddit.com/r/dataengineering/comments/1rmu2ad/dq_monitoring_with_scaling_problems/) (Score: 2)
    *   The discussion addresses data quality (DQ) monitoring and scaling issues, particularly with SAP full loads, offering solutions like Change Data Capture (CDC), Azure Data Factory for orchestration, and dbt for transformations and DQ checks.

11. [Changing career path to Data Engineering](https://www.reddit.com/r/dataengineering/comments/1rnbe8k/changing_career_path_to_data_engineering/) (Score: 1)
    *   This thread provides guidance to an individual transitioning to data engineering, emphasizing leveraging existing math and programming skills, focusing on core DE concepts, and building a practical portfolio project.

12. [How should I convert my Internship to a full time role.](https://www.reddit.com/r/dataengineering/comments/1rnc691/how_should_i_convert_my_internship_to_a_full_time/) (Score: 0)
    *   The thread offers advice to an intern aiming for a full-time role, suggesting direct communication with the company while also preparing to seek other job opportunities.

13. [How to transform raw scraped data into a nice data model for analysis](https://www.reddit.com/r/dataengineering/comments/1rng8q2/how_to_transform_raw_scraped_data_into_a_nice/) (Score: 0)
    *   The discussion focuses on strategies for transforming raw scraped data into a structured data model, particularly for identifying and clustering unique entities across multiple sources using source IDs and entity resolution.

14. [What repetitive task would you automate with AI?](https://www.reddit.com/r/dataengineering/comments/1rnie1t/what_repetitive_task_would_you_automate_with_ai/) (Score: 0)
    *   Users discussed the potential of AI for automating repetitive tasks in data engineering, expressing skepticism about AI for critical data tasks but acknowledging its utility for code assistance and summarization.

# Detailed Analysis by Thread
**[Client wants <1s query time on OLAP scale. Wat do (Score: 271)](https://www.reddit.com/r/dataengineering/comments/1rmrmxk/client_wants_1s_query_time_on_olap_scale_wat_do/)**
*   **Summary:** Users discussed strategies for meeting a client's demanding request for sub-second query times on OLAP-scale data. Discussions ranged from managing client expectations and clarifying actual business needs to suggesting specific technical solutions like ClickHouse or optimized indexing. Comments also touched on the significant investment often required for such performance.
*   **Emotion:** The overall emotional tone is **Neutral**, characterized by a pragmatic and problem-solving approach. While there's an underlying acknowledgment of the challenge posed by unrealistic client demands, responses focus on offering concrete technical advice, strategic questions, and best practices for managing expectations.
*   **Top 3 Points of View:**
    *   **Manage Client Expectations & Understand Needs:** The most prominent view is to push back on the client's arbitrary demand by clarifying the actual business problem, the value of sub-second queries, and managing expectations. This includes asking about the decisions being actioned, the financial impact, and exploring specific use cases rather than taking constraints at face value.
    *   **Technical Solutions & Performance Optimization:** Many users suggested various technical approaches to achieve high performance. These included database choices like ClickHouse (with NVMe and in-memory caching), Hyper-scale databases with proper indexing, and NoSQL solutions like DynamoDB for point lookups. Partitioning and indexing were frequently mentioned as fundamental optimization techniques.
    *   **Cost vs. Benefit Analysis:** Several comments highlighted the significant investment required to meet such stringent SLAs, suggesting that the client should be made aware of the cost and the necessity of such an investment versus the actual business benefit.

**[Is it standard for data engineers to work blind without front end access, or is this what happens when a business leans on one person’s tribal knowledge for years? (Score: 35)](https://www.reddit.com/r/dataengineering/comments/1rnbmtv/is_it_standard_for_data_engineers_to_work_blind/)**
*   **Summary:** The thread explores whether it's standard for data engineers to lack front-end access to the systems they build pipelines for, and if this issue stems from over-reliance on individual "tribal knowledge." Users largely agree it's not ideal but common, especially in certain organizational structures or startups. They emphasize the importance of access for validation and understanding.
*   **Emotion:** The emotional tone is predominantly **Neutral**, but with a noticeable presence of **Negative** sentiment regarding the situation itself (e.g., "bananas dumb," "crazy inefficient") and **Positive** acknowledgment that while problematic, it's a common scenario, particularly in startups. The sentiment primarily focuses on expressing problems and suggesting solutions.
*   **Top 3 Points of View:**
    *   **Not Standard, but Common Problem:** The consensus is that working without front-end access is not standard practice for data engineers but is extremely common due to data governance gaps, reliance on tribal knowledge, or outsourced IT structures. This often leads to inefficient work and low-quality data.
    *   **Necessity of Front-End Access:** Users strongly emphasize that read-only front-end access is vital for data engineers to understand user workflows, how data is captured, and to validate that delivered data matches what users see, thereby ensuring data quality.
    *   **Solutions & Advocacy:** Solutions include framing the lack of access as a business risk (not just personal convenience), taking a "political approach" to educate leadership on the problem's effects, and addressing underlying organizational issues that create reliance on "hero" individuals instead of a robust data culture.

**[We open-sourced a small AST-based Go tool for catching risky SQL in CI(no ai) (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1rmyz39/we_opensourced_a_small_astbased_go_tool_for/)**
*   **Summary:** This thread introduces an open-source Go tool that uses Abstract Syntax Trees (AST) to detect risky SQL queries in Continuous Integration (CI) pipelines without relying on AI. The main comment inquires about the tool's effectiveness with dynamically built SQL.
*   **Emotion:** The emotional tone is **Neutral**, characterized by an informative and curious sentiment. The sole meaningful comment acknowledges the technical approach and seeks clarification on specific edge cases.
*   **Top 3 Points of View:**
    *   **AST-based Checks are Superior for Complex SQL:** A key point is that AST-based checks are more suitable and robust than regex for analyzing SQL, especially when query generation becomes complex.
    *   **Challenge of Dynamic SQL:** The critical challenge for such tools is effectively handling SQL queries that are built dynamically at runtime, as this is where their capabilities are most rigorously tested.

**[Help needed in dataform js and sqlx scripting (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1rmy9az/help_needed_in_dataform_js_and_sqlx_scripting/)**
*   **Summary:** A user is seeking help with Dataform.js and SQLX scripting. The provided comment offers a specific debugging tip related to function context. The advice focuses on ensuring `ctx` is passed correctly and not overwritten, especially in complex or nested functions.
*   **Emotion:** The emotional tone is **Neutral** and helpful, focusing purely on providing a technical solution to a common programming issue.
*   **Top 3 Points of View:**
    *   **Context Passing is Key for Nested Functions:** The primary point of view is that issues with complex functions in Dataform.js/SQLX, when simple ones work, often stem from incorrect or overwritten `ctx` (context) passing within nested functions. Ensuring `ctx` is forwarded properly is crucial.

**[Ai and side projects (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1rmtv40/ai_and_side_projects/)**
*   **Summary:** The discussion revolves around the appropriateness of using AI tools like Claude Code for side projects, particularly for a learner who struggles with understanding and recreating the actual code. Opinions vary on leveraging AI for speed versus building foundational coding skills.
*   **Emotion:** The overall emotional tone is a mix of **Neutral** advice and **Positive** encouragement for using AI, balanced by strong **Negative** warnings about the pitfalls of over-reliance without understanding. The sentiment is primarily instructive and cautionary.
*   **Top 3 Points of View:**
    *   **Use AI to Accelerate Learning, but Understand Fundamentals:** Many advise using AI tools to speed up development but strongly emphasize the need to learn the underlying code, understand "why" it works, and be able to debug and modify it independently. It's akin to using a calculator but still learning math.
    *   **Black-Box Coding is Detrimental:** A critical point is that relying on AI without understanding the code (i.e., "vibe coding" or "black box coding") is highly detrimental. It leads to an inability to troubleshoot, fix issues, or progress, potentially creating massive technical debt for others.
    *   **AI Use Differs by Experience Level:** Experienced developers can leverage AI effectively because they already understand what they're building and can critically review the output, whereas beginners risk simply prompting until something works without actual learning.

**[Query (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1rn74st/query/)**
*   **Summary:** This thread, despite its generic title, focuses on career advice for someone with SQL and PySpark experience looking into data engineering, specifically regarding cloud platforms. Recommendations include focusing on specific cloud stacks and building practical projects.
*   **Emotion:** The emotional tone is predominantly **Neutral** and helpful, offering practical career advice and learning pathways with a focus on skill development and hands-on experience.
*   **Top 3 Points of View:**
    *   **Focus on a Single Cloud Stack:** A primary recommendation is to concentrate on mastering one cloud provider's data engineering stack (e.g., Azure: Data Lake Gen2, Data Factory, Synapse/Databricks) rather than trying to learn multiple platforms at once.
    *   **Prioritize Core Tools and Concepts:** Key tools like Azure Data Factory, Azure Databricks, and ADLS are identified as core for most Azure DE roles. Learning pipeline scheduling, monitoring, and versioning is also highlighted as crucial for reliable pipelines.
    *   **Build End-to-End Projects:** Gaining hands-on experience by building real ETL pipeline projects is strongly advised to demonstrate practical skills to potential employers and solidify theoretical knowledge.

**[Api in deltalake (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1rmx702/api_in_deltalake/)**
*   **Summary:** Users discuss how to build an API service to access data stored in Delta Lake, particularly addressing performance challenges with large, frequently updated datasets. Solutions range from creating a separate serving layer to leveraging specific Databricks features.
*   **Emotion:** The emotional tone is **Neutral** and problem-solving, with a focus on technical solutions and clarifications. There's an underlying acknowledgment of performance challenges but without overt negativity.
*   **Top 3 Points of View:**
    *   **Performance Challenges with Direct Delta Lake Access:** Directly querying Delta Lake for API services, especially with large datasets and frequent updates (millions of records every 15 minutes), can be slow and may not handle deleted items well with certain tools.
    *   **Separate Serving Layer for API:** The recommended approach is to create a dedicated, more performant serving database layer on top of the Delta Lake (e.g., Postgres, using tools like Databricks Lakebase) to handle high-frequency API hits, as direct file reads from cloud storage can be costly and slow.
    *   **Consider Delta Sharing & Clarify API Intent:** Suggestions also include exploring Delta Sharing as a non-traditional API option and clarifying the API's actual purpose, as attempting to return billions of records directly via API is generally impractical.

**[MWAA Cost (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1rnb0l9/mwaa_cost/)**
*   **Summary:** This thread focuses on the costs and performance of AWS Managed Workflows for Apache Airflow (MWAA), particularly concerning scaling and optimization for DAGs. Users share experiences with different instance sizes and discuss strategies for cost-efficiency.
*   **Emotion:** The emotional tone is **Neutral** and exploratory, with users sharing experiences and offering advice on MWAA usage and potential cost-saving measures. There's a slight positive note about MWAA's capabilities when used effectively.
*   **Top 3 Points of View:**
    *   **MWAA Performance and Scaling:** MWAA instances can handle a significant number of DAGs (e.g., 150 on a small instance) but may require scaling up to a medium instance for concurrent heavy loads. It's important to distinguish between UI slowness and DAG task slowness for troubleshooting.
    *   **Optimize Airflow Usage:** Airflow itself should primarily be used for orchestration and interacting with other services, not for heavy compute tasks. Heavy lifting, especially with tools like dbt, should be offloaded to the data warehouse for efficiency.
    *   **Consider Serverless Options:** MWAA serverless is being considered as a potential cost-saving solution, especially for environments with daily batch processing, due to its ability to scale down to zero when not in use.

**[Best Data Pipeline Connector to move data from an Excel Online to BigQuery for Looker Studio Visualization (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1rmvqfl/best_data_pipeline_connector_to_move_data_from_an/)**
*   **Summary:** Users are looking for the best way to move data from Excel Online to Google BigQuery for visualization in Looker Studio, discussing various manual and automated methods. The consensus leans towards leveraging existing Google Cloud tools or scripting.
*   **Emotion:** The emotional tone is entirely **Neutral** and helpful, offering straightforward technical advice and alternative solutions to achieve the desired data flow.
*   **Top 3 Points of View:**
    *   **Leverage Google Sheets as an Intermediate:** The most common and recommended approach is to use Google Sheets as an intermediary, as it can be directly connected to BigQuery or Looker, simplifying the data flow from Excel Online.
    *   **Manual & Scripted Solutions:** For less frequent updates, manual loading of CSVs into BigQuery or creating external tables linked to Google Cloud Storage (GCS) are viable options. For more automation, Python scripts can be used to push data to BigQuery or GCS on a schedule.
    *   **No Direct "Connector" for Excel Online:** There isn't a widely recognized direct "connector" for this specific Excel Online to BigQuery pipeline, implying workarounds are usually necessary.

**[DQ Monitoring with scaling problems (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1rmu2ad/dq_monitoring_with_scaling_problems/)**
*   **Summary:** This thread addresses data quality (DQ) monitoring challenges, particularly scaling issues with SAP full loads. The provided comment offers comprehensive solutions for improving extraction, transformation, and DQ checks within an Azure lakehouse architecture.
*   **Emotion:** The emotional tone is **Neutral** and highly technical, focusing on providing an efficient and structured solution to a complex data engineering problem, demonstrating expertise and practicality.
*   **Top 3 Points of View:**
    *   **Enable CDC for SAP Full Loads:** The key to improving SAP full load efficiency is enabling Change Data Capture (CDC) via SLT or CDS views to get reliable change detection, drastically reducing extraction windows.
    *   **Orchestration and Lakehouse Architecture:** For Azure environments, using Azure Data Factory (ADF) for orchestration with watermark-based incremental loads into a lakehouse layer (ADLS + Delta Lake for native merge/upsert) is recommended.
    *   **dbt for Transformations and DQ:** Moving transformation logic into dbt on top of Synapse or Databricks allows for dependency-aware incremental models and building DQ checks as dbt tests, significantly collapsing processing windows.

**[Changing career path to Data Engineering (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1rnbe8k/changing_career_path_to_data_engineering/)**
*   **Summary:** This thread offers advice to an individual with a math background, Python, and DAX experience who is looking to transition into data engineering. Recommendations focus on skill development, learning core concepts, and building a practical portfolio.
*   **Emotion:** The emotional tone is overwhelmingly **Neutral** and supportive, providing clear, actionable steps for career transition and emphasizing the advantages of existing skills.
*   **Top 3 Points of View:**
    *   **Leverage Existing Strengths:** A math background is considered a significant advantage, as it aids in optimization and algorithmic thinking, which many DE candidates lack. Existing Python and DAX skills are also highlighted as valuable starting points.
    *   **Core Skill Focus:** Key areas to focus on are SQL (deep understanding including window functions, CTEs, query optimization), at least one orchestration tool (like Airflow), and conceptual understanding of data warehouses (star schema, slowly changing dimensions). Learning Docker is also mentioned as beneficial.
    *   **Build a Practical Portfolio Project:** The most emphasized advice is to build one end-to-end data engineering project (ingest from API, transform, load to warehouse, serve in dashboard) to demonstrate hands-on experience and gain interviews, especially within existing domain knowledge (supply chain/finance).

**[How should I convert my Internship to a full time role. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rnc691/how_should_i_convert_my_internship_to_a_full_time/)**
*   **Summary:** A user is asking for advice on converting an internship into a full-time role. The primary advice is to directly ask for a full-time offer and be prepared to seek other opportunities if the company seems unwilling to commit.
*   **Emotion:** The emotional tone is **Neutral** and pragmatic, leaning towards a slightly cautious or skeptical outlook regarding the company's intentions, while also being direct and empowering for the intern.
*   **Top 3 Points of View:**
    *   **Directly Ask for a Full-Time Role:** The most straightforward approach is to directly ask the company if they can offer a full-time position.
    *   **Be Prepared for a "No" and Plan B:** It's common for companies to prefer paying intern rates and not extend full-time offers. Therefore, the intern should start applying to other roles immediately until a signed offer letter is in hand.

**[How to transform raw scraped data into a nice data model for analysis (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rng8q2/how_to_transform_raw_scraped_data_into_a_nice/)**
*   **Summary:** The thread discusses strategies for transforming raw scraped data into a structured data model suitable for analysis, specifically focusing on identifying unique entities across multiple sources. Recommendations include creating unique identifiers and implementing entity resolution logic.
*   **Emotion:** The emotional tone is **Neutral** and instructive, providing clear technical steps for data modeling and entity management.
*   **Top 3 Points of View:**
    *   **Create Unique Source IDs:** For each ingested entity from each source, a unique "source id" (e.g., using a hash) should be created to uniquely identify that entity from its origin.
    *   **Implement Entity Resolution Logic:** To link and cluster similar entities from different sources, entity resolution logic is needed. This can involve using name similarity algorithms (like Edit Distance or Soundex).
    *   **Generate Cluster IDs:** Each identified cluster of related entities from different sources should be assigned a unique ID, potentially a hash of the concatenated source IDs within that cluster.

**[What repetitive task would you automate with AI? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rnie1t/what_repetitive_task_would_you_automate_with_ai/)**
*   **Summary:** Users discuss which repetitive tasks, if any, they would automate with AI in data engineering/analytics contexts. There's general skepticism about AI for critical data tasks but acceptance for code assistance and summarization.
*   **Emotion:** The emotional tone is predominantly **Neutral**, with a clear undercurrent of **Skepticism** and caution regarding AI's current capabilities, particularly with numbers and critical data operations. There's a positive acknowledgement of its utility for specific, less critical tasks.
*   **Top 3 Points of View:**
    *   **AI for Code Assistance, Not Data Automation:** A strong consensus is that AI is useful for assisting with code writing, making it readable and maintainable, and generating tests, but it should not be trusted with automating tasks involving critical numbers or data manipulation directly due to its unreliability.
    *   **AI for Summarization and Non-Critical Tasks:** "AI" (or rather, advanced NLP tools) is effectively used for summarizing information, such as meeting transcripts and notes, to extract actions, as already done by conferencing apps like Zoom.
    *   **Human Expertise Remains Paramount for Critical Tasks:** For tasks requiring folk knowledge, business domain understanding, experience, and expertise, AI currently causes rework and cannot replace human input. These critical tasks are what people are for.
