---
title: "Data Engineering Subreddit"
date: "2026-02-16"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "ETL", "APIs", "data-volume", "AI-tools", "data-preservation"]
---

# Overall Ranking and Top Discussions
*   1. [What is the maximum incremental load you have witnessed?](https://www.reddit.com/r/dataengineering/comments/1r69f91/what_is_the_maximum_incremental_load_you_have/) (Score: 58)
    *   This thread discusses the immense scale of data processing in various industries, with users sharing experiences of incremental loads ranging from hundreds of GBs per minute to petabytes per day at large tech companies and telcos.
*   2. [How often do you make webhooks and APIs as a data engineer?](https://www.reddit.com/r/dataengineering/comments/1r5xqqt/how_often_do_you_make_webhooks_and_apis_as_a_data/) (Score: 33)
    *   Users debate the role of data engineers in building webhooks and APIs, often highlighting the overlap with software engineering skills and discussing practical applications for data ingestion and monitoring.
*   3. [Spent last quarter evaluating enterprise ETL tools](https://www.reddit.com/r/dataengineering/comments/1r5w346/spent_last_quarter_evaluating_enterprise_etl_tools/) (Score: 32)
    *   The community shares insights and recommendations on various enterprise ETL tools, discussing the pros and cons of self-hosted open-source solutions versus commercial or cloud-native offerings, and considering factors like cost and specific data requirements.
*   4. [What is the best way to preserve the greatest amount of information over the longest period of time?](https://www.reddit.com/r/dataengineering/comments/1r603vg/what_is_the_best_way_to_preserve_the_greatest/) (Score: 14)
    *   This discussion explores imaginative and practical methods for extremely long-term data preservation, ranging from durable physical materials to theoretical concepts like holographic storage and black holes.
*   5. [Org Claude code projects](https://www.reddit.com/r/dataengineering/comments/1r5tm64/org_claude_code_projects/) (Score: 11)
    *   Users exchange tips and best practices for organizing and utilizing AI tools like Claude for code projects, particularly within a Databricks environment, focusing on providing context to the AI and integrating it into development workflows.
*   6. [Opensource tool for small business](https://www.reddit.com/r/dataengineering/comments/1r6d7a5/opensource_tool_for_small_business/) (Score: 8)
    *   The thread provides recommendations for cost-effective, open-source data engineering tools and simple scripting solutions suitable for small businesses with limited budgets.
*   7. [Doubt regarding the viability of large tabular model and tabular diffusion model on real business data](https://www.reddit.com/r/dataengineering/comments/1r5t38r/doubt_regarding_the_viability_of_large_tabular/) (Score: 6)
    *   A bot directs users to community learning resources relevant to discussions around the viability of advanced tabular models in real-world business data scenarios.
*   8. [Cortex code use case resources](https://www.reddit.com/r/dataengineering/comments/1r60uol/cortex_code_use_case_resources/) (Score: 6)
    *   Users briefly discuss the performance of Cortex code for data modeling, with one positive report, and a bot shares links to learning resources.
*   9. [Integration with Synapse](https://www.reddit.com/r/dataengineering/comments/1r62ntd/integration_with_synapse/) (Score: 3)
    *   The discussion focuses on best practices for integrating with Azure Synapse, emphasizing the platform's native capabilities and the importance of proper configuration and monitoring to avoid complex or inefficient setups.
*   10. [Moving away from ETL](https://www.reddit.com/r/dataengineering/comments/1r6a56a/moving_away_from_etl/) (Score: 3)
    *   Users explore alternatives to traditional ETL processes, suggesting transactional bidirectional IPaaS solutions and Change Data Capture (CDC) mechanisms, especially when dealing with limited database access.
*   11. [Any advice on how to build a pipeline with Microsoft Access?](https://www.reddit.com/r/dataengineering/comments/1r5wkl0/any_advice_on_how_to_build_a_pipeline_with_microsoft_access/) (Score: 0)
    *   The thread offers mixed advice on building data pipelines using Microsoft Access, from pragmatic tips for working within its limitations to strong recommendations for migrating to more modern tools to avoid technical debt.
*   12. [Deploying R Shiny Apps via Dataiku: How Much Rework Is Really Needed?](https://www.reddit.com/r/dataengineering/comments/1r6kcem/deploying_r_shiny_apps_via_dataiku_how_much/) (Score: 0)
    *   This discussion addresses the amount of rework required when deploying R Shiny applications through Dataiku, emphasizing the critical role of consistent environments and diligent package management.

# Detailed Analysis by Thread
**[What is the maximum incremental load you have witnessed? (Score: 58)](https://www.reddit.com/r/dataengineering/comments/1r69f91/what_is_the_maximum_incremental_load_you_have/)**
*   **Summary:** Users share their experiences with large incremental data loads, ranging from 25 GB bi-monthly to exabytes daily at major tech companies. Examples include 100 GB every 10 minutes in telcos, 1 TB per hour in e-commerce, and 50 TB per day with 1M Kafka messages/sec. Some also mention petabytes per day at Facebook.
*   **Emotion:** Predominantly Neutral, with some Positive undertones. Comments focus on factual reporting of data volumes.
*   **Top 3 Points of View:**
    *   Many users report extremely high data volumes: Incremental loads frequently reach terabytes or even petabytes per day/hour, especially in industries like telco, e-commerce, and social media.
    *   Perception of "big data" evolves rapidly: What was considered large data a few years ago (e.g., 200M records/day) is now dwarfed by current workloads (e.g., 600M+ records/hour), indicating rapid growth in data generation.
    *   Data architecture and optimization are more crucial than raw size: Some argue that the discussion shouldn't solely focus on data volume, but rather on how data is managed, processed, and optimized (e.g., partitioning, indexing) to handle the scale efficiently.

**[How often do you make webhooks and APIs as a data engineer? (Score: 33)](https://www.reddit.com/r/dataengineering/comments/1r5xqqt/how_often_do_you_make_webhooks_and_apis_as_a_data/)**
*   **Summary:** The discussion revolves around the frequency and necessity of data engineers building webhooks and APIs. Many view it as an integral part of modern data engineering, highlighting the overlap with software engineering, while others see it as less common or primarily a backend task.
*   **Emotion:** Predominantly Neutral, with some Positive contributions regarding the value of these skills.
*   **Top 3 Points of View:**
    *   Data Engineering is a specialization of Software Engineering: A common sentiment is that data engineers should possess strong software engineering skills, including the ability to build APIs and webhooks, as it's essential for a well-rounded DE.
    *   Webhooks and APIs are useful for specific DE tasks: They are valuable for utility, monitoring, CI/CD, and as a consumption interface, especially for data ingestion (thin receivers).
    *   The boundary between DE and backend is fuzzy: The extent to which a data engineer builds and maintains APIs/webhooks often depends on team structure, data volume, and the complexity of required features (e.g., auth, retries, uptime guarantees), which might shift responsibility to a dedicated backend team for more complex cases.

**[Spent last quarter evaluating enterprise ETL tools (Score: 32)](https://www.reddit.com/r/dataengineering/comments/1r5w346/spent_last_quarter_evaluating_enterprise_etl_tools/)**
*   **Summary:** Users discuss various enterprise ETL tools, sharing experiences and recommendations. The conversation covers self-hosting solutions like Airbyte and Airflow, using cloud-native options, and considering alternatives for specific challenges like normalization and cost.
*   **Emotion:** Predominantly Neutral, with some Positive and Negative comments reflecting varied experiences and opinions on tools.
*   **Top 3 Points of View:**
    *   Self-hosted open-source tools like Airbyte and Airflow can be effective: A team successfully self-hosts these for ETL, praising Airbyte's connectors and declarative setup with Terraform/Airflow, despite a noted slowness in normalization for JSON data.
    *   Various tools and approaches exist for different use cases: Suggestions range from Snowflake's Openflow, dlt for connectors, Trino + dbt for ingestion/reverse ETL, dbx Lakeflow, SSIS, and even Flink/Beam for real-time performance, indicating no single universal solution.
    *   Cost and specific data needs drive tool selection: Factors like real-time requirements, data volume, and pricing models (e.g., compute vs. data volume for Fivetran alternatives) are key considerations, with a note that simpler Python/cron jobs might suffice for smaller, daily loads.

**[What is the best way to preserve the greatest amount of information over the longest period of time? (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1r603vg/what_is_the_best_way_to_preserve_the_greatest/)**
*   **Summary:** This thread explores speculative and practical methods for extremely long-term data preservation. Responses range from highly theoretical concepts like black holes to durable physical media and ancient storage techniques.
*   **Emotion:** Exclusively Neutral, with a humorous and speculative tone in many suggestions.
*   **Top 3 Points of View:**
    *   Highly durable physical materials: Suggestions include titanium tablets, stone (like the Code of Hammurabi), data etched into diamond, and 3D prints on "forever plastics."
    *   Technologically advanced storage concepts: Ideas like holographic storage (potentially petabytes per cm³) and DNA storage are proposed for their high density and potential longevity.
    *   Existing long-term storage technologies: Magnetic tapes are mentioned as a practical, cost-effective solution for long-term archiving, while punch cards are humorously noted for their non-degrading nature despite low density.

**[Org Claude code projects (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1r5tm64/org_claude_code_projects/)**
*   **Summary:** Discussion about organizing and utilizing Claude for code projects, particularly within a Databricks environment. Users share tips on providing context to AI, workflow integration, and recommended tools.
*   **Emotion:** Predominantly Neutral, with a positive sentiment towards Claude's potential.
*   **Top 3 Points of View:**
    *   Providing AI with context is crucial for performance: Creating a `CLAUDE.md` file in the project root to describe pipeline structure, schemas, and naming conventions significantly improves Claude's effectiveness.
    *   Integrate AI into development workflows: Using Claude Code in a terminal or VS Code extension, connected to project repositories, is recommended over manual copy-pasting, especially when paired with Databricks repos for version control.
    *   Databricks tools and apps are useful for AI-assisted development: The Databricks SQL MCP server and Databricks apps (using FastAPI/HTMX for dashboards) are highlighted as valuable for local development and business-oriented solutions, alongside tools like `databricks ai-dev-kit`.

**[Opensource tool for small business (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1r6d7a5/opensource_tool_for_small_business/)**
*   **Summary:** Users recommend open-source tools and simple approaches for data engineering needs in small business contexts, focusing on cost-effectiveness and ease of implementation.
*   **Emotion:** Exclusively Neutral, offering practical advice.
*   **Top 3 Points of View:**
    *   Simple scripting and scheduling are often sufficient: For daily loads of a few million records, basic Python scripts combined with `crontab` (Linux) or Windows Task Scheduler are recommended as a free and effective solution.
    *   Leveraging existing database capabilities or cloud services: Suggestions include using SQL for transformations, DuckDB on a small VM, or utilizing native data transformation tools offered by major cloud providers for clean, structured data, which saves on setup and offers good performance.
    *   Apache Nifi as a low-code option: Apache Nifi is presented as a viable, albeit heavy, open-source tool capable of creating HTTP endpoints with minimal coding, suitable for certain integration needs.

**[Doubt regarding the viability of large tabular model and tabular diffusion model on real business data (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1r5t38r/doubt_regarding_the_viability_of_large_tabular/)**
*   **Summary:** A bot provides a link to learning resources in response to a question about tabular models and diffusion models.
*   **Emotion:** Neutral, as the only comment is an automated response.
*   **Top 3 Points of View:**
    *   The subreddit maintains a repository of community-submitted learning resources for data engineering topics.

**[Cortex code use case resources (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1r60uol/cortex_code_use_case_resources/)**
*   **Summary:** A user confirms positive experience with Cortex code for data modeling, and a bot provides a link to learning resources.
*   **Emotion:** Mixed (one Positive, one Neutral). Mostly Neutral, with a positive contribution from a user.
*   **Top 3 Points of View:**
    *   Cortex code is effective for data modeling: One user had a positive experience using Cortex code for both data model and code generation, indicating good performance.
    *   The subreddit offers a list of community-submitted learning resources.

**[Integration with Synapse (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1r62ntd/integration_with_synapse/)**
*   **Summary:** A user criticizes a proposed solution for Synapse integration, advocating for leveraging Synapse's existing capabilities and proper setup.
*   **Emotion:** Neutral, with a critical but constructive tone.
*   **Top 3 Points of View:**
    *   Proposed solutions might be over-complicated: The commenter believes the user's proposed integration method is messier, more expensive, and harder to maintain than necessary.
    *   Synapse is fully capable if configured correctly: Azure Synapse is deemed sufficient for most data engineering needs, implying that any current issues likely stem from improper setup rather than tool limitations.
    *   Importance of monitoring and proper error handling: The commenter emphasizes using Synapse's built-in pipeline monitoring and notification features to prevent "silent failures."

**[Moving away from ETL (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1r6a56a/moving_away_from_etl/)**
*   **Summary:** Users suggest alternative approaches and tools for data integration when moving away from traditional ETL processes, especially when direct database access is limited.
*   **Emotion:** Exclusively Neutral, offering solution-oriented advice.
*   **Top 3 Points of View:**
    *   Consider transactional bidirectional IPaaS solutions: For complex integrations beyond traditional ETL, tools like MuleSoft or Boomi are suggested as more suitable IPaaS (Integration Platform as a Service) options.
    *   Explore Change Data Capture (CDC) mechanisms: If direct database access is limited, exploring CDC features like SAP HANA CDC might provide a way to get necessary metrics and data updates.
    *   Direct database access is critical for certain metrics: Without direct access to the database, obtaining specific metrics might be impossible, highlighting a fundamental limitation.

**[Any advice on how to build a pipeline with Microsoft Access? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1r5wkl0/any_advice_on_how_to_build_a_pipeline_with_microsoft_access/)**
*   **Summary:** Users provide advice for building data pipelines using Microsoft Access, ranging from practical tips within Access/VBA to strong recommendations to migrate to more modern tools.
*   **Emotion:** Mixed (several Positive, some Neutral).
*   **Top 3 Points of View:**
    *   Avoid Microsoft Access; request better tools: Many strongly advise against using Access for pipelines, viewing it as legacy software that creates technical debt, and suggest asking for more modern tools.
    *   Leverage existing tools and scripting within limitations: If stuck with Access, users recommend using VBA professionally, focusing on clear input/output, and expanding capabilities with PowerShell. AI coding tools like Claude can also assist in building out solutions.
    *   Consider modern alternatives if migration is possible: Suggestions include moving to platforms like Directus, which can wrap PostgreSQL with an Access-like UI and provide APIs for event capturing, offering a more robust and scalable solution.

**[Deploying R Shiny Apps via Dataiku: How Much Rework Is Really Needed? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1r6kcem/deploying_r_shiny_apps_via_dataiku_how_much/)**
*   **Summary:** A user discusses the variability of rework needed when deploying R Shiny apps via Dataiku, emphasizing the importance of consistent environments and package management.
*   **Emotion:** Neutral, providing a nuanced technical perspective.
*   **Top 3 Points of View:**
    *   Rework depends heavily on environment consistency: The amount of rework required is highly variable, depending on whether the R Shiny app is developed and deployed in similar environments (e.g., Docker/Linux) with consistent package versions.
    *   R's leniency can lead to production issues: R's flexibility, while beneficial in development, can cause significant differences in production applications if not carefully managed, making environment setup critical.
    *   Environment management is key: Explicitly managing package versions and deploying in controlled environments (like Docker) can mitigate rework and ensure consistency.
