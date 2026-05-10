---
title: "LocalLLaMA Subreddit"
date: "2026-05-10"
description: "Analysis of top discussions and trends in the localllama subreddit"
tags: ["LLaMA", "AI", "LocalLLaMA", "LLMs"]
---

# Overall Ranking and Top Discussions

*   1.  [[D] Getting a feel for how fast X tokens/second really is.](https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/) (Score: 190)
    *   This post discusses the perceived speed of token generation in local LLMs and how to visualize it, with users sharing their thoughts on what constitutes a usable speed and offering alternative tools.
*   2.  [[D] NCCL-Free Tensor Parallelism on Dual Blackwell PCIe llama.cpp b9095 released!](https://www.reddit.com/r/LocalLLaMA/comments/1t96l6r/ncclfree_tensor_parallelism_on_dual_blackwell/) (Score: 24)
    *   This thread announces the release of NCCL-Free Tensor Parallelism for llama.cpp and discusses its performance implications, particularly on dual Blackwell GPUs, with users sharing benchmark results and potential trade-offs.
*   3.  [[D] DeepSeek-V4-Flash W4A16+FP8 with MTP self-speculation: 85 tok/s @ 524k on 2× RTX PRO 6000 Max-Q](https://www.reddit.com/r/LocalLLaMA/comments/1t9em98/deepseekv4flash_w4a16fp8_with_mtp_selfspeculation/) (Score: 23)
    *   This post highlights impressive token generation speeds with a specific model and configuration, sparking discussions about performance on different hardware and the potential of MTP.
*   4.  [[D] Anybody else noticing how good gemma-4-26b-a4b is with one-shotting three.js?](https://www.reddit.com/r/LocalLLaMA/comments/1t9cle9/anybody_else_noticing_how_good_gemma426ba4b_is/) (Score: 17)
    *   Users are discussing the capabilities of the gemma-4-26b-a4b model, particularly its effectiveness in generating code for three.js, with appreciation for its "magical" performance.
*   5.  [[D] Speeding up local LLM for usable coding agent](https://www.reddit.com/r/LocalLLaMA/comments/1t96kfh/speeding_up_local_llm_for_usable_coding_agent/) (Score: 14)
    *   This thread focuses on optimizing local LLMs for coding agent tasks, with users sharing their configurations, speed benchmarks, and advice on GPU offloading and CPU utilization.
*   6.  [[D] MTP benchmark results: the nature of the generative task dictates whether you will benefit (coding) or get slower inference (creative) from speculative inference. No other factor comes close.](https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/) (Score: 12)
    *   This discussion explores the performance of MTP (speculative inference), highlighting that its benefits are task-dependent, with coding tasks showing improvements while creative tasks may see slower inference.
*   7.  [[D] DS4](https://www.reddit.com/r/LocalLLaMA/comments/1t95k73/ds4/) (Score: 10)
    *   Users are discussing the DS4 model, sharing initial impressions and hopes for its integration with llama.cpp, with some expressing caution about download size and performance.
*   8.  [[D] Hermes Agent is now #1 most used globally in past 24 hours in Openrouter global token metrics, above Claude Code and OpenClaw.](https://www.reddit.com/r/LocalLLaMA/comments/1t9gid2/hermes_agent_is_now_1_most_used_globally_in_past/) (Score: 29)
    *   This post highlights Hermes Agent's top ranking on OpenRouter, leading to discussions about its actual utility, comparison with other tools, and skepticism about the metric's relevance.
*   9.  [[D] Running Qwen3.6 35b a3b on 8gb vram and 32gb ram ~190k context](https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/) (Score: 29)
    *   Users are sharing their experiences and configurations for running the Qwen3.6 35b model on limited hardware, discussing performance trade-offs and model quality.
*   10. [[D] Switched from OpenCode to Pi - What Settings/Plugins would you recommend?](https://www.reddit.com/r/LocalLLaMA/comments/1t9fta2/switched_from_opencode_to_pi_what_settingsplugins/) (Score: 6)
    *   This thread is about user recommendations for settings and plugins after switching from OpenCode to Pi, with discussions on plugins, compound engineering skills, and subagents.
*   11. [[D] I cannot decide for local OCR model for most of the tasks preferably I would like more individual experiences than reviews.](https://www.reddit.com/r/LocalLLaMA/comments/1t993om/i_cannot_decide_for_local_ocr_model_for_most_of/) (Score: 3)
    *   Users are seeking recommendations for local OCR models, sharing their experiences with various options like DeepSeek OCR, Paddle OCR, and Gemma-4-26B-A4B, discussing their strengths and weaknesses.
*   12. [[D] LM Studio / Windows / Vulkan possible to prioritize GPU order?](https://www.reddit.com/r/LocalLLaMA/comments/1t975bx/lm_studio_windows_vulkan_possible_to_prioritize/) (Score: 4)
    *   This post discusses the possibility of prioritizing GPU order in LM Studio on Windows with Vulkan, with users sharing tuning advice for better performance.
*   13. [[D] Building out my tool library, any recommendations? I just added email capability and im starting to get hyped!](https://www.reddit.com/r/LocalLLaMA/comments/1t97163/building_out_my_tool_library_any_recommendations/) (Score: 2)
    *   Users are sharing recommendations for building out their tool libraries, discussing tool selection with LLMs and the effectiveness of different models for specific tasks like web search and email.
*   14. [[D] How does llama-server pick which MoE experts go on the GPU and which stay on the CPU?](https://www.reddit.com/r/LocalLLaMA/comments/1t9fy74/how_does_llamaserver_pick_which_moe_experts_go_on/) (Score: 2)
    *   This thread delves into the technical details of how llama-server manages Mixture-of-Experts (MoE) models, discussing parameter fitting, expert distribution, and the performance impact of CPU/GPU allocation.
*   15. [[D] Is HIPfire worth it for Strix Halo?](https://www.reddit.com/r/LocalLLaMA/comments/1t9gmyq/is_hipfire_worth_it_for_strix_halo/) (Score: 3)
    *   A brief discussion on whether HIPfire is currently worth using for Strix Halo, with the recommendation to use llamacpp with MTP for now.

# Detailed Analysis by Thread

**[ Getting a feel for how fast X tokens/second really is. (Score: 190)](https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/)**
*   **Summary:** Users are discussing and visualizing the speed of token generation in local LLMs, aiming to understand what constitutes a "fast" or "usable" speed. Discussions touch on different model speeds and the subjective experience of using them.
*   **Emotion:** Primarily Positive, with a strong sense of shared interest and appreciation for the tool presented.
*   **Top 3 Points of View:**
    *   Appreciation for the visualization tool and its clarity in demonstrating token speeds.
    *   Discussion on what token speeds are considered "usable" for different tasks (chat, coding, multi-agent).
    *   Suggestions for community showcases for such projects to prevent them from being lost.

**[ Hermes Agent is now #1 most used globally in past 24 hours in Openrouter global token metrics, above Claude Code and OpenClaw. (Score: 29)](https://www.reddit.com/r/LocalLLaMA/comments/1t9gid2/hermes_agent_is_now_1_most_used_globally_in_past/)**
*   **Summary:** The post claims Hermes Agent is the most used globally on OpenRouter based on token metrics, sparking debate about the validity of these metrics and the efficiency of the agent.
*   **Emotion:** Mixed, with skepticism and critical viewpoints clashing with the initial claim.
*   **Top 3 Points of View:**
    *   Skepticism that high token usage per day is a reliable metric for tool success, comparing it to lines of code for programmers.
    *   Questioning the relevance of OpenRouter metrics, especially when many users might not use it.
    *   Inquiries about suitable local LLMs to use with Hermes Agent on consumer hardware.

**[ Running Qwen3.6 35b a3b on 8gb vram and 32gb ram ~190k context (Score: 29)](https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/)**
*   **Summary:** Users are sharing their experiences and configurations for running the Qwen3.6 35b model on hardware with limited VRAM (8GB) and moderate RAM (32GB), aiming for large contexts.
*   **Emotion:** Largely Positive, with users appreciating the shared information and discussing performance on their own setups.
*   **Top 3 Points of View:**
    *   Appreciation for the post providing valuable information for running large models on consumer hardware.
    *   Discussion on the trade-off between model size/speed and output quality, with some finding the 35B model's results "noticeably dumber" than smaller ones.
    *   Sharing of specific configurations and performance metrics (tokens/sec) with different quantizations and settings.

**[ NCCL-Free Tensor Parallelism on Dual Blackwell PCIe llama.cpp b9095 released! (Score: 24)](https://www.reddit.com/r/LocalLLaMA/comments/1t96l6r/ncclfree_tensor_parallelism_on_dual_blackwell/)**
*   **Summary:** This thread announces the release of NCCL-Free Tensor Parallelism for llama.cpp and discusses its performance implications, especially on dual Blackwell GPUs, with users sharing benchmark results and potential trade-offs in context size and prompt processing.
*   **Emotion:** Neutral to Positive, with a focus on technical evaluation and benchmark sharing.
*   **Top 3 Points of View:**
    *   Users are sharing benchmark results comparing different configurations (with/without NCCL, MTP) and noting performance gains in token generation.
    *   Discussion on potential trade-offs, such as reduced context window size (from 83k to 32k) when using tensor split, impacting coding agent workloads.
    *   Questions arise about the general applicability of NCCL-Free for non-Nvidia hardware and its compatibility with specific GPU setups (P40s, 3090s, Mi50s).

**[ DeepSeek-V4-Flash W4A16+FP8 with MTP self-speculation: 85 tok/s @ 524k on 2× RTX PRO 6000 Max-Q (Score: 23)](https://www.reddit.com/r/LocalLLaMA/comments/1t9em98/deepseekv4flash_w4a16fp8_with_mtp_selfspeculation/)**
*   **Summary:** The post highlights impressive token generation speeds (85 tok/s) for DeepSeek-V4-Flash with MTP self-speculation on high-end hardware, prompting discussions about performance on different setups and specific flags.
*   **Emotion:** Primarily Positive and Enthusiastic, with a sense of awe at the reported performance.
*   **Top 3 Points of View:**
    *   Enthusiastic reactions to the high token generation speed achieved with the specified model and configuration.
    *   Comparisons of performance on significantly lower-end hardware (e.g., a Thinkpad laptop) showing much slower speeds.
    *   Technical questions regarding specific flags and their applicability to different hardware configurations.

**[ Anybody else noticing how good gemma-4-26b-a4b is with one-shotting three.js? (Score: 17)](https://www.reddit.com/r/LocalLLaMA/comments/1t9cle9/anybody_else_noticing_how_good_gemma426ba4b_is/)**
*   **Summary:** Users are discussing the impressive ability of the gemma-4-26b-a4b model to generate functional code for three.js with just a single prompt example.
*   **Emotion:** Positive and Appreciative, with users expressing admiration for the model's capabilities.
*   **Top 3 Points of View:**
    *   High praise for the gemma-4-26b-a4b model's "magical" performance in one-shot code generation for three.js.
    *   Interest in the concept of using generative demos as a learning tool.
    *   Sharing of similar projects and future plans to integrate three.js functionality.

**[ Speeding up local LLM for usable coding agent (Score: 14)](https://www.reddit.com/r/LocalLLaMA/comments/1t96kfh/speeding_up_local_llm_for_usable_coding_agent/)**
*   **Summary:** This thread is dedicated to optimizing local LLMs for coding agent tasks, with users sharing their configurations, speed tests, and advice on hardware utilization, particularly concerning GPU offloading and CPU management.
*   **Emotion:** Neutral to Positive, focused on problem-solving and performance optimization.
*   **Top 3 Points of View:**
    *   Users are sharing their personal benchmark results and configurations for achieving higher tokens/sec on their specific hardware.
    *   Advice is given on optimizing GPU offload, CPU usage for MoE experts, and distinguishing between prompt processing and token generation speeds.
    *   Recommendations are made to use llama.cpp or Jan over LM Studio for better performance and optimizations.

**[ MTP benchmark results: the nature of the generative task dictates whether you will benefit (coding) or get slower inference (creative) from speculative inference. No other factor comes close. (Score: 12)](https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/)**
*   **Summary:** This discussion analyzes the performance of MTP (speculative inference), concluding that its benefits are highly dependent on the generative task, with coding tasks showing improvements and creative tasks potentially experiencing slower inference.
*   **Emotion:** Neutral, focused on technical analysis and reporting of benchmark findings.
*   **Top 3 Points of View:**
    *   The primary conclusion is that MTP's effectiveness is task-specific (coding benefits, creative suffers).
    *   Concerns are raised about significant slowdowns in prompt processing (PP) speeds with MTP implementations, which may negate generation speedups.
    *   Limitations like the inability to perform parallel requests or image decoding are mentioned as drawbacks for wider adoption.

**[ DS4 (Score: 10)](https://www.reddit.com/r/LocalLLaMA/comments/1t95k73/ds4/)**
*   **Summary:** Users are discussing the DS4 model, sharing initial impressions and their hopes for its integration with the llama.cpp framework. Some express reservations about the model's large download size and potential performance issues.
*   **Emotion:** Mixed, with positive excitement about the model's potential tempered by concerns about practical implementation and performance.
*   **Top 3 Points of View:**
    *   Positive early impressions of DS4's performance on high-end hardware (M5 Max 128GB).
    *   Hope for llama.cpp support for the DS4 model.
    *   Concerns about the large model size (150GB) and whether it will perform well compared to existing smaller models.

**[ Switched from OpenCode to Pi - What Settings/Plugins would you recommend? (Score: 6)](https://www.reddit.com/r/LocalLLaMA/comments/1t9fta2/switched_from_opencode_to_pi_what_settingsplugins/)**
*   **Summary:** Users are asking for and sharing recommendations for settings and plugins for the Pi agent after switching from OpenCode, discussing specific plugins and their effectiveness.
*   **Emotion:** Neutral to Positive, with users actively seeking and sharing practical advice.
*   **Top 3 Points of View:**
    *   Recommendations for specific plugins like "pi-subagents" and "little-coder" for enhanced functionality.
    *   Discussion on the need for compound engineering skills to get the best results.
    *   Some users express very negative opinions of OpenCode ("piece of shit").

**[ I cannot decide for local OCR model for most of the tasks preferably I would like more individual experiences than reviews. (Score: 3)](https://www.reddit.com/r/LocalLLaMA/comments/1t993om/i_cannot_decide_for_local_ocr_model_for_most_of/)**
*   **Summary:** Users are seeking recommendations for local OCR models, asking for personal experiences rather than just reviews. They are looking for models that perform well across various tasks.
*   **Emotion:** Neutral, focused on gathering information and sharing practical experiences.
*   **Top 3 Points of View:**
    *   Recommendations for specific OCR models like DeepSeek OCR, Paddle OCR, and Gemma-4-26B-A4B, with mentions of their strengths for different document types (typed, handwritten, complex tables).
    *   Advice to benchmark models on specific tasks to determine the best fit.
    *   Mentions of specialized tools like Docling.ai and GLM-OCR, with notes on their features and limitations.

**[ LM Studio / Windows / Vulkan possible to prioritize GPU order? (Score: 4)](https://www.reddit.com/r/LocalLLaMA/comments/1t975bx/lm_studio_windows_vulkan_possible_to_prioritize/)**
*   **Summary:** This post inquires about prioritizing GPU order in LM Studio on Windows with Vulkan, leading to discussions on tensor splitting and memory pinning for performance optimization.
*   **Emotion:** Neutral, focused on technical troubleshooting and performance tuning.
*   **Top 3 Points of View:**
    *   Confirmation that GPU prioritization is possible through tensor splitting and parallelism settings.
    *   Personal anecdotes of performance gains after tuning these configurations.
    *   Discussion of specific flags and their impact on different hardware setups.

**[ Building out my tool library, any recommendations? I just added email capability and im starting to get hyped! (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1t97163/building_out_my_tool_library_any_recommendations/)**
*   **Summary:** Users are discussing how to build effective tool libraries for LLMs, sharing recommendations for models and strategies to improve tool selection and reduce errors, particularly with complex queries.
*   **Emotion:** Neutral, focused on practical advice and sharing of experiences.
*   **Top 3 Points of View:**
    *   Qwen 3.6 35B A3B is noted for handling tool selection well with small libraries but can exhibit "selection drift" with larger ones.
    *   Renaming tools for clearer semantic distance and providing "use this when..." descriptions in tool descriptions are suggested as improvements.
    *   Discussions around specific tools like web search (exa) and the challenges of iterative search with LLMs.

**[ How does llama-server pick which MoE experts go on the GPU and which stay on the CPU? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1t9fy74/how_does_llamaserver_pick_which_moe_experts_go_on/)**
*   **Summary:** This thread investigates how llama-server determines which experts in a Mixture-of-Experts (MoE) model are loaded onto the GPU versus the CPU.
*   **Emotion:** Neutral, focused on technical explanation and understanding of MoE architecture.
*   **Top 3 Points of View:**
    *   Explanation that llama.cpp primarily fits parameters based on ordering and uses optimizations to minimize CUDA graphs, with no current system for "commonly used" expert fitting due to GGUF's layer-wise tensor storage.
    *   Discussion on how most modern MoE implementations penalize "expert collapse" during training, forcing balanced expert usage across tokens.
    *   A user shares an experience where the number of experts offloaded to the CPU significantly impacted token generation speed, suggesting a performance benefit in freeing up GPU compute for attentions.
