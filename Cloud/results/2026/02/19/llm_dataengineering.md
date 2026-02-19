---
title: "Data Engineering Subreddit"
date: "2026-02-19"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["Spark", "Career", "AI", "Data Management", "PySpark"]
---

# Overall Ranking and Top Discussions
*   1. [Best practices for logging and error handling in Spark Streaming executor code](https://www.reddit.com/r/dataengineering/comments/1r8r115/best_practices_for_logging_and_error_handling_in/) (Score: 11)
    *   Runtime vs checked exceptions doesn’t really matter here. Spark treats both the same once serialized into the task. What matters is whether the failure survives retries or just gets retried into oblivion. The real fix is shifting from exception based visibility to signal based visibility. In Spark Streaming retries hide failures by design.
*   2. [Will there be less/no entry/mid and more contractors bz of AI?](https://www.reddit.com/r/dataengineering/comments/1r8ry9w/will_there_be_lessno_entrymid_and_more/) (Score: 9)
    *   80% of people who apply at entry level are just LLM spamming, so they get immediately disqualified. Only 5% of non-LLM applicants consider how they can help the company. Our current experimental approach is no further mid, junior or offshore hires. They want a high skilled team of agentic ai supported seniors. They’re running with that until summer and then doing a week long breakdown of how it’s working out. No talk of contractors as they don’t fit in the model. Data engineering is a fairly future proof job as far as tech job goes. Frontend jobs are hiring much more. DE wants to pay someone to be responsible for a data observation. 100%. So if i would have to take a guess. Contract potential for an average entry Data Engineer probably shrank around 80% Contract potential for an average mid Data Engineer probably shrank around 60% Contract potential for an average senior data engineer probably also shrank around 30%
*   3. [DEs: How many engineers work with you on a project?](https://www.reddit.com/r/dataengineering/comments/1r8mnlo/des_how_many_engineers_work_with_you_on_a_project/) (Score: 8)
    *   I'm usually solo. There is another analytics engineer that handles some of the maintenance but is mostly occupied with random stakeholder requests. There are 5 DEs supporting 20+ unique pipelines with very different data sources and building more pipelines every quarter. They have to process the data into a couple canonical models and build automated validation & reconciliation systems. I am the alpha and omega, I am the data analyst, data engineer, ai engineer, platform architect. I am everything! Depends! My team is basically a garbage in and garbage out team, handles all the data that enters our product, many downstream teams though. We have 16 people total just in my team. Company of about 200. It's just me. I built it, I run it. We have three reporting analysts and departments have direct data access via Power BI Dataflows. we have a team of 40 data engineers including staff and contractors
*   4. [Sharing Gold Layer data with Ops team](https://www.reddit.com/r/dataengineering/comments/1r8udhp/sharing_gold_layer_data_with_ops_team/) (Score: 7)
    *   How often will it be queried and how will they use it? If queries are often and nr of rows needed are low, SQL Server is better than DBX. Can your operational platform read Iceberg tables? If so, just create your gold layer tables to generate Iceberg metadata and then your operational platform can just read them i would default to a gold delta table and put a thin "serving" layer in front of it so ops can query it without copying data into the database. deltashare
*   5. [Need help with Pyspark](https://www.reddit.com/r/dataengineering/comments/1r8yia2/need_help_with_pyspark/) (Score: 5)
    *   Easiest nowadays is solving a problem through any LLM (Claude is quite good) and deep diving on the technical concepts in the solution. That’s the modern day equivalent of googling and spending hours on stack overflow Use spark SQL and go learning how to translate it to spark DF 80% of what you do in PySpark is the same as in SQL. Frank Kane's PySpark course on Udemy was helpful for him. He took coding notes of boilerplate syntax in notebook and sometimes wrote the template code byheart when doing assignments. He could not keep up because of interviews and his new job doesn't require spark knowledge. Why you want to learn pyspark when you have snowflake? Both are just tools to process data, doesn't matter whatever you use, your basics should be clear for distributed computing.
*   6. [Data engineering + AI](https://www.reddit.com/r/dataengineering/comments/1r90t1c/data_engineering_ai/) (Score: 4)
    *   AI Data Engineer got his first job as an AI engineer. He missed a lot of opportunities during the hiring freeze because he was still in school. He expected an economic downturn but nowhere did it come up that America the largest outsourcer of work would cut off funding. Go on LinkedIn and spam posts like “Wow so insightful! AI is the future! 🚀👏🦾” On any post with AI in it and you will be as educated as the average executive pushing to implement AI in everything. Fingers on Keyboard writing code You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) if you have any questions or concerns.* If you have an engineering background, just open claude code and start building stuff. You will learn more by doing than reading at first, then build expertise around prompts and context
*   7. [Using dlt to ingest nested api data](https://www.reddit.com/r/dataengineering/comments/1r8tkkm/using_dlt_to_ingest_nested_api_data/) (Score: 3)
    *   Use dlt’s Python API to override defaults. Define a schema forcing all nested data into your target granularity - their docs have solid examples. Sure, like this : @dlt.resource(max_table_nesting=0) What if you have a parent table that has 2 children each with n records per parent row? you'd end up with cartesian product of sub-granularities? or how would you want it handled?
*   8. [DE jobs in California](https://www.reddit.com/r/dataengineering/comments/1r9ahk0/de_jobs_in_california/) (Score: 2)
    *   Your post looks like it's related to Data Engineering in India. You might find posting in [r/dataengineersindia](https://www.reddit.com/r/dataengineersindia/) more helpful to your situation. *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   9. [A week ago, I discovered that in Data Vault 2.0, people aren't stored as people, but as business entities... But the client just wants to see actual humans in the data views.](https://www.reddit.com/r/dataengineering/comments/1r9af4f/a_week_ago_i_discovered_that_in_data_vault_20/) (Score: 2)
    *   how about some healthy pragmatism. do as the client wishes if it's not moronic and move on to more important stuff.
*   10. [Reorged to backend team - Wwyd](https://www.reddit.com/r/dataengineering/comments/1r9b8fy/reorged_to_backend_team_wwyd/) (Score: 1)
    *   Are you interested in transitioning into Data Engineering? Read our community guide: https://dataengineering.wiki/FAQ/How+can+I+transition+into+Data+Engineering *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   11. [Career Crossroads](https://www.reddit.com/r/dataengineering/comments/1r8z5hx/career_crossroads/) (Score: 1)
    *   I don't think that offer letter is an open invitation to come work whenever you're ready, if it's from September I'd assume that opportunity is long since passed
*   12. [Advice on Setting up Version Control](https://www.reddit.com/r/dataengineering/comments/1r98afo/advice_on_setting_up_version_control/) (Score: 1)
    *   Use the system that your IT department uses. This will give you: 1. Free source control system 2. Free expertise 3. Very competent help with a setup 4. Possibly also a work management system literally anything other than not doing any version control would be such much better. git was developed in 2005. just start with a *** git repo in snowflake
*   13. [Help me find a career](https://www.reddit.com/r/dataengineering/comments/1r957nt/help_me_find_a_career/) (Score: 0)
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   14. [Would you Trust an AI agent in your Cloud Environment?](https://www.reddit.com/r/dataengineering/comments/1r8qso1/would_you_trust_an_ai_agent_in_your_cloud/) (Score: 0)
    *   Absolutely not. I've seen the chaos it can wreak locally, no way I want that *anywhere near* anything precious. I wouldn't trust it in dev. Actions in cloud environment have prices associated with them. Basic OpenAI or Claude prompts fail to produce meaningful SQL aggregations. For the first time we have something the result of which cannot be predicted. People with no knowledge about AI systems go gaga over it on the internet. They compare AI with calculators and say when calculators came they only made our work faster. However, the output of calculators

# Detailed Analysis by Thread

**[ Best practices for logging and error handling in Spark Streaming executor code (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1r8r115/best_practices_for_logging_and_error_handling_in/)**
*   **Summary:** Runtime vs checked exceptions doesn’t really matter here. Spark treats both the same once serialized into the task. What matters is whether the failure survives retries or just gets retried into oblivion. The real fix is shifting from exception based visibility to signal based visibility. In Spark Streaming retries hide failures by design.
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Spark treats runtime and checked exceptions similarly; the key is whether failures survive retries or lead to 'retry oblivion'.
    * Shift from exception-based visibility to signal-based visibility, using structured logs and metrics to identify failures as distributed telemetry rather than relying on the driver for truth.

**[ Will there be less/no entry/mid and more contractors bz of AI? (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1r8ry9w/will_there_be_lessno_entrymid_and_more/)**
*   **Summary:** 80% of people who apply at entry level are just LLM spamming, so they get immediately disqualified. Only 5% of non-LLM applicants consider how they can help the company. Our current experimental approach is no further mid, junior or offshore hires. They want a high skilled team of agentic ai supported seniors. They’re running with that until summer and then doing a week long breakdown of how it’s working out. No talk of contractors as they don’t fit in the model. Data engineering is a fairly future proof job as far as tech job goes. Frontend jobs are hiring much more. DE wants to pay someone to be responsible for a data observation. 100%. So if i would have to take a guess. Contract potential for an average entry Data Engineer probably shrank around 80% Contract potential for an average mid Data Engineer probably shrank around 60% Contract potential for an average senior data engineer probably also shrank around 30%
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * AI (LLMs) is changing the job market, making junior roles more challenging to fill due to LLM-spamming applicants, but also enabling capable juniors to perform at a senior level.
    * Some companies are experimenting with hiring fewer mid/junior/offshore roles, preferring high-skilled teams supported by agentic AI.
    * Data engineering remains relatively future-proof, especially where data integrity and compliance are critical, making 100% AI pipelines unlikely in such areas.

**[ DEs: How many engineers work with you on a project? (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1r8mnlo/des_how_many_engineers_work_with_you_on_a_project/)**
*   **Summary:** I'm usually solo. There is another analytics engineer that handles some of the maintenance but is mostly occupied with random stakeholder requests. There are 5 DEs supporting 20+ unique pipelines with very different data sources and building more pipelines every quarter. They have to process the data into a couple canonical models and build automated validation & reconciliation systems. I am the alpha and omega, I am the data analyst, data engineer, ai engineer, platform architect. I am everything! Depends! My team is basically a garbage in and garbage out team, handles all the data that enters our product, many downstream teams though. We have 16 people total just in my team. Company of about 200. It's just me. I built it, I run it. We have three reporting analysts and departments have direct data access via Power BI Dataflows. we have a team of 40 data engineers including staff and contractors
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Team sizes vary significantly, from solo Data Engineers handling all roles (analyst, engineer, architect) to large teams of 40+ DEs.
    * Small teams (e.g., 5 DEs) often feel unsustainable given the volume and complexity of pipelines (20+ unique pipelines) and additional responsibilities like validation and vendor communication.
    * In smaller companies (around 200 people), a single DE might be responsible for building and running the entire data infrastructure.

**[ Sharing Gold Layer data with Ops team (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1r8udhp/sharing_gold_layer_data_with_ops_team/)**
*   **Summary:** How often will it be queried and how will they use it? If queries are often and nr of rows needed are low, SQL Server is better than DBX. Can your operational platform read Iceberg tables? If so, just create your gold layer tables to generate Iceberg metadata and then your operational platform can just read them i would default to a gold delta table and put a thin "serving" layer in front of it so ops can query it without copying data into the database. deltashare
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Consider the query frequency, latency needs, and data usage patterns (aggregation vs. few rows) to decide between SQL Server (better for frequent, low-row queries) and Databricks (DBX) for data sharing.
    * If the operational platform can read Iceberg tables, this is a clean solution for sharing gold layer data.
    * A common approach is using a gold Delta table with a 'thin serving layer' (e.g., Databricks SQL with views/perms) to avoid data copying and its associated issues like extra pipelines and schema drift.

**[ Need help with Pyspark (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1r8yia2/need_help_with_pyspark/)**
*   **Summary:** Easiest nowadays is solving a problem through any LLM (Claude is quite good) and deep diving on the technical concepts in the solution. That’s the modern day equivalent of googling and spending hours on stack overflow Use spark SQL and go learning how to translate it to spark DF 80% of what you do in PySpark is the same as in SQL. Frank Kane's PySpark course on Udemy was helpful for him. He took coding notes of boilerplate syntax in notebook and sometimes wrote the template code byheart when doing assignments. He could not keep up because of interviews and his new job doesn't require spark knowledge. Why you want to learn pyspark when you have snowflake? Both are just tools to process data, doesn't matter whatever you use, your basics should be clear for distributed computing.
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * PySpark is approachable for those with SQL skills, as many operations translate directly (JOIN, SELECT, WHERE, GROUP BY).
    * Leveraging LLMs (like Claude) for problem-solving is a modern way to learn, followed by deep diving into technical concepts.
    * Consider whether PySpark is truly necessary if other tools like Snowflake are already in use, emphasizing strong distributed computing basics over specific tool mastery.

**[ Data engineering + AI (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1r90t1c/data_engineering_ai/)**
*   **Summary:** AI Data Engineer got his first job as an AI engineer. He missed a lot of opportunities during the hiring freeze because he was still in school. He expected an economic downturn but nowhere did it come up that America the largest outsourcer of work would cut off funding. Go on LinkedIn and spam posts like “Wow so insightful! AI is the future! 🚀👏🦾” On any post with AI in it and you will be as educated as the average executive pushing to implement AI in everything. Fingers on Keyboard writing code You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.* If you have an engineering background, just open claude code and start building stuff. You will learn more by doing than reading at first, then build expertise around prompts and context
*   **Emotion:** The emotional tone is positive with some variation. It includes 3 positive, 2 neutral comments. Positive sentiment (average score: 0.54) is also noted.
*   **Top 3 Points of View:**
    * AI engineering skills are in demand and can help secure roles, even if traditional ML/engineering remains the core.
    * Hands-on learning by building with AI tools (e.g., Claude Code) is an effective way to gain expertise.
    * There's skepticism towards AI hype, with some suggesting superficial engagement on platforms like LinkedIn is sufficient for perceived 'expertise'.

**[ Using dlt to ingest nested api data (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1r8tkkm/using_dlt_to_ingest_nested_api_data/)**
*   **Summary:** Use dlt’s Python API to override defaults. Define a schema forcing all nested data into your target granularity - their docs have solid examples. Sure, like this : @dlt.resource(max_table_nesting=0) What if you have a parent table that has 2 children each with n records per parent row? you'd end up with cartesian product of sub-granularities? or how would you want it handled?
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Use dlt's Python API to override defaults and define schemas to control nested data granularity.
    * Explicitly setting `max_table_nesting=0` in dlt.resource can help manage nested structures.
    * Consider the implications of nested data on granularity, such as avoiding Cartesian products when dealing with multiple children per parent row.

**[ DE jobs in California (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1r9ahk0/de_jobs_in_california/)**
*   **Summary:** Your post looks like it's related to Data Engineering in India. You might find posting in [r/dataengineersindia](https://www.reddit.com/r/dataengineersindia/) more helpful to your situation. *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * The post is related to Data Engineering jobs in India, and the user is redirected to a more relevant subreddit.

**[ A week ago, I discovered that in Data Vault 2.0, people aren't stored as people, but as business entities... But the client just wants to see actual humans in the data views. (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1r9af4f/a_week_ago_i_discovered_that_in_data_vault_20/)**
*   **Summary:** how about some healthy pragmatism. do as the client wishes if it's not moronic and move on to more important stuff.
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Prioritize client needs and apply pragmatism: if the client wants to see 'humans' instead of 'business entities' in Data Vault, it's best to accommodate that if it's not fundamentally flawed.

**[ Reorged to backend team - Wwyd (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1r9b8fy/reorged_to_backend_team_wwyd/)**
*   **Summary:** Are you interested in transitioning into Data Engineering? Read our community guide: https://dataengineering.wiki/FAQ/How+can+I+transition+into+Data+Engineering *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * The user is directed to community resources for transitioning into Data Engineering, implying a career transition scenario.

**[ Career Crossroads (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1r8z5hx/career_crossroads/)**
*   **Summary:** I don't think that offer letter is an open invitation to come work whenever you're ready, if it's from September I'd assume that opportunity is long since passed
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * An old job offer (from September) is likely no longer valid, suggesting that career opportunities are time-sensitive.

**[ Advice on Setting up Version Control (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1r98afo/advice_on_setting_up_version_control/)**
*   **Summary:** Use the system that your IT department uses. This will give you: 1. Free source control system 2. Free expertise 3. Very competent help with a setup 4. Possibly also a work management system literally anything other than not doing any version control would be such much better. git was developed in 2005. just start with a *** git repo in snowflake
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * Utilize existing IT department systems for version control to leverage free resources, expertise, and integrated work management.
    * Any form of version control, even a basic Git repository, is vastly superior to having none at all.

**[ Help me find a career (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1r957nt/help_me_find_a_career/)**
*   **Summary:** You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/dataengineering) with any questions or concerns.*
*   **Emotion:** The overall emotional tone is predominantly neutral.
*   **Top 3 Points of View:**
    * The user is directed to community resources for learning and career guidance in data engineering.

**[ Would you Trust an AI agent in your Cloud Environment? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1r8qso1/would_you_trust_an_ai_agent_in_your_cloud/)**
*   **Summary:** Absolutely not. I've seen the chaos it can wreak locally, no way I want that *anywhere near* anything precious. I wouldn't trust it in dev. Actions in cloud environment have prices associated with them. Basic OpenAI or Claude prompts fail to produce meaningful SQL aggregations. For the first time we have something the result of which cannot be predicted. People with no knowledge about AI systems going gaga over it on the internet. They compare AI with calculators and say when calculators came they only made our work faster. However, the output of calculators
*   **Emotion:** The emotional tone is negative with some variation. It includes 2 negative, 1 neutral comments. Negative sentiment (average score: 0.72) is present in some comments.
*   **Top 3 Points of View:**
    * Strong skepticism exists regarding trusting AI agents in production cloud environments due to unpredictability and potential for costly errors (e.g., recursive calls, excessive API usage).
    * AI outputs are not 100% predictable, unlike calculators, making their unsupervised use risky, especially in critical environments.
    * Some might trust AI agents in local dev environments for testing, but not in production or even development cloud environments.
