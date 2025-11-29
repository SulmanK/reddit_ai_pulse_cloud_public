---
title: "Data Engineering Subreddit"
date: "2025-11-29"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "career", "tools"]
---

# Overall Ranking and Top Discussions
1.  [I messed up :(](https://www.reddit.com/r/dataengineering/comments/1p9k43o/i_messed_up/) (Score: 158)
    *   This thread discusses the common experience of making mistakes in data engineering and the importance of having backups.
2.  [Have you ever worked with a data source that required zero or low transformations?](https://www.reddit.com/r/dataengineering/comments/1p9e1xr/have_you_ever_worked_with_a_data_source_that/) (Score: 12)
    *   This thread explores the rare occurrence of working with data sources that require minimal or no transformations.
3.  [How to speed up AWS glue job to compact 500k parquet files?](https://www.reddit.com/r/dataengineering/comments/1p9puon/how_to_speed_up_aws_glue_job_to_compact_500k/) (Score: 11)
    *   This thread seeks advice on optimizing AWS Glue jobs for compacting a large number of Parquet files.
4.  [The current jobmarket is quite frustrating!](https://www.reddit.com/r/dataengineering/comments/1p9xi3l/the_current_jobmarket_is_quite_frustrating/) (Score: 10)
    *   This thread discusses the frustrations of the current job market for data engineers, particularly for those lacking experience with modern tech stacks.
5.  [How do you inspect actual Avro/Protobuf data or detect schema when debugging?](https://www.reddit.com/r/dataengineering/comments/1p9f4gp/how_do_you_inspect_actual_avroprotobuf_data_or/) (Score: 6)
    *   This thread asks about methods for inspecting Avro/Protobuf data and detecting schemas during debugging.
6.  [Is there a PySpark DataFrame validation library that automatically splits valid and invalid rows?](https://www.reddit.com/r/dataengineering/comments/1p9mg2x/is_there_a_pyspark_dataframe_validation_library/) (Score: 5)
    *   This thread seeks a PySpark DataFrame validation library for automatically separating valid and invalid rows.
7.  [I’m Informatica developer with some experience in databricks and pyspark as well currently searching job in data engineering field but not able to find any role permanent role in regular shift so planning do MS fabric certification..just wanted to if anyone done certification?](https://www.reddit.com/r/dataengineering/comments/1p9h03o/im_informatica_developer_with_some_experience_in/) (Score: 3)
    *   This thread discusses career advice for an Informatica developer transitioning to data engineering, including the value of MS Fabric certification.
8.  [How bad is the market? EU and US?](https://www.reddit.com/r/dataengineering/comments/1p9qmhr/how_bad_is_the_market_eu_and_us/) (Score: 3)
    *   This thread discusses the current state of the data engineering job market in the EU and US.
9.  [Confused about Git limitations in Databricks Repos — what do you do externally?](https://www.reddit.com/r/dataengineering/comments/1p9hrqu/confused_about_git_limitations_in_databricks/) (Score: 3)
    *   This thread discusses the limitations of Git integration within Databricks Repos and how to manage code externally.
10. [way of approaching](https://www.reddit.com/r/dataengineering/comments/1p9w6g9/way_of_approaching/) (Score: 3)
    *   This thread discusses different approaches in the data engineering field, particularly focusing on data platform engineering and the value of a "full stack" engineer.
11. [How is this Course](https://www.reddit.com/r/dataengineering/comments/1p9qlp8/how_is_this_course/) (Score: 2)
    *   This thread asks about a course.
12. [Is Hadoop, Hive, and Spark still Relevant?](https://www.reddit.com/r/dataengineering/comments/1p9xcr0/is_hadoop_hive_and_spark_still_relevant/) (Score: 2)
    *   This thread discusses the relevance of Hadoop, Hive, and Spark in the current data engineering landscape.
13. [Stuck on incremental ETL for a very normalised dataset (multi-hop relationships). Has anyone solved this before?](https://www.reddit.com/r/dataengineering/comments/1p9x52g/stuck_on_incremental_etl_for_a_very_normalised/) (Score: 2)
    *   This thread seeks solutions for incremental ETL challenges with highly normalized datasets.
14. [Best Practices for Transforming Python DataFrames Before Loading into SQLite – dbt or Alternatives?](https://www.reddit.com/r/dataengineering/comments/1p9lbga/best_practices_for_transforming_python_dataframes/) (Score: 2)
    *   This thread explores best practices for transforming Python DataFrames before loading them into SQLite, questioning the suitability of dbt and suggesting alternatives.
15. [Need suggestion [urgent]](https://www.reddit.com/r/dataengineering/comments/1p9y1op/need_suggestion_urgent/) (Score: 1)
    *   This thread urgently requests suggestions.
16. [Establishing GCP resource hierarchy/governance structure](https://www.reddit.com/r/dataengineering/comments/1p9ujws/establishing_gcp_resource_hierarchygovernance/) (Score: 0)
    *   This thread discusses establishing a GCP resource hierarchy/governance structure.

# Detailed Analysis by Thread
**[I messed up :( (Score: 158)](https://www.reddit.com/r/dataengineering/comments/1p9k43o/i_messed_up/)**
*   **Summary:** This thread revolves around the poster's confession of making a mistake. The comments consist of supportive messages, shared experiences of similar errors, and reminders about the importance of backups and learning from mistakes.
*   **Emotion:** The overall emotional tone is positive, with elements of empathy and encouragement. Despite the initial post indicating a negative situation, the responses are largely supportive.
*   **Top 3 Points of View:**
    *   Everyone makes mistakes in data engineering.
    *   Backups are crucial for recovering from errors.
    *   Mistakes are learning opportunities for becoming better engineers.

**[Have you ever worked with a data source that required zero or low transformations? (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1p9e1xr/have_you_ever_worked_with_a_data_source_that/)**
*   **Summary:** The discussion centers on experiences with data sources that require minimal or no transformation. Commenters share instances where data was already clean and ready for use, often due to the source being well-designed or pre-processed by another team. Some note the importance of still having transformation pipelines in place for future changes.
*   **Emotion:** The overall tone is neutral and informative. The discussion is matter-of-fact, with people sharing their experiences without strong emotional expression.
*   **Top 3 Points of View:**
    *   Some data sources are naturally clean and require little transformation.
    *   Even with clean data, it's good to have a transformation process in place for future changes.
    *   Reference and master data often require minimal transformations.

**[How to speed up AWS glue job to compact 500k parquet files? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1p9puon/how_to_speed_up_aws_glue_job_to_compact_500k/)**
*   **Summary:**  The thread discusses methods to improve the performance of an AWS Glue job used for compacting a large number of small Parquet files.  Suggestions include using alternative technologies better suited for handling small files, adjusting Spark configurations, and modifying the data production process.
*   **Emotion:** The emotional tone is primarily neutral, focusing on technical solutions. There's a hint of frustration acknowledged regarding the inefficiency of using Spark for this particular task.
*   **Top 3 Points of View:**
    *   Spark/Glue is not ideal for handling a very large number of small files due to metadata management overhead.
    *   Alternative technologies like S3 Select SDK or DuckDB might be more efficient.
    *   Adjusting Spark configurations (e.g., `spark.sql.files.maxPartitionBytes`) and using `repartition` instead of `coalesce` can provide some improvement.

**[The current jobmarket is quite frustrating! (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1p9xi3l/the_current_jobmarket_is_quite_frustrating/)**
*   **Summary:** The thread expresses frustration with the data engineering job market. Commenters discuss the importance of modern tech stack experience, suggest ways to frame existing experience to be more relevant, and acknowledge the impact of layoffs and increased competition.
*   **Emotion:** The emotional tone is mixed, with initial frustration evolving into a discussion with elements of both negativity (acknowledging the difficulty) and positivity (offering advice and encouragement).
*   **Top 3 Points of View:**
    *   Experience with a modern tech stack is crucial for landing a data engineering job.
    *   It is important to demonstrate Python or Scala skills.
    *   The current job market is highly competitive due to layoffs and a surplus of talent.

**[How do you inspect actual Avro/Protobuf data or detect schema when debugging? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1p9f4gp/how_do_you_inspect_actual_avroprotobuf_data_or/)**
*   **Summary:**  The thread asks about the tools and techniques for debugging and inspecting Avro/Protobuf data, specifically focusing on how to view the data and detect the schema. The solution presented involves using a schema registry and tools like kafkacat to view the payload.
*   **Emotion:** The tone of the comments is neutral and helpful, providing practical advice and tool recommendations.
*   **Top 3 Points of View:**
    *   Use a schema registry to store and track schema versions.
    *   Use tools like `kafkacat` to inspect the data in Kafka topics.
    *   `kafkacat` allows you to configure a Schema Registry.

**[Is there a PySpark DataFrame validation library that automatically splits valid and invalid rows? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1p9mg2x/is_there_a_pyspark_dataframe_validation_library/)**
*   **Summary:** This thread is a query for a PySpark library that can automatically separate valid and invalid rows in a DataFrame. One suggestion provided using an anti-join. Another suggested using [DQX](https://github.com/databrickslabs/dqx).
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   Anti Join your new dataframe to the original to extract the correct records.
    *   Look at DQX.
    *   Implement your own validation library.

**[I’m Informatica developer with some experience in databricks and pyspark as well currently searching job in data engineering field but not able to find any role permanent role in regular shift so planning do MS fabric certification..just wanted to if anyone done certification? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p9h03o/im_informatica_developer_with_some_experience_in/)**
*   **Summary:** The poster is looking for job opportunities and career advice in the data engineering field. They are also asking about the value of getting MS Fabric certification.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   MS Fabric might be worth getting to add to your resume.
    *   Databricks and Snowflake are dominant players.
    *   Here is a list of community-submitted learning resources.

**[How bad is the market? EU and US? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p9qmhr/how_bad_is_the_market_eu_and_us/)**
*   **Summary:** This thread is a discussion on the current state of the data engineering market in both the EU and US. Commenters provide a pessimistic outlook on the job market.
*   **Emotion:** The tone is mostly pessimistic and negative.
*   **Top 3 Points of View:**
    *   The market is tough for everyone, unless you are in the top 1-5%.
    *   The level of knowledge of candidates is really low.
    *   New H1B visas are limited, so the market may get better.

**[Confused about Git limitations in Databricks Repos — what do you do externally? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p9hrqu/confused_about_git_limitations_in_databricks/)**
*   **Summary:** This thread discusses the limitations of Git integration within Databricks Repos and how users manage code externally.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   You can perform Git operations like clone, checkout, pull, push, and commit from within the Databricks UI.
    *   Pull requests are created and merged externally, typically in Azure DevOps.
    *   Databricks UI doesn't support command line commands.

**[way of approaching (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1p9w6g9/way_of_approaching/)**
*   **Summary:** This thread discusses different approaches to the data engineering field, particularly focusing on data platform engineering and the qualities of a "full-stack" engineer.
*   **Emotion:** The tone is informative.
*   **Top 3 Points of View:**
    *   The unicorn is the full stack engineer who knows data modeling, PySpark, python and takes an active interest in building business domain knowledge.
    *   Here is a list of learning resources.
    *   Transitioning into Data Engineering may be of interest.

**[How is this Course (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p9qlp8/how_is_this_course/)**
*   **Summary:** This is a quick question about a course.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   The course is more theoretical.

**[Is Hadoop, Hive, and Spark still Relevant? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p9xcr0/is_hadoop_hive_and_spark_still_relevant/)**
*   **Summary:** This thread discusses the relevance of Hadoop, Hive, and Spark.
*   **Emotion:** The tone is mostly neutral.
*   **Top 3 Points of View:**
    *   Spark is still relevant.
    *   Hadoop is not that useful anymore.
    *   Understanding map/reduce is still useful when working with Spark.

**[Stuck on incremental ETL for a very normalised dataset (multi-hop relationships). Has anyone solved this before? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p9x52g/stuck_on_incremental_etl_for_a_very_normalised/)**
*   **Summary:** This thread is seeking a solution for incremental ETL challenges.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   Build add all the ids you need to each table or build more flattened intermediate tables.

**[Best Practices for Transforming Python DataFrames Before Loading into SQLite – dbt or Alternatives? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1p9lbga/best_practices_for_transforming_python_dataframes/)**
*   **Summary:** This thread discusses alternative tools.
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   DBT does only the transformation part.
    *   You are trying to use the wrong tool for the job.
    *   What's the problem with current type conversions in Python?

**[Need suggestion [urgent] (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1p9y1op/need_suggestion_urgent/)**
*   **Summary:** Discussion about layers of an architecture.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The dichotomy of the silver to gold layers should be set up correctly.

**[Establishing GCP resource hierarchy/governance structure (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1p9ujws/establishing_gcp_resource_hierarchygovernance/)**
*   **Summary:** Bot says, "You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources"
*   **Emotion:** The tone is neutral.
*   **Top 3 Points of View:**
    *   Here is a list of community-submitted learning resources.
