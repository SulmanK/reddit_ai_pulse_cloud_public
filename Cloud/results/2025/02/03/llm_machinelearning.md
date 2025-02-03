---
title: "Machine Learning Subreddit"
date: "2025-02-03"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "LLMs", "model performance"]
---

# Overall Ranking and Top Discussions
1.  [[D] [P] Measuring model performance when training from inaccurate labels](https://www.reddit.com/r/MachineLearning/comments/1igi8nu/d_p_measuring_model_performance_when_training/) (Score: 3)
    *   The discussion focused on the challenges of evaluating model performance when training data has inaccurate labels, particularly in fraud and financial crime prevention.
2.  [[D] Why can't we skip RL for LLMs and just allow them to generate extra tokens when training the base model?](https://www.reddit.com/r/MachineLearning/comments/1igttby/d_why_cant_we_skip_rl_for_llms_and_just_allow/) (Score: 0)
    *   The discussion revolved around why Reinforcement Learning (RL) is considered necessary for training Large Language Models (LLMs) instead of allowing models to simply generate extra tokens during training.
3.  [[D] Should I keep AAC-encoded audio for deepfake training or convert to WAV?](https://www.reddit.com/r/MachineLearning/comments/1igolkt/d_should_i_keep_aacencoded_audio_for_deepfake/) (Score: 0)
    *   The discussion was about whether to use AAC-encoded audio files or convert them to WAV format when training deepfake models.

# Detailed Analysis by Thread
**[[D] [P] Measuring model performance when training from inaccurate labels (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1igi8nu/d_p_measuring_model_performance_when_training/)**
*   **Summary:** This thread discusses methods to evaluate model performance when training with inaccurate labels, with specific examples from fraud and financial crime prevention. Participants share strategies like testing on old labels, using correlated metrics, label spreading, and expert validation.
*   **Emotion:** The overall emotional tone of the thread is Neutral. The sentiment scores of the comments are all relatively high, without strong negative or positive emotions, indicating an objective and technical discussion.
*   **Top 3 Points of View:**
    *   Testing model performance on old labels, correlated properties, or a subset of more confident labels can help validate model performance when ground truth is unavailable.
    *  Techniques like Label Spreading and Propagation can help identify new instances of bad behavior.
    *  Multi-Instance Learning can be useful, and while an accuracy cannot be calculated without a ground truth, you can still look at the individual predictions and see if they're sensible.

**[[D] Why can't we skip RL for LLMs and just allow them to generate extra tokens when training the base model? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1igttby/d_why_cant_we_skip_rl_for_llms_and_just_allow/)**
*   **Summary:** The thread explores the rationale behind the use of Reinforcement Learning (RL) for LLMs, questioning why they can't just generate extra tokens during training. The discussion highlights the importance of parallel decoding, teacher forcing, and how RL facilitates learning from negative examples.
*  **Emotion:** The overall emotional tone of the thread is Neutral. The sentiment scores of the comments are mostly neutral, indicating an informational discussion and the tone is more of an inquisitive one.
*   **Top 3 Points of View:**
    *   Pre-training efficiency comes from parallel decoding and teacher forcing, allowing training on all tokens in a sequence simultaneously.
    *   RL is needed to learn from negative examples, which cannot be achieved through standard next token prediction.
    *  There is research using  RNNs to reason through multiple steps using the hidden state and backprop through time, which does not involve RL or output tokens, and they are able to train on small mazes and generalize to extremely large mazes.

**[[D] Should I keep AAC-encoded audio for deepfake training or convert to WAV? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1igolkt/d_should_i_keep_aacencoded_audio_for_deepfake/)**
*   **Summary:**  The thread addresses the question of whether to convert AAC-encoded audio to WAV for deepfake training. The main point is that lossless conversions don't introduce artifacts, and models that can handle lossy files are converting them internally anyway.
*  **Emotion:** The overall emotional tone of the thread is Neutral. The sentiment scores are positive, indicating agreement and an informational exchange.
*   **Top 3 Points of View:**
    *   Converting to lossless formats (like WAV) from lossy formats (like AAC) does not introduce new artifacts.
    *   If models can handle lossy compressed files, they are likely converting them internally.
    *   Downsampling during conversions should be avoided to prevent information loss.
