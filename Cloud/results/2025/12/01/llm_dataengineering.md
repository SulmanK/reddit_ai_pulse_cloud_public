---
title: "Data Engineering Subreddit"
date: "2025-12-01"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "kafka", "snowflake"]
---

# Overall Ranking and Top Discussions
1.  [[D] I spent 6 months fighting kafka for ml pipelines and finally rage quit the whole thing](https://www.reddit.com/r/dataengineering/comments/1pbiodi/i_spent_6_months_fighting_kafka_for_ml_pipelines/) (Score: 43)
    *   The thread discusses a user's negative experience with Kafka for ML pipelines, leading them to abandon it.
2.  [Snowflake](https://www.reddit.com/r/dataengineering/comments/1pbdunm/snowflake/) (Score: 19)
    *   This thread involves users providing advice and resources for learning Snowflake.
3.  [Facing issues with talend interface?](https://www.reddit.com/r/dataengineering/comments/1pbjx4j/facing_issues_with_talend_interface/) (Score: 2)
    *   Users discuss issues with the Talend interface and suggest alternative tools.
4.  [How to start???](https://www.reddit.com/r/dataengineering/comments/1pbanon/how_to_start/) (Score: 1)
    *   The thread is a question about how to get started in data engineering.
5.  [What is your max amount of data in one etl?](https://www.reddit.com/r/dataengineering/comments/1pbkqxq/what_is_your_max_amount_of_data_in_one_etl/) (Score: 0)
    *   The thread asks about the maximum amount of data processed in a single ETL job.
6.  ["Software Engineering" Structure vs. "Tool-Based" Structure , What does the industry actually use?](https://www.reddit.com/r/dataengineering/comments/1pbmo3x/software_engineering_structure_vs_toolbased/) (Score: 0)
    *   This thread discusses the differences between software engineering and tool-based approaches in data engineering.

# Detailed Analysis by Thread
**[[D] I spent 6 months fighting kafka for ml pipelines and finally rage quit the whole thing (Score: 43)](https://www.reddit.com/r/dataengineering/comments/1pbiodi/i_spent_6_months_fighting_kafka_for_ml_pipelines/)**
*   **Summary:** A user shares their frustrating experience using Kafka for ML pipelines, ultimately leading them to abandon it. Other users chime in with their own experiences, advice, and alternative solutions.
*   **Emotion:** The overall emotional tone is Neutral, with spikes of Positive sentiment where people agree with OP.
*   **Top 3 Points of View:**
    *   Kafka can be over-engineered for certain needs and not always the best solution.
    *   Kafka rebalancing does not lead to lost events, but rather processing slowdown, and systems should be designed to be idempotent.
    *   Alternatives to Kafka, like Synadia, exist and might be more suitable for multi-region scaling.

**[Snowflake (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1pbdunm/snowflake/)**
*   **Summary:** This thread provides advice and resources for learning Snowflake, covering topics like setting up small end-to-end projects, understanding key concepts (warehouses, stages, roles, pipes), and utilizing community resources.
*   **Emotion:** The overall emotional tone is Neutral, with some Positive sentiment due to providing helpful learning resources.
*   **Top 3 Points of View:**
    *   Start with a small end-to-end project to get familiar with loading, querying, and scheduling in Snowflake.
    *   Focus on understanding core Snowflake concepts like warehouses, stages, roles, and pipes.
    *   Utilize community-submitted learning resources and free workshops offered by Snowflake.

**[Facing issues with talend interface? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1pbjx4j/facing_issues_with_talend_interface/)**
*   **Summary:** Users discuss their problems with the Talend interface, with some suggesting alternatives and highlighting potential issues with the tool's stability and pricing after being acquired by a VC firm.
*   **Emotion:** The overall emotional tone is Neutral, however, the lowest sentiment score is negative.
*   **Top 3 Points of View:**
    *   Talend is a problematic tool, and users should consider alternatives like dbt or Bruin.
    *   Talend's pricing and stability have become concerns after being acquired by a VC firm.
    *   Code-based tools are better than drag-and-drop tools, like Talend.

**[How to start??? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1pbanon/how_to_start/)**
*   **Summary:** The thread acknowledges that the question of how to get started in data engineering is frequently asked and directs the user to available resources within the subreddit, such as the Wiki and search bar.
*   **Emotion:** The overall emotional tone is Positive due to providing resources.
*   **Top 3 Points of View:**
    *   This question is frequently asked.
    *   Resources are available in the subreddit Wiki and search bar.
    *   The dataengineering.wiki contains community submitted learning resources.

**[What is your max amount of data in one etl? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1pbkqxq/what_is_your_max_amount_of_data_in_one_etl/)**
*   **Summary:** The thread discusses the maximum amount of data processed in a single ETL job, with one user mentioning a 50 billion row table.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The ETL processed a 50 billion row wide table.
    *   Another user asks what kind of data is coming in.

**["Software Engineering" Structure vs. "Tool-Based" Structure , What does the industry actually use? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1pbmo3x/software_engineering_structure_vs_toolbased/)**
*   **Summary:** The thread discusses the differences between software engineering and tool-based approaches in data engineering, suggesting that most companies use a mix of both. Asset-based workflows are becoming more common.
*   **Emotion:** The overall emotional tone is Negative.
*   **Top 3 Points of View:**
    *   Companies typically mix software engineering and tool-based approaches.
    *   Asset-based workflows with tools like dbt, Dagster, and Bruin are becoming more common due to their clearer dependency graphs and easier debugging.
    *   A basic understanding of Python, Docker, and an orchestrator is sufficient for junior roles.
