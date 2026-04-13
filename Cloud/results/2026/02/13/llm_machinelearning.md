---
title: "Machine Learning Subreddit"
date: "2026-02-13"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "AI", "research", "hardware", "ethics"]
---

# Overall Ranking and Top Discussions
*   1. [[D] ICML: every paper in my review batch contains prompt-injection text embedded in the PDF](https://www.reddit.com/r/MachineLearning/comments/1r3oekq/d_icml_every_paper_in_my_review_batch_contains/) (Score: 267)
    *   Reviewers for ICML (and AISTAT) noticed that papers contained hidden prompt-injection text embedded in the PDF, likely as a method by the conference organizers to detect reviewers using LLMs. This sparked a discussion about the ethical implications for authors and reviewers, the effectiveness of such a trick, and the broader challenges of enforcing LLM usage policies.
*   2. [[R] Has anyone experimented with MHC on traditional autoencoders/convolutional architectures?](https://www.reddit.com/r/MachineLearning/comments/1r3gqng/r_has_anyone_experimented_with_mhc_on_traditional/) (Score: 18)
    *   The discussion revolves around experimenting with MHC (presumably related to deep learning architectures, possibly within the context of hyperspectral imaging) on autoencoders/convolutional architectures. Users shared insights on architectural choices, particularly the role of residual connections and alternative dimensionality reduction methods for hyperspectral data, and enquired about the dataset used.
*   3. [[P] ML training cluster for university students](https://www.reddit.com/r/MachineLearning/comments/1r388tr/p_ml_training_cluster_for_university_students/) (Score: 6)
    *   University students discussed building an ML training cluster, exploring hardware choices, budget allocation, and infrastructure considerations. Key concerns included the suitability of Mac Studios, the value of specific NVIDIA GPUs like the 3090, and the need for expert guidance or cloud alternatives.
*   4. [[D] Conformal Prediction vs naive thresholding to represent uncertainty](https://www.reddit.com/r/MachineLearning/comments/1r37m2f/d_conformal_prediction_vs_naive_thresholding_to/) (Score: 5)
    *   The discussion explores the differences between Conformal Prediction (CP) and naive thresholding for representing uncertainty, particularly in anomaly detection. Users highlighted CP's theoretical guarantees versus thresholding's heuristic nature and offered a cautionary note on using the abbreviation 'CP'.
*   5. [[D] Has anyone received their ICML papers to review yet?](https://www.reddit.com/r/MachineLearning/comments/1r3jz58/d_has_anyone_received_their_icml_papers_to_review/) (Score: 5)
    *   Reviewers discussed whether they had received their ICML papers for review. The conversation quickly shifted to a discovery of hidden prompt-injection text within the submitted PDFs, raising concerns about its purpose and potential ethical implications for both authors and reviewers.
*   6. [[D] Teaching AI to Reason With Just 13 Parameters](https://www.reddit.com/r/MachineLearning/comments/1r3rzmt/d_teaching_ai_to_reason_with_just_13_parameters/) (Score: 0)
    *   This post briefly mentions teaching AI to reason with a minimal number of parameters. The only comment is a sarcastic or appreciative 'Thank u chatgpt', implying skepticism or acknowledgment of AI's role in the topic.

# Detailed Analysis by Thread
**[ [D] ICML: every paper in my review batch contains prompt-injection text embedded in the PDF (Score: 267)](https://www.reddit.com/r/MachineLearning/comments/1r3oekq/d_icml_every_paper_in_my_review_batch_contains/)**
*  **Summary:** Reviewers for ICML (and AISTAT) noticed that papers contained hidden prompt-injection text embedded in the PDF, likely as a method by the conference organizers to detect reviewers using LLMs. This sparked a discussion about the ethical implications for authors and reviewers, the effectiveness of such a trick, and the broader challenges of enforcing LLM usage policies.
*  **Emotion:** The overall emotional tone is predominantly neutral. There is some variation in sentiment among comments.
*  **Top 3 Points of View:**
    * ICML's Use of Prompt Injection: The conference embedded hidden prompt injections in papers, intended to detect reviewers using LLMs for automated reviews. This is seen by some as ironic, given it's a field they study.
    * Ethical Concerns & Negative Impact: Reviewers expressed worry that these injections could inadvertently cause authors to be flagged for collusion or ethics violations if LLMs detect the prompts, leading to desk rejects. It's viewed as a poorly thought-out strategy.
    * Debate on Justification & Effectiveness: Some questioned if prompt injection is justified as a deterrent for lazy reviewers who use LLMs, suggesting it's 'fair game.' Others reported that current LLMs (like Gemini) didn't include the injected prompts in their reviews, casting doubt on the trick's effectiveness.
**[ [R] Has anyone experimented with MHC on traditional autoencoders/convolutional architectures? (Score: 18)](https://www.reddit.com/r/MachineLearning/comments/1r3gqng/r_has_anyone_experimented_with_mhc_on_traditional/)**
*  **Summary:** The discussion revolves around experimenting with MHC (presumably related to deep learning architectures, possibly within the context of hyperspectral imaging) on autoencoders/convolutional architectures. Users shared insights on architectural choices, particularly the role of residual connections and alternative dimensionality reduction methods for hyperspectral data, and enquired about the dataset used.
*  **Emotion:** The overall emotional tone is predominantly neutral.
*  **Top 3 Points of View:**
    * Caution with Residual Connections: Swapping out residual connections in deep convolutional autoencoders for hyperspectral data could lead to stability issues and debugging optimization rather than learning capacity, as residuals are crucial for stability.
    * Alternative Strategies for Hyperspectral AEs: For hyperspectral data, structured dimensionality reduction, spectral grouping, 1x1 spectral bottlenecks, or hybrid 3D->2D convolutional stages are often more effective than immediate architectural changes for memory and performance improvements.
    * Dataset Availability Inquiry: There was interest in whether the dataset used for the experimentation was public, reflecting a general curiosity about hyperspectral image data.
**[ [P] ML training cluster for university students (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1r388tr/p_ml_training_cluster_for_university_students/)**
*  **Summary:** University students discussed building an ML training cluster, exploring hardware choices, budget allocation, and infrastructure considerations. Key concerns included the suitability of Mac Studios, the value of specific NVIDIA GPUs like the 3090, and the need for expert guidance or cloud alternatives.
*  **Emotion:** The overall emotional tone is generally neutral, but with a leaning towards negative sentiment. There is some variation in sentiment among comments.
*  **Top 3 Points of View:**
    * Avoid Mac Studio/Apple Silicon: Mac Studio clusters are considered a poor fit due to limited MLX ecosystem, second-class PyTorch support, and non-transferable workflows compared to the CUDA-first environment of most research labs.
    * Prioritize NVIDIA 3090 GPUs for Value: For a 15-30k CAD budget, commodity NVIDIA GPUs, especially used 3090s (24GB VRAM), are recommended over expensive H100s or lower VRAM cards like 5070s. VRAM is crucial for student ML projects.
    * Consult Experts and Consider Infrastructure: It's essential to seek advice from university IT or knowledgeable students to avoid wasting money and ensure a well-designed cluster (cooling, power, networking, job scheduling like Slurm). Cloud solutions (AWS, Colab) are also suggested as potentially more cost-effective alternatives.
**[ [D] Conformal Prediction vs naive thresholding to represent uncertainty (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1r37m2f/d_conformal_prediction_vs_naive_thresholding_to/)**
*  **Summary:** The discussion explores the differences between Conformal Prediction (CP) and naive thresholding for representing uncertainty, particularly in anomaly detection. Users highlighted CP's theoretical guarantees versus thresholding's heuristic nature and offered a cautionary note on using the abbreviation 'CP'.
*  **Emotion:** The overall emotional tone is predominantly neutral. There is some variation in sentiment among comments.
*  **Top 3 Points of View:**
    * Conformal Prediction (CP) Provides Guarantees: CP offers formal coverage guarantees (e.g., true label within prediction set at 95% probability) under exchangeability assumptions, making it suitable for safety-critical settings. It adapts thresholds based on empirical data distribution.
    * Naive Thresholding is Heuristic and Lacks Guarantees: Simple thresholding acts as a decision rule but offers no formal statistical guarantees about error rates on future data, even if empirically informed by PR curves. It captures score uncertainty, not epistemic uncertainty.
    * Nuances in Anomaly Detection & Abbreviation Caution: Applying CP to anomaly detection needs careful consideration due to the exchangeability assumption being complicated by anomalies coming from different distributions. Additionally, a user warns against abbreviating 'Conformal Prediction' to 'CP' due to unintended search results.
**[ [D] Has anyone received their ICML papers to review yet? (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1r3jz58/d_has_anyone_received_their_icml_papers_to_review/)**
*  **Summary:** Reviewers discussed whether they had received their ICML papers for review. The conversation quickly shifted to a discovery of hidden prompt-injection text within the submitted PDFs, raising concerns about its purpose and potential ethical implications for both authors and reviewers.
*  **Emotion:** The overall emotional tone is predominantly neutral. There is some variation in sentiment among comments.
*  **Top 3 Points of View:**
    * Initial Query about Paper Reception: The primary purpose of the thread was for reviewers to inquire about the timing of receiving their ICML papers for review, with several users confirming they had just received them.
    * Discovery of Hidden Prompt Injection: Reviewers noticed that ICML submissions contained randomized hidden prompt-injection text, seemingly designed to detect the use of LLMs for generating reviews.
    * Concerns over Ethics and Misinterpretation: There's significant worry that LLMs detecting these prompts could mistakenly imply authors attempted prompt injection, potentially leading to false ethics violations or desk rejections for authors.
**[ [D] Teaching AI to Reason With Just 13 Parameters (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1r3rzmt/d_teaching_ai_to_reason_with_just_13_parameters/)**
*  **Summary:** This post briefly mentions teaching AI to reason with a minimal number of parameters. The only comment is a sarcastic or appreciative 'Thank u chatgpt', implying skepticism or acknowledgment of AI's role in the topic.
*  **Emotion:** The overall emotional tone is notably positive (dominant emotion: Positive).
*  **Top 3 Points of View:**
    * Brief Statement on AI Reasoning: The post title suggests an advanced topic regarding teaching AI with very few parameters.
    * Sarcastic/Appreciative Acknowledgment of AI: The sole comment 'Thank u chatgpt' could be a sarcastic remark on the nature of AI-generated content or a simple acknowledgment of the increasing capabilities of AI tools in research.
