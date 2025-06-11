---
title: "Data Engineering Subreddit"
date: "2025-04-16"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [Data Engineering: Now with 30% More ***](https://luminousmen.com/post/data-engineering-now-with-30-more-bullshit) (Score: 204)
    *   People are praising an article that cuts through the BS in data engineering and offers a clear and concise vision.
2.  [Whats the simplest/fastest way to bulk import 100s of CSVs each into their OWN table in SSMS? (Using SSIS, command prompt, or possibly python)](https://www.reddit.com/r/dataengineering/comments/1k0mgmh/whats_the_simplestfastest_way_to_bulk_import_100s/) (Score: 6)
    *   Users are discussing various methods for importing multiple CSV files into separate tables in SSMS, including SSMS Bulk Insert, PowerShell, Azure ADF, and Python.
3.  [Is Kafka a viable way to store lots of streaming data?](https://www.reddit.com/r/dataengineering/comments/1k0qy7u/is_kafka_a_viable_way_to_store_lots_of_streaming/) (Score: 6)
    *   The discussion revolves around whether Kafka is suitable for long-term storage of streaming data, with most arguing it's not its intended purpose and suggesting alternatives.
4.  [Switching batch jobs to streaming](https://www.reddit.com/r/dataengineering/comments/1k0t6ua/switching_batch_jobs_to_streaming/) (Score: 4)
    *   Users are discussing the feasibility of refactoring transformation queries to adapt to both business logic and the constraints of streaming environments, suggesting it as the most viable path forward.
5.  [Issue with Data Model with Querying Dynamics 365 via ADF](https://www.reddit.com/r/dataengineering/comments/1k0b99g/issue_with_data_model_with_querying_dynamics_365/) (Score: 3)
    *   A user is directed to the PowerApps subreddit for assistance with a data model issue involving querying Dynamics 365 via ADF.
6.  [Refactoring a script taking 17hours to run wit 0 Documentation](https://www.reddit.com/r/dataengineering/comments/1k0lgfr/refactoring_a_script_taking_17hours_to_run_wit_0/) (Score: 3)
    *   Users share strategies for refactoring a long-running script without documentation, including understanding the process at a high level, breaking it down into smaller pieces, writing tests, and creating data lineage diagrams.
7.  [How Universities Are Using Data Warehousing to Meet Compliance and Funding Demands](https://www.reddit.com/r/dataengineering/comments/1k0ogu0/how_universities_are_using_data_warehousing_to/) (Score: 3)
    *   A bot provides a link to community-submitted learning resources related to data warehousing.
8.  [Criticism at work because my lack of understanding business requirements is coinciding with quick turnaround times](https://www.reddit.com/r/dataengineering/comments/1k0rxxi/criticism_at_work_because_my_lack_of/) (Score: 3)
    *   The discussion centers around the importance of understanding business requirements and the role of stakeholders in providing necessary context.
9.  [migrating from No-Code middleware platform to another more fundamental tech stack](https://www.reddit.com/r/dataengineering/comments/1k0n177/migrating_from_nocode_middleware_platform_to/) (Score: 2)
    *   A user asks for the name of the current no-code platform.
10. [Very high level Data Services tool](https://www.reddit.com/r/dataengineering/comments/1k0sg0i/very_high_level_data_services_tool/) (Score: 2)
    *   A bot provides links to an open-source project showcase and a submission form for featuring projects.
11. [GCP Professional Data Engineer](https://www.reddit.com/r/dataengineering/comments/1k0kjbu/gcp_professional_data_engineer/) (Score: 1)
    *   Users share resources and strategies for preparing for the GCP Professional Data Engineer certification, including practice tests and study guides.
12. [AI for data anomaly detection?](https://www.reddit.com/r/dataengineering/comments/1k0miny/ai_for_data_anomaly_detection/) (Score: 1)
    *   A user asks about the type of anomaly detection being sought and whether a plug-and-play option is desired.
13. [Vibe Coding in Data Engineering — Microsoft Fabric Test](https://medium.com/@mariusz_kujawski/vibe-coding-in-data-engineering-microsoft-fabric-test-76e8d32db74f) (Score: 0)
    *   Users debate the value of using AI for coding, with some viewing it as a way to avoid learning to code and others considering it a time-saving tool.
14. [Data Mapping](https://www.reddit.com/r/dataengineering/comments/1k0jkfv/data_mapping/) (Score: 0)
    *   The discussion revolves around using AI for data mapping and automatically granting permissions based on employee roles and data requirements.

# Detailed Analysis by Thread
**[Data Engineering: Now with 30% More *** (Score: 204)](https://luminousmen.com/post/data-engineering-now-with-30-more-bullshit)**
*   **Summary:**  The thread is filled with positive feedback for an article on data engineering that is perceived as clear, concise, and free of hype. Many users express appreciation for its directness and relevance.
*   **Emotion:** The overall emotional tone of the thread is overwhelmingly positive. There's a sense of appreciation and enthusiasm for the content of the article.
*   **Top 3 Points of View:**
    *   The article provides a clear and concise explanation of data engineering concepts without unnecessary hype.
    *   The article resonates with the personal vision and experience of the readers in the field.
    *   The article helps consultants cut through the BS in software/hardware marketing/sales for CIOs.

**[Whats the simplest/fastest way to bulk import 100s of CSVs each into their OWN table in SSMS? (Using SSIS, command prompt, or possibly python) (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k0mgmh/whats_the_simplestfastest_way_to_bulk_import_100s/)**
*   **Summary:** The thread discusses different approaches to bulk importing hundreds of CSV files into individual tables within SSMS, considering SSIS, command prompt, and Python.
*   **Emotion:** The emotional tone is mostly neutral, focusing on providing technical solutions and advice.
*   **Top 3 Points of View:**
    *   SSMS Bulk Insert with dynamic SQL and a cursor can be used.
    *   PowerShell, especially with the DBATools package, is a viable option.
    *   Azure ADF with the Copy Tool and auto table creation is another solution.

**[Is Kafka a viable way to store lots of streaming data? (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1k0qy7u/is_kafka_a_viable_way_to_store_lots_of_streaming/)**
*   **Summary:** This thread discusses the suitability of using Kafka for storing large amounts of streaming data. The consensus seems to be that while technically possible, it is not the ideal use case for Kafka, as it's primarily designed as a message bus.
*   **Emotion:** The emotional tone is generally neutral, with a hint of negativity towards the idea of using Kafka as a primary data store.
*   **Top 3 Points of View:**
    *   Kafka can store data indefinitely but querying is difficult, and it lacks features found in RDBMS.
    *   Pulsar is better suited for long-term storage of streaming data than Kafka.
    *   Using Kafka as a data store is like parking a car on the highway - not its intended purpose.

**[Switching batch jobs to streaming (Score: 4)](https://www.reddit.com/r/dataengineering/comments/1k0t6ua/switching_batch_jobs_to_streaming/)**
*   **Summary:**  Users are discussing the feasibility and best approaches for transitioning from batch processing to streaming.
*   **Emotion:** The emotional tone is neutral and practical.
*   **Top 3 Points of View:**
    *   Refactoring the entire transformation queries to conform to both business logic and streaming limitations is the best way forward.

**[Issue with Data Model with Querying Dynamics 365 via ADF (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k0b99g/issue_with_data_model_with_querying_dynamics_365/)**
*   **Summary:**  A user seeking help with querying Dynamics 365 via ADF is redirected to the PowerApps subreddit.
*   **Emotion:** The emotional tone is positive.
*   **Top 3 Points of View:**
    *   The user should seek help on the PowerApps subreddit.

**[Refactoring a script taking 17hours to run wit 0 Documentation (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k0lgfr/refactoring_a_script_taking_17hours_to_run_wit_0/)**
*   **Summary:** The thread discusses strategies for refactoring a large, undocumented script, emphasizing understanding the code, breaking it into smaller parts, writing tests, and creating data lineage.
*   **Emotion:** The overall emotional tone is neutral to positive, offering practical advice and encouragement.
*   **Top 3 Points of View:**
    *   Focus on understanding the process at a high level and then break it down into smaller pieces.
    *   Ensure you have a backed-up copy of the original code before making changes and try to deduplicate code.
    *   Write tests to ensure that your new pipeline produces the same results as the original pipeline and then start breaking up the script into manageable modules.

**[How Universities Are Using Data Warehousing to Meet Compliance and Funding Demands (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k0ogu0/how_universities_are_using_data_warehousing_to/)**
*   **Summary:** A bot provides a link to learning resources for data warehousing.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   DataEngineering.wiki provides a list of community-submitted learning resources.

**[Criticism at work because my lack of understanding business requirements is coinciding with quick turnaround times (Score: 3)](https://www.reddit.com/r/dataengineering/comments/1k0rxxi/criticism_at_work_because_my_lack_of/)**
*   **Summary:** This thread explores the challenges of meeting quick turnaround times when there's a lack of understanding of business requirements.
*   **Emotion:** The emotional tone is mostly neutral, with a focus on identifying the root cause of the issue.
*   **Top 3 Points of View:**
    *   Lack of direct interaction with stakeholders is likely the root cause.
    *   The person managing the stakeholders should provide context and functional implications of requests.
    *   People are often unable to clearly articulate what they need in terms of business requirements.

**[migrating from No-Code middleware platform to another more fundamental tech stack (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k0n177/migrating_from_nocode_middleware_platform_to/)**
*   **Summary:** The thread consists of a single question asking for the name of the current platform.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The commenter wants to know the name of the current No-Code middleware platform.

**[Very high level Data Services tool (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1k0sg0i/very_high_level_data_services_tool/)**
*   **Summary:**  A bot provides links to an open-source project showcase and a submission form.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   DataEngineering.wiki provides a showcase of open-source projects.

**[GCP Professional Data Engineer (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k0kjbu/gcp_professional_data_engineer/)**
*   **Summary:** The thread discusses resources and strategies for preparing for the GCP Professional Data Engineer certification.
*   **Emotion:** The emotional tone is neutral, with users sharing their experiences and recommendations.
*   **Top 3 Points of View:**
    *   Cloud Skills Boost may not be the most effective resource for preparation.
    *   Practice tests on Udemy and Dan Sullivan's study guide are recommended.
    *   Using AI to build and test on these subjects could be a good use case.

**[AI for data anomaly detection? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1k0miny/ai_for_data_anomaly_detection/)**
*   **Summary:** The thread initiates a discussion about AI options for data anomaly detection, inquiring about the specific type of anomaly detection needed.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The commenter is asking what kind of Anomaly detection you are looking for.

**[Vibe Coding in Data Engineering — Microsoft Fabric Test (Score: 0)](https://medium.com/@mariusz_kujawski/vibe-coding-in-data-engineering-microsoft-fabric-test-76e8d32db74f)**
*   **Summary:** The discussion revolves around the use of AI in coding, with differing opinions on its value.
*   **Emotion:** The emotional tone is negative, with some skepticism towards relying on AI for coding.
*   **Top 3 Points of View:**
    *   Letting an LLM do all the work is seen as an excuse to avoid learning how to code.
    *   Coding with AI is considered a time-saving tool.

**[Data Mapping (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1k0jkfv/data_mapping/)**
*   **Summary:** The thread explores the use of AI for data mapping and automatic permission granting based on employee roles and data needs.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The commenter is asking if the user is trying to use AI to group datasets together based on their context and automatically grant permissions for a specific group of datasets?
