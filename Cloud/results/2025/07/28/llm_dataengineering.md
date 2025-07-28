---
title: "Data Engineering Subreddit"
date: "2025-07-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1. [[D] How to automate data quality](https://www.reddit.com/r/dataengineering/comments/1mbap0p/how_to_automate_data_quality/) (Score: 13)
    * Discusses methods and tools for automating data quality checks in data pipelines, including using dbt, SQLMesh, and open-source tools like Great Expectations and Soda.
2. [Upskill from Power BI to Data Engineering/Data Architecture](https://www.reddit.com/r/dataengineering/comments/1mb9y5s/upskill_from_power_bi_to_data_engineeringdata/) (Score: 10)
    *  Discusses how to transition from Power BI to data engineering/data architecture, suggesting creating a project using publicly available datasets and building a Power BI report.
3. [Data Governance on pause and breach on play: McHire’s Data Spill](https://www.reddit.com/r/dataengineering/comments/1mbgri9/data_governance_on_pause_and_breach_on_play/) (Score: 9)
    * Discusses a data breach and the importance of data governance, with some comments about AI.
4. [event-driven or real-time streaming?](https://www.reddit.com/r/dataengineering/comments/1mbgihi/eventdriven_or_realtime_streaming/) (Score: 6)
    *  Presents a blog post on designing analytics stacks with streaming and event-driven architecture.
5. [Grafana DE Pipeline Board](https://www.reddit.com/r/dataengineering/comments/1mbiio9/grafana_de_pipeline_board/) (Score: 6)
    *  Discusses the idea of a unified Grafana dashboard for Dagster metrics and Snowflake costs, and the implementation using Grafana with Dagster's GraphQL API and Snowflake's `ACCOUNT_USAGE` schema.
6. [Dreaming of Graphs in the Open Lakehouse](https://semyonsinchenko.github.io/ssinchenko/post/dreams-about-graph-in-lakehouse/) (Score: 4)
    * Discusses challenges with RDF Graphs and Property Graphs.
7. [[RFC] Type-safe dataframes](https://www.reddit.com/r/dataengineering/comments/1mbaky4/rfc_typesafe_dataframes/) (Score: 3)
    *  Links to a showcase of open-source projects and a form for submitting projects to be featured.
8. [Quick demo DB setup for private projects and learning](https://www.reddit.com/r/dataengineering/comments/1mbftbx/quick_demo_db_setup_for_private_projects_and/) (Score: 3)
    *  Links to a list of community-submitted learning resources.
9. [Best practices for processing real-time IoT data at scale?](https://www.reddit.com/r/dataengineering/comments/1mbgjpf/best_practices_for_processing_realtime_iot_data/) (Score: 2)
    *  Discusses best practices for processing real-time IoT data at scale, mentioning AWS Kinesis, Azure IoT, Flink, and Kafka.
10. [Football result prediction](https://www.reddit.com/r/dataengineering/comments/1mbj1p9/football_result_prediction/) (Score: 2)
    *  Discusses the idea of using data engineering for football result prediction as a learning project.
11. [Need Doubt Clearing on Azure Data Engineering](https://www.reddit.com/r/dataengineering/comments/1mbl92t/need_doubt_clearing_on_azure_data_engineering/) (Score: 2)
    * Mentions paid mentorship for people wanting to clear doubts on Azure Data Engineering
12. [How do I upgrade dbt-core/dbt-snowflake to get the latest snapshot schema evolution fix?](https://www.reddit.com/r/dataengineering/comments/1mbkmli/how_do_i_upgrade_dbtcoredbtsnowflake_to_get_the/) (Score: 1)
    *  Advises checking for a release to pypi including the change and reviewing the release notes/log section on their GitHub repos.
13. [Landed opportunity with Perplexity.. here's how I did it](https://i.redd.it/b05vb6bgvnff1.png) (Score: 0)
    *  Congratulates someone on landing a job opportunity with Perplexity and asks about their tech stack and educational background.
14. [Switching Career Paths: DevOps vs Cloud Data Engineering – Need Advice](https://www.reddit.com/r/dataengineering/comments/1mbboz7/switching_career_paths_devops_vs_cloud_data/) (Score: 0)
    *  Discusses switching career paths from SAP to DevOps or Cloud Data Engineering, with advice on work-life balance and company culture.
15. [Is proposing myself for an internship the right move?](https://www.reddit.com/r/dataengineering/comments/1mbihny/is_proposing_myself_for_an_internship_the_right/) (Score: 0)
    *  Discusses whether proposing oneself for an internship is a good idea, advising against tying oneself too much to any one company.
16. [Engineering managers / tech leads - what’s missing from your current dev workflow/management tools?](https://www.reddit.com/r/dataengineering/comments/1mbn89b/engineering_managers_tech_leads_whats_missing/) (Score: 0)
    *  Asks engineering managers and tech leads what's missing from their current dev workflow/management tools.

# Detailed Analysis by Thread
**[[D] How to automate data quality (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1mbap0p/how_to_automate_data_quality/)**
*  **Summary:**  The thread discusses automating data quality checks in data pipelines.  Suggestions include moving data through bronze, silver, and gold tables; using dbt for testing; and exploring tools like Great Expectations, Soda, and AWS Deequ.  An intern is advised to consult with their mentor for engine selection.
*  **Emotion:** The emotional tone of the thread is overwhelmingly Neutral, reflecting informational and technical discussions.
*  **Top 3 Points of View:**
    *   As an intern, consult with your mentor on ETL engine selection.
    *   Automate data quality during the transition from bronze to silver tables in a data pipeline.
    *   Consider using dbt, SQLMesh, Great Expectations, or Soda for data quality automation.

**[Upskill from Power BI to Data Engineering/Data Architecture (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1mb9y5s/upskill_from_power_bi_to_data_engineeringdata/)**
*  **Summary:** The thread centers around how to transition from Power BI to data engineering or data architecture roles.  Participants suggest building personal projects using publicly available datasets and showcasing the results in a Power BI report.
*  **Emotion:** The emotional tone of the thread is Neutral, reflecting helpful and practical advice.
*  **Top 3 Points of View:**
    *   Create a project using publicly available datasets and showcase it with a Power BI report.
    *   Refer to the community-submitted learning resources available on the Data Engineering Wiki.
    *   Focus on understanding the non-aggregated data sources used in Power BI reports to scope a data engineering learning project.

**[Data Governance on pause and breach on play: McHire’s Data Spill (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1mbgri9/data_governance_on_pause_and_breach_on_play/)**
*  **Summary:** The thread discusses a data breach incident and the importance of data governance. It touches on the lack of gatekeepers for AI.
*  **Emotion:** The emotional tone is mixed, with both Positive and Negative sentiments detected, reflecting concern about the breach and security.
*  **Top 3 Points of View:**
    *   Simple password combinations are still a problem.
    *   Staying on the right side of data ethics is crucial.
    *   The situation will worsen because there are no gatekeepers for AI.

**[event-driven or real-time streaming? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mbgihi/eventdriven_or_realtime_streaming/)**
*  **Summary:** The thread shares a blog post about designing analytics stacks with streaming and event-driven architecture.
*  **Emotion:** The emotional tone is Neutral, reflecting the sharing of informational content.
*  **Top 1 Points of View:**
    *   The blog post provides insights into designing analytics stacks with streaming and event-driven architecture.

**[Grafana DE Pipeline Board (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mbiio9/grafana_de_pipeline_board/)**
*  **Summary:** The thread discusses the idea of creating a unified Grafana dashboard for Dagster metrics and Snowflake costs. The implementation involves using Grafana with Dagster's GraphQL API and Snowflake's `ACCOUNT_USAGE` schema.
*  **Emotion:** The emotional tone of the thread is Positive, reflecting enthusiasm for the idea.
*  **Top 1 Points of View:**
    *  A unified dashboard for Dagster metrics and Snowflake costs is a valuable tool and not overkill.

**[Dreaming of Graphs in the Open Lakehouse (Score: 4)](https://semyonsinchenko.github.io/ssinchenko/post/dreams-about-graph-in-lakehouse/)**
*  **Summary:** The thread discusses issues with RDF Graphs and Property Graphs, suggesting hypergraphs as a related concept.
*  **Emotion:** The emotional tone is Neutral, reflecting a technical discussion of graph technologies.
*  **Top 3 Points of View:**
    *   There are compatibility issues between RDF Graphs and Property Graphs.
    *   Consider using hypergraphs or related technologies.
    *   Schema languages for property graphs is another issue.

**[[RFC] Type-safe dataframes (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mbaky4/rfc_typesafe_dataframes/)**
*  **Summary:** The thread provides links to a community project showcase and a form for submitting projects.
*  **Emotion:** The emotional tone is Neutral, reflecting the sharing of informational links.
*  **Top 1 Points of View:**
    *   The Data Engineering Wiki hosts a showcase of open-source projects.

**[Quick demo DB setup for private projects and learning (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mbftbx/quick_demo_db_setup_for_private_projects_and/)**
*  **Summary:** The thread links to a list of community-submitted learning resources.
*  **Emotion:** The emotional tone is Neutral, reflecting the sharing of informational links.
*  **Top 1 Points of View:**
    *  The Data Engineering Wiki provides a list of community-submitted learning resources.

**[Best practices for processing real-time IoT data at scale? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mbgjpf/best_practices_for_processing_realtime_iot_data/)**
*  **Summary:** The thread discusses best practices for processing real-time IoT data at scale, mentioning tools like AWS Kinesis, Azure IoT, Flink, and Kafka. The relevance of real-time analytics is also questioned.
*  **Emotion:** The emotional tone of the thread is Neutral.
*  **Top 3 Points of View:**
    *   AWS Kinesis can be used to process real-time IoT data.
    *   Azure IoT is suitable for small teams and projects.
    *   Consider whether real-time analytics is actually necessary for the use case.

**[Football result prediction (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mbj1p9/football_result_prediction/)**
*  **Summary:**  The thread discusses using data engineering for football result prediction as a learning project.  It questions if models will work in crashing the betting industry and recommends focusing on dataset granularity.
*  **Emotion:** The emotional tone of the thread is slightly Positive.
*  **Top 3 Points of View:**
    *   Football result prediction is a nice learning project.
    *   The dataset should have xG metrics for better prediction.
    *   The accuracy for betting is very unpredictable.

**[Need Doubt Clearing on Azure Data Engineering (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mbl92t/need_doubt_clearing_on_azure_data_engineering/)**
*  **Summary:** A thread from someone who has some doubts and someone offering paid mentorship in this area.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 1 Points of View:**
    *   The user is offering paid mentorship for Azure Data Engineering.

**[How do I upgrade dbt-core/dbt-snowflake to get the latest snapshot schema evolution fix? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mbkmli/how_do_i_upgrade_dbtcoredbtsnowflake_to_get_the/)**
*  **Summary:** The thread suggests checking for a new release on pypi and reviewing the GitHub release notes/log.
*  **Emotion:** The emotional tone is Neutral, providing practical advice.
*  **Top 1 Points of View:**
    *   Check the release notes on GitHub or PyPi.

**[Landed opportunity with Perplexity.. here's how I did it (Score: 0)](https://i.redd.it/b05vb6bgvnff1.png)**
*  **Summary:** Congratulatory and inquisitive comments regarding a new job at Perplexity.
*  **Emotion:** The emotional tone of the thread is primarily Positive, consisting of congratulations and well wishes.
*  **Top 3 Points of View:**
    *   Congratulations on landing the opportunity.
    *   Inquiries about the tech stack used in the role.
    *   Questions about educational background and its relevance to similar roles.

**[Switching Career Paths: DevOps vs Cloud Data Engineering – Need Advice (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mbboz7/switching_career_paths_devops_vs_cloud_data/)**
*  **Summary:** The thread discusses whether someone should switch career paths from SAP to either DevOps or Cloud Data Engineering.
*  **Emotion:** The emotional tone is Neutral, providing advice.
*  **Top 3 Points of View:**
    *   DevOps roles may have a poorer work/life balance.
    *   SAP is a more stable career path.
    *   The Data Engineering Wiki contains learning resources.

**[Is proposing myself for an internship the right move? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mbihny/is_proposing_myself_for_an_internship_the_right/)**
*  **Summary:**  Discusses the strategy of creating a proposal for an internship versus submitting a standard application.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 1 Points of View:**
    *   Apply to multiple companies rather than focusing on one.

**[Engineering managers / tech leads - what’s missing from your current dev workflow/management tools? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mbn89b/engineering_managers_tech_leads_whats_missing/)**
*  **Summary:**  Thread asking engineering managers for feedback on what tools they may want or need in the future.
*  **Emotion:** The emotional tone is mixed, mostly positive.
*  **Top 3 Points of View:**
    *   Tool for 1:1, allowing notes and reminders.
    *   Dislikes measuring work, prefer to measure outcome and usage.
    *   The Org is considering leaving Atlassian.
