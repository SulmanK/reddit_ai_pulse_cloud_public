---
title: "Data Engineering Subreddit"
date: "2025-07-26"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Microsoft admits it 'cannot guarantee' data sovereignty -- "Under oath in French Senate, exec says it would be compelled – however unlikely – to pass local customer info to US admin"](https://www.theregister.com/2025/07/25/microsoft_admits_it_cannot_guarantee/) (Score: 155)
    *   Discussion revolves around Microsoft's admission regarding data sovereignty and the implications of the CLOUD Act and other related regulations.
2.  [Primary Keys: Am I crazy?](https://i.redd.it/meg7r48jr8ff1.jpeg) (Score: 36)
    *   The thread discusses the necessity and usage of primary keys in data warehouses, debating between surrogate keys, natural keys, and unique identifiers.
3.  [What is the need of a full refresh pipeline when you have an incremental pipeline that does everything](https://www.reddit.com/r/dataengineering/comments/1m9n3fz/what_is_the_need_of_a_full_refresh_pipeline_when/) (Score: 30)
    *   Discussion regarding the benefits and drawbacks of full refresh pipelines versus incremental pipelines, focusing on data accuracy, backfilling, and simplicity.
4.  [Modernizing our data stack, looking for practical advice](https://www.reddit.com/r/dataengineering/comments/1m9c42u/modernizing_our_data_stack_looking_for_practical/) (Score: 18)
    *   Users share advice and suggestions on modernizing a data stack, including tool recommendations, architecture considerations, and potential pitfalls.
5.  [Scalable solution for finding the path between collection of dynamic graphs](https://www.reddit.com/r/dataengineering/comments/1m9nc41/scalable_solution_for_finding_the_path_between/) (Score: 3)
    *   Discussion about finding a scalable solution for finding paths between nodes in dynamic graphs.
6.  [Data Quality Profiling/Reporting tools](https://www.reddit.com/r/dataengineering/comments/1m9nykt/data_quality_profilingreporting_tools/) (Score: 2)
    *   Inquiring about tools for data quality profiling and reporting.
7.  [Upskilling ideas](https://www.reddit.com/r/dataengineering/comments/1m9xtcn/upskilling_ideas/) (Score: 1)
    *   Advice is provided to look for a job with a preferred tool or explore existing company resources for projects.
8.  [App Integrations and the Data Lake](https://www.reddit.com/r/dataengineering/comments/1ma19ck/app_integrations_and_the_data_lake/) (Score: 1)
    *   A bot provides a link to learning resources.
9.  [New repo to auto Create pandas Pipelines.](https://www.reddit.com/r/dataengineering/comments/1m9i8vq/new_repo_to_auto_create_pandas_pipelines/) (Score: 0)
    *   A bot provides a link to the open-source project showcase.

# Detailed Analysis by Thread
**[Microsoft admits it 'cannot guarantee' data sovereignty -- "Under oath in French Senate, exec says it would be compelled – however unlikely – to pass local customer info to US admin"](https://www.theregister.com/2025/07/25/microsoft_admits_it_cannot_guarantee/) (Score: 155)**
*  **Summary:** The thread discusses Microsoft's admission that it cannot guarantee data sovereignty due to the CLOUD Act and other related US regulations. Users are discussing the implications for businesses operating in the EU and the potential impact on cloud providers like Azure, AWS, and Google.
*  **Emotion:** The overall emotional tone is Neutral, with users primarily sharing information and opinions in a factual manner. There are some elements of concern and caution regarding the implications of the data sovereignty issue.
*  **Top 3 Points of View:**
    *   The CLOUD Act and related US regulations pose a significant challenge to data sovereignty for American companies operating internationally.
    *   Microsoft's admission is not new but a public acknowledgement of existing issues.
    *   The EU may take action that could impact Azure and other cloud providers.

**[Primary Keys: Am I crazy?](https://i.redd.it/meg7r48jr8ff1.jpeg) (Score: 36)**
*  **Summary:** The thread is about the use of primary keys in data warehousing. Some argue against strict primary key constraints due to performance concerns and the nature of data warehouses, while others advocate for unique identifiers and surrogate keys to ensure data integrity.
*  **Emotion:** The overall emotional tone is Neutral. There's some negative sentiment directed at the original post for what some consider an amateurish perspective.
*  **Top 3 Points of View:**
    *   Primary key constraints can be detrimental to performance in large-scale data warehouses.
    *   Unique identifiers and surrogate keys are essential for data integrity, even if formal primary key constraints are not used.
    *   The concept of DRY (Don't Repeat Yourself) may not always be applicable in data modeling.

**[What is the need of a full refresh pipeline when you have an incremental pipeline that does everything](https://www.reddit.com/r/dataengineering/comments/1m9n3fz/what_is_the_need_of_a_full_refresh_pipeline_when/) (Score: 30)**
*  **Summary:** The discussion explores the reasons for using full refresh pipelines despite having incremental pipelines. It highlights the simplicity of full refresh, its ability to handle changing business rules, and its utility in backfilling data or reprocessing historical data.
*  **Emotion:** The overall emotional tone is Neutral. Some positive sentiment towards tools like dbt, but it is mostly informational.
*  **Top 3 Points of View:**
    *   Full refresh pipelines offer simplicity and ease of maintenance compared to incremental pipelines.
    *   Full refresh is necessary for reprocessing historical data when business rules change or bugs are found.
    *   Incremental pipelines can drift away from the source over time, making full refresh a valuable check.

**[Modernizing our data stack, looking for practical advice](https://www.reddit.com/r/dataengineering/comments/1m9c42u/modernizing_our_data_stack_looking_for_practical/) (Score: 18)**
*  **Summary:** The thread consists of users providing advice on modernizing a data stack. Topics include the choice of ETL tools, the complexity of a data stack, and the benefits of different technologies.
*  **Emotion:** The overall emotional tone is Neutral. There are opinions given and options considered, but no strong emotion is expressed.
*  **Top 3 Points of View:**
    *   Simplicity is key; avoid unnecessary complexity by using only the tools needed for the job.
    *   Consider alternatives to "modern" technologies, as they may not always be superior.
    *   Ensure that existing dashboards continue to function during the modernization process.

**[Scalable solution for finding the path between collection of dynamic graphs](https://www.reddit.com/r/dataengineering/comments/1m9nc41/scalable_solution_for_finding_the_path_between/) (Score: 3)**
*  **Summary:** The thread explores scalable solutions for finding the path between nodes in dynamic graphs. Users recommend using GraphX or a graph database like Neo4j for computing the shortest path, depending on whether the task is sporadic or requires computing the shortest path between all nodes.
*  **Emotion:** The overall emotional tone is Neutral. The sentiment scores of the comments are relatively high, but indicate general statements without strong emotion.
*  **Top 3 Points of View:**
    *   GraphX, the graph library of Spark, is a good solution for computing the shortest path between all nodes.
    *   For sporadic path computations between two given nodes, consider using a graph database like Neo4j.
    *  Try igraph

**[Data Quality Profiling/Reporting tools](https://www.reddit.com/r/dataengineering/comments/1m9nykt/data_quality_profilingreporting_tools/) (Score: 2)**
*  **Summary:** The thread is about data quality profiling and reporting tools. Informatica's data quality product supports most of what the user wants, but it's expensive and not available in any cheap/open source way.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Informatica's data quality product supports most of what the user wants.
    *   It is expensive and not available in any cheap/open source way.
    *   A very old resource of automatic profiling solution is aws amazon

**[Upskilling ideas](https://www.reddit.com/r/dataengineering/comments/1m9xtcn/upskilling_ideas/) (Score: 1)**
*  **Summary:** This thread involves users offering advice on upskilling. The consensus is that practical experience is the best approach, either through job opportunities or personal projects.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Experience is the best way to upskill.
    *   Look for job opportunities that involve desired tools.
    *   Consider exploring internal projects or addressing tech debt within your current company.

**[App Integrations and the Data Lake](https://www.reddit.com/r/dataengineering/comments/1ma19ck/app_integrations_and_the_data_lake/) (Score: 1)**
*  **Summary:** A bot provides a link to learning resources related to app integrations and data lakes.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Link to learning resources related to app integrations and data lakes.

**[New repo to auto Create pandas Pipelines.](https://www.reddit.com/r/dataengineering/comments/1m9i8vq/new_repo_to_auto_create_pandas_pipelines/) (Score: 0)**
*  **Summary:** A bot shares a link to the open-source project showcase.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Link to the open-source project showcase.
