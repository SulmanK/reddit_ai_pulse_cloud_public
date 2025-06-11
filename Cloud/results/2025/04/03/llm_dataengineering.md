---
title: "Data Engineering Subreddit"
date: "2025-04-03"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data", "engineering", "etl"]
---

# Overall Ranking and Top Discussions
1.  [[D] How do you handle deduplication in streaming pipelines?](https://www.reddit.com/r/dataengineering/comments/1jqkdvu/how_do_you_handle_deduplication_in_streaming/) (Score: 14)
    *   This thread discusses different approaches to deduplication in streaming pipelines, including using Redis, Risingwave, Kafka with Snowflake, and custom solutions.
2.  [Can you suggest a flexible ETL incremental replication tool that integrates with other systems?](https://www.reddit.com/r/dataengineering/comments/1jqlb48/can_you_suggest_a_flexible_etl_incremental/) (Score: 3)
    *   Users are seeking suggestions for flexible ETL incremental replication tools that integrate well with other systems like Jira and Salesforce.
3.  [Code Exams - Tips from a hiring manager](https://www.reddit.com/r/dataengineering/comments/1jqnphu/code_exams_tips_from_a_hiring_manager/) (Score: 3)
    *   A hiring manager shared tips on code exams, prompting discussion about the relevance and effectiveness of such exams in the hiring process.
4.  [Practical advice/resources for data engineering in digital transformation?](https://www.reddit.com/r/dataengineering/comments/1jqlgz1/practical_adviceresources_for_data_engineering_in/) (Score: 2)
    *   This thread is requesting practical advice and resources for data engineering in the context of digital transformation.
5.  [Intern working on data quality/anomaly detection — looking for ideas & tech suggestions](https://www.reddit.com/r/dataengineering/comments/1jqm173/intern_working_on_data_qualityanomaly_detection/) (Score: 2)
    *   An intern is seeking ideas and technology suggestions for a data quality/anomaly detection project.
6.  [How to build UV-project into a Dockerimage with an external (local) package?](https://www.reddit.com/r/dataengineering/comments/1jqoog3/how_to_build_uvproject_into_a_dockerimage_with_an/) (Score: 2)
    *   The thread discusses how to integrate a UV-project into a Docker image with an external package.
7.  [can we print current branch name (feature branch / master) inside databricks Notebook](https://www.reddit.com/r/dataengineering/comments/1jqle02/can_we_print_current_branch_name_feature_branch/) (Score: 1)
    *   The author asking for solution to print current branch name inside databricks Notebook
8.  [SSIS resources and it's contribution to career](https://www.reddit.com/r/dataengineering/comments/1jqr8c7/ssis_resources_and_its_contribution_to_career/) (Score: 1)
    *   This thread seeks resources for SQL Server Integration Services (SSIS) and discusses its relevance to career advancement in data engineering.
9.  [Is the entry level barrier high for DE than SWE?](https://www.reddit.com/r/dataengineering/comments/1jqscpa/is_the_entry_level_barrier_high_for_de_than_swe/) (Score: 1)
    *   The thread discusses whether the entry-level barrier is higher for Data Engineering (DE) compared to Software Engineering (SWE).
10. [Climbed from Jr to Staff in 2 years, but still paid peanuts—should I quit? (Panic attacks, US job offers, and a proposal in Hawaii… Lost)](https://www.reddit.com/r/dataengineering/comments/1jqnwlc/climbed_from_jr_to_staff_in_2_years_but_still/) (Score: 0)
    *   This thread discusses about whether it is worth it to quit a job when dealing with panic attacks, US job offers, and a proposal in Hawaii while feeling lost.
11. [Is it reasonable to expect flawless work from juniors?](https://www.reddit.com/r/dataengineering/comments/1jqqm5h/is_it_reasonable_to_expect_flawless_work_from/) (Score: 0)
    *   This thread questions the expectation of flawless work from junior data engineers and suggests ways to address mistakes and improve.

# Detailed Analysis by Thread
**[[D] How do you handle deduplication in streaming pipelines? (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1jqkdvu/how_do_you_handle_deduplication_in_streaming/)**
*  **Summary:** The thread is focused on discussing strategies for deduplication in streaming pipelines. Participants share their experiences and preferred methods, including using Redis with TTL, Risingwave, and handling deduplication at different stages of the pipeline.
*  **Emotion:** The emotional tone is largely Neutral, with a slight hint of Positive sentiment in some comments.
*  **Top 3 Points of View:**
    *   Use Redis as a lookup cache with TTL for recent events, handling older dupes with nightly batch jobs.
    *   Use Risingwave, which persists its state store on S3 and uses bloom filters.
    *   Define a "key" to deduplicate data. Reduce all documents having the same key.

**[Can you suggest a flexible ETL incremental replication tool that integrates with other systems? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jqlb48/can_you_suggest_a_flexible_etl_incremental/)**
*  **Summary:** The post requests suggestions for flexible ETL incremental replication tools that can integrate with other systems, specifically mentioning Jira and Salesforce. One user recommends Estuary, highlighting its no-code, realtime CDC connectors.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Looking for an ETL tool that supports incremental replication.
    *   Need the tool to integrate with systems like Jira and Salesforce.
    *   Estuary is suggested as a potential solution with no-code CDC connectors.

**[Code Exams - Tips from a hiring manager (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1jqnphu/code_exams_tips_from_a_hiring_manager/)**
*  **Summary:** A hiring manager shares tips regarding coding exams. One user thanks them for sharing.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    *   A hiring manager shared their perspective on code exams.
    *   A user thanked the hiring manager.
    *   A bot provided a list of learning resources.

**[Practical advice/resources for data engineering in digital transformation? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jqlgz1/practical_adviceresources_for_data_engineering_in/)**
*  **Summary:** The user is seeking advice and resources for data engineering within digital transformation. A bot responds with a link to community learning resources.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   Request for practical advice and resources for data engineering in digital transformation.
    *   Link to dataengineering.wiki/Learning+Resources provided.
    *   This link is provided by a bot account.

**[Intern working on data quality/anomaly detection — looking for ideas & tech suggestions (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jqm173/intern_working_on_data_qualityanomaly_detection/)**
*  **Summary:** An intern is seeking ideas and tech suggestions for data quality and anomaly detection project. Users suggest unsupervised methods due to small data samples and to consider the cost of false positives.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   Intern is looking for project ideas and technology suggestions.
    *   Unsupervised methods might be necessary because of small sample size.
    *   Consider whether false positives are critical or if there is wiggle room.

**[How to build UV-project into a Dockerimage with an external (local) package? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1jqoog3/how_to_build_uvproject_into_a_dockerimage_with_an/)**
*  **Summary:** Advice given to not overcomplicate it for freshers and build UV project, move it to docker and install.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   Advice to not overcomplicate the process.
    *   Suggestion to use uv build, move wheel to docker.
    *   Installation within the docker environment.

**[can we print current branch name (feature branch / master) inside databricks Notebook (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jqle02/can_we_print_current_branch_name_feature_branch/)**
*  **Summary:** User asked solution on printing current branch name inside databricks Notebook. Some one suggests databricks sdk to do this.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   User asking for a solution to print the current branch name in Databricks Notebook.
    *   Suggestion to use Databricks SDK and ReposAPI.get() method
    *   User feeling unhappy that there are no responses but happy to ask a rare requirement

**[SSIS resources and it's contribution to career (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jqr8c7/ssis_resources_and_its_contribution_to_career/)**
*  **Summary:**  This thread discusses SQL Server Integration Services (SSIS) and its relevance to career advancement in data engineering.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *  User is looking for SSIS resources and career advice
    *  A bot account provides a link to learning resources
    *  Focus on community submitted resources

**[Is the entry level barrier high for DE than SWE? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1jqscpa/is_the_entry_level_barrier_high_for_de_than_swe/)**
*  **Summary:**  This thread analyzes whether the entry-level barrier is higher for Data Engineering (DE) compared to Software Engineering (SWE).
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * There are fewer DE jobs than SWE jobs
    * DE is a subset of SWE and in most DE jobs, you are expected to have a SWE background
    * Entry level DE jobs are very rare

**[Climbed from Jr to Staff in 2 years, but still paid peanuts—should I quit? (Panic attacks, US job offers, and a proposal in Hawaii… Lost) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jqnwlc/climbed_from_jr_to_staff_in_2_years_but_still/)**
*  **Summary:** This thread is about asking whether the user should quit due to low salary, panic attacks, and lost job opportunities. The commenters generally say to not feel bad and that the poster deserves better.
*  **Emotion:** The emotional tone is mixed, primarily Neutral, with some comments expressing Negative sentiment (sympathy) and some Positive (encouragement).
*  **Top 3 Points of View:**
    *   The user is underpaid and experiencing negative mental health effects.
    *   The user is advised to keep applying for jobs while doing the bare minimum at the current one.
    *   Certifications in Palantir Foundry and Databricks are recommended.

**[Is it reasonable to expect flawless work from juniors? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1jqqm5h/is_it_reasonable_to_expect_flawless_work_from/)**
*  **Summary:** The thread discusses expectations for junior data engineers, particularly whether flawless work is a reasonable expectation. Several responses indicate that it is not, and suggest ways to improve and learn from mistakes.
*  **Emotion:** The emotional tone is mixed, with Neutral responses offering advice, Negative responses criticizing the boss's expectations, and Positive responses encouraging the poster to take action and improve.
*  **Top 3 Points of View:**
    *   Flawless work from juniors is not a realistic expectation.
    *   The poster's boss may be setting unrealistic expectations.
    *   Focus on setting up a good testing workflow and documenting mistakes to learn from them.
