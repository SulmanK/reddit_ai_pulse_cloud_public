---
title: "Data Engineering Subreddit"
date: "2025-08-18"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data", "engineering", "reddit"]
---

# Overall Ranking and Top Discussions
1.  [[D] Github Actions to run my data pipeliens?](https://www.reddit.com/r/dataengineering/comments/1mtj8kd/github_actions_to_run_my_data_pipeliens/) (Score: 22)
    * The discussion revolves around using Github Actions for data pipelines, with mixed opinions on its suitability for production environments and heavy workloads.
2.  [Upskilling](https://www.reddit.com/r/dataengineering/comments/1mt5l8i/upskilling/) (Score: 12)
    *  Users discuss balancing upskilling with personal time and hobbies, with a focus on Power BI and Python.
3.  [Remote Desktop development](https://www.reddit.com/r/dataengineering/comments/1mtp9ml/remote_desktop_development/) (Score: 8)
    *  The discussion centers on the challenges and drawbacks of using Remote Desktop Protocol (RDP) for development, particularly in data engineering contexts, with some suggesting SSH as a better alternative.
4.  [How do you manage web scraping pipelines at scale without constant breakage?](https://www.reddit.com/r/dataengineering/comments/1mtr5d2/how_do_you_manage_web_scraping_pipelines_at_scale/) (Score: 6)
    *  The discussion focuses on the challenges of managing web scraping pipelines at scale, with many recommending against it for production environments, and suggesting to use internal/hidden APIs instead.
5.  [When should I start looking for a new job?](https://www.reddit.com/r/dataengineering/comments/1mtsgz9/when_should_i_start_looking_for_a_new_job/) (Score: 4)
    *  The thread discusses the user's low hourly wage and encourages them to seek better opportunities.
6.  [Slow Changing Dimension Type 1 and Idempotency?](https://www.reddit.com/r/dataengineering/comments/1mtnh3b/slow_changing_dimension_type_1_and_idempotency/) (Score: 3)
    *  Users discuss slow changing dimensions, idempotency, and how the aggregation table is built.
7.  [Automation of PowerBi](https://www.reddit.com/r/dataengineering/comments/1mtsr2h/automation_of_powerbi/) (Score: 3)
    *  Discussion about automating Power BI, using Semantic Link python library and Fabric Ecosystem.
8.  [What's learning on the job like?](https://www.reddit.com/r/dataengineering/comments/1mtws1v/whats_learning_on_the_job_like/) (Score: 2)
    *  A bot provides a link to community-submitted learning resources.
9.  [How do small data teams handle data SLAs?](https://www.reddit.com/r/dataengineering/comments/1mtvc4f/how_do_small_data_teams_handle_data_slas/) (Score: 1)
    *  The discussion suggests using dbt tests and slack notifications for handling data SLAs.
10. [2 YOE but no real project, please help me out!!](https://www.reddit.com/r/dataengineering/comments/1mt8lnu/2_yoe_but_no_real_project_please_help_me_out/) (Score: 0)
    * Users share advice on how to gain practical experience and build a portfolio with end-to-end projects.
11. [Anyone doing Zach Wilson’s DE Bootcamp?](https://www.reddit.com/r/dataengineering/comments/1mtd1ec/anyone_doing_zach_wilsons_de_bootcamp/) (Score: 0)
    * Two users confirm they are participating in the Zach Wilson DE Bootcamp.
12. [Thing that destroys your reputation as a data engineer](https://www.reddit.com/r/dataengineering/comments/1mtu5by/thing_that_destroys_your_reputation_as_a_data/) (Score: 0)
    *  The thread humorously and seriously discusses actions that can damage a data engineer's reputation, ranging from lack of accountability to data breaches.

# Detailed Analysis by Thread
**[ [D] Github Actions to run my data pipeliens? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1mtj8kd/github_actions_to_run_my_data_pipeliens/)**
*  **Summary:** The main question is whether Github Actions is a good choice for running data pipelines. Some suggest it is suitable for small companies with a few batch jobs, while others warn against using it for production, citing maintenance overhead and better alternatives.
*  **Emotion:** The overall emotional tone is mixed, with both Positive and Negative sentiments expressed, but primarily Neutral. There is a debate on the topic, leading to the variety of emotions.
*  **Top 3 Points of View:**
    *   Github Actions can be a good starting point for simple data pipelines, especially for companies without built-in orchestration platforms.
    *   Github Actions is not suitable for heavy data workloads or production environments due to cost, runtime overhead, and maintenance.
    *   Emerging solutions are trying to make Github Actions cheaper and faster for data engineering use cases.

**[Upskilling (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1mt5l8i/upskilling/)**
*  **Summary:** This thread is about balancing upskilling, specifically learning Power BI, Python and Swift, with personal life and other hobbies. Users share personal experiences and time management strategies.
*  **Emotion:**  The overall emotional tone is Neutral, with a hint of positive sentiment regarding balancing work and personal interests.
*  **Top 3 Points of View:**
    *   Python is generally useful in Data Engineering (DE), but may not be immediately relevant for analysts. Swift is less relevant for DE.
    *   Time should be blocked out for both career-aligned skills and interest-driven projects.
    *   Balancing continuous learning with hobbies and family time is challenging but important to avoid burnout.

**[Remote Desktop development (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1mtp9ml/remote_desktop_development/)**
*  **Summary:** Users are discussing the pros and cons of using Remote Desktop (RDP) for development work, highlighting issues such as slowness, screen fitting problems, and overall inefficiency, with several people recounting negative experiences and advocating for alternatives like SSH. Security requirements and under-provisioned machines are also discussed.
*  **Emotion:** The emotional tone is primarily Neutral, with hints of Negative sentiment due to the frustrations with RDP. Positive sentiments are expressed by those who demanded changes.
*  **Top 3 Points of View:**
    *   RDP is generally a bad experience due to slowness and lag, with users preferring SSH for remote development.
    *   Security requirements leading to RDP can be a sign of under-provisioning and inefficient company culture.
    *   Developers should push back against RDP policies and advocate for better solutions and proper provisioning.

**[How do you manage web scraping pipelines at scale without constant breakage? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1mtr5d2/how_do_you_manage_web_scraping_pipelines_at_scale/)**
*  **Summary:**  This thread explores the challenges of managing web scraping pipelines at scale due to frequent breakage. Many commenters advise against using web scraping for production and suggest obtaining data through official APIs or other means. The need for robust alerting is mentioned.
*  **Emotion:** The emotion is predominantly Neutral, with a slight lean towards Negative due to the inherent frustrations with web scraping.
*  **Top 3 Points of View:**
    *   Web scraping is generally unreliable for production-level pipelines due to frequent changes in website structure.
    *   The preferred approach is to obtain data through official APIs or direct contact with site owners.
    *   If web scraping is necessary, robust alerting capabilities are crucial for promptly addressing breakage.

**[When should I start looking for a new job? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1mtsgz9/when_should_i_start_looking_for_a_new_job/)**
*  **Summary:** The user is asking when they should start looking for a new job, the general consensus is immediately because they are being severely underpaid.
*  **Emotion:** Predominantly Neutral and Negative due to the discussion of low wages, with some Positive sentiment from users offering guidance.
*  **Top 3 Points of View:**
    *   The user is being paid a very low wage for the type of work they are doing.
    *   The user should immediately start applying for new jobs.
    *   Some users offered to provide personal guidance.

**[Slow Changing Dimension Type 1 and Idempotency? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mtnh3b/slow_changing_dimension_type_1_and_idempotency/)**
*  **Summary:** The thread discusses slow changing dimensions (Type 1) and idempotency in the context of data pipelines. Users are seeking clarification and guidance on how to ensure data consistency and accuracy.
*  **Emotion:** The overall emotional tone is Neutral, reflecting a technical discussion seeking information and clarity.
*  **Top 3 Points of View:**
    *   Idempotency depends on the specifics of the pipeline and data loading process.
    *   It is important to understand how the aggregation (AGG) table is built and whether duplicate data is being loaded.
    *   More details about the pipeline are needed to determine whether it is idempotent.

**[Automation of PowerBi (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1mtsr2h/automation_of_powerbi/)**
*  **Summary:** The discussion is centered on automating Power BI tasks, particularly with the use of the Semantic Link python library and the Fabric Ecosystem for managing the Azure Data Stack. The goal is to programmatically manage and orchestrate various aspects of Power BI.
*  **Emotion:** The overall tone is Neutral with slight positive sentiments on the idea of automation.
*  **Top 3 Points of View:**
    *   The Semantic Link Python library is very promising for the automation of Power BI.
    *   Fabric Ecosystem provides good functionality to manage Azure Data Stack.
    *   Dependency graphs are very insightful.

**[What's learning on the job like? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1mtws1v/whats_learning_on_the_job_like/)**
*  **Summary:** This thread is essentially a bot posting a link to community-submitted learning resources.
*  **Emotion:** The emotion is Neutral.
*  **Top 3 Points of View:**
    *   N/A - Bot response.

**[How do small data teams handle data SLAs? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1mtvc4f/how_do_small_data_teams_handle_data_slas/)**
*  **Summary:** The thread discusses how small data teams handle data SLAs, suggesting the use of dbt tests and Slack notifications as an effective solution.
*  **Emotion:** The sentiment is Neutral.
*  **Top 3 Points of View:**
    *   dbt tests offer a good solution for handling data SLAs.
    *   Slack notifications are helpful for alerting on issues.
    *   Running dbt tests on a DAG is a simple and effective approach.

**[2 YOE but no real project, please help me out!! (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mt8lnu/2_yoe_but_no_real_project_please_help_me_out/)**
*  **Summary:** The discussion is about a data engineer with 2 years of experience but lacking real project experience. Users offer advice on how to gain practical skills and build a portfolio.
*  **Emotion:** The emotional tone is Neutral, with elements of encouragement and advice.
*  **Top 3 Points of View:**
    *   Focus on SQL, Python, and cloud platforms (AWS, Google Cloud, or Azure).
    *   Work on end-to-end data engineering projects to understand the full lifecycle and gain practical experience.
    *   Replicate existing projects from sources like YouTube to get comfortable with the environment, then select a dataset and try to solve a problem.

**[Anyone doing Zach Wilson’s DE Bootcamp? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mtd1ec/anyone_doing_zach_wilsons_de_bootcamp/)**
*   **Summary:** This thread simply asks if anyone is participating in Zach Wilson's Data Engineering Bootcamp.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Two users confirm they are doing the bootcamp.

**[Thing that destroys your reputation as a data engineer (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1mtu5by/thing_that_destroys_your_reputation_as_a_data/)**
*  **Summary:**  This thread discusses various ways a data engineer's reputation can be damaged. It ranges from humorous examples to more serious issues like lack of accountability and data breaches.
*  **Emotion:** The emotional tone is mixed, ranging from Neutral to Positive (humorous) and Negative (serious issues).
*  **Top 3 Points of View:**
    *   Lack of accountability is a major factor.
    *   Data breaches or security lapses are reputation-killers.
    *   Incompetence, such as poor database design, can significantly damage credibility.
