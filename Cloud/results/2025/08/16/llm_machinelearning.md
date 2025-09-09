---
title: "Machine Learning Subreddit"
date: "2025-08-16"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "nlp", "ai"]
---

# Overall Ranking and Top Discussions

1.  [[D] Cool new ways to mix linear optimization with GNNs? (LP layers, simplex-like updates, etc.)](https://www.reddit.com/r/MachineLearning/comments/1mrjs5i/d_cool_new_ways_to_mix_linear_optimization_with/) (Score: 14)
    *   Discussion about combining linear optimization techniques with Graph Neural Networks (GNNs), including LP layers and simplex-like updates.
2.  [[D] model architecture or data?](https://www.reddit.com/r/MachineLearning/comments/1mrwm3w/d_model_architecture_or_data/) (Score: 12)
    *   A discussion on whether model architecture or data is more important, specifically in the context of transformers and data augmentation.
3.  [[R] How do I choose the best model in validation when I have no target data??](https://www.reddit.com/r/MachineLearning/comments/1mrqyni/r_how_do_i_choose_the_best_model_in_validation/) (Score: 0)
    *   A request for guidance on model selection during validation when target data is unavailable, with the suggestion that all models have target data.

# Detailed Analysis by Thread

**[[D] Cool new ways to mix linear optimization with GNNs? (LP layers, simplex-like updates, etc.) (Score: 14)](https://www.reddit.com/r/MachineLearning/comments/1mrjs5i/d_cool_new_ways_to_mix_linear_optimization_with/)**
*  **Summary:** The thread discusses novel methods for integrating linear optimization with Graph Neural Networks (GNNs). A user shared a survey on using GNNs for combinatorial optimization and another provided a paper using diffusion models to solve co problems without using solution data during training.
*  **Emotion:** The emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * GNNs can be used for combinatorial optimization problems.
    * Diffusion models can be parameterized by GNNs for unsupervised neural combinatorial optimization.
    * The discussion focuses on applying GNNs to both linear and combinatorial optimization problems.

**[[D] model architecture or data? (Score: 12)](https://www.reddit.com/r/MachineLearning/comments/1mrwm3w/d_model_architecture_or_data/)**
*  **Summary:**  The thread revolves around the significance of model architecture versus data in achieving success, especially with transformer models.  Users discussed the role of transformers in enabling the processing of large datasets, the importance of data augmentation, and the potential of fine-tuning strategies.
*  **Emotion:** The emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * Transformers are architecturally significant for enabling the processing of large datasets in a parallelizable and scalable manner.
    * Data augmentation is key, especially hard-coded augmentations that don't affect the label, although this might limit generalization.
    * Success may be a combination of pretraining on comprehensive data and fine-tuning on a high-quality subset.

**[[R] How do I choose the best model in validation when I have no target data?? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1mrqyni/r_how_do_i_choose_the_best_model_in_validation/)**
*  **Summary:**  A user asks for advice on how to select the best model during validation when no target data is available. A response claims that all models are ultimately trained in a supervised manner and suggests reusing the training error/cost function for testing.
*  **Emotion:** The emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    *  All models are trained as supervised models, even those considered unsupervised.
    *  The error/cost function used for training can be reused for evaluating the model during validation.
    *  The question stems from confusion about the nature of training and validation in the absence of explicitly labeled target data.
