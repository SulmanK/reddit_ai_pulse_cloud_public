---
title: "Machine Learning Subreddit"
date: "2025-01-31"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "AI", "deep learning"]
---

# Overall Ranking and Top Discussions
1.  [[D] DeepSeek? Schmidhuber did it first.](https://www.reddit.com/gallery/1ielwh5) (Score: 181)
    *   The thread discusses the contributions of Jürgen Schmidhuber in the field of machine learning, particularly in relation to DeepSeek's work. There's a debate on whether he receives enough credit and if DeepSeek's work is truly novel.
2.  [[D] Non-deterministic behavior of LLMs when temperature is 0](https://www.reddit.com/r/MachineLearning/comments/1ie15ev/d_nondeterministic_behavior_of_llms_when/) (Score: 129)
    *   Users are discussing the reasons behind the non-deterministic behavior of Large Language Models (LLMs) even when the temperature parameter is set to zero. Various theories are being explored, including GPU errors, Mixture-of-Experts models, and batching issues.
3.  Why does the DeepSeek student model (7B parameters) perform slightly better than the teacher model (671B parameters)? [D](https://www.reddit.com/r/MachineLearning/comments/1ie46nq/why_does_the_deepseek_student_model_7b_parameters/) (Score: 79)
    *   The discussion revolves around why a smaller student model might outperform its larger teacher model in the context of DeepSeek. Theories such as knowledge distillation, teacher overfitting, and the quality of data are debated.
4.  [R] Fully open source codebase to train SOTA VLMs](https://www.reddit.com/r/MachineLearning/comments/1ieh3e3/r_fully_open_source_codebase_to_train_sota_vlms/) (Score: 42)
     * This thread discusses a fully open-source codebase for training state-of-the-art vision language models (VLMs), with questions about the training time and acknowledgements for the effort.
5.  [Discussion] Reproducibility in reporting Performance and Benchmarks](https://www.reddit.com/r/MachineLearning/comments/1iei30l/discussion_reproducibility_in_reporting/) (Score: 12)
    *   This is a discussion thread where users share their frustrations regarding the lack of reproducibility in machine learning papers and the importance of open-source code.
6.  [P] Interactive Explanation to ROC AUC Score](https://www.reddit.com/r/MachineLearning/comments/1iem7bq/p_interactive_explanation_to_roc_auc_score/) (Score: 10)
    *  This thread discusses an interactive blog post that explains the ROC AUC score, with some users finding the interactivity useful.
7.  [R] Classification: Image with imprint](https://www.reddit.com/r/MachineLearning/comments/1iee8mi/r_classification_image_with_imprint/) (Score: 3)
    *   This thread discusses how to measure a model in the context of image classification with imprint, suggesting the user needs a comparable number of counterfeit images.
8.   [D] Does all distillation only use soft labels (probability distribution)?](https://www.reddit.com/r/MachineLearning/comments/1ieig2r/d_does_all_distillation_only_use_soft_labels/) (Score: 2)
    *   This thread explores whether all distillation methods use soft labels and discusses whether soft labels are more effective.
9.  [P] Project - Document information extraction and structured data mapping](https://www.reddit.com/r/MachineLearning/comments/1iebt78/p_project_document_information_extraction_and/) (Score: 1)
    *   This thread discusses a project related to document information extraction, with suggestions that an agent and a document parser VLM should be used.
10. [D] Ethical Dataset Licenses](https://www.reddit.com/r/MachineLearning/comments/1ie1f4m/d_ethical_dataset_licenses/) (Score: 0)
    *   This discussion focuses on the challenges and limitations of ethical restrictions on dataset licenses.

# Detailed Analysis by Thread
**[[D] DeepSeek? Schmidhuber did it first. (Score: 181)](https://www.reddit.com/gallery/1ielwh5)**
*   **Summary:**  The thread centers around the debate whether the DeepSeek team's work is truly novel. Many users pointed out that Jürgen Schmidhuber's earlier work covered the fundamental concepts DeepSeek used. The discussion also touches upon the lack of recognition for Schmidhuber's contribution and the challenges of assigning credit in the field of Machine Learning.
*   **Emotion:** The emotional tone is predominantly neutral, with some users expressing negative sentiments towards the perceived lack of credit given to Schmidhuber, and others expressing frustration or sarcasm.
*   **Top 3 Points of View:**
    *   Schmidhuber's work is foundational, and he deserves more credit than he receives.
    *   DeepSeek is not innovating much, but merely applying existing techniques.
    *   The field of ML is bad at assigning credit.

**[[D] Non-deterministic behavior of LLMs when temperature is 0 (Score: 129)](https://www.reddit.com/r/MachineLearning/comments/1ie15ev/d_nondeterministic_behavior_of_llms_when/)**
*  **Summary:** This thread explores the reasons why Large Language Models (LLMs) exhibit non-deterministic behavior even when the temperature parameter is set to 0. It investigates different potential causes including issues with GPUs, use of Mixture-of-Experts models, the batching process, and random seeds not properly set.
*  **Emotion:** The overall emotion is neutral, with a mix of curiosity and frustration about debugging the non-deterministic behavior.
*  **Top 3 Points of View:**
    *  Non-deterministic behavior is due to GPU errors and floating-point precision.
    *  It might be due to the architecture of the model, specifically using a Mixture-of-Experts approach.
    *  It's a software issue not properly handled during batching.

**[Why does the DeepSeek student model (7B parameters) perform slightly better than the teacher model (671B parameters)? [D] (Score: 79)](https://www.reddit.com/r/MachineLearning/comments/1ie46nq/why_does_the_deepseek_student_model_7b_parameters/)**
*   **Summary:** The discussion investigates why a smaller student model (7B parameters) from DeepSeek performs better than its larger teacher model (671B parameters).  Various theories are explored such as knowledge distillation, teacher overfitting and the quality of data. Some users question the premise of the question, stating that the student model may not actually be better.
*   **Emotion:** The emotional tone is largely neutral, with a mix of curiosity and skepticism. There are some positive sentiments related to learning and knowledge transfer.
*   **Top 3 Points of View:**
    *   Knowledge distillation process allows the smaller student model to learn a more efficient representation.
    *   The teacher model might be overfitted, allowing the student model to generalize better.
    *   The student model does not necessarily perform better than the teacher model.

**[[R] Fully open source codebase to train SOTA VLMs (Score: 42)](https://www.reddit.com/r/MachineLearning/comments/1ieh3e3/r_fully_open_source_codebase_to_train_sota_vlms/)**
*   **Summary:** This thread is about a fully open-source codebase for training state-of-the-art vision language models (VLMs). The discussion is very short, mostly with questions about training time and appreciation for the work.
*   **Emotion:**  The emotional tone is positive, with expressions of gratitude and a curiosity to find out more information.
*    **Top 3 Points of View:**
        *   Inquiry about training time on 256 H100s.
        *   Expression of gratitude for sharing the codebase.
        *   No other points are available.

**[[Discussion] Reproducibility in reporting Performance and Benchmarks (Score: 12)](https://www.reddit.com/r/MachineLearning/comments/1iei30l/discussion_reproducibility_in_reporting/)**
*   **Summary:** The main topic in this thread is the lack of reproducibility in machine learning research. Users share their frustrations regarding the lack of open-source code and the difficulty in reproducing results.
*   **Emotion:** The emotional tone is negative, reflecting frustration with the status quo, and a general agreement on the issues related to reproducibility.
*   **Top 3 Points of View:**
    *   Lack of reproducibility is a big issue in ML research.
    *   Open-source code should be mandatory for all ML papers.
    *   ML engineers share the same frustration about reproducibility.

**[[P] Interactive Explanation to ROC AUC Score (Score: 10)](https://www.reddit.com/r/MachineLearning/comments/1iem7bq/p_interactive_explanation_to_roc_auc_score/)**
*   **Summary:**  This thread is about a blog post that provides an interactive explanation of the ROC AUC score. People generally appreciated the post with some thinking it does not need interactive elements like sliders.
*   **Emotion:** The emotional tone is positive, with appreciation for the blog and its interactive elements.
*  **Top 3 Points of View:**
        *   Users like the blog.
        *   Some users found the interactivity nice.
        *  Some users think the interactive elements are not needed.

**[[R] Classification: Image with imprint (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1iee8mi/r_classification_image_with_imprint/)**
*   **Summary:** This thread centers around how to do image classification with imprints. A user advises the original poster to get their hands on a number of comparable counterfeit images to measure their model effectively.
*   **Emotion:** The emotion is mostly neutral, and somewhat informative.
*   **Top 3 Points of View:**
    *   Acquiring a dataset of counterfeit images is essential for effective model measurement.
    *   No other points are available.
    *   No other points are available.

**[[D] Does all distillation only use soft labels (probability distribution)? (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1ieig2r/d_does_all_distillation_only_use_soft_labels/)**
*   **Summary:** This thread explores whether all knowledge distillation methods exclusively rely on soft labels and discusses the effectiveness of soft labels versus hard labels.
*   **Emotion:** The emotional tone is neutral, focusing on technical aspects and clarification of concepts.
*   **Top 3 Points of View:**
    *  Soft labels are seen to be more informative than hard labels.
    *  Some users believe that Deepseek does not use soft label distillation.
    *   Some re-distilled models using logit distillation perform better.

**[[P] Project - Document information extraction and structured data mapping (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1iebt78/p_project_document_information_extraction_and/)**
*   **Summary:** This thread discusses a project involving document information extraction and structured data mapping. The user suggests using an agent and a document parser VLM to perform this task.
*   **Emotion:** The emotional tone is neutral, with a focus on providing technical advice.
*   **Top 3 Points of View:**
    *   An agent is needed to decide if a question should be answered.
    *   An agent and a doc parser VLM should be used.
    *   The process should include memory for the agent.

**[[D] Ethical Dataset Licenses (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1ie1f4m/d_ethical_dataset_licenses/)**
*   **Summary:** The discussion in this thread revolves around the use of ethical restrictions in dataset licenses. A user expresses doubts on the effectiveness of such restrictions.
*   **Emotion:** The emotional tone is neutral, but with a bit of skepticism and realism.
*   **Top 3 Points of View:**
    *   You can change licenses to include custom restrictions as long as the license has a different name.
    *   Ethical restrictions are not effective.
    *   People would bypass restrictions in dataset licenses.
