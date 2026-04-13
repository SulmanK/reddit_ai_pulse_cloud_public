---
title: "Data Engineering Subreddit"
date: "2026-02-23"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "data pipelines", "programming languages", "career advice", "data tools"]
---

# Overall Ranking and Top Discussions
*   1. [Can seniors suggest some resource to learn data pipeline design.](https://www.reddit.com/r/dataengineering/comments/1rccu65/can_seniors_suggest_some_resource_to_learn_data/) (Score: 21)
    *   What helped me was sketching simple architectures for real use cases.
*   2. [Java scala or rust ?](https://www.reddit.com/r/dataengineering/comments/1rcixei/java_scala_or_rust/) (Score: 5)
    *   SQL > Python (polars/pySpark) > Java/Scala (Spark).
*   3. [Has anyone found a self healing data pipeline tool in 2026 that actually works or is it all marketing](https://www.reddit.com/r/dataengineering/comments/1rcmam2/has_anyone_found_a_self_healing_data_pipeline/) (Score: 4)
    *   It’s a newer terminology but self healing pipelines have become a thing now that LLMs can “make decisions” on the next steps for a failed job.
*   4. [How are you selling datalakes and data processing pipeline?](https://www.reddit.com/r/dataengineering/comments/1rcos21/how_are_you_selling_datalakes_and_data_processing/) (Score: 4)
    *   Don't sell the tool.
*   5. [Netflix Data Engineering Open Forum 2026](https://www.reddit.com/r/dataengineering/comments/1rcldox/netflix_data_engineering_open_forum_2026/) (Score: 4)
    *   Can you share a link?
*   6. [How Own Risks and Boost Your Data Career](https://www.datagibberish.com/p/how-to-own-risks-and-boost-your-data-career) (Score: 3)
    *   Man I wish I could give you an award.
*   7. [Left alone facing business requirements without context](https://www.reddit.com/r/dataengineering/comments/1rcf6em/left_alone_facing_business_requirements_without/) (Score: 2)
    *   Project yourself into a new role and think about what questions you would ask if you were in that role.
*   8. [Major career change into DE](https://www.reddit.com/r/dataengineering/comments/1rcppq7/major_career_change_into_de/) (Score: 2)
    *   good luck.
*   9. [Same PKI, same raw data, two platforms (Databricks, Snowflake)… different results. Where would you even start debugging this?](https://www.reddit.com/r/dataengineering/comments/1rc1qde/same_pki_same_raw_data_two_platforms_databricks/) (Score: 1)
    *   There are 350+ pipelines in this project.
*   10. [Planning to migrate to SingleStore worth it?](https://www.reddit.com/r/dataengineering/comments/1rcs0jb/planning_to_migrate_to_singlestore_worth_it/) (Score: 1)
    *   singlestore's fast, but costly.
*   11. [RANT, I have break into DE](https://www.reddit.com/r/dataengineering/comments/1rcfayc/rant_i_have_break_into_de/) (Score: 0)
    *   Do some end to end projects and focus on the foundations you should be good.
*   12. [Is databricks + dbt still a great solution or should I look to study or migrate to other strategy?](https://www.reddit.com/r/dataengineering/comments/1rcnr89/is_databricks_dbt_still_a_great_solution_or/) (Score: 0)
    *   You talk about solutions without mentioning your problems ….
*   13. [Are ‘Fabric Analysts’ just Data Engineers with a lower salary, or is there a real difference in 2026?](https://www.reddit.com/r/dataengineering/comments/1rcr4wr/are_fabric_analysts_just_data_engineers_with_a/) (Score: 0)
    *   You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources.

# Detailed Analysis by Thread
**[Can seniors suggest some resource to learn data pipeline design. (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1rccu65/can_seniors_suggest_some_resource_to_learn_data/)**
*  **Summary:** Dagster university. Dbt documentation and their courses. Data Engineering Design Patterns by Bartosz Konieczny might be close what you are after. There are few cases when you should use Stream processing. What helped me was sketching simple architectures for real use cases. You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources.
*  **Emotion:** Predominantly Neutral with a slightly positive underlying tone.
*  **Top 3 Points of View:**
    * Leverage practical, real-world experience like sketching architectures for use cases and reverse-engineering existing pipelines.
    * Consult established learning resources such as specific books (e.g., 'Designing Data-Intensive Applications', 'Fundamentals of Data Engineering') and community wikis.
    * Consider product-centric courses (Dagster, dbt) for practical application, and focus on core skills like SQL, Python, Spark, and data modeling concepts, prioritizing batch processing over streaming where possible.
**[Java scala or rust ? (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1rcixei/java_scala_or_rust/)**
*  **Summary:** I know all 3 I didn’t learn them for DE just out of curiosity. I liked Scala a lot, it's a really interesting language, sadly it seems that it's not a used as java, so I'd pick java. In my personal experience, Python is the end all be all for most tasks. It depends on the type of DE work you do. It's good to understand programming languages, but it's probably not necessary for a lot of DE jobs. Rust is starting to replace Java and scala in data processing framework. SQL > Python (polars/pySpark) > Java/Scala (Spark). You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources.
*  **Emotion:** Mixed, but predominantly Neutral.
*  **Top 3 Points of View:**
    * Python and SQL are considered primary for most data engineering tasks, with other languages like Java, Scala, or Rust being secondary for specialized uses.
    * Rust is gaining traction for streaming and performance-oriented data processing frameworks (e.g., Polars, Apache DataFusion), potentially replacing Java/Scala in certain contexts.
    * Understanding diverse programming languages is beneficial for architectural knowledge (e.g., Scala for Spark) and cross-team collaboration, but may not be strictly necessary for daily DE jobs.
**[Has anyone found a self healing data pipeline tool in 2026 that actually works or is it all marketing (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1rcmam2/has_anyone_found_a_self_healing_data_pipeline/)**
*  **Summary:** Automatic retries and exponential backoff are not self-healing. Auto messaging to the corpo messenger in airflow through webhooks is a new concept for me. I’m not aware of any self-healing data pipeline tools. Imo pipelines and data contracts should be rigid. It’s a newer terminology but self healing pipelines have become a thing now that LLMs can “make decisions” on the next steps for a failed job. No tooling can self-adjust if API endpoint suddenly disappears or the spec changes. Same question is running in my head & I have checked or tried doing research but couldn’t find much info. The interesting part is when tools detect that an api schema changed and automatically adjust the extraction logic. We switched our saas ingestion to precog and the connector maintenance went to basically zero because they handle the api changes on their end.
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * True '100% self-healing pipelines' that autonomously adapt to major API or schema changes are considered marketing hype and do not widely exist.
    * AI-assisted repair with human oversight, involving detection, sandbox testing, and human approval, is a more realistic and controlled approach to pipeline resilience.
    * Pipelines should ideally be rigid and fail loudly on unexpected changes to prevent data corruption, with basic resilience mechanisms like retries not constituting true self-healing.
**[How are you selling datalakes and data processing pipeline? (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1rcos21/how_are_you_selling_datalakes_and_data_processing/)**
*  **Summary:** A data lake is not always a good idea for every company. A trigger for adopting datalake solution is complexity of managing data & metadata at scale. Don't sell the tool. The fist step is to be convinced yourself of the value you are proposing before trying to convince your customer.
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * Focus on selling the business capabilities and value derived from data lakes and processing pipelines, rather than the tools themselves.
    * The primary drivers for data lake adoption are the increasing complexity of managing data and metadata at scale, and the rising costs of operations with growing data volumes and teams.
    * It's crucial to acknowledge that data lakes are not universally beneficial; for many businesses, simpler solutions like spreadsheets might suffice, and the value proposition must directly demonstrate financial or operational gains.
**[Netflix Data Engineering Open Forum 2026 (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1rcldox/netflix_data_engineering_open_forum_2026/)**
*  **Summary:** Can you share a link?
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    * Users are seeking official links and information about the Netflix Data Engineering Open Forum 2026.
    * There's a general lack of public information or resources available for this specific event through standard search methods.
    * The community expresses interest in details about Netflix's data engineering initiatives and events.
**[How Own Risks and Boost Your Data Career (Score: 3)](https://www.datagibberish.com/p/how-to-own-risks-and-boost-your-data-career)**
*  **Summary:** Man I wish I could give you an award.
*  **Emotion:** Predominantly Positive.
*  **Top 3 Points of View:**
    * The provided article is highly praised for being well-written and insightful.
    * It offers valuable guidance on managing career risks within the data engineering field.
    * The content is perceived as beneficial for personal and professional growth in data careers.
**[Left alone facing business requirements without context (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1rcf6em/left_alone_facing_business_requirements_without/)**
*  **Summary:** Get good at asking questions and building things that help is what sets engineers apart. It might be an opportunity for you to interact with end users to understand their core need and get some business context. Most people are more than happy to explain what they do. Project yourself into a new role and think about what questions you would ask if you were in that role.
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * This situation presents an opportunity for engineers to develop critical soft skills, particularly in engaging with stakeholders and understanding business context directly.
    * Proactively asking clarifying questions and reiterating understanding of business problems is essential for effective solution design.
    * Empathy and curiosity, by trying to understand the stakeholder's role and pain points, are key to building trust and delivering impactful solutions.
**[Major career change into DE (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1rcppq7/major_career_change_into_de/)**
*  **Summary:** You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources. good luck.
*  **Emotion:** Mixed, with a dominant Neutral tone but some Positive sentiment.
*  **Top 3 Points of View:**
    * A recommended starting point for a career change into Data Engineering is to gain experience as a Data Analyst and master SQL.
    * Leveraging community-provided learning resources is advised for self-study and skill development.
    * The transition is seen as a positive career move, with an emphasis on foundational knowledge acquisition.
**[Same PKI, same raw data, two platforms (Databricks, Snowflake)… different results. Where would you even start debugging this? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1rc1qde/same_pki_same_raw_data_two_platforms_databricks/)**
*  **Summary:** There are 350+ pipelines in this project. The first 2 points must be fixed in order to get reliable result and success. The data hunt should focus on 2 to 5 KPI's and the data they rely on.
*  **Emotion:** Predominantly Positive.
*  **Top 3 Points of View:**
    * Prioritize debugging fundamental issues such as sporadic errors and data loss from type conversions, as these are critical for ensuring reliable data results.
    * Adopt a systematic debugging approach by breaking down the pipeline, auditing specific KPIs midway through the data flow, and comparing curated tables.
    * Communicate findings clearly to management, advocate for improved tooling (like lineage tools), and collaborate with teammates while managing expectations on timelines.
**[Planning to migrate to SingleStore worth it? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1rcs0jb/planning_to_migrate_to_singlestore_worth_it/)**
*  **Summary:** Personally, I wouldn't adopt a product that just got taken over by private equity. singlestore's fast, but costly.
*  **Emotion:** Mixed, with a dominant Negative tone but some Positive sentiment.
*  **Top 3 Points of View:**
    * SingleStore offers high performance but comes with significant costs, necessitating a careful evaluation of whether performance gains justify the migration effort and budget.
    * Concerns are raised regarding the long-term viability and strategic direction of products recently acquired by private equity, suggesting potential risks of profit-mining over product development.
    * The decision involves assessing current technical debt and the overall ecosystem compatibility with SingleStore.
**[RANT, I have break into DE (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rcfayc/rant_i_have_break_into_de/)**
*  **Summary:** Do some end to end projects and focus on the foundations you should be good. Get a junior data engineer role instead of shooting for a mid. Learn the language of choice, general knowledge of deployment, database basics, how APIs work and how http communciation works is a good one. You have the theory under control, but you need to practice more.
*  **Emotion:** Predominantly Positive.
*  **Top 3 Points of View:**
    * Emphasis on hands-on, end-to-end projects built from scratch to solidify theoretical knowledge and gain practical confidence.
    * Mastering foundational technical skills: Python, SQL, Docker, cloud basics (leveraging free tiers), database types (NoSQL, SQL, data warehouses), and understanding APIs/HTTP communication.
    * Considering a junior data engineer role is a practical step to bridge the gap between theoretical learning and real-world industry experience.
**[Is databricks + dbt still a great solution or should I look to study or migrate to other strategy? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rcnr89/is_databricks_dbt_still_a_great_solution_or/)**
*  **Summary:** You talk about solutions without mentioning your problems ….
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * The suitability of Databricks + dbt as a solution is entirely dependent on the specific business problems and requirements it aims to solve.
    * Users are advised to clearly articulate their existing challenges before seeking or evaluating specific tooling or migration strategies.
    * The general sentiment is that a solution's 'greatness' is measured by its effectiveness in addressing defined problems.
**[Are ‘Fabric Analysts’ just Data Engineers with a lower salary, or is there a real difference in 2026? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rcr4wr/are_fabric_analysts_just_data_engineers_with_a/)**
*  **Summary:** Are databricks engineers just data engineers with lower salaries? There's a bit to unpack here, but you shouldn't be expected to accept a lower compensation rate based on a "job title" that is misaligned to the actual job you're doing. This post is so Indian that I knew it before I even checked OPs post history :). You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources.
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * The core discussion revolves around whether the 'Fabric Analyst' role is distinct or merely a rebranding of Data Engineer with potentially lower compensation.
    * It's asserted that compensation should align with the actual job responsibilities, irrespective of a potentially misleading job title.
    * The question highlights broader industry concerns about evolving job titles and their impact on role definition and salary expectations.
