---
title: "Data Engineering Subreddit"
date: "2025-05-29"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Team wants every service to write individual records directly to Apache Iceberg - am I wrong to think this won't scale?](https://www.reddit.com/r/dataengineering/comments/1kych1l/team_wants_every_service_to_write_individual/) (Score: 39)
    * Discusses the scalability of writing individual records directly to Apache Iceberg and whether it's a suitable approach.
2.  [Is new dbt announcement driving bigger wedge between core and cloud?](https://www.reddit.com/r/dataengineering/comments/1kyccwt/is_new_dbt_announcement_driving_bigger_wedge/) (Score: 38)
    * Discusses whether the new dbt announcement is driving a bigger wedge between core and cloud.
3.  [Apache Iceberg vs Delta lake](https://www.reddit.com/r/dataengineering/comments/1ky5gtt/apache_iceberg_vs_delta_lake/) (Score: 20)
    * A comparison between Apache Iceberg and Delta Lake.
4.  ["Normal" amount of data re-calculation](https://www.reddit.com/r/dataengineering/comments/1ky7983/normal_amount_of_data_recalculation/) (Score: 20)
    * Discusses whether the amount of data recalculation is normal.
5.  [ELT hobby project](https://www.reddit.com/r/dataengineering/comments/1ky80zh/elt_hobby_project/) (Score: 11)
    * Discusses ideas and tools for an ELT hobby project.
6.  [What’s a Data Engineering hiring process like in 2025?](https://www.reddit.com/r/dataengineering/comments/1kyffrm/whats_a_data_engineering_hiring_process_like_in/) (Score: 10)
    * Discusses the current Data Engineering hiring process.
7.  [Redshift query compilation is slow, will BigQuery fix this?](https://www.reddit.com/r/dataengineering/comments/1ky5smd/redshift_query_compilation_is_slow_will_bigquery/) (Score: 9)
    * A discussion on whether BigQuery would fix the slow query compilation in Redshift.
8.  [Built a data quality inspector that actually shows you what's wrong with your files (in seconds)](https://v.redd.it/b2l5jicwur3f1) (Score: 8)
    * This thread is about a tool that inspects data quality and reports issues.
9.  [Data Science VS Data Engineering](https://www.reddit.com/r/dataengineering/comments/1ky9xj5/data_science_vs_data_engineering/) (Score: 7)
    * Discusses the differences between Data Science and Data Engineering.
10. [Vertex AI vs. Llama for a RAG project ¿what are the main trade-offs?](https://www.reddit.com/r/dataengineering/comments/1kydrf2/vertex_ai_vs_llama_for_a_rag_project_what_are_the/) (Score: 2)
    * A thread about the main trade-offs between using Vertex AI vs. Llama for a RAG (Retrieval-Augmented Generation) project.
11. [Placement of fact tables in data architecture](https://www.reddit.com/r/dataengineering/comments/1ky6iz8/placement_of_fact_tables_in_data_architecture/) (Score: 1)
    * Discusses the placement of fact tables in data architecture.
12. [Master in Data Engineering [Europe]](https://www.reddit.com/r/dataengineering/comments/1ky8job/master_in_data_engineering_europe/) (Score: 1)
    * Discusses masters degrees in Data Engineering in Europe.
13. [Table or infra observability for iceberg?](https://www.reddit.com/r/dataengineering/comments/1kyi8v4/table_or_infra_observability_for_iceberg/) (Score: 1)
    * A discussion about table or infra observability for Iceberg.
14. [Bootcamp Recommendations](https://www.reddit.com/r/dataengineering/comments/1ky7vpt/bootcamp_recommendations/) (Score: 0)
    * Asks for recommendations about bootcamps.
15. [Do analytics teams in your company own their logic end-to-end? Or do you rely on devs to deploy it?](https://www.reddit.com/r/dataengineering/comments/1kyc2bh/do_analytics_teams_in_your_company_own_their/) (Score: 0)
    * Asks whether analytics teams own their logic end-to-end or rely on developers.
16. [Quero migrar do Planejamento Estratégico para Engenharia de Dados - Conselhos (?)](https://www.reddit.com/r/dataengineering/comments/1kyhaib/quero_migrar_do_planejamento_estratégico_para/) (Score: 0)
    * The title translates to: "I want to migrate from Strategic Planning to Data Engineering - Advice (?)".

# Detailed Analysis by Thread
**[Team wants every service to write individual records directly to Apache Iceberg - am I wrong to think this won't scale? (Score: 39)](https://www.reddit.com/r/dataengineering/comments/1kych1l/team_wants_every_service_to_write_individual/)**
*  **Summary:**  The discussion revolves around the feasibility of having every service write individual records directly to Apache Iceberg. Many users express concerns about scalability and performance issues with this approach.
*  **Emotion:** Predominantly Neutral. While some comments express frustration or disbelief at the suggestion, the overall tone is informative and analytical.
*  **Top 3 Points of View:**
    *   Direct writes to Iceberg are a bad idea due to scalability issues. It's not designed for high-frequency, low-volume writes.
    *   A better approach is to use an operational store or message queue (like Kafka) to buffer writes before batching them into Iceberg.
    *   For high-volume ingestion, consider using micro-batching with tools like Flink or Warpstream.

**[Is new dbt announcement driving bigger wedge between core and cloud? (Score: 38)](https://www.reddit.com/r/dataengineering/comments/1kyccwt/is_new_dbt_announcement_driving_bigger_wedge/)**
*  **Summary:**  The thread discusses the new dbt announcement and its potential impact on the relationship between dbt Core and dbt Cloud. Users debate whether the changes are creating a two-tiered system that favors the cloud version.
*  **Emotion:** Mixed, with a combination of Neutral and Positive sentiments. Some users express concerns about the potential for a widening gap between Core and Cloud, while others are optimistic about the improvements offered by the new Fusion engine.
*  **Top 3 Points of View:**
    *   The new Fusion engine and Elastic License are designed to push users towards the paid dbt Cloud offering.
    *   dbt Labs is trying to remove the distinction between Core and Cloud, offering improved tooling for everyone.
    *   The Elastic License is a good move to prevent cloud providers from profiting off of open-source work without contributing back.

**[Apache Iceberg vs Delta lake (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1ky5gtt/apache_iceberg_vs_delta_lake/)**
*  **Summary:**  This thread compares Apache Iceberg and Delta Lake, discussing their respective strengths and weaknesses, and under what circumstances one might be preferred over the other.
*  **Emotion:** Largely Neutral, with users presenting factual information and opinions without strong emotional expression.
*  **Top 3 Points of View:**
    *   Delta Lake is suitable for DBX environments.
    *   Iceberg is a vendor-agnostic solution.
    *   Delta Lake may not survive in the future.

**["Normal" amount of data re-calculation (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1ky7983/normal_amount_of_data_recalculation/)**
*  **Summary:**  The discussion centers around the "normalcy" of recalculating a large amount of data, with users expressing concern and offering alternative strategies.
*  **Emotion:** Predominantly Neutral, with some Negative sentiments expressing concern and disbelief at the large-scale recalculation.
*  **Top 3 Points of View:**
    *   Recalculating 50TB of data is excessive and indicates a potential problem with the data pipeline.
    *   Implementing SCD (Slowly Changing Dimensions) and timestamps on dimensions could help reduce the need for full recalculations.
    *   While unusual, legitimate use cases for large-scale recalculation exist, such as long-term forecasting.

**[ELT hobby project (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1ky80zh/elt_hobby_project/)**
*  **Summary:**  Users are discussing ideas and tool recommendations for an ELT (Extract, Load, Transform) hobby project.
*  **Emotion:** Largely Neutral, with information being shared.
*  **Top 2 Points of View:**
    *   Use Dagster.
    *   Check out the open-source project showcase for ideas.

**[What’s a Data Engineering hiring process like in 2025? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1kyffrm/whats_a_data_engineering_hiring_process_like_in/)**
*  **Summary:**  This thread discusses the typical hiring process for Data Engineering roles, including the skills and tools that are in demand.
*  **Emotion:** Mostly Neutral, providing factual observations about the hiring landscape. There's a touch of Positive sentiment in providing advice and encouragement.
*  **Top 3 Points of View:**
    *   Interviews often involve live SQL coding, especially with window functions.
    *   Companies are looking for candidates with experience in end-to-end solutions and a broad range of tools.
    *   Assessment tests include Python and SQL problems on platforms like HackerRank.

**[Redshift query compilation is slow, will BigQuery fix this? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1ky5smd/redshift_query_compilation_is_slow_will_bigquery/)**
*  **Summary:**  The thread questions if switching to BigQuery will resolve slow query compilation issues experienced with Redshift.
*  **Emotion:** Predominantly Neutral, offering advice and comparisons between the two platforms.
*  **Top 3 Points of View:**
    *   BigQuery can eliminate upfront cluster provisioning delays.
    *   Clickhouse offers faster querying.
    *   Redshift performance depends on correct configurations.

**[Built a data quality inspector that actually shows you what's wrong with your files (in seconds) (Score: 8)](https://v.redd.it/b2l5jicwur3f1)**
*   **Summary:** This thread discusses a data quality tool that quickly identifies issues in data files.
*   **Emotion:** A mix of Positive and Neutral. One user expresses excitement, while another voices concerns about security.
*   **Top 2 Points of View:**
    *   The tool looks promising.
    *   Some users are wary of sharing their data with an unknown site.

**[Data Science VS Data Engineering (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1ky9xj5/data_science_vs_data_engineering/)**
*  **Summary:**  The thread discusses the differences between Data Science and Data Engineering roles, career paths, and job security.
*  **Emotion:** Mostly Neutral, providing insights and comparisons between the two fields. There are some Positive sentiments regarding job security in DE.
*  **Top 3 Points of View:**
    *   Data Engineering offers better job security compared to Data Science.
    *   Data Science involves solving problems **with** data, while Data Engineering involves solving problems **about** data.
    *   In Australia, Data Engineering roles are currently more abundant than Data Science roles.

**[Vertex AI vs. Llama for a RAG project ¿what are the main trade-offs? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1kydrf2/vertex_ai_vs_llama_for_a_rag_project_what_are_the/)**
*  **Summary:**  The thread discusses the main trade-offs between using Vertex AI vs. Llama for a RAG (Retrieval-Augmented Generation) project.
*  **Emotion:** Neutral with some hints of Positive sentiment. The answers are helpful and encouraging.
*  **Top 2 Points of View:**
    *   Cost and third-party dependency are the top considerations.
    *   Llama 3.1 is good for summarization and chatbots.

**[Placement of fact tables in data architecture (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ky6iz8/placement_of_fact_tables_in_data_architecture/)**
*  **Summary:**  This thread is about where to place fact tables within a data architecture.
*  **Emotion:** Predominantly Neutral.
*  **Top 1 Point of View:**
    *   Fact and snapshot tables should be placed in the integration layer, co-located within the fact table's Schema.

**[Master in Data Engineering [Europe] (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ky8job/master_in_data_engineering_europe/)**
*   **Summary:** This thread discusses Masters programs in Data Engineering in Europe.
*   **Emotion:** Neutral.
*   **Top 1 Point of View:**
    *   A user was given a link to community learning resources.

**[Table or infra observability for iceberg? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kyi8v4/table_or_infra_observability_for_iceberg/)**
*   **Summary:** This thread asks about table or infra observability for Iceberg.
*   **Emotion:** Neutral.
*   **Top 1 Point of View:**
    *   A user was given a link to community learning resources.

**[Bootcamp Recommendations (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ky7vpt/bootcamp_recommendations/)**
*   **Summary:** This thread asks for Bootcamp Recommendations.
*   **Emotion:** Neutral.
*   **Top 2 Points of View:**
    *   A user was given a link to community learning resources.
    *   A user asked what specific role the poster was aiming for.

**[Do analytics teams in your company own their logic end-to-end? Or do you rely on devs to deploy it? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kyc2bh/do_analytics_teams_in_your_company_own_their/)**
*   **Summary:** This thread asks whether analytics teams own their logic end-to-end or rely on developers.
*   **Emotion:** Mixed, ranging from neutral to positive.
*   **Top 3 Points of View:**
    *   Analytics teams should use SQL and BI tools without backend developer involvement.
    *   It depends on the type of analytics team, the services consumed, and potential operational risks.
    *   DEs are responsible for data ingestion and exposing ingested information, while DAs develop and test logic within that infrastructure.

**[Quero migrar do Planejamento Estratégico para Engenharia de Dados - Conselhos (?) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kyhaib/quero_migrar_do_planejamento_estratégico_para/)**
*   **Summary:** The thread title asks for advice on migrating from Strategic Planning to Data Engineering.
*   **Emotion:** Neutral.
*   **Top 1 Point of View:**
    *   The poster was advised to start a degree in IT to help with the fundamentals.
