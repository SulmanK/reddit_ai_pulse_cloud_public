---
title: "Machine Learning Subreddit"
date: "2025-07-23"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "NeurIPS", "VAE"]
---

# Overall Ranking and Top Discussions
1.  [[D] - NeurIPS'2025 Reviews](https://www.reddit.com/r/MachineLearning/comments/1m74ugv/d_neurips2025_reviews/) (Score: 87)
    *   Users are discussing the NeurIPS 2025 review process, anxiety surrounding the reviews, and timelines for results.
2.  [[D] Training VAE for Stable Diffusion 1.5 from scratch](https://www.reddit.com/r/MachineLearning/comments/1m6y8uv/d_training_vae_for_stable_diffusion_15_from/) (Score: 17)
    *   Users are discussing the process of training a VAE for Stable Diffusion 1.5 from scratch, focusing on loss functions, weighting terms, and potential artifacts.
3.  [[D] problems with pytorch's mps backend](https://www.reddit.com/r/MachineLearning/comments/1m7ixro/d_problems_with_pytorchs_mps_backend/) (Score: 3)
    *   A user is asking for help with some problems they encountered using PyTorch's MPS backend.
4.  [[D]Coupling between normalization, projection, KL divergence and adaptive feedback. Interesting or not?](https://www.reddit.com/r/MachineLearning/comments/1m7c1vc/dcoupling_between_normalization_projection_kl/) (Score: 2)
    *   A user is asking if their idea of coupling normalization, projection, KL divergence, and adaptive feedback is interesting.
5.  [[D] UK grants for ML research?](https://www.reddit.com/r/MachineLearning/comments/1m6yo7a/d_uk_grants_for_ml_research/) (Score: 0)
    *   A user is asking about available UK grants for Machine Learning research.

# Detailed Analysis by Thread
**[ [D] - NeurIPS'2025 Reviews (Score: 87)](https://www.reddit.com/r/MachineLearning/comments/1m74ugv/d_neurips2025_reviews/)**
*  **Summary:** The thread focuses on the upcoming NeurIPS 2025 reviews, including anxieties related to the review process, discussion of scoring (1-6 instead of 1-10 this year), coping mechanisms for stress, and speculation about the timing of the review release.
*  **Emotion:** The overall emotional tone is neutral, with some spikes of negative sentiment related to anxiety about the review outcomes and positive sentiment with users crossing their fingers.
*  **Top 3 Points of View:**
    *   Anxiety and stress are high among those awaiting NeurIPS reviews.
    *   The reviewer scoring system this year is different (1-6) than in previous years.
    *   A new community (r/Neurips_2025) has been created for discussions related to NeurIPS 2025.

**[[D] Training VAE for Stable Diffusion 1.5 from scratch (Score: 17)](https://www.reddit.com/r/MachineLearning/comments/1m6y8uv/d_training_vae_for_stable_diffusion_15_from/)**
*  **Summary:** The thread discusses the challenges and best practices of training a VAE for Stable Diffusion 1.5 from scratch. Topics include the importance of the weighting term in the loss function, the specific type of VAE used in SD (VQGAN), and the use of L1 loss with LPIPS regularization instead of MSE.
*  **Emotion:** The overall emotional tone is neutral, focusing on technical aspects of training.
*  **Top 3 Points of View:**
    *   The weighting term for the loss function is crucial for balancing reconstruction and KL divergence.
    *   Stable Diffusion uses a VQGAN, not a traditional VAE.
    *   L1 loss with LPIPS regularization is preferred over MSE for image reconstruction.

**[[D] problems with pytorch's mps backend (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1m7ixro/d_problems_with_pytorchs_mps_backend/)**
*  **Summary:** A user is asking for help regarding issues with the Pytorch's MPS backend. The suggestion is that the original user should be more specific.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   The MPS backend doesn't support float64.
    *   Some matrix based operations fall back to a CPU implementation.

**[[D]Coupling between normalization, projection, KL divergence and adaptive feedback. Interesting or not? (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1m7c1vc/dcoupling_between_normalization_projection_kl/)**
*  **Summary:** The thread is about whether coupling normalization, projection, KL divergence and adaptive feedback is interesting. Some users suggest it could be a more sophisticated version of batchnorm/layernorm.
*  **Emotion:** The overall emotional tone is neutral/positive.
*  **Top 3 Points of View:**
    *   It could be a more sophisticated version of batchnorm/layernorm.
    *   The crucial test for this is whether it helps in realistic situations.
    *   It seems like adding an extra error term with extra steps.

**[[D] UK grants for ML research? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1m6yo7a/d_uk_grants_for_ml_research/)**
*  **Summary:** A user asks about available UK grants for ML research. The response gives a link to a website with government grants and suggests that InnovateUK funder may be relevant for businesses, potentially requiring an academic partner.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   UKRI is a good resource for government grants for academic organizations.
    *   InnovateUK is relevant for businesses, potentially requiring an academic partner.
