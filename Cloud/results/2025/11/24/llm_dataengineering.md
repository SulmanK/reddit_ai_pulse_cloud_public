---
title: "Data Engineering Subreddit"
date: "2025-11-24"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Data Quality at Scale: Why Your Pipeline Needs More Than Green Checkmarks](https://medium.com/@kalluripradeep99/data-quality-at-scale-why-your-pipeline-needs-more-than-green-checkmarks-f3af3dbff8a4) (Score: 51)
    *   Discusses the importance of data quality monitoring beyond simple pipeline status checks, highlighting lessons learned from a $2M mistake due to undetected data issues.
2.  [What are the necessary skills and proficiency level required for a data engineer with 4+ years exp](https://www.reddit.com/r/dataengineering/comments/1p5ccrg/what_are_the_necessary_skills_and_proficiency/) (Score: 26)
    *   Asks about the necessary skills and proficiency level required for a data engineer with 4+ years of experience.
3.  [Spark executor pods keep dying on k8s help please](https://www.reddit.com/r/dataengineering/comments/1p55vlu/spark_executor_pods_keep_dying_on_k8s_help_please/) (Score: 13)
    *   Seeks help with Spark executor pods that keep dying on Kubernetes.
4.  [I Just Finished Building a Full App Store Database (1M+ Apps, 8M+ Store Pages, Nov 2025). Anyone Interested?](https://www.reddit.com/r/dataengineering/comments/1p5h18n/i_just_finished_building_a_full_app_store/) (Score: 12)
    *   Asks if anyone is interested in a full app store database with over 1 million apps and 8 million store pages.
5.  [Which File Format is Best?](https://www.reddit.com/r/dataengineering/comments/1p578y5/which_file_format_is_best/) (Score: 10)
    *   Discusses the best file formats for data engineering purposes.
6.  [What things to learn or must know next 2 year as Data Engineer ?](https://www.reddit.com/r/dataengineering/comments/1p5ar60/what_things_to_learn_or_must_know_next_2_year_as/) (Score: 9)
    *   Asks about the things to learn or must know in the next 2 years as a Data Engineer.
7.  [Why raw production context does not work for Spark ...anyone solved this?](https://www.reddit.com/r/dataengineering/comments/1p56eh6/why_raw_production_context_does_not_work_for/) (Score: 8)
    *   Discusses why raw production context doesn't work for Spark and seeks solutions.
8.  [Integrated Big Data from ClickHouse to PowerBI](https://www.reddit.com/r/dataengineering/comments/1p5asxs/integrated_big_data_from_clickhouse_to_powerbi/) (Score: 5)
    *   Discusses integrating big data from ClickHouse to PowerBI.
9.  [Anyone know how to get metadata of PowerBI Fabric?](https://www.reddit.com/r/dataengineering/comments/1p55y2n/anyone_know_how_to_get_metadata_of_powerbi_fabric/) (Score: 4)
    *   Seeks information on how to get metadata of PowerBI Fabric.
10. [I built an open source CLI tool that lets you query CSV and Excel files in plain English no SQL needed](https://www.reddit.com/r/dataengineering/comments/1p5judy/i_built_an_open_source_cli_tool_that_lets_you/) (Score: 4)
    *   The author presents an open-source CLI tool that lets you query CSV and Excel files in plain English, without needing SQL.
11. [Data Engineers Assemble - Stuck and need help!](https://www.reddit.com/r/dataengineering/comments/1p5fg1r/data_engineers_assemble_stuck_and_need_help/) (Score: 3)
    *   A Data Engineer is stuck and needs help.
12. [Is still worthy to learn informatica power center in 2026](https://www.reddit.com/r/dataengineering/comments/1p5dwp5/is_still_worthy_to_learn_informatica_power_center/) (Score: 2)
    *   Asks about the worthiness of learning Informatica PowerCenter in 2026.
13. [Migrating to Snowflake Semantic Views for Microsoft SSAS Cubes](https://www.reddit.com/r/dataengineering/comments/1p5m7sl/migrating_to_snowflake_semantic_views_for/) (Score: 2)
    *   Asks about migrating to Snowflake Semantic Views for Microsoft SSAS Cubes
14. [Skills required for 9Y experience](https://www.reddit.com/r/dataengineering/comments/1p5e0cm/skills_required_for_9y_experience/) (Score: 1)
    *   Asks about skills required for 9 years of experience in data engineering.
15. [What high-impact projects are you using to level up?](https://www.reddit.com/r/dataengineering/comments/1p5huc0/what_highimpact_projects_are_you_using_to_level_up/) (Score: 1)
    *   Asks about high-impact projects being used to level up data engineering skills.
16. [How to scale airflow 3?](https://www.reddit.com/r/dataengineering/comments/1p5pfs3/how_to_scale_airflow_3/) (Score: 1)
    *   Asks about how to scale airflow 3.
17. [What I need more for working in the Netherlands?](https://www.reddit.com/r/dataengineering/comments/1p5ptfy/what_i_need_more_for_working_in_the_netherlands/) (Score: 0)
    *   Asks about what's needed to work in the Netherlands.

# Detailed Analysis by Thread
**[Data Quality at Scale: Why Your Pipeline Needs More Than Green Checkmarks (Score: 51)](https://medium.com/@kalluripradeep99/data-quality-at-scale-why-your-pipeline-needs-more-than-green-checkmarks-f3af3dbff8a4)**
*  **Summary:** The article discusses the importance of data quality monitoring beyond simple pipeline status checks. It highlights lessons learned from a $2M mistake due to undetected data issues, such as silent schema changes and currency confusion.
*  **Emotion:** The overall emotional tone is positive, driven by users sharing insightful solutions and expressing enthusiasm for the topic of data quality.
*  **Top 3 Points of View:**
    *   Drift detection can catch silent schema changes and currency confusion. Tracking distributions over time and monitoring schema changes proactively are useful.
    *   Standard unique tests on customer ID, invoice ID, and invoice line item should catch double-counting issues. Dates should always be in ISO standard format (YYYY-MM-DD).
    *   The article may be generated by AI.

**[What are the necessary skills and proficiency level required for a data engineer with 4+ years exp (Score: 26)](https://www.reddit.com/r/dataengineering/comments/1p5ccrg/what_are_the_necessary_skills_and_proficiency/)**
*  **Summary:** The discussion revolves around the necessary skills and proficiency level for a data engineer with 4+ years of experience. Recommendations include building end-to-end projects, mastering SQL, and understanding Spark architecture.
*  **Emotion:** The overall emotional tone is neutral, with commenters providing factual advice and recommendations.
*  **Top 3 Points of View:**
    *   Build end-to-end, production-style projects to demonstrate design, execution, and troubleshooting skills. A CDC pipeline from SQL Server or MongoDB into Snowflake/Delta is suggested as a good example.
    *   Master SQL with window functions and be able to replicate queries in PySpark.
    *   Focus on SQL, Python, Spark architecture, and PySpark.

**[Spark executor pods keep dying on k8s help please (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1p55vlu/spark_executor_pods_keep_dying_on_k8s_help_please/)**
*  **Summary:** The thread discusses issues with Spark executor pods dying on Kubernetes. Suggested solutions include checking shuffle files, GC settings, data skew, and Spark Web UI.
*  **Emotion:** The overall emotional tone is neutral, with users providing technical suggestions and advice.
*  **Top 3 Points of View:**
    *   Check shuffle files and GC settings for memory fragmentation or spill. Scaling won't help until the underlying memory pressure is addressed.
    *   Increase GC frequency and turn the GC debug flag on.
    *   Check if data is skewed and leading to certain executors getting huge partitions.

**[I Just Finished Building a Full App Store Database (1M+ Apps, 8M+ Store Pages, Nov 2025). Anyone Interested? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1p5h18n/i_just_finished_building_a_full_app_store/)**
*  **Summary:** The author shares a completed project of building a full app store database and asks if anyone is interested. Discussions revolve around data confidence, historical snapshots, legality, and practical steps for query and distribution.
*  **Emotion:** The overall emotional tone is neutral, with users expressing curiosity and offering suggestions.
*  **Top 3 Points of View:**
    *   Confidence in the completeness of listings and the feasibility of monthly snapshots are key considerations.
    *   Ensure the database is legal.
    *   Prioritize a stable schema, precomputed aggregates, and a sane distribution path. Add covering indexes, precompute aggregates, and create an FTS5 virtual table.

**[Which File Format is Best? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1p578y5/which_file_format_is_best/)**
*  **Summary:** The thread discusses the best file formats for data engineering. The consensus is that Parquet is suitable for OLAP, while Avro is suitable for OLTP. Iceberg and Delta are also mentioned for ACID properties.
*  **Emotion:** The overall emotional tone is neutral, with users providing factual information.
*  **Top 3 Points of View:**
    *   Iceberg is generally a good choice, and JSON is fine for transferring raw CDC.
    *   Parquet is best for columnar databases (OLAP), while Avro is best for row-based storage (OLTP).
    *   Parquet, Iceberg, or Delta are good choices depending on needs.

**[What things to learn or must know next 2 year as Data Engineer ? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1p5ar60/what_things_to_learn_or_must_know_next_2_year_as/)**
*  **Summary:** The thread discusses what data engineers should learn in the next 2 years, with a focus on AI, system architecture, and continuous learning.
*  **Emotion:** The overall emotional tone is positive, with commenters emphasizing the importance of AI and continuous learning.
*  **Top 3 Points of View:**
    *   AI is important and should be utilized for varying needs.
    *   System/pipeline architecture and design are critical.
    *   Focus on learning how to get value out of LLMs and when to use scripting over AI.

**[Why raw production context does not work for Spark ...anyone solved this? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1p56eh6/why_raw_production_context_does_not_work_for/)**
*  **Summary:** The thread discusses why raw production context doesn't work for Spark and seeks solutions. Preprocessing, filtering, and using tools like Dataflint are suggested.
*  **Emotion:** The overall emotional tone is neutral, with users providing technical advice and suggestions.
*  **Top 3 Points of View:**
    *   Multi-stage preprocessing is better: filter irrelevant logs, compress plans intelligently, and aggregate metrics before feeding into Spark.
    *   Use Dataflint for a TLDR of the run with metrics that can be fed to an LLM.
    *   Set Spark's log level to WARN and parse the event log into a DataFrame to surface key metrics like spills, skew, and shuffle volume.

**[Integrated Big Data from ClickHouse to PowerBI (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p5asxs/integrated_big_data_from_clickhouse_to_powerbi/)**
*  **Summary:** The thread discusses integrating big data from ClickHouse to PowerBI, recommending avoiding live DirectQuery and optimizing ClickHouse SQL.
*  **Emotion:** The overall emotional tone is neutral, with users providing practical recommendations.
*  **Top 1 Points of View:**
    *   Avoid live DirectQuery to ClickHouse. If live querying is necessary, push the work into ClickHouse SQL and optimize Power BI side with query reduction and aggregations.

**[Anyone know how to get metadata of PowerBI Fabric? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p55y2n/anyone_know_how_to_get_metadata_of_powerbi_fabric/)**
*  **Summary:** The thread discusses how to get metadata of PowerBI Fabric, with recommendations to use REST APIs, log workspace analytics, and the FUAM framework.
*  **Emotion:** The overall emotional tone is neutral, with users providing technical advice and links to resources.
*  **Top 3 Points of View:**
    *   Use the Get Activity Events API.
    *   Use log workspace analytics.
    *   Check out the scanner API.

**[I built an open source CLI tool that lets you query CSV and Excel files in plain English no SQL needed (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1p5judy/i_built_an_open_source_cli_tool_that_lets_you/)**
*  **Summary:** The author presents an open-source CLI tool that lets you query CSV and Excel files in plain English, without needing SQL. Commenters raise concerns about data schema leaks and accuracy.
*  **Emotion:** The overall emotional tone is mixed, with users expressing interest but also raising concerns.
*  **Top 2 Points of View:**
    *   Sending data schemas to an API raises concerns about local processing.
    *   Potential data leaks from schema and lack of information about accuracy are major concerns.

**[Data Engineers Assemble - Stuck and need help! (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p5fg1r/data_engineers_assemble_stuck_and_need_help/)**
*  **Summary:** A Data Engineer is stuck and needs help! Discussions are around starting your own project or applying yourself to solving some of the "meta" that you currently have to deal with.
*  **Emotion:** The overall emotional tone is neutral
*  **Top 1 Points of View:**
    *   If you find yourself in a job that doesn't stretch you, start your own project or apply yourself to solving some of the "meta" that you currently have to deal with. Nobody will ever hand you a pre-packaged career that will always be interesting.

**[Is still worthy to learn informatica power center in 2026 (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p5dwp5/is_still_worthy_to_learn_informatica_power_center/)**
*  **Summary:** The thread questions the worthiness of learning Informatica PowerCenter in 2026. The consensus is that it's not a good investment due to the rise of modern tools like DBT.
*  **Emotion:** The overall emotional tone is neutral, with users discouraging the learning of Informatica PowerCenter.
*  **Top 3 Points of View:**
    *   It's time to run away whenever you see Informatica roles in 2026. Legacy tools are being replaced by modern tools like DBT.
    *   Learning a new ETL tool doesn't seem like a good investment unless you want to be involved in a lot of migration jobs.
    *   The best ETL platform in 2025 continues to be SSIS.

**[Migrating to Snowflake Semantic Views for Microsoft SSAS Cubes (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p5m7sl/migrating_to_snowflake_semantic_views_for/)**
*  **Summary:** Asks about migrating to Snowflake Semantic Views for Microsoft SSAS Cubes
*  **Emotion:** The overall emotional tone is neutral
*  **Top 1 Points of View:**
    *   In general, no query should include more than one fact table. Each fact table (and it's associated dimensions) should be queried individually and then the resultsets should be "assembled" into the final result - in your case Sigma should be doing this final part

**[Skills required for 9Y experience (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p5e0cm/skills_required_for_9y_experience/)**
*  **Summary:** The thread discusses the skills required for 9 years of experience in data engineering, recommending learning DBT, strengthening SQL, and mastering data modeling.
*  **Emotion:** The overall emotional tone is positive, offering encouragement and practical advice.
*  **Top 1 Points of View:**
    *   Focus on learning DBT, strengthening SQL skills, and mastering data modeling.

**[What high-impact projects are you using to level up? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p5huc0/what_highimpact_projects_are_you_using_to_level_up/)**
*  **Summary:** The thread discusses high-impact projects to level up data engineering skills, including rewriting services in Go, building end-to-end pipelines, and developing event-driven analytics platforms.
*  **Emotion:** The overall emotional tone is neutral, with users sharing their projects and recommendations.
*  **Top 3 Points of View:**
    *   Rewriting services in Go is a good way to level up.
    *   Building end-to-end pipelines with a nice report at the end would help to refresh tech skills.
    *   Build an event-driven analytics platform ingesting IoT data with AWS serverless.

**[How to scale airflow 3? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p5pfs3/how_to_scale_airflow_3/)**
*  **Summary:** Asks about how to scale airflow 3.
*  **Emotion:** The overall emotional tone is neutral
*  **Top 2 Points of View:**
    *   Just curious, what killer features of Airflow 3 made you consider it in favor of Airflow 2?
    *   Increasing the values for AIRFLOW\_\_DAG\_PROCESSOR\_\_DAG\_FILE\_PROCESSOR\_TIMEOUT, AIRFLOW\_\_DAG\_PROCESSOR\_\_REFRESH\_INTERVAL and AIRFLOW\_\_DAG\_PROCESSOR\_\_MIN\_FILE\_PROCESS\_INTERVAL might help scaling Airflow 3.

**[What I need more for working in the Netherlands? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p5ptfy/what_i_need_more_for_working_in_the_netherlands/)**
*  **Summary:** The thread discusses what's needed to work in the Netherlands, with a focus on visa sponsorship, gaining experience, and obtaining certifications.
*  **Emotion:** The overall emotional tone is neutral
*  **Top 3 Points of View:**
    *   Find a company that sponsors visa, likely only large companies. You have a better chance gaining working experience first in your own country, there is zero reason to hire a foreigner without experience.
    *   A company will take somebody who is alright and doesn't need a visa vs. somebody who is much better, but needs a visa.
    *   Focus on taking some official or semi official certifications to get some "papers" on what you can do.
