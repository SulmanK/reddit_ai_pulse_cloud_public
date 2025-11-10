---
title: "Data Engineering Subreddit"
date: "2025-11-10"
description: "Analysis of top discussions and trends in the dataengineering subreddit"
tags: ["data engineering", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Boss wants to do data pipelines in n8n](https://www.reddit.com/r/dataengineering/comments/1otf0bc/boss_wants_to_do_data_pipelines_in_n8n/) (Score: 41)
    * The discussion revolves around the suitability of n8n, a low-code platform, for building data pipelines, with some suggesting alternatives like dbt and Prefect.
2.  [How are you handling projected AI costs ($75k+/mo) and data conflicts for customer-facing agents?](https://www.reddit.com/r/dataengineering/comments/1ota9vg/how_are_you_handling_projected_ai_costs_75kmo_and/) (Score: 15)
    *  The discussion focuses on the high costs associated with AI and potential solutions, as well as how to deal with data conflicts arising from AI usage in customer service.
3.  [Is the market finally recovering?](https://www.reddit.com/r/dataengineering/comments/1oth893/is_the_market_finally_recovering/) (Score: 14)
    *  Users are sharing their perspectives on whether the data engineering job market is improving, with some reporting an increase in opportunities while others remain skeptical.
4.  [What’s your achievements in Data Engineering](https://www.reddit.com/r/dataengineering/comments/1otilmc/whats_your_achievements_in_data_engineering/) (Score: 11)
    *  Data engineers are sharing their accomplishments, such as building data pipelines that prevented overbooking, deleting unused data to save money, and creating self-service A/B testing dashboards.
5.  [Tools for tracking data ownership (fields, reports, datasets)?](https://www.reddit.com/r/dataengineering/comments/1osxxqa/tools_for_tracking_data_ownership_fields_reports/) (Score: 11)
    *  The discussion centers on tools for tracking data ownership, with suggestions including data catalogs like DataHub and OpenMetadata, as well as using Power BI and Purview.
6.  [DAMA Certificate (Data Management CDMP)](https://www.reddit.com/r/dataengineering/comments/1ot9jjk/dama_certificate_data_management_cdmp/) (Score: 10)
    *  The discussion is about the DAMA Data Management CDMP certification, with users sharing resources for studying and preparing for the exam.
7.  [Help with Terraform](https://www.reddit.com/r/dataengineering/comments/1otehvq/help_with_terraform/) (Score: 8)
    *  The discussion revolves around using Terraform for managing data infrastructure, with some arguing it's a valuable skill for data engineers, while others see it as more of a DevOps responsibility.
8.  [What topics should i cover for pyspark experience 2yrs](https://www.reddit.com/r/dataengineering/comments/1otcrl9/what_topics_should_i_cover_for_pyspark_experience/) (Score: 7)
    *  Users are recommending topics related to PySpark that should be covered by a data engineer with 2 years of experience.
9.  [When to stop using sheets and start using proper database](https://www.reddit.com/r/dataengineering/comments/1ot5z6i/when_to_stop_using_sheets_and_start_using_proper/) (Score: 6)
    *  The discussion centers around the transition from using spreadsheets to proper databases, with advice focusing on the benefits of databases for collaboration, version control, and error reduction.
10. [Production support to data engineer guide](https://www.reddit.com/r/dataengineering/comments/1otd6a5/production_support_to_data_engineer_guide/) (Score: 2)
    *  This thread seems to be centered around the transferability of pyspark skills in data engineering roles.
11. [Is part of idempotency property also ensuring information synchronization with the source?](https://www.reddit.com/r/dataengineering/comments/1otab89/is_part_of_idempotency_property_also_ensuring/) (Score: 1)
    *  This thread discusses methods for ensuring data idempotency in a data lake environment.
12. [How to convert image to excel (csv) ??](https://www.reddit.com/r/dataengineering/comments/1otfl35/how_to_convert_image_to_excel_csv/) (Score: 0)
    *  The discussion focuses on methods to convert images into Excel or CSV format, recommending Tesseract OCR, AWS Textract, and LLM APIs.
13. [On-Prem Data Lake Solutions](https://www.reddit.com/r/dataengineering/comments/1otdi46/onprem_data_lake_solutions/) (Score: 0)
    *  Users are discussing on-premise data lake solutions, with one suggesting pg_lake.

# Detailed Analysis by Thread
**[[D] Boss wants to do data pipelines in n8n (Score: 41)](https://www.reddit.com/r/dataengineering/comments/1otf0bc/boss_wants_to_do_data_pipelines_in_n8n/)**
*   **Summary:** The thread discusses the use of n8n for data pipelines, with some arguing it's not suitable and suggesting alternatives like dbt and Prefect. Concerns are raised about maintainability, lineage, backfilling, and materialization concepts. Others advise on how to approach the situation with the boss, suggesting a POC and focusing on business context.
*   **Emotion:** The overall emotional tone is Neutral, with users providing objective advice and technical opinions.
*   **Top 3 Points of View:**
    *   n8n is not a good choice for data pipelines due to limitations in maintainability, lineage, and backfilling.
    *   Conduct a POC to demonstrate the limitations of n8n and compare it to alternatives.
    *   Frame the discussion in a business context, focusing on the company's specific data needs.

**[How are you handling projected AI costs ($75k+/mo) and data conflicts for customer-facing agents? (Score: 15)](https://www.reddit.com/r/dataengineering/comments/1ota9vg/how_are_you_handling_projected_ai_costs_75kmo_and/)**
*   **Summary:** The thread addresses the high costs associated with AI and potential data conflicts. Users suggest pricing by usage, treating access to data as a product with rate-limited APIs, and fixing engineering bugs related to incorrect data access.
*   **Emotion:** The overall emotional tone is Positive, with a focus on problem-solving and practical solutions.
*   **Top 3 Points of View:**
    *   Implement pricing by usage to address high AI costs.
    *   Expose data through predictable, rate-limited APIs rather than allowing arbitrary queries.
    *   Address data conflicts as engineering bugs related to access control and logging.

**[Is the market finally recovering? (Score: 14)](https://www.reddit.com/r/dataengineering/comments/1oth893/is_the_market_finally_recovering/)**
*   **Summary:** Users share their experiences and opinions on whether the data engineering job market is recovering. Some report an uptick in opportunities, while others remain skeptical. Factors like new budgets being set in January are mentioned.
*   **Emotion:** The overall emotional tone is Negative, reflecting uncertainty and mixed experiences.
*   **Top 3 Points of View:**
    *   There is an uptick in job opportunities and interview volume.
    *   The market has not recovered, and opportunities are still scarce.
    *   Market recovery is cyclical, with Q1 and Q2 being the strongest recruitment periods due to new budgets.

**[What’s your achievements in Data Engineering (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1otilmc/whats_your_achievements_in_data_engineering/)**
*   **Summary:** Data engineers share their accomplishments, including building pipelines that prevent overbooking, saving money by deleting unused data, and creating self-service A/B testing dashboards.
*   **Emotion:** The overall emotional tone is Positive, with pride and satisfaction in the achievements shared.
*   **Top 3 Points of View:**
    *   Building pipelines that solve critical business problems and prevent losses.
    *   Optimizing data storage and reducing costs by deleting unused data.
    *   Empowering data scientists and product teams with self-service tools and properly modeled data.

**[Tools for tracking data ownership (fields, reports, datasets)? (Score: 11)](https://www.reddit.com/r/dataengineering/comments/1osxxqa/tools_for_tracking_data_ownership_fields_reports/)**
*   **Summary:** The discussion revolves around tools for tracking data ownership. Suggestions include data catalogs like DataHub and OpenMetadata, using Power BI with Unity Catalog, and considering Purview. The best approach depends on the size and complexity of the organization.
*   **Emotion:** The overall emotional tone is Positive, with users sharing practical solutions and recommendations.
*   **Top 3 Points of View:**
    *   Data catalogs like DataHub and OpenMetadata are suitable for larger organizations with many datasets.
    *   For Databricks users, Unity Catalog can be the source of truth and synced to Power BI.
    *   Power BI can be used creatively to keep metadata with the artifact.

**[DAMA Certificate (Data Management CDMP) (Score: 10)](https://www.reddit.com/r/dataengineering/comments/1ot9jjk/dama_certificate_data_management_cdmp/)**
*   **Summary:** The thread discusses the DAMA Data Management CDMP certification, with users sharing resources for studying and preparing for the exam. The DAMA-DMBOK is recommended as a mandatory resource, and advice is given on structuring a study plan.
*   **Emotion:** The overall emotional tone is Positive, with encouragement and helpful advice for those pursuing the certification.
*   **Top 3 Points of View:**
    *   The DAMA-DMBOK is essential for preparing for the CDMP exam.
    *   Creating a personalized study plan based on experience and using tools like Gemini can be helpful.
    *   The CDMP certification is more suitable for those aiming for management positions.

**[Help with Terraform (Score: 8)](https://www.reddit.com/r/dataengineering/comments/1otehvq/help_with_terraform/)**
*   **Summary:** The discussion centers on the role of Terraform in data engineering. Some argue that it's a valuable skill for DEs to manage infrastructure as code (IaC), while others see it as more of a DevOps responsibility. Resources and tools like Terraform MCP Server and Databricks Asset Bundle (DABs) are mentioned.
*   **Emotion:** The overall emotional tone is Positive, with encouragement to learn Terraform and recognition of its value in modern data engineering.
*   **Top 3 Points of View:**
    *   Terraform is a valuable skill for data engineers and should be embraced.
    *   Data engineers should manage their own infrastructure as code for observability and repeatability.
    *   Terraform is becoming increasingly important as data engineers take on responsibilities in dataops and data platform engineering.

**[What topics should i cover for pyspark experience 2yrs (Score: 7)](https://www.reddit.com/r/dataengineering/comments/1otcrl9/what_topics_should_i_cover_for_pyspark_experience/)**
*   **Summary:** The thread requests topics to cover for a PySpark interview with 2 years experience, with a recommendation for "Data shuffle, cache/persist, resource provisioning".
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    * Data shuffle
    * Cache/persist
    * Resource provisioning

**[When to stop using sheets and start using proper database (Score: 6)](https://www.reddit.com/r/dataengineering/comments/1ot5z6i/when_to_stop_using_sheets_and_start_using_proper/)**
*   **Summary:** The discussion centers around the transition from spreadsheets to databases, focusing on the benefits of databases for collaboration, version control, and error reduction.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   When collaboration and version control are needed, switch to a database.
    *   Focus on the benefits for users, such as error reduction and time savings.
    *   Spreadsheets might still be appropriate if basic formatting and validation constraints are implemented.

**[Production support to data engineer guide (Score: 2)](https://www.reddit.com/r/dataengineering/comments/1otd6a5/production_support_to_data_engineer_guide/)**
*   **Summary:** The thread discusses the transferability of pyspark skills in data engineering roles.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Pyspark is transferable

**[Is part of idempotency property also ensuring information synchronization with the source? (Score: 1)](https://www.reddit.com/r/dataengineering/comments/1otab89/is_part_of_idempotency_property_also_ensuring/)**
*   **Summary:** This thread discusses methods for ensuring data idempotency in a data lake environment.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Store a copy of external source data in the data lake.

**[How to convert image to excel (csv) ?? (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1otfl35/how_to_convert_image_to_excel_csv/)**
*   **Summary:** The discussion focuses on methods to convert images into Excel or CSV format, recommending Tesseract OCR, AWS Textract, and LLM APIs.
*   **Emotion:** The overall emotional tone is Positive.
*   **Top 3 Points of View:**
    *   LLM APIs
    *   Tesseract OCR with custom training
    *   AWS Textract

**[On-Prem Data Lake Solutions (Score: 0)](https://www.reddit.com/r/dataengineering/comments/1otdi46/onprem_data_lake_solutions/)**
*   **Summary:** Users are discussing on-premise data lake solutions.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Check out pg_lake — just released.
