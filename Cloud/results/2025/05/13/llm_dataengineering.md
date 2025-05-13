---
title: "Data Engineering Subreddit"
date: "2025-05-13"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Do you rather hate or love using Python for writing your own ETL jobs?](https://www.reddit.com/r/dataengineering/comments/1klpzaf/do_you_rather_hate_or_love_using_python_for/) (Score: 22)
    *   This thread discusses the pros and cons of using Python for ETL jobs, with various users sharing their experiences and preferences.
2.  [Building a RAG-based Q&A tool for legal documents: Architecture and insights](https://www.reddit.com/r/dataengineering/comments/1kloo6d/building_a_ragbased_qa_tool_for_legal_documents/) (Score: 12)
    *   This thread features a project showcase of a RAG-based Q&A tool for legal documents.
3.  [When is a good time to use an EC2 Instance instead of Glue or Lambdas?](https://www.reddit.com/r/dataengineering/comments/1klpn5v/when_is_a_good_time_to_use_an_ec2_instance/) (Score: 10)
    *   This thread discusses when to use EC2 instances versus Glue or Lambdas, with a focus on control, custom code, and long-running jobs.
4.  [Data engineering in a quant/trading shop](https://www.reddit.com/r/dataengineering/comments/1klmv6x/data_engineering_in_a_quanttrading_shop/) (Score: 8)
    *   This thread discusses the data engineering role in quant/trading shops.
5.  [Transition From Data Engineering into Research](https://www.reddit.com/r/dataengineering/comments/1klkk2m/transition_from_data_engineering_into_research/) (Score: 5)
    *   This thread is about transitioning from data engineering to research.
6.  [Amazon Redshift vs. Athena: A Data Engineering Perspective (Case Study)](https://www.reddit.com/r/dataengineering/comments/1klrlgo/amazon_redshift_vs_athena_a_data_engineering/) (Score: 5)
    *   This thread compares Amazon Redshift and Athena from a data engineering perspective, featuring a case study.
7.  [User stories in Azure DevOps for standard Data Engineering workflows?](https://www.reddit.com/r/dataengineering/comments/1klqmn0/user_stories_in_azure_devops_for_standard_data/) (Score: 3)
    *   This thread asks about user stories in Azure DevOps for standard Data Engineering workflows.
8.  [Elephant in the room - Jira for DE teams](https://www.reddit.com/r/dataengineering/comments/1klsa36/elephant_in_the_room_jira_for_de_teams/) (Score: 3)
    *   This thread discusses the use of Jira for Data Engineering teams, with suggestions for improving workflows and task management.
9.  [Streaming data framework](https://www.reddit.com/r/dataengineering/comments/1klo32v/streaming_data_framework/) (Score: 2)
    *   This thread discusses different streaming data frameworks.
10. [Postgres using Keycloak Auth Credentials](https://www.reddit.com/r/dataengineering/comments/1klqxkx/postgres_using_keycloak_auth_credentials/) (Score: 2)
    *   This thread discusses how to use Keycloak Auth Credentials with Postgres.
11. [We’re the co-founders of WarpStream. Ask Us Anything.](https://www.reddit.com/r/apachekafka/comments/1kijwdz/were_the_cofounders_of_warpstream_ask_us_anything/) (Score: 1)
    *   This thread is an "Ask Us Anything" session with the co-founders of WarpStream.
12. [Need help](https://www.reddit.com/r/dataengineering/comments/1kltf4s/need_help/) (Score: 1)
    *   This thread requests help and is answered by a bot pointing to learning resources.
13. [I need help creating a data flow diagram](https://i.redd.it/1kiw3gxcal0f1.jpeg) (Score: 0)
    *   This thread asks for help creating a data flow diagram, with various suggestions and some critical comments.
14. [i need your help pleaaase (SQL, data engineering)](https://www.reddit.com/r/dataengineering/comments/1klncu5/i_need_your_help_pleaaase_sql_data_engineering/) (Score: 0)
    *   This thread asks for help with a SQL data engineering problem related to comparing data in two different servers.
15. [Leveling up from Senior to Staff. Learn another language?](https://www.reddit.com/r/dataengineering/comments/1klvh5o/leveling_up_from_senior_to_staff_learn_another/) (Score: 0)
    *   This thread discusses leveling up from Senior to Staff.

# Detailed Analysis by Thread
**[[D] Do you rather hate or love using Python for writing your own ETL jobs? (Score: 22)](https://www.reddit.com/r/dataengineering/comments/1klpzaf/do_you_rather_hate_or_love_using_python_for/)**
*  **Summary:** This thread explores opinions on using Python for ETL jobs. Users share both positive and negative experiences, discussing its versatility, ease of prototyping, and ecosystem maturity, as well as drawbacks like debugging challenges and the preference for other languages like Scala or SQL in certain contexts.
*  **Emotion:** The emotional tone is largely Positive, but with a mix of Neutral and Negative sentiments as users express both love and hate for Python in ETL.
*  **Top 3 Points of View:**
    *   Python is loved for its granularity, portability, and rapid prototyping capabilities.
    *   Python is disliked for reasons outlined in the original post and debugging challenges. Some prefer other languages like Scala for ETL.
    *   Python is popular due to its mature ecosystem and ease of use, particularly for data analysts/scientists, but this doesn't necessarily equate to universal love among data engineers.

**[Building a RAG-based Q&A tool for legal documents: Architecture and insights (Score: 12)](https://www.reddit.com/r/dataengineering/comments/1kloo6d/building_a_ragbased_qa_tool_for_legal_documents/)**
*  **Summary:** This thread showcases a RAG-based Q&A tool for legal documents and includes discussions about retrieval methods, chunking, and how to gauge the quality of the answers. It includes a link to an open-source project showcase and a submission form.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The project is perceived as "really cool" and well-suited for dense, hard-to-read legal documents.
    *   Custom tools are a good way to get exactly what you need.
    *   The thread includes a bot response with links to resources and project submissions.

**[When is a good time to use an EC2 Instance instead of Glue or Lambdas? (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1klpn5v/when_is_a_good_time_to_use_an_ec2_instance/)**
*  **Summary:** This thread discusses the appropriate use cases for EC2 instances compared to AWS Glue or Lambdas, focusing on factors like control, custom code, job duration, and resource requirements.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   EC2 is preferred when more control is needed over the environment, when running custom code/tools that don’t work well with Glue/Lambda, or for long-running jobs exceeding Lambda's timeout.
    *   Lambdas are versatile and cheap but can become expensive with high memory/CPU requirements or jobs exceeding 15 minutes.
    *   Fargate or ECS are often preferred over EC2 directly for ETL, with Kubernetes infrastructure being the most optimal choice for companies already using it.

**[Data engineering in a quant/trading shop (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1klmv6x/data_engineering_in_a_quanttrading_shop/)**
*  **Summary:** The thread discusses the role of data engineers in quant/trading shops, interview processes, and compensation.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   New grads are often put through a SWE interview loop.
    *   Experienced candidates may interview directly for DE roles.
    *   Compensation may be better outside of select firms.

**[Transition From Data Engineering into Research (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1klkk2m/transition_from_data_engineering_into_research/)**
*  **Summary:** The thread discusses transitioning from Data Engineering into Research and includes a link to a community guide on transitioning into data engineering.
*  **Emotion:** The overall emotional tone is Neutral to Negative.
*  **Top 3 Points of View:**
    *   A bot links to a guide on transitioning *into* Data Engineering.
    *   The usefulness of a DE background depends on the research area.

**[Amazon Redshift vs. Athena: A Data Engineering Perspective (Case Study) (Score: 5)](https://www.reddit.com/r/dataengineering/comments/1klrlgo/amazon_redshift_vs_athena_a_data_engineering/)**
*  **Summary:** The thread compares Amazon Redshift and Athena from a data engineering perspective. It includes a case study, and explains the use of both tools.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    *   Athena is used for ad hoc analysis, modeling, ELT, and data audits.
    *   Redshift serverless is the serving layer for customer-facing metrics and internal BI.

**[User stories in Azure DevOps for standard Data Engineering workflows? (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1klqmn0/user_stories_in_azure_devops_for_standard_data/)**
*  **Summary:** This thread explores the organization of user stories in Azure DevOps for data engineering workflows, focusing on clear tracking and efficiency.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Break down work into separate user stories for each phase, improving clarity and tracking.
    *   Combine ingestion and bronze work if tightly linked to save effort.
    *   Utilize basic story templates with checklists for each layer to maintain detail without overwhelming tickets.

**[Elephant in the room - Jira for DE teams (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1klsa36/elephant_in_the_room_jira_for_de_teams/)**
*  **Summary:** This thread discusses the use of Jira for DE teams, with suggestions for improving workflows and task management.
*  **Emotion:** The overall emotional tone is Positive and Neutral.
*  **Top 3 Points of View:**
    *   Simplify Jira by establishing a clear workflow with only the needed statuses.
    *   Focus on clear task descriptions.
    *   Using Jira is not worth it.

**[Streaming data framework (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1klo32v/streaming_data_framework/)**
*  **Summary:** This thread discusses different streaming data frameworks.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    *   Flink is an ideal use case.
    *   Check out Bytewax.

**[Postgres using Keycloak Auth Credentials (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1klqxkx/postgres_using_keycloak_auth_credentials/)**
*  **Summary:** This thread explores the integration of Keycloak authentication with Postgres, discussing the limitations of native support and alternative solutions.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    *   Postgres doesn’t natively support OIDC, so direct Keycloak integration isn’t possible out of the box.
    *   Alternatives include using LDAP as a bridge or a proxy like pgbouncer-oidc or Cloud SQL Auth Proxy.

**[We’re the co-founders of WarpStream. Ask Us Anything. (Score: 1)](https://www.reddit.com/r/apachekafka/comments/1kijwdz/were_the_cofounders_of_warpstream_ask_us_anything/)**
*  **Summary:** This thread is an "Ask Us Anything" session with the co-founders of WarpStream.
*  **Emotion:** The overall emotional tone is Positive and Neutral.
*  **Top 3 Points of View:**
    *   Users are curious if it is open source.
    *   Users are curious how it compares to RedPanda.
    *   Users are wishing the co-founders good luck.

**[Need help (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1kltf4s/need_help/)**
*  **Summary:** This thread requests help and is answered by a bot pointing to learning resources.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    *   A bot provides a link to learning resources.

**[I need help creating a data flow diagram (Score: 0)](https://i.redd.it/1kiw3gxcal0f1.jpeg)**
*  **Summary:** This thread asks for help creating a data flow diagram, with suggestions and critical comments.
*  **Emotion:** The overall emotional tone is mixed, with some Positive, Neutral, and Negative sentiments.
*  **Top 3 Points of View:**
    *   Use GPT to give you mermaid code for your diagram.
    *   This looks like a user diagram, are you sure you’re looking for a data diagram and not a user diagram?
    *   Users should ask their TAs or Profs for advice and help.

**[i need your help pleaaase (SQL, data engineering) (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1klncu5/i_need_your_help_pleaaase_sql_data_engineering/)**
*  **Summary:** This thread asks for help with a SQL data engineering problem related to comparing data in two different servers.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   Use Linked Server to run queries that encompass more than one database.
    *   Use Power BI to link datasets and create visualizations.
    *   If you are not allowed to link the databases, you have to copy data from DB A to DB B or copy it to a third place like MS Excel or Access.

**[Leveling up from Senior to Staff. Learn another language? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1klvh5o/leveling_up_from_senior_to_staff_learn_another/)**
*  **Summary:** This thread discusses leveling up from Senior to Staff and learning another language.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   The poster should learn Hindi or Mandarin.
    *   The poster should be learning Communication and Emotional Intelligence at Staff level.
    *   The poster is very far from any kind of staff-level position.
