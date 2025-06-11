---
title: "Data Engineering Subreddit"
date: "2025-05-04"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "ML engineering", "data pipelines"]
---

# Overall Ranking and Top Discussions
1.  [[D] Partition evolution in iceberg- useful or not?](https://www.reddit.com/r/dataengineering/comments/1kedne3/partition_evolution_in_iceberg_useful_or_not/) (Score: 19)
    *   Discussing the usefulness of partition evolution in Apache Iceberg, with differing opinions on its complexity and performance implications.
2.  [How much do ML Engineering and Data Engineering overlap in practice?](https://www.reddit.com/r/dataengineering/comments/1kenf7n/how_much_do_ml_engineering_and_data_engineering/) (Score: 14)
    *   Exploring the overlap between ML Engineering and Data Engineering roles, especially in smaller organizations, and how AI might change these roles.
3.  [How do I run the DuckDB UI on a container](https://www.reddit.com/r/dataengineering/comments/1keiwyc/how_do_i_run_the_duckdb_ui_on_a_container/) (Score: 11)
    *   Seeking advice on running the DuckDB UI within a containerized environment, addressing issues with internet access and suggesting alternative UIs.
4.  [Hyperparameter Tuning Is a Resource Scheduling Problem](https://www.reddit.com/r/dataengineering/comments/1keoj0b/hyperparameter_tuning_is_a_resource_scheduling/) (Score: 10)
    *   Discussing hyperparameter tuning as a resource scheduling problem.
5.  [Built a free tool to clean up messy multi-file CSV exports into normalized SQL + ERDs. Would love your thoughts.](https://layernexus.com/) (Score: 7)
    *   Seeking feedback on a tool for cleaning up messy CSV exports, with concerns raised about uploading proprietary data to a web-based tool.
6.  [How much of your time is spent fixing broken pipelines, and what tools help?](https://www.reddit.com/r/dataengineering/comments/1keoptt/how_much_of_your_time_is_spent_fixing_broken/) (Score: 6)
    *   Discussing the amount of time spent fixing broken data pipelines and the tools used to manage and recover from these breakages.
7.  [I Built YouTube Analytics Pipeline](https://i.redd.it/xsexphn80sye1.jpeg) (Score: 5)
    *   Presenting a YouTube analytics pipeline, with feedback on the readability of the graphs.
8. [I’m thinking of starting content creation in tech/ data engineering. Anything you guys want to see?](https://www.reddit.com/r/dataengineering/comments/1keqz1m/im_thinking_of_starting_content_creation_in_tech/) (Score: 2)
    * Asking for ideas to start creating tech/data engineering content.
9.  [Is there an open source library to solve for workflows in parallel?](https://www.reddit.com/r/dataengineering/comments/1ked1rd/is_there_an_open_source_library_to_solve_for/) (Score: 1)
    *   Searching for an open-source library to solve workflows in parallel, with suggestions for using topological sort or tools like Airflow/Dagster.
10. [How to build something like datanerd.tech?!?](https://www.reddit.com/r/dataengineering/comments/1kenj7s/how_to_build_something_like_datanerdtech/) (Score: 1)
    * Asking for advice on how to build a data visualization platform.
11. [CS or Applied Maths BS for data engineering?](https://www.reddit.com/r/dataengineering/comments/1kercn1/cs_or_applied_maths_bs_for_data_engineering/) (Score: 1)
    * Asking about the best degree for a data engineering career.
12. [advice for rising senior trying to do DE/MLE](https://www.reddit.com/r/dataengineering/comments/1kero07/advice_for_rising_senior_trying_to_do_demle/) (Score: 1)
    * Asking for advice on how to do Data Engineering or Machine Learning Engineer role.
13. [I wrote a short post on what makes a modern data warehouse (feedback welcome)](https://www.reddit.com/r/dataengineering/comments/1ke2857/i_wrote_a_short_post_on_what_makes_a_modern_data/) (Score: 0)
    * Seeking feedback on a blog post about modern data warehouses.
14. [Do entry level DE jobs exist in the US?](https://www.reddit.com/r/dataengineering/comments/1kerenq/do_entry_level_de_jobs_exist_in_the_us/) (Score: 0)
    * Questioning the existence of entry-level Data Engineering jobs in the US and discussing alternative paths and the importance of certification.
15. [Need help to grow in Data Engineering field.](https://www.reddit.com/r/dataengineering/comments/1kesmjh/need_help_to_grow_in_data_engineering_field/) (Score: 0)
    * Asking for help to grow in the Data Engineering field.

# Detailed Analysis by Thread
**[[D] Partition evolution in iceberg- useful or not? (Score: 19)](https://www.reddit.com/r/dataengineering/comments/1kedne3/partition_evolution_in_iceberg_useful_or_not/)**
*  **Summary:** The discussion revolves around the usefulness of partition evolution in Apache Iceberg. Some users believe it's an overly complex approach that might incur performance hits due to multiple partition patterns. Others find it useful for evolving schema/partition over time without rewriting the entire table. An alternative approach of using separate "cold" and "hot" storage tables is also suggested.
*  **Emotion:** The emotional tone of the thread is neutral, with users providing technical explanations and suggesting alternatives in a calm and informative manner.
*  **Top 3 Points of View:**
    * Partition evolution is complex and might lead to performance issues.
    * Partition evolution is useful for schema evolution without full table rewrites.
    * Maintaining separate "cold" and "hot" storage is a more efficient alternative.

**[How much do ML Engineering and Data Engineering overlap in practice? (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1kenf7n/how_much_do_ml_engineering_and_data_engineering/)**
*  **Summary:** The discussion explores the overlap between ML Engineering (MLE) and Data Engineering (DE) roles, particularly in smaller organizations. Participants discuss how MLEs often handle data pipeline work, especially in dysfunctional orgs. Some suggest that DE is a stepping stone to MLE, while others predict that AI-assisted MLEs will diminish the DE role over time.  The complementary skill sets and the split of responsibilities (DE for data integration, MLE for model deployment) are also discussed.
*  **Emotion:** The emotional tone is mostly neutral, with a hint of concern/speculation about the future of DE roles.
*  **Top 3 Points of View:**
    * MLE and DE roles have significant overlap, especially in smaller companies.
    * DE is sometimes a precursor to becoming an MLE.
    * AI-assisted MLEs might take over DE roles in the future.

**[How do I run the DuckDB UI on a container (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1keiwyc/how_do_i_run_the_duckdb_ui_on_a_container/)**
*  **Summary:** This thread discusses the challenges of running the DuckDB UI in a container environment.  The UI requires internet access to connect to MotherDuck.  Alternatives like Marimo and sqlmesh are suggested. One user recommends looking at deepseek.ai's GitHub for an example of using DuckDB in containers.
*  **Emotion:** The emotional tone is neutral, with a mix of problem-solving and suggestions.
*  **Top 3 Points of View:**
    * DuckDB UI needs internet access, which poses a challenge in containers.
    * Marimo and sqlmesh are alternative UI options.
    * deepseek.ai's GitHub provides an example of using DuckDB in containers.

**[Hyperparameter Tuning Is a Resource Scheduling Problem (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1keoj0b/hyperparameter_tuning_is_a_resource_scheduling/)**
*  **Summary:** This thread is a discussion centered on a post highlighting hyperparameter tuning as a resource scheduling problem. Commenters found the post easy to follow. The bot also lists community-submitted learning resources.
*  **Emotion:** The emotional tone is positive, with one user expressing a positive sentiment.
*  **Top 3 Points of View:**
    * The post about hyperparameter tuning is well-received and easy to understand.
    * (Bot's Perspective) There is a list of learning resources available.

**[Built a free tool to clean up messy multi-file CSV exports into normalized SQL + ERDs. Would love your thoughts. (Score: 7)](https://layernexus.com/)**
*  **Summary:** The author is seeking feedback on a tool that cleans messy multi-file CSVs into normalized SQL and ERDs. A key concern raised is the reluctance to upload proprietary data to a web-based tool. The commenter suggests offering a Dockerized or self-hosted version for privacy. Another commenter questions the concept of "messy denormalized CSVs."
*  **Emotion:** The emotional tone is neutral, mixed with concerns about data privacy.
*  **Top 3 Points of View:**
    * Concerns about uploading proprietary data to a web tool.
    * Suggestion to offer a Dockerized/self-hosted version for privacy.
    * Questioning the concept of messy denormalized CSVs.

**[How much of your time is spent fixing broken pipelines, and what tools help? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1keoptt/how_much_of_your_time_is_spent_fixing_broken/)**
*  **Summary:** The discussion centers around the time spent fixing broken data pipelines. The biggest issues are upstream data stability, code quality, and test coverage. A team with 300 pipelines experiences breakages weekly, using Airflow for notification and quick recovery. Emphasis is placed on building tools and processes for rapid recovery rather than solely preventing breakages.
*  **Emotion:** The emotional tone is neutral, focused on practical experiences and solutions.
*  **Top 3 Points of View:**
    * Upstream data stability, code quality, and test coverage are critical.
    * Airflow is useful for detecting and managing pipeline breakages.
    * Prioritize rapid recovery over solely preventing breakages.

**[I Built YouTube Analytics Pipeline (Score: 5)](https://i.redd.it/xsexphn80sye1.jpeg)**
*  **Summary:** A user shares a YouTube Analytics Pipeline, and one comment notes that half of the graphs are unreadable.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * The graphs in the YouTube Analytics Pipeline are difficult to read.

**[I’m thinking of starting content creation in tech/ data engineering. Anything you guys want to see? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1keqz1m/im_thinking_of_starting_content_creation_in_tech/)**
*  **Summary:** A user is asking for ideas to start creating tech/data engineering content. The bot lists community-submitted learning resources.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * A user is looking for content ideas.
    * (Bot's Perspective) There are learning resources available.

**[Is there an open source library to solve for workflows in parallel? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1ked1rd/is_there_an_open_source_library_to_solve_for/)**
*  **Summary:** The thread is a query for an open-source library to solve workflows in parallel. Solutions include suggesting writing helper functions using topological sort or using Airflow/Dagster. One user thinks this is more of a programmer or javascript question.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Write custom helper functions.
    * Consider Airflow/Dagster.
    * It may be a programmer/JavaScript question.

**[How to build something like datanerd.tech?!? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kenj7s/how_to_build_something_like_datanerdtech/)**
*  **Summary:** A user asks for advice on how to build a data visualization platform. Suggestions include using Streamlit, web scraping, and simple databases like DuckDB or SQLite. Arkalos, a Python backend with React frontend, is also suggested.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Use Streamlit for building the platform.
    * Web scrape and store data in a simple database.
    * Use Arkalos with Python backend and React frontend.

**[CS or Applied Maths BS for data engineering? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kercn1/cs_or_applied_maths_bs_for_data_engineering/)**
*  **Summary:** The discussion is about the ideal major for a data engineering career.  It's suggested to do what interests you most and to learn as much about DE as possible. Alternatives like Informatics or Information Science are also mentioned.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Choose a major that interests you.
    * Informatics or Information Science are other options.

**[advice for rising senior trying to do DE/MLE (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kero07/advice_for_rising_senior_trying_to_do_demle/)**
*  **Summary:** A student is looking for advice for a Data Engineering or Machine Learning Engineering position. The bot lists community-submitted learning resources.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Advice seeker.
    * (Bot's Perspective) There are learning resources available.

**[I wrote a short post on what makes a modern data warehouse (feedback welcome) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1ke2857/i_wrote_a_short_post_on_what_makes_a_modern_data/)**
*  **Summary:** The thread is about getting feedback on a short post on modern data warehouses. One commenter states that the post is incorrect and that modern data warehouses are hybrid. The bot provided a link to an open-source project showcase.
*  **Emotion:** The emotional tone is negative, with one user disagreeing with the post.
*  **Top 3 Points of View:**
    * The original post is wrong.
    * Modern data warehouses are hybrid.
    * (Bot's Perspective) Here are open-source projects.

**[Do entry level DE jobs exist in the US? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kerenq/do_entry_level_de_jobs_exist_in_the_us/)**
*  **Summary:** The discussion centers on the existence of entry-level DE jobs in the US. DE is often promoted from Data Analyst or SWE positions. Having certifications is an important factor when looking for a DE job. Entry level jobs are rare, but they exist in bigger companies.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * DE is often a promotion from other roles.
    * Certification is an important factor.
    * Entry-level DE jobs are rare.

**[Need help to grow in Data Engineering field. (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1kesmjh/need_help_to_grow_in_data_engineering_field/)**
*  **Summary:** A user needs help to grow in the Data Engineering field. The bot provides a link to community-submitted learning resources.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Help seeker.
    * (Bot's Perspective) There are learning resources available.
