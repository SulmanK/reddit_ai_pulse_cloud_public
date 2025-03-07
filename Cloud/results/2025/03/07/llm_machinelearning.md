---
title: "Machine Learning Subreddit"
date: "2025-03-07"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "nlp", "llm"]
---

# Overall Ranking and Top Discussions
1.  [[D] Best resources to learn how to build with LLMs](https://www.reddit.com/r/MachineLearning/comments/1j5jlae/d_best_resources_to_learn_how_to_build_with_llms/) (Score: 21)
    * Discusses the best resources for learning how to build with Large Language Models (LLMs), mentioning resources like Sebastian Raschka's notebooks, Jurafsky NLP book, and Andrej Karpathy's building GPT video.
2.  [[R] HybridNorm: Combining Pre-Norm and Post-Norm for More Stable and Effective Transformer Training](https://www.reddit.com/r/MachineLearning/comments/1j5l9mk/r_hybridnorm_combining_prenorm_and_postnorm_for/) (Score: 6)
    *  Discusses a research paper on "HybridNorm," a technique combining pre-norm and post-norm for transformer training. The discussion touches on computational time and comparisons with RMSNorm.
3.  [[D] What are the best practices for using PySpark with ML libraries](https://www.reddit.com/r/MachineLearning/comments/1j5y3d2/d_what_are_the_best_practices_for_using_pyspark/) (Score: 5)
    * Focuses on best practices for using PySpark with ML libraries. The discussion includes alternatives to Spark like Dask and Polars, and whether or not Spark is still relevant for ML, outside of foundation models.
4.  [[R] [P] SLM recommendation to solve sound-alike word errors](https://www.reddit.com/r/MachineLearning/comments/1j57nyy/r_p_slm_recommendation_to_solve_soundalike_word/) (Score: 4)
    *  Seeks recommendations for solving sound-alike word errors using Statistical Language Models (SLMs).
5.  [[D] Impact of Using BERT as the Encoder in T5](https://www.reddit.com/r/MachineLearning/comments/1j5gtie/d_impact_of_using_bert_as_the_encoder_in_t5/) (Score: 1)
    * Discusses the impact of using BERT as the encoder in the T5 model, mentioning that T5 was pretrained on 800GB of data.
6.  [[D] How do you orchestrate on-prem/local training and scale to the cloud?](https://www.reddit.com/r/MachineLearning/comments/1j5lkw9/d_how_do_you_orchestrate_onpremlocal_training_and/) (Score: 1)
    *  Focuses on orchestrating on-prem/local training and scaling to the cloud, mentioning DAG pipeline frameworks like Ploomber and Argo, as well as Kubeflow.
7.  [[D] Cloud Computing vs. Personal Workstation—Why the Cloud Wins for Heavy Workloads](https://www.reddit.com/r/MachineLearning/comments/1j5ph94/d_cloud_computing_vs_personal_workstationwhy_the/) (Score: 0)
    *  Discusses the advantages of cloud computing over personal workstations for heavy workloads, referencing Andrej Karpathy's recommendation of Lambda Labs and comparing the cost of renting vs. buying GPU resources, and alternative GPU marketplaces.

# Detailed Analysis by Thread
**[[D] Best resources to learn how to build with LLMs (Score: 21)](https://www.reddit.com/r/MachineLearning/comments/1j5jlae/d_best_resources_to_learn_how_to_build_with_llms/)**
*  **Summary:** Users share and recommend resources for learning to build with Large Language Models (LLMs). Mentions specific resources, including Jupyter notebooks and video series.
*  **Emotion:** Predominantly Positive and Neutral. Recommendations are presented with enthusiasm and generally seen as helpful.
*  **Top 3 Points of View:**
    *   Sebastian Raschka's Jupyter notebooks are highly recommended as time-efficient for learning LLM basics.
    *   Andrej Karpathy's videos provide an overview, while Vizuara's "LLM from Scratch" playlist offers a detailed explanation.
    *   The Jurafsky NLP book provides the base of NLP, and the Hugging Face NLP course focuses on applications.

**[[R] HybridNorm: Combining Pre-Norm and Post-Norm for More Stable and Effective Transformer Training (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1j5l9mk/r_hybridnorm_combining_prenorm_and_postnorm_for/)**
*  **Summary:** Users discuss a research paper about HybridNorm for improving transformer training.
*  **Emotion:** Neutral. The discussion is focused on the technical aspects of the paper, without strong positive or negative sentiment.
*  **Top 3 Points of View:**
    *   One user questions the computational time added by HybridNorm.
    *   Another user thinks the paper seems insufficient and questions why RMSNorm isn't used everywhere.

**[[D] What are the best practices for using PySpark with ML libraries (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1j5y3d2/d_what_are_the_best_practices_for_using_pyspark/)**
*  **Summary:** Users discuss best practices for using PySpark with ML libraries. The discussion also explores whether Spark is still necessary for Machine Learning, since cloud instances can now scale vertically.
*  **Emotion:** Neutral. The discussion centers around technical advice and opinions on the usefulness of PySpark.
*  **Top 3 Points of View:**
    *   Spark is primarily useful for ETL and feature engineering, with training/inference done on a single machine due to memory limitations.
    *   Alternatives like Dask and Polars should be considered for scaling ML workloads.
    *   Few people use Spark for ML anymore, because cloud can now scale vertically.

**[[R] [P] SLM recommendation to solve sound-alike word errors (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1j57nyy/r_p_slm_recommendation_to_solve_soundalike_word/)**
*  **Summary:** A user requests recommendations for solving sound-alike word errors with Statistical Language Models (SLMs).
*  **Emotion:** Neutral. A user expresses confusion about the provided example sentence and suggests that the problem may be under-specified.
*  **Top 3 Points of View:**
    *   The nature of the sound-alike error is unclear.
    *   The problem might be under-specified.

**[[D] Impact of Using BERT as the Encoder in T5 (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1j5gtie/d_impact_of_using_bert_as_the_encoder_in_t5/)**
*  **Summary:** A discussion on the implications of using BERT as the encoder in T5.
*  **Emotion:** Neutral. The discussion centers around the pretraining datasets and potential strategies for adapting the models.
*  **Top 3 Points of View:**
    *   The T5 model was pretrained on a much larger dataset than the original BERT.
    *   Frankensteining BERT as a base may be less effective than training T5 on the same corpus.

**[[D] How do you orchestrate on-prem/local training and scale to the cloud? (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1j5lkw9/d_how_do_you_orchestrate_onpremlocal_training_and/)**
*  **Summary:** Users discuss how to orchestrate on-prem/local training and scale to the cloud.
*  **Emotion:** Neutral. Users share recommendations for tools and frameworks.
*  **Top 3 Points of View:**
    *   Using a DAG pipeline framework with configurability for different deployments is useful.
    *   Ploomber is a good option.
    *   Kubeflow is another option.

**[[D] Cloud Computing vs. Personal Workstation—Why the Cloud Wins for Heavy Workloads (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1j5ph94/d_cloud_computing_vs_personal_workstationwhy_the/)**
*  **Summary:** The discussion revolves around whether to use cloud computing or a personal workstation, particularly for heavy workloads.
*  **Emotion:** Neutral. The discussion includes arguments both for renting resources in the cloud and investing in personal hardware.
*  **Top 3 Points of View:**
    *   Renting cloud resources is often more practical, particularly when needing expensive GPUs like A100s.
    *   Continuous use can make buying hardware more cost-effective over time.
    *   GPU marketplaces, can help save money on cloud computing by comparing pricing from multiple providers.
