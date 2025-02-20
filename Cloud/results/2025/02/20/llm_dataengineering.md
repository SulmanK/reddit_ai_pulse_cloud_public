---
title: "Data Engineering Subreddit"
date: "2025-02-20"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "data", "analytics"]
---

# Overall Ranking and Top Discussions
1.  [What's your ratio of analysts to data engineers?](https://www.reddit.com/r/dataengineering/comments/1iu75id/whats_your_ratio_of_analysts_to_data_engineers/) (Score: 22)
    *   The discussion revolves around the ratio of data analysts to data engineers in different companies and teams.
2.  [Data quality monitoring for data pipelines](https://www.reddit.com/r/dataengineering/comments/1iu1opl/data_quality_monitoring_for_data_pipelines/) (Score: 6)
    *   The discussion focuses on tools and methods for data quality monitoring in data pipelines.
3.  [Using a DWH as a backend?!](https://www.reddit.com/r/dataengineering/comments/1iu2umj/using_a_dwh_as_a_backend/) (Score: 6)
    *   The discussion questions the practice of using a data warehouse (DWH) as a backend for applications, particularly transactional systems.
4.  [Apache Cassandra](https://www.reddit.com/r/dataengineering/comments/1iu3cfm/apache_cassandra/) (Score: 4)
    *   The discussion explores why Apache Cassandra is discussed less frequently and its relevance in modern data architectures.
5.  [Data modelling NYC taxi](https://www.reddit.com/r/dataengineering/comments/1itzndo/data_modelling_nyc_taxi/) (Score: 2)
    *   The discussion discusses data modeling for NYC taxi data, highlighting the importance of proper modeling for query performance and data analysis.
6.  [Extraction of data from saas tools?](https://www.reddit.com/r/dataengineering/comments/1iu1kna/extraction_of_data_from_saas_tools/) (Score: 2)
    *   The discussion talks about the extraction of data from SaaS tools.
7.  [Go an extra mile !](https://www.reddit.com/r/dataengineering/comments/1iu4tml/go_an_extra_mile/) (Score: 2)
    *   The discussion emphasizes the importance of understanding star schemas.
8.  [Do you need a deep knowledge of maths to become a Data Engineer?](https://www.reddit.com/r/dataengineering/comments/1iu6vot/do_you_need_a_deep_knowledge_of_maths_to_become_a/) (Score: 2)
    *   The discussion questions the level of mathematical knowledge required to be a Data Engineer.
9.  [Make a Time Series Animated GIF with Kepler.gl in 5 Minutes](https://www.reddit.com/r/dataengineering/comments/1itzc8z/make_a_time_series_animated_gif_with_keplergl_in/) (Score: 1)
    *   The discussion touches on using Kepler.gl to create time series animated GIFs.
10. [Warehouse data for external clients](https://www.reddit.com/r/dataengineering/comments/1iu00oa/warehouse_data_for_external_clients/) (Score: 1)
    *   The discussion focuses on how to provide warehouse data to external clients.
11. [Advice on Skill development?](https://www.reddit.com/r/dataengineering/comments/1iu177v/advice_on_skill_development/) (Score: 1)
    *   The discussion gives advice on skill development.
12. [How to build a impactful yet budget-friendly personal project](https://www.reddit.com/r/dataengineering/comments/1iu18at/how_to_build_a_impactful_yet_budgetfriendly/) (Score: 1)
    *   The discussion talks about building an impactful personal project.
13. [Fabric for an Enterprise Data Platform?](https://www.reddit.com/r/dataengineering/comments/1iu6sdc/fabric_for_an_enterprise_data_platform/) (Score: 1)
    *   The discussion centers on Fabric for an Enterprise Data Platform.
14. [Azure Synapse Pipeline: Multiple Notebooks vs Single, Consolidates Notebook](https://www.reddit.com/r/dataengineering/comments/1iu8dic/azure_synapse_pipeline_multiple_notebooks_vs/) (Score: 1)
    *   The discussion revolves around Azure Synapse Pipeline.
15. [How do you deal with less-techies-than-you giving you advice?](https://www.reddit.com/r/dataengineering/comments/1iu846x/how_do_you_deal_with_lesstechiesthanyou_giving/) (Score: 0)
    *   The discussion centers on how to deal with people that give advice on a technical topic and have less technical skills.

# Detailed Analysis by Thread
**[What's your ratio of analysts to data engineers? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1iu75id/whats_your_ratio_of_analysts_to_data_engineers/)**
*  **Summary:** People are sharing the ratio of data analysts to data engineers in their respective organizations, with responses ranging from 3:1 to 1:5, solo DE/AE/BIE, and even cases of 0:1 due to layoffs. One person states "Divide by zero error".
*  **Emotion:** The overall emotional tone of the thread is neutral, with people simply sharing data points and experiences.
*  **Top 3 Points of View:**
    *   The ratio of analysts to data engineers varies greatly depending on the company size, industry, and team structure.
    *   Some organizations have a significantly higher number of analysts compared to data engineers.
    *   Layoffs can drastically impact the ratio, leading to situations where there are no analysts or data engineers left.

**[Data quality monitoring for data pipelines (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1iu1opl/data_quality_monitoring_for_data_pipelines/)**
*  **Summary:**  People are discussing tools and methods for data quality monitoring in data pipelines, including DataOps Data Quality TestGen and Great Expectations.
*  **Emotion:** The thread has a neutral to slightly positive emotional tone, with people sharing and recommending tools.
*  **Top 3 Points of View:**
    *   DataOps Data Quality TestGen is a tool that does simple, fast data quality test generation and execution.
    *   Great Expectations is also a tool that is being used for data quality monitoring.
    *   Data quality monitoring is an important aspect of data pipelines.

**[Using a DWH as a backend?! (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1iu2umj/using_a_dwh_as_a_backend/)**
*  **Summary:** The thread questions the practice of using a data warehouse (DWH) as a backend for applications, especially transactional systems, with people largely agreeing that it's generally a bad idea due to performance and architectural differences between OLTP and OLAP systems. However, some exceptions are noted, such as smaller applications or leveraging specific platforms like Snowflake.
*  **Emotion:** The emotional tone is mixed, ranging from negative (expressing concern and disagreement) to positive (acknowledging potential exceptions).
*  **Top 3 Points of View:**
    *   Using a DWH as a backend for transactional systems is generally a bad idea due to performance and architectural differences.
    *   There might be edge cases where it's acceptable, such as append-only event systems or real-time analytics integration.
    *   Platforms like Snowflake are evolving to potentially support both analytical and transactional workloads.

**[Apache Cassandra (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1iu3cfm/apache_cassandra/)**
*  **Summary:**  The discussion explores why Apache Cassandra is discussed less frequently now compared to other databases and its relevance in modern data architectures. People point to the rise of managed NoSQL solutions, operational complexity, and changing application needs as reasons for its decline in popularity.
*  **Emotion:** The overall emotional tone is neutral, analyzing the trends and reasons behind Cassandra's reduced prominence.
*  **Top 3 Points of View:**
    *   Managed NoSQL solutions like DynamoDB and Cosmos DB have become more popular due to ease of maintenance and scaling.
    *   Cassandra's operational complexity and challenging data model make it less appealing compared to newer options.
    *   Hadoop outcompeted Cassandra because it was more flexible and a bigger ecosystem was developed around it.

**[Data modelling NYC taxi (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1itzndo/data_modelling_nyc_taxi/)**
*  **Summary:** The discussion revolves around data modeling for NYC taxi data, highlighting the importance of proper modeling for query performance, data analysis, and preventing data messes.
*  **Emotion:** The emotional tone is positive, with people sharing information on data modeling.
*  **Top 3 Points of View:**
    *   Data modeling helps optimize query performance and storage.
    *   Data model should match the purposes of the users.
    *   Data modeling is an extremely valuable skill to have under the sleeve.

**[Extraction of data from saas tools? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1iu1kna/extraction_of_data_from_saas_tools/)**
*  **Summary:** The thread revolves around suggestions for extracting data from SaaS tools.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Puppeteer is what is needed to extract data from SaaS tools.

**[Go an extra mile ! (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1iu4tml/go_an_extra_mile/)**
*  **Summary:**  The discussion is a one liner that is emphasizing the importance of understanding star schemas.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   People need to understand star schemas.

**[Do you need a deep knowledge of maths to become a Data Engineer? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1iu6vot/do_you_need_a_deep_knowledge_of_maths_to_become_a/)**
*  **Summary:** The discussion questions whether a Data Engineer needs a deep knowledge of maths.
*  **Emotion:** The emotional tone is neutral to slightly negative.
*  **Top 3 Points of View:**
    *   You don’t need to have deep knowledge of math to be a data engineer.
    *   You are expected to have good problem solving and logical reasoning.
    *   Most of the time you'll not be too math dependant.

**[Make a Time Series Animated GIF with Kepler.gl in 5 Minutes (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1itzc8z/make_a_time_series_animated_gif_with_keplergl_in/)**
*  **Summary:** The discussion highlights the use of Kepler.gl for creating time series animated GIFs, while also pointing out the limitation of the tool due to its browser-based nature and data volume constraints.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Kepler.gl is a useful tool for creating time series animated GIFs.
    *   Kepler has some issues with data volume, since it runs in your browser.

**[Warehouse data for external clients (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iu00oa/warehouse_data_for_external_clients/)**
*  **Summary:**  The discussion is about how to provide warehouse data to external clients.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   You can serve external clients through Snowflake's data sharing.

**[Advice on Skill development? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iu177v/advice_on_skill_development/)**
*  **Summary:** The discussion is about giving advice on skill development.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Just check requirements of DE job applications, study and build projects and apply.

**[How to build a impactful yet budget-friendly personal project (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iu18at/how_to_build_a_impactful_yet_budget-friendly/)**
*  **Summary:** The discussion is about building an impactful personal project.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Check out dbt-core with SQLite - completely free and shows real DE skills.

**[Fabric for an Enterprise Data Platform? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iu6sdc/fabric_for_an_enterprise_data_platform/)**
*  **Summary:** The discussion centers on Fabric for an Enterprise Data Platform.
*  **Emotion:** The emotional tone is positive.
*  **Top 3 Points of View:**
    *   The general consensus of Fabric in the subreddit is avoid as much as you can and move towards Snowflake or Databricks.

**[Azure Synapse Pipeline: Multiple Notebooks vs Single, Consolidates Notebook (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1iu8dic/azure_synapse_pipeline_multiple_notebooks_vs/)**
*  **Summary:** The discussion revolves around Azure Synapse Pipeline.
*  **Emotion:** The emotional tone is positive.
*  **Top 3 Points of View:**
    *   Microsoft is planning to consolidate the notebooks in Azure Synapse to reduce the cost.

**[How do you deal with less-techies-than-you giving you advice? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1iu846x/how_do_you_deal_with_lesstechiesthanyou_giving/)**
*  **Summary:** The discussion is about how to deal with people that give advice on a technical topic and have less technical skills.
*  **Emotion:** The emotional tone is positive.
*  **Top 3 Points of View:**
    *   There is a communication issue across both parties.
