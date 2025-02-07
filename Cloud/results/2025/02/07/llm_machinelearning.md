---
title: "Machine Learning Subreddit"
date: "2025-02-07"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "RNN", "vectorDB"]
---

# Overall Ranking and Top Discussions
1.  [[R] It Turns Out We Really Did Need RNNs](https://www.reddit.com/r/MachineLearning/comments/1ijjq5y/r_it_turns_out_we_really_did_need_rnns/) (Score: 286)
    *   Discussion about a research paper suggesting that RNNs are still necessary for certain machine learning tasks.
2.  [[R] Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2](https://www.reddit.com/r/MachineLearning/comments/1ijpmfg/r_goldmedalist_performance_in_solving_olympiad/) (Score: 36)
    *   A discussion about AlphaGeometry2, a system that achieved gold-medalist performance in solving Olympiad geometry problems.
3.  [[D] What is good practice to deploy a deep learning model  (docker, onnx, serving...) ?](https://www.reddit.com/r/MachineLearning/comments/1ijr075/d_what_is_good_practice_to_deploy_a_deep_learning/) (Score: 24)
    *   Users discuss best practices for deploying deep learning models, including the use of Docker, ONNX, and various serving frameworks.
4.  [[D] ViT from Scratch Overfitting](https://www.reddit.com/r/MachineLearning/comments/1ijr0ap/d_vit_from_scratch_overfitting/) (Score: 18)
    *   Discussion centered around the challenges of training Vision Transformer (ViT) models from scratch, particularly overfitting, and potential solutions.
5.  [What's the best Vector DB? What's new in vector db and how is one better than other? [D]](https://www.reddit.com/r/MachineLearning/comments/1ijxrqj/whats_the_best_vector_db_whats_new_in_vector_db/) (Score: 16)
    *   A conversation regarding the selection of the best vector database, including comparisons between different options like Postgres with pgvector, Pinecone, Qdrant, and others.
6.  [Why do we need the ELBO in VAEs, why not just sample from the posterior? [D]](https://www.reddit.com/r/MachineLearning/comments/1ik17hx/why_do_we_need_the_elbo_in_vaes_why_not_just/) (Score: 4)
    *   A discussion about the necessity of the Evidence Lower Bound (ELBO) in Variational Autoencoders (VAEs), questioning why one cannot simply sample from the posterior distribution.
7.  [TMLR or UAI [D]](https://www.reddit.com/r/MachineLearning/comments/1ijv9px/tmlr_or_uai_d/) (Score: 3)
    *   Users discuss the pros and cons of submitting to TMLR (Transactions on Machine Learning Research) versus UAI (Conference on Uncertainty in Artificial Intelligence).
8.  [[D] How can we define a causal network if we do not have access to domain expertise?](https://www.reddit.com/r/MachineLearning/comments/1ik0xbf/d_how_can_we_define_a_causal_network_if_we_do_not/) (Score: 1)
    *   A discussion on how to define a causal network without access to domain expertise.
9.  [[D] ONNX runtime inference silently defaults to CPUExecutionProvider](https://www.reddit.com/r/MachineLearning/comments/1ijl7r8/d_onnx_runtime_inference_silently_defaults_to/) (Score: 0)
    *   A user seeks help with ONNX Runtime defaulting to CPU execution, despite the presence of compatible GPU resources.
10. [[D] voice as fingerprint?](https://www.reddit.com/r/MachineLearning/comments/1ijsfjr/d_voice_as_fingerprint/) (Score: 0)
    *   Discussion about using voice as a biometric identifier.

# Detailed Analysis by Thread
**[[R] It Turns Out We Really Did Need RNNs (Score: 286)](https://www.reddit.com/r/MachineLearning/comments/1ijjq5y/r_it_turns_out_we_really_did_need_rnns/)**
*  **Summary:** The thread discusses a research paper that suggests recurrent neural networks (RNNs) are still valuable and necessary for certain machine learning tasks, even with the advancements in transformers. Users discuss the paper's findings, alternative solutions, and potential limitations of the conclusions.
*  **Emotion:** The overall emotional tone is neutral, with a mix of positive comments about the paper and negative comments about the title.
*  **Top 3 Points of View:**
    *   RNNs are still a relevant solution for problems requiring iterative refinement.
    *   The attention mechanism in transformers can provide a similar function to RNNs in an auto-regressive way.
    *   The title is considered clickbait, as the concept of RNNs is very specific in the literature.

**[[R] Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2 (Score: 36)](https://www.reddit.com/r/MachineLearning/comments/1ijpmfg/r_goldmedalist_performance_in_solving_olympiad/)**
*  **Summary:** The thread centers around a discussion of AlphaGeometry2, an AI system developed to solve complex geometry problems at an Olympiad level. Users primarily inquire about the types of skills and knowledge tested in such competitions.
*  **Emotion:** The overall emotional tone is neutral, expressing curiosity about the topic.
*  **Top 3 Points of View:**
    *   Inquiry about the skills tested in Olympiad geometry problems.

**[[D] What is good practice to deploy a deep learning model  (docker, onnx, serving...) ? (Score: 24)](https://www.reddit.com/r/MachineLearning/comments/1ijr075/d_what_is_good_practice_to_deploy_a_deep_learning/)**
*  **Summary:** This thread is focused on best practices for deploying deep learning models. The discussion covers aspects such as efficiency, inference speed, and deployment/hosting options, with recommendations for tools like Docker, ONNX, TensorRT, and serving frameworks.
*  **Emotion:** The overall emotional tone is neutral, providing informative and helpful suggestions.
*  **Top 3 Points of View:**
    *   ONNX and TensorRT are good for optimizing efficiency and inference speed, with TensorRT being hardware-specific.
    *   Docker is the best option for deployment and hosting on providers like Azure, Runpod, and Amazon.
    *   Triton can be advantageous with automatic mini-batching, but only if it is necessary to squeeze out as much as possible out of each machine.

**[[D] ViT from Scratch Overfitting (Score: 18)](https://www.reddit.com/r/MachineLearning/comments/1ijr0ap/d_vit_from_scratch_overfitting/)**
*  **Summary:** The discussion revolves around the issue of overfitting when training Vision Transformer (ViT) models from scratch, particularly with limited data. Recommendations include using pre-trained models, augmentation techniques, regularization, and alternative architectures like CNNs.
*  **Emotion:** The overall emotional tone is neutral, with users offering advice and suggestions to solve the problem.
*  **Top 3 Points of View:**
    *   Training ViT models from scratch with only 27,000 samples is not feasible; using a pre-trained model and fine-tuning is recommended.
    *   Strong augmentation, regularization, and self-supervised pre-training are necessary when training a ViT from scratch.
    *   Using CNNs or CNN-like architectures could be more effective if training from scratch is a must.

**[What's the best Vector DB? What's new in vector db and how is one better than other? [D] (Score: 16)](https://www.reddit.com/r/MachineLearning/comments/1ijxrqj/whats_the_best_vector_db_whats_new_in_vector_db/)**
*  **Summary:** This thread is a discussion about different vector databases and their pros and cons. It involves comparisons between Postgres with pgvector, Pinecone, Qdrant, FAISS, ChromaDB, and hnswlib. Users are sharing their experiences and recommendations based on different use cases and requirements.
*  **Emotion:** The emotional tone is mostly positive, with users providing suggestions and experiences.
*  **Top 3 Points of View:**
    *   Postgres with pgvector is highly recommended, especially if a relational database is desired.
    *   Pinecone is a good option for quickly developing state-of-the-art vector search.
    *   Qdrant is a generally good, open-source option that can scale to millions of dense vectors.

**[Why do we need the ELBO in VAEs, why not just sample from the posterior? [D] (Score: 4)](https://www.reddit.com/r/MachineLearning/comments/1ik17hx/why_do_we_need_the_elbo_in_vaes_why_not_just/)**
*  **Summary:** This thread discusses the role of the ELBO in Variational Autoencoders (VAEs) and whether it is possible to train a VAE by directly sampling from the posterior distribution.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Sampling directly from the posterior is possible, but inefficient because the latent variables sampled from the prior may not match the data well.
    *   Using the ELBO to sample from q(z | x) gives a better chance of obtaining a decent z.
    *    Other methods can be used to build a model, but each method has its own difficulties.

**[TMLR or UAI [D] (Score: 3)](https://www.reddit.com/r/MachineLearning/comments/1ijv9px/tmlr_or_uai_d/)**
*  **Summary:** This thread involves a user asking whether they should submit to TMLR or UAI. One user suggests ECAI as another option and notes that TMLR reviews may take up to 5 months for the first round.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Consider ECAI as a submission venue.
    *   TMLR reviews may take up to 5 months for the first round.

**[[D] How can we define a causal network if we do not have access to domain expertise? (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1ik0xbf/d_how_can_we_define_a_causal_network_if_we_do_not/)**
*  **Summary:** This thread explores methods for defining a causal network without domain expertise.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Causal inference is extremely difficult without expert knowledge.
    *   Causal graph learning algorithms can be used but are often unreliable.
    *   Causality can be inferred in dynamic/temporal domains where actions can be taken and their effects observed.

**[[D] ONNX runtime inference silently defaults to CPUExecutionProvider (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1ijl7r8/d_onnx_runtime_inference_silently_defaults_to/)**
*  **Summary:** This thread is about an issue where ONNX Runtime defaults to CPU execution, even when GPU resources are available.
*  **Emotion:** The emotional tone is negative due to the problem faced by the user, but neutral with the suggestions.
*  **Top 3 Points of View:**
    *   The user needs to share code and environment setup for debugging.
    *   The issue may be related to configuration problems with CUDA or missing dependencies.
    *   Importing torch before onnxruntime might solve the issue.

**[[D] voice as fingerprint? (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1ijsfjr/d_voice_as_fingerprint/)**
*  **Summary:** The thread discusses the feasibility of using voice as a fingerprint for identification purposes. The responses vary from doubts about current speaker recognition technology to asserting that the problem is mostly solved.
*  **Emotion:** The emotional tone is neutral to positive.
*  **Top 3 Points of View:**
    *   Speaker recognition is an active research field.
    *   Current speaker recognition technology, such as in Google Assistant and Alexa, is not accurate enough for voice to be used as a fingerprint.
    *   Voice biometrics is mostly solved with 95% accuracy and can be used with a second factor for better security.
