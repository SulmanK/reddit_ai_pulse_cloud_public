---
title: "LocalLLaMA Subreddit"
date: "2025-05-02"
description: "Analysis of top discussions and trends in the localllama subreddit"
tags: ["LLM", "Local Models", "AI"]
---

# Overall Ranking and Top Discussions
1.  [[D] Qwen3 Fine-tuning now in Unsloth - 2x faster with 70% less VRAM](https://www.reddit.com/r/LocalLLaMA/comments/1kd531l/qwen3_finetuning_now_in_unsloth_2x_faster_with_70/) (Score: 159)
    *   The discussion revolves around the new Qwen3 fine-tuning capabilities within the Unsloth framework, highlighting its speed and reduced VRAM usage.
2.  [Qwen3 235B-A22B on a Windows tablet @ ~11.1t/s on AMD Ryzen AI Max 395+ 128GB RAM (Radeon 8060S iGPU-only inference, using 87.7GB out of 95.8GB total for 'VRAM')](https://v.redd.it/yct8as264eye1) (Score: 153)
    *   This thread discusses running the Qwen3 235B-A22B model on a Windows tablet, achieving a speed of ~11.1t/s using an AMD Ryzen AI Max 395+ with 128GB RAM and Radeon 8060S iGPU.
3.  [SOLO Bench - A new type of LLM benchmark I developed to address the shortcomings of many existing benchmarks](https://www.reddit.com/gallery/1kd50fl) (Score: 132)
    *   The thread introduces SOLO Bench, a new benchmark designed to evaluate LLMs, addressing the limitations of existing benchmarks.
4.  [California’s A.B. 412: A Bill That Could Crush Startups and Cement A Big Tech AI Monopoly](https://www.eff.org/deeplinks/2025/03/californias-ab-412-bill-could-crush-startups-and-cement-big-tech-ai-monopoly) (Score: 13)
    *   The thread discusses California’s A.B. 412 bill, which could potentially hinder startups and strengthen the dominance of large tech companies in the AI field.
5.  [Kinda lost with the Qwen3 MoE fixes.](https://www.reddit.com/r/LocalLLaMA/comments/1kd7dgs/kinda_lost_with_the_qwen3_moe_fixes/) (Score: 9)
    *   This thread discusses problems, fixes, and quant updates for the Qwen3 Mixture of Experts (MoE) model.
6.  [How to add token metrics to open webui?](https://www.reddit.com/r/LocalLLaMA/comments/1kd502d/how_to_add_token_metrics_to_open_webui/) (Score: 4)
    *   This thread asks for help on adding token metrics to the open webui.
7.  [I'm proud of myself for getting this to work](https://www.reddit.com/r/LocalLLaMA/comments/1kd8t3r/im_proud_of_myself_for_getting_this_to_work/) (Score: 2)
    *   This thread shows the poster being proud of making the 3b parameter local model work.
8.  [Local chat w/multiple human participants?](https://www.reddit.com/r/LocalLLaMA/comments/1kd7juk/local_chat_wmultiple_human_participants/) (Score: 1)
    *   This thread inquires about local chat solutions with multiple human participants, mentioning IRC chatbots for Ollama.
9.  [GPU/NPU accelerated inference on Android?](https://www.reddit.com/r/LocalLLaMA/comments/1kd9y8v/gpunpu_accelerated_inference_on_android/) (Score: 1)
    *   This thread is about GPU/NPU accelerated inference on Android, someone suggests layla on the app store.
10. [runnint local llms on android hexagon NPU.](https://www.reddit.com/r/LocalLLaMA/comments/1kd6v8u/runnint_local_llms_on_android_hexagon_npu/) (Score: 0)
    *   The thread discusses running local LLMs on Android using the Hexagon NPU.
11. [Cline + Qwen3 30b-8bit performance far worse than expected. Very surprising; think I might’ve set it up wrong. Any tips?](https://www.reddit.com/r/LocalLLaMA/comments/1kd78on/cline_qwen3_30b8bit_performance_far_worse_than/) (Score: 0)
    *   The thread asks for tips on running cline with qwen3 30b-8bit.
12. [Augment code backend? Claude?](https://www.reddit.com/r/LocalLLaMA/comments/1kd7ugp/augment_code_backend_claude/) (Score: 0)
    *   This thread asks about the backend models of Augment code, with some speculation that it could be Claude.
13. [Small models are funny](https://www.reddit.com/r/LocalLLaMA/comments/1kd9bfj/small_models_are_funny/) (Score: 0)
    *   This thread is about the performance of small language models and how they react to prompts.

# Detailed Analysis by Thread
**[[D] Qwen3 Fine-tuning now in Unsloth - 2x faster with 70% less VRAM (Score: 159)](https://www.reddit.com/r/LocalLLaMA/comments/1kd531l/qwen3_finetuning_now_in_unsloth_2x_faster_with_70/)**
*   **Summary:** This thread discusses the new Qwen3 fine-tuning capabilities within the Unsloth framework, highlighting its speed and reduced VRAM usage. Users express gratitude to the Unsloth team and inquire about optimization criteria, VRAM costs for training larger contexts, benchmarks, and potential issues with routing layers. There's also a question about converting technical reports into a dataset for AI training.
*   **Emotion:** The overall emotional tone is positive, with expressions of gratitude, excitement, and interest in the new features and optimizations. Neutral sentiments are also present, mainly related to technical inquiries.
*   **Top 3 Points of View:**
    *   Gratitude towards the Unsloth team for their work on optimizing Qwen3 fine-tuning.
    *   Inquiries about the technical aspects of the optimization, such as VRAM usage and routing layer implications.
    *   Seeking advice on migrating coding tasks from Claude to local solutions and creating datasets for specific AI tasks.

**[Qwen3 235B-A22B on a Windows tablet @ ~11.1t/s on AMD Ryzen AI Max 395+ 128GB RAM (Radeon 8060S iGPU-only inference, using 87.7GB out of 95.8GB total for 'VRAM') (Score: 153)](https://v.redd.it/yct8as264eye1)**
*   **Summary:** This thread discusses running the Qwen3 235B-A22B model on a Windows tablet, achieving a speed of ~11.1t/s using an AMD Ryzen AI Max 395+ with 128GB RAM and Radeon 8060S iGPU. Users share tips for getting ROCm to work, troubleshoot memory allocation issues, and inquire about battery feasibility and temperature concerns. Comparisons with Apple M-series chips and requests for batch size testing are also present.
*   **Emotion:** The emotional tone is mostly neutral, with users sharing technical information, asking questions, and expressing interest. There are also some positive sentiments, like "Super cool!" and "very interesting."
*   **Top 3 Points of View:**
    *   Achieving impressive performance with Qwen3 on a Windows tablet is possible with specific hardware and software configurations.
    *   ROCm can be made to work with tweaks, including following instructions from a specific GitHub repository and adjusting Windows pagefile size.
    *   Memory allocation and bandwidth are key factors in performance, with some users experiencing crashes and others suggesting batch size adjustments.

**[SOLO Bench - A new type of LLM benchmark I developed to address the shortcomings of many existing benchmarks (Score: 132)](https://www.reddit.com/gallery/1kd50fl)**
*   **Summary:** This thread introduces SOLO Bench, a new benchmark designed to evaluate LLMs, addressing the limitations of existing benchmarks. Users commend the work, discuss the performance of various models (like Gemini and Qwen), and suggest improvements such as adding more models, using a dictionary database, and exploring constrained generation. The author also shares insights into models refusing to participate and variations in scores.
*   **Emotion:** The emotional tone is generally positive and interested, with users praising the benchmark, asking questions, and suggesting enhancements. There's also a neutral tone in technical discussions and observations.
*   **Top 3 Points of View:**
    *   SOLO Bench is a valuable contribution to LLM evaluation, addressing shortcomings of existing benchmarks.
    *   Gemini Pro performs well on this benchmark.
    *   Suggestions for improvement include adding more models, using a dictionary database, and exploring constrained generation.

**[California’s A.B. 412: A Bill That Could Crush Startups and Cement A Big Tech AI Monopoly (Score: 13)](https://www.eff.org/deeplinks/2025/03/californias-ab-412-bill-could-crush-startups-and-cement-big-tech-ai-monopoly)**
*   **Summary:** The thread discusses California’s A.B. 412 bill, which could potentially hinder startups and strengthen the dominance of large tech companies in the AI field. Users express concerns that the bill would drive businesses out of California and exclude residents from using AI tools.
*   **Emotion:** The emotional tone is a mix of positive and neutral. Positive in the sense of trying to help the situation, but also neutral in discussing the potential impacts of the bill.
*   **Top 3 Points of View:**
    *   The bill could harm startups and give big tech companies a monopoly in the AI space.
    *   The bill may lead to businesses leaving California.
    *   The bill could exclude California residents from using AI tools.

**[Kinda lost with the Qwen3 MoE fixes. (Score: 9)](https://www.reddit.com/r/LocalLLaMA/comments/1kd7dgs/kinda_lost_with_the_qwen3_moe_fixes/)**
*   **Summary:** This thread discusses problems, fixes, and quant updates for the Qwen3 Mixture of Experts (MoE) model. Users suggest using Bartowski's quants and highlight improvements from Unsloth's bug-fixing quants. Some users also express confusion and question downvotes on specific comments.
*   **Emotion:** The emotional tone is mostly neutral, with users providing recommendations and reporting on model performance. There's some positive sentiment related to the improved model quality after the fixes.
*   **Top 3 Points of View:**
    *   Bartowski's quants are a reliable option for Qwen3 MoE.
    *   Unsloth's bug-fixing quants have significantly improved the Qwen3-30B-A3B model.
    *   There is some confusion and concern regarding downvotes on specific comments.

**[How to add token metrics to open webui? (Score: 4)](https://www.reddit.com/r/LocalLLaMA/comments/1kd502d/how_to_add_token_metrics_to_open_webui/)**
*   **Summary:** This thread asks for help on adding token metrics to the open webui. One comment says that it only works for ollama as the backend, but you can use a function called "advanced metrics" to get that info.
*   **Emotion:** The emotional tone is mostly neutral, with users asking questions and seeking solutions. There's some positive sentiment related to interest in learning how to add token metrics.
*   **Top 3 Points of View:**
    *   Users are interested in tracking token metrics within the open webui.
    *   The "advanced metrics" function in ollama might provide some of the desired information.
    *   Finding a solution for LiteLLM is also a concern.

**[I'm proud of myself for getting this to work (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1kd8t3r/im_proud_of_myself_for_getting_this_to_work/)**
*   **Summary:** This thread shows the poster being proud of making the 3b parameter local model work.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   The users are proud that the 3b parameter local model works.

**[Local chat w/multiple human participants? (Score: 1)](https://www.reddit.com/r/LocalLLaMA/comments/1kd7juk/local_chat_wmultiple_human_participants/)**
*   **Summary:** This thread inquires about local chat solutions with multiple human participants, mentioning IRC chatbots for Ollama.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   There is a desire for local chat solutions involving multiple human participants.
    *   IRC chatbots for Ollama might be a viable option.

**[GPU/NPU accelerated inference on Android? (Score: 1)](https://www.reddit.com/r/LocalLLaMA/comments/1kd9y8v/gpunpu_accelerated_inference_on_android/)**
*   **Summary:** This thread is about GPU/NPU accelerated inference on Android, someone suggests layla on the app store.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Users are asking about GPU/NPU accelerated inference on Android
    *   Layla on the appstore has a logo that is a butterfly

**[runnint local llms on android hexagon NPU. (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1kd6v8u/runnint_local_llms_on_android_hexagon_npu/)**
*   **Summary:** The thread discusses running local LLMs on Android using the Hexagon NPU. One comment suggests trying a different app and starting with a smaller model.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Users are attempting to run local LLMs on Android using the Hexagon NPU.
    *   Starting with a smaller model is recommended for testing.
    *   Trying a different app might resolve potential issues.

**[Cline + Qwen3 30b-8bit performance far worse than expected. Very surprising; think I might’ve set it up wrong. Any tips? (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1kd78on/cline_qwen3_30b8bit_performance_far_worse_than/)**
*   **Summary:** The thread asks for tips on running cline with qwen3 30b-8bit. The Qwen3 series is not tuned for coding specifically, one user says.
*   **Emotion:** The emotional tone is mostly positive, but there is some confusion.
*   **Top 3 Points of View:**
    *   Users need tips on how to get qwen3 30b-8bit to work.
    *   Qwen3 series is not tuned for coding specifically
    *   The 30B-A3B one is an MoE model, which is fast but can't compare to the 32B version on performance.

**[Augment code backend? Claude? (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1kd7ugp/augment_code_backend_claude/)**
*   **Summary:** This thread asks about the backend models of Augment code, with some speculation that it could be Claude.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Users are curious about the backend model used by Augment code.
    *   There is speculation that Claude might be the backend model.
    *   Augment code's agent logic is considered better than Cursor's.

**[Small models are funny (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1kd9bfj/small_models_are_funny/)**
*   **Summary:** This thread is about the performance of small language models and how they react to prompts. One user passes the prompt into gemma3:1b and likes the results.
*   **Emotion:** The emotional tone is neutral.
*   **Top 3 Points of View:**
    *   Users are testing the performance of small language models
    *   The user might be confusing the two.
    *   gemma3:1b is a small language model that produces coherent summaries
