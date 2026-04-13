---
title: "Machine Learning Subreddit"
date: "2026-03-07"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["Machine Learning", "Deep Learning", "LLM", "Research", "PhD"]
---

# Overall Ranking and Top Discussions
*   1. [[P] VeridisQuo - open-source deepfake detector that combines spatial + frequency analysis and shows you where the face was manipulated](https://i.redd.it/j51nr1pqomng1.gif) (Score: 170)
    *   Discussion centered on the technical details, performance metrics, integration, and potential future uses of a new open-source deepfake detector.
*   2. [[P] NanoJudge: Instead of prompting a big LLM once, it prompts a tiny LLM thousands of times.](https://www.reddit.com/r/MachineLearning/comments/1rn8g9a/p_nanojudge_instead_of_prompting_a_big_llm_once/) (Score: 36)
    *   Users debated the methodology, validity, and practical applications of a novel LLM evaluation approach that uses many small models for pairwise comparisons.
*   3. [[D] Image Augmentation in Practice: In-Distribution vs OOD Augmentations, TTA, and the Manifold View](https://i.redd.it/wsjk3r0xcmng1.jpeg) (Score: 22)
    *   A highly appreciated Medium article on practical aspects of image augmentation methods, specifically in-distribution vs. OOD augmentations and Test-Time Augmentation.
*   4. [[R] Graph-Oriented Generation (GOG): Replacing Vector R.A.G. for Codebases with Deterministic AST Traversal (70% Average Token Reduction)](https://www.reddit.com/r/MachineLearning/comments/1rmz1zr/r_graphoriented_generation_gog_replacing_vector/) (Score: 18)
    *   Introduction of GOG, a new method for code generation, with discussion focusing on its precision and a potential limitation in its initial keyword matching step.
*   5. [[D] Is it a reg flag that my PhD topic keeps changing every few months?](https://www.reddit.com/r/MachineLearning/comments/1rneeic/d_is_it_a_reg_flag_that_my_phd_topic_keeps/) (Score: 17)
    *   A discussion offering advice and reassurance to a PhD student concerned about frequent changes in their research topic, emphasizing the normalcy of exploration in early stages.
*   6. [[D] ISBI 2026 in London](https://www.reddit.com/r/MachineLearning/comments/1rmqs51/d_isbi_2026_in_london/) (Score: 1)
    *   An announcement about the ISBI 2026 conference, with a comment noting a peculiar experience regarding paper assignment to special sessions.

# Detailed Analysis by Thread
**[[P] VeridisQuo - open-source deepfake detector that combines spatial + frequency analysis and shows you where the face was manipulated (Score: 170)](https://i.redd.it/j51nr1pqomng1.gif)**
*   **Summary:** The discussion around VeridisQuo, an open-source deepfake detector, focused on its technical aspects, performance, and practical deployment. Users inquired about its integration with existing tools like ComfyUI, the datasets used for training and validation, and key metrics such as discovery and false positive rates. There was also interest in its resource requirements and potential for further development, including its use in improving deepfake methods. Overall, the project received positive feedback and suggestions for broader dissemination.
*   **Emotion:** The emotional tone is predominantly neutral, characterized by technical questions and analytical inquiries (average sentiment score ~0.67). However, there's a strong positive undertone from users expressing appreciation and encouraging wider promotion of the tool.
*   **Top 3 Points of View:**
    *   **Technical Specifications & Performance:** Users frequently asked for detailed technical information, including the datasets used for training and ground truth validation, specific performance metrics like discovery rate and false positive rate, and system resource requirements (e.g., RAM).
    *   **Practical Integration & Future Development:** Questions were raised about the detector's compatibility with other tools (like ComfyUI) and its potential evolution, such as whether it could be used as a feedback mechanism to improve deepfake generation methods.
    *   **Appreciation & Promotion:** The project received commendation for its effort, with users expressing positive feedback and suggesting cross-posting to other relevant communities like /r/stablediffusion and /r/singularity to maximize its visibility and impact.

**[[P] NanoJudge: Instead of prompting a big LLM once, it prompts a tiny LLM thousands of times. (Score: 36)](https://www.reddit.com/r/MachineLearning/comments/1rn8g9a/p_nanojudge_instead_of_prompting_a_big_llm_once/)**
*   **Summary:** This thread discussed NanoJudge, a novel approach to LLM evaluation that utilizes numerous prompts to a small LLM rather than a single prompt to a large one. The conversation revolved around the methodology's complexity, its comparative validity against larger models or human judgment, and its practical implications. Users questioned the necessity of its bias subtraction method, debated its calibration, and explored its potential advantages, particularly the robustness of pairwise comparisons in certain evaluation contexts.
*   **Emotion:** The overall emotional tone is predominantly neutral and analytical (average sentiment score ~0.64). Users expressed curiosity, skepticism, and critical assessment of the proposed methodology, often posing probing questions about its effectiveness and underlying principles.
*   **Top 3 Points of View:**
    *   **Skepticism Towards Methodological Complexity:** Some users questioned whether the complex bias subtraction techniques employed by NanoJudge were necessary, suggesting simpler alternatives like randomizing presentation order could achieve similar results.
    *   **Validity, Calibration, and Comparison to Other Models:** A significant point of discussion was the model's validity, how well its rankings align with expert judgment, and concerns about calibration issues. Users also questioned whether an ensemble of small models could truly capture the "knowledge" of larger, more powerful LLMs.
    *   **Advantages of Pairwise Comparison and Potential Use Cases:** Several users acknowledged the benefit of pairwise comparisons for robustness against prompt wording and calibration issues. The potential for NanoJudge in a two-tier evaluation system, where it filters top candidates for deeper analysis by stronger models, was also highlighted.

**[[D] Image Augmentation in Practice: In-Distribution vs OOD Augmentations, TTA, and the Manifold View (Score: 22)](https://i.redd.it/wsjk3r0xcmng1.jpeg)**
*   **Summary:** This thread points to an article delving into practical aspects of image augmentation, covering distinctions between in-distribution and out-of-distribution augmentations, Test-Time Augmentation (TTA), and a manifold perspective. The discussion, though brief, centers on the high utility of the shared content.
*   **Emotion:** The emotional tone is strongly positive (average sentiment score ~0.99). The single comment expresses significant appreciation for the article, highlighting its usefulness and rarity.
*   **Top 3 Points of View:**
    *   **High Value of Practical ML Content:** The dominant viewpoint is one of appreciation for well-written, practical, and useful articles in the machine learning domain, with the shared content being singled out for its quality and helpfulness.

**[[R] Graph-Oriented Generation (GOG): Replacing Vector R.A.G. for Codebases with Deterministic AST Traversal (70% Average Token Reduction) (Score: 18)](https://www.reddit.com/r/MachineLearning/comments/1rmz1zr/r_graphoriented_generation_gog_replacing_vector/)**
*   **Summary:** The post introduces Graph-Oriented Generation (GOG), a new research approach designed to replace Vector R.A.G. for codebases, achieving a 70% average token reduction through deterministic Abstract Syntax Tree (AST) traversal. The comment section focused on a specific perceived limitation of the method's initial phase.
*   **Emotion:** The emotional tone is neutral (average sentiment score ~0.77). The single comment provides a critical, analytical observation about a potential weakness of the method.
*   **Top 3 Points of View:**
    *   **Critique of Initial Keyword Matching:** The primary point of view identifies a potential weakness in GOG's methodology: while precise after the first step, its reliance on keyword matching for that initial step might not be robust enough for real-world codebases that often lack obvious keywords.

**[[D] Is it a reg flag that my PhD topic keeps changing every few months? (Score: 17)](https://www.reddit.com/r/MachineLearning/comments/1rneeic/d_is_it_a_reg_flag_that_my_phd_topic_keeps/)**
*   **Summary:** This discussion addresses a common concern among PhD students regarding frequent shifts in their research topic. The consensus among responders is largely reassuring, suggesting that such changes are often normal and beneficial, particularly in the initial exploratory phases of a PhD program. Advice frequently included open communication with supervisors, focusing on foundational coursework in the early years, and understanding that research inherently involves adaptation and problem discovery.
*   **Emotion:** The emotional tone is predominantly neutral and supportive (average sentiment score ~0.61). While not overtly joyful, comments offer practical advice, reassurance, and shared experiences, indicating a helpful and empathetic community response to a student's worries.
*   **Top 3 Points of View:**
    *   **Normalcy of Early PhD Topic Exploration:** Many users agreed that frequent topic changes are normal and even healthy in the first year or early stages of a PhD, as it represents a period of exploration, learning, and refining research interests.
    *   **Importance of Supervisor Guidance and Later Specialization:** While initial flexibility is accepted, advice emphasized the crucial role of communicating with supervisors about concerns and gradually narrowing down to a more fixed research direction after completing coursework or candidacy exams.
    *   **Research as an Adaptive Process:** The discussion highlighted that research is inherently dynamic and requires adaptation to new findings, unforeseen challenges (e.g., data availability), and evolving ideas, suggesting that the ability to pivot is a valuable skill in a PhD journey.

**[[D] ISBI 2026 in London (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1rmqs51/d_isbi_2026_in_london/)**
*   **Summary:** This thread is a brief announcement about the ISBI 2026 conference taking place in London. The sole comment reflects a user's personal experience of receiving a presentation email for the conference, noting an unusual detail about their paper being automatically assigned to two special sessions.
*   **Emotion:** The emotional tone is neutral (average sentiment score ~0.31). The comment is factual and observational, describing an event and a minor peculiarity without expressing strong positive or negative sentiment.
*   **Top 3 Points of View:**
    *   **Conference Logistics and Personal Experience:** The sole viewpoint describes a personal interaction with the conference logistics, specifically receiving an email about a presentation and a somewhat unexpected automatic assignment of a paper to multiple special sessions.
