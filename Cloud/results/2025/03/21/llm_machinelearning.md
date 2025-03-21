---
title: "Machine Learning Subreddit"
date: "2025-03-21"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "AI", "research"]
---

# Overall Ranking and Top Discussions
1.  [[D] The Recurrent Delusion: How ML Collectively Forgot What RNNs Were Built For](https://www.reddit.com/r/MachineLearning/comments/1jgfkrl/d_the_recurrent_delusion_how_ml_collectively/) (Score: 50)
    * Discusses the resurgence of interest in RNNs for state tracking capabilities, contrasting them with transformers and state-space models (SSMs).
2.  [[N] ​Introducing FlashTokenizer: The World's Fastest Tokenizer Library for LLM Inference](https://www.reddit.com/r/MachineLearning/comments/1jg9ou5/n_introducing_flashtokenizer_the_worlds_fastest/) (Score: 24)
    * Introduction of FlashTokenizer, claimed to be the fastest tokenizer library for LLM inference.
3.  [[P] AlphaZero applied to Tetris (incl. other MCTS policies)](https://www.reddit.com/r/MachineLearning/comments/1jgf0lf/p_alphazero_applied_to_tetris_incl_other_mcts/) (Score: 9)
    * Applying AlphaZero to Tetris with other Monte Carlo Tree Search policies.
4.  [[R] Looking for an Estimator to Measure the Coverage of Sampled Points in N-Dimensional Space](https://www.reddit.com/r/MachineLearning/comments/1jgfo2h/r_looking_for_an_estimator_to_measure_the/) (Score: 6)
    * Someone is looking for a metric to measure the coverage of sampled points in N-dimensional space.
5.  [[R] Scale-wise Distillation of Diffusion Models](https://www.reddit.com/r/MachineLearning/comments/1jgjf73/r_scalewise_distillation_of_diffusion_models/) (Score: 6)
    * Discussion around Scale-wise Distillation of Diffusion Models, a method to improve the efficiency and structure of data generation by treating spectral complexity across time in the generative process.
6.  [[D] Best Practices for Diagramming ML System Internals?](https://www.reddit.com/r/MachineLearning/comments/1jglv23/d_best_practices_for_diagramming_ml_system/) (Score: 6)
    * Discussion on best practices for diagramming ML system internals.
7.  [[D] Journals with no publication charge or article processing fee](https://www.reddit.com/r/MachineLearning/comments/1jfykdy/d_journals_with_no_publication_charge_or_article/) (Score: 1)
    * Discussion around journals with no publication charges or article processing fees.
8.  [[D] Roast my CV (PhD Applicant, Medical Imaging + AI)](https://www.reddit.com/r/MachineLearning/comments/1jgpu1y/d_roast_my_cv_phd_applicant_medical_imaging_ai/) (Score: 0)
    * Asking for feedback on a CV for a PhD applicant in Medical Imaging + AI.

# Detailed Analysis by Thread
**[[D] The Recurrent Delusion: How ML Collectively Forgot What RNNs Were Built For (Score: 50)](https://www.reddit.com/r/MachineLearning/comments/1jgfkrl/d_the_recurrent_delusion_how_ml_collectively/)**
*   **Summary:** This thread discusses the potential resurgence of interest in Recurrent Neural Networks (RNNs) for their state-tracking capabilities, contrasting them with the current dominance of Transformers and State-Space Models (SSMs). The discussion covers the theoretical advantages and disadvantages of each architecture, the computational efficiency of RNNs compared to the test-time compute needed for Transformers, and specific implementations like recurrent transformers and Meta's COCONUT.
*   **Emotion:** The overall emotional tone is Neutral, although some individual comments show negative sentiments in response to the post.
*   **Top 3 Points of View:**
    *   RNNs possess inherent state-tracking capabilities that Transformers lack, potentially making them more efficient for certain tasks.
    *   Transformers currently outperform RNNs at scale due to their parallelization capabilities and training stability, despite any theoretical advantages of RNNs.
    *   There is a need to revisit RNNs and explore hybrid architectures like recurrent transformers to address the unsustainable compute requirements of large-scale Transformers.

**[[N] ​Introducing FlashTokenizer: The World's Fastest Tokenizer Library for LLM Inference (Score: 24)](https://www.reddit.com/r/MachineLearning/comments/1jg9ou5/n_introducing_flashtokenizer_the_worlds_fastest/)**
*   **Summary:** The thread discusses the introduction of a new tokenizer library, FlashTokenizer, which claims to be the fastest tokenizer library for LLM inference.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Tokenization is a deterministic process and any differences are bugs or incompatible implementation choices.

**[[P] AlphaZero applied to Tetris (incl. other MCTS policies) (Score: 9)](https://www.reddit.com/r/MachineLearning/comments/1jgf0lf/p_alphazero_applied_to_tetris_incl_other_mcts/)**
*   **Summary:** The thread discusses the application of AlphaZero to Tetris with other Monte Carlo Tree Search policies.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The project seems neat.

**[[R] Looking for an Estimator to Measure the Coverage of Sampled Points in N-Dimensional Space (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1jgfo2h/r_looking_for_an_estimator_to_measure_the/)**
*   **Summary:** The thread discusses the need for a metric to measure the coverage of sampled points in N-dimensional space, specifically in the context of neural network embeddings.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The problem can be addressed with techniques like Gaussian processes and confidence intervals.
    *   Kernel density estimation might be a viable approach, especially when the bounds of the space are unknown.
    *   The goal is to determine the minimum number of samples needed for reliable search using cosine similarity in the embedding space.

**[[R] Scale-wise Distillation of Diffusion Models (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1jgjf73/r_scalewise_distillation_of_diffusion_models/)**
*   **Summary:** This thread discusses a new approach by Yandex Research on diffusion models that treats spectral complexity across time in the generative process, aligning space and time for more efficient and structured data generation, without cascading models.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Traditional diffusion models assume a constant spatial complexity at each timestep, which is a false symmetry.
    *   Scale-wise Distillation (SWD) is more aligned with the generative structure of the data.
    *   SWD focuses on aligning space and time instead of skipping time.

**[[D] Best Practices for Diagramming ML System Internals? (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1jglv23/d_best_practices_for_diagramming_ml_system/)**
*   **Summary:** The thread discusses best practices for diagramming Machine Learning system internals.
*   **Emotion:** The overall emotional tone is Positive.
*   **Top 3 Points of View:**
    *   Don't overthink it and use either https://excalidraw.com/ or draw.io.

**[[D] Journals with no publication charge or article processing fee (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1jfykdy/d_journals_with_no_publication_charge_or_article/)**
*   **Summary:** The thread discusses journals with no publication charges or article processing fees.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   Almost all of the good journals are free, except for open access journals.
    *   IEEE transactions journals are free to publish in, although they charge an over page fee for any pages beyond 10.
    *   Mentioned journals like JMLR/TMLR.

**[[D] Roast my CV (PhD Applicant, Medical Imaging + AI) (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1jgpu1y/d_roast_my_cv_phd_applicant_medical_imaging_ai/)**
*   **Summary:** The thread discusses a request for feedback on a CV for a PhD applicant in Medical Imaging + AI.
*   **Emotion:** The overall emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   The CV format needs improvement.
    *   Try publishing in standard AI conferences/journals.
