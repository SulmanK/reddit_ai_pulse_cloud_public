---
title: "Data Engineering Subreddit"
date: "2026-02-26"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "LLMs", "business logic", "parquet", "FAANG", "AI"]
---

# Overall Ranking and Top Discussions
* 1. [Life before LLMs](https://i.redd.it/r4tsphz1qslg1.jpeg) (Score: 48)
    * Nostalgia is great, but don't get lost in it. Things are going to change in your career. How you adapt to these changes over your career is what makes or breaks it.
* 2. [Where should Business Logic live in a Data Solution?](https://leszekmichalak.substack.com/p/where-should-business-logic-live) (Score: 39)
    * Silver to Gold layers are more simple filters or pre-aggregations for end users. They don't have to worry about filtering or handling conversions. Nice article. I think the tension I find is trying to not reload upstream (and therefore everything downstream) with biz logic that changes frequently. Especially true if that logic is feeding other systems and trying to keep everything idempotent, sending signals that a particular record not longer qualifies (ie soft delete and not filtering), etc. Enjoyed it. I agree. Now if you can please help me convince leadership that it’s worth spending time on making it a reality instead of consistently dealing with problems caused by the business logic sprawling everywhere.
* 3. [Hardwood: A New Parser for Apache Parquet](https://www.morling.dev/blog/hardwood-new-parser-for-apache-parquet/) (Score: 25)
    * That is beautiful! Finally we have a Hadoop-free parquet in JVM ecosystem! great stuff Gunnar, congrats!
* 4. [I finally found a use case for Go in Data Engineering](https://www.reddit.com/r/dataengineering/comments/1rfe366/i_finally_found_a_use_case_for_go_in_data/) (Score: 12)
    * I've occasionally used Bento, which is written in go.
https://github.com/warpstreamlabs/bento. How does it compare to sling. Sounds interesting, care to share your work?
* 5. [Breaking Into FAANG](https://www.reddit.com/r/dataengineering/comments/1rfhg8b/breaking_into_faang/) (Score: 10)
    * When I interviewed at Amazon, they cared more about behavioral skills and stories about making an impact over your career than technical skills. I wouldn't recommend working there though, it drains your life energy. The most challenging part for most DE applicants is landing an interview. It's much easier than you think. Be strong on:1. Behavioral, 2. SQL, 3. Leetcode, 4 Architecture and 5 Data Modeling. You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources. Microsoft, Meta and Amazon/AWS are all involved with Epstein. Main prep for interviewing at those companies is leetcode - you should master all of the hardest SQL leetcode questions, and all easy/medium python question
* 6. [Sqlmesh randomly drops table when it should not](https://www.reddit.com/r/dataengineering/comments/1rf81by/sqlmesh_randomly_drops_table_when_it_should_not/) (Score: 6)
    * You'd best ask on the sqlmesh discord.
* 7. [Automated GBQ Slot Optimization](https://www.reddit.com/r/dataengineering/comments/1rf2w4q/automated_gbq_slot_optimization/) (Score: 5)
    * Building this in-house is usually better than overpaying for a SaaS, but I'm curious about the 'automatic' part. How do you handle edge cases where a sudden spike is actually a critical business query that shouldn't be throttled? A 10-12% saving is great, but did you notice any impact on query latency during peak times?. What did you end up doing? And how did you do it?
* 8. [Data gaps](https://www.reddit.com/r/dataengineering/comments/1rf6rc6/data_gaps/) (Score: 5)
    * Gap filling should be an event to fix asap, not be an overnight thing. A DE knows programming and can make the necessary tool to use in the workflow process. To fix gaps, quantify the gaps and set up simple freshness and row count checks per location. It's worth checking if their export schedule or batching logic differs from the others.
* 9. [What's the rsync way for postgres?](https://www.reddit.com/r/dataengineering/comments/1rf7uug/whats_the_rsync_way_for_postgres/) (Score: 2)
    * Are you looking to write your own solution? It is possible, but there are many tools that can do this for you. Look into log-based change data capture: it’s the safest way to extract data out of Postgres without actually having to query the tables. logs?
* 10. [Did you already faced failed migrations? How it was?](https://www.reddit.com/r/dataengineering/comments/1resrgh/did_you_already_faced_failed_migrations_how_it_was/) (Score: 1)
    * The new way of doing most migration is to create a new cost center for the new migration, sort teams by the amount they pay and move the teams that are paying the most out of the old one. The key to successful migrations is having a end goal with a flexible deadline and key milestones that you can achieve on the way to said deadline. It's also important to scope what is and isn't a part of the migration up front so you waste as little time with scope creep and
* 11. [Ontology driven data modeling](https://www.reddit.com/r/dataengineering/comments/1rf8u09/ontology_driven_data_modeling/) (Score: 0)
    * This is on most data expert's radar.

Semantic layer can include ontology information, if you make it to.

The only thing I disagree with is to use ontology to drive data modeling. Ontology doesn't answer all questions that data modeling needs.

I work on this topic on daily basis. Ontology driven data modeling is already what everyone is doing. The point of the field is to take data without context and put it into context to provide business meaning. Even using top tier tooling, I get so many data issues that require repair. LLMs need to learn the ontology from the simplified relationships in a model before they can understand it. An Ontology is a form of a dimensional model. A semantic layer is almost always a text-based model. An LLM can use it to answer questions about a product, a customer, an event, a date, a sale or a campaign. Why would ontology not be on the radar? Nice topic to bring up but odd way of getting people interested. I have built this, but it use the knowledge graph based on which it answers user's question.
Happy to collaborate and solve this very overlooked problem. i’m basically doing this now at work and agree with you. meta models are key. it’ll help humans conceptualize data as well. Saw the title thought I walked in on a Curt Jaimungal podcast. When serving raw data to LLM, rather than giving ERD and column definitions, we give it the ontology. What does that mean in practice? What are examples of code that incorporate ontology, compared to code that doesn't?
* 12. [How good can you use AI in DE?](https://www.reddit.com/r/dataengineering/comments/1reqytb/how_good_can_you_use_ai_in_de/) (Score: 0)
    * It works better for small tasks like creating a SQL with rows from 1 to 1000 or repetitive tasks over something locally defined like a JSON schema object or several files that import the same function. It is not magic but it can help. What do you mean by legacy data engineering projects?. I’ve tried using AI and it works well in several use case. But code review has become increasingly more important. This week we tried ontology driven development and it works, we put some of the experiments in prod as it was better than human quality. Clauude code has created skills for querying BQ, running dbt and validating data pipelines. CC has been having CC write .ipynb files I can import into Hex and then use Hex LLM to do the final bits of creating all the dashboard inputs. Doesn’t do modeling. So at most AI answers questions about the cloud and tools. Works fine when there is something SWE related but basically useless for DE work. I find it incredibly useful when it comes to documentation, creating ER diagrams, investigating data discrepancies (especially if you use an MCP tool to directly query your data), and automate boring/admin type tasks. >... they’re making code better ...

Oh boy

# Detailed Analysis by Thread
**[ Life before LLMs (Score: 48)](https://i.redd.it/r4tsphz1qslg1.jpeg)**
*  **Summary:** Nostalgia is great, but don't get lost in it. Things are going to change in your career. How you adapt to these changes over your career is what makes or breaks it.
*  **Emotion:** Predominantly Positive
*  **Top 3 Points of View:**
    * Nostalgia for 'life before LLMs' is appreciated, but the constant and intense change in data engineering careers means adaptability is paramount for success.
    * Success in data engineering is defined by one's ability to adapt to continuous technological and methodological changes over a long career span.

**[ Where should Business Logic live in a Data Solution? (Score: 39)](https://leszekmichalak.substack.com/p/where-should-business-logic-live)**
*  **Summary:** Silver to Gold layers are more simple filters or pre-aggregations for end users. They don't have to worry about filtering or handling conversions. Nice article. I think the tension I find is trying to not reload upstream (and therefore everything downstream) with biz logic that changes frequently. Especially true if that logic is feeding other systems and trying to keep everything idempotent, sending signals that a particular record not longer qualifies (ie soft delete and not filtering), etc. Enjoyed it. I agree. Now if you can please help me convince leadership that it’s worth spending time on making it a reality instead of consistently dealing with problems caused by the business logic sprawling everywhere.
*  **Emotion:** Predominantly Positive
*  **Top 3 Points of View:**
    * A significant challenge is preventing frequent business logic changes from triggering costly reloads across data pipelines, highlighting the need for idempotent systems.
    * It's difficult to convince leadership to invest in robust business logic placement despite the long-term problems caused by sprawling logic.
    * A multi-layered data architecture (e.g., Bronze to Silver for transformations, Silver to Gold for simple aggregations) effectively manages business logic and improves end-user experience.

**[ Hardwood: A New Parser for Apache Parquet (Score: 25)](https://www.morling.dev/blog/hardwood-new-parser-for-apache-parquet/)**
*  **Summary:** That is beautiful! Finally we have a Hadoop-free parquet in JVM ecosystem! great stuff Gunnar, congrats!
*  **Emotion:** Predominantly Positive
*  **Top 3 Points of View:**
    * The introduction of 'Hardwood' as a new parser for Apache Parquet is a highly positive development.
    * It provides a much-anticipated Hadoop-free Parquet solution within the JVM ecosystem.

**[ I finally found a use case for Go in Data Engineering (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1rfe366/i_finally_found_a_use_case_for_go_in_data/)**
*  **Summary:** I've occasionally used Bento, which is written in go.
https://github.com/warpstreamlabs/bento. How does it compare to sling. Sounds interesting, care to share your work?
*  **Emotion:** Predominantly Neutral
*  **Top 3 Points of View:**
    * Users are interested in understanding how Go-based data engineering solutions compare to existing tools like Sling.
    * There's curiosity about specific practical applications and shared experiences of using Go in data engineering.
    * Other Go-based tools, such as Bento, are also being used for data engineering tasks.

**[ Breaking Into FAANG (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1rfhg8b/breaking_into_faang/)**
*  **Summary:** When I interviewed at Amazon, they cared more about behavioral skills and stories about making an impact over your career than technical skills. I wouldn't recommend working there though, it drains your life energy. The most challenging part for most DE applicants is landing an interview. It's much easier than you think. Be strong on:1. Behavioral, 2. SQL, 3. Leetcode, 4 Architecture and 5 Data Modeling. You can find a list of community-submitted learning resources here: https://dataengineering.wiki/Learning+Resources. Microsoft, Meta and Amazon/AWS are all involved with Epstein. Main prep for interviewing at those companies is leetcode - you should master all of the hardest SQL leetcode questions, and all easy/medium python question
*  **Emotion:** Mixed, with some negative sentiment
*  **Top 3 Points of View:**
    * Comprehensive preparation for FAANG data engineering interviews requires mastering LeetCode (especially hard SQL and easy/medium Python) and strong behavioral skills.
    * Amazon interviews emphasize behavioral skills and impact stories, but working there can lead to burnout due to intense demands.
    * Some FAANG DE roles (e.g., Meta, Google) lean more towards Analytics Engineering, focusing heavily on SQL, and there are concerns about job security (layoffs) at these companies.

**[ Sqlmesh randomly drops table when it should not (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1rf81by/sqlmesh_randomly_drops_table_when_it_should_not/)**
*  **Summary:** You'd best ask on the sqlmesh discord.
*  **Emotion:** Predominantly Neutral
*  **Top 3 Points of View:**
    * Issues with Sqlmesh, such as unexpected table drops, are best addressed by seeking support on the official Sqlmesh Discord channel.

**[ Automated GBQ Slot Optimization (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1rf2w4q/automated_gbq_slot_optimization/)**
*  **Summary:** Building this in-house is usually better than overpaying for a SaaS, but I'm curious about the 'automatic' part. How do you handle edge cases where a sudden spike is actually a critical business query that shouldn't be throttled? A 10-12% saving is great, but did you notice any impact on query latency during peak times?. What did you end up doing? And how did you do it?
*  **Emotion:** Predominantly Neutral
*  **Top 3 Points of View:**
    * In-house automated BigQuery slot optimization is seen as a cost-effective alternative to SaaS, but needs to carefully manage critical business queries to prevent throttling.
    * Concerns exist regarding how automatic optimization handles sudden spikes from critical queries and its potential impact on query latency during peak times.

**[ Data gaps (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1rf6rc6/data_gaps/)**
*  **Summary:** Gap filling should be an event to fix asap, not be an overnight thing. A DE knows programming and can make the necessary tool to use in the workflow process. To fix gaps, quantify the gaps and set up simple freshness and row count checks per location. It's worth checking if their export schedule or batching logic differs from the others.
*  **Emotion:** Predominantly Neutral
*  **Top 3 Points of View:**
    * Addressing data gaps requires assigning responsibility to the business unit owning the source data and implementing clear workflows, potentially including pausing ingestion until gaps are resolved.
    * Proactive measures involve quantifying gap types (e.g., late arrival, partial batches) and setting up automated freshness and row count checks to alert before downstream impact.
    * Data engineers should be able to develop tools and processes, like idempotent loads with automated retry windows, to fix data gaps quickly.

**[ What's the rsync way for postgres? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1rf7uug/whats_the_rsync_way_for_postgres/)**
*  **Summary:** Are you looking to write your own solution? It is possible, but there are many tools that can do this for you. Look into log-based change data capture: it’s the safest way to extract data out of Postgres without actually having to query the tables. logs?
*  **Emotion:** Mixed, generally neutral
*  **Top 3 Points of View:**
    * For PostgreSQL data synchronization, log-based Change Data Capture (CDC) is highly recommended as the safest method for data extraction without querying tables.
    * While direct 'logs' might be a consideration, existing tools and CDC provide more robust and secure solutions for replication.

**[ Did you already faced failed migrations? How it was? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1resrgh/did_you_already_faced_failed_migrations_how_it_was/)**
*  **Summary:** The new way of doing most migration is to create a new cost center for the new migration, sort teams by the amount they pay and move the teams that are paying the most out of the old one. The key to successful migrations is having a end goal with a flexible deadline and key milestones that you can achieve on the way to said deadline. It's also important to scope what is and isn't a part of the migration up front so you waste as little time with scope creep and
*  **Emotion:** Predominantly Positive
*  **Top 3 Points of View:**
    * Successful migrations hinge on flexible deadlines, clear milestones, and upfront technical scoping to prevent scope creep and ensure team focus.
    * Crucial for project success is securing buy-in from all stakeholders – those performing the work, those using the output, and decision-makers.
    * A 'corporate-friendly' migration approach can involve creating new cost centers for the new solution, gradually shifting high-paying teams, and using cost pressure to encourage migration.

**[ Ontology driven data modeling (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1rf8u09/ontology_driven_data_modeling/)**
*  **Summary:** This is on most data expert's radar.

Semantic layer can include ontology information, if you make it to.

The only thing I disagree with is to use ontology to drive data modeling. Ontology doesn't answer all questions that data modeling needs.

I work on this topic on daily basis. Ontology driven data modeling is already what everyone is doing. The point of the field is to take data without context and put it into context to provide business meaning. Even using top tier tooling, I get so many data issues that require repair. LLMs need to learn the ontology from the simplified relationships in a model before they can understand it. An Ontology is a form of a dimensional model. A semantic layer is almost always a text-based model. An LLM can use it to answer questions about a product, a customer, an event, a date, a sale or a campaign. Why would ontology not be on the radar? Nice topic to bring up but odd way of getting people interested. I have built this, but it use the knowledge graph based on which it answers user's question.
Happy to collaborate and solve this very overlooked problem. i’m basically doing this now at work and agree with you. meta models are key. it’ll help humans conceptualize data as well. Saw the title thought I walked in on a Curt Jaimungal podcast. When serving raw data to LLM, rather than giving ERD and column definitions, we give it the ontology. What does that mean in practice? What are examples of code that incorporate ontology, compared to code that doesn't?
*  **Emotion:** Mixed, with some negative sentiment
*  **Top 3 Points of View:**
    * While semantic layers can incorporate ontology, using ontology to *drive* data modeling is contentious, as it may not fully address all practical data modeling requirements.
    * There's skepticism about the additional value of 'ontology' compared to a well-structured semantic layer or dimensional model, especially when LLMs can already consume such models.
    * If LLMs rely heavily on explicit ontology, it suggests limitations in their ability to understand structural models; relying on LLM-derived engineering based solely on ontology could be fragile and prone to data issues.

**[ How good can you use AI in DE? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1reqytb/how_good_can_you_use_ai_in_de/)**
*  **Summary:** It works better for small tasks like creating a SQL with rows from 1 to 1000 or repetitive tasks over something locally defined like a JSON schema object or several files that import the same function. It is not magic but it can help. What do you mean by legacy data engineering projects?. I’ve tried using AI and it works well in several use case. But code review has become increasingly more important. This week we tried ontology driven development and it works, we put some of the experiments in prod as it was better than human quality. Clauude code has created skills for querying BQ, running dbt and validating data pipelines. CC has been having CC write .ipynb files I can import into Hex and then use Hex LLM to do the final bits of creating all the dashboard inputs. Doesn’t do modeling. So at most AI answers questions about the cloud and tools. Works fine when there is something SWE related but basically useless for DE work. I find it incredibly useful when it comes to documentation, creating ER diagrams, investigating data discrepancies (especially if you use an MCP tool to directly query your data), and automate boring/admin type tasks. >... they’re making code better ...

Oh boy
*  **Emotion:** Mixed, leaning positive
*  **Top 3 Points of View:**
    * AI (LLMs) can be highly effective for specific data engineering tasks like code generation (SQL), code explanation, documentation, creating ER diagrams, and automating administrative tasks, but human code review is crucial.
    * Advanced use cases involve integrating LLMs with CLIs to interact with databases (e.g., BQ, dbt) for data exploration, pipeline validation, and creating dashboard inputs.
    * There are varied opinions: some find AI limited for core data modeling, while others observe it can produce high-quality results for experiments and specific problems.
