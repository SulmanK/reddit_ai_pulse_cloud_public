---
title: "Data Science Subreddit"
date: "2026-05-04"
description: "Analysis of top discussions and trends in the datascience subreddit"
tags: ["datascience", "AI", "machine learning", "LLMs", "PyTorch", "TensorFlow"]
---

# Overall Ranking and Top Discussions
*   1. [[D] Are teams still using Pytorch/Tensorflow, or is most ML work just calling LLM endpoints and prompt engineering now?](https://www.reddit.com/r/datascience/comments/1t32duy/are_teams_still_using_pytorchtensorflow_or_is/) (Score: 144)
    *   This thread discusses the current landscape of machine learning work, specifically whether traditional frameworks like PyTorch and TensorFlow are still prevalent or if the focus has shifted to LLM endpoints and prompt engineering.
*   2. [[W] Weekly Entering & Transitioning - Thread 04 May, 2026 - 11 May, 2026](https://www.reddit.com/r/datascience/comments/1t36w9e/weekly_entering_transitioning_thread_04_may_2026/) (Score: 3)
    *   This is a weekly thread for individuals entering or transitioning into the data science field, with discussions covering job market challenges and interview preparation topics.
*   3. [[Q] Q-Q plot criteria relaxed for Regression with huge sample size?](https://www.reddit.com/r/AskStatistics/comments/1t36pft/qq_plot_criteria_relaxed_for_regression_with_huge/) (Score: 2)
    *   This thread explores whether Q-Q plot criteria can be relaxed for regression analysis when dealing with very large sample sizes.
*   4. [[P] The Problem with Calling Model Distillation an "Attack"](https://www.interconnects.ai/p/the-distillation-panic) (Score: 1)
    *   This post examines the concept of model distillation, questioning its framing as an "attack" and discussing its implications for AI development and competition.

# Detailed Analysis by Thread
**[ Are teams still using Pytorch/Tensorflow, or is most ML work just calling LLM endpoints and prompt engineering now? (Score: 144)](https://www.reddit.com/r/datascience/comments/1t32duy/are_teams_still_using_pytorchtensorflow_or_is/)**
*   **Summary:** The core of the discussion revolves around the shift in applied ML. While traditional frameworks like PyTorch and TensorFlow are still in use for specialized tasks (frontier training, recsys, robotics, etc.) and in large companies, many newly posted "AI engineer" roles focus on LLM integration, prompt engineering, and RAG. This is often due to cost and speed benefits for shipping "AI features." However, there's a recognized need for skills that bridge both worlds, such as custom model development alongside LLM orchestration and evaluation. The market is seen as competitive, with a potential over-hiring correction and cyclical market factors contributing to the current hiring challenges.
*   **Emotion:** The overall emotional tone is Neutral, with users providing factual observations and analyses of the current ML job market and technology trends. Some comments express concerns about hiring difficulty and the evolving skillsets required.
*   **Top 3 Points of View:**
    *   The framing of "PyTorch vs. endpoints" mixes different labor markets; while many mid-tier supervised ML tasks have been simplified by LLMs, specialized areas still heavily rely on traditional frameworks for training, proprietary data handling, and performance-critical applications.
    *   Many "AI Engineer" roles are increasingly about "glue work" – integrating LLMs and prompt engineering – rather than deep model development. The critical skills often lie in evaluation design, dataset curation, and reasoning about cost/latency tradeoffs.
    *   The current "brutal market" is a combination of cyclical economic factors and the bullwhip effect from past over-hiring, rather than solely AI displacement, although the AI framing makes it feel that way.

**[ Weekly Entering & Transitioning - Thread 04 May, 2026 - 11 May, 2026 (Score: 3)](https://www.reddit.com/r/datascience/comments/1t36w9e/weekly_entering_transitioning_thread_04_may_2026/)**
*   **Summary:** This weekly thread serves as a space for individuals entering or transitioning into the data science field to ask questions and share experiences. Comments indicate it's a good place to lurk for career switchers, but also highlight the current difficulties in the hiring market. One user is preparing for interviews and struggling with topics like marginal and conditional probability.
*   **Emotion:** The emotional tone is mixed, with some positive sentiment ("Good one!") but also a significant undertone of concern and negativity regarding the current hiring landscape. There's also a sense of struggle related to learning specific statistical concepts for interviews.
*   **Top 3 Points of View:**
    *   The thread is a valuable resource for those looking to switch fields into data science.
    *   The current hiring market is described as "messed up" and challenging for newcomers.
    *   Interview preparation can involve revisiting and struggling with fundamental statistical concepts.

**[ Q-Q plot criteria relaxed for Regression with huge sample size? (Score: 2)](https://www.reddit.com/r/AskStatistics/comments/1t36pft/qq_plot_criteria_relaxed_for_regression_with_huge/)**
*   **Summary:** This comment explains that the Central Limit Theorem (CLT) does not guarantee normality of residuals, but rather applies to the sampling distribution of estimators. It outlines key questions to consider when evaluating regression models, including the type of regression, model fit, the goal of the analysis (inference, prediction, explanation), and the scope of application. It also highlights that heteroscedasticity and dependence can be more significant issues than mild non-normality, especially for inference.
*   **Emotion:** The emotional tone is Neutral, as it provides a direct, informative, and analytical response to a statistical question.
*   **Top 3 Points of View:**
    *   The Central Limit Theorem does not imply normality of residuals in regression.
    *   Key considerations for regression analysis include the model type, fitting, goals, and generalizability.
    *   Heteroscedasticity and dependence are often greater concerns than mild non-normality in regression.

**[ The Problem with Calling Model Distillation an "Attack" (Score: 1)](https://www.interconnects.ai/p/the-distillation-panic)**
*   **Summary:** This comment suggests that LLMs essentially distill human intelligence and refine entropy, with the substrate (the underlying technology) being less important than the mapping of concepts as entropy decreases. Another user is building a tool for prompt distillation and questions if this activity contributes to a decline in the US's AI leadership.
*   **Emotion:** The emotional tone is Neutral, with philosophical observations about LLMs and a question about the implications of developing AI tools.
*   **Top 3 Points of View:**
    *   LLMs act as mirrors to their users, distilling and refining human intelligence.
    *   The underlying technology of LLMs is secondary to their ability to map concepts as entropy decreases.
    *   There's a concern about whether developing tools like prompt distillation contributes to a nation's AI race position.
