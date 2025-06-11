---
title: "Machine Learning Subreddit"
date: "2025-04-16"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "AI", "TPU"]
---

# Overall Ranking and Top Discussions
1.  [[D] Google just released a new generation of TPUs. Who actually uses TPUs in production?](https://www.reddit.com/r/MachineLearning/comments/1k0fg57/d_google_just_released_a_new_generation_of_tpus/) (Score: 88)
    * Discussing which companies use Google's TPUs in production and for what purposes.
2.  [[R] Beyond-NanoGPT: Go From LLM Noob to AI Researcher!](https://www.reddit.com/r/MachineLearning/comments/1k0npdk/r_beyondnanogpt_go_from_llm_noob_to_ai_researcher/) (Score: 37)
    *  Sharing resources and expressing gratitude for a guide aimed at helping people learn about LLMs and AI research.
3.  [[D] ACL 2025 Meta Reviews Discussion](https://www.reddit.com/r/MachineLearning/comments/1k0a3r7/d_acl_2025_meta_reviews_discussion/) (Score: 31)
    *  Discussing experiences and frustrations with the ACL 2025 meta-review process, including concerns about reviewer understanding and the impact on paper acceptance.
4.  [[D] Contrastive Learning (SimCLR, MoCo) vs. Non-Contrastive Pretext Tasks (Rotation, Inpainting): When/Why Does One Approach Dominate?](https://www.reddit.com/r/MachineLearning/comments/1k0fbvq/d_contrastive_learning_simclr_moco_vs/) (Score: 4)
    *  Comparing contrastive learning approaches like SimCLR and MoCo with non-contrastive pretext tasks and discussing when each approach is more effective.
5.  [[P] I fine-tuned GPT-2 and GPT-J to mimic Mr. Darcy. Results were a mixture of promising and strange.](https://www.reddit.com/r/MachineLearning/comments/1k03i0k/p_i_finetuned_gpt2_and_gptj_to_mimic_mr_darcy/) (Score: 2)
    * Sharing a project where GPT-2 and GPT-J were fine-tuned to mimic Mr. Darcy's writing style, with mixed results.
6.  [[P] How and should I use Deepgaze pytorch? - Saliency Maps](https://www.reddit.com/r/MachineLearning/comments/1k040es/p_how_and_should_i_use_deepgaze_pytorch_saliency/) (Score: 1)
    *  Asking for advice on how to use Deepgaze pytorch for saliency maps.
7.  [[P] Releasing RepAlignLoss (Custom Perceptual loss function used on my software)](https://www.reddit.com/r/MachineLearning/comments/1k0qfhi/p_releasing_repalignloss_custom_perceptual_loss/) (Score: 1)
    *  Sharing a custom perceptual loss function and providing a link to the associated paper.
8.  [MODE: A Lightweight TraditionalRAG Alternative (Looking for arXiv Endorsement) [P]](https://www.reddit.com/r/MachineLearning/comments/1k0dov1/mode_a_lightweight_traditionalrag_alternative/) (Score: 0)
    *  Seeking arXiv endorsement for a lightweight RAG alternative, but receiving advice that this is not the appropriate place for such requests.
9.  [[D]Mistake accesor model](https://www.reddit.com/r/MachineLearning/comments/1k0fx5b/dmistake_accesor_model/) (Score: 0)
    *  Discussing questions about how you are going to come up with ground truth penalties for ranch kind of mistake and why you train a secondary model instead of just incorporating this training into the LLM itself?

# Detailed Analysis by Thread
**[[D] Google just released a new generation of TPUs. Who actually uses TPUs in production? (Score: 88)](https://www.reddit.com/r/MachineLearning/comments/1k0fg57/d_google_just_released_a_new_generation_of_tpus/)**
*  **Summary:** The thread discusses which companies are using Google's TPUs in production. Users mention companies like Apple, DeepMind, and Anthropic as well as startups and big companies using them on edge devices. There are also discussions on TPUs scaling better than GPUs for training.
*  **Emotion:** The overall emotional tone of the thread is neutral, with a mix of informative statements and questions. Some negative sentiment is expressed about difficulties experienced using TPUs.
*  **Top 3 Points of View:**
    *   Several large companies and startups are using TPUs in production for various purposes, including LLM inference and edge devices.
    *   TPUs scale better than GPUs for training large models, making them advantageous for certain use cases.
    *   Vendor lock-in is not a major issue for TPUs because models are generally portable, although CUDA ecosystem lock-in can be a hurdle.

**[[R] Beyond-NanoGPT: Go From LLM Noob to AI Researcher! (Score: 37)](https://www.reddit.com/r/MachineLearning/comments/1k0npdk/r_beyondnanogpt_go_from_llm_noob_to_ai_researcher/)**
*  **Summary:** The thread is centered around users expressing gratitude for a resource called "Beyond-NanoGPT" which is aimed at helping people learn about LLMs and become AI researchers. Some users are asking for advice on getting started with NanoGPT.
*  **Emotion:** The overall emotional tone is positive, with expressions of gratitude and excitement about the resource being shared.
*  **Top 3 Points of View:**
    *   The resource "Beyond-NanoGPT" is valuable for aspiring AI researchers.
    *   There is a concern about the job market for ML engineers, with some questioning the possibility of needing published papers to secure employment.
    *   Some users are seeking guidance on where to start with NanoGPT.

**[[D] ACL 2025 Meta Reviews Discussion (Score: 31)](https://www.reddit.com/r/MachineLearning/comments/1k0a3r7/d_acl_2025_meta_reviews_discussion/)**
*  **Summary:** This thread is a discussion about experiences with the ACL 2025 meta-review process. Many users express frustration and disappointment with the quality of reviews and meta-reviews, with some suspecting reviewers did not fully understand their papers. Some users are concerned about low meta-review scores impacting their chances of acceptance.
*  **Emotion:** The dominant emotion is negative, with expressions of disappointment, frustration, and concern about the quality and fairness of the review process.
*  **Top 3 Points of View:**
    *   The quality of ACL reviewers and meta-reviewers is perceived as low by some participants.
    *   Meta-reviews are not always aligned with the individual reviewer scores and rebuttals.
    *   Low meta-review scores are causing anxiety about paper acceptance.

**[[D] Contrastive Learning (SimCLR, MoCo) vs. Non-Contrastive Pretext Tasks (Rotation, Inpainting): When/Why Does One Approach Dominate? (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1k0fbvq/d_contrastive_learning_simclr_moco_vs/)**
*  **Summary:** The thread discusses contrastive learning approaches and non-contrastive pretext tasks, focusing on which approaches dominate and when. The Dino V2 model is mentioned as a current winner using contrastive learning with masked token prediction.
*  **Emotion:** The tone is mostly neutral and informative.
*  **Top 3 Points of View:**
    *   Contrastive learning has largely replaced pretext tasks, even in fields like medical image processing.
    *   Dino V2 model is the current state-of-the-art for SSL.
    *   The next word prediction version of images is an unsolved problem.

**[[P] I fine-tuned GPT-2 and GPT-J to mimic Mr. Darcy. Results were a mixture of promising and strange. (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1k03i0k/p_i_finetuned_gpt2_and_gptj_to_mimic_mr_darcy/)**
*  **Summary:** The author shares a project where they fine-tuned GPT-2 and GPT-J to mimic the writing style of Mr. Darcy. A commenter describes their method of creating an AI with a certain personality that involves a reasoning model to determine the basis of reasoning of the person being mimicked.
*  **Emotion:** The overall tone is neutral with some curiosity.
*  **Top 3 Points of View:**
    *   Mimicking a person's style involves understanding their reasoning and thinking process, not just their writing style.
    *   Using a reasoning model to identify traits and generate reasoning samples is a useful approach.
    *   Quantitatively judging performance is difficult in personality mimicking projects.

**[[P] How and should I use Deepgaze pytorch? - Saliency Maps (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1k040es/p_how_and_should_i_use_deepgaze_pytorch_saliency/)**
*  **Summary:** The user is asking for guidance on how to use Deepgaze pytorch for saliency maps.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   Instead of trying to build from the repo, clone it, load the model and export it to torchscript.

**[[P] Releasing RepAlignLoss (Custom Perceptual loss function used on my software) (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1k0qfhi/p_releasing_repalignloss_custom_perceptual_loss/)**
*  **Summary:** The user is sharing their custom perceptual loss function, RepAlignLoss and providing a link to the associated paper.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   The linked Github is the project repository.

**[MODE: A Lightweight TraditionalRAG Alternative (Looking for arXiv Endorsement) [P] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1k0dov1/mode_a_lightweight_traditionalrag_alternative/)**
*  **Summary:** The user is looking for arXiv endorsement.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   This is not the place for arXiv endorsement.

**[[D]Mistake accesor model (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1k0fx5b/dmistake_accesor_model/)**
*  **Summary:** This thread discusses how to come up with ground truth penalties for ranch kind of mistakes and why to train a secondary model instead of just incorporating this training into the LLM itself.
*  **Emotion:** The overall tone is neutral.
*  **Top 3 Points of View:**
    *   How are you going to come up with ground truth penalties for ranch kind of mistake?
    *   Why train a secondary model instead of just incorporating this training into the LLM itself?
