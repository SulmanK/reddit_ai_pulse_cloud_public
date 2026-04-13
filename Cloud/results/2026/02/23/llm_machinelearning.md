---
title: "Machine Learning Subreddit"
date: "2026-02-23"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machine learning", "conferences", "research", "LLMs", "peer review"]
---

# Overall Ranking and Top Discussions
*   1. [[D] Is Conference prestige slowing reducing?](https://i.redd.it/66xzqzcu95lg1.png) (Score: 666)
    *   The discussion explores whether the prestige of machine learning conferences is declining due to issues like lack of expert review, oversaturation, and challenges in handling the increasing scale of research.
*   2. [[R] Neural PDE solvers built (almost) purely from learned warps](https://www.reddit.com/r/MachineLearning/comments/1rcgmrh/r_neural_pde_solvers_built_almost_purely_from/) (Score: 45)
    *   People were discussing new architectures that use qualities of the data more efficiently, with excitement for the warp-based approach and its potential applications.
*   3. [[D] Is the move toward Energy-Based Models for reasoning a viable exit from the "hallucination" trap of LLMs?](https://www.reddit.com/r/MachineLearning/comments/1rco6go/d_is_the_move_toward_energybased_models_for/) (Score: 31)
    *   The conversation revolves around whether Energy-Based Models (EBMs) can provide a solution to the hallucination problem in Large Language Models (LLMs).
*   4. [[D] CVPR results shock due to impressive score drop since reviews](https://www.reddit.com/r/MachineLearning/comments/1rcb3sa/d_cvpr_results_shock_due_to_impressive_score_drop/) (Score: 27)
    *   Not even 2 years ago, a decent enough idea could get into these conferences.
*   5. [[R] CVPR results](https://www.reddit.com/r/MachineLearning/comments/1rc2dm2/r_cvpr_results/) (Score: 8)
    *   Reviewers were really good this time round with thoughtful questions/clarifications.
*   6. [[D] ACL Januray ARR problem with reviewer](https://www.reddit.com/r/MachineLearning/comments/1rcpymj/d_acl_januray_arr_problem_with_reviewer/) (Score: 2)
    *   This happens all the time and is just part of the process.
*   7. [[D] WACV 2026- Queries Regarding Virtual presentation](https://www.reddit.com/r/MachineLearning/comments/1rcb92i/d_wacv_2026_queries_regarding_virtual_presentation/) (Score: 1)
    *   I think it's only online.
*   8. [[D] SIGIR 2026 Reviews are (likely) done. Why the delay in releasing scores?](https://www.reddit.com/r/MachineLearning/comments/1rccyev/d_sigir_2026_reviews_are_likely_done_why_the/) (Score: 1)
    *   I received a mail (since i reviewed a few papers) today that the discussion phase has begun, this is solely between the reviewers and the SPC's.
*   9. [[D] I wish papers could at least be judged in part by code quality (usability) for conference submissions.](https://www.reddit.com/r/MachineLearning/comments/1rcpxb3/d_i_wish_papers_could_at_least_be_judged_in_part/) (Score: 0)
    *   I fully endorse the open-source initiatives, but sharing the code is always encouraged, but never required.

# Detailed Analysis by Thread
**[ [D] Is Conference prestige slowing reducing? (Score: 666)](https://i.redd.it/66xzqzcu95lg1.png)**
*  **Summary:** The way conferences are run is not able to handle the change in scale. The biggest problem is the lack of actual expert review. AI is a big topic, applicable in many areas. Acceptance rate hasn't changed much. There is more research. There are too many people working on AI. It doesn't make sense that there are no specialized conferences except 3D computer vision. trying to run any code bases of those papers should be a new way of torturing people In such a situation, papers in lower-tier conferences are simply dismissed, despite the fact that many of them may be just as solid. Conference prestige is playing a bigger role than the true contribution of the paper. People still want to publish at and attend prestigious conferences. Papers published there are still highly cited. Conferences are too high-latency to behave like arXiv. Acceptance and rejection has always been viewed differently depending on the researchers involved. Conferences still yield meaningful progress, even though the bar is still high. BTW, I really like this meme with Buzz. Represents the current situation very well. Me with no paper published cries in the corner. The only thing that matters is building and releasing working code.
*  **Emotion:** The emotional tone is mixed, with 4 negative, 5 neutral, and 1 positive sentiments. The overall average sentiment score is 0.53, indicating a slight leaning towards positive.
*  **Top 3 Points of View:**
    * Conference prestige is reducing due to lack of expert review, oversaturation, and inability to handle the scale of research, leading to false or unreproducible results.
    * Despite challenges, prestigious conferences still hold value for publication and citation, and the 'bar is still high' for acceptance.
    * The current system faces problems like reviewer bias, lack of reproducibility of code, and difficulty in assessing novel but unclear papers, suggesting a need for systemic change.

**[ [R] Neural PDE solvers built (almost) purely from learned warps (Score: 45)](https://www.reddit.com/r/MachineLearning/comments/1rcgmrh/r_neural_pde_solvers_built_almost_purely_from/)**
*  **Summary:** There are new architectures that use qualities of the data more efficiently. I am in real-time computer graphics and the method could be applied to a lot of problems here. Have you tried testing this concept on more advanced PDEs like e.g. weather prediction or some part of it? You mentioned that during long roll-out you see poorer performance, didn’t read the paper yet so the answer might me inside, but do you have any clues why? I had the same reaction. What changed my mind was realizing that execution details and feedback loops decide most real-world results. Once you instrument your workflow and iterate on concrete failure cases, outcomes get way more consistent. The warp-based approach here is brilliant—I’ve been wrestling with spectral methods in my own work, and seeing this perform so well on stiff problems like diffusion is genuinely exciting. Can’t wait to dig into the code this weekend.
*  **Emotion:** The emotional tone is mixed, with 2 positive and 2 neutral sentiments. The overall average sentiment score is 0.68, indicating a slight leaning towards positive.
*  **Top 3 Points of View:**
    * The warp-based approach is considered brilliant and exciting for its efficiency and potential application in various fields like computer graphics.
    * Questions arise regarding the computational efficiency, especially with memory-bound operations, and comparisons to other methods like Transformer-stack solutions.
    * Users are interested in the method's performance on more advanced PDEs (e.g., weather prediction) and understanding reasons for poorer performance during long roll-outs.

**[ [D] Is the move toward Energy-Based Models for reasoning a viable exit from the "hallucination" trap of LLMs? (Score: 31)](https://www.reddit.com/r/MachineLearning/comments/1rco6go/d_is_the_move_toward_energybased_models_for/)**
*  **Summary:** Building new paradigms while ignoring interpretability does not solve the fundamental problems we are having. However the approach is interesting and I support any divergence from the main focal point. Energybased models can improve performance but often require more computational resources. Focus on balancing efficiency with the specific needs of your application. Evaluate the tradeoffs based on your project's requirements to find the right fit. I’ve been working with EBMs on a small reasoning dataset and the shift from chasing the next token to minimizing a global energy function feels like a fundamentally different, more constrained optimization process. It hasn’t eliminated hallucinations for me, but it does make the model's confidence in its output much more interpretable. I feel it is too computationally expensive at the moment. Modeling the entire energy landscape and making gradient descent calculations require orders of magnitude more memory than current LLMs. Also there is the issue of parallelization and getting them to actually utilize the current hardware stack we have dug ourselves a hole with. Sorry, what would EBMs reduce hallucinations? I think the way to reduce hallucinations will be to get agents a better internal state, train them by letting them interact in the world once continuous learning is working and so get them a better sense for consistency and context. I don't buy that EBMs solve hallucination either. Diffusion models certainly hallucinate just as much as autoregressive transformers, and they're very similar to EBMs. I think hallucination is a failure mode of statistics *as a whole* - when it's wrong, it's approximately wrong in plausible ways - and can't be solved by tweaking architectures. EBMs provide a nice framework for test-time search and scaling, but they are probabilistic generative models subject to the same pitfalls as LLMs, diffusion models and others like them. The role of EBMs is already somewhat filled by reward models, and that's
*  **Emotion:** The emotional tone is mixed, with 3 positive, 2 negative, and 2 neutral sentiments. The overall average sentiment score is 0.70, indicating a slight leaning towards positive.
*  **Top 3 Points of View:**
    * EBMs are seen as a promising new paradigm that might offer more interpretable confidence in output and a fundamentally different optimization process than autoregressive models.
    * Skepticism exists regarding EBMs' ability to solve hallucinations, as they are still probabilistic generative models and diffusion models (similar to EBMs) also hallucinate.
    * Concerns are raised about the computational expense and memory requirements of EBMs, as well as challenges in parallelization and hardware utilization.

**[ [D] CVPR results shock due to impressive score drop since reviews (Score: 27)](https://www.reddit.com/r/MachineLearning/comments/1rcb3sa/d_cvpr_results_shock_due_to_impressive_score_drop/)**
*  **Summary:** Not even 2 years ago, a decent enough idea could get into these conferences. Now it's very competitive and the area is oversatured. Your paper needs to be flawless and convincing to get into the conference. Wouldn't referring to an outside benchmark submission in the manuscript violate the anonymity of the paper? Did you get the findings workshop? Reviewer 2 dropped from 4 to 2 after a rebuttal where you addressed their concerns point-by-point. The online benchmark thing is especially maddening since platform submissions often take weeks. Some ACs were more involved this year than in previous years. On some papers, the AC wanted the reviewers to come to a consensus and not stay borderline. The current conference system is about to collapse. Everyone is coerced into reviewing. I didn't get it. Did you eventually include the result from the missing benchmark?
*  **Emotion:** The discussion is predominantly neutral. The discussion primarily maintains a factual or objective stance (average score: 0.68). Some comments also show negative sentiments.
*  **Top 3 Points of View:**
    * The review process for CVPR is perceived as highly competitive and oversaturated, making it exceptionally difficult for papers to get accepted, even with good initial scores.
    * Reviewers may be biased or influenced by the competitive environment, potentially lowering scores punitively or due to the pressure to force a decision.
    * The lack of transparency and inconsistency in reviewer feedback, especially concerning rebuttals and benchmark requirements, is a significant source of frustration.

**[ [R] CVPR results (Score: 8)](https://www.reddit.com/r/MachineLearning/comments/1rc2dm2/r_cvpr_results/)**
*  **Summary:** Reviewers were really good this time round with thoughtful questions/clarifications. Honestly didn’t expect an accept with the initial scores and only found out when my co-authors told me results were out. 2 reviewers were irresponsible even though they checked themselves as experts. review comments weren't deep enough and didn't update the final scores after the rebuttal. However, ac read the rebuttal thoroughly, and then made a decision. Well I had 542 before rebuttal, changed to 544 after, AC simply rejected both the paper, reviewers and the rebuttal for absolutely baseless reasons. The reviewer who liked the method lowered his score from 6/5/4/4 to 4/2/2. Receiving a review is more important than arguing it. Receiving the review clarifies misunderstandings. 5/4/2 -> 5/3/2 Rejection, recommended for findings. Papers "seem novel, but some points are unclear" are easier to reject than papers "not exciting, but with comprehensive standard experiments." CVPR should open an "alternative perspectives" track to papers that challenge common community beliefs. ACs discussed and find reviewer concerns addressed hence we recommend acceptance The amount of AI generated slop is alarming, it was clear reviewer didn’t even know what he asked for the first time and didn’t understand the domain 443, rebuttals works. AC found the reviewer giving 3 didnt respond, and all of the concerns were addressed in the rebuttal so suggestted acceptance
*  **Emotion:** The discussion is predominantly neutral. The discussion primarily maintains a factual or objective stance (average score: 0.58). Some comments also show negative and positive sentiments.
*  **Top 3 Points of View:**
    * The CVPR review process is inconsistent and often frustrating, with some reviewers being irresponsible or unfair in their scoring and feedback.
    * Rebuttals can sometimes matter, clarifying misunderstandings and leading to acceptance, but often reviewers don't respond or scores are lowered despite addressed concerns.
    * There's a negative trend where novel but unclear papers are more easily rejected, and a wish for alternative tracks to encourage challenging community beliefs.

**[ [D] ACL Januray ARR problem with reviewer (Score: 2)](https://www.reddit.com/r/MachineLearning/comments/1rcpymj/d_acl_januray_arr_problem_with_reviewer/)**
*  **Summary:** Write a message to the meta reviewer. Flip a misconduct reviewer is doable with good evidences This happens all the time and is just part of the process. It's helpful to cite other published work to back up their baselessness.
*  **Emotion:** The discussion primarily maintains a factual or objective stance (average score: 0.81).
*  **Top 3 Points of View:**
    * Reviewer misconduct or unfair reviews are common in the process, and authors should respond during rebuttal to clarify misunderstandings or provide evidence.
    * If reviews are egregious (e.g., LLM-generated, baseless), contacting the area chair (meta reviewer) with good evidence is a possible course of action.
    * Authors often feel pressured to perform proposed experiments even if they don't make sense, just to meet reviewer expectations.

**[ [D] WACV 2026- Queries Regarding Virtual presentation (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1rcb92i/d_wacv_2026_queries_regarding_virtual_presentation/)**
*  **Summary:** I think it's only online. The best thing you can do is to promote your work on social media or have someone else hang the poster and present it for you. Low chance that people will go into the platform unless they have a paper recommendation.
*  **Emotion:** The overall emotional tone is consistently positive (average score: 0.46).
*  **Top 3 Points of View:**
    * The conference is likely only online, which limits in-person engagement.
    * Authors should promote their work on social media or have a representative present a poster on their behalf.
    * There's a low likelihood of audience engagement on the virtual platform without strong recommendations.

**[ [D] SIGIR 2026 Reviews are (likely) done. Why the delay in releasing scores? (Score: 1)](https://www.reddit.com/r/MachineLearning/comments/1rccyev/d_sigir_2026_reviews_are_likely_done_why_the/)**
*  **Summary:** I received a mail (since i reviewed a few papers) today that the discussion phase has begun, this is solely between the reviewers and the SPC's. Also they do not mention a timeline as such, so I have no clue when the scores would be released...
*  **Emotion:** The discussion primarily maintains a factual or objective stance (average score: 0.80).
*  **Top 3 Points of View:**
    * The discussion phase between reviewers and SPCs has begun, indicating the review process is in an advanced stage.
    * There is no clear timeline for when scores will be released, causing uncertainty for authors.
    * Reviewers (and authors) are aware of the delay but do not have additional information about its cause.

**[ [D] I wish papers could at least be judged in part by code quality (usability) for conference submissions. (Score: 0)](https://www.reddit.com/r/MachineLearning/comments/1rcpxb3/d_i_wish_papers_could_at_least_be_judged_in_part/)**
*  **Summary:** I fully endorse the open-source initiatives, but sharing the code is always encouraged, but never required. The real crisis is that a paper should be self-contained so that readers can reproduce it independently. This is the golden standard in bioscience and physics. you're lucky if there's a github repo at all, there isnt always!! Reproducibility first for me
*  **Emotion:** The emotional tone is mixed, with 1 positive and 2 neutral sentiments. The overall average sentiment score is 0.77, indicating a slight leaning towards positive.
*  **Top 3 Points of View:**
    * There's a strong desire for code quality and reproducibility to be a factor in paper judgment, especially for industry relevance.
    * The current open-source initiatives, where code sharing is encouraged but not required, are seen by some as a good balance, driven by impact/citations.
    * Many papers lack readily available or working code, making reproducibility a significant challenge and highlighting a gap in current publishing standards.
