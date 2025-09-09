---
title: "Data Engineering Subreddit"
date: "2025-07-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Do companies like "Astronomer" even have real customers](https://www.reddit.com/r/dataengineering/comments/1m2f6w1/do_companies_like_astronomer_even_have_real/) (Score: 78)
    *   The discussion revolves around the legitimacy and business model of Astronomer, a company providing managed Airflow services.
2.  [Multi-repo vs Monorepo Architechture: Which do you use?](https://www.reddit.com/r/dataengineering/comments/1m1u7u5/multirepo_vs_monorepo_architechture_which_do_you/) (Score: 38)
    *   This thread discusses the pros and cons of using a multi-repo versus a monorepo architecture for data engineering projects.
3.  [Is anyone already using SQLMesh in production? Any features you are missing from dbt?](https://www.reddit.com/r/dataengineering/comments/1m2caev/is_anyone_already_using_sqlmesh_in_production_any/) (Score: 14)
    *   Users share their experiences with SQLMesh in production, comparing its features to dbt (data build tool) and highlighting missing functionalities.
4.  [Churning out data pipelines as a DA](https://www.reddit.com/r/dataengineering/comments/1m1yt2n/churning_out_data_pipelines_as_a_da/) (Score: 7)
    *   The thread is about a data analyst who is building data pipelines and seeking advice on transitioning to a data engineer role.
5.  [Transition to DE](https://www.reddit.com/r/dataengineering/comments/1m23rzb/transition_to_de/) (Score: 7)
    *   This discussion focuses on how to successfully transition into a Data Engineering role, with advice on leveraging current experience and upskilling.
6.  [two pages cv for solo consultant?](https://www.reddit.com/r/dataengineering/comments/1m276g0/two_pages_cv_for_solo_consultant/) (Score: 7)
    *   The discussion revolves around the appropriate length and content of a CV for a solo data engineering consultant.
7.  [What project are you currently working on at your company?](https://www.reddit.com/r/dataengineering/comments/1m2f96f/what_project_are_you_currently_working_on_at_your/) (Score: 7)
    *   Data engineers share details about the projects they are currently working on, including the tools and technologies they use.
8.  [Productionizing Dead Letter Queues in PySpark Streaming Pipelines – Part 2 (Medium Article)](https://www.reddit.com/r/dataengineering/comments/1m1uy7i/productionizing_dead_letter_queues_in_pyspark/) (Score: 5)
    *   The thread discusses productionizing Dead Letter Queues in PySpark Streaming Pipelines.
9.  [How important is the company brand on my profile in the future?](https://www.reddit.com/r/dataengineering/comments/1m295tm/how_important_is_the_company_brand_on_my_profile/) (Score: 5)
    *   Users discuss the importance of company brand recognition on a data engineer's profile and its impact on future career prospects.
10. [How do I integrate an MWAA with a dbt repo?](https://www.reddit.com/r/dataengineering/comments/1m21s7f/how_do_i_integrate_an_mwaa_with_a_dbt_repo/) (Score: 3)
    *   The thread asks about how to integrate an MWAA (Managed Workflow for Apache Airflow) with a dbt repository.
11. [Processing large volume of records through Open AI gpt 4o endpoints](https://www.reddit.com/r/dataengineering/comments/1m285qe/processing_large_volume_of_records_through_open/) (Score: 3)
    *   Users discuss strategies and potential issues when processing a large number of records through OpenAI's GPT-4o endpoints.
12. [Storing historical data for analysis](https://www.reddit.com/r/dataengineering/comments/1m2af8l/storing_historical_data_for_analysis/) (Score: 3)
    *   The discussion is about the best practices for storing historical data for analysis in a data warehouse.
13. [Tasked with migration to Open Table Formats at company, seeking for guidance](https://www.reddit.com/r/dataengineering/comments/1m2dwuj/tasked_with_migration_to_open_table_formats_at/) (Score: 3)
    *   This thread is about a discussion regarding migrating to Open Table Formats, where the user is seeking for guidance.
14. [Career switch from biotech to DE](https://www.reddit.com/r/dataengineering/comments/1m20hlw/career_switch_from_biotech_to_de/) (Score: 2)
    *   The thread discusses the possibility and challenges of switching careers from the biotechnology field to data engineering.
15. [Looking for feedback on Bossocoder’s Data Engineering course](https://www.reddit.com/r/dataengineering/comments/1m2f6a8/looking_for_feedback_on_bossocoders_data/) (Score: 1)
    *   The discussion is about user is looking for feedback on Bossocoder’s Data Engineering course
16. [How to leverage a job with Mechanical engineering background](https://www.reddit.com/r/dataengineering/comments/1m1uqmg/how_to_leverage_a_job_with_mechanical_engineering/) (Score: 0)
    *   This thread is about a mechanical engineer looking to transition into data engineering.

# Detailed Analysis by Thread
**[[D] Do companies like "Astronomer" even have real customers (Score: 78)](https://www.reddit.com/r/dataengineering/comments/1m2f6w1/do_companies_like_astronomer_even_have_real/)**
*  **Summary:** The discussion revolves around the legitimacy and business model of Astronomer, a company providing managed Airflow services. Users discuss whether Astronomer provides real value to its customers, especially in comparison to self-hosting Airflow or using alternatives like MWAA.
*  **Emotion:** The overall emotional tone is neutral, with a mix of positive and neutral sentiments. Some users express skepticism, while others share positive experiences using Astronomer.
*  **Top 3 Points of View:**
    *   Astronomer is a legitimate business that provides value by managing Airflow for companies that don't want to handle the infrastructure themselves.
    *   Astronomer is expensive for what it offers, especially when compared to self-hosting Airflow or using alternatives like MWAA.
    *   Companies may choose Astronomer due to shareholder preferences for variable OPEX over fixed OPEX, even if it ends up being more costly.

**[Multi-repo vs Monorepo Architechture: Which do you use? (Score: 38)](https://www.reddit.com/r/dataengineering/comments/1m1u7u5/multirepo_vs_monorepo_architechture_which_do_you/)**
*  **Summary:** This thread discusses the pros and cons of using a multi-repo versus a monorepo architecture for data engineering projects. Users share their experiences with each approach and discuss factors that influence their choice.
*  **Emotion:** The overall emotional tone is neutral, with users presenting arguments and sharing experiences in an objective manner. Some slightly positive sentiments when expressing preference.
*  **Top 3 Points of View:**
    *   Monorepos are easier to manage and promote code reuse, especially with good branching policies, but require a large team to manage.
    *   Multi-repos allow for independent deployments and easier setup/IDE integration, especially when splitting by language or framework.
    *   The choice between monorepo and multi-repo depends on how changes will be released and the level of coupling desired between components.

**[Is anyone already using SQLMesh in production? Any features you are missing from dbt? (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1m2caev/is_anyone_already_using_sqlmesh_in_production_any/)**
*  **Summary:** Users share their experiences with SQLMesh in production, comparing its features to dbt (data build tool) and highlighting missing functionalities.
*  **Emotion:** The overall emotional tone is somewhat negative due to the expression of features missing from dbt.
*  **Top 3 Points of View:**
    *   SQLMesh is super fast and the Git diff workflow is nice.
    *   SQLMesh is missing the flexibility around materializations as in dbt.
    *   SQLMesh is missing multi-data source and reverse ETL capabilities.

**[Churning out data pipelines as a DA (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m1yt2n/churning_out_data_pipelines_as_a_da/)**
*  **Summary:** The thread is about a data analyst who is building data pipelines and seeking advice on transitioning to a data engineer role. Commenters encourage the DA to apply for DE positions, highlighting their relevant experience.
*  **Emotion:** The overall emotional tone is positive, with users offering encouragement and support to the original poster.
*  **Top 3 Points of View:**
    *   The poster already has sufficient experience to apply for data engineer roles.
    *   Listing relevant experiences and asking software engineers for references can aid the job search.
    *   The poster should be confident in their abilities and seek a title and compensation that matches their contributions.

**[Transition to DE (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m23rzb/transition_to_de/)**
*  **Summary:** This discussion focuses on how to successfully transition into a Data Engineering role, with advice on leveraging current experience and upskilling.
*  **Emotion:** The overall emotional tone is positive and neutral, with users providing practical advice and resources.
*  **Top 3 Points of View:**
    *   Focus on applying first principles and showcasing relevant experience on your resume.
    *   Consider transitioning internally within your current company if a DE team exists.
    *   Utilize community learning resources to acquire necessary skills and knowledge.

**[two pages cv for solo consultant? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m276g0/two_pages_cv_for_solo_consultant/)**
*  **Summary:** The discussion revolves around the appropriate length and content of a CV for a solo data engineering consultant.
*  **Emotion:** The overall emotional tone is neutral, with users sharing their opinions and experiences regarding CV length.
*  **Top 3 Points of View:**
    *   A two-page CV is acceptable as long as all the content is relevant.
    *   After many years of experience, limiting oneself to one page is unnecessary.
    *   Having a website with a portfolio or using LinkedIn projects can be a better alternative to a traditional CV.

**[What project are you currently working on at your company? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1m2f96f/what_project_are_you_currently_working_on_at_your/)**
*  **Summary:** Data engineers share details about the projects they are currently working on, including the tools and technologies they use.
*  **Emotion:** The overall emotional tone is neutral, as users are mainly describing their projects in an objective manner. A couple of comments carry positive sentiments.
*  **Top 3 Points of View:**
    *   Building metadata-driven pipelines to land data into a lake house in fabric.
    *   Getting unstructured data from PDFs into medallion architecture for RAG and search using a vector DB.
    *   Building pyspark data pipelines in Databricks to bring healthcare data and exposing the Unity catalog to Thoughtspot for analytics and AI use cases.

**[Productionizing Dead Letter Queues in PySpark Streaming Pipelines – Part 2 (Medium Article) (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1m1uy7i/productionizing_dead_letter_queues_in_pyspark/)**
*  **Summary:** The thread discusses productionizing Dead Letter Queues in PySpark Streaming Pipelines.
*  **Emotion:** The overall emotional tone is Negative due to comments about Spark streaming.
*  **Top 3 Points of View:**
    *   Spark streaming is a hot mess, PySpark even more so.

**[How important is the company brand on my profile in the future? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1m295tm/how_important_is_the_company_brand_on_my_profile/)**
*  **Summary:** Users discuss the importance of company brand recognition on a data engineer's profile and its impact on future career prospects.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Company brand matters as it can attract more interviews in the future.
    *   The actual work and skills developed are more important than the company brand.

**[How do I integrate an MWAA with a dbt repo? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m21s7f/how_do_i_integrate_an_mwaa_with_a_dbt_repo/)**
*  **Summary:** The thread asks about how to integrate an MWAA (Managed Workflow for Apache Airflow) with a dbt repository.
*  **Emotion:** The overall emotional tone is neutral, with factual information and links being provided.
*  **Top 3 Points of View:**
    *   Use the ecsruntask operator.
    *   Consult the AWS documentation for samples.

**[Processing large volume of records through Open AI gpt 4o endpoints (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m285qe/processing_large_volume_of_records_through_open/)**
*  **Summary:** Users discuss strategies and potential issues when processing a large number of records through OpenAI's GPT-4o endpoints.
*  **Emotion:** The overall emotional tone is positive and neutral.
*  **Top 3 Points of View:**
    *   Use async requests.
    *   Every LLM provider has a batch api now.
    *   Check if memory issue.

**[Storing historical data for analysis (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m2af8l/storing_historical_data_for_analysis/)**
*  **Summary:** The discussion is about the best practices for storing historical data for analysis in a data warehouse.
*  **Emotion:** The overall emotional tone is neutral, with users providing technical suggestions and resources.
*  **Top 3 Points of View:**
    *   Use Slowly Changing Dimension type 2.
    *   Consider using daily snapshots with timestamps.

**[Tasked with migration to Open Table Formats at company, seeking for guidance (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1m2dwuj/tasked_with_migration_to_open_table_formats_at/)**
*  **Summary:** This thread is about a discussion regarding migrating to Open Table Formats, where the user is seeking for guidance.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[Career switch from biotech to DE (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1m20hlw/career_switch_from_biotech_to_de/)**
*  **Summary:** The thread discusses the possibility and challenges of switching careers from the biotechnology field to data engineering.
*  **Emotion:** The overall emotional tone is neutral, with users offering advice and insights on the transition.
*  **Top 3 Points of View:**
    *   The market is better than a wet lab scientist.
    *   Bioinformatics is a more specialized area to start.
    *   It's difficult to get into entry level positions.

**[Looking for feedback on Bossocoder’s Data Engineering course (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1m2f6a8/looking_for_feedback_on_bossocoders_data/)**
*  **Summary:** The discussion is about user is looking for feedback on Bossocoder’s Data Engineering course
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[How to leverage a job with Mechanical engineering background (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1m1uqmg/how_to_leverage_a_job_with_mechanical_engineering/)**
*  **Summary:** This thread is about a mechanical engineer looking to transition into data engineering.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Market yourself as a DE. Ur mech Eng degree won’t help you much but will just tell employers you’re competent
    *   Are you interested in transitioning into Data Engineering? Read our community guide: https://dataengineering.wiki/FAQ/How+can+I+transition+into+Data+Engineering
    *   data engineering for data coming in from sensors and equipment. plenty of data in robotics.
