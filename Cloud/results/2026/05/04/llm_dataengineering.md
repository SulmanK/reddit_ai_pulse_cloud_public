---
title: "Data Engineering Subreddit"
date: "2026-05-04"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "data pipelines", "OLAP", "dbt", "AI"]
---

# Overall Ranking and Top Discussions
*   1. [[How can I gain an understanding on how big corps like Google handle their data?](https://www.reddit.com/r/dataengineering/comments/1t3a5jr/how_can_i_gain_an_understanding_on_how_big_corps/)] (Score: 25)
    *   Discussions focused on learning about how large corporations manage their data, with recommendations for books and resources on scalable data systems.
*   2. [[Solo DE managing pipelines](https://www.reddit.com/r/dataengineering/comments/1t31azn/solo_de_managing_pipelines/)] (Score: 25)
    *   Advice for solo data engineers on managing pipelines, emphasizing robust foundations, version control, testing environments, and the importance of not being entirely solo.
*   3. [[OLAP Server](https://www.reddit.com/r/dataengineering/comments/1t361hu/olap_server/)] (Score: 19)
    *   Users discussed various technologies and approaches for OLAP servers, considering factors like cost, scalability, and suitability for academic projects.
*   4. [[IceStream - enabling efficient streaming writes in Apache Iceberg](https://github.com/jordepic/icestream)] (Score: 8)
    *   A discussion about a new tool for Iceberg, with questions about its long-term maintenance and critiques of its reliance on Cassandra and suitability for certain data workloads.
*   5. [[How do you choose what to test in dbt?](https://www.reddit.com/r/dataengineering/comments/1t3fdf2/how_do_you_choose_what_to_test_in_dbt/)] (Score: 7)
    *   Users shared their strategies for selecting tests in dbt, emphasizing the importance of lightweight tests, collaboration with analytics teams, and automated testing.
*   6. [[Advice for an Intern](https://www.reddit.com/r/dataengineering/comments/1t3lqko/advice_for_an_intern/)] (Score: 6)
    *   Advice for interns on how to approach seniors with problems, encouraging them to attempt solutions and present their thought processes.
*   7. [[Data engineer](https://www.reddit.com/r/dataengineering/comments/1t2xuwk/data_engineer/)] (Score: 3)
    *   A discussion about career development for data engineers, including advice on skill building, seeking projects, and potential salary expectations.
*   8. [[AI in your data pipeline](https://www.reddit.com/r/dataengineering/comments/1t3quts/ai_in_your_data_pipeline/)] (Score: 1)
    *   Exploration of how AI can be integrated into data pipelines, with discussions on its use for data generation, coding assistance, and improving efficiency.
*   9. [[Question on Salary.](https://www.reddit.com/r/dataengineering/comments/1t3s7d1/question_on_salary/)] (Score: 1)
    *   Users discussed salary expectations and provided opinions on whether a particular salary was average or low, considering experience and location.

# Detailed Analysis by Thread
**[ How can I gain an understanding on how big corps like Google handle their data? (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1t3a5jr/how_can_i_gain_an_understanding_on_how_big_corps/)**
*  **Summary:** Users are asking how to learn about the data handling practices of large tech companies like Google.
*  **Emotion:** Primarily Neutral, with a focus on information seeking and sharing.
*  **Top 3 Points of View:**
    *   Recommend reading "Designing Data Intensive Applications" by Martin Kleppman as a foundational resource.
    *   Suggest exploring resources like highscalability.com for insights into large-scale systems.
    *   Advise learning core concepts like sharding, replication, and distributed systems to understand how big corporations maintain data speed at scale.

**[ Solo DE managing pipelines (Score: 25)](https://www.reddit.com/r/dataengineering/comments/1t31azn/solo_de_managing_pipelines/)**
*  **Summary:** A solo data engineer is seeking advice on managing data pipelines effectively.
*  **Emotion:** Generally Neutral, with practical advice and some shared experiences.
*  **Top 3 Points of View:**
    *   Treat ingestion pipelines as "cattle, not pets" by abstracting ingestion logic into reusable functions and managing variations through configuration files.
    *   Establish at least two, ideally three, environments for testing (dev, staging, prod) and automate deployments between them.
    *   Consider the benefit of having a peer or junior developer to share the workload and enable taking vacations, rather than solely relying on outsourcing or being a solo dev.

**[ OLAP Server (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1t361hu/olap_server/)**
*  **Summary:** Users are discussing options for OLAP servers, particularly for academic or smaller-scale projects, with a focus on cost and accessibility.
*  **Emotion:** Neutral, with a range of technical suggestions.
*  **Top 3 Points of View:**
    *   Suggest using technologies like Apache Iceberg with DuckDB or Trino, or exploring ClickHouse for its columnar query capabilities and free cloud deployment.
    *   Mention that SQL Server's columnar index can function as an OLAP database, and developer editions are available for free for academic use.
    *   Recommend PostgreSQL (potentially via platforms like Railway or Supabase) as a cost-effective and suitable option for academic projects, unless dealing with billions of rows.

**[ IceStream - enabling efficient streaming writes in Apache Iceberg (Score: 8)](https://github.com/jordepic/icestream)**
*  **Summary:** This discussion is about a new tool called IceStream, designed to improve streaming writes in Apache Iceberg.
*  **Emotion:** A mix of positive interest and critical technical assessment.
*  **Top 3 Points of View:**
    *   The tool is seen as "super cool" with an inquiry about its long-term maintenance.
    *   There's skepticism about Iceberg's suitability if write loads significantly impact read performance, suggesting that a distributed database with in-memory WAL (like Clickhouse, Doris, Pinot, Druid) might be a better fit.
    *   A drawback noted is the dependency on Cassandra.

**[ How do you choose what to test in dbt? (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1t3fdf2/how_do_you_choose_what_to_test_in_dbt/)**
*  **Summary:** Users are sharing their approaches to determining what to test within dbt projects.
*  **Emotion:** Neutral, focused on best practices for data quality.
*  **Top 3 Points of View:**
    *   Data engineering should focus on technical tests like duplicates and nulls, while collaborating with analytics teams for business logic tests.
    *   Essential lightweight tests include `unique` and `not_null`. More comprehensive tests can be applied to models with exposures outside the dbt project (e.g., mart/BI tables).
    *   Using generated test data (e.g., with Python faker library) and running tests through CI/CD pipelines (like GitHub Actions) is a method for ensuring code quality before merging.

**[ Advice for an Intern (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1t3lqko/advice_for_an_intern/)**
*  **Summary:** This post offers advice to an intern on how to approach senior team members for help.
*  **Emotion:** Neutral, with a constructive and helpful tone.
*  **Top 3 Points of View:**
    *   Interns should try to solve issues independently first before asking for help.
    *   When seeking assistance, interns should come prepared with a suggestion or a plan of action, even if it's not the perfect solution.
    *   The goal is to demonstrate problem-solving effort, which allows seniors to guide and correct effectively, rather than simply doing the task themselves.

**[ Data engineer (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1t2xuwk/data_engineer/)**
*  **Summary:** A discussion revolving around career development and opportunities for data engineers.
*  **Emotion:** Mixed, with supportive and inquisitive tones.
*  **Top 3 Points of View:**
    *   Building skills and obtaining certifications are valuable, but ideally, this should be accompanied by paid work or project experience.
    *   Companies should provide projects or training opportunities for new hires/interns.
    *   Individuals might need to proactively ask for opportunities, or potentially adjust their expectations (e.g., salary) to gain initial experience.

**[ AI in your data pipeline (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1t3quts/ai_in_your_data_pipeline/)**
*  **Summary:** Users are discussing the integration and impact of AI in data pipelines.
*  **Emotion:** Mostly Neutral, with some positive outlooks on efficiency gains and some skepticism about current AI capabilities.
*  **Top 3 Points of View:**
    *   AI can be useful for tasks like generating data, delegating coding, or speeding up delivery of ad hoc requests, by using tools like Dagster, Duck, Spark, or Claude.
    *   A key emerging area is producing "AI-ready data assets," which may involve imputing missing data or ensuring data is suitable for AI models.
    *   Direct integration of AI into pipelines can be risky, especially for deterministic tasks, and it's often better to focus on ancillary work like writing new pipelines, auditing performance, or building supporting tools.

**[ Question on Salary. (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1t3s7d1/question_on_salary/)**
*  **Summary:** Users are discussing a salary for a data engineering role, with opinions on whether it's competitive.
*  **Emotion:** Neutral, with a focus on objective salary assessment.
*  **Top 3 Points of View:**
    *   The most direct way to determine if one is underpaid is to interview and receive offers.
    *   The salary in question is generally considered to be average to low, even for lower cost of living (LCOL) areas, with some users sharing their own past experiences and salary expectations.
    *   Many factors influence salary, but from a higher cost of living (HCOL) area perspective, the discussed salary appears well below market average.
