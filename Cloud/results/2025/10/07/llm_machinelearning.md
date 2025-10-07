---
title: "Machine Learning Subreddit"
date: "2025-10-07"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "AI", "research"]
---

# Overall Ranking and Top Discussions
1.  [[D] Best practices for structuring an applied ML research project?](https://www.reddit.com/r/MachineLearning/comments/1nzw0v3/d_best_practices_for_structuring_an_applied_ml/) (Score: 24)
    * The thread discusses best practices for structuring an applied machine learning research project, including using uv for Python environments, MLflow for experiment tracking, pre-commit for linting, and separating code for dataset, model, and evaluation.
2.  [[D] Why RHLF instead of DAGGER (multi-step SFT)](https://www.reddit.com/r/MachineLearning/comments/1o099v3/d_why_rhlf_instead_of_dagger_multistep_sft/) (Score: 15)
    * The thread explores the differences between Reinforcement Learning from Human Feedback (RLHF) and DAGGER (multi-step Supervised Fine-Tuning) for model alignment, with a focus on how models generalize from feedback. RLHF creates a value function, while DAGGER uses supervised learning on trajectories.
3.  [[R] Predictive control of generative models](https://www.reddit.com/r/MachineLearning/comments/1o03yqd/r_predictive_control_of_generative_models/) (Score: 14)
    * The thread discusses the possibility of treating diffusion or flow sampling as a controlled process, using Model Predictive Control (MPC) or Model Predictive Path Integral (MPPI) to steer it during generation.
4.  [[D] AAAI Alignment Track Phase 2](https://www.reddit.com/r/MachineLearning/comments/1o0a215/d_aaai_alignment_track_phase_2/) (Score: 12)
    * This thread discusses the AAAI Alignment Track Phase 2, with participants sharing their review scores and discussing the quality and helpfulness of the reviews they received.
5.  [[d] AAAI 2026 Rebuttal Strategies](https://www.reddit.com/r/MachineLearning/comments/1o0h8kn/d_aaai_2026_rebuttal_strategies/) (Score: 9)
    * This thread focuses on strategies for writing rebuttals for AAAI 2026 paper submissions, with users sharing their review scores and seeking advice on how to address reviewer concerns.
6.  [[R] Schedule-free Lion optimizer](https://www.reddit.com/r/MachineLearning/comments/1o08yl7/r_schedulefree_lion_optimizer/) (Score: 6)
    * This thread introduces a schedule-free Lion optimizer and compares it to other optimizers like Prodigy, Fromage, or DoWG.
7.  [[D] Can time series foundation models knowledge transfer from stationary to non-stationary monotonic data?](https://www.reddit.com/r/MachineLearning/comments/1o0bd0c/d_can_time_series_foundation_models_knowledge/) (Score: 5)
    * The thread questions whether time series foundation models can transfer knowledge from stationary to non-stationary monotonic data.
8.  [[D] Indie AI Paper: Emergent Self-Diagnostics from Constraint Architecture – No CS Background, Just Vibe-Coding. Feedback?](https://www.reddit.com/r/MachineLearning/comments/1o0lcgj/d_indie_ai_paper_emergent_selfdiagnostics_from/) (Score: 0)
    * The thread discusses an indie AI paper on emergent self-diagnostics from constraint architecture, with users asking for feedback.

# Detailed Analysis by Thread
**[ [D] Best practices for structuring an applied ML research project? (Score: 24)](https://www.reddit.com/r/MachineLearning/comments/1nzw0v3/d_best_practices_for_structuring_an_applied_ml/)**
*  **Summary:**  The thread discusses best practices for structuring an applied machine learning research project.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * Use uv for your python environment. If collaborating, perhaps consider using a devcontainer.
    * Mlflow for experiment tracking, and if possible store your models in your mlflow runs for reproducibility.
    * Possibly a controversial take, but I advise against using frameworks like Lightning; instead do as much as you can from scratch, with plenty of copying from good projects.

**[ [D] Why RHLF instead of DAGGER (multi-step SFT) (Score: 15)](https://www.reddit.com/r/MachineLearning/comments/1o099v3/d_why_rhlf_instead_of_dagger_multistep_sft/)**
*  **Summary:**  The thread explores the differences between Reinforcement Learning from Human Feedback (RLHF) and DAGGER (multi-step Supervised Fine-Tuning) for model alignment.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * In RL you do not need perfect expert data anymore but only a reward function. And this reward model is trained on expert data so that it scales to unseen token trajectories.
    *  DAgger require an oracle at every rollout timestep.
    * RLHF creates this value function that helps the model understand not just what the right answer is, but why it's better than alternatives. With multi-step SFT, you're essentially doing supervised learning on increasingly better trajectories, but the model doesn't develop that internal sense of "goodness" that comes from the reward modeling in RLHF.

**[ [R] Predictive control of generative models (Score: 14)](https://www.reddit.com/r/MachineLearning/comments/1o03yqd/r_predictive_control_of_generative_models/)**
*  **Summary:**  The thread discusses the possibility of treating diffusion or flow sampling as a controlled process, using Model Predictive Control (MPC) or Model Predictive Path Integral (MPPI) to steer it during generation.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 3 Points of View:**
    * MPC and MPPI can be used to control diffusion or flow sampling during generation rather than only at the end.
    * There are some works in the robotics domain and I worked on am unfinished paper that adds e.g. kinematic constraints to the diffusion process.
    * Something like this? https://arxiv.org/abs/2409.08861

**[ [D] AAAI Alignment Track Phase 2 (Score: 12)](https://www.reddit.com/r/MachineLearning/comments/1o0a215/d_aaai_alignment_track_phase_2/)**
*  **Summary:** This thread discusses the AAAI Alignment Track Phase 2, with participants sharing their review scores and discussing the quality and helpfulness of the reviews they received.
*  **Emotion:** The overall emotional tone is Neutral, with some expressions of Positive sentiment regarding scores.
*  **Top 3 Points of View:**
    * Some users express optimism about their scores and the possibility of addressing reviewer concerns.
    * Others are critical of the review quality, citing inattentiveness from reviewers.
    * There's confusion about the number of reviews received (4 vs. 5).

**[ [d] AAAI 2026 Rebuttal Strategies (Score: 9)](https://www.reddit.com/r/MachineLearning/comments/1o0h8kn/d_aaai_2026_rebuttal_strategies/)**
*  **Summary:** This thread focuses on strategies for writing rebuttals for AAAI 2026 paper submissions, with users sharing their review scores and seeking advice on how to address reviewer concerns.
*  **Emotion:** The overall emotional tone is mixed, with Negative sentiment arising from poor reviews mixed with Positive sentiment.
*  **Top 3 Points of View:**
    * Some are frustrated with garbage reviews and reviewers asking for comparisons to SOTA methods that do not exist.
    * Some users are seeking advice on whether to add evaluations to the appendix or to explain the rationale behind the paper.
    * Address the specific issue(s) and not something more general or tangential; try to point to a specific passage if you can.

**[ [R] Schedule-free Lion optimizer (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1o08yl7/r_schedulefree_lion_optimizer/)**
*  **Summary:** This thread introduces a schedule-free Lion optimizer and compares it to other optimizers like Prodigy, Fromage, or DoWG.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 2 Points of View:**
    * Comparison with other schedule-free optimisers, like Prodigy, Fromage, or DoWG.
    * Wonder how LionSF would compare to them

**[ [D] Can time series foundation models knowledge transfer from stationary to non-stationary monotonic data? (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1o0bd0c/d_can_time_series_foundation_models_knowledge/)**
*  **Summary:** The thread questions whether time series foundation models can transfer knowledge from stationary to non-stationary monotonic data.
*  **Emotion:** The overall emotional tone is Neutral.
*  **Top 1 Points of View:**
    * These models are pretrained on any type of time series data, including non-stationary data. If they don't work for toy data, it is usually because there is no discernible pattern in the data to act upon.

**[ [D] Indie AI Paper: Emergent Self-Diagnostics from Constraint Architecture – No CS Background, Just Vibe-Coding. Feedback? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1o0lcgj/d_indie_ai_paper_emergent_selfdiagnostics_from/)**
*  **Summary:** The thread discusses an indie AI paper on emergent self-diagnostics from constraint architecture, with users asking for feedback.
*  **Emotion:** The overall emotional tone is Positive, with users expressing a desire to understand the author's work.
*  **Top 2 Points of View:**
    * LLM speech is hard to read and understand.
    * I would like to see the draft of your architecture/philosophy without any LLMs condensed into a blog or some other medium.
