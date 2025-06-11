---
title: "Machine Learning Subreddit"
date: "2025-05-14"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "AI", "research"]
---

# Overall Ranking and Top Discussions
1.  [[D] Overleaf is down?](https://www.reddit.com/r/MachineLearning/comments/1km8d7p/d_overleaf_is_down/) (Score: 158)
    *   Users discussed the Overleaf service being down and shared tips for backing up work and dealing with deadlines.
2.  [[D] Need to train a model for a client whilst proving I never saw the data](https://www.reddit.com/r/MachineLearning/comments/1km7xmu/d_need_to_train_a_model_for_a_client_whilst/) (Score: 27)
    *   Users discussed how to train a model on a client's data without directly accessing it, focusing on security and proving data isolation.
3.  [[Project] OM3 - A modular LSTM-based continuous learning engine for real-time AI experiments (GitHub release)](https://www.reddit.com/r/MachineLearning/comments/1km7biz/project_om3_a_modular_lstmbased_continuous/) (Score: 6)
    *   Users discussed the OM3 project, with one user expressing confusion about its functionality due to the lack of optimizer and loss function in the code.
4.  [[D] Trying to make sparse neural retrieval more usable](https://www.reddit.com/r/MachineLearning/comments/1kly39h/d_trying_to_make_sparse_neural_retrieval_more/) (Score: 4)
    *   A user shared their experience with building a similar tool for data annotation and pre-annotating various types of data.
5.  [[D] What’s your favorite podcast covering AI news, trends, technical deep dives and stories?](https://www.reddit.com/r/MachineLearning/comments/1kmm99s/d_whats_your_favorite_podcast_covering_ai_news/) (Score: 3)
    *   Users recommended Deepmind's podcasts on YouTube for AI news and trends.
6.  [[P] ViSOR – Dual-Billboard Neural Sheets for Real-Time View Synthesis (GitHub)](https://www.reddit.com/r/MachineLearning/comments/1kmg1uu/p_visor_dualbillboard_neural_sheets_for_realtime/) (Score: 2)
    *   A user inquired about the theoretical advantages of ViSOR compared to Gaussian splats for real-time view synthesis.
7.  [[D] Can dataset size make up for noisy labels?](https://www.reddit.com/r/MachineLearning/comments/1kmix9x/d_can_dataset_size_make_up_for_noisy_labels/) (Score: 2)
    *   Users discussed whether a large dataset can compensate for noisy labels in machine learning models.
8.  [[D] Innocent authors should not be penalized for the misconduct of irresponsible coauthors](https://www.reddit.com/r/MachineLearning/comments/1kmovqt/d_innocent_authors_should_not_be_penalized_for/) (Score: 1)
    *   Users debated the fairness of penalizing innocent authors for the misconduct of irresponsible co-authors, particularly in the context of peer review.
9.  [[D] Hello can we train using google images as they have large images](https://www.reddit.com/r/MachineLearning/comments/1km65v1/d_hello_can_we_train_using_google_images_as_they/) (Score: 0)
    *   The discussion involved a question about training using Google Images, with a suggestion to use `torchvision.transforms.Resize`.
10. [[R] Has anyone saved + reloaded a model’s internal state mid-inference to enable agent collaboration?](https://www.reddit.com/r/MachineLearning/comments/1km6ny5/r_has_anyone_saved_reloaded_a_models_internal/) (Score: 0)
    *   Users discussed saving and reloading a model's internal state mid-inference for agent collaboration.
11. [[D] Interviewing a PhD candidate after their speech, what should I ask them](https://www.reddit.com/r/MachineLearning/comments/1kmc1eg/d_interviewing_a_phd_candidate_after_their_speech/) (Score: 0)
    *   Users provided suggestions for interview questions to ask a PhD candidate after their speech, covering research experience, motivation, and ethical considerations.
12. [[R] Neurips Desk Rejected: This submission was identified as a “placeholder” submission](https://www.reddit.com/r/MachineLearning/comments/1kmdibo/r_neurips_desk_rejected_this_submission_was/) (Score: 0)
    *   Users discussed the desk rejection of a NeurIPS submission due to being identified as a "placeholder" submission.
13. [[R] How the jax.jit() compiler works in jax-js](https://www.reddit.com/r/MachineLearning/comments/1kmhg1h/r_how_the_jaxjit_compiler_works_in_jaxjs/) (Score: 0)
    *   A user was directed to TFJS folks for help with the jax.jit() compiler in jax-js.
14. [[R] As a highschool student, how can I get article processing fee waivered?](https://www.reddit.com/r/MachineLearning/comments/1kmkaos/r_as_a_highschool_student_how_can_i_get_article/) (Score: 0)
    *   Users provided advice to a high school student on how to get article processing fees waived, alternative publishing options, and the importance of mentorship.

# Detailed Analysis by Thread
**[[D] Overleaf is down? (Score: 158)](https://www.reddit.com/r/MachineLearning/comments/1km8d7p/d_overleaf_is_down/)**
*   **Summary:** Users are discussing the Overleaf service being down, likely due to high traffic around a deadline. They are sharing tips on backing up work, using Git, and working locally.
*   **Emotion:** The overall emotional tone is neutral, with users sharing information and offering support.
*   **Top 3 Points of View:**
    *   Users should back up their Overleaf projects using Git or other online storage services.
    *   Working with LaTeX on a local machine can prevent issues with online services.
    *   The Overleaf outage is likely due to a conference deadline, and extensions may be possible.

**[[D] Need to train a model for a client whilst proving I never saw the data (Score: 27)](https://www.reddit.com/r/MachineLearning/comments/1km7xmu/d_need_to_train_a_model_for_a_client_whilst/)**
*   **Summary:** The thread discusses the challenges and potential solutions for training a model on a client's data without directly accessing or viewing the data. Several suggestions are offered, including using secure enclaves, homomorphic encryption, and infrastructure-as-code.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Implementing strict infrastructure-as-code practices and access controls can help ensure data isolation and prove that the data was not directly accessed.
    *   Technologies like Azure Confidential VMs or secure enclaves (e.g., using SCONE) can provide provable isolation and encryption of data and code.
    *   Homomorphic encryption or federated learning could allow training on encrypted data or training models collaboratively without sharing raw data.

**[[Project] OM3 - A modular LSTM-based continuous learning engine for real-time AI experiments (GitHub release) (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1km7biz/project_om3_a_modular_lstmbased_continuous/)**
*   **Summary:** A user released their project "OM3," a modular LSTM-based continuous learning engine. One user expressed confusion about its functionality due to the lack of optimizer and loss function in the code.
*   **Emotion:** The overall emotional tone is neutral, with some confusion about the project's functionality.
*   **Top 3 Points of View:**
    *   The project looks interesting.
    *   There is confusion about what the project does due to missing key components like an optimizer and loss function.

**[[D] Trying to make sparse neural retrieval more usable (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1kly39h/d_trying_to_make_sparse_neural_retrieval_more/)**
*   **Summary:** The thread discusses making sparse neural retrieval more usable. A user shares their experience with a similar tool for data annotation.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   Sparse neural retrieval is an interesting approach.
    *   AI-powered tools can significantly improve data annotation speed and accuracy.

**[[D] What’s your favorite podcast covering AI news, trends, technical deep dives and stories? (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1kmm99s/d_whats_your_favorite_podcast_covering_ai_news/)**
*   **Summary:** The thread is about recommendations for AI-related podcasts.
*   **Emotion:** The overall emotional tone is positive.
*   **Top 3 Points of View:**
    *   Deepmind's podcasts on YouTube are a good resource for AI news and trends.

**[[P] ViSOR – Dual-Billboard Neural Sheets for Real-Time View Synthesis (GitHub) (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1kmg1uu/p_visor_dualbillboard_neural_sheets_for_realtime/)**
*   **Summary:** The thread discusses ViSOR, a method for real-time view synthesis, and compares it to Gaussian splats.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   A user is curious about the theoretical advantages of ViSOR compared to gaussian splats, especially regarding performance and quality.

**[[D] Can dataset size make up for noisy labels? (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1kmix9x/d_can_dataset_size_make_up_for_noisy_labels/)**
*   **Summary:** This thread explores whether increasing dataset size can compensate for noisy labels in machine learning models.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   More data can help if the noise is unbiased.
    *   Performance scales with the square root of the dataset size; larger batches or adapting learning dynamics may be needed.
    *   With limited data, it's best to test both the original and cleaned versions to determine which performs better on a holdout set.

**[[D] Innocent authors should not be penalized for the misconduct of irresponsible coauthors (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1kmovqt/d_innocent_authors_should_not_be_penalized_for/)**
*   **Summary:** The discussion revolves around the fairness of penalizing authors for misconduct by co-authors, specifically in peer review.
*   **Emotion:** The overall emotional tone is mixed, with some frustration but also acceptance of the logic behind the policy.
*   **Top 3 Points of View:**
    *   The current policy is fair because co-authors should be responsible for each other's actions.
    *   A point-based system for reviewers could be a better solution, rewarding good reviews and penalizing poor ones.
    *   Co-authors should contribute to the paper.

**[[D] Hello can we train using google images as they have large images (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1km65v1/d_hello_can_we_train_using_google_images_as_they/)**
*   **Summary:** A user asked about training using google images.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Use torchvision.transforms.Resize.

**[[R] Has anyone saved + reloaded a model’s internal state mid-inference to enable agent collaboration? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1km6ny5/r_has_anyone_saved_reloaded_a_models_internal/)**
*   **Summary:** The discussion is about saving and reloading a model's internal state mid-inference.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   A recent paper "Learning from Peers in Reasoning Models" did something similar.
    *   optiLLM has several sota inference optimization techniques already implemented.
    *   Questioning the benefit as opposed to just keeping the state in memory.

**[[D] Interviewing a PhD candidate after their speech, what should I ask them (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1kmc1eg/d_interviewing_a_phd_candidate_after_their_speech/)**
*   **Summary:** The thread seeks advice on what questions to ask a PhD candidate after their speech.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Focus on the candidate's research experience, contributions to papers, and challenges they faced.
    *   Ask about their motivation for pursuing a PhD and their thoughts on ethical considerations in machine learning.
    *   Keep the discussion technical but not stressful, focusing on their presentation and understanding of the field.

**[[R] Neurips Desk Rejected: This submission was identified as a “placeholder” submission (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1kmdibo/r_neurips_desk_rejected_this_submission_was/)**
*   **Summary:** The discussion is about a NeurIPS submission being desk rejected as a placeholder.
*   **Emotion:** The overall emotional tone is mixed with disappointment.
*   **Top 3 Points of View:**
    *   The desk rejection makes sense because it wasn't a real title and abstract.
    *   It is a learning experience to improve the paper for ICLR.
    *   The message is clear that the paper was a placeholder.

**[[R] How the jax.jit() compiler works in jax-js (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1kmhg1h/r_how_the_jaxjit_compiler_works_in_jaxjs/)**
*   **Summary:** This thread is about the jax.jit() compiler in jax-js.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Reach out to TFJS folks for help.

**[[R] As a highschool student, how can I get article processing fee waivered? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1kmkaos/r_as_a_highschool_student_how_can_i_get_article/)**
*   **Summary:** A high school student is seeking advice on how to get article processing fees waived.
*   **Emotion:** The overall emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Ask for an APC waiver or publish in a closed access journal.
    *   Upload it to GitHub or submit to publication elsewhere to improve skills.
    *   Submit your article to a closed access journal and talk to your advisor.
