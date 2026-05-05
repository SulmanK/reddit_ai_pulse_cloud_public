---
title: "Machine Learning Subreddit"
date: "2026-05-05"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["AI", "Machine Learning", "Research", "Industry"]
---

# Overall Ranking and Top Discussions

1.  [[R] Struggling to reproduce paper results before improving them — stuck below reported accuracy](https://www.reddit.com/r/MachineLearning/comments/1t4dkew/struggling_to_reproduce_paper_results_before/) (Score: 59)
    *   Discussions centered around the difficulty of reproducing results from published machine learning papers and strategies for handling such situations in academic research.
2.  [[D] Production AI very different from the demos](https://www.reddit.com/r/MachineLearning/comments/1t4mzm3/production_ai_very_different_from_the_demos_d/) (Score: 27)
    *   This thread discussed the significant differences between AI demos and real-world production AI, focusing on issues like cost management and the practical challenges of deployment.
3.  [[D] Is there a notable increase in demand for privacy-preserving AI/ML with the advent of LLMs?](https://www.reddit.com/r/MachineLearning/comments/1t3u2jh/is_there_a_notable_increase_in_demand_for/) (Score: 26)
    *   The conversation explored whether the rise of LLMs has increased the demand for privacy-preserving AI/ML, with various perspectives on user concerns and industry trends.
4.  [[P] Building a 9-ball AI player: Candidate generation for direct cut shots](https://i.redd.it/aw3nvcz9b7zg1.png) (Score: 15)
    *   This post showcased a project focused on developing an AI player for the game of 9-ball, specifically addressing candidate generation for direct cut shots.
5.  [[D] NeurIPS Submission Number](https://www.reddit.com/r/MachineLearning/comments/1t4oykt/neurips_submission_number_d/) (Score: 6)
    *   A brief discussion about submission numbers for NeurIPS.
6.  [[R] TritonSigmoid: A fast, padding-aware sigmoid attention kernel for GPUs](https://www.reddit.com/r/MachineLearning/comments/1t4kalf/tritonsigmoid_a_fast_paddingaware_sigmoid/) (Score: 5)
    *   This thread discussed a new kernel for GPUs, TritonSigmoid, focusing on its potential for variable sequence length scenarios and its memory efficiency compared to FlashAttention.
7.  [[D] Radar Engineer to Autonomy/AI](https://www.reddit.com/r/MachineLearning/comments/1t4ombd/radar_engineer_to_autonomyai_d/) (Score: 1)
    *   This thread provided a link to a research paper as a starting point for individuals transitioning from radar engineering to autonomy/AI.
8.  [[D] NeurIPS openreview - can I upload paper pdf after abstract deadline or should I upload something first to be able to update it later?](https://www.reddit.com/r/MachineLearning/comments/1t46wzz/neurips_openreview_can_i_upload_paper_pdf_after/) (Score: 0)
    *   Users discussed the procedures and potential issues regarding uploading PDF papers to NeurIPS openreview after the abstract deadline.
9.  [[D] Fixing Unsupervised Hyperbolic Contrastive Loss](https://www.reddit.com/r/MachineLearning/comments/1t45ggk/fixing_unsupervised_hyperbolic_contrastive_loss_d/) (Score: 0)
    *   This thread provided advice on fixing unsupervised hyperbolic contrastive loss, suggesting parameter adjustments and projection steps.
10. [[D] Neurips, how can i submit the "link" to the code?](https://www.reddit.com/r/MachineLearning/comments/1t3zovv/neurips_how_can_i_submit_the_link_to_the_code_d/) (Score: 0)
    *   Discussions revolved around the best practices for submitting code links for NeurIPS papers, including anonymization and alternative methods.
11. [[R] Confusion about the NeurIPS 2026 page limit](https://www.reddit.com/r/MachineLearning/comments/1t3y3nu/confusion_about_the_neurips_2026_page_limit_r/) (Score: 0)
    *   Users clarified the page limit for NeurIPS submissions.

# Detailed Analysis by Thread

**[ Struggling to reproduce paper results before improving them — stuck below reported accuracy [R] (Score: 59)](https://www.reddit.com/r/MachineLearning/comments/1t4dkew/struggling_to_reproduce_paper_results_before/)**
*   **Summary:** The main discussion revolves around the common and frustrating experience of being unable to reproduce results from published machine learning papers, often finding that one's own implementations yield lower accuracy than reported. This leads to questions about how to proceed with one's own research and publications.
*   **Emotion:** The dominant emotion is Neutral, with underlying tones of frustration and shared experience. Users express empathy and offer practical advice, indicating a supportive but not overtly emotional discussion.
*   **Top 3 Points of View:**
    *   **Directly contact authors:** Several users suggested reaching out to the paper's authors for clarification or code.
    *   **Reproducibility issues are common:** Many contributors acknowledged that this is a widespread problem in academia, particularly in ML, and advised the original poster that they are not alone.
    *   **Focus on own baseline:** A recurring suggestion is to treat the current reproducible results as the baseline and frame improvements relative to that, rather than focusing on matching potentially unreproducible reported numbers.

**[ Production AI very different from the demos [D] (Score: 27)](https://www.reddit.com/r/MachineLearning/comments/1t4mzm3/production_ai_very_different_from_the_demos_d/)**
*   **Summary:** This thread highlights that the experience of using AI in production is vastly different from what is presented in demonstrations, primarily due to cost management and the unpredictability of real-user inputs. Key issues include tracking costs per feature and the rapid consumption of context windows.
*   **Emotion:** Predominantly Neutral, with a hint of frustration related to the practical challenges of production AI. The tone is informative and problem-solving oriented.
*   **Top 3 Points of View:**
    *   **Cost attribution is key:** A major point is the difficulty in attributing costs to specific features, as providers often give aggregate spend. Solutions involve detailed logging and tagging at the application layer.
    *   **Real-world usage impacts cost:** Demos use controlled inputs, whereas real users generate long, messy inputs that consume context windows much faster, leading to higher costs.
    *   **Strategic model and prompt management:** Suggestions include using smaller, cheaper models for less demanding tasks and implementing prompt length caps to control costs.

**[ Is there a notable increase in demand for privacy-preserving AI/ML with the advent of LLMs? [D] (Score: 26)](https://www.reddit.com/r/MachineLearning/comments/1t3u2jh/is_there_a_notable_increase_in_demand_for/)**
*   **Summary:** The discussion investigates whether the rise of Large Language Models (LLMs) has led to a greater demand for privacy-preserving AI/ML techniques. Contributors shared insights from various sectors, including healthcare, and debated the general public's willingness to trade privacy for utility.
*   **Emotion:** The tone is largely Neutral, with some sentiment leaning towards skepticism regarding widespread public demand for privacy. The discussion involves contrasting opinions and evidence from different fields.
*   **Top 3 Points of View:**
    *   **Increased demand in specific sectors:** Several users, particularly those in healthcare, noted a significant increase in demand for privacy-preserving AI due to sensitive data and regulatory pressures.
    *   **General public prioritizes convenience over privacy:** A common viewpoint is that most individuals are not highly concerned with privacy and are willing to share data for appealing services, contrasting with a niche group that actively seeks privacy.
    *   **Technical challenges and solutions:** Some comments touched upon the technical hurdles in achieving privacy-preserving AI and pointed to emerging solutions like local, open-source models.

**[ Building a 9-ball AI player: Candidate generation for direct cut shots [P] (Score: 15)](https://i.redd.it/aw3nvcz9b7zg1.png)**
*   **Summary:** This post presents a project focused on developing an AI for the game of 9-ball, specifically concentrating on the candidate generation aspect for direct cut shots.
*   **Emotion:** The emotions expressed are primarily Positive, with users showing enthusiasm and appreciation for the project.
*   **Top 3 Points of View:**
    *   **Appreciation for applying ML to games:** Several commenters expressed joy at seeing a game like 9-ball explored through machine learning, finding it to be a "human" aspect of the field.
    *   **Project looks fun:** The general sentiment is that this is an enjoyable and interesting project.

**[ NeurIPS Submission Number [D] (Score: 6)](https://www.reddit.com/r/MachineLearning/comments/1t4oykt/neurips_submission_number_d/)**
*   **Summary:** This is a brief thread where users share their submission numbers for NeurIPS.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Sharing submission numbers.

**[ TritonSigmoid: A fast, padding-aware sigmoid attention kernel for GPUs [R] (Score: 5)](https://www.reddit.com/r/MachineLearning/comments/1t4kalf/tritonsigmoid_a_fast_paddingaware_sigmoid/)**
*   **Summary:** The discussion is about TritonSigmoid, a new attention kernel for GPUs, and its potential benefits for variable sequence length scenarios. Users are curious about its memory usage compared to FlashAttention.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   **Promising for variable sequence lengths:** The kernel is seen as a positive development for handling varying sequence lengths, potentially beyond just single-cell data.
    *   **Curiosity about memory trade-offs:** Users are keen to understand if the padding awareness comes at the cost of memory efficiency compared to existing solutions like FlashAttention.

**[ Radar Engineer to Autonomy/AI [D] (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1t4ombd/radar_engineer_to_autonomyai_d/)**
*   **Summary:** This post provides a link to a specific research paper as a recommended starting point for individuals looking to transition from a radar engineering background to roles in autonomy or AI.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   Providing a resource for career transition.

**[ NeurIPS openreview - can I upload paper pdf after abstract deadline or should I upload something first to be able to update it later? [D] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1t46wzz/neurips_openreview_can_i_upload_paper_pdf_after/)**
*   **Summary:** Users are discussing the process of submitting paper PDFs to NeurIPS openreview, specifically whether it's possible to upload a placeholder or update the PDF after the abstract deadline, and sharing error messages encountered.
*   **Emotion:** Neutral, with some undertones of confusion and technical frustration due to errors.
*   **Top 3 Points of View:**
    *   **Upload a placeholder:** The safest approach is to upload a placeholder PDF to enable later updates, as OpenReview can be strict about deadlines.
    *   **Abstract deadline requirements:** At the abstract deadline, only title and abstract are mandatory; PDFs can be updated later, but the author list is locked.
    *   **Technical issues:** Some users reported encountering specific error messages ("Cannot read properties of undefined (reading 'id')") preventing them from submitting.

**[ Fixing Unsupervised Hyperbolic Contrastive Loss [D] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1t45ggk/fixing_unsupervised_hyperbolic_contrastive_loss_d/)**
*   **Summary:** This thread offers technical advice on how to fix issues with unsupervised hyperbolic contrastive loss, suggesting adjustments to the temperature parameter and ensuring proper gradient updates.
*   **Emotion:** Neutral, focused on technical problem-solving.
*   **Top 3 Points of View:**
    *   **Adjust temperature parameter:** The temperature parameter for hyperbolic space might be too low and needs to be increased.
    *   **Ensure projection step:** The projection step should occur after every gradient update, not just during the forward pass.

**[ Neurips, how can i submit the "link" to the code? [D] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1t3zovv/neurips_how_can_i_submit_the_link_to_the_code_d/)**
*   **Summary:** This discussion centers on how to properly submit links to code repositories for NeurIPS papers, especially given the constraints of supplementary materials and anonymization requirements.
*   **Emotion:** Neutral, with some comments reflecting mild annoyance at the strictness of supplementary submission rules.
*   **Top 3 Points of View:**
    *   **Link in PDF:** A common workaround is to include the code link directly within the PDF of the paper.
    *   **Anonymization is crucial:** If linking to platforms like GitHub, ensuring the repository is anonymized is critical to avoid desk rejection.
    *   **Future code upload:** It's acceptable to state that code will be uploaded in the future, though providing a link is generally preferred.

**[ Confusion about the NeurIPS 2026 page limit [R] (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1t3y3nu/confusion_about_the_neurips_2026_page_limit_r/)**
*   **Summary:** Users are seeking clarification on the page limit for NeurIPS submissions, specifically debating whether it is 8 or 9 pages, excluding references and appendices.
*   **Emotion:** Neutral.
*   **Top 3 Points of View:**
    *   **Page limit is 9 pages:** The official handbook and style guide indicate 9 pages, excluding references and appendices.
    *   Clarification on existing information: Users are seeking confirmation of the page limit based on official documentation.
