---
title: "Machine Learning Subreddit"
date: "2026-04-29"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "AI", "research"]
---

# Overall Ranking and Top Discussions

1.  [[D] Why isn’t LLM reasoning done in vector space instead of natural language?](https://www.reddit.com/r/MachineLearning/comments/1syjlc2/why_isnt_llm_reasoning_done_in_vector_space/) (Score: 115)
    *   This discussion explores the reasons behind LLM reasoning primarily occurring in natural language rather than directly in vector space, touching on aspects like interpretability, debuggability, and the current state of research.
2.  [[P] An interactive semantic map of the latest 10 million published papers](https://www.reddit.com/gallery/1sz14mi) (Score: 96)
    *   This post presents an interactive tool for visualizing and exploring a large corpus of research papers, eliciting positive reactions and questions about its methodology.
3.  [[D] IJCAI-ECAI 2026: Decision Notification and ChairingTool Status Thread](https://www.reddit.com/r/MachineLearning/comments/1syl769/ijcaiecai_2026_decision_notification_and/) (Score: 19)
    *   This thread serves as a discussion point for participants of the IJCAI-ECAI 2026 conference, primarily focusing on the notification of paper decisions and a minor technical issue with comment visibility.
4.  [[D] Stanford Paper review](https://www.reddit.com/r/MachineLearning/comments/1sz0yy8/stanford_paper_review_d/) (Score: 7)
    *   A user shares their experience using a Stanford paper review tool, noting that it rejected their accepted papers and requested further experiments.
5.  [[N] Free Registration & $20K Prize Pool: 2nd MLC-SLM Challenge 2026 on Multilingual Speech LLMs](https://www.reddit.com/r/MachineLearning/comments/1symd9i/free_registration_20k_prize_pool_2nd_mlcslm/) (Score: 2)
    *   This post announces a challenge related to Multilingual Speech LLMs, providing details on free registration and a prize pool, along with a link for more information.
6.  [[D] Am I crazy to think that the UAI authors are confusing the discussion deadline with the rebuttal deadline ?](https://www.reddit.com/r/MachineLearning/comments/1syx7n6/am_i_crazy_to_think_that_the_uai_authors_are/) (Score: 2)
    *   This discussion revolves around potential confusion regarding deadlines for discussions and rebuttals in the UAI conference, with authors sharing their experiences with reviewer responses and the submission process.
7.  [[D] How strongly do you believe LLM judges on the for the ML papers??](https://www.reddit.com/r/MachineLearning/comments/1sz6uuj/how_strongly_do_you_believe_llm_judges_on_the_for/) (Score: 1)
    *   This thread discusses the reliability and effectiveness of using LLM judges for reviewing ML papers, with users sharing mixed experiences and highlighting the importance of human validation and calibration.

# Detailed Analysis by Thread

**[[D] Why isn’t LLM reasoning done in vector space instead of natural language?](https://www.reddit.com/r/MachineLearning/comments/1syjlc2/why_isnt_llm_reasoning_done_in_vector_space/) (Score: 115)**
*   **Summary:** The discussion delves into why large language models (LLMs) primarily perform reasoning in natural language rather than directly within vector spaces. Key points include the role of vector spaces in representing features and associations, the lack of backward paths for information flow in vector space during a forward pass, and ongoing research into "looped LLMs" that use RNN-like mechanisms. The trade-off between vector-based computation and natural language for debuggability and interpretability is also a significant theme.
*   **Emotion:** Predominantly Neutral, with a slight leaning towards Negative in one comment which expresses a lack of a correct answer and touches upon the limitations of current models.
*   **Top 3 Points of View:**
    *   LLMs already perform reasoning in latent (vector) space, with natural language outputs being a surfaced trace for human readability and debuggability.
    *   Maintaining natural language reasoning is crucial for debuggability and control, as full vector-space reasoning would reduce interpretability and make it harder to trace errors.
    *   The auto-regressive nature of LLMs and the lack of "concept" data directly in vector space (except through language) necessitate the current approach, with potential for diffusion LLMs or recurrent architectures to explore vector-space reasoning more effectively.

**[[P] An interactive semantic map of the latest 10 million published papers](https://www.reddit.com/gallery/1sz14mi) (Score: 96)**
*   **Summary:** This post introduces an interactive tool that creates a semantic map of the 10 million most recent published papers. The community responded with enthusiasm, appreciating the visualization and seeking more details about the underlying methodology, including the Voronoi partitioning and labeling processes.
*   **Emotion:** Overwhelmingly Positive, with users expressing excitement and appreciation for the presented tool.
*   **Top 3 Points of View:**
    *   General appreciation for the "coolness" and usefulness of the semantic map for exploring research papers.
    *   Curiosity and desire for more technical details regarding the Voronoi partitioning procedure, clustering methods (like HDBSCAN), and the labeling process.
    *   Interest in the scalability of processing such a large number of papers and whether a knowledge graph forms the core of the system.

**[[D] IJCAI-ECAI 2026: Decision Notification and ChairingTool Status Thread](https://www.reddit.com/r/MachineLearning/comments/1syl769/ijcaiecai_2026_decision_notification_and/) (Score: 19)**
*   **Summary:** This thread is a status update for the IJCAI-ECAI 2026 conference, where participants are sharing information about their paper decision notifications and a minor issue with the display of comment counts.
*   **Emotion:** Neutral, with a slight underlying tone of mild confusion regarding the comment count discrepancy.
*   **Top 3 Points of View:**
    *   Notification of paper decisions being available in the conference submission system.
    *   Observation and mild confusion about the discrepancy between the reported number of comments and the number visible on the post.
    *   Confirmation of decisions being received.

**[[D] Stanford Paper review](https://www.reddit.com/r/MachineLearning/comments/1sz0yy8/stanford_paper_review_d/) (Score: 7)**
*   **Summary:** A user shares their negative experience with a Stanford paper review tool, reporting that it rejected their already accepted papers and demanded further experiments.
*   **Emotion:** Neutral, expressing a factual account of an experience.
*   **Top 3 Points of View:**
    *   The paper review tool rejected the user's papers that had already been accepted.
    *   The tool requested additional experiments for the user's papers.
    *   This suggests a potential issue with the tool's calibration or understanding of publication criteria.

**[[N] Free Registration & $20K Prize Pool: 2nd MLC-SLM Challenge 2026 on Multilingual Speech LLMs](https://www.reddit.com/r/MachineLearning/comments/1symd9i/free_registration_20k_prize_pool_2nd_mlcslm/) (Score: 2)**
*   **Summary:** This post announces the second MLC-SLM Challenge 2026, focusing on Multilingual Speech LLMs, featuring free registration and a $20,000 prize pool. A link is provided for more detailed information.
*   **Emotion:** Neutral, serving as an announcement.
*   **Top 3 Points of View:**
    *   Announcement of the MLC-SLM Challenge 2026.
    *   Highlighting free registration and a $20,000 prize pool.
    *   Provision of a link for further details.

**[[D] Am I crazy to think that the UAI authors are confusing the discussion deadline with the rebuttal deadline ?](https://www.reddit.com/r/MachineLearning/comments/1syx7n6/am_i_crazy_to_think_that_the_uai_authors_are/) (Score: 2)**
*   **Summary:** This thread discusses potential confusion surrounding the UAI conference's discussion and rebuttal deadlines. Authors express frustration with reviewers not responding to rebuttals, issues with presenting complex corrections due to character limits, and the tight timeline for submitting responses.
*   **Emotion:** Predominantly Neutral, with an undercurrent of frustration and concern due to the difficult submission and response process.
*   **Top 3 Points of View:**
    *   Authors are experiencing issues with reviewers not responding to their rebuttals or misunderstanding the deadlines.
    *   The current format for submitting rebuttals (e.g., multiple posts due to character limits for proof-related issues) is problematic.
    *   The overall timeline and the pressure to finalize submissions while also reviewing other papers are creating significant stress for participants.

**[[D] How strongly do you believe LLM judges on the for the ML papers??](https://www.reddit.com/r/MachineLearning/comments/1sz6uuj/how_strongly_do_you_believe_llm_judges_on_the_for/) (Score: 1)**
*   **Summary:** This discussion explores the trustworthiness of LLM judges in evaluating Machine Learning papers. While some users report positive experiences validated by human judgment, others express skepticism, particularly regarding the LLMs' ability to assess novelty and incremental advances. The importance of human oversight and calibration is frequently mentioned.
*   **Emotion:** Neutral, with a mix of positive and skeptical viewpoints.
*   **Top 3 Points of View:**
    *   LLM judges can be useful and yield good results, but human validation is almost always necessary for publications.
    *   LLMs struggle to accurately assess novelty and incremental advancements, making their judgments less reliable for high-stakes evaluations like conference submissions.
    *   Statistical validation to assert inter-rater reliability between human and semantic measurements is important for addressing risks associated with LLM judges.
