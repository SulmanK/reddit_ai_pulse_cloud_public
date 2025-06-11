---
title: "Machine Learning Subreddit"
date: "2025-03-30"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "transformers", "time series"]
---

# Overall Ranking and Top Discussions
1.  [[R] [D] My (Mostly Failed) Attempt to Improve Transformers by Enriching Embeddings with the Last Hidden State – Why It Didn't Scale](https://www.reddit.com/r/MachineLearning/comments/1jn0ha9/r_d_my_mostly_failed_attempt_to_improve/) (Score: 129)
    * Discusses an attempt to improve Transformers by enriching embeddings with the last hidden state, detailing why it didn't scale.
2.  [[R] Text based backprop: Optimizing generative AI by backpropagating language model feedback](https://www.reddit.com/r/MachineLearning/comments/1jn7jvg/r_text_based_backprop_optimizing_generative_ai_by/) (Score: 15)
    * Discusses optimizing generative AI through backpropagating language model feedback.
3.  [[N] [P] Transformer model made with PHP](https://www.reddit.com/r/MachineLearning/comments/1jn11wq/n_p_transformer_model_made_with_php/) (Score: 8)
    * Presents a Transformer model built using PHP.
4.  [[D] Why is table extraction still not solved by modern multimodal models?](https://www.reddit.com/r/MachineLearning/comments/1jnjfaq/d_why_is_table_extraction_still_not_solved_by/) (Score: 4)
    *  Asks why table extraction is still a challenge for modern multimodal models.
5.  [[Discussion] Linear Regression performs better than LGBM or XGBoost on Time Series](https://www.reddit.com/r/MachineLearning/comments/1jneuix/discussion_linear_regression_performs_better_than/) (Score: 3)
    * Discusses the observation that Linear Regression can outperform LGBM or XGBoost in Time Series forecasting.

# Detailed Analysis by Thread
**[[R] [D] My (Mostly Failed) Attempt to Improve Transformers by Enriching Embeddings with the Last Hidden State – Why It Didn't Scale (Score: 129)](https://www.reddit.com/r/MachineLearning/comments/1jn0ha9/r_d_my_mostly_failed_attempt_to_improve/)**
*  **Summary:** The author details their attempt to improve Transformers by enriching embeddings with the last hidden state, explaining why the approach did not scale. The comments offer alternative methods for parallelizing training and debugging of the project.
*  **Emotion:** The emotional tone is largely Neutral, with some Positive sentiment expressed towards the author's detailed write-up and willingness to share a failed experiment. Some Negative sentiments are also present.
*  **Top 3 Points of View:**
    *   The approach may have failed due to model capacity issues, with the feedback loop causing the model to focus on noise.
    *   There are errors in the initial motivation, specifically regarding bit representation.
    *   Standard attention does allow communication between tokens but from only earlier layers and earlier tokens.

**[[R] Text based backprop: Optimizing generative AI by backpropagating language model feedback (Score: 15)](https://www.reddit.com/r/MachineLearning/comments/1jn7jvg/r_text_based_backprop_optimizing_generative_ai_by/)**
*  **Summary:** This thread discusses the concept of optimizing generative AI by using language model feedback in backpropagation.
*  **Emotion:** The emotional tone is Neutral.
*  **Top 3 Points of View:**
    *   One user asks for a link to the related paper.
    *   One user questions the statement that backpropagation transformed the field of neural networks, arguing that it was always present.

**[[N] [P] Transformer model made with PHP (Score: 8)](https://www.reddit.com/r/MachineLearning/comments/1jn11wq/n_p_transformer_model_made_with_php/)**
*  **Summary:** A user presents a Transformer model implemented in PHP, sparking discussions about the choice of language and its potential benefits.
*  **Emotion:** Overall, the thread exhibits a mix of Positive and Negative emotions. Some users express appreciation and support for the author's effort, while others question the practicality of using PHP for such a task.
*  **Top 3 Points of View:**
    *   PHP is not the most popular language, and the project might have received more attention if it were implemented in a different language like Rust.
    *   The project is valuable because it democratizes machine learning and makes it accessible to PHP developers.
    *   Some question why one would choose PHP over Python for machine learning tasks.

**[[D] Why is table extraction still not solved by modern multimodal models? (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1jnjfaq/d_why_is_table_extraction_still_not_solved_by/)**
*  **Summary:** This thread discusses the difficulties modern multimodal models face with table extraction.
*  **Emotion:** The overall emotional tone is Neutral, with a touch of Positive sentiment as users suggest solutions.
*  **Top 3 Points of View:**
    *   Training a model with synthetic data could be a solution. VLMs have trouble positioning parts of an image precisely.
    *   Fine-tuning is necessary for tasks where VLMs don't perform well out-of-the-box.
    *   Gemini 1.5 flash is a cheap and easy to use tool for table extraction.

**[[Discussion] Linear Regression performs better than LGBM or XGBoost on Time Series (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1jneuix/discussion_linear_regression_performs_better_than/)**
*  **Summary:** The thread discusses the observation that Linear Regression sometimes outperforms more complex models like LGBM or XGBoost in time series forecasting.
*  **Emotion:** The overall tone is Neutral, with some Positive sentiment.
*  **Top 3 Points of View:**
    *   Linear regression outperforming more complex models in time series forecasting is normal.
    *   ML options have only become competitive with statistical methods in the last few years, and only in certain scenarios.
    *   Ensembling different models might improve results.
