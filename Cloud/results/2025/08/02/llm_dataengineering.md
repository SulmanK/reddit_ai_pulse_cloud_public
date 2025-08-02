---
title: "Data Engineering Subreddit"
date: "2025-08-02"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [I used to think data engineering was a small specialty of software engineering. I was very mistaken.](https://www.reddit.com/r/dataengineering/comments/1mfx209/i_used_to_think_data_engineering_was_a_small/) (Score: 108)
    * Discusses the complexity and depth of data engineering compared to initial perceptions.
2.  [Best certifications to take for a data engineer?](https://www.reddit.com/r/dataengineering/comments/1mfnphn/best_certifications_to_take_for_a_data_engineer/) (Score: 44)
    * Asks about and discusses the value and relevance of data engineering certifications, particularly those from cloud vendors.
3.  [Real-time data pipeline with late arriving IoT](https://www.reddit.com/r/dataengineering/comments/1mforgf/realtime_data_pipeline_with_late_arriving_iot/) (Score: 26)
    * Addresses challenges in building real-time data pipelines for IoT data, especially handling late-arriving data and schema evolution.
4.  [How many of you use Go?](https://www.reddit.com/r/dataengineering/comments/1mfohjj/how_many_of_you_use_go/) (Score: 19)
    * Explores the usage of the Go programming language in data engineering tasks.
5.  [Is data engineering just backend distributed systems?](https://www.reddit.com/r/dataengineering/comments/1mfjof8/is_data_engineering_just_backend_distributed/) (Score: 11)
    * A question about whether data engineering can be summarized as simply back end distribution systems.
6.  [Iceberg, The Right Idea - The Wrong Spec - Part 2 of 2: The Spec](https://www.reddit.com/r/dataengineering/comments/1mfrvpt/iceberg_the_right_idea_the_wrong_spec_part_2_of_2/) (Score: 11)
    * Discusses the strengths and weaknesses of the Iceberg table format, and compares it to Delta Lake.
7. [Released an Airflow provider that makes DAG monitoring actually reliable](https://www.reddit.com/r/dataengineering/comments/1mfx5u8/released_an_airflow_provider_that_makes_dag/) (Score: 6)
    * A post about a reliable Airflow provider that can monitor DAG
8. [Can anyone help me understand data ingestion system design for compliance/archival domain please?](https://www.reddit.com/r/dataengineering/comments/1mfynaf/can_anyone_help_me_understand_data_ingestion/) (Score: 1)
    * A question about understanding of data ingestion system design for compliance/archival domain
9. [Do I need to get a masters to start a career in data science/engineering?](https://www.reddit.com/r/dataengineering/comments/1mfca3k/do_i_need_to_get_a_masters_to_start_a_career_in/) (Score: 0)
    * Asks whether a master's degree is required to start a career in data science or data engineering.
10. [Need Guidance : Oracle GoldenGate to Data Engineer](https://www.reddit.com/r/dataengineering/comments/1mfoitd/need_guidance_oracle_goldengate_to_data_engineer/) (Score: 0)
    * Asks for advice on transitioning from Oracle GoldenGate to data engineering.
11. [Azure key vault backed secret Scope issue](https://www.reddit.com/r/dataengineering/comments/1mfvn34/azure_key_vault_backed_secret_scope_issue/) (Score: 0)
    * A post about Azure key vault backed secret Scope issue

# Detailed Analysis by Thread
**[I used to think data engineering was a small specialty of software engineering. I was very mistaken. (Score: 108)](https://www.reddit.com/r/dataengineering/comments/1mfx209/i_used_to_think_data_engineering_was_a_small/)**
*   **Summary:** The thread revolves around the realization that data engineering is a much broader and more complex field than initially perceived, exceeding the scope of a simple software engineering specialty.
*   **Emotion:** Predominantly Neutral, with some Negative sentiments expressed regarding frustrations with terminology and challenges. Some Positive sentiment also surfaces, reflecting the satisfaction of understanding the field's depth.
*   **Top 3 Points of View:**
    *   Data engineering is often underestimated in its complexity and depth.
    *   Companies frequently get lost in technical details and fail to focus on the underlying business problems.
    *   The terminology used in data engineering can be confusing and relies too heavily on metaphors.

**[Best certifications to take for a data engineer? (Score: 44)](https://www.reddit.com/r/dataengineering/comments/1mfnphn/best_certifications_to_take_for_a_data_engineer/)**
*   **Summary:** The thread discusses the value and relevance of certifications for data engineers, with a focus on certifications from major cloud vendors like Azure, AWS, GCP, Databricks, and Snowflake.
*   **Emotion:** Mostly Neutral, with some Positive sentiment regarding the value of certifications in demonstrating knowledge and standing out in the job market, and some Negative sentiment expressing skepticism about their overall impact.
*   **Top 3 Points of View:**
    *   Certifications can be beneficial for learning and demonstrating understanding of specific platforms.
    *   Experience is more valuable than certifications in the hiring process.
    *   Vendor-specific certifications (e.g., Databricks, AWS, Azure) are generally considered more valuable than generic ones.

**[Real-time data pipeline with late arriving IoT (Score: 26)](https://www.reddit.com/r/dataengineering/comments/1mforgf/realtime_data_pipeline_with_late_arriving_iot/)**
*   **Summary:** The thread focuses on the challenges of building real-time data pipelines for IoT data, specifically addressing issues like late-arriving data, schema evolution, and technology choices.
*   **Emotion:** Primarily Neutral, reflecting technical discussions.
*   **Top 3 Points of View:**
    *   Handling late-arriving data requires event-time windowing and watermarking techniques using tools like Flink or Kafka Streams.
    *   Decoupling ingestion from transformation can improve system stability, even if it sacrifices true real-time processing.
    *   Consider aggregating data at the edge to reduce data volume and simplify the pipeline.

**[How many of you use Go? (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1mfohjj/how_many_of_you_use_go/)**
*   **Summary:** The thread discusses the adoption and use cases of the Go programming language in data engineering, with comparisons to other languages like Python and Rust.
*   **Emotion:** A mix of Neutral and Positive sentiments, with users expressing interest in or positive experiences with Go, while some express Negative sentiments due to the lack of tooling in the DE world.
*   **Top 3 Points of View:**
    *   Go is a nice language for data engineering, especially for ingestion and backend tasks.
    *   Python remains the dominant language for many data engineering tasks due to its tooling and framework support.
    *   Rust is a strong alternative to Go for performance-critical tasks, particularly when dealing with large data volumes.

**[Is data engineering just backend distributed systems? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1mfjof8/is_data_engineering_just_backend_distributed/)**
*   **Summary:** The thread is regarding the technologies that are required for the role of a data engineer
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   Technologies like Apache Flink can be very useful for real time streams
    *   The question is whether technologies such as Kafka and Postgres are expected to be set up in data engineer take home tests

**[Iceberg, The Right Idea - The Wrong Spec - Part 2 of 2: The Spec (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1mfrvpt/iceberg_the_right_idea_the_wrong_spec_part_2_of_2/)**
*   **Summary:** The thread discusses the pro's and con's of the Apache Iceberg system.
*   **Emotion:** Neutral, Positive
*   **Top 3 Points of View:**
    *   The iceberg system has flaws and needs to be set up in a better way.
    *   That Delta is just set and forget
    *   The article has clear misunderstandings

**[Released an Airflow provider that makes DAG monitoring actually reliable (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mfx5u8/released_an_airflow_provider_that_makes_dag/)**
*   **Summary:** This is a post from a bot that showcases their open-source project here: https://dataengineering.wiki/Community/Projects
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The bot simply links their open source project

**[Can anyone help me understand data ingestion system design for compliance/archival domain please? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mfynaf/can_anyone_help_me_understand_data_ingestion/)**
*   **Summary:** The thread is regarding the understanding of data ingestion system design for compliance/archival domain
*   **Emotion:** Neutral, Negative
*   **Top 3 Points of View:**
    *   The best way to understand the subject of data ingestion is to use LLMs
    *   The OP is sorry for asking so many questions

**[Do I need to get a masters to start a career in data science/engineering? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mfca3k/do_i_need_to_get_a_masters_to_start_a_career_in/)**
*   **Summary:** The thread is about whether or not getting a master's degree is required to become a data engineer or data scientist.
*   **Emotion:** Negative
*   **Top 3 Points of View:**
    *   A master's degree is probably going to be required if you want to become a data scientist.
    *   Just get experience in the field, AI might make junior engineers less attractive.
    *   No, you don't need to get a master's degree.

**[Need Guidance : Oracle GoldenGate to Data Engineer (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mfoitd/need_guidance_oracle_goldengate_to_data_engineer/)**
*   **Summary:** The thread is regarding a way to transition from Oracle GoldenGate to Data Engineer
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The response links a community-submitted learning resource

**[Azure key vault backed secret Scope issue (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mfvn34/azure_key_vault_backed_secret_scope_issue/)**
*   **Summary:** The thread is regarding an issue with Azure key vault backed secret scope.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   The response links a community-submitted learning resource
