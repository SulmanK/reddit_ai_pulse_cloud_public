---
title: "LocalLLaMA Subreddit"
date: "2025-12-05"
description: "Analysis of top discussions and trends in the localllama subreddit"
tags: ["LLM", "AI", "Local Models"]
---

# Overall Ranking and Top Discussions
1.  [You will own nothing and you will be happy!](https://www.reddit.com/r/LocalLLaMA/comments/1pf0q99/you_will_own_nothing_and_you_will_be_happy/) (Score: 263)
    *   This thread discusses the idea of centralized computing and the potential downsides of relying on the "cloud," including security risks and market manipulation, particularly in the context of RAM pricing.
2.  [Why do LLM response formats often use <| |> (as in <|message|>) instead of <message>, and why do they use <|end|> instead of </message>?](https://i.redd.it/5e5ir2zlte5g1.png) (Score: 61)
    *   This thread explores the reasons behind the use of specific token formats in LLM responses, focusing on how these formats avoid conflicts with training data, ensure single-token representations, and maintain compatibility with the autoregressive nature of models.
3.  [Blood and stardust! Watch 9 local LLMs debate Star Wars vs Star Trek](https://v.redd.it/t6y4gtw0se5g1) (Score: 37)
    *   This thread showcases a project where 9 local LLMs debate Star Wars vs. Star Trek, generating positive feedback and requests for further development and integration with package managers.
4.  [Are models creators choosing to not do QAT?](https://www.reddit.com/r/LocalLLaMA/comments/1pf4nuf/are_models_creators_choosing_to_not_do_qat/) (Score: 9)
    *   This thread discusses the use of Quantization-Aware Training (QAT) and its trade-offs with Post-Training Quantization (PTQ), the increasing expense of QAT for large models, and the hardware support needed for FP4 and FP8.
5.  [been experimenting with parallel agent execution locally. way harder than i thought](https://www.reddit.com/r/LocalLLaMA/comments/1pf0qbz/been_experimenting_with_parallel_agent_execution/) (Score: 4)
    *   The thread discusses challenges in parallel agent execution, with suggestions including event-driven coordination, message queues, and the use of orchestrator agents.
6.  [Llama 405B is worse than Gemma 3 12B?](https://www.reddit.com/r/LocalLLaMA/comments/1pf3ai8/llama_405b_is_worse_than_gemma_3_12b/) (Score: 4)
    *   This thread discusses a comparison between Llama 405B and Gemma 3 12B, with users discussing their performance, training standards, and limitations.
7.  [For those of you with ai max+ 395 mini pc that have experience or no bias hate with mac computers: Would you recommend a max 395+ to someone where it currently or are you thinking of switching to or back to mac?](https://www.reddit.com/r/LocalLLaMA/comments/1pf6jcj/for_those_of_you_with_ai_max_395_mini_pc_that/) (Score: 2)
    *   Users discuss the AI Max+ 395 mini PC and whether it's good at running 70B LLMs and whether it is worth the investment.
8.  [Whats the best local llm to fully use 128 GB of unified memory in a DGX Spark or AMD Max+ 395?](https://www.reddit.com/r/LocalLLaMA/comments/1pf0gmo/whats_the_best_local_llm_to_fully_use_128_gb_of/) (Score: 2)
    *   This thread asks for suggestions on the best local LLM to utilize 128 GB of unified memory, with users recommending models like qwen3-next80B, GPT OSS 120B, and Minimax-M2 UD-IQ3\_XSS, and discussing inference optimization techniques.
9.  [Best qwen3 next finetune?](https://www.reddit.com/r/LocalLLaMA/comments/1pf1ej4/best_qwen3_next_finetune/) (Score: 2)
    *   The thread asks about the best qwen3 next finetune. Some users have had no luck with finetuning Qwen 3 MoE models.
10. [I Guess I discovered AGI](https://www.reddit.com/r/LocalLLaMA/comments/1pezzar/i_guess_i_discovered_agi/) (Score: 0)
    * The thread is a Meme Friday post about AGI.
11. [What to do with an unused server?](https://www.reddit.com/r/LocalLLaMA/comments/1pf3a3w/what_to_do_with_an_unused_server/) (Score: 0)
    * This thread discusses ways to utilize an unused server for AI-related tasks, such as testing LLM workflows and automating documentation writing.
12. [Poll : when is the ai bubble going to burst?](https://www.reddit.com/r/LocalLLaMA/comments/1pf2p81/poll_when_is_the_ai_bubble_going_to_burst/) (Score: 0)
    * The thread discusses when the AI bubble is going to burst. Some users think it will be in a few years and some users think that it will never burst.
13. [Deepseek must be losing money from output token generation  and training or are getting subsidized/free gpus](https://www.reddit.com/r/LocalLLaMA/comments/1pf4l6w/deepseek_must_be_losing_money_from_output_token/) (Score: 0)
    * This thread discusses whether Deepseek is losing money from output token generation. Some users believe the Chinese government could be subsidizing it.
14. [The matrix is glitching](https://i.redd.it/uqd05mkj0f5g1.png) (Score: 0)
    * This thread has a screenshot of a screenshot of a screenshot.
15. [A lightweight way to track agent drift / repair / reentry in real workloads](https://www.reddit.com/r/LocalLLaMA/comments/1pf2lz3/a_lightweight_way_to_track_agent_drift_repair/) (Score: 0)
    * This thread discusses a way to track agent drift / repair / reentry in real workloads.
16. [how are you supposed to pronounce the name Qwen?](https://www.reddit.com/r/LocalLLaMA/comments/1pf4w4e/how_are_you_supposed_to_pronounce_the_name_qwen/) (Score: 0)
    * This thread discusses how the name Qwen is supposed to be pronounced.

# Detailed Analysis by Thread
**[You will own nothing and you will be happy! (Score: 263)](https://www.reddit.com/r/LocalLLaMA/comments/1pf0q99/you_will_own_nothing_and_you_will_be_happy/)**
*  **Summary:** The thread discusses the trend of moving computing to the cloud, the potential for nation-state hacks, and the impact on consumer access to private computing. Concerns are raised about RAM shortages, market manipulation, and the shift to subscription-based services. Some users see a conspiracy, while others believe it's just capitalism at work.
*  **Emotion:** The overall emotional tone is neutral, with a mix of concern, skepticism, and resignation.
*  **Top 3 Points of View:**
    *   Concerns about security risks in cloud computing and potential hacks by nation-states.
    *   Belief that the market is being starved of private computing in favor of cloud services.
    *   The idea that RAM shortages and pricing are being artificially manipulated for profit.

**[Why do LLM response formats often use <| |> (as in <|message|>) instead of <message>, and why do they use <|end|> instead of </message>? (Score: 61)](https://i.redd.it/5e5ir2zlte5g1.png)**
*  **Summary:** The thread explores the rationale behind using the `<| |>` format for special tokens in LLMs. The format is intended to avoid conflicts with common text, ensure single-token representations, and work well with the autoregressive nature of these models. XML incompatibility and the importance of tokenization are also discussed.
*  **Emotion:** The overall emotional tone is neutral and informative, with users providing technical explanations.
*  **Top 3 Points of View:**
    *   The `<| |>` format helps avoid conflicts with common text found in the training corpus.
    *   These tokens are designed to be single-token representations, which simplifies processing.
    *   The format is optimized for the autoregressive nature of LLMs, supporting features like tool calling and multi-message turns.

**[Blood and stardust! Watch 9 local LLMs debate Star Wars vs Star Trek (Score: 37)](https://v.redd.it/t6y4gtw0se5g1)**
*  **Summary:** This thread is about a project where 9 local LLMs debate Star Wars vs Star Trek. Users find it awesome and want to see more of the tool and add to the winget repo.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Users found the project awesome.
    *   AI is a superior form of intelligence.
    *   Request to add it to the winget repo.

**[Are models creators choosing to not do QAT? (Score: 9)](https://www.reddit.com/r/LocalLLaMA/comments/1pf4nuf/are_models_creators_choosing_to_not_do_qat/)**
*  **Summary:** The thread explores the reasons why model creators might choose not to use Quantization-Aware Training (QAT). Discussions cover the cost and complexity of QAT, the availability of post-training quantization (PTQ), the trade-offs between different bit widths (FP4, FP8, FP16), and the influence of benchmarks on the preference for higher precision.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   QAT is increasingly expensive and complex for large models, making PTQ more attractive.
    *   Training in higher bit widths (like FP8) offers more flexibility because PTQ can be applied afterward.
    *   If a model publishes a 4-bit quantization but it doesn't perform accurately as the FP16, someone can say your claims are inflated

**[been experimenting with parallel agent execution locally. way harder than i thought (Score: 4)](https://www.reddit.com/r/LocalLLaMA/comments/1pf0qbz/been_experimenting_with_parallel_agent_execution/)**
*  **Summary:** This thread discusses the challenges of parallel agent execution. Users suggest using event-driven coordination with a message queue. Using a fourth agent as the planning/calling agent. And using one instance of something that supports continuous batching.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Having separate agents work on different tasks can affect each other, leading to the suggestion of an event-driven coordination with a message queue.
    *   Having a fourth agent tasked with coming up with the overall design/interactions between the subagents work \*BEFORE\* the sub-agents have to make the decision.
    *   Use one instance of something that supports continuous batching such as vllm.

**[Llama 405B is worse than Gemma 3 12B? (Score: 4)](https://www.reddit.com/r/LocalLLaMA/comments/1pf3ai8/llama_405b_is_worse_than_gemma_3_12b/)**
*  **Summary:** This thread discusses whether Llama 405B is worse than Gemma 3 12B, with users discussing their performance, training standards, and limitations.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Llama3-405B is undertrained by current model standards, with only about 30 tokens/parameter.
    *   Gemma3 was released almost year later. L3.1 is quite ancient by today standards.
    *   12b wouldnt beat 405b in worldly knowledge/trivia, but 12b follows prompt instructions way better.

**[For those of you with ai max+ 395 mini pc that have experience or no bias hate with mac computers: Would you recommend a max 395+ to someone where it currently or are you thinking of switching to or back to mac? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1pf6jcj/for_those_of_you_with_ai_max_395_mini_pc_that/)**
*  **Summary:** This thread discusses the AI Max+ 395 mini PC and whether it's good at running 70B LLMs and whether it is worth the investment.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   If your goal is to run 70B LLMs then it’s great for that.
    *   If you want a machine that’s good at image gen and gaming, look elsewhere.

**[Whats the best local llm to fully use 128 GB of unified memory in a DGX Spark or AMD Max+ 395? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1pf0gmo/whats_the_best_local_llm_to_fully_use_128_gb_of/)**
*  **Summary:** This thread asks for suggestions on the best local LLM to utilize 128 GB of unified memory, with users recommending models like qwen3-next80B, GPT OSS 120B, and Minimax-M2 UD-IQ3\_XSS, and discussing inference optimization techniques.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   Try the qwen3-next80B, it's very good.
    *   GPT OSS 120B
    *   Try Minimax-M2 UD-IQ3\_XSS. It's very good and allows interleaved reasoning.

**[Best qwen3 next finetune? (Score: 2)](https://www.reddit.com/r/LocalLLaMA/comments/1pf1ej4/best_qwen3_next_finetune/)**
*  **Summary:** The thread asks about the best qwen3 next finetune. Some users have had no luck with finetuning Qwen 3 MoE models.
*  **Emotion:** The overall emotional tone is negative.
*  **Top 3 Points of View:**
    *   You must try to convience u/TheLocalDrummer
    *   I’ve not had much luck with fine tuning Qwen 3 MoE models. The dense models are much better / smarter for engineering.

**[I Guess I discovered AGI (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pezzar/i_guess_i_discovered_agi/)**
*  **Summary:** The thread is a Meme Friday post about AGI.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   now scale it to 600B parameters and make it run on my potato
    *   Oh It's meme Friday, right. 🤣
    *   Get this guy $1B funding stat

**[What to do with an unused server? (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pf3a3w/what_to_do_with_an_unused_server/)**
*  **Summary:** This thread discusses ways to utilize an unused server for AI-related tasks, such as testing LLM workflows and automating documentation writing.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   use a local llm to automate issue closing.
    *   AI ***?  Shovel all your company policies into it and have it rewrite them and clean them all up.
    *   Turn the box into a small internal platform rather than a playground: expose a couple of repeatable, low friction utilities people actually need.

**[Poll : when is the ai bubble going to burst? (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pf2p81/poll_when_is_the_ai_bubble_going_to_burst/)**
*  **Summary:** The thread discusses when the AI bubble is going to burst. Some users think it will be in a few years and some users think that it will never burst.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   There will be another AI Winter in 2027. The open source community should take advantage of the good things happening now to prepare for the Winter.
    *   4-5 years. They will milk the public with small controlled hypes and crashes before the big final theft.
    *   AI is just an excuse for centralizing compute resources and making consumer computing unaffordable.

**[Deepseek must be losing money from output token generation  and training or are getting subsidized/free gpus (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pf4l6w/deepseek_must_be_losing_money_from_output_token/)**
*  **Summary:** This thread discusses whether Deepseek is losing money from output token generation. Some users believe the Chinese government could be subsidizing it.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   8x910c running Deepseek R1 or V3.1 should process 2000 tokens per second.
    *   The government wants to dominate all emerging markets. China massively subsidizes all emerging markets and only needs 1-3 winning companies to emerge that can compete globally. They are doing the same with robotics.
    *   They probably have created a distributed network that can perform arbitrary remote operations and send the result back bundled into their state-run apps.

**[The matrix is glitching (Score: 0)](https://i.redd.it/uqd05mkj0f5g1.png)**
*  **Summary:** This thread has a screenshot of a screenshot of a screenshot.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Is this a screenshot of a screenshot of a screenshot, seriously?

**[A lightweight way to track agent drift / repair / reentry in real workloads (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pf2lz3/a_lightweight_way_to_track_agent_drift_repair/)**
*  **Summary:** This thread discusses a way to track agent drift / repair / reentry in real workloads.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    *   If anyone here wants to see more concrete examples or edge cases, I can add a few.

**[how are you supposed to pronounce the name Qwen? (Score: 0)](https://www.reddit.com/r/LocalLLaMA/comments/1pf4w4e/how_are_you_supposed_to_pronounce_the_name_qwen/)**
*  **Summary:** This thread discusses how the name Qwen is supposed to be pronounced.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *   Most people say Kwen. I think it's a pretty sensible pronunciation.
    *   In English we call it the Universal Meaning Thousand Questions.
    *    Don't go down that rabbit hole and just read it in english. it's a westernized name.
