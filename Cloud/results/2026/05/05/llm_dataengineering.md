---
title: "Data Engineering Subreddit"
date: "2026-05-05"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "data analysis", "AI", "LLM", "PowerBI"]
---

# Overall Ranking and Top Discussions
*   1. [[Data Landscape: An opinionated, interactive map of the relevant open standards in the world of data.](https://www.data-landscape.com) (Score: 34)
    *   This thread discusses a new interactive map of open standards in data, with users sharing their thoughts and asking about the inclusion of Master Data Management (MDM).
*   2. [How to model the Gold layer for a CRM dataset in Databricks? (Score: 14)
    *   Users are discussing best practices for modeling a "Gold layer" in Databricks for CRM data, with advice on table naming conventions, star schemas, and the distinction between silver and gold layers.
*   3. [How are DE interviews these days? LeetCode + AI tools? (Score: 13)
    *   This discussion revolves around current data engineering interview practices, specifically questioning the role of LeetCode-style problems, the use of AI tools, and the relevance of these to day-to-day data engineering tasks.
*   4. [Help with friction between architecture team and our PowerBI team (Score: 6)
    *   This thread explores the friction between an architecture team and a PowerBI team, with users offering advice on data modeling, centralized data layers, and the importance of communication and data governance.
*   5. [DE or Data Analyst which is more suitable for me? (Score: 5)
    *   A user is seeking guidance on whether to pursue a career in Data Engineering (DE) or Data Analysis, with respondents discussing the core differences, required skills, and personal interests that might steer them towards one role over the other.
*   6. [Looking for a structured end-to-end data engineering program (Score: 3)
    *   This discussion focuses on recommendations for structured learning resources and programs for aspiring data engineers, including books, online courses, and project ideas.
*   7. [Stanford Seminar - Big Data is (at least) Four Different Problems (Score: 2)
    *   This thread shares a link to a Stanford seminar discussing big data as multiple distinct problems.
*   8. [A dedicated LLM library for data engineering (Score: 0)
    *   Users are questioning the practicality and cost-effectiveness of using LLMs directly within data engineering pipelines, especially for large-scale data processing, and comparing it to traditional machine learning models.
*   9. [A RAG postmortem: when the dashboard read 89% accuracy and production was 40% wrong (Score: 0)
    *   This postmortem analyzes a failure pattern in RAG (Retrieval-Augmented Generation) systems where a dashboard's reported accuracy was misleading, leading to incorrect decisions.
*   10. [Building a secondary research pipeline for my urbanization thesis using old chronicling America newspapers (Score: 0)
    *   This thread discusses a research pipeline that uses LLMs for secondary research, with a user expressing concerns about the reliability of one LLM reviewing another and suggesting human review.

# Detailed Analysis by Thread
**[ Data Landscape: An opinionated, interactive map of the relevant open standards in the world of data. (Score: 34)](https://www.data-landscape.com)**
*  **Summary:** A user shared an interactive map of open standards in the data world. The discussion included positive feedback on the presentation and questions about the inclusion of Master Data Management (MDM).
*  **Emotion:** Primarily Neutral with strong Positive sentiment. Users expressed admiration for the tool and curiosity about its content.
*  **Top 3 Points of View:**
    *   Appreciation for the well-presented interactive map and its utility.
    *   Inquiry about the absence of Master Data Management (MDM) in the map and reasons behind it.
    *   Acknowledgement of the effort and the value of the provided information, despite a slight learning curve for understanding the criteria.

**[ How to model the Gold layer for a CRM dataset in Databricks? (Score: 14)](https://i.redd.it/079ru4obbczg1.png)**
*  **Summary:** The discussion centers on how to effectively model the "Gold layer" for a CRM dataset within Databricks. Advice includes table naming conventions, understanding fact and dimension tables, and clarifying the role of the silver layer.
*  **Emotion:** Predominantly Neutral. The tone is analytical and focused on technical best practices for data modeling.
*  **Top 3 Points of View:**
    *   The importance of proper naming conventions (e.g., ending with \_Fact or \_Dim) and the structure of fact tables with timestamps and surrogate keys.
    *   A question about the layered architecture, suggesting the silver layer should handle cleaned data and the gold layer aggregations and reporting structures.
    *   Clarification sought on the event or transaction to be modeled with a star schema, with a suggestion that the current tables might be ML source tables rather than a dimension model.

**[ How are DE interviews these days? LeetCode + AI tools? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1t4hgzf/how_are_de_interviews_these_days_leetcode_ai_tools/)**
*  **Summary:** This thread discusses the current landscape of data engineering interviews, focusing on the relevance of LeetCode problems, the integration of AI tools, and whether these assessments truly reflect daily job responsibilities.
*  **Emotion:** Mostly Neutral, with some undertones of concern and reflection on past experiences.
*  **Top 3 Points of View:**
    *   Interviews often include SQL optimization, Python algorithm questions, and architecture discussions (like medallion architecture), with mixed opinions on AI tool usage.
    *   A user shared an experience with a take-home assignment involving database creation and querying, which they found to be a more practical assessment of DE skills. They also noted that AI tool usage was discussed positively.
    *   A key question raised is whether LeetCode problems are genuinely representative of daily DE tasks or merely "interviewer ego stroking."

**[ Help with friction between architecture team and our PowerBI team (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1t4mv8r/help_with_friction_between_architecture_team_and/)**
*  **Summary:** The user is seeking advice on resolving friction between an architecture team and their PowerBI team. Suggestions involve data modeling practices for currency and time, the separation of concerns between data engineering and BI development, and the importance of clear ownership.
*  **Emotion:** Mostly Neutral, with some users sharing negative experiences and offering pragmatic, albeit sometimes cynical, advice.
*  **Top 3 Points of View:**
    *   Power BI developers should learn SQL and the data engineering team should centralize data. Power BI teams should utilize this centralized data rather than modeling their own "gold" layer within the tool.
    *   It's a misguided approach to hold the data engineering team solely responsible for all data objects on Snowflake. BI developers should have the ability to materialize their own aggregate tables for visualization.
    *   A more pragmatic view suggests giving more freedom to BI teams, accepting that PowerBI might be messy but is established and fast, and that fighting this can be futile.

**[ DE or Data Analyst which is more suitable for me? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1t49rs6/de_or_data_analyst_which_is_more_suitable_for_me/)**
*  **Summary:** A user is asking for help deciding between a career as a Data Engineer (DE) or a Data Analyst. The responses highlight the core differences in responsibilities, skills, and interests that should guide this decision.
*  **Emotion:** Neutral, with a helpful and guiding tone.
*  **Top 3 Points of View:**
    *   Data Engineers who understand query optimization and data modeling are more valuable long-term than analysts who can learn SQL, as DE requires understanding data movement and storage.
    *   The decision should be based on personal interests: Data Analysts focus on business insights, stakeholder communication, and presentations, while Data Engineers focus on technology, infrastructure, building pipelines, and system design.
    *   There's also a suggestion to consider "analytics engineering" as a middle ground, and a pragmatic comment that both roles are "easy" and the choice might depend on what one can land.

**[ Looking for a structured end-to-end data engineering program (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1t4ildy/looking_for_a_structured_endtoend_data/)**
*  **Summary:** Users are looking for structured resources to learn end-to-end data engineering. Recommendations include using open data sources for projects, designing ELT pipelines, utilizing the Medallion architecture, and specific books and learning paths.
*  **Emotion:** Neutral, with a focus on providing helpful resources.
*  **Top 3 Points of View:**
    *   Suggestions include using open data sources, designing ELT pipelines, and implementing the Medallion layers with Python for extraction/loading and SQL/dbt for transformation.
    *   Several key books are recommended, such as "Fundamentals of Data Engineering," "Learning Spark," "The Data Warehouse Toolkit," and "Designing Data-Intensive Applications."
    *   A link to community-submitted learning resources on dataengineering.wiki is provided.

**[ Stanford Seminar - Big Data is (at least) Four Different Problems (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1t4ikp5/stanford_seminar_big_data_is_at_least_four/)**
*  **Summary:** This thread shares a link to a YouTube presentation from a Stanford Seminar that breaks down "Big Data" into at least four distinct problems.
*  **Emotion:** Neutral. The post is informational.
*  **Top 3 Points of View:**
    *   The primary point is the sharing of a link to a YouTube presentation on the topic. (No further discussion points are present in the provided data).

**[ A dedicated LLM library for data engineering (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1t4g9b6/a_dedicated_llm_library_for_data_engineering/)**
*  **Summary:** Users are discussing the integration of Large Language Models (LLMs) into data engineering pipelines. Concerns are raised about the cost and practicality for big data scenarios compared to traditional machine learning.
*  **Emotion:** Negative and skeptical. Users are critical of the presented LLM use cases and question their feasibility.
*  **Top 3 Points of View:**
    *   The example of using LLMs for molar mass calculations is criticized as impractical for a data pipeline.
    *   Concerns are raised about the high cost of using LLMs for big data and the suggestion that traditional ML models might be more cost-effective, even for tasks like sentiment analysis.
    *   A question is posed about whether AI is being integrated into pipelines for real-time responses or transformations.

**[ A RAG postmortem: when the dashboard read 89% accuracy and production was 40% wrong (Score: 0)](https://failurearchaeology.substack.com/p/a-rag-postmortem-89-internal-accuracy)**
*  **Summary:** This postmortem details a failure pattern observed in RAG systems where a dashboard's reported accuracy was significantly misleading, leading to incorrect business decisions. It highlights issues with static evaluation sets and the defense of inaccurate metrics.
*  **Emotion:** Neutral, analytical, and cautionary. The tone is that of a technical postmortem.
*  **Top 3 Points of View:**
    *   A dashboard based on a static, self-authored evaluation set can be misleading, especially when non-technical decisions are made based on it.
    *   The problem of metric/reality drift is not unique to RAG systems and can occur in any data pipeline.
    *   The postmortem emphasizes the importance of questioning the accuracy metrics presented on dashboards and provides operative questions to identify potential deception.

**[ Building a secondary research pipeline for my urbanization thesis using old chronicling America newspapers (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1t4aug1/building_a_secondary_research_pipeline_for_my/)**
*  **Summary:** The discussion revolves around a research pipeline that uses LLMs for secondary research from old newspapers. A concern is raised about the reliability of LLMs reviewing other LLMs, with a suggestion for human review.
*  **Emotion:** Neutral, with a note of caution.
*  **Top 3 Points of View:**
    *   Skepticism about the reliability of an LLM reviewing another LLM's output for research purposes.
    *   A suggestion to use the secondary LLM to prompt the user for manual review of the data before it is finalized in the database.
    *   The user is building a pipeline for an urbanization thesis using historical newspaper data.
