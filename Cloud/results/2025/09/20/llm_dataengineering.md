---
title: "Data Engineering Subreddit"
date: "2025-09-20"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions

1.  [Exporting 4 Billion Rows from SQL Server to TSV?](https://www.reddit.com/r/dataengineering/comments/1nl7f2c/exporting_4_billion_rows_from_sql_server_to_tsv/) (Score: 52)
    *   Users discuss methods and potential pitfalls of exporting a very large dataset from SQL Server to TSV format.

2.  [Why is modern data architecture so confusing? (and what finally made sense for me - sharing for beginners)](https://www.reddit.com/r/dataengineering/comments/1nl7h5w/why_is_modern_data_architecture_so_confusing_and/) (Score: 43)
    *   The thread revolves around the complexities of modern data architecture, offering advice to beginners and sharing resources to help navigate the field.

3.  [How to prepare for an upcoming AWS Data Engineer role?](https://www.reddit.com/r/dataengineering/comments/1nlos9p/how_to_prepare_for_an_upcoming_aws_data_engineer/) (Score: 30)
    *   Users provide guidance on how to prepare for an AWS Data Engineer role, focusing on certifications, practical skills, and relevant AWS services.

4.  [Homelabs do you have one? I have a question](https://www.reddit.com/r/dataengineering/comments/1nl9lu9/homelabs_do_you_have_one_i_have_a_question/) (Score: 20)
    *   The thread discusses the use of homelabs for data engineering, with users sharing their setups, hardware choices (Raspberry Pi, mini PCs, servers), and the types of projects they run.

5.  [Those who switched from data engineering to data platform engineering roles - how did you like it ?](https://www.reddit.com/r/dataengineering/comments/1nlqgjp/those_who_switched_from_data_engineering_to_data/) (Score: 20)
    *   Users share their experiences and preferences regarding the switch from data engineering to data platform engineering roles, discussing the different responsibilities and skill sets involved.

6.  [Considering contributing to dbt-core as my first open source project, but I’m afraid it’s slowly dying](https://www.reddit.com/r/dataengineering/comments/1nlqp6w/considering_contributing_to_dbtcore_as_my_first/) (Score: 15)
    *   The discussion centers around the idea of contributing to the dbt-core open-source project, with users weighing the pros and cons and suggesting alternative projects.

7.  [Data Warehouse Advice](https://www.reddit.com/r/dataengineering/comments/1nla3bv/data_warehouse_advice/) (Score: 11)
    *   Users provide advice on setting up a data warehouse, including selecting vendors, estimating costs, and the necessary skills and expertise.

8.  [WASM columnar approach](https://www.reddit.com/r/dataengineering/comments/1nl623u/wasm_columnar_approach/) (Score: 9)
    *   The thread discusses the use of WebAssembly (WASM) and columnar databases like DuckDB-WASM in analytics, focusing on its potential in operational tools and limitations in traditional BI.

9. [Data Engineering Jobs](https://www.reddit.com/r/dataengineering/comments/1nlozst/data_engineering_jobs/) (Score: 6)
    * A thread where users point each other to Data Engineering Jobs.

10. [Is this a common experience? A BI vendor is being heavily pushed regardless of feedback](https://www.reddit.com/r/dataengineering/comments/1nkrnw2/is_this_a_common_experience_a_bi_vendor_is_being/) (Score: 5)
    *   Users discuss the common experience of BI vendors being pushed regardless of feedback, highlighting the reasons behind it and offering advice on how to handle the situation.

11. [Syncing data from Snowflake to MongoDB using CDC streams](https://www.reddit.com/r/dataengineering/comments/1nlhkw4/syncing_data_from_snowflake_to_mongodb_using_cdc/) (Score: 5)
    *   The thread discusses methods for syncing data from Snowflake to MongoDB using Change Data Capture (CDC) streams, with users suggesting different approaches and tools.

12. [Poor data quality](https://www.reddit.com/r/dataengineering/comments/1nlyvjg/poor_data_quality/) (Score: 5)
    *   Users discuss the issue of poor data quality, its impact on reports, and strategies for addressing it, including automated checks and data governance.

13. [Advancing into Senior Roles](https://www.reddit.com/r/dataengineering/comments/1nm30aq/advancing_into_senior_roles/) (Score: 4)
    *   The discussion centers around how to advance into senior roles in data engineering, with users debating the importance of leadership skills and people management.

14. [How to handle custom/dynamic defined fields in dimensions](https://www.reddit.com/r/dataengineering/comments/1nlgefo/how_to_handle_customdynamic_defined_fields_in/) (Score: 1)
    *   The thread explores different options for handling custom/dynamic defined fields in dimensions, with users suggesting approaches like EVA objects, JSON columns, and mini-dims.

15. [Is DSML course from Scaler worth it?](https://www.reddit.com/r/dataengineering/comments/1nm28h0/is_dsml_course_from_scaler_worth_it/) (Score: 1)
    *   The thread recommends a list of community-submitted learning resources.

16. [Advice on allowing multiple users to access an Access database via a GUI without having data loss or corruption?](https://www.reddit.com/r/dataengineering/comments/1nlngm5/advice_on_allowing_multiple_users_to_access_an/) (Score: 0)
    *   Users provide advice on how to allow multiple users to access an Access database via a GUI without data loss or corruption, primarily recommending migrating to a different database system.

17. [Personal Health Data Management](https://www.reddit.com/r/dataengineering/comments/1nlvz6f/personal_health_data_management/) (Score: 0)
    *   The thread discusses personal health data management, recommending standards like FHIR and simple databases for getting started.

18. [Do data teams even care about CSR, or is it always seen as a distraction?](https://www.reddit.com/r/dataengineering/comments/1nm3sbc/do_data_teams_even_care_about_csr_or_is_it_always/) (Score: 0)
    *   Users share their perspectives on whether data teams care about Corporate Social Responsibility (CSR) initiatives, with some viewing it as a distraction.

# Detailed Analysis by Thread

**[Exporting 4 Billion Rows from SQL Server to TSV? (Score: 52)](https://www.reddit.com/r/dataengineering/comments/1nl7f2c/exporting_4_billion_rows_from_sql_server_to_tsv/)**

*   **Summary:** Users discuss methods and potential pitfalls of exporting a very large dataset from SQL Server to TSV format. Suggestions include using Python with Polars, breaking the export into chunks, and alternative formats like Parquet. Some users express concerns about the practicality of the client using such a large TSV file.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiment related to offering help and solutions.
*   **Top 3 Points of View:**
    *   The sheer size of the data makes a TSV export impractical for the end-user.
    *   Breaking the data into smaller chunks is essential for error handling and manageability.
    *   Using Python with libraries like Polars can simplify and parallelize the export process.

**[Why is modern data architecture so confusing? (and what finally made sense for me - sharing for beginners) (Score: 43)](https://www.reddit.com/r/dataengineering/comments/1nl7h5w/why_is_modern_data_architecture_so_confusing_and/)**

*   **Summary:** The thread revolves around the complexities of modern data architecture, offering advice to beginners and sharing resources to help navigate the field. Emphasis is placed on focusing on business needs, keeping things simple, and understanding the fundamental functions of data architecture.
*   **Emotion:** The overall emotional tone is positive and neutral, with users expressing agreement and offering helpful advice.
*   **Top 3 Points of View:**
    *   Focus on business needs and avoid getting distracted by trends.
    *   Modern data architecture can be simplified by thinking in terms of functions (ingest, store, transform, serve) rather than tiers.
    *   Gaining real-world experience through hands-on projects is crucial for understanding data architecture.

**[How to prepare for an upcoming AWS Data Engineer role? (Score: 30)](https://www.reddit.com/r/dataengineering/comments/1nlos9p/how_to_prepare_for_an_upcoming_aws_data_engineer/)**

*   **Summary:** Users provide guidance on how to prepare for an AWS Data Engineer role, focusing on certifications, practical skills, and relevant AWS services. The importance of learning Python, SQL, and AWS services like Glue, S3, and Athena is emphasized.
*   **Emotion:** The overall emotional tone is neutral, with positive sentiments related to encouragement and offering practical advice.
*   **Top 3 Points of View:**
    *   Focus on gaining hands-on experience with AWS services like Glue, S3, and Athena.
    *   Consider pursuing AWS certifications, starting with the Cloud Practitioner.
    *   Develop proficiency in Python and SQL as essential skills for the role.

**[Homelabs do you have one? I have a question (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1nl9lu9/homelabs_do_you_have_one_i_have_a_question/)**

*   **Summary:** The thread discusses the use of homelabs for data engineering, with users sharing their setups, hardware choices (Raspberry Pi, mini PCs, servers), and the types of projects they run.
*   **Emotion:** The overall emotional tone is positive and neutral, with users enthusiastically sharing their experiences and offering helpful suggestions.
*   **Top 3 Points of View:**
    *   Mini PCs offer a good balance of power and efficiency for homelab activities.
    *   Raspberry Pis are useful for control plane tasks.
    *   Older servers can be repurposed for homelabs, offering significant resources at a lower cost.

**[Those who switched from data engineering to data platform engineering roles - how did you like it ? (Score: 20)](https://www.reddit.com/r/dataengineering/comments/1nlqgjp/those_who_switched_from_data_engineering_to_data/)**

*   **Summary:** Users share their experiences and preferences regarding the switch from data engineering to data platform engineering roles, discussing the different responsibilities and skill sets involved.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiments from those who prefer data platform engineering.
*   **Top 3 Points of View:**
    *   Data platform engineering is more focused on building tooling and infrastructure for other data teams.
    *   Some find data platform roles to be too DevOps-heavy.
    *   Others find data platform roles add value for ml/gen ai products.

**[Considering contributing to dbt-core as my first open source project, but I’m afraid it’s slowly dying (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1nlqp6w/considering_contributing_to_dbtcore_as_my_first/)**

*   **Summary:** The discussion centers around the idea of contributing to the dbt-core open-source project, with users weighing the pros and cons and suggesting alternative projects.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiments towards contributing to open source projects in general.
*   **Top 3 Points of View:**
    *   Contributing to dbt-core is still valuable, regardless of its future.
    *   Consider contributing to adapters or other related projects.
    *   Airflow is a good alternative open-source project to contribute to.

**[Data Warehouse Advice (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1nla3bv/data_warehouse_advice/)**

*   **Summary:** Users provide advice on setting up a data warehouse, including selecting vendors, estimating costs, and the necessary skills and expertise.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiments towards suggesting specific solutions.
*   **Top 3 Points of View:**
    *   Consider using a hosted solution like Snowflake or Databricks.
    *   Engage a consultant with data warehousing expertise.
    *   Clearly define business needs before selecting a specific solution.

**[WASM columnar approach (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1nl623u/wasm_columnar_approach/)**

*   **Summary:** The thread discusses the use of WebAssembly (WASM) and columnar databases like DuckDB-WASM in analytics, focusing on its potential in operational tools and limitations in traditional BI.
*   **Emotion:** The overall emotional tone is neutral, with some expressing interest in the technology.
*   **Top 3 Points of View:**
    *   DuckDB-WASM is useful for operational tools and pre-aggregated datasets.
    *   WASM columnar databases have limitations due to browser memory constraints.
    *   This approach can shift more compute to the client and reduces cloud workload.

**[Data Engineering Jobs (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1nlozst/data_engineering_jobs/)**
*   **Summary:** The thread points the user to `/r/dataengineeringjobs`
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *  Unclear, thread is a redirect

**[Is this a common experience? A BI vendor is being heavily pushed regardless of feedback (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1nkrnw2/is_this_a_common_experience_a_bi_vendor_is_being/)**

*   **Summary:** Users discuss the common experience of BI vendors being pushed regardless of feedback, highlighting the reasons behind it and offering advice on how to handle the situation.
*   **Emotion:** The overall emotional tone is neutral, with some negative sentiment expressing frustration with the situation.
*   **Top 3 Points of View:**
    *   Management often pushes for specific BI vendors due to sales pitches or relationships.
    *   Pushback should involve asking the vendor to handle the setup.
    *   These decisions are rarely influenced by the data engineering team.

**[Syncing data from Snowflake to MongoDB using CDC streams (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1nlhkw4/syncing_data_from_snowflake_to_mongodb_using_cdc/)**

*   **Summary:** The thread discusses methods for syncing data from Snowflake to MongoDB using Change Data Capture (CDC) streams, with users suggesting different approaches and tools.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiment related to offering solutions and promoting services.
*   **Top 3 Points of View:**
    *   Using Snowflake Streams and Tasks with a lightweight worker is a viable pattern.
    *   Avoid calling MongoDB directly from Snowflake.
    *   Estuary is a tool that can simplify the process.

**[Poor data quality (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1nlyvjg/poor_data_quality/)**

*   **Summary:** Users discuss the issue of poor data quality, its impact on reports, and strategies for addressing it, including automated checks and data governance.
*   **Emotion:** The overall emotional tone is neutral, with some negative sentiment expressing concern about the frequency of data quality issues.
*   **Top 3 Points of View:**
    *   Data quality issues often stem from upstream data sources.
    *   Implement automated checks to detect data quality issues.
    *   Collaborate with downstream consumers to address data quality problems.

**[Advancing into Senior Roles (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1nm30aq/advancing_into_senior_roles/)**

*   **Summary:** The discussion centers around how to advance into senior roles in data engineering, with users debating the importance of leadership skills and people management.
*   **Emotion:** The overall emotional tone is neutral, with some positive sentiment related to the possibility of advancing without people management.
*   **Top 3 Points of View:**
    *   Leadership is important in senior roles, but doesn't necessarily mean people management.
    *   Mentoring junior engineers is a key aspect of being a senior engineer.
    *   Significant experience and technical competence are required to advance.

**[How to handle custom/dynamic defined fields in dimensions (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1nlgefo/how_to_handle_customdynamic_defined_fields_in/)**

*   **Summary:** The thread explores different options for handling custom/dynamic defined fields in dimensions, with users suggesting approaches like EVA objects, JSON columns, and mini-dims.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   EVA object along with dimension
    *   JSON/Variant column on the dimension
    *   Mini dims

**[Is DSML course from Scaler worth it? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1nm28h0/is_dsml_course_from_scaler_worth_it/)**

*   **Summary:** The thread recommends a list of community-submitted learning resources.
*   **Emotion:** Neutral
*   **Top 3 Points of View:**
    *   N/A, it recommends user to view external link.

**[Advice on allowing multiple users to access an Access database via a GUI without having data loss or corruption? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nlngm5/advice_on_allowing_multiple_users_to_access_an/)**

*   **Summary:** Users provide advice on how to allow multiple users to access an Access database via a GUI without data loss or corruption, primarily recommending migrating to a different database system.
*   **Emotion:** The overall emotional tone is neutral, with some negative sentiment expressing concern about the limitations of Access.
*   **Top 3 Points of View:**
    *   Migrate the database to a more robust system like MySQL or PostgreSQL.
    *   Use a front-end like Dbeaver with MariaDB or PostgreSQL as the database.
    *   Avoid Access DB migration if possible, due to inevitable disasters.

**[Personal Health Data Management (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nlvz6f/personal_health_data_management/)**

*   **Summary:** The thread discusses personal health data management, recommending standards like FHIR and simple databases for getting started.
*   **Emotion:** The overall emotional tone is positive and neutral, with helpful advice.
*   **Top 3 Points of View:**
    *   Use simple databases like DynamoDB or Postgres for personal projects.
    *   Look into the health data standard called FHIR.
    *   "Just do something," get started instead of overthinking.

**[Do data teams even care about CSR, or is it always seen as a distraction? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1nm3sbc/do_data_teams_even_care_about_csr_or_is_it_always/)**

*   **Summary:** Users share their perspectives on whether data teams care about Corporate Social Responsibility (CSR) initiatives, with some viewing it as a distraction.
*   **Emotion:** The overall emotional tone is neutral, with some negative sentiment expressing reluctance to do unpaid work.
*   **Top 3 Points of View:**
    *   CSR should be paid as task
    *   Users don't need their job to guilt them for free work
