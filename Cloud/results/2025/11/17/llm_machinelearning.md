---
title: "Machine Learning Subreddit"
date: "2025-11-17"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "AI", "NLP"]
---

# Overall Ranking and Top Discussions
1.  [[D] Do industry researchers log test set results when training production-level models?](https://www.reddit.com/r/MachineLearning/comments/1oz3he6/d_do_industry_researchers_log_test_set_results/) (Score: 12)
    *   The discussion revolves around whether industry researchers log test set results during the training of production-level models.
2.  [[D] An alternative to Nested Cross Validation and independent test set doubts](https://www.reddit.com/r/MachineLearning/comments/1ozhv8q/d_an_alternative_to_nested_cross_validation_and/) (Score: 7)
    *   This thread discusses an alternative to nested cross-validation and addresses doubts about independent test sets.
3.  [[D] Comparing Giskard and Rhesis for LLM evaluation — looking for experiences](https://www.reddit.com/r/MachineLearning/comments/1ozkj1f/d_comparing_giskard_and_rhesis_for_llm_evaluation/) (Score: 7)
    *   The thread compares Giskard and Rhesis for evaluating Large Language Models (LLMs) and seeks experiences with both tools.
4.  [OpenGuardrails: open-source AI safety and guardrail platform released](https://arxiv.org/abs/2510.19169) (Score: 1)
    *   This post announces the release of OpenGuardrails, an open-source platform for AI safety and guardrails.
5.  [[D] Seeking arXiv Endorsement for Individual-Scale AI Orchestration Research (cs.AI)](https://www.reddit.com/r/MachineLearning/comments/1ozheni/d_seeking_arxiv_endorsement_for_individualscale/) (Score: 0)
    *   The thread is about seeking arXiv endorsement for research on Individual-Scale AI Orchestration.
6.  [[P] AI Learns to Speedrun Mario Bros After 6 Million Deaths](https://youtube.com/watch?v=3YyiYH327gY&si=oLtZ50MWPWDrm9su) (Score: 0)
    *   The discussion covers an AI learning to speedrun Mario Bros, initially reported as after 6 million deaths, but corrected to 271k.

# Detailed Analysis by Thread
**[[D] Do industry researchers log test set results when training production-level models? (Score: 12)](https://www.reddit.com/r/MachineLearning/comments/1oz3he6/d_do_industry_researchers_log_test_set_results/)**
*   **Summary:** The thread discusses the practice of logging test set results when training models in industry settings.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Some labs use three splits: training, optimization, and benchmarking, with only the post-trained benchmark being marketed.
    *   Training on the test set can lead to distrust in the model.
    *   Labs often run every checkpoint on an eval suite and pick the best one, even if they don't train directly on the test set.

**[[D] An alternative to Nested Cross Validation and independent test set doubts (Score: 7)](https://www.reddit.com/r/MachineLearning/comments/1ozhv8q/d_an_alternative_to_nested_cross_validation_and/)**
*   **Summary:** The discussion revolves around an alternative to nested cross-validation and questions the necessity of independent test sets. Some users criticize retraining the model in the final phase as bad practice.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   A test set simulates model behavior in production and addresses biases from hyperparameter tuning.
    *   Retraining the model in the final phase is considered bad practice as it modifies the weights.
    *   The proposed method is potentially biased, especially for smaller sample sizes, and alternatives exist for model selection using cross-validation.

**[[D] Comparing Giskard and Rhesis for LLM evaluation — looking for experiences (Score: 7)](https://www.reddit.com/r/MachineLearning/comments/1ozkj1f/d_comparing_giskard_and_rhesis_for_llm_evaluation/)**
*   **Summary:** Users discuss and compare Giskard and Rhesis, two tools used for evaluating Large Language Models (LLMs).
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   Giskard is good out-of-the-box but has limited customizability.
    *   Rhesis offers a modular design, which is preferable for complex deployments, but requires more setup.
    *   Being able to track how eval criteria evolve is crucial for understanding model drift.

**[OpenGuardrails: open-source AI safety and guardrail platform released](https://arxiv.org/abs/2510.19169) (Score: 1)**
*   **Summary:** A new open-source AI safety and guardrail platform called OpenGuardrails has been released. Users are discussing how it compares to other similar tools.
*   **Emotion:** The overall emotional tone of the thread is mixed with Neutral and Positive.
*   **Top 3 Points of View:**
    *   Users are interested in how OpenGuardrails compares to existing guardrail platforms like Guard Rails AI.
    *   Protecting against code-interpreter abuse is a good idea.
    *   Unifying communication across different safety detection and enforcement methods is beneficial.

**[[D] Seeking arXiv Endorsement for Individual-Scale AI Orchestration Research (cs.AI)](https://www.reddit.com/r/MachineLearning/comments/1ozheni/d_seeking_arxiv_endorsement_for_individualscale/) (Score: 0)**
*   **Summary:** The author is seeking arXiv endorsement for their research.
*   **Emotion:** The overall emotional tone of the thread is Negative.
*   **Top 3 Points of View:**
    *   The research is considered low quality and riddled with errors.

**[[P] AI Learns to Speedrun Mario Bros After 6 Million Deaths](https://youtube.com/watch?v=3YyiYH327gY&si=oLtZ50MWPWDrm9su) (Score: 0)**
*   **Summary:** A discussion around an AI learning to speedrun Mario Bros, clarifying the number of deaths it took to learn.
*   **Emotion:** The overall emotional tone of the thread is Neutral.
*   **Top 2 Points of View:**
    *   The actual number of deaths was closer to 271k than 6 million.
    *   Question about the AI architecture (RNN).
