---
title: "Data Engineering Subreddit"
date: "2025-11-09"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Snowflake to Databricks Migration?](https://www.reddit.com/r/dataengineering/comments/1osj0qo/snowflake_to_databricks_migration/) (Score: 39)
    *   The discussion revolves around migrations between Snowflake and Databricks, with some questioning the reasons and motivations behind these migrations.
2.  [How do big companies get all their different systems to talk to one platform?](https://www.reddit.com/r/dataengineering/comments/1osglur/how_do_big_companies_get_all_their_different/) (Score: 18)
    *   The thread discusses the challenges and strategies large companies use to integrate data from disparate systems into a unified platform, including the use of ETL tools, data warehousing, and the involvement of dedicated teams.
3.  [SQL vs Python data pipeline](https://www.reddit.com/r/dataengineering/comments/1osobde/sql_vs_python_data_pipeline/) (Score: 9)
    *   The discussion compares and contrasts the use of SQL and Python for data pipelines, considering factors like performance, use case, and ease of use.
4.  [SSIS for Migration](https://www.reddit.com/r/dataengineering/comments/1oshd0z/ssis_for_migration/) (Score: 9)
    *   The thread discusses the use of SQL Server Integration Services (SSIS) for data migration, with varying opinions on its effectiveness and alternatives.
5.  [Are u building apps?](https://www.reddit.com/r/dataengineering/comments/1osqyd9/are_u_building_apps/) (Score: 5)
    *   The discussion centers on whether data engineers are building applications, with mention of tools like Streamlit, React, and R Shiny for app development.
6.  [After a DW migration](https://www.reddit.com/r/dataengineering/comments/1osk7z8/after_a_dw_migration/) (Score: 5)
    *   The conversation covers the costs and challenges associated with data warehouse migrations, particularly in cloud environments like Snowflake and Databricks.
7.  [If serialisability is enforced in the app/middleware, is it safe to relax DB isolation (e.g., to READ COMMITTED)?](https://www.reddit.com/r/dataengineering/comments/1osm6x8/if_serialisability_is_enforced_in_the/) (Score: 3)
    *   The thread discusses database isolation levels and whether it's safe to relax them if serializability is enforced at the application or middleware layer.
8.  [Connect/Extract data from Facebook/Instagram to a Power Bi dashboard](https://www.reddit.com/r/dataengineering/comments/1osm0r4/connectextract_data_from_facebookinstagram_to_a/) (Score: 3)
    *   This thread is a request for resources on connecting and extracting data from Facebook/Instagram to a Power BI dashboard.
9.  [What the *** is unstructured data modeling?](https://www.reddit.com/r/dataengineering/comments/1osu4ng/what_the_hell_is_unstructured_data_modeling/) (Score: 2)
    *   The discussion defines unstructured data and touches on how it is handled, as well as its relative importance in the field of data engineering.
10. [About to start at WGU. Should I go for the BSSWE or BSCS degree if I want to to pursue a career in DE?](https://www.reddit.com/r/dataengineering/comments/1osts4l/about_to_start_at_wgu_should_i_go_for_the_bsswe/) (Score: 2)
    *   This thread is a question about which degree path at WGU is most suitable for a data engineering career.
11. [Experience in creating a proper database within a team that has a questionable data entry process](https://www.reddit.com/r/dataengineering/comments/1osaqtl/experience_in_creating_a_proper_database_within_a/) (Score: 1)
    *   The thread seeks advice on building a database for a team with poor data entry practices, with suggestions ranging from using CRMs to implementing standardized data entry processes.

# Detailed Analysis by Thread
**[Snowflake to Databricks Migration? (Score: 39)](https://www.reddit.com/r/dataengineering/comments/1osj0qo/snowflake_to_databricks_migration/)**
*  **Summary:**  The discussion revolves around the trend of migrating between Snowflake and Databricks, with users questioning the reasons behind these migrations and suggesting that companies may be chasing the "flavor of the month" or responding to better deals from vendors. Some users see more clients interested in Databricks currently, while others find their clients looking to move from Databricks to Snowflake. The possibility of guerrilla marketing from Databricks and the influence of individual experiences on perceptions are also discussed.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Companies migrate to whichever platform gives them a better deal.
    *   Migrations are often driven by chasing trends rather than making existing platforms better.
    *   The perception of migration trends is influenced by individual experiences and the platforms one is already familiar with.

**[How do big companies get all their different systems to talk to one platform? (Score: 18)](https://www.reddit.com/r/dataengineering/comments/1osglur/how_do_big_companies_get_all_their_different/)**
*  **Summary:**  The thread explores how large companies integrate data from various systems into a single platform. It mentions using a portfolio of connectors from tools like Fivetran, Airflow, and Streamsets, along with custom APIs and SQL extracts. The importance of data modeling and harmonization is highlighted, as well as the use of data warehouses.  Some users pointed out that a lot of organizations do not have one platform.
*  **Emotion:** The emotional tone is generally Neutral.
*  **Top 3 Points of View:**
    *   A combination of ETL tools, custom code, and data warehousing is used to integrate data.
    *   Data modeling and harmonization are critical for making the data usable.
    *   Business Intelligence (BI) and Data Engineering (DE) are interconnected, but distinct disciplines.

**[SQL vs Python data pipeline (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1osobde/sql_vs_python_data_pipeline/)**
*  **Summary:** The discussion contrasts SQL and Python for data pipelines, weighing factors such as performance, specific use cases like AI/ML, and personal preference. SQL is favored for basic cleaning and transformations, while Python is preferred for feature engineering in AI/ML workloads. CTEs are mentioned as faster than pandas dataframes in some scenarios. The role of dataframes in the context of Python pipelines is also discussed.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   SQL is better for basic cleaning and transformations in typical reporting workloads.
    *   Python is more suitable for complex feature engineering in AI/ML.
    *   The choice depends on the specific requirements and transformations needed.

**[SSIS for Migration (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1oshd0z/ssis_for_migration/)**
*  **Summary:**  The thread discusses the use of SSIS (SQL Server Integration Services) for data migration. Some users express strong dislike for SSIS, citing maintainability issues, string type problems, and Excel import difficulties. Others consider it a fast tool and a leading ETL platform. Paid platforms are suggested as alternatives for their risk mitigation and operational support.
*  **Emotion:** The emotional tone is mixed, with both Negative and Positive sentiments expressed.
*  **Top 3 Points of View:**
    *   SSIS is disliked for its maintainability issues and problems with data types.
    *   SSIS is considered a fast and effective ETL platform.
    *   Paid platforms offer benefits like better support and reduced risk, even though SSIS can work.

**[Are u building apps? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1osqyd9/are_u_building_apps/)**
*  **Summary:**  The discussion addresses whether data engineers are involved in building applications.  Some participate in app development, with Streamlit being a popular choice for smaller apps. Other options mentioned are React and R Shiny.
*  **Emotion:** The emotional tone is mixed, with some Positive sentiments.
*  **Top 3 Points of View:**
    *   Data engineers are sometimes involved in building applications.
    *   Streamlit is a favored tool for creating small applications.
    *   ORM and OOP aren't necessary in a data-intensive application.

**[After a DW migration (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1osk7z8/after_a_dw_migration/)**
*  **Summary:** The thread discusses the costs and benefits after a Data Warehouse (DW) migration to the cloud, particularly Snowflake and Databricks. The general sentiment is that cloud solutions might not necessarily save money, but they offer advantages in terms of maintenance and upgrades.  The persistence of legacy systems after migration is also mentioned, adding to overall costs.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Cloud DW migrations might not always result in cost savings.
    *   Maintenance and upgrade costs are lower in cloud DWs.
    *   Legacy systems often persist after migration, increasing costs.

**[If serialisability is enforced in the app/middleware, is it safe to relax DB isolation (e.g., to READ COMMITTED)? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1osm6x8/if_serialisability_is_enforced_in_the/)**
*  **Summary:** The discussion explores whether it's safe to relax database isolation levels (e.g., to READ COMMITTED) if serializability is enforced at the application or middleware level. One response recommends using READ COMMITTED SNAPSHOT in SQL Server and exclusive locks.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Relying on client code to enforce change ordering is reasonable if the app is the only database writer.
    *   Database isolation levels should be treated the same across all service accounts.
    *   READ COMMITTED SNAPSHOT and exclusive locks are recommended for SQL Server.

**[Connect/Extract data from Facebook/Instagram to a Power Bi dashboard (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1osm0r4/connectextract_data_from_facebookinstagram_to_a/)**
*  **Summary:**  This thread simply directs the user to community-submitted learning resources for data engineering.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The user should check this page for information https://dataengineering.wiki/Learning+Resources

**[What the *** is unstructured data modeling? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1osu4ng/what_the_hell_is_unstructured_data_modeling/)**
*  **Summary:** The discussion centers on defining unstructured data and its modeling. Unstructured data includes emails, documents, images, videos, and audio files. The modeling involves organizing it for access and search.  It's noted that many data engineers don't deal with unstructured data.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Unstructured data consists of non-tabular data types like documents, images, and videos.
    *   Unstructured data modeling focuses on organizing and enabling access/search, rather than strict schemas.
    *   Most data engineers do not work with unstructured data.

**[About to start at WGU. Should I go for the BSSWE or BSCS degree if I want to to pursue a career in DE? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1osts4l/about_to_start_at_wgu_should_i_go_for_the_bsswe/)**
*  **Summary:** The thread is a question about the best degree path for a data engineering career at WGU. There's a suggestion to consider the Data Analytics program with specific electives, and a pointer to a community guide about transitioning into Data Engineering.
*  **Emotion:** The overall emotional tone is Positive.
*  **Top 3 Points of View:**
    *   Consider the Data Analytics program with specific electives at WGU.
    *   The user should check this page for information https://dataengineering.wiki/FAQ/How+can+I+transition+into+Data+Engineering

**[Experience in creating a proper database within a team that has a questionable data entry process (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1osaqtl/experience_in_creating_a_proper_database_within_a/)**
*  **Summary:** The thread seeks advice on creating a database within a team with poor data entry practices. Suggestions include using a CRM, standardizing data entry, and using tools like MS Forms and Power Automate.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The team might need a CRM more than a custom database.
    *   Focus on process improvements and data entry standardization.
    *   Start with simple tools like MS Forms and Power Automate.
