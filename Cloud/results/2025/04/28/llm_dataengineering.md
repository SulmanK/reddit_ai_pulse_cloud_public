---
title: "Data Engineering Subreddit"
date: "2025-04-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "pyspark", "ETL"]
---

# Overall Ranking and Top Discussions
1.  [Several unavoidable for loops are slowing this PySpark code. Is it possible to improve it?](https://i.redd.it/jyf7vzym3lxe1.png) (Score: 34)
    *   Discussion on optimizing PySpark code that is slowed down by unavoidable for loops.
2.  [How are things hosted IRL?](https://www.reddit.com/r/dataengineering/comments/1k9s354/how_are_things_hosted_irl/) (Score: 23)
    *   Users discussed various hosting methods, including Docker on VMs, managed VMs, EC2 + Docker, and managed services like Kubernetes.
3.  [Is Starting as a Data Engineer a Good Path to Become an ML Engineer Later?](https://www.reddit.com/r/dataengineering/comments/1k9t0ms/is_starting_as_a_data_engineer_a_good_path_to/) (Score: 17)
    *   Discussion on whether a data engineering role is a good starting point for becoming an ML engineer, comparing skillsets and career paths.
4.  [dbt MCP Server – Bringing Structured Data to AI Workflows and Agents](https://docs.getdbt.com/blog/introducing-dbt-mcp-server) (Score: 16)
    *   Discussion on using dbt MCP Server to bring structured data to AI workflows and agents, with a user sharing their experience of using dlt schemas with GPT for creating enterprise bus matrices.
5.  [How well positioned am I to enter the Data Engineering job market? Where can I improve?](https://www.reddit.com/r/dataengineering/comments/1k9zpb0/how_well_positioned_am_i_to_enter_the_data/) (Score: 6)
    *   Users shared their experiences with the Data Engineering job market, they also advised to solve Python Leetcode problems.
6.  [Open source orchestration or workflow platforms with native NATS support](https://www.reddit.com/r/dataengineering/comments/1k9x46i/open_source_orchestration_or_workflow_platforms/) (Score: 3)
    *   Discussion about open-source orchestration or workflow platforms with native NATS support.
7.  [How do I get out of consulting?](https://www.reddit.com/r/dataengineering/comments/1k9zbyh/how_do_i_get_out_of_consulting/) (Score: 3)
    *   Discussion on getting out of consulting and landing an in-house Data Engineer role, focusing on the relevance of consulting experience.
8.  [Iam looking for opnions about my edited dashboard](https://www.reddit.com/gallery/1k9y4zj) (Score: 2)
    *   Users provided feedback and suggestions on an edited dashboard design, covering aspects like color contrast, chart types, and functionality.
9.  [Handling really inefficient partitioning](https://www.reddit.com/r/dataengineering/comments/1k9xbqo/handling_really_inefficient_partitioning/) (Score: 2)
    *   Discussion about handling inefficient partitioning in Polars, seeking advice on how to optimize memory usage and processing.
10. [Doubt about the coexistence of different partitioning methods](https://www.reddit.com/r/dataengineering/comments/1ka3a7b/doubt_about_the_coexistence_of_different/) (Score: 2)
    *   Discussion about coexistence of different partitioning methods.
11. [27 Databases and same Model - ETL](https://www.reddit.com/r/dataengineering/comments/1k9tgkq/27_databases_and_same_model_etl/) (Score: 1)
    *   Discussion on how to handle ETL processes for 27 databases with the same schema, with suggestions for using a single parameterized DAG.
12. [How can I set up metastore on K8s cluster?](https://www.reddit.com/r/dataengineering/comments/1k9txeg/how_can_i_set_up_metastore_on_k8s_cluster/) (Score: 1)
    *   The bot links learning resources for how to set up metastore on a K8s cluster.
13. [Beginner question: I am often stuck but I am not sure what knowledge gap I am lacking](https://www.reddit.com/r/dataengineering/comments/1k9nkwm/beginner_question_i_am_often_stuck_but_i_am_not/) (Score: 0)
    *   A beginner asks for advice on overcoming knowledge gaps in data engineering, seeking guidance on building, scaling, and monitoring data pipelines.
14. [I am building an agentic Python coding copilot for data analysis and would like to hear your feedback](https://www.reddit.com/r/dataengineering/comments/1k9r4s6/i_am_building_an_agentic_python_coding_copilot/) (Score: 0)
    *   A user requests feedback on an agentic Python coding copilot for data analysis, sparking a discussion about the tool's potential user base.

# Detailed Analysis by Thread
**[Several unavoidable for loops are slowing this PySpark code. Is it possible to improve it? (Score: 34)](https://i.redd.it/jyf7vzym3lxe1.png)**
*   **Summary:** The thread discusses ways to optimize PySpark code that is slowed down by unavoidable for loops. Suggestions include using `select` or `selectExpr`, defining UDFs, avoiding multiple `withColumn` operations, and considering SQL-based solutions.
*   **Emotion:** The overall emotional tone is Neutral, with discussions focused on technical solutions and advice.
*   **Top 3 Points of View:**
    *   Multiple `withColumn` operations significantly slow down Spark. Use `select` or `selectExpr` instead.
    *   Define a UDF that implements all mappings at once to avoid looping through individual mappings.
    *   Consider using SQL for better performance, and avoid creating full map columns just to select one key out of it.

**[How are things hosted IRL? (Score: 23)](https://www.reddit.com/r/dataengineering/comments/1k9s354/how_are_things_hosted_irl/)**
*   **Summary:** This thread discusses how data engineering infrastructure is hosted in real-world scenarios. Options range from Docker on VMs and managed VMs to more mature setups using Kubernetes and managed services from cloud providers.
*   **Emotion:** The emotional tone is generally Neutral, with a hint of Positive sentiment in responses thanking contributors.
*   **Top 3 Points of View:**
    *   Docker on VMs is a common starting point for hosting.
    *   More mature organizations use Kubernetes managed by dedicated infra teams.
    *   Managed services are increasingly popular, simplifying infrastructure management.

**[Is Starting as a Data Engineer a Good Path to Become an ML Engineer Later? (Score: 17)](https://www.reddit.com/r/dataengineering/comments/1k9t0ms/is_starting_as_a_data_engineer_a_good_path_to/)**
*   **Summary:** The discussion centers on whether starting as a data engineer is a viable path to becoming a machine learning engineer. Opinions diverge, with some suggesting that DE is a good foundation for MLE while others believe the roles require significantly different skill sets and a transition would be challenging.
*   **Emotion:** The overall sentiment is Neutral, with varied opinions and considerations being presented. Some comments lean towards Positive, highlighting the benefits of DE experience for MLE.
*   **Top 3 Points of View:**
    *   DE provides a good foundation for MLE as it allows you to handle data pipelines independently.
    *   The transition can be challenging due to the different skill sets required, with MLE being closer to SWE or Data Science.
    *   Many companies oversell DE roles, and a Data Warehouse Developer might be more suitable for some environments.

**[dbt MCP Server – Bringing Structured Data to AI Workflows and Agents (Score: 16)](https://docs.getdbt.com/blog/introducing-dbt-mcp-server)**
*   **Summary:** This thread is about the introduction of dbt MCP Server and its role in bringing structured data to AI workflows and agents. One user shared their experience using dlt schemas with GPT.
*   **Emotion:** The overall emotional tone is Positive due to the enthusiasm about the new tool.
*   **Top 3 Points of View:**
    *   dbt MCP Server is a good tool for bringing structured data to AI workflows.
    *   Modelling raw data with dlt schemas and GPT can be effective for creating enterprise bus matrices.

**[How well positioned am I to enter the Data Engineering job market? Where can I improve? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k9zpb0/how_well_positioned_am_i_to_enter_the_data/)**
*   **Summary:** The thread discusses how well-positioned someone is to enter the Data Engineering job market and where they can improve. Suggestions include focusing on Leetcode Python problems, adding DBT projects to the resume, and emphasizing experience with distributed systems like Spark.
*   **Emotion:** The overall emotional tone is Neutral, with comments offering practical advice. There are also hints of a Positive tone when encouraging the poster.
*   **Top 3 Points of View:**
    *   Focus on Leetcode Python problems.
    *   Add DBT projects to the resume.
    *   Emphasize experience with distributed systems like Spark.

**[Open source orchestration or workflow platforms with native NATS support (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k9x46i/open_source_orchestration_or_workflow_platforms/)**
*   **Summary:** The thread seeks recommendations for open-source orchestration or workflow platforms that natively support NATS. The comments mention Temporal and Kestra, discussing their integration and capabilities.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Temporal can be integrated with NATS using its SDK.
    *   Kestra provides straightforward YAML configuration for event-driven workflows with NATS.
    *   The uncertainty surrounding NATS' OSS status highlights the importance of flexible platform options.

**[How do I get out of consulting? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k9zbyh/how_do_i_get_out_of_consulting/)**
*   **Summary:** The thread is about a data engineer with 3 YoE in the US seeking advice on transitioning from consulting to an in-house DE role.
*   **Emotion:** The overall emotional tone is Positive.
*   **Top 3 Points of View:**
    *   There is no difference between consulting experience and an "inhouse" position.
    *   Consulting experience is valuable and demonstrates the ability to quickly adapt to new environments.
    *   Apply for jobs at non-consulting firms and back yourself.

**[Iam looking for opnions about my edited dashboard (Score: 2)](https://www.reddit.com/gallery/1k9y4zj)**
*   **Summary:** The thread is for getting opinions about the edited dashboard. Commenters gave feedback on readability, design, and functionality.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The black text on the blue background is hard to read.
    *   Pie graphs should be avoided.
    *   Consider using Python for dashboard creation instead of Power BI.

**[Handling really inefficient partitioning (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k9xbqo/handling_really_inefficient_partitioning/)**
*   **Summary:** This thread discusses the handling of inefficient partitioning. Users offer suggestions, asking for more details about the input data and process, and recommending processing in chunks.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Process the data in chunks to control memory usage.
    *   Investigate if a skew problem is causing the inefficiency.
    *   Avoid reading all partitions into memory simultaneously.

**[Doubt about the coexistence of different partitioning methods (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ka3a7b/doubt_about_the_coexistence_of_different/)**
*   **Summary:** The thread revolves around a doubt about the coexistence of different partitioning methods.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Partition has order.
    *   Partition represents how the lookup will be executed.

**[27 Databases and same Model - ETL (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k9tgkq/27_databases_and_same_model_etl/)**
*   **Summary:** The thread discusses how to handle ETL processes for 27 databases with the same schema. The advice centers on using a single parameterized DAG for efficiency and maintainability.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Use a single parameterized DAG instead of creating 27 separate DAGs.
    *   Create a config file with all 27 database connection details.
    *   Structure the pipeline to handle each database dynamically and potentially fetch credentials from a secrets manager.

**[How can I set up metastore on K8s cluster? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k9txeg/how_can_i_set_up_metastore_on_k8s_cluster/)**
*   **Summary:** This thread is a question about setting up a metastore on a K8s cluster. The bot provides links to learning resources.
*   **Emotion:** The overall emotional tone is Neutral.

**[Beginner question: I am often stuck but I am not sure what knowledge gap I am lacking (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k9nkwm/beginner_question_i_am_often_stuck_but_i_am_not/)**
*   **Summary:** A beginner asks for advice on overcoming knowledge gaps in data engineering. Commenters provide guidance on building, scaling, and monitoring data pipelines.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Build a POC to ensure it works.
    *   Consider scalability and future requirements.
    *   Optimize the pipeline for performance and maintainability.

**[I am building an agentic Python coding copilot for data analysis and would like to hear your feedback (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k9r4s6/i_am_building_an_agentic_python_coding_copilot/)**
*   **Summary:** A user requests feedback on an agentic Python coding copilot for data analysis. The comments question the tool's target audience.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Organizations that use agentic tools generally don't want or need to see the code.
    *   The tool might be useful as an educational resource for those learning to code.

