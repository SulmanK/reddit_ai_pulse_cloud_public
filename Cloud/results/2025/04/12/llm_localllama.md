---
title: "LocalLLaMA Subreddit"
date: "2025-04-12"
description: "Analysis of top discussions and trends in the localllama subreddit"
tags: ["LLM", "Local AI", "Models"]
---

# Overall Ranking and Top Discussions
1.  [[D] What if you could run 50+ LLMs per GPU — without keeping them in memory?](https://www.reddit.com/r/LocalLLaMA/comments/1jxn8x7/what_if_you_could_run_50_llms_per_gpu_without/) (Score: 52)
    * The thread discusses the possibility of running 50+ LLMs per GPU without keeping them in memory.
2.  [[PSA] Google have fixed the QAT 27 model](https://www.reddit.com/r/LocalLLaMA/comments/1jxlqil/psa_google_have_fixed_the_qat_27_model/) (Score: 44)
    * The thread discusses Google's fix for the QAT 27 model.
3.  [llama.cpp got 2 fixes for Llama 4 (RoPE & wrong norms)](https://www.reddit.com/r/LocalLLaMA/comments/1jxo7lb/llamacpp_got_2_fixes_for_llama_4_rope_wrong_norms/) (Score: 29)
    * The thread discusses two fixes for Llama 4 within llama.cpp related to RoPE and incorrect norms.
4.  [Intel A.I. ask me anything (AMA)](https://www.reddit.com/r/LocalLLaMA/comments/1jxohy4/intel_ai_ask_me_anything_ama/) (Score: 16)
    * The thread discusses an Intel A.I. AMA, with users asking questions and commenting on Intel's approach.
5.  [Anyone else find benchmarks don't match their real-world needs?](https://www.reddit.com/r/LocalLLaMA/comments/1jxk8rx/anyone_else_find_benchmarks_dont_match_their/) (Score: 14)
    * The thread discusses the relevance and reliability of benchmarks for LLMs in real-world applications, especially in programming language tasks like Rust.
6.  [How to mke a local llm to adpat a personality?](https://www.reddit.com/r/LocalLLaMA/comments/1jxkd7j/how_to_mke_a_local_llm_to_adpat_a_personality/) (Score: 4)
    * The thread discusses how to give a local LLM a personality by using detailed system prompts.
7.  [What's the current best instruction following/structured output open source model available?](https://www.reddit.com/r/LocalLLaMA/comments/1jxkpzk/whats_the_current_best_instruction/) (Score: 2)
    * The thread discusses the best open-source models available for instruction following and structured output.
8.  [64 vs 128 MBP?](https://www.reddit.com/r/LocalLLaMA/comments/1jxnh0m/64_vs_128_mbp/) (Score: 2)
    * The thread discusses whether 64GB or 128GB of memory is better for running local LLMs.
9.  [Building a chat for my company, llama-3.3-70b or DeepSeek-R1?](https://www.reddit.com/r/LocalLLaMA/comments/1jxnrl5/building_a_chat_for_my_company_llama3370b_or/) (Score: 2)
    * The thread discusses the best model to use for a company chat application.
10. [Should I get a GPU to speed up my Perplexica+Ollama-based deal-checker script?](https://www.reddit.com/r/LocalLLaMA/comments/1jxkx3i/should_i_get_a_gpu_to_speed_up_my/) (Score: 1)
    * The thread discusses whether getting a GPU will speed up a Perplexica+Ollama-based deal-checker script.
11. [Building a llama.cpp playground – need motherboard advice for multi-GPU setup](https://www.reddit.com/r/LocalLLaMA/comments/1jxmusq/building_a_llamacpp_playground_need_motherboard/) (Score: 1)
    * The thread discusses motherboard advice for a multi-GPU setup for a llama.cpp playground.
12. [I want to build virtual try on for jwellery and accesories can anyone guide me?](https://www.reddit.com/r/LocalLLaMA/comments/1jxn1su/i_want_to_build_virtual_try_on_for_jwellery_and/) (Score: 1)
    * The thread is a request for guidance on building a virtual try-on application for jewelry and accessories.
13. [mysterious website 'ai.com' that used to refer to ChatGPT, Grok & DeepSeek, now shows "SOMETHING IS COMING" ♾️](https://www.reddit.com/gallery/1jxlgof) (Score: 0)
    * The thread discusses the mysterious changes to the ai.com website.
14. [The new Optimus alpha and quasar models behave very similarly to OpenAI models an even claim to be based on GPT-4!](https://www.reddit.com/r/LocalLLaMA/comments/1jxl22q/the_new_optimus_alpha_and_quasar_models_behave/) (Score: 0)
    * The thread discusses the behavior of new Optimus alpha and quasar models.

# Detailed Analysis by Thread
**[[D] What if you could run 50+ LLMs per GPU — without keeping them in memory? (Score: 52)](https://www.reddit.com/r/LocalLLaMA/comments/1jxn8x7/what_if_you_could_run_50_llms_per_gpu_without/)**
*  **Summary:** The thread discusses the possibility of running multiple LLMs on a single GPU by loading and unloading them from storage, raising questions about speed, implementation details, and comparisons to existing solutions like Ollama.
*  **Emotion:** Predominantly neutral, with some positive sentiment expressing interest in the project.
*  **Top 3 Points of View:**
    *   The core idea involves loading and unloading models from storage to allow more models to run on a single GPU.
    *   Questions are raised about the speed of loading models, especially large ones (65B), and comparisons are made to existing solutions that perform similar functions.
    *   Concerns are raised about GPU Cuda contention and whether the approach allows parallel processing of multiple requests.

**[[PSA] Google have fixed the QAT 27 model (Score: 44)](https://www.reddit.com/r/LocalLLaMA/comments/1jxlqil/psa_google_have_fixed_the_qat_27_model/)**
*  **Summary:** The thread announces that Google has fixed the QAT 27 model, with users confirming the fix and discussing the strange release process of Google models.
*  **Emotion:** The overall emotion is neutral, with some expressing mild negativity regarding Google's release process.
*  **Top 3 Points of View:**
    *   Google has fixed the issue of the QAT 27 model outputting `<end_of_turn>` prematurely.
    *   The fixes implemented by Google are similar to those already made by other contributors in the community.
    *   Users express confusion about Google's quality control and release procedures.

**[llama.cpp got 2 fixes for Llama 4 (RoPE & wrong norms) (Score: 29)](https://www.reddit.com/r/LocalLLaMA/comments/1jxo7lb/llamacpp_got_2_fixes_for_llama_4_rope_wrong_norms/)**
*  **Summary:** This thread announces and discusses two fixes implemented in llama.cpp for Llama 4 models, addressing RoPE issues and incorrect norms.
*  **Emotion:** The overall sentiment is neutral, focusing on the technical aspects and impact of the fixes. Some positivity is present anticipating new benchmark results.
*  **Top 3 Points of View:**
    *   The fixes aim to improve output quality for Llama 4 models.
    *   The fixes require re-quantization of the models to be effective.
    *   One fix is a temporary workaround (commenting out an assert) primarily preventing crashes during GGUF conversion.

**[Intel A.I. ask me anything (AMA) (Score: 16)](https://www.reddit.com/r/LocalLLaMA/comments/1jxohy4/intel_ai_ask_me_anything_ama/)**
*  **Summary:** This thread is about an Intel A.I. AMA (Ask Me Anything) session. However, users express disappointment and criticism because no questions have been answered.
*  **Emotion:** Predominantly neutral, with hints of negativity and disappointment due to the lack of responses from Intel.
*  **Top 3 Points of View:**
    *   Users are disappointed and critical of Intel for not answering any questions in the AMA.
    *   Some users suggest Intel is trying to crowdsource ideas under the guise of an AMA.
    *   There's a discussion about Intel's memory bandwidth limitations and the need for improvement to stay relevant.

**[Anyone else find benchmarks don't match their real-world needs? (Score: 14)](https://www.reddit.com/r/LocalLLaMA/comments/1jxk8rx/anyone_else_find_benchmarks_dont_match_their/)**
*  **Summary:** The thread is focused on the idea that benchmarks often fail to accurately reflect real-world performance and user experience with LLMs, particularly in specific domains such as programming.
*  **Emotion:** Mixed, with positive sentiment toward sharing results and discussion, but overall neutral as the conversation centres around objective observations.
*  **Top 3 Points of View:**
    *   Benchmarks can be misleading because real-world use cases vary significantly.
    *   Users should conduct their own tests with real-world data to accurately assess model performance for their specific needs.
    *   Some users find that specific benchmarks, like the polyglot test, correlate well with performance in certain areas, such as Rust programming.

**[How to mke a local llm to adpat a personality? (Score: 4)](https://www.reddit.com/r/LocalLLaMA/comments/1jxkd7j/how_to_mke_a_local_llm_to_adpat_a_personality/)**
*  **Summary:** This thread discusses how to make a local LLM adopt a specific personality using system prompts.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   Setting a detailed system prompt is key to giving an LLM a personality.
    *   Referencing resources like the "awesome-ai-system-prompts" GitHub repository can be helpful.
    *   Including specific personality traits in the system prompt, such as referencing Marvin the paranoid robot, can add flavor.

**[What's the current best instruction following/structured output open source model available? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1jxkpzk/whats_the_current_best_instruction/)**
*  **Summary:** A user is asking for recommendations on the best open-source model for instruction following and structured output.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   Check the instruction following leaderboard on llm.extractum.io for options.

**[64 vs 128 MBP? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1jxnh0m/64_vs_128_mbp/)**
*  **Summary:** The thread discusses the pros and cons of 64GB versus 128GB of memory for running LLMs on a Macbook Pro.
*  **Emotion:** Mixed, with some positive and negative sentiments, but overall mostly neutral.
*  **Top 3 Points of View:**
    *   64GB is sufficient for running models like Gemma 27B or Qwen 32B at 8Bit, or LLAMA 70B at 6Bit.
    *   You will always want more RAM.
    *   128GB allows you to run higher quality 70B models with more context.

**[Building a chat for my company, llama-3.3-70b or DeepSeek-R1? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1jxnrl5/building_a_chat_for_my_company_llama3370b_or/)**
*  **Summary:** The thread discusses the best model options for building a chat application for a company, comparing llama-3.3-70b and DeepSeek-R1.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   DeepSeek models are generally preferred over Llama 3.3 70B for coding tasks due to their superior quality. DeepSeek V3.1 is preferred over R1 due to faster performance.
    *   Alternative models like Gemma 27B, Qwen 2.5 72B, and Llama 4 maverick should be considered, especially for speed.
    *   Legal implications of using these models for business need to be reviewed.

**[Should I get a GPU to speed up my Perplexica+Ollama-based deal-checker script? (Score: 1)](https://www.reddit.com/r/LocalLLaMA/comments/1jxkx3i/should_i_get_a_gpu_to_speed_up_my/)**
*  **Summary:** The thread is a question about whether to get a GPU to speed up a Perplexica+Ollama-based deal-checker script.
*  **Emotion:** Positive
*  **Top 3 Points of View:**
    *   Getting a GPU would significantly speed up the script (40x faster).
    *   A 3060 12GB from Facebook Marketplace is recommended.
    *   Users are interested in seeing the script and setup.

**[Building a llama.cpp playground – need motherboard advice for multi-GPU setup (Score: 1)](https://www.reddit.com/r/LocalLLaMA/comments/1jxmusq/building_a_llamacpp_playground_need_motherboard/)**
*  **Summary:** The thread is seeking advice on motherboards for a multi-GPU setup to run llama.cpp.
*  **Emotion:** Mostly neutral with some negative comments about llama.cpp not utilizing GPUs effectively.
*  **Top 3 Points of View:**
    *   llama.cpp doesn't fully utilize multiple GPUs simultaneously, primarily using their VRAM.
    *   vllm with tensor parallelism is suggested as a better alternative for multi-GPU setups.
    *   ETH79-X5 is suggested as a cheap option for a motherboard.

**[I want to build virtual try on for jwellery and accesories can anyone guide me? (Score: 1)](https://www.reddit.com/r/LocalLLaMA/comments/1jxn1su/i_want_to_build_virtual_try_on_for_jwellery_and/)**
*  **Summary:** The thread involves a user seeking guidance on building a virtual try-on application for jewelry and accessories.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    *   A link to a relevant GitHub repository is shared: https://github.com/uddin007/Virtual-try-on-evaluation

**[mysterious website 'ai.com' that used to refer to ChatGPT, Grok & DeepSeek, now shows "SOMETHING IS COMING" ♾️ (Score: 0)](https://www.reddit.com/gallery/1jxlgof)**
*  **Summary:** The thread discusses the change on the ai.com website, which now displays "SOMETHING IS COMING" instead of references to ChatGPT, Grok & DeepSeek.
*  **Emotion:** Neutral.
*  **Top 3 Points of View:**
    *   The domain was updated recently and might have changed ownership.
    *   The change is likely an advertisement for crypto or something else.
    *   It is registered to Godaddy and was originally created in 1993.

**[The new Optimus alpha and quasar models behave very similarly to OpenAI models an even claim to be based on GPT-4! (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1jxl22q/the_new_optimus_alpha_and_quasar_models_behave/)**
*  **Summary:** The thread discusses the behavior of the new Optimus alpha and quasar models, noting their similarity to OpenAI models and their claim to be based on GPT-4.
*  **Emotion:** Neutral to Negative
*  **Top 3 Points of View:**
    *  Models can't be trusted to accurately self-report their origins or architecture.
    *  The models' coding abilities are poor, suggesting a possible OpenAI origin.
    *  Unless the models are open weight, there is little interest in them.
