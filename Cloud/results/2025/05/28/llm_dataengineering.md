---
title: "Data Engineering Subreddit"
date: "2025-05-28"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "dbt", "lakehouse"]
---

# Overall Ranking and Top Discussions
1.  [Duckberg - The rise of medium sized data.](https://medium.com/@trew.josh/duckberg-e310d9541bf2) (Score: 60)
    * Discusses using DuckDB and Iceberg to solve medium data problems without the bloat of Spark.
2.  [dbt Labs' new VSCode extension has a 15 account cap for companies don't don't pay up](https://www.getdbt.com/dbt-assets/vscode-plugin-aup) (Score: 49)
    *  Concerns dbt Labs' new VSCode extension which has a 15 account cap.
3.  [Decentralized compute for AI is starting to feel less like a dream and more like a necessity](https://www.reddit.com/r/dataengineering/comments/1kxmcb2/decentralized_compute_for_ai_is_starting_to_feel/) (Score: 22)
    * The feasibility and challenges of using decentralized computing for AI, especially with proprietary data.
4.  [Meet the dbt Fusion Engine: the new Rust-based, industrial-grade engine for dbt](https://docs.getdbt.com/blog/dbt-fusion-engine) (Score: 19)
    * Introducing the new Rust-based, industrial-grade engine for dbt.
5.  [Data Engineering Design Patterns by Bartosz Konieczny](https://www.reddit.com/r/dataengineering/comments/1kxfi6c/data_engineering_design_patterns_by_bartosz/) (Score: 8)
    *  Links to community-submitted learning resources for data engineering design patterns.
6.  [Data Migration in Modernization Projects Still Feels Broken — How Are You Solving Governance & Validation?](https://www.reddit.com/r/dataengineering/comments/1kxe0l5/data_migration_in_modernization_projects_still/) (Score: 7)
    * Discusses the challenges of data migration in modernization projects, focusing on governance and validation.
7.  [How many of you succeed to bring RAG to your company for internal Analysis?](https://www.reddit.com/r/dataengineering/comments/1kxeg0i/how_many_of_you_succeed_to_bring_rag_to_your/) (Score: 7)
    * Experiences of implementing Retrieval Augmented Generation (RAG) for internal data analysis.
8.  [dbt-like features but including Python?](https://www.reddit.com/r/dataengineering/comments/1kxnzb8/dbtlike_features_but_including_python/) (Score: 7)
    * Discussion on tools that provide dbt-like features but also include Python support.
9. [Ducklake with dbt or sqlmesh](https://www.reddit.com/r/dataengineering/comments/1kxg3xs/ducklake_with_dbt_or_sqlmesh/) (Score: 6)
    * Debating whether to use dbt or SQLMesh for Ducklake.
10. [Transitioning from Data Engineering to DataOps — Worth It?](https://www.reddit.com/r/dataengineering/comments/1kxkzvs/transitioning_from_data_engineering_to_dataops/) (Score: 5)
    * Whether or not transitioning from Data Engineering to DataOps is worth it.
11. [Sql notebooks?](https://www.reddit.com/r/dataengineering/comments/1kxo89k/sql_notebooks/) (Score: 3)
    * Discussion on SQL Notebooks.
12. [How do you balance the demands of "Nested & Repeating" schema while keeping query execution costs low? I am facing a dilemma where I want to use "Nested & Repeating" schema, but I should also consider using partitioning and clustering to make my query executions more cost-effective.](https://www.reddit.com/r/dataengineering/comments/1kxgb8j/how_do_you_balance_the_demands_of_nested/) (Score: 1)
    * Discussion on balancing nested schema demands with query execution costs, considering partitioning and clustering.
13. [Introducing DEtermined: The Open Resource for Data Engineering Mastery](https://www.reddit.com/r/dataengineering/comments/1kxqzcx/introducing_determined_the_open_resource_for_data/) (Score: 1)
    * Links to community-submitted learning resources for data engineering.
14. [Beyond the Buzzword: What Lakehouse Actually Means for Your Business](https://www.databend.com/blog/category-product/databend-lakehouse) (Score: 0)
    * Meaning of Lakehouse for Business.
15. [Everyone’s talking about LLMs — but the real power comes when you pair them with structured and semantic search.](https://www.reddit.com/r/dataengineering/comments/1kxf2ip/everyones_talking_about_llms_but_the_real_power/) (Score: 0)
    * The real power comes when you pair them with structured and semantic search.

# Detailed Analysis by Thread
**[Duckberg - The rise of medium sized data. (Score: 60)](https://medium.com/@trew.josh/duckberg-e310d9541bf2)**
*  **Summary:** Discusses using DuckDB and Iceberg to solve medium data problems without the bloat of Spark. People discuss how to define medium data, data compaction, rewriting, and what to do about Python and DuckDB knowledge.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * DuckDB + Iceberg is a simple solution for medium data without Spark's complexity.
    * Defining "medium" data is essential.
    * Handling data compaction and rewriting is a concern.

**[dbt Labs' new VSCode extension has a 15 account cap for companies don't don't pay up (Score: 49)](https://www.getdbt.com/dbt-assets/vscode-plugin-aup)**
*  **Summary:** Concerns dbt Labs' new VSCode extension which has a 15 account cap. People are recommending alternatives like SQLMesh and Power User for dbt.
*  **Emotion:** Neutral, with a hint of Positive sentiment in one comment indicating excitement initially but disappointment with the account cap.
*  **Top 3 Points of View:**
    * The 15-account limit is a significant drawback.
    * Alternatives like Power User for dbt and SQLMesh are viable options.
    * This limitation is expected since they need to make money from some products.

**[Decentralized compute for AI is starting to feel less like a dream and more like a necessity (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1kxmcb2/decentralized_compute_for_ai_is_starting_to_feel/)**
*  **Summary:** The feasibility and challenges of using decentralized computing for AI, especially with proprietary data.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    * Decentralized compute works well for training models on public datasets.
    * Data privacy and corporate policies often prevent its use with proprietary data.
    * Similar to Foldingathome.org

**[Meet the dbt Fusion Engine: the new Rust-based, industrial-grade engine for dbt (Score: 19)](https://docs.getdbt.com/blog/dbt-fusion-engine)**
*  **Summary:** Introducing the new Rust-based, industrial-grade engine for dbt. People have questions regarding orchestration time, FedRAMP, and whether VS code extension and fusion will stay free.
*  **Emotion:** Neutral, with a bit of Positive sentiment due to excitement.
*  **Top 3 Points of View:**
    * Concerns about whether orchestration time is an actual issue.
    * Questions about what path exists for organizations that exclusively use Core and are fedRAMP moderate in Snowflake.
    * Will the VS code extension and fusion stay free for < 15 devs over time ?

**[Data Engineering Design Patterns by Bartosz Konieczny (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1kxfi6c/data_engineering_design_patterns_by_bartosz/)**
*  **Summary:** Links to community-submitted learning resources for data engineering design patterns.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * The post is just a bot providing a link to learning resources.

**[Data Migration in Modernization Projects Still Feels Broken — How Are You Solving Governance & Validation? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kxe0l5/data_migration_in_modernization_projects_still/)**
*  **Summary:** Discusses the challenges of data migration in modernization projects, focusing on governance and validation.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Speculating whether or not AI was used to write the article.
    * IT is supposed to move data from A to B automatically, but business users are the ones who should take responsibility.
    * The expectation is technology will solve all business problems.

**[How many of you succeed to bring RAG to your company for internal Analysis? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kxeg0i/how_many_of_you_succeed_to_bring_rag_to_your/)**
*  **Summary:** Experiences of implementing Retrieval Augmented Generation (RAG) for internal data analysis.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    * One user asks what RAG is.
    * RAG has helped teams get real-time, contextual insights from internal business data.
    * One organization has banned insights.

**[dbt-like features but including Python? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1kxnzb8/dbtlike_features_but_including_python/)**
*  **Summary:** Discussion on tools that provide dbt-like features but also include Python support.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    * Dagster has the smoothest integration with dbt compared to the alternative orchestrators.
    * dbt with an iceberg table allows you to build python models.
    * getbruin.com and SQL Mesh have an open source free version as well as a paid cloud version.

**[Ducklake with dbt or sqlmesh (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1kxg3xs/ducklake_with_dbt_or_sqlmesh/)**
*  **Summary:** Debating whether to use dbt or SQLMesh for Ducklake.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * dbt works with the normal duckdb extension
    * Use duck lake as a transactional staging layer and then query it to create a single parquet file in bronze that dbt can read.

**[Transitioning from Data Engineering to DataOps — Worth It? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1kxkzvs/transitioning_from_data_engineering_to_dataops/)**
*  **Summary:** Whether or not transitioning from Data Engineering to DataOps is worth it.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    * What are the differences between the roles?
    * The DE team handles all of the code delivery on the provided infras. The SRE team handles terraform deployment.
    * Find the job that allows you to do both, would be a great choice.

**[Sql notebooks? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1kxo89k/sql_notebooks/)**
*  **Summary:** Discussion on SQL Notebooks.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Checkout Hex
    * Marino might be what you need, uses duckdb to connect to postgres though, might want to use duckdb ui directly as well.

**[How do you balance the demands of "Nested & Repeating" schema while keeping query execution costs low? I am facing a dilemma where I want to use "Nested & Repeating" schema, but I should also consider using partitioning and clustering to make my query executions more cost-effective. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kxgb8j/how_do_you_balance_the_demands_of_nested/)**
*  **Summary:** Discussion on balancing nested schema demands with query execution costs, considering partitioning and clustering.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Partitioning is useful in BQ for incremental loading. Predicate fields are common and won't be repeated. View-specific tables can also be denormalized.
    * An OLAP DW is normally modelled as star schemas so you wouldn't use "nested and repeated" columns.
    * Denormalizing and using the complex types (Structs, Arrays) is a great way to use BigQuery effectively and efficiently.

**[Introducing DEtermined: The Open Resource for Data Engineering Mastery (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kxqzcx/introducing_determined_the_open_resource_for_data/)**
*  **Summary:** Links to community-submitted learning resources for data engineering.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * The post is just a bot providing a link to learning resources.

**[Beyond the Buzzword: What Lakehouse Actually Means for Your Business (Score: 0)](https://www.databend.com/blog/category-product/databend-lakehouse)**
*  **Summary:** Meaning of Lakehouse for Business.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Lakehouse is where you go to chill and get away from the troubles of the world!
    * The data lake I built handles metadata backup for a vector db with vector search and some finance stuff.
    * According to a Reddit post, lakehouses are a bad idea. In fact, they are great for their use cases. My current job has made a bad version of a lakehouse into a good one.

**[Everyone’s talking about LLMs — but the real power comes when you pair them with structured and semantic search. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kxf2ip/everyones_talking_about_llms_but_the_real_power/)**
*  **Summary:** The real power comes when you pair them with structured and semantic search.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    * A user says the post is just an advertisement.
    * Another users states: so.. RAG
    * A final user asks what the UI is.
