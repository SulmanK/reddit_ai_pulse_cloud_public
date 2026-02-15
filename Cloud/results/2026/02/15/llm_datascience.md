---
title: "Data Science Subreddit"
date: "2026-02-15"
description: "Analysis of top discussions and trends in the datascience subreddit"
tags: ["datascience", "machine learning", "salaries", "career"]
---

# Overall Ranking and Top Discussions
1.  [Best technique for training models on a sample of data?](https://www.reddit.com/r/datascience/comments/1r53jy3/best_technique_for_training_models_on_a_sample_of/) (Score: 20)
    *   Discussions focused on best practices for handling sampled data in machine learning, emphasizing that sampling should only occur on training sets, ideally within cross-validation, and that validation and test sets should retain their original distribution.
2.  [Outside the US, What is the avg salary someone can get in like Canada, UK, Germany or other countries? For early level](https://www.reddit.com/r/datascience/comments/1r4wfu9/outside_the_us_what_is_the_avg_salary_someone_can/) (Score: 0)
    *   Users shared insights and salary expectations for entry-level data science roles in various countries outside the US, comparing them to US salaries and highlighting regional differences.

# Detailed Analysis by Thread
**[Best technique for training models on a sample of data? (Score: 20)](https://www.reddit.com/r/datascience/comments/1r53jy3/best_technique_for_training_models_on_a_sample_of/)**
*   **Summary:** The thread discusses optimal strategies for training machine learning models using sampled data, particularly in scenarios involving class imbalance. Key advice includes applying sampling solely to the training dataset and within cross-validation folds, while leaving validation and test sets untouched to ensure accurate performance evaluation. Alternatives like subsampling the entire dataset, leveraging models capable of training from disk, and performing post-training calibration for probability accuracy are also explored.
*   **Emotion:** The overall emotional tone of the thread is predominantly **Neutral**. The discussion is highly technical and instructional, with users offering practical guidance, best practices, and cautionary advice on model training techniques. While one comment carries a slightly positive sentiment for suggesting a beneficial approach (treating the problem as a scoring problem with AUC), the general atmosphere remains objective and focused on problem-solving.
*   **Top 3 Points of View:**
    *   **Sampling should be strictly limited to the training dataset:** The most emphasized point is that sampling (e.g., undersampling) must only be applied to the training data, never to validation or test sets, which should retain their original, imbalanced distribution for realistic evaluation.
    *   **Integrate sampling within cross-validation (CV) folds:** Users advise performing any sampling procedure inside each cross-validation training fold, rather than upfront, to ensure robust model selection and evaluation.
    *   **Consider alternative approaches and calibration:** Suggestions include subsampling the entire dataset, utilizing models designed to train large datasets from disk, approaching problems as scoring rather than classification, and performing post-training calibration to correct predicted probabilities if sampling affects their accuracy.

**[Outside the US, What is the avg salary someone can get in like Canada, UK, Germany or other countries? For early level (Score: 0)](https://www.reddit.com/r/datascience/comments/1r4wfu9/outside_the_us_what_is_the_avg_salary_someone_can/)**
*   **Summary:** This thread explores early-career data science salaries outside the United States, with a focus on countries like Canada, the UK, and Germany. Contributors share salary ranges and observations, discussing how these figures compare to US salaries and noting the competitiveness of roles, particularly those for American companies operating internationally. Specific mentions include high potential earnings in Singapore and Persian Gulf countries.
*   **Emotion:** The emotional tone is primarily **Neutral**, as participants provide factual salary figures and market observations. There are elements of **Positive** sentiment when discussing particularly well-paying regions or specific opportunities, such as competitive roles for US companies in Canada, or the generally decent salaries in Canada compared to other non-US countries. The discussion is pragmatic and informative.
*   **Top 3 Points of View:**
    *   **Non-US salaries are generally lower than in the US, with specific ranges:** Users reported typical entry-level salaries in the UK (30-50k GBP) and Europe (around €50-55k), explicitly noting these are lower than comparable US junior analyst roles ($120-130k).
    *   **Canada offers relatively good salaries for non-US regions, especially with US-affiliated companies:** Canadian entry-level salaries typically range from $75K-$90K CAD, with highly competitive roles for American companies potentially reaching $170-250K TC (total compensation) in CAD.
    *   **Certain international regions are perceived to offer extremely high salaries:** Singapore and the Persian Gulf countries were highlighted as places where data scientists, even at early career levels, could expect significantly higher compensation.
