---
title: "Data Engineering Subreddit"
date: "2025-06-20"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "tools", "career"]
---

# Overall Ranking and Top Discussions
1.  [The Data Engineering Toolkit](https://toolkit.ssp.sh/) (Score: 68)
    *   A user shared a data engineering toolkit which was well received by the community
2.  [What's the fastest-growing data engineering platform in the US right now?](https://www.reddit.com/r/dataengineering/comments/1lfz2f4/whats_the_fastestgrowing_data_engineering/) (Score: 42)
    *   Users discussed the fastest-growing data engineering platforms, with mentions of Snowflake, Databricks, dbt, and Fivetran
3.  [Which industries/companies tend to use DE for more than just feeding dashboards?](https://www.reddit.com/r/dataengineering/comments/1lg6b82/which_industriescompanies_tend_to_use_de_for_more/) (Score: 21)
    *   Users discussed which industries utilize data engineering for more than just feeding dashboards, including trading, gaming, and cloud application vendors.
4.  [Does anyone still think "Schema on Read" is a good idea?](https://www.reddit.com/r/dataengineering/comments/1lg6d3x/does_anyone_still_think_schema_on_read_is_a_good/) (Score: 15)
    *   Users debated the merits of "Schema on Read," with some arguing it's a necessary evil for flexibility and others viewing it as laziness
5.  [Any DE consultants here find it impossible to convince clients to switch to "modern" tooling?](https://www.reddit.com/r/dataengineering/comments/1lg74vv/any_de_consultants_here_find_it_impossible_to/) (Score: 13)
    *   Data engineering consultants discussed the challenges of convincing clients to adopt modern tooling, citing reasons like regulatory requirements, familiarity, and a focus on business value over technology.
6.  [SSAS cube too large to process in one go — separate transactions in SSIS won’t save](https://www.reddit.com/r/dataengineering/comments/1lfysr0/ssas_cube_too_large_to_process_in_one_go_separate/) (Score: 12)
    *   A user sought help with processing a large SSAS cube, and another suggested using XMLA scripting within a For Each Loop container in SSIS
7.  [Best practises for strongly typed data checks in a dbt medallion architecture](https://www.reddit.com/r/dataengineering/comments/1lg2z0l/best_practises_for_strongly_typed_data_checks_in/) (Score: 9)
    *   A user asked about best practices for strongly typed data checks in a dbt medallion architecture.
8.  [Converting from relational model to star schema](https://www.reddit.com/r/dataengineering/comments/1lg6v0f/converting_from_relational_model_to_star_schema/) (Score: 5)
    *   Users discussed converting from a relational model to a star schema, emphasizing the importance of starting with the analytical queries the schema needs to support and suggesting a reference to Kimball's Data Warehouse Toolkit.
9.  [Analysts providing post-hoc adjustments to aggregated metrics — now feeding back into the DAG. Feels wrong. Is this ever legit?](https://www.reddit.com/r/dataengineering/comments/1lg6kub/analysts_providing_posthoc_adjustments_to/) (Score: 3)
    *   Users discussed the issue of analysts making post-hoc adjustments to aggregated metrics and feeding them back into the DAG, with suggestions for tracking adjustments separately and addressing the root cause of the need for adjustments.
10. [How do I manage the size of my VM](https://www.reddit.com/gallery/1lg3dzl) (Score: 2)
    *   A user asked how to manage the size of their VM. The user was hitting the quota limit on the Azure subscription itself.
11. [Proper production practises in Databricks?](https://www.reddit.com/r/dataengineering/comments/1lfywaz/proper_production_practises_in_databricks/) (Score: 2)
    *   Users discussed best practices for productionizing code in Databricks, including using Databricks jobs, integrating with Git repositories, and managing different environments (dev, UAT, prod).
12. [Should I learn Flask, HTML & CSS to build a frontend to my project, or should I just use Streamlit?](https://www.reddit.com/r/dataengineering/comments/1lg6dsl/should_i_learn_flask_html_css_to_build_a_frontend/) (Score: 2)
    *   Users discussed whether to learn Flask, HTML, and CSS or use Streamlit for building a frontend, generally recommending Streamlit or dashboard visualization tools like Tableau or Power BI for data engineering projects.
13. [What do Data Engineers in FinOps do?](https://www.reddit.com/r/dataengineering/comments/1lg7n3v/what_do_data_engineers_in_finops_do/) (Score: 2)
    *   Users discussed the role of Data Engineers in FinOps, noting that it involves data processing related to sales and expenses, particularly for profit and loss analysis.
14. [Advice on spreadhseet based CDC](https://www.reddit.com/r/dataengineering/comments/1lgae7z/advice_on_spreadhseet_based_cdc/) (Score: 2)
    *   Users provided advice on Change Data Capture (CDC) for spreadsheet-based data, suggesting comparing spreadsheets to calculate diffs or copying data into a proper database for easier diff calculations.
15. [Rejected for no python](https://www.reddit.com/r/dataengineering/comments/1lgdi0i/rejected_for_no_python/) (Score: 2)
    *   A user reported being rejected for a data engineering job due to a lack of Python skills, and other users offered encouragement and learning resources.
16. [Made a free documentation tool for enhancing conceptual diagramming](https://www.reddit.com/r/dataengineering/comments/1lg2bec/made_a_free_documentation_tool_for_enhancing/) (Score: 1)
    *   A user shared a free documentation tool for conceptual diagramming, and others suggested using Draw.io as an alternative.

# Detailed Analysis by Thread
**[The Data Engineering Toolkit (Score: 68)](https://toolkit.ssp.sh/)**
*   **Summary:**  A user shared a data engineering toolkit which was well received by the community
*   **Emotion:** The emotional tone of the thread is overwhelmingly positive, with users expressing excitement and gratitude.
*   **Top 3 Points of View:**
    *   The toolkit is awesome and exactly what some users were looking for.
    *   It's a great single pane of glass for data engineering resources.
    *   It's a helpful source of aggregated information, especially for data modeling.

**[What's the fastest-growing data engineering platform in the US right now? (Score: 42)](https://www.reddit.com/r/dataengineering/comments/1lfz2f4/whats_the_fastestgrowing_data_engineering/)**
*   **Summary:** Users discussed the fastest-growing data engineering platforms, with mentions of Snowflake, Databricks, dbt, and Fivetran. The discussion also touches on the Modern Data Stack and the rETL space.
*   **Emotion:** The overall emotional tone is neutral and positive. Users are genuinely interested in understanding trends and sharing their perspectives.
*   **Top 3 Points of View:**
    *   Snowflake's growth may be slowing down.
    *   Databricks, dbt, and Fivetran are experiencing rapid growth within the Modern Data Stack.
    *   There is a need for more competition in the rETL space due to current solutions being overpriced.

**[Which industries/companies tend to use DE for more than just feeding dashboards? (Score: 21)](https://www.reddit.com/r/dataengineering/comments/1lg6b82/which_industriescompanies_tend_to_use_de_for_more/)**
*   **Summary:** Users discussed which industries utilize data engineering for more than just feeding dashboards, including trading, gaming, and cloud application vendors.
*   **Emotion:** The emotional tone of this thread is mostly neutral, with a hint of positivity. Users are sharing information and experiences in a matter-of-fact way.
*   **Top 3 Points of View:**
    *   Data engineering is used for creating data products that fuel data science models and analytics.
    *   Industries like trading and gaming use data engineering for ML, statistical research, and driving sales.
    *   Cloud application vendors use data engineering to provide clients with their own data for analysis.

**[Does anyone still think "Schema on Read" is a good idea? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1lg6d3x/does_anyone_still_think_schema_on_read_is_a_good/)**
*   **Summary:** Users debated the merits of "Schema on Read," with some arguing it's a necessary evil for flexibility and others viewing it as laziness.
*   **Emotion:** The overall tone is neutral, but tinged with negativity from some users who dislike the practice.
*   **Top 3 Points of View:**
    *   "Schema on Read" is useful for ingesting data without immediate analysis, acting as a landing zone before transforming to "Schema on Write."
    *   "Schema on Read" puts the burden on data consumers.
    *   "Schema on Read" is an excuse for lazy data producers.

**[Any DE consultants here find it impossible to convince clients to switch to "modern" tooling? (Score: 13)](https://www.reddit.com/r/dataengineering/comments/1lg74vv/any_de_consultants_here_find_it_impossible_to/)**
*   **Summary:** Data engineering consultants discussed the challenges of convincing clients to adopt modern tooling, citing reasons like regulatory requirements, familiarity, and a focus on business value over technology.
*   **Emotion:** The thread has a generally negative emotional tone, reflecting frustration with the difficulty of convincing clients.
*   **Top 3 Points of View:**
    *   Clients in regulated industries prioritize accountability and support over open-source solutions.
    *   Enterprises are more interested in delivering value than using the latest technology.
    *   Sometimes, clients prefer familiar tools and approaches that solve their specific problems, even if they aren't "modern."

**[SSAS cube too large to process in one go — separate transactions in SSIS won’t save (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1lfysr0/ssas_cube_too_large_to_process_in_one_go_separate/)**
*   **Summary:** A user sought help with processing a large SSAS cube, and another suggested using XMLA scripting within a For Each Loop container in SSIS
*   **Emotion:** The emotional tone of this thread is neutral and helpful.
*   **Top 3 Points of View:**
    *   Using XMLA scripting within a For Each Loop container can solve the user's problem.
    *   Recommend u/Nekobul help somebody use the best ETL platform on the market

**[Best practises for strongly typed data checks in a dbt medallion architecture (Score: 9)](https://www.reddit.com/r/dataengineering/comments/1lg2z0l/best_practises_for_strongly_typed_data_checks_in/)**
*   **Summary:** A user asked about best practices for strongly typed data checks in a dbt medallion architecture.
*   **Emotion:** The emotional tone of this thread is neutral and inquisitive.
*   **Top 3 Points of View:**
    *   The catalog being loaded as a seed file.
    *   The best approach would be to specify debt contracts with the data types in question.

**[Converting from relational model to star schema (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1lg6v0f/converting_from_relational_model_to_star_schema/)**
*   **Summary:** Users discussed converting from a relational model to a star schema, emphasizing the importance of starting with the analytical queries the schema needs to support and suggesting a reference to Kimball's Data Warehouse Toolkit.
*   **Emotion:** The tone is helpful and informative.
*   **Top 3 Points of View:**
    *   Start with the questions users want to answer.
    *   The form of the database should normally follow the functioning of the company.
    *   List the queries you want to be able to answer and ref to Kimball's book.

**[Analysts providing post-hoc adjustments to aggregated metrics — now feeding back into the DAG. Feels wrong. Is this ever legit? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1lg6kub/analysts_providing_posthoc_adjustments_to/)**
*   **Summary:** Users discussed the issue of analysts making post-hoc adjustments to aggregated metrics and feeding them back into the DAG, with suggestions for tracking adjustments separately and addressing the root cause of the need for adjustments.
*   **Emotion:** The emotional tone of this thread is somewhat negative and solution-oriented.
*   **Top 3 Points of View:**
    *   It's not ideal to let analysts adjust the metrics.
    *   Create an "adjustment" metric that defaults to zero or null.
    *   Bot identification should really happen upstream at an event or session level.

**[How do I manage the size of my VM (Score: 2)](https://www.reddit.com/gallery/1lg3dzl)**
*   **Summary:** A user asked how to manage the size of their VM. The user was hitting the quota limit on the Azure subscription itself.
*   **Emotion:** The emotional tone of this thread is neutral.
*   **Top 3 Points of View:**
    *   Edit the compute that is problematic, Go to performance and node type, Select another compute type.
    *   If you are sharing your azure tenant, other users may have deployed the same VM Size for their project so you won’t have enough for your databricks compute.
    *   Either you can’t access that VM size or there are capacity issues and that size can’t be allocated to you.

**[Proper production practises in Databricks? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lfywaz/proper_production_practises_in_databricks/)**
*   **Summary:** Users discussed best practices for productionizing code in Databricks, including using Databricks jobs, integrating with Git repositories, and managing different environments (dev, UAT, prod).
*   **Emotion:** The emotional tone of this thread is neutral and informative.
*   **Top 3 Points of View:**
    *   Scripts are important in production for reasons relating to automated testing, CI/CD, maintainability etc.
    *   Once the code works in a notebook, you can create a Databricks job based on the code.
    *   The plan is to use databricks asset bundles to handle the environment and not using notebooks for anything except exploratory type work.

**[Should I learn Flask, HTML & CSS to build a frontend to my project, or should I just use Streamlit? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lg6dsl/should_i_learn_flask_html_css_to_build_a_frontend/)**
*   **Summary:** Users discussed whether to learn Flask, HTML, and CSS or use Streamlit for building a frontend, generally recommending Streamlit or dashboard visualization tools like Tableau or Power BI for data engineering projects.
*   **Emotion:** The thread's emotional tone is mostly neutral, providing practical advice.
*   **Top 3 Points of View:**
    *   Just focus on what you have to do.
    *   If you're sure you want to do a data role then simply use streamlit.
    *   Streamlit for prototyping, dash for production.

**[What do Data Engineers in FinOps do? (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lg7n3v/what_do_data_engineers_in_finops_do/)**
*   **Summary:** Most of the data processing is related to sales and expenses. Finance collegues want everything in excel.
*   **Emotion:** The emotional tone of this thread is neutral and informative.
*   **Top 3 Points of View:**
    *   Most of the data processing is related to sales and expenses.
    *   Finance colleagues want everything in excel.
    *   It gets hectic during monthly or quarterly bill runs.

**[Advice on spreadhseet based CDC (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lgae7z/advice_on_spreadhseet_based_cdc/)**
*   **Summary:** The thread's emotional tone is mostly neutral and advice driven.
*   **Emotion:** Users provided advice on Change Data Capture (CDC) for spreadsheet-based data, suggesting comparing spreadsheets to calculate diffs or copying data into a proper database for easier diff calculations.
*   **Top 3 Points of View:**
    *   Turn it into a csv file and append to it.
    *   Write some Java to compare them and calculate the "diff" yourself.
    *   You could start tracking/copying the data in a proper DB to be able to calculate the weekly diff more easily.

**[Rejected for no python (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1lgdi0i/rejected_for_no_python/)**
*   **Summary:** A user reported being rejected for a data engineering job due to a lack of Python skills, and other users offered encouragement and learning resources.
*   **Emotion:** The thread's emotional tone is mostly neutral and advice driven.
*   **Top 3 Points of View:**
    *   Try to recreate what you do using tools and SQL in python
    *   Find a list of community-submitted learning resources
    *   Study by solving some interview questions and learning a lil bit of theory.

**[Made a free documentation tool for enhancing conceptual diagramming (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1lg2bec/made_a_free_documentation_tool_for_enhancing/)**
*   **Summary:** A user shared a free documentation tool for conceptual diagramming, and others suggested using Draw.io as an alternative.
*   **Emotion:** The thread's emotional tone is mostly neutral and informative.
*   **Top 3 Points of View:**
    *   Draw.io doesn’t suffice for this?
    *   Here’s just the tool if you want to try it https://www.plsfix-thx.com/
    *   You can find our open-source project showcase here.
