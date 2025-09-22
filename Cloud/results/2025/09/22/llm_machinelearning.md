---
title: "Machine Learning Subreddit"
date: "2025-09-22"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[D] Is non-DL related research a poor fit for ICLR?](https://www.reddit.com/r/MachineLearning/comments/1nn56yu/d_is_nondl_related_research_a_poor_fit_for_iclr/) (Score: 34)
    * The discussion revolves around whether non-Deep Learning research is suitable for the International Conference on Learning Representations (ICLR), with opinions varying on the relevance and review quality of different conferences.
2.  [[D] Is it reasonable that reviewers aren’t required to read the appendix?](https://www.reddit.com/r/MachineLearning/comments/1nnhkz8/d_is_it_reasonable_that_reviewers_arent_required/) (Score: 20)
    * This thread discusses the reasonableness of reviewers not being required to read the appendix of research papers.
3.  [[D] Best practice for providing code during review](https://www.reddit.com/r/MachineLearning/comments/1nni5ld/d_best_practice_for_providing_code_during_review/) (Score: 11)
    *  The discussion centers on the best practices for providing code during the review process for machine learning papers, including the use of anonymous repositories and zipped files.
4.  [[D] Mixture of Attention?](https://www.reddit.com/r/MachineLearning/comments/1nnh6gi/d_mixture_of_attention/) (Score: 4)
    * The discussion focuses on the intuition of Large Language Models and the use of Mixture of Experts in the MLP layer of transformer blocks.
5.  [[D] Semantic image synthesis state-of-the-art?](https://www.reddit.com/r/MachineLearning/comments/1nngswn/d_semantic_image_synthesis_stateoftheart/) (Score: 2)
    *  This thread is about the current state-of-the-art methods for semantic image synthesis.
6.  [[D] Implement Mamba from scratch or use the official github repo?](https://www.reddit.com/r/MachineLearning/comments/1nnlas0/d_implement_mamba_from_scratch_or_use_the/) (Score: 1)
    * The discussion asks whether to implement Mamba from scratch or use the official GitHub repo.
7.  [[D] experiment analysis workflow with wandb or mlflow](https://www.reddit.com/r/MachineLearning/comments/1nnig4r/d_experiment_analysis_workflow_with_wandb_or/) (Score: 0)
    * This thread discusses experiment analysis workflow with Weights & Biases (wandb) or MLflow
8.  [[D] Handwritten OCR GOAT?](https://www.reddit.com/r/MachineLearning/comments/1nnr8lz/d_handwritten_ocr_goat/) (Score: 0)
    * This thread is about finding the best Handwritten Optical Character Recognition (OCR) model.
9.  [[D] Multi Task Learning](https://www.reddit.com/r/MachineLearning/comments/1nnull7/d_multi_task_learning/) (Score: 0)
    * The discussion is about Multi-Task Learning (MTL) and its potential benefits and drawbacks in different scenarios.

# Detailed Analysis by Thread
**[ [D] Is non-DL related research a poor fit for ICLR? (Score: 34)](https://www.reddit.com/r/MachineLearning/comments/1nn56yu/d_is_nondl_related_research_a_poor_fit_for_iclr/)**
*  **Summary:** The thread discusses whether research not directly related to Deep Learning (non-DL) is a good fit for the International Conference on Learning Representations (ICLR). Some believe ICLR is still a good venue for broader machine learning research, while others suggest alternatives like AISTATS. The quality of reviews at ICLR, ICML, and NeurIPS is also questioned.
*  **Emotion:** The overall emotional tone is neutral, with some comments expressing positive sentiment about specific conferences.
*  **Top 3 Points of View:**
    *   ICLR, NeurIPS, and ICML are essentially the same in terms of reviewers and paper quality.
    *   AISTATS is a good alternative for non-DL related research.
    *   Paper and review quality at ICLR, ICML, and NeurIPS has declined.

**[ [D] Is it reasonable that reviewers aren’t required to read the appendix? (Score: 20)](https://www.reddit.com/r/MachineLearning/comments/1nnhkz8/d_is_it_reasonable_that_reviewers_arent_required/)**
*  **Summary:**  The thread discusses the reasonableness of reviewers not being required to read the appendix of research papers. The general consensus is that the appendix should contain supplementary material, and reviewers shouldn't be expected to sift through excessively long appendices.
*  **Emotion:** The overall emotional tone is neutral to positive, with some negative sentiment expressed by reviewers who dislike important information being placed in the appendix.
*  **Top 3 Points of View:**
    *   The appendix should contain supplementary material, and the main paper should stand alone.
    *   Reviewers can't reasonably be expected to read lengthy appendices.
    *   Important information should not be placed in the appendix to circumvent page limits.

**[ [D] Best practice for providing code during review (Score: 11)](https://www.reddit.com/r/MachineLearning/comments/1nni5ld/d_best_practice_for_providing_code_during_review/)**
*  **Summary:** The discussion is about the best ways to provide code for reviewers, including using anonymous GitHub repositories or zipped files. Some prefer anonymous GitHub repos for their UI, while others suggest zipped files to prevent modifications after submission.
*  **Emotion:** The overall emotional tone is neutral, with some positive sentiment towards using anonymous repos.
*  **Top 3 Points of View:**
    *   Anonymous GitHub repositories are convenient due to their UI.
    *   Zipped files prevent modifications after submission.
    *   Making anonymous accounts for code sharing is helpful.

**[ [D] Mixture of Attention? (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1nnh6gi/d_mixture_of_attention/)**
*  **Summary:** So far as we know, the intuition about LLMs is that the MLP layer of a transformer block does the “memorizing” knowledge, so MoE is extensively used at that position. MoE doesn’t seem anywhere near that effective for the attention block.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   MLP layer of a transformer block does the “memorizing” knowledge.

**[ [D] Semantic image synthesis state-of-the-art? (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1nngswn/d_semantic_image_synthesis_stateoftheart/)**
*  **Summary:** Maybe not the best, but if you already have skeleton images, then you could train a controlNet and fine-tune a stable diffusion denoiser for that? the original controlNet paper had examples with semantic segmentation maps.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Train a controlNet and fine-tune a stable diffusion denoiser.

**[ [D] Implement Mamba from scratch or use the official github repo? (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1nnlas0/d_implement_mamba_from_scratch_or_use_the/)**
*  **Summary:** Community consensus is to use the public repo. Not sure why you wouldnt at least start from there even if you wanted to have a modified implementation to be honest. Implementing the kernel is certainly no joke and wouldnt be recommended unless you really knew what you were doing.
*  **Emotion:** The overall emotional tone is neutral to positive.
*  **Top 3 Points of View:**
    *   Start from the public repo.
    *   Consider using the HuggingFace model.

**[ [D] experiment analysis workflow with wandb or mlflow (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1nnig4r/d_experiment_analysis_workflow_with_wandb_or/)**
*  **Summary:** User agrees it’s suboptimal especially since fetching data from multiple runs is slow in a similar mlflow workflow.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Fetching data from multiple runs is slow.

**[ [D] Handwritten OCR GOAT? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1nnr8lz/d_handwritten_ocr_goat/)**
*  **Summary:** AI is not magic. It doesn't predict the future or intuit dark secrets of the page that the annotation process can't see.
*  **Emotion:** The overall emotional tone is neutral to positive.
*  **Top 3 Points of View:**
    *   Azure OCR is a good platform.
    *   Try parseextract.com.

**[ [D] Multi Task Learning (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1nnull7/d_multi_task_learning/)**
*  **Summary:** I don't know much about MTL, but from an architecture perspective, wouldn't you want to decouple those tasks into standalone modules in a production environment for easier maintenance/replacement/advancement/extension?
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Decouple those tasks into standalone modules in a production environment for easier maintenance/replacement/advancement/extension.
