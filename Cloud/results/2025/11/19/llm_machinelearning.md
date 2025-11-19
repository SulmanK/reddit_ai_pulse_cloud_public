---
title: "Machine Learning Subreddit"
date: "2025-11-19"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "reddit", "analysis"]
---

# Overall Ranking and Top Discussions
1.  [[R] Segment Anything Model 3 (SAM 3) is released](https://www.reddit.com/r/MachineLearning/comments/1p1cfvx/r_segment_anything_model_3_sam_3_is_released/) (Score: 68)
    *   This thread discusses the release of Segment Anything Model 3 (SAM 3) and its integration into Roboflow.
2.  [[D] Spiking LR during pretraining](https://www.reddit.com/r/MachineLearning/comments/1p0sdo2/d_spiking_lr_during_pretraining/) (Score: 5)
    *   This thread discusses the learning rate (LR) during pretraining of a machine learning model, particularly the use of a "spiking" LR and alternative approaches.
3.  [Edge vs Cloud GPU Inference [D]](https://www.reddit.com/r/MachineLearning/comments/1p11yk0/edge_vs_cloud_gpu_inference_d/) (Score: 2)
    *   This thread briefly discusses the cost of GPU inference in the cloud versus using local hardware.
4.  [[D] Are probabilistic approaches to ML a research dead-end?](https://www.reddit.com/r/MachineLearning/comments/1p17iuw/d_are_probabilistic_approaches_to_ml_a_research/) (Score: 0)
    *   This thread discusses whether probabilistic approaches to machine learning are becoming obsolete, particularly in comparison to deep learning.
5.  [[D]After testing Veo vs Sora clips… I’m not sure which one “understands” video better](https://www.reddit.com/r/MachineLearning/comments/1p18r6y/dafter_testing_veo_vs_sora_clips_im_not_sure/) (Score: 0)
    *   This thread involves a comparison between Veo and Sora, two video generation models, questioning which one better understands video content.
6.  [[D] Scale-out is the silent killer of LLM applications. Are we solving the wrong problem?](https://www.reddit.com/r/MachineLearning/comments/1p18wg1/d_scaleout_is_the_silent_killer_of_llm/) (Score: 0)
    *   This thread explores the challenges of scaling out Large Language Model (LLM) applications and questions whether the current approach is effective.
7.  [[D] Human Annotations Needed?](https://www.reddit.com/r/MachineLearning/comments/1p1eqmn/d_human_annotations_needed/) (Score: 0)
    *   The need for human annotation is being discussed. It is important to ensure subjective judgements correlate with human sentiment analysis.

# Detailed Analysis by Thread
**[[R] Segment Anything Model 3 (SAM 3) is released (Score: 68)](https://www.reddit.com/r/MachineLearning/comments/1p1cfvx/r_segment_anything_model_3_sam_3_is_released/)**
*  **Summary:** The thread discusses the release of Segment Anything Model 3 (SAM 3). A Roboflow representative highlights its integration into their platform for tasks such as auto-labeling and fine-tuning.
*  **Emotion:** The overall emotional tone is mixed. While some express positivity about the model's capabilities (Positive: 0.45), others express sadness about layoffs at Meta affecting the team (Negative: 0.63). The overall sentiment can be considered slightly more towards neutral due to one neutral sentiment (Neutral: 0.79).
*  **Top 3 Points of View:**
    * SAM3 is a good model and is well-integrated into Roboflow's platform, enabling auto-labeling and fine-tuning.
    * SAM3 might simply be a software update instead of a completely new model.
    * It's unfortunate that Meta laid off people working on SAM.

**[[D] Spiking LR during pretraining (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1p0sdo2/d_spiking_lr_during_pretraining/)**
*  **Summary:** The thread discusses the appropriate learning rate (LR) strategies for pretraining machine learning models, particularly focusing on the use of "spiking" learning rates. Several users provide advice on LR schedules, optimizers, and related hyperparameters.
*  **Emotion:** The emotional tone is predominantly neutral, with all comments having neutral emotion labels. The discussion is technical and advisory, lacking strong positive or negative sentiments.
*  **Top 3 Points of View:**
    * A high peak LR (like 8e-3) is likely too high and should be reduced. LR warmup should be included.
    * Cosine LR schedule should be used
    * Matching Adam's update RMS norm for Muon updates allows for a single LR for both optimizers. A much lower LR should be used for Adam.

**[Edge vs Cloud GPU Inference [D] (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1p11yk0/edge_vs_cloud_gpu_inference_d/)**
*  **Summary:** This thread explores the economics of GPU inference, particularly comparing cloud-based solutions with owning local hardware (e.g., a used 3090).
*  **Emotion:** The emotional tone is neutral, with a score of 0.65.
*  **Top 3 Points of View:**
    * Cloud GPU inference at 1.5c/hr for an H200 is questioned, suggesting it might be more cost-effective to buy a used 3090.

**[[D] Are probabilistic approaches to ML a research dead-end? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1p17iuw/d_are_probabilistic_approaches_to_ml_a_research/)**
*  **Summary:** The thread revolves around the question of whether probabilistic approaches to Machine Learning are becoming less relevant, especially in the context of the rise of deep learning. The discussion explores different perspectives on the continued utility and research potential of probabilistic methods.
*  **Emotion:** The emotional tone is predominantly neutral. There are a couple negative sentements, but overall neutral.
*  **Top 3 Points of View:**
    * The entire discipline of Machine Learning is about estimating parameters, making it fundamentally statistical/probabilistic.
    * Deep learning/neural networks can be considered separate from probabilistic approaches.
    * Probabilistic techniques like GPRs are still used by engineers.

**[[D]After testing Veo vs Sora clips… I’m not sure which one “understands” video better (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1p18r6y/dafter_testing_veo_vs_sora_clips_im_not_sure/)**
*  **Summary:** The thread discusses the conceptual or semantic understanding of video by video generation models Veo and Sora.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Conceptual or semantic understanding of video is more important than raw physics.

**[[D] Scale-out is the silent killer of LLM applications. Are we solving the wrong problem? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1p18wg1/d_scaleout_is_the_silent_killer_of_llm/)**
*  **Summary:** The discussion is focused on the challenges of scaling out LLM applications, suggesting potential inefficiencies in the current approaches. Some users suggest caching CPU/GPU state.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * Caching the full relevant CPU/GPU system state after loading can be a solution to scaling LLMs.
    * Paying Databricks to handle the scaling problem.

**[[D] Human Annotations Needed? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1p1eqmn/d_human_annotations_needed/)**
*  **Summary:**  The discussion emphasizes the importance of correlating subjective AI analyses (such as sentiment analysis) with human judgement
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * It is important to show subjective type things (like sentiment analysis) correlate with human judgement.
