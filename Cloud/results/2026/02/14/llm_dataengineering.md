---
title: "Data Engineering Subreddit"
date: "2026-02-14"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "AI", "career", "Docker", "ETL"]
---

# Overall Ranking and Top Discussions
1. [I’m planning to move into Data Engineering. With AI growing fast, do you think this career will be heavily affected in the next 5–10 years? Is it still a stable and good path to choose?](https://www.reddit.com/r/dataengineering/comments/1r4j3bw/im_planning_to_move_into_data_engineering_with_ai/) (Score: 78)
    * I’m planning to move into Data Engineering. With AI growing fast, do you think this career will be heavily affected in the next 5–10 years? Is it still a stable and good path to choose?
2. [Is my ETL project at work using Python + SQL well designed? Or am I just being nitpicky](https://www.reddit.com/r/dataengineering/comments/1r49mr4/is_my_etl_project_at_work_using_python_sql_well/) (Score: 26)
    * Is my ETL project at work using Python + SQL well designed? Or am I just being nitpicky
3. [What are the best resources to learn Docker from scratch?](https://www.reddit.com/r/dataengineering/comments/1r4kugz/what_are_the_best_resources_to_learn_docker_from/) (Score: 20)
    * What are the best resources to learn Docker from scratch?
4. [How I created my first Dimensional Data Model from FPL data](https://www.reddit.com/r/dataengineering/comments/1r4sr4u/how_i_created_my_first_dimensional_data_model/) (Score: 5)
    * How I created my first Dimensional Data Model from FPL data
5. [What are the main challenges currently for enterprise-grade KG adoption in AI?](https://www.reddit.com/r/dataengineering/comments/1r4icv5/what_are_the_main_challenges_currently_for/) (Score: 2)
    * What are the main challenges currently for enterprise-grade KG adoption in AI?
6. [Help needed for my code](https://www.reddit.com/r/dataengineering/comments/1r4j8m9/help_needed_for_my_code/) (Score: 2)
    * Help needed for my code
7. [Data engineering vs AI engineering](https://www.reddit.com/r/dataengineering/comments/1r4r12t/data_engineering_vs_ai_engineering/) (Score: 2)
    * Data engineering vs AI engineering
8. [Airflow 3: Development on a Raspberry Pi](https://www.reddit.com/r/dataengineering/comments/1r4sy5d/airflow_3_development_on_a_raspberry_pi/) (Score: 1)
    * Airflow 3: Development on a Raspberry Pi

# Detailed Analysis by Thread
**[I’m planning to move into Data Engineering. With AI growing fast, do you think this career will be heavily affected in the next 5–10 years? Is it still a stable and good path to choose? (Score: 78)](<https://www.reddit.com/r/dataengineering/comments/1r4j3bw/im_planning_to_move_into_data_engineering_with_ai/>)**
*  **Summary:** The thread discusses the impact of AI on the Data Engineering (DE) career path in the next 5-10 years, questioning its stability. There is no question that DE will be affected by AI. However, there are "substitution effects" (job displacement) and "income effects" (overall increase in data processing) which affect DE in different ways. At a recent engineering all-hands, it was noted that AI has a lot of catching up to do in DE, particularly with building queries and working with data. Conversely, some argue that AI has significantly improved in complex DE tasks like Kafka, Spark, and API services, and those who learn to leverage AI tools effectively will be crucial. Learning more about domain knowledge and understanding the business meaning of data is advised. Even if AI foundation models don't improve further, their current capabilities will shift ways of working, but human institutions will take time to adapt. Precise predictions for 2035 are impossible, but DEs should expect to focus on data-engineering-applied-to-AI and remain flexible. DE may evolve into a "jack of all trades" role, requiring knowledge across SRE, SDET, DA, and ML, increasing competition as more people transition into DE. The long-term impact is highly uncertain, with some suggesting a temporary role in feeding AI models, while others believe DE is more insulated than SWE due to AI's limitations with proprietary business domain information. Some even humorously suggest DEs might be "sabotaging" AI's DE capabilities for job security.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.72). There is also a notable presence of negative sentiment.
*  **Top 3 Points of View:**
    * AI will affect Data Engineering, but the role will evolve rather than disappear. Tasks may shift from manual pipeline fixing to monitoring AI agents that manage pipelines, leading to an overall increase in data processing.
    * AI currently struggles with complex Data Engineering tasks like building queries and working with proprietary business data, suggesting Data Engineering is more insulated than Software Engineering.
    * AI is rapidly improving in complex DE tasks (Kafka, Spark, API services), and those who learn to leverage AI tools effectively will thrive, while others might be left behind. DEs will need to become 'jack of all trades' with broader skill sets.

**[Is my ETL project at work using Python + SQL well designed? Or am I just being nitpicky (Score: 26)](<https://www.reddit.com/r/dataengineering/comments/1r49mr4/is_my_etl_project_at_work_using_python_sql_well/>)**
*  **Summary:** The thread discusses the design of an ETL project using Python + SQL, specifically questioning the approach of not using third-party libraries. The post asks for opinions on whether the project is well-designed or if the original poster is "nitpicky." Rewriting things that are already written is considered insane, suggesting that existing, well-maintained packages should be used to avoid maintenance nightmares. If using SQL Server, it's advised to take advantage of SSIS and third-party extensions for time-saving and stability. Not using libraries like SQLAlchemy or Polars for ETL is seen as a bad idea, as they offer better value for delivering analytics and data products. Some argue for detaching SQL from code and not using ORMs for data engineering, suggesting it might be overkill for simple API to DB data pulls. Minimizing dependencies can be sensible for simple, stable solutions, but rebuilding ORM patterns and custom error handling (like avoiding Python's exception model) creates significant long-term maintenance overhead. However, others suggest that low-level Python work can offer excellent learning, and that sometimes starting with the standard library is best depending on the use case, acknowledging that some libraries like SQLAlchemy have limitations. Company regulations on third-party libraries might also be a factor.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.54). There is also a notable presence of positive sentiment.
*  **Top 3 Points of View:**
    * Rewriting existing libraries or frameworks for ETL is inefficient and creates maintenance nightmares; using well-maintained third-party packages like SQLAlchemy or Polars is generally preferred.
    * Minimizing dependencies can be beneficial for simple, stable projects that require minimal maintenance, but building custom solutions for complex functionalities like ORM patterns, connection pooling, or error handling (e.g., avoiding Python's exception model) creates significant long-term maintenance costs.
    * The decision to use or avoid third-party libraries should be based on company regulations, the project's maintenance horizon, and whether specific constraints justify the overhead of custom solutions.

**[What are the best resources to learn Docker from scratch? (Score: 20)](<https://www.reddit.com/r/dataengineering/comments/1r4kugz/what_are_the_best_resources_to_learn_docker_from/>)**
*  **Summary:** The thread seeks the best resources for learning Docker from scratch for Data Engineers. Users recommend starting with a high-level overview of the problems Docker solves, then immediately applying it by running Airflow locally using `docker compose`. A community-submitted learning resources list is also provided. Practical application is highly emphasized, such as creating DAGs that run Docker images with DockerOperator, and understanding how production deployments utilize services like ECS or Cloud Run. A specific YouTube course by Javascript Mastery is suggested for foundational knowledge. Some argue that learning Docker "from scratch" beyond practical application for tools like Airflow or Airbyte is pointless. Structured learning should cover installation, navigating Docker Hub, essential CLI commands (`docker build`, `docker run`, `docker pull`, `docker exec`, `docker container cp`), creating Dockerfiles (e.g., `ADD` vs. `COPY`, `CMD` vs. `ENTRYPOINT`), and understanding Docker networking and volumes. For more advanced learning, transitioning to Kubernetes after mastering Docker basics is recommended, especially for production-grade Airflow deployments.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.76). There is also a notable presence of positive sentiment.
*  **Top 3 Points of View:**
    * Hands-on learning is key: start by understanding the problems Docker solves, then immediately apply it by running tools like Airflow locally using `docker compose`.
    * Structured learning should cover Docker basics: installation, navigating Docker Hub, essential CLI commands (`build`, `run`, `pull`), creating Dockerfiles (ADD vs. COPY, CMD vs. ENTRYPOINT), and understanding Docker networking and volumes.
    * For Data Engineering specific learning, focus on practical applications like running Airflow with Docker, using DockerOperator in DAGs, and understanding how Docker containers are deployed in production environments (e.g., ECS, Cloud Run, Kubernetes).

**[How I created my first Dimensional Data Model from FPL data (Score: 5)](<https://www.reddit.com/r/dataengineering/comments/1r4sr4u/how_i_created_my_first_dimensional_data_model/>)**
*  **Summary:** This post is about creating a first dimensional data model using FPL (Fantasy Premier League) data. The discussion includes community-submitted project showcases and constructive feedback regarding the data model design, such as suggesting dropping redundant team H/A scores from the fact table if that information is already in the fixtures dimension, and inquiring about the source of player's own team information.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.76).
*  **Top 3 Points of View:**
    * The project showcases a successful first attempt at creating a dimensional data model using FPL data.
    * Users provided constructive feedback and suggestions for optimization, such as dropping redundant data from the fact table if it exists in a dimension, and clarifying data sources (e.g., 'home team id').

**[What are the main challenges currently for enterprise-grade KG adoption in AI? (Score: 2)](<https://www.reddit.com/r/dataengineering/comments/1r4icv5/what_are_the_main_challenges_currently_for/>)**
*  **Summary:** This thread inquires about the main challenges for enterprise-grade Knowledge Graph (KG) adoption in AI. Nobody cared about Knowledge Graph before, and with modern LLM, they couldn't care less now: just feed Gemini/ChatGPT/etc the questions and it will give them a probabilistic correct answer.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.88).
*  **Top 3 Points of View:**
    * Knowledge Graphs (KGs) are seeing reduced interest for enterprise AI adoption because modern Large Language Models (LLMs) can directly provide probabilistic answers, diminishing the perceived need for complex KG structures.

**[Help needed for my code (Score: 2)](<https://www.reddit.com/r/dataengineering/comments/1r4j8m9/help_needed_for_my_code/>)**
*  **Summary:** The post is a request for help with code. A practical solution involves using Azure Functions to call a REST API and invoking it from Synapse for data processing. Community learning resources are also provided.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.89).
*  **Top 3 Points of View:**
    * A practical solution involves using Azure Functions to call a REST API and invoking it from Synapse for data processing.

**[Data engineering vs AI engineering (Score: 2)](<https://www.reddit.com/r/dataengineering/comments/1r4r12t/data_engineering_vs_ai_engineering/>)**
*  **Summary:** This thread discusses the distinctions and potential risks between Data Engineering and AI Engineering roles. Community learning resources are available. If you are an AI engineer and you are not touching your own company's in-house model or doing actual machine learning work, you are in danger. The "AI engineer" role focusing on workflows and agents for a system is a rapidly evolving space externally, which often outpaces enterprise implementation, quickly rendering internal work outdated. It is advisable to focus on a Data Engineer or developer role that one enjoys and use AI tools to enhance that role, rather than pursuing a role solely defined by promoting specific AI tools within a company.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.79).
*  **Top 3 Points of View:**
    * Focusing solely on 'AI engineering' by promoting generic AI tools within a company, without doing actual in-house model development or machine learning work, is risky due to the rapid advancement of external AI tools making internal efforts quickly outdated.
    * It is safer to pursue a stable Data Engineer or Developer role and leverage AI tools to enhance that role, rather than specializing in a role defined purely by the application of rapidly evolving generic AI agents.

**[Airflow 3: Development on a Raspberry Pi (Score: 1)](<https://www.reddit.com/r/dataengineering/comments/1r4sy5d/airflow_3_development_on_a_raspberry_pi/>)**
*  **Summary:** The post focuses on developing Airflow 3 on a Raspberry Pi. CI/CD is just added complexity for such a small scale. For small-scale development, it's suggested to mount a local development folder containing DAGs directly into the Docker container, making updates automatically visible to Airflow. The Docker deployment for Airflow is very much NOT production-grade.
*  **Emotion:** The overall emotional tone is primarily Neutral (average score: 0.82).
*  **Top 3 Points of View:**
    * For small-scale Airflow development on a Raspberry Pi, CI/CD adds unnecessary complexity; a simpler approach is to mount a local development folder containing DAGs directly into the Docker container.
    * The Docker deployment for Airflow is generally not suitable for production-grade environments, implying it's primarily for local development and testing.
