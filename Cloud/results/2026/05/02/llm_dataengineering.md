---
title: "Data Engineering Subreddit"
date: "2026-05-02"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions

*   1. [[D] Impress me with your dbt macros](https://www.reddit.com/r/dataengineering/comments/1t1cgjk/impress_me_with_your_dbt_macros/) (Score: 43)
    *   Users shared their custom dbt macros and their use cases, ranging from data flattening and exporting to S3, to handling test failures and creating incremental materializations.
*   2. [[D] 700+ DE applications, 200+ rejections. What is actually working in this market?](https://www.reddit.com/r/dataengineering/comments/1t1r8ok/700_de_applications_200_rejections_what_is/) (Score: 31)
    *   Discussions revolved around the challenges of the current data engineering job market, with users sharing advice on resume tailoring, networking, and the impact of unqualified applicants.
*   3. [[D] Passing data to an LLM](https://www.reddit.com/r/dataengineering/comments/1t1j8mt/passing_data_to_an_llm/) (Score: 13)
    *   The thread explored the complexities of integrating LLMs with data sources, focusing on security, data governance, and the practical implementation of LLM-powered data analysis.
*   4. [[D] Building a vector db from a cnc documentation site: is my rate limiting safe?](https://www.reddit.com/r/dataengineering/comments/1t1l63b/building_a_vector_db_from_a_cnc_documentation/) (Score: 3)
    *   A user sought advice on safe rate limiting practices when building a vector database from documentation, with a suggestion to implement exponential backoff.
*   5. [[D] Need Help](https://www.reddit.com/r/dataengineering/comments/1t1r1q5/need_help/) (Score: 2)
    *   Users provided guidance on data engineering best practices, particularly concerning querying data layers and understanding replication in Azure databases.

# Detailed Analysis by Thread

**[ Impress me with your dbt macros (Score: 43)](https://www.reddit.com/r/dataengineering/comments/1t1cgjk/impress_me_with_your_dbt_macros/)**
*   **Summary:** Users shared their custom dbt macros, including one for flattening array columns across multiple tables, another for exporting empty models to S3, and a macro/test mix for handling source test failures. Other examples include an incremental materialization for handling batched data and idempotency, a macro to check for recently updated tables for incremental loads, a macro for shared fields to ensure DRY principles, a pre-run hook to enforce the use of `--select` arguments, and a complex macro to store test failure results in S3.
*   **Emotion:** Neutral. The sentiment score is generally high across comments, indicating a neutral and informative tone.
*   **Top 3 Points of View:**
    *   The importance of DRY (Don't Repeat Yourself) principles and how macros facilitate this by centralizing common logic, such as shared fields across reports.
    *   The use of macros for data quality and error handling, like flagging key collisions, null spikes, or comparing row counts and hash diffs to catch silent drift and bad data early.
    *   The development of complex and innovative macros for specific, challenging use cases, such as flattening deeply nested array data or creating robust incremental materializations for append-mostly data.

**[ 700+ DE applications, 200+ rejections. What is actually working in this market? (Score: 31)](https://www.reddit.com/r/dataengineering/comments/1t1r8ok/700_de_applications_200_rejections_what_is/)**
*   **Summary:** The discussion centers on the highly competitive data engineering job market. Advice includes tailoring resumes to specific roles, following application instructions, highlighting key strengths, and understanding that recruiters often spend only a brief time reviewing initial applications. Networking and referrals are emphasized as crucial for getting noticed, as many resumes are not thoroughly reviewed, and there's an influx of unqualified candidates, some of whom struggle with basic computer skills.
*   **Emotion:** Mixed. While the topic is about market challenges, the sentiment scores show a mix of Neutral and Negative, reflecting the difficulties but also offering practical advice.
*   **Top 3 Points of View:**
    *   **Resume Tailoring and Clarity:** Candidates need to meticulously tailor their CVs to each job and company, clearly stating their strengths and relevant technologies, rather than listing every tool they've encountered.
    *   **The Importance of Networking and Referrals:** Referrals and introductions are significantly more effective than general applications, often stemming from active community involvement, and are a key way to bypass initial screening filters.
    *   **The Impact of Unqualified Applicants:** A significant number of applicants lack even basic technical proficiency, leading to wasted time for recruiters and hiring managers, and making it harder for genuinely qualified candidates to stand out.

**[ Passing data to an LLM (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1t1j8mt/passing_data_to_an_llm/)**
*   **Summary:** The thread discusses the challenges and best practices for passing data to Large Language Models (LLMs). Key themes include security concerns, data governance, the need for strict access controls, and the method of exposing data through semantic layers or defined views rather than direct table access. There's also debate on the LLMs' ability to interpret complex data and generate accurate SQL queries, with a preference for using LLMs to interpret user intent or assist with code development.
*   **Emotion:** Neutral. Most comments have neutral sentiment scores, indicating a factual and analytical discussion of the topic.
*   **Top 3 Points of View:**
    *   **Security and Data Governance are Paramount:** It is critical to implement robust security measures, including PII scrubbing, limiting access to governed reporting layers, and defining strict query budgets, to prevent misuse and data breaches.
    *   **LLMs are Best for Intent Interpretation and Code Assistance:** While LLMs can aid in code development, their current ability to accurately interpret complex data and generate SQL is debated; they are more effectively used for understanding user intent and rephrasing data.
    *   **Structured Data Exposure is Key:** Instead of direct database access, data should be exposed through well-documented views or semantic layers (like Cube's MCP) that LLMs can query, ensuring controlled and predictable interactions.

**[ Building a vector db from a cnc documentation site: is my rate limiting safe? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1t1l63b/building_a_vector_db_from_a_cnc_documentation/)**
*   **Summary:** A user asked about the safety of their rate limiting when building a vector database from CNC documentation. The advice given was to implement exponential backoff for scrapers and to check for sitemaps or APIs, which can simplify data extraction compared to HTML parsing.
*   **Emotion:** Positive. The sentiment score for the comment is positive, suggesting helpful and constructive advice.
*   **Top 3 Points of View:**
    *   Implementing exponential backoff is crucial for scraper reliability and server friendliness.
    *   Exploring sitemaps or APIs can provide a more efficient data extraction method than direct HTML parsing.
    *   Local scraping is acceptable for initial tests, but production-level operations require more robust error handling.

**[ Need Help (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1t1r1q5/need_help/)**
*   **Summary:** This thread offers advice on data engineering practices, specifically regarding the querying of data layers and understanding database replication. One comment emphasizes the importance of documenting the raw data layer before building transformation logic to avoid rework. Another points out that Azure tables, if replicated, must have a primary key or uniqueness constraint. A question is also raised about whether the Azure databases are supporting applications.
*   **Emotion:** Neutral. The sentiment scores are predominantly neutral, indicating a focus on technical problem-solving and information sharing.
*   **Top 3 Points of View:**
    *   **Document the Raw Layer First:** It's essential to understand and document the contents of the bronze layer (raw data) before building any transformation logic to prevent future rework.
    *   **Replication Implies Uniqueness:** If Azure tables are replicated, they must have a primary key or a mechanism for uniqueness to enable replication.
    *   **Application Dependency:** Understanding whether Azure databases are supporting applications is a key initial question in troubleshooting data infrastructure issues.
