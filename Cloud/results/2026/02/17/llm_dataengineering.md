---
title: "Data Engineering Subreddit"
date: "2026-02-17"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["dataengineering", "Reddit", "analysis", "trends"]
---

# Overall Ranking and Top Discussions
*   1. [In 6 years, I've never seen a data lake used properly](https://www.reddit.com/r/dataengineering/comments/1r73l52/in_6_years_ive_never_seen_a_data_lake_used/) (Score: 271)
    *   The discussion revolves around the common misuse and over-promising of data lakes, with many viewing them as utopian pipe dreams rather than practical solutions for most organizations. Some users argue that data lakes, especially when integrated with data warehouses (lakehouse architecture), can be highly effective for staging and specific data sharing needs, offering benefits like cost savings and flexibility. Others point out that failures often stem from a "tool-first" mentality, poor implementation, and a lack of understanding of actual data requirements, suggesting that simpler data warehousing or specialized databases might be more appropriate for many use cases.
*   2. [Just overwrote something in prod on a holiday.](https://www.reddit.com/r/dataengineering/comments/1r6rz37/just_overwrote_something_in_prod_on_a_holiday/) (Score: 128)
    *   Users offered support and empathy for the original poster who accidentally overwrote production data on a holiday, acknowledging such incidents as a common experience for engineers. Many emphasized that such failures are often systemic, resulting from inadequate systems, processes, backups, or access controls, rather than solely the individual's fault. The advice was to use the incident as a learning opportunity, conduct a thorough post-mortem, and implement preventative measures to improve system resilience.
*   3. [Is the Data Engineering market actually good right now?](https://www.reddit.com/r/dataengineering/comments/1r7bk2u/is_the_data_engineering_market_actually_good/) (Score: 12)
    *   The general sentiment is that the data engineering market for senior-level professionals is currently good, with high demand and frequent recruiter outreach, especially for those with specific skills or willing to work in an office. However, there's a strong undercurrent of skepticism regarding the quality of many job offers, noting that some firms are seeking highly experienced engineers for insufficient pay or presenting overly demanding and unrealistic lists of requirements, implying that some roles might not be worth the effort. The discussion also touches on the influence of AI, with many believing data engineering skills are essential for AI initiatives, contributing to a stable market despite broader tech industry uncertainties.
*   4. [Data Governance is Dead*](https://open.substack.com/pub/camdenwilleford/p/data-governance-is-dead?r=5t0kqt&utm_medium=ios&shareImageVariant=solid) (Score: 9)
    *   The discussion explores the evolving role of data governance, with some users expressing enthusiasm for how AI could automate documentation and data explanation, thereby reducing "busy work" for engineers. Others highlight persistent challenges in traditional data governance, such as difficulties in implementing rules and managing conflicting data definitions across different business functions, issues that they believe AI doesn't inherently resolve. There's also a point made that data warehouses have historically handled data cleansing and metric definitions, suggesting a long-standing pattern of governance functions being embedded within data platforms.
*   5. [Website for practicing pandas for technical prep](https://www.reddit.com/r/dataengineering/comments/1r6wius/website_for_practicing_pandas_for_technical_prep/) (Score: 4)
    *   Users recommended several platforms for practicing Pandas for technical interviews, including stratascratch.com, datawars.io, and Stat Significant, some of which also offer practice in Polars or PySpark. There were also suggestions to leverage AI tools like Grok or ChatGPT to generate custom practice problems. The conversation also included advice to consider alternative data processing libraries like Polars or dlt, especially if scalability is a concern, as they might offer better performance and syntax than Pandas for certain use cases.
*   6. [Team Lead or Senior IC?](https://www.reddit.com/r/dataengineering/comments/1r6o0rj/team_lead_or_senior_ic/) (Score: 4)
    *   The main advice given is to choose a career path (Team Lead or Senior IC) based on personal enjoyment and preference for daily work activities; a Team Lead involves more mentoring and planning, while a Senior IC stays closer to technical execution. Users also emphasized considering job stability and security, with roles in established companies (like fintech) being favored over early-stage startups during uncertain economic times. A key point was made that job titles and levels often differ significantly across companies, urging evaluation based on actual responsibilities and company context rather than just the title.
*   7. [Career Progression out of Data](https://www.reddit.com/r/dataengineering/comments/1r6o49y/career_progression_out_of_data/) (Score: 3)
    *   A user shared their experience of transitioning into warehouse automation and simulation, and moving towards a solution architect role, highlighting the potential for diverse career paths outside traditional data engineering. The advice given was to hold onto and explore any potential interests or "sparks" that arise, as finding genuine passion in a career path can be rare. A bot also provided a link to community-submitted learning resources for data engineering, offering general support for career development.
*   8. [Data Engineer at crossroads](https://www.reddit.com/r/dataengineering/comments/1r7153x/data_engineer_at_crossroads/) (Score: 2)
    *   A user questioned what "pivot into AI" truly means for a data engineer, suggesting that AI is typically a tool rather than a direct career pivot, unless one is pursuing advanced academic research roles. Another comment simply states "4.2 years ***," which might be an inside joke or a benchmark for experience, but does not provide additional distinct viewpoints.
*   9. [DataDecoded is taking on London?](https://www.reddit.com/r/dataengineering/comments/1r70ht4/datadecoded_is_taking_on_london/) (Score: 2)
    *   A user suggested attending "Data Mesh Live" in Antwerp as an alternative to DataDecoded in London, implying it might be a more suitable or cost-effective event.
*   10. [Senior Data Engineer they said, it's easy they said](https://www.reddit.com/r/dataengineering/comments/1r7bwo2/senior_data_engineer_they_said_its_easy_they_said/) (Score: 1)
    *   Many users reacted to a senior data engineer job description, highlighting that it seems to demand an unrealistic "unicorn" candidate with an overly broad and sometimes illogical skill set (e.g., deep SQL knowledge combined with VPN/MPLS networking). There's a strong sentiment that the salary offered is incompatible with the extensive role expectations, suggesting that the hiring manager might be clueless or the team is under-resourced, leading to a problematic work environment. Conversely, some comments indicated that a substantial portion of the listed requirements might be considered standard for a senior role, implying the original poster might be overwhelmed by typical responsibilities.
*   11. [Dilemma on Data ingestion migration: FROM raw to gold layer](https://www.reddit.com/r/dataengineering/comments/1r6sw5j/dilemma_on_data_ingestion_migration_from_raw_to/) (Score: 0)
    *   Users recommended explicit casting of data types during migration to prevent inference issues between different tools like Pandas and PySpark, suggesting a dedicated casting layer in the raw zone for consistency. Advice was given on handling historical data, proposing either a one-time backfill to new canonical types or appending new data after migrating old data to the new table, rather than managing two separate type systems indefinitely. The discussion also included questioning the scalability of Pandas for large datasets and suggesting alternatives like dlt or Polars, along with a robust data loading process using S3 and Redshift temporary tables for type management and upsert logic.
*   12. [Cross training timelines](https://www.reddit.com/r/dataengineering/comments/1r7fll1/cross_training_timelines/) (Score: 0)
    *   A bot comment provided a link to community-submitted learning resources for data engineering, offering a general resource for professional development and training.

# Detailed Analysis by Thread
**[In 6 years, I've never seen a data lake used properly](https://www.reddit.com/r/dataengineering/comments/1r73l52/in_6_years_ive_never_seen_a_data_lake_used/) (Score: 271)**
*  **Summary:** Data lakes are the continuation of the concept of democratization of data, only on steroids. It's been all the rage to position data lakes as some sort of magic data library where "data managers" browse every byte of the corporate data mass. Data lakes are good for staging and structured stores. Tools and teams can share data onto S3 in their native format. The staff data engineer is an aws fan boy. He's the only person that seems to know how any of this works. Iceberg files/tables solve Netflix's problems. Most of his B2B customers have less than 100 million rows in their largest table. 90% of tables can be easily read in one go without needing delta loads. Streaming and batch data are processed in the same way. The key difference between the two is that the batch method keeps the raw data in s3 via external tables, while the streaming method loads the CDC events into a table resting in the data warehouse. I don’t see any reason why I would want to go back to a database after adopting Delta? Alan Kay sells datalake with the idea that data scientists can do exploratory analysis on the raw unstructured data. It's been over a year and he hasn't seen any insights. Datalake and databricks are useful for data-driven stuff. They model the infrastructure, create some processes, and give power to the people within some defined boundaries. All this is happening because the management needs to adapt to new technologies.

My company was running in On Prem until 1.5 years back and I was specifically hired to setup AWS + Databricks. Because the management decided its cloud era.

Same tables , same dimensions, but within Databricks.
Only positive thing is I get paid to do this.
*  **Emotion:** The emotional tone is mixed, with 3 positive, 7 neutral sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * Data lakes are often misused or are utopian pipe dreams for most organizations, failing to deliver on promises of data democratization and easy access.
    * Data lakes, when combined with structured stores (Lakehouse approach) or used for specific purposes like staging, can be effective and provide benefits like cost savings and data sharing.
    * The challenges with data lakes stem from a 'tool-first' mentality, bad implementation, over-engineering, and a lack of understanding of underlying data needs; simpler data warehouses or purpose-built databases might be better for most use cases.

**[Just overwrote something in prod on a holiday.](https://www.reddit.com/r/dataengineering/comments/1r6rz37/just_overwrote_something_in_prod_on_a_holiday/) (Score: 128)**
*  **Summary:** Send wishes for a president day miracle, for you Sending virtual hugs. Their should be systems and processes in place to stop this sort of thing even being possible, so if it's any comfort this is everyone f up, you just happen to be in the center 😅 There are systems missing that should have prevented the big ups. Write up a strong post mortem and prescribe a system you can implement to prevent someone else from doing the same thing in the future. You don't have backups to restore from? The best way to deal with the stress chemicals you are probably flooded with is to exercise.   It's not your fault - there are policy and system issues that allowed the event to occur. The swiss cheese theory of accidents Having a downstream with longer retention than upstream and no way to recover (cold storage, undelete, etc) was a disaster waiting to happen anyway. You just happened to be the catalyst. Your company data warehouse and infrastructure isn't set up correctly. I know that feeling. I caused an incident like this by deleting a kafka topic once. One of us! One of us!

Edit to add: it happened to all of us, it's almost a rite of passage at that point. And seeing the setup you described, it was going to happen at some point, it's not on you.

Now use that incident to learn how you can protect yourself for next time :)
*  **Emotion:** The emotional tone is mixed, with 4 positive, 5 neutral, 1 negative sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * The incident is a systemic failure, not just the individual's fault, due to missing safeguards like proper backups, access controls, or robust testing in the production environment.
    * Support and empathy for the person, acknowledging that such incidents are common rites of passage for engineers, and suggesting self-care (like exercise).
    * The incident should be used as an opportunity for learning and implementing preventative measures through a post-mortem to improve future system resilience.

**[Is the Data Engineering market actually good right now?](https://www.reddit.com/r/dataengineering/comments/1r7bk2u/is_the_data_engineering_market_actually_good/) (Score: 12)**
*  **Summary:** What skills do you have on your profile to get reached out to ? I think yes, but seasonally. Its difficult for me to apply in 3rd and 4th quarter. But now I only applied to 4 jobs, got 3 interviews with verbal offers now. 30% jump. People realising data engineer is required for AI and it is also taking over to what level reporting was 5 years back. Yup, I've been noticing the same. I've also been getting popular profile alerts even though I haven't made an update in like 3 years. There's a lot of interest in the last few weeks from younger firms looking for a senior engineer. Most of the jobs look like they blow and are not worth the money. Every company is looking to hire a senior engineer to fix everything, migrate to the cloud, help the junior engineers or specialize in a particular software. If you’re a senior and willing to work in an office, yes. Also if you’re willing to do senior-level work for junior-level pay. I think it’s normal, which is amazing in a ai software apocalypse. The market for senior DEs in Norway is very good. 4 YoE

Seems pretty good to me.

Not as good as 2-5 years ago, but there’s no shortage of recruiter outreach and the salaries are decent, if a bit lower across the board unless it’s a role for an AI company.
*  **Emotion:** The emotional tone is mixed, with 4 positive, 5 neutral, 1 negative sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * The market for senior Data Engineers is currently good, with high demand and recruiters actively seeking experienced candidates, especially those with specific skills or willingness for certain conditions (e.g., office work).
    * There's skepticism about the quality of some job offers, with firms seeking senior talent for junior-level pay, high expectations, and demanding requirements, suggesting some roles are not worth it.
    * AI is influencing the demand for Data Engineers, as their skills are crucial for AI initiatives, and the market generally feels stable despite broader tech uncertainties.

**[Data Governance is Dead*](https://open.substack.com/pub/camdenwilleford/p/data-governance-is-dead?r=5t0kqt&utm_medium=ios&shareImageVariant=solid) (Score: 9)**
*  **Summary:** Great for the documentation part of Governance; I'm not too sure how it will work with the rules and implementation part of it. Thanks, loved the first half! Lost me in the second, though. Will you reframe the approach you're proposing as the solution? I read it twice and it's not clicking. Data warehouses have always cleaned up data that couldn't be repaired in upstream sources. They define metrics that aren't in upstream systems. AI can maintain the governance documentation and explain the data to the users.
*  **Emotion:** The emotional tone is mixed, with 2 positive, 2 neutral sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * AI could revolutionize data governance by automating documentation and data explanation, freeing engineers from manual 'busy work'.
    * Traditional data governance faces challenges in implementing rules and dealing with inconsistent data definitions across different business units, a problem that AI doesn't inherently solve.
    * Data warehouses have historically handled data cleanup and metric definition, suggesting some governance functions have always been managed at the data platform level rather than purely through policy.

**[Website for practicing pandas for technical prep](https://www.reddit.com/r/dataengineering/comments/1r6wius/website_for_practicing_pandas_for_technical_prep/) (Score: 4)**
*  **Summary:** stratascratch.com Unsure if it's the type of questions you want but this site has the option of choosing pandas, polars or pyspark Sign in and filter for the free questions have grok/chatgpt whip stuff up for you datawars.io Use Stat Significant.
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Recommendations for specific websites like stratascratch.com, datawars.io, and Stat Significant for practicing data manipulation skills.
    * Suggestions to use AI tools like Grok/ChatGPT to generate practice material.
    * Consideration of alternative data processing libraries like Polars or PySpark, especially for scalability, instead of Pandas.

**[Team Lead or Senior IC?](https://www.reddit.com/r/dataengineering/comments/1r6o0rj/team_lead_or_senior_ic/) (Score: 4)**
*  **Summary:** A team lead role will probably mean less hands on coding and more time mentoring, planning and dealing with stakeholders. Senior IC path keeps you closer to the tech and might sharpen your skills faster. AI proofing is safe if you build real judgment and system design skills. May I know the country? I’d favor stability/security right now. The job market is bad and has potential to get worse. Take the fintech team lead role imo. The startup sounds early and has more likelihood of going bust overnight. Good luck Titles at different companies doesn’t translate well. I know several people who came from some small companies had titles director or above but joined Amazon as L6 manager.

There were times when Amazon, Meta acquired some companies and CEOs joined as directors.

Levels at different companies translate differently. You need to decide for yourself which career path you want to follow.
*  **Emotion:** The emotional tone is mixed, with 2 positive, 3 neutral sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * Career choice depends on personal enjoyment: Team Lead involves more mentoring and planning, less coding; Senior IC stays closer to tech, sharpening skills.
    * Stability and security should be considered, with team lead roles in established companies (like fintech) potentially offering more security than early-stage startups.
    * Titles and levels vary significantly across companies, so one must assess roles based on actual responsibilities and company context rather than just the title.

**[Career Progression out of Data](https://www.reddit.com/r/dataengineering/comments/1r6o49y/career_progression_out_of_data/) (Score: 3)**
*  **Summary:** I went into warehouse automation and simulation oddly enough and seem to be headed in a more solution artichectesque direction. If you find a potential interest, hold onto it, that spark it's hard to come by! You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Exploring alternative career paths like warehouse automation and simulation, leading towards solution architecture.
    * The importance of following personal interests and 'sparks' when considering career changes.
    * Resources for learning and career development in data engineering (bot comment).

**[Data Engineer at crossroads](https://www.reddit.com/r/dataengineering/comments/1r7153x/data_engineer_at_crossroads/) (Score: 2)**
*  **Summary:** What does "pivot into AI" mean? One simply uses the tool, they do not pivot to it. Unless you are planning on getting a PHD and moving to California 4.2 years ***
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Skepticism about the term 'pivot into AI,' suggesting AI is a tool to be used rather than a career path unless pursuing advanced research roles.
    * Simple, non-elaborated comment suggesting a specific experience duration, possibly implying a benchmark or an inside joke.
    * No additional distinct point of view identified.

**[DataDecoded is taking on London?](https://www.reddit.com/r/dataengineering/comments/1r70ht4/datadecoded_is_taking_on_london/) (Score: 2)**
*  **Summary:** Come to Antwerp for Data Mesh Live instead. Probably cheaper to go from MCR to Antwerp than London anyway :-D
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Suggesting an alternative conference, 'Data Mesh Live' in Antwerp, as a potentially better or cheaper option.
    * No additional distinct point of view identified.
    * No additional distinct point of view identified.

**[Senior Data Engineer they said, it's easy they said](https://www.reddit.com/r/dataengineering/comments/1r7bwo2/senior_data_engineer_they_said_its_easy_they_said/) (Score: 1)**
*  **Summary:** What's the issue? Is salary monthly or a yearly figure? Which country? If you're phased by anything in the job specification, you're not at a senior level. okay, but which country? Looks about right for senior position. This is like a third of what I do :D The previous person didn't understand how networks work. For such a small monthly salary I hope it's 100% remote. A unicorn All of that seems pretty standard expectations for a senior level role except for the last one. I'm not sure what SQL has to do with networking. Tensorflow? Uh oh. Sounds like you will be wearing ALL of the hats, or maybe the guy who made the post is an idiot:

"SQL - deep understanding of ... VPNs, MPLs..." .. Well, that answers our question. Salary is not compatible to role expectations. Increase to at least 6k and you’ll get some decent candidates.

I’d pass hard on this role. Looks like too much trouble for the money.

The hiring manager either have no clue what he needs or the team is not minimally capable. Either way, bright red flag
*  **Emotion:** The emotional tone is mixed, with 1 positive, 7 neutral, 2 negative sentiments contributing to the discussion.
*  **Top 3 Points of View:**
    * The job description seems to demand an unrealistic 'unicorn' engineer with an extensive and sometimes illogical skill set (e.g., SQL and deep networking knowledge) for a potentially low salary, indicating a clueless hiring manager.
    * The listed expectations are standard for a senior role, implying the original poster might be overwhelmed by typical senior responsibilities or the salary is too low for the scope.
    * Salary expectations are not compatible with the role's demands; the role requires an increase in pay to attract decent candidates, and the scope suggests potential for a problematic work environment.

**[Dilemma on Data ingestion migration: FROM raw to gold layer](https://www.reddit.com/r/dataengineering/comments/1r6sw5j/dilemma_on_data_ingestion_migration_from_raw_to/) (Score: 0)**
*  **Summary:** The VIEW union approach works for the new ingestion path. Pandas sometimes gets more specific than PySpark. If you are switching to the new type system permanently, you might consider backfilling the old data. For large datasets, I save the data to s3 as a parquet and copy to a temp redshift table, and then copy from the temp to the target table. Redshift table determines the types, and you can control what types you send redshift from python to Why pandas? If you have to scale you would need to already change engines. Prefer dlt or polars. Polars has better syntax anyhow. Kinda what others said, use explicit casting. Don't rely on auto types. When the data type drifts, retain the most permissive data type. For example, if the old is a varchar and the new is an int, use vARCHar. If the historic data was stored as varchars, you can query to confirm all the values
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Recommendations to use explicit casting for data types to avoid inference issues (e.g., Pandas vs. PySpark) and ensure compatibility during migration, potentially with a casting layer in the raw zone.
    * Suggestions for handling historical data: either backfill old data to match new canonical types or append new data after migrating old data to the new table, rather than maintaining two type systems.
    * Questioning the use of Pandas for scalability and suggesting alternatives like dlt or Polars, and outlining a process using S3 and Redshift temp tables for robust data loading and type management.

**[Cross training timelines](https://www.reddit.com/r/dataengineering/comments/1r7fll1/cross_training_timelines/) (Score: 0)**
*  **Summary:** You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * A bot comment suggesting a list of community-submitted learning resources for data engineering, which is a general resource for professional development.
    * No additional distinct point of view identified.
    * No additional distinct point of view identified.
