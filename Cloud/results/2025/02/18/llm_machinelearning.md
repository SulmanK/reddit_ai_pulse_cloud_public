---
title: "Machine Learning Subreddit"
date: "2025-02-18"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "AI", "LLM"]
---

# Overall Ranking and Top Discussions
1.  [[R] Evaluating LLMs on Real-World Software Engineering Tasks: A $1M Benchmark Study](https://www.reddit.com/r/MachineLearning/comments/1isbo6t/r_evaluating_llms_on_realworld_software/) (Score: 126)
    * Discusses the evaluation of Large Language Models (LLMs) on real-world software engineering tasks, referencing a $1M benchmark study.
2.  [[R] Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention (submitted by Liang  Wenfeng - DeepSeek)](https://www.reddit.com/r/MachineLearning/comments/1is9ufs/r_native_sparse_attention_hardwarealigned_and/) (Score: 60)
    *  Discusses native sparse attention, which is hardware-aligned and natively trainable.
3.  [[R] The Curse of Depth in Large Language Models](https://www.reddit.com/r/MachineLearning/comments/1isdopn/r_the_curse_of_depth_in_large_language_models/) (Score: 40)
    * Discusses the potential problems that could occur with large language models.
4.  [[D] Finetuning ModernBERT is taking 3hrs (2 epochs) and 35gigs of vram. is it normal?](https://www.reddit.com/r/MachineLearning/comments/1is0q1a/d_finetuning_modernbert_is_taking_3hrs_2_epochs/) (Score: 21)
    * Asks if the time and vram usage taken to finetune ModernBERT is normal.
5.  [[D] How AISTATS/UAI/TMLR is viewed when applied for industry job?](https://www.reddit.com/r/MachineLearning/comments/1is3c39/d_how_aistatsuaitmlr_is_viewed_when_applied_for/) (Score: 4)
    * Question about how AISTATS/UAI/TMLR conferences are viewed when applying for industry jobs.
6.  [[R] Membership Inference Attacks for Face Images Against Fine-Tuned Latent Diffusion Models](https://www.reddit.com/r/MachineLearning/comments/1isa46f/r_membership_inference_attacks_for_face_images/) (Score: 3)
    * Discusses membership inference attacks for face images against fine-tuned latent diffusion models.
7.  [built a chrome extension to read arXiv papers 2x faster [P]](https://www.reddit.com/r/MachineLearning/comments/1irwcii/built_a_chrome_extension_to_read_arxiv_papers_2x/) (Score: 0)
    * Discussion about a chrome extension built to read arXiv papers faster
8.  [[D] Is It Okay to Train and Compare Models Without a Benchmark Dataset?](https://www.reddit.com/r/MachineLearning/comments/1is1sbg/d_is_it_okay_to_train_and_compare_models_without/) (Score: 0)
    * Asks if it is okay to train and compare models without a benchmark dataset.

# Detailed Analysis by Thread
**[[R] Evaluating LLMs on Real-World Software Engineering Tasks: A $1M Benchmark Study (Score: 126)](https://www.reddit.com/r/MachineLearning/comments/1isbo6t/r_evaluating_llms_on_realworld_software/)**
*   **Summary:**  Evaluating Large Language Models (LLMs) on real-world software engineering tasks, referencing a $1M benchmark study.  The discussion includes whether LLMs can replace mid-level engineers, the performance of coding tasks when working against an existing large codebase, and the accuracy of newer models.
*   **Emotion:** The emotional tone is largely Neutral, with some instances of Positive and Negative sentiment.
*   **Top 3 Points of View:**
    * LLMs may not be ready to replace mid-level engineers.
    * Newer models perform better on coding tasks than the models used in the study.
    * Concern that OpenAI might manipulate results to create hype.

**[[R] Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention (Score: 60)](https://www.reddit.com/r/MachineLearning/comments/1is9ufs/r_native_sparse_attention_hardwarealigned_and/)**
*   **Summary:**  Discusses native sparse attention, which is hardware-aligned and natively trainable, submitted by Liang Wenfeng from DeepSeek. The discussion also notes that dense attention might not be the best way to do attention long term.
*   **Emotion:** The emotional tone is largely Neutral, with some instances of Positive sentiment.
*   **Top 3 Points of View:**
    * Sparse attention that adapts to hardware is promising.
    * DeepSeek is producing high-quality research.
    * It is questioned if this can replace an attention layer in PyTorch.

**[[R] The Curse of Depth in Large Language Models (Score: 40)](https://www.reddit.com/r/MachineLearning/comments/1isdopn/r_the_curse_of_depth_in_large_language_models/)**
*   **Summary:**  Discussion about an architectural modification of the transformer that adds dense skip connections to the key and value projections from earlier layers. The weights of the skip connections from the earliest layers tend to have higher weights for values rather than the keys.
*   **Emotion:** The emotional tone is largely Neutral, with some instances of Positive sentiment.
*   **Top 3 Points of View:**
    * Skip connections from the earliest layers tend to have higher weights.
    * The problem may be a non-issue with weight normalization.

**[[D] Finetuning ModernBERT is taking 3hrs (2 epochs) and 35gigs of vram. is it normal? (Score: 21)](https://www.reddit.com/r/MachineLearning/comments/1is0q1a/d_finetuning_modernbert_is_taking_3hrs_2_epochs/)**
*   **Summary:**  Asks if the time and vram usage taken to finetune ModernBERT is normal. Some tricks to consider when using HF Trainer are FP16 or BF16 and gradient accumulation.
*   **Emotion:** The emotional tone is largely Neutral.
*   **Top 3 Points of View:**
    * The model may only be loaded into the CPU. A param like device\_map="auto" can make the difference.
    * When doing FP32 training with 8192 sequence length, there is a lot of memory usage. Some tricks to consider when using HF Trainer are FP16 or BF16 and gradient accumulation.
    * You can try using adaptive classifier

**[[D] How AISTATS/UAI/TMLR is viewed when applied for industry job? (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1is3c39/d_how_aistatsuaitmlr_is_viewed_when_applied_for/)**
*   **Summary:**  Question about how AISTATS/UAI/TMLR conferences are viewed when applying for industry jobs.
*   **Emotion:** The emotional tone is largely Neutral.
*   **Top 3 Points of View:**
    * They will be viewed in a positive light in any place other than say top 5 companies/labs.

**[[R] Membership Inference Attacks for Face Images Against Fine-Tuned Latent Diffusion Models (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1isa46f/r_membership_inference_attacks_for_face_images/)**
*   **Summary:**  Discusses membership inference attacks for face images against fine-tuned latent diffusion models.
*   **Emotion:** The emotional tone is largely Neutral.
*   **Top 3 Points of View:**
    * How does this method perform when considering test-time conditioning methods (e.g. IP-Adapter)?
    * How does it perform on similar but disjointed datasets?

**[built a chrome extension to read arXiv papers 2x faster [P] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1irwcii/built_a_chrome_extension_to_read_arxiv_papers_2x/)**
*   **Summary:**  Discussion about a chrome extension built to read arXiv papers faster
*   **Emotion:** The emotional tone is largely Neutral.
*   **Top 3 Points of View:**
    * Doesn't seem like it's available

**[[D] Is It Okay to Train and Compare Models Without a Benchmark Dataset? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1is1sbg/d_is_it_okay_to_train_and_compare_models_without/)**
*   **Summary:**  Asks if it is okay to train and compare models without a benchmark dataset.
*   **Emotion:** The emotional tone is largely Neutral, with some instances of Positive and Negative sentiment.
*   **Top 3 Points of View:**
    * It is normal, and you should retrain and compare other approaches on your new dataset.
    * Without benchmark there is little value.
    * An external benchmark dataset would be a good idea for a paper implementation.
