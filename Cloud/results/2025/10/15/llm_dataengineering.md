---
title: "Data Engineering Subreddit"
date: "2025-10-15"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Do you really need databricks?](https://www.reddit.com/r/dataengineering/comments/1o738t6/do_you_really_need_databricks/) (Score: 56)
    *   A discussion about whether Databricks is necessary for all data engineering needs, with various viewpoints on its benefits and alternatives.
2.  ["Data Person" in a small fintech - How do I shape my “flexible”role towards Data Engineering?](https://www.reddit.com/r/dataengineering/comments/1o7dp2i/data_person_in_a_small_fintech_how_do_i_shape_my/) (Score: 21)
    *   Advice for a data professional in a fintech company on transitioning their role towards data engineering.
3.  [Testing data changes without blowing up prod](https://www.reddit.com/r/dataengineering/comments/1o78mvz/testing_data_changes_without_blowing_up_prod/) (Score: 14)
    *   Discussion on best practices for testing data changes in a data pipeline without disrupting the production environment.
4.  [Final nail in the coffin of OSS dbt](https://www.reddit.com/r/dataengineering/comments/1o7k8av/final_nail_in_the_coffin_of_oss_dbt/) (Score: 12)
    *   A discussion on the impact of recent merger on the open-source dbt project.
5.  [Looking for Advice to Stay Relevant technically as a Senior Data Engineer](https://www.reddit.com/r/dataengineering/comments/1o7eicq/looking_for_advice_to_stay_relevant_technically/) (Score: 10)
    *   Advice for senior data engineers looking to stay technically relevant in the field.
6.  [dbt Coalesce 2025 Highlights: dbt + Fivetran Merger, Open Data Infrastructure, dbt Fusion and more](https://www.selectstar.com/resources/dbt-coalesce-2025) (Score: 10)
    *   Highlights and key takeaways from the dbt Coalesce 2025 event, including the dbt + Fivetran merger and dbt Fusion.
7.  [What's the best way to ingest data into a BI platform?](https://www.reddit.com/r/dataengineering/comments/1o77b20/whats_the_best_way_to_ingest_data_into_a_bi/) (Score: 9)
    *   Discussion about the best approaches to ingest data into a BI platform, considering different tools and architectures.
8.  [Up-to-date data governance platform pricings help](https://www.reddit.com/r/dataengineering/comments/1o73qo4/uptodate_data_governance_platform_pricings_help/) (Score: 7)
    *   Seeking information and assistance with understanding the pricing structures of modern data governance platforms.
9.  [Learn pipelines with databricks and dataflow(gcp)](https://www.reddit.com/r/dataengineering/comments/1o70g6r/learn_pipelines_with_databricks_and_dataflowgcp/) (Score: 7)
    *   Inquiry about learning resources for building data pipelines using Databricks and Google Cloud Dataflow.
10. [Has anyone migrated to airflow 3.1?](https://www.reddit.com/r/dataengineering/comments/1o6zzo8/has_anyone_migrated_to_airflow_31/) (Score: 6)
    *   Discussion about experiences and challenges related to migrating to Apache Airflow 3.1.
11. [Real-time Data Analytics at Scale: Integrating Apache Flink and Apache Doris with Flink Doris Connector and Flink CDC](https://www.reddit.com/r/dataengineering/comments/1o6sfce/realtime_data_analytics_at_scale_integrating/) (Score: 4)
    *   Discussion of using Apache Flink and Apache Doris for real-time data analytics at scale.
12. [Dbt certification exam and certification renewal experience?](https://www.reddit.com/r/dataengineering/comments/1o7e0zl/dbt_certification_exam_and_certification_renewal/) (Score: 4)
    *   Questions about the dbt certification exam and the certification renewal process.
13. [Scraping HTML for NLP training data.](https://www.reddit.com/r/dataengineering/comments/1o77amx/scraping_html_for_nlp_training_data/) (Score: 1)
    *   Discussion about techniques and tools for scraping HTML to gather training data for NLP models.
14. [Business lead vs tech lead: who is more valuable?](https://www.reddit.com/r/dataengineering/comments/1o6sf1g/business_lead_vs_tech_lead_who_is_more_valuable/) (Score: 0)
    *   Discussion about the relative value of business leads and tech leads in an organization.

# Detailed Analysis by Thread
**[ [D] Do you really need databricks? (Score: 56)](https://www.reddit.com/r/dataengineering/comments/1o738t6/do_you_really_need_databricks/)**
*  **Summary:** A discussion about the necessity of Databricks for data engineering, considering its benefits and alternatives.
*  **Emotion:** The emotional tone is predominantly neutral, as the comments focus on objective comparisons and technical considerations.
*  **Top 3 Points of View:**
    * Databricks simplifies the setup and integration of Spark and other components, especially for organizations already heavily invested in Spark.
    * The basic data architecture can be implemented on various platforms like Snowflake, AWS, GCP, or even on-premise solutions, depending on specific needs and preferences.
    * Databricks is useful for quickly testing ideas and concepts, but for production environments, other architectures might be more suitable.

**[ "Data Person" in a small fintech - How do I shape my “flexible”role towards Data Engineering? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1o7dp2i/data_person_in_a_small_fintech_how_do_i_shape_my/)**
*  **Summary:** Advice for a "data person" in a small fintech company looking to transition their role towards data engineering.
*  **Emotion:** The emotional tone is largely positive, offering encouragement and actionable steps.
*  **Top 3 Points of View:**
    * Focus on shipping small, real ELT stacks using tools like dbt and automate reporting pipelines using Python and PostgreSQL.
    * Prioritize solving problems quickly, reliably, and within budget to gain trust and establish oneself as a data engineer.
    * Emphasize learning core skills such as data modeling, SQL, and cloud services like AWS S3, Lambda, and Redshift.

**[ Testing data changes without blowing up prod (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1o78mvz/testing_data_changes_without_blowing_up_prod/)**
*  **Summary:**  Discussion on best practices for testing data changes in a data pipeline without disrupting the production environment.
*  **Emotion:** The emotional tone is neutral, with comments focusing on providing practical solutions and sharing experiences.
*  **Top 3 Points of View:**
    * Create shadow pipelines that run changes against a recent snapshot of production data, writing results to a temporary schema for comparison before merging.
    * Ensure the staging environment is as close as possible to production, ideally an exact replica, to catch edge cases and accurately test changes.
    * Implement a data unit testing framework with representative data samples for each source table and expected outputs to verify code changes.

**[ Final nail in the coffin of OSS dbt (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1o7k8av/final_nail_in_the_coffin_of_oss_dbt/)**
*  **Summary:** A discussion on the implications of a recent merger on the open-source dbt project, with opinions on its future and potential alternatives.
*  **Emotion:** The emotional tone is mixed, ranging from neutral to slightly negative, reflecting uncertainty about the future of OSS dbt.
*  **Top 3 Points of View:**
    * The merger may shift priorities towards profit, potentially impacting the active development and community contributions to OSS dbt.
    * Despite concerns, the open-source version remains available, and the community can continue to fork and develop the project independently.
    * There is uncertainty about dbt's business model and its ability to generate revenue, even with the new fusion.

**[ Looking for Advice to Stay Relevant technically as a Senior Data Engineer (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1o7eicq/looking_for_advice_to_stay_relevant_technically/)**
*  **Summary:** Advice for senior data engineers on how to stay technically relevant in the rapidly evolving field.
*  **Emotion:** The emotional tone is largely positive, offering advice and acknowledging the challenges of keeping up with technology.
*  **Top 3 Points of View:**
    * Focus on strengthening core skills like SQL and data modeling, which are foundational and less susceptible to obsolescence.
    * Embrace distributed compute and storage solutions like Databricks and Snowflake, which are becoming increasingly important.
    * Consider transitioning to a Solutions Architect role, which may be less affected by automation and offers strategic opportunities.

**[ dbt Coalesce 2025 Highlights: dbt + Fivetran Merger, Open Data Infrastructure, dbt Fusion and more (Score: 10)](https://www.selectstar.com/resources/dbt-coalesce-2025)**
*  **Summary:** Highlights and key takeaways from the dbt Coalesce 2025 event, including the dbt + Fivetran merger and dbt Fusion.
*  **Emotion:** The emotional tone is positive and curious, expressing interest in the potential benefits and impacts of the discussed developments.
*  **Top 3 Points of View:**
    * The dbt and Fivetran merger could streamline workflows significantly by providing more integrated data solutions.
    * There is curiosity about how dbt Fusion will impact existing data pipelines and what new capabilities it will offer.
    * Open data infrastructure sounds promising but will require effective execution to realize its potential benefits.

**[ What's the best way to ingest data into a BI platform? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1o77b20/whats_the_best_way_to_ingest_data_into_a_bi/)**
*  **Summary:**  Discussion about the best approaches to ingest data into a BI platform, considering different tools and architectures.
*  **Emotion:** The emotional tone is neutral, offering various solutions and advice based on different contexts and requirements.
*  **Top 3 Points of View:**
    * Use a data warehouse and an ETL tool like Fivetran or self-hosted Airbyte for easy data ingestion and cleaning.
    * Build a data pipeline to denormalize data before it reaches the BI tool, improving query performance and usability.
    * Utilize declarative data flows with dynamic tables in Snowflake, Delta Live Tables in Databricks, or Tabsdata to simplify data ingestion.

**[ Up-to-date data governance platform pricings help (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1o73qo4/uptodate_data_governance_platform_pricings_help/)**
*  **Summary:** Seeking information and assistance with understanding the pricing structures of modern data governance platforms.
*  **Emotion:** The emotional tone is informative and helpful, providing specific pricing ranges and tactics for negotiating with vendors.
*  **Top 3 Points of View:**
    * Pricing varies widely based on company size, data team size, industry, use case, deployment (cloud vs. on-prem), and data sensitivity.
    * Recent quotes show that Collibra with lineage/workflow costs 180k–320k, Alation or Atlan for catalog + basic governance costs 60k–180k, and lighter catalogs like Secoda/Castor/OvalEdge around 15k–60k.
    * Tactics for getting better pricing include searching public procurement PDFs, checking G2 and Peer Insights reviews, and negotiating editor vs. viewer definitions.

**[ Learn pipelines with databricks and dataflow(gcp) (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1o70g6r/learn_pipelines_with_databricks_and_dataflowgcp/)**
*  **Summary:**  Inquiry about learning resources for building data pipelines using Databricks and Google Cloud Dataflow.
*  **Emotion:** The emotional tone is positive, offering straightforward and encouraging advice.
*  **Top 3 Points of View:**
    * Databricks and Google Cloud Dataflow have great documentation and tutorials on their websites.
    * GCP offers free online courses for Dataflow.
    * Both Databricks and Dataflow can be self-taught with the available resources.

**[ Has anyone migrated to airflow 3.1? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1o6zzo8/has_anyone_migrated_to_airflow_31/)**
*  **Summary:**  Discussion about experiences and challenges related to migrating to Apache Airflow 3.1.
*  **Emotion:** The emotional tone is mixed, ranging from neutral to slightly positive, with users sharing both positive experiences and encountering some pain points.
*  **Top 3 Points of View:**
    * Some users have successfully migrated and found it relatively easy, with tools like Ruff's AIR301 rule helping to fix syntax issues.
    * Others have encountered issues with documentation being outdated or with specific features like manually triggered DAGs being broken until version 3.1.1.
    * One user found the UI in versions 2.7 and later to be less desirable and is considering upgrading only to version 2.6.3.

**[ Real-time Data Analytics at Scale: Integrating Apache Flink and Apache Doris with Flink Doris Connector and Flink CDC (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o6sfce/realtime_data_analytics_at_scale_integrating/)**
*  **Summary:** Discussion of using Apache Flink and Apache Doris for real-time data analytics at scale.
*  **Emotion:** The emotional tone is largely neutral, with comments focusing on the technical merits of the technologies discussed.
*  **Top 3 Points of View:**
    * Apache Flink and Apache Doris are considered solid choices for real-time data work.
    * The Flink Doris Connector boosts read throughput and supports asynchronous lookups, improving performance.
    * Processing data directly in the stream may not be the best approach for analytics; streaming data to a modern analytics database might be preferable.

**[ Dbt certification exam and certification renewal experience? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1o7e0zl/dbt_certification_exam_and_certification_renewal/)**
*  **Summary:** Questions about the dbt certification exam and the certification renewal process.
*  **Emotion:** The emotional tone is neutral, with comments offering practical advice about certification renewals.
*  **Top 3 Points of View:**
    * Certification renewals often require payment.
    * It is worth checking the support documentation for details about the renewal process.
    * The certification might be worth it if your job values it.

**[ Scraping HTML for NLP training data. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1o77amx/scraping_html_for_nlp_training_data/)**
*  **Summary:** Discussion about techniques and tools for scraping HTML to gather training data for NLP models.
*  **Emotion:** The emotional tone is neutral, with comments offering specific tools and resources.
*  **Top 3 Points of View:**
    * LLMs can be used to help write parsing code, but the HTML should be downloaded first.
    * Tools like Scrapy and Scrapy-poet can be used to separate parsing logic from scraping logic.
    * Jigsawstack.com can generate selectors and scrape the information needed.

**[ Business lead vs tech lead: who is more valuable? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1o6sf1g/business_lead_vs_tech_lead_who_is_more_valuable/)**
*  **Summary:** Discussion about the relative value of business leads and tech leads in an organization.
*  **Emotion:** The emotional tone is somewhat negative, with responses ranging from emphasizing the importance of business over tech to highlighting the differing responsibilities of each role.
*  **Top 3 Points of View:**
    * Business leads are often seen as more valuable because tech doesn't exist without the business.
    * In an agile team, the business lead is the product owner, while the tech lead is responsible for design and implementation.
    * It's important to provide more context to get helpful answers about quantifying the value of each role.
