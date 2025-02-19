---
title: "Data Engineering Subreddit"
date: "2025-02-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Gold Layer: Wide vs Fact Tables](https://www.reddit.com/r/dataengineering/comments/1it5wn1/gold_layer_wide_vs_fact_tables/) (Score: 53)
    *  The thread discusses the pros and cons of using wide tables versus fact tables with dimensions in the gold layer of a data warehouse, particularly in the context of Power BI.
2.  [LangChain Feels Like an ETL Framework – Should We Use Traditional ETL for RAG](https://www.reddit.com/r/dataengineering/comments/1it988q/langchain_feels_like_an_etl_framework_should_we/) (Score: 16)
    *  The thread explores whether LangChain can be considered an ETL framework and if traditional ETL tools should be used for Retrieval-Augmented Generation (RAG) implementations.
3.  [Data Products: A Case Against Medallion Architecture](https://moderndata101.substack.com/p/data-products-a-case-against-medallion) (Score: 15)
    *   The thread discusses an article presenting a case against the Medallion architecture in favor of data products, focusing on the implications and potential drawbacks of each approach.
4.  [Banking + Open Source ETL: Am I Crazy or Is This Doable?](https://www.reddit.com/r/dataengineering/comments/1itepsk/banking_open_source_etl_am_i_crazy_or_is_this/) (Score: 9)
    *   The thread discusses the feasibility and challenges of using open-source ETL tools in the banking industry.
5.  [You don't need a gold layer](https://www.reddit.com/r/dataengineering/comments/1itese4/you_dont_need_a_gold_layer/) (Score: 9)
    *   The thread discusses the necessity of a gold layer in data architecture.
6.  [Does anyone have a remotely enjoyable New Data Request Process?](https://www.reddit.com/r/dataengineering/comments/1itcln0/does_anyone_have_a_remotely_enjoyable_new_data/) (Score: 6)
    *   The thread discusses strategies for implementing a streamlined and efficient data request process.
7.  [Cheap and painless way to easily host dbt docs?](https://www.reddit.com/r/dataengineering/comments/1iteu31/cheap_and_painless_way_to_easily_host_dbt_docs/) (Score: 6)
    *   The thread explores different options for hosting dbt documentation in a cheap, painless, and secure manner.
8.  [Pandas: how to keep date-like from becoming datetime type?](https://www.reddit.com/r/dataengineering/comments/1itddg9/pandas_how_to_keep_datelike_from_becoming/) (Score: 3)
    *   The thread discusses how to prevent Pandas from automatically converting date-like strings to datetime objects.
9.  [Advice for dbt certification](https://www.reddit.com/r/dataengineering/comments/1ite9qm/advice_for_dbt_certification/) (Score: 2)
    *   The thread requests advice and resources for preparing for dbt certification.
10. [Best approach for handling surrogate keys and relationships in a read-only database for analytics](https://www.reddit.com/r/dataengineering/comments/1item2v/best_approach_for_handling_surrogate_keys_and/) (Score: 2)
    *   The thread seeks advice on the best way to handle surrogate keys and relationships in a read-only database used for analytics.
11. [Guidance on career switch: Within Data Field](https://www.reddit.com/r/dataengineering/comments/1it8oau/guidance_on_career_switch_within_data_field/) (Score: 1)
    *   The thread requests guidance on resources for learning about data engineering.
12. [People who work with DE remotely for the US from other countries](https://www.reddit.com/r/dataengineering/comments/1it4uhf/people_who_work_with_de_remotely_for_the_us_from/) (Score: 0)
    *   The thread discusses the challenges and realities of working remotely as a Data Engineer for US-based companies from other countries.
13. [Opinion Validation and Knowledge Base Improvement](https://www.reddit.com/r/dataengineering/comments/1itcov4/opinion_validation_and_knowledge_base_improvement/) (Score: 0)
    *   The thread discusses the value of a particular architecture design tool.
14. [Am I underpaid?](https://www.reddit.com/r/dataengineering/comments/1itemuq/am_i_underpaid/) (Score: 0)
    *   The thread asks if the poster is underpaid in Europe.
15. [Is It Time to Say Goodbye to Data Engineers? - The Data Engineering Dilemma [Seattle Data Guy]](https://www.youtube.com/watch?v=4FcG_ocJ41Y) (Score: 0)
    *   The thread discusses the relevance of data engineering in the present time.

# Detailed Analysis by Thread
**[Gold Layer: Wide vs Fact Tables (Score: 53)](https://www.reddit.com/r/dataengineering/comments/1it5wn1/gold_layer_wide_vs_fact_tables/)**
*  **Summary:** The thread discusses the pros and cons of using wide tables versus fact tables with dimensions in the gold layer of a data warehouse, particularly in the context of Power BI.
*  **Emotion:** The overall emotional tone is neutral, with comments presenting both sides of the argument.
*  **Top 3 Points of View:**
    *   Wide tables can be easier for quick and dirty solutions, but dimensional models are more powerful in the long run.
    *   Fact tables with dimensions are standard for a reason, but wide tables can be explored for simplicity, especially for newcomers.
    *   Power BI is designed for a star schema, so fact tables and dimensions work best.

**[LangChain Feels Like an ETL Framework – Should We Use Traditional ETL for RAG (Score: 16)](https://www.reddit.com/r/dataengineering/comments/1it988q/langchain_feels_like_an_etl_framework_should_we/)**
*  **Summary:** The thread explores whether LangChain can be considered an ETL framework and if traditional ETL tools should be used for Retrieval-Augmented Generation (RAG) implementations.
*  **Emotion:** The overall emotional tone is neutral, with a slight positive leaning due to agreement about LangChain being complicated.
*  **Top 3 Points of View:**
    *   LangChain is too high-level and its interface changes frequently, making direct implementation a more stable option.
    *   LangChain's value lies in tracking input/output of LLMs and token consumption, making it more of an orchestrator.
    *   Consider using Ray to scale data-oriented steps of RAG rather than Spark.

**[Data Products: A Case Against Medallion Architecture (Score: 15)](https://moderndata101.substack.com/p/data-products-a-case-against-medallion)**
*  **Summary:** The thread discusses an article presenting a case against the Medallion architecture in favor of data products, focusing on the implications and potential drawbacks of each approach.
*  **Emotion:** The overall emotional tone is neutral, with elements of negativity expressing skepticism about the proposed alternative to the Medallion architecture.
*  **Top 3 Points of View:**
    *   The Medallion architecture is successful because it requires less context to implement.
    *   Data product approach requires amazing requirements specifications and deep knowledge of data structures.
    *   The Medallion design is a natural way of visualizing data lifecycle and compartmentalizing processes.

**[Banking + Open Source ETL: Am I Crazy or Is This Doable? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1itepsk/banking_open_source_etl_am_i_crazy_or_is_this/)**
*  **Summary:** The thread discusses the feasibility and challenges of using open-source ETL tools in the banking industry.
*  **Emotion:** The emotional tone is neutral, focusing on practical advice and questions.
*  **Top 3 Points of View:**
    *   Consider optimizing current ETL processes before switching to open source.
    *   Data processing logic should be looked at rather than the ETL tool.
    *   Open source ETL tools are a feasible option.

**[You don't need a gold layer (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1itese4/you_dont_need_a_gold_layer/)**
*  **Summary:** The thread discusses the necessity of a gold layer in data architecture.
*  **Emotion:** The overall emotional tone is neutral, reflecting disagreement with the headline.
*  **Top 3 Points of View:**
    *   A gold layer is necessary for different schemas for API consumers vs Power BI.
    *   Medallion architecture is just marketing hype for people who don't understand data.
    *   The gold layer should be the bigger version of the star model.

**[Does anyone have a remotely enjoyable New Data Request Process? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1itcln0/does_anyone_have_a_remotely_enjoyable_new_data/)**
*  **Summary:** The thread discusses strategies for implementing a streamlined and efficient data request process.
*  **Emotion:** The overall emotional tone is neutral, focusing on practical solutions and shared experiences.
*  **Top 3 Points of View:**
    *   A two-stage request process with a short initial form followed by a structured discussion works well.
    *   Long forms are never fully filled out; a phone call is necessary to hammer out the details.
    *   Quickly providing a dataset to the analyst, even if not perfect, helps them understand what is missing.

**[Cheap and painless way to easily host dbt docs? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1iteu31/cheap_and_painless_way_to_easily_host_dbt_docs/)**
*  **Summary:** The thread explores different options for hosting dbt documentation in a cheap, painless, and secure manner.
*  **Emotion:** The overall emotional tone is neutral, focusing on practical solutions and recommendations.
*  **Top 3 Points of View:**
    *   Use S3 as a static site with a VPN.
    *   Use AWS Amplify with HTTPS and basic authentication.
    *   Run dbt docs with the static flag and drop them in a bucket.

**[Pandas: how to keep date-like from becoming datetime type? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1itddg9/pandas_how_to_keep_datelike_from_becoming/)**
*  **Summary:** The thread discusses how to prevent Pandas from automatically converting date-like strings to datetime objects.
*  **Emotion:** The overall emotional tone is neutral, with users seeking and providing technical assistance.
*  **Top 2 Points of View:**
    *   Read every frame as dtype=str and then explicitly retype columns as needed.
    *   Unable to replicate the issue in the local environment

**[Advice for dbt certification (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1ite9qm/advice_for_dbt_certification/)**
*  **Summary:** The thread requests advice and resources for preparing for dbt certification.
*  **Emotion:** The overall emotional tone is neutral, with the post containing a reference link to learning resources.
*  **Top 1 Points of View:**
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[Best approach for handling surrogate keys and relationships in a read-only database for analytics (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1item2v/best_approach_for_handling_surrogate_keys_and/)**
*  **Summary:** The thread seeks advice on the best way to handle surrogate keys and relationships in a read-only database used for analytics.
*  **Emotion:** The overall emotional tone is neutral, with the post containing a solution.
*  **Top 1 Points of View:**
    *   Copy into another database for OLAP is the usual approach for batch-viable pipelines

**[Guidance on career switch: Within Data Field (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1it8oau/guidance_on_career_switch_within_data_field/)**
*  **Summary:** The thread requests guidance on resources for learning about data engineering.
*  **Emotion:** The overall emotional tone is neutral, with the post containing a reference link to learning resources.
*  **Top 1 Points of View:**
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources

**[People who work with DE remotely for the US from other countries (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1it4uhf/people_who_work_with_de_remotely_for_the_us_from/)**
*  **Summary:** The thread discusses the challenges and realities of working remotely as a Data Engineer for US-based companies from other countries.
*  **Emotion:** The overall emotional tone is neutral, with the post containing challenges for leetcode.
*  **Top 1 Points of View:**
    *   75% of companies won't want to hire Leetcode. Even if you are highly desirable, you're going to make less. There's less demand for overseas jobs.

**[Opinion Validation and Knowledge Base Improvement (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1itcov4/opinion_validation_and_knowledge_base_improvement/)**
*  **Summary:** The thread discusses the value of a particular architecture design tool.
*  **Emotion:** The overall emotional tone is neutral, with the post containing challenges for leetcode.
*  **Top 1 Points of View:**
    *   This tool seems to apply only to greenfield architectures. New architecture standup is the difficult part of architectural design. Technical architecture generally has to happen in a phased approach. It's something that you build up to.

**[Am I underpaid? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1itemuq/am_i_underpaid/)**
*  **Summary:** The thread asks if the poster is underpaid in Europe.
*  **Emotion:** The overall emotional tone is neutral, with the post containing challenges for leetcode.
*  **Top 2 Points of View:**
    *   maybe ask an aggregator instead of randoms ... i'd say you're doing swimmingly considering everyone probably makes fun of you behind your back and you can't ever know.
    *   If u have only 3 years of exp , 54k is a very good salary for europe.

**[Is It Time to Say Goodbye to Data Engineers? - The Data Engineering Dilemma [Seattle Data Guy] (Score: 0)](https://www.youtube.com/watch?v=4FcG_ocJ41Y)**
*  **Summary:** The thread discusses the relevance of data engineering in the present time.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Every manager or executive can get by without data engineers. Data engineers are not serious players anyway. Most of the time they are needed because of how bad corporate data governance becomes without them.
    *   Businesses that do not have data engineers are irresponsible.
    *   *** video that’s just trying to be relevant.
