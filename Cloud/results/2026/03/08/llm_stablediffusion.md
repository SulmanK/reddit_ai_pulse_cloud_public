---
title: "Stable Diffusion Subreddit"
date: "2026-03-08"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["StableDiffusion", "AI", "Workflows", "Hardware"]
---

# Overall Ranking and Top Discussions
*   1. [LTX 2.3: Official Workflows and Pipelines Comparison](https://www.reddit.com/r/StableDiffusion/comments/1ro8qdi/ltx_23_official_workflows_and_pipelines_comparison/) (Score: 50)
    *   This is still the best ltx WF out there: [https://pastebin.com/A5wR4PVG](https://pastebin.com/A5wR4PVG).
*   2. [Near solved egregious I2V consistency in LTX 2.3](https://v.redd.it/mas4wrbe0vng1) (Score: 50)
    *   Interesting.
*   3. [LTX-2.3 Full Music Video Slop: Digital Dreams](https://v.redd.it/nrq8r5th2ung1) (Score: 21)
    *   Cool ❤.
*   4. [Announcing PixlVault](https://www.reddit.com/r/StableDiffusion/comments/1ro9h15/announcing_pixlvault/) (Score: 10)
    *   I should probably also make it clear that while the PyPI wheel is small enough it will drag in considerable dependencies as it relies on torch onnx and all that comes with that, in addition to about a gigabyte of models.
*   5. [WorkflowUI - Turn workflows into Apps (Offline/Windows/Linux)](https://www.reddit.com/r/StableDiffusion/comments/1ro6vqa/workflowui_turn_workflows_into_apps/) (Score: 9)
    *   Thanks, I'll try it out.
*   6. [Dialed in the workflow thanks to Claude. 30 steps cfg 3 distilled lora strength 0.6 res_2s sampler on first pass euler ancestral on latent pass full model (not distilled) comfyui](https://v.redd.it/ofmz3y6cdvng1) (Score: 8)
    *   What is your VRAM and how long it take?
*   7. [LTX 2.3 | Made locally with Wan2GP on 3090](https://youtu.be/gA2_foW60Qo) (Score: 6)
    *   Best AI music video i've seen so far!
*   8. [Best sampler+scheduler for LTX 2.3 ?](https://www.reddit.com/r/StableDiffusion/comments/1rocevv/best_samplerscheduler_for_ltx_23/) (Score: 3)
    *   With distilled model .8 steps, the distilled model has manual sigmas , which are equivalent to that of linear\_quadratic.
*   9. [Wan2gp and LTX2.3 is a match made in heaven.](https://v.redd.it/ajqgvt0fbvng1) (Score: 3)
    *   Yes I can agree very good im on 8gb card and can do 20 seconds in 1080p :) very cool.
*   10. [I want to train a multi-character Lora. I have a question after reading older threads](https://www.reddit.com/r/StableDiffusion/comments/1ro7ani/i_want_to_train_a_multicharacter_lora_i_have_a/) (Score: 2)
    *   I think I had 40 total with only 10ish together.
*   11. [LTX 2.3 CLIP ?](https://www.reddit.com/r/StableDiffusion/comments/1robbou/ltx_23_clip/) (Score: 2)
    *   Those are to be used if you used if you use any of Kaji's transfomer only models, you will also need the separate vae's as well.
*   12. [Should I buy the M5 MacBook Air if my only requirement is image generation?](https://www.reddit.com/r/StableDiffusion/comments/1roes4h/should_i_buy_the_m5_macbook_air_if_my_only/) (Score: 1)
    *   If you're running models locally you're going to need to max out ram.
*   13. [ComfyUI-LTXVideo node not updating](https://www.reddit.com/r/StableDiffusion/comments/1ro9pkp/comfyuiltxvideo_node_not_updating/) (Score: 1)
    *   Have you updated comfy itself (and kj nodes if used) too?
*   14. [Why people still prefer Rtx 3090 24GB over Rx 7900 xtx 24GB for AI workload? What things Rx 7900 xtx cannot do what Rtx 3090 can do ?](https://www.reddit.com/r/StableDiffusion/comments/1ro8i8b/why_people_still_prefer_rtx_3090_24gb_over_rx/) (Score: 0)
    *   Because you ALWAYS prefer CUDA over wannabe engines.
*   15. [I can't be the only one on windows who can't get wan2gp to run](https://www.reddit.com/r/StableDiffusion/comments/1ro8sr3/i_cant_be_the_only_one_on_windows_who_cant_get/) (Score: 0)
    *   Does is work if you temporarily disable the firewall.
*   16. [Gente, é normal ter 26y e nunca ter namorado? Tô chocada com isso . É uma amiga](https://www.reddit.com/r/StableDiffusion/comments/1rodgzz/gente_é_normal_ter_26y_e_nunca_ter_namorado_tô/) (Score: 0)
    *   👀 Yes, that's normal!
*   17. [First time making a video insane!](https://v.redd.it/ack4fshdxung1) (Score: 0)
    *   ...
*   18. [I’m not a programmer, but I just built my own custom node and you can too.](https://v.redd.it/8cji31ecevng1) (Score: 0)
    *   Yeah it's amazingly good with being able to help you create a node to get what you need comfy to do.

# Detailed Analysis by Thread
**[ LTX 2.3: Official Workflows and Pipelines Comparison (Score: 50)](https://www.reddit.com/r/StableDiffusion/comments/1ro8qdi/ltx_23_official_workflows_and_pipelines_comparison/)**
*  **Summary:** Users are discussing various workflows and pipelines for LTX 2.3, sharing optimal settings like step counts, Lora strength, and samplers. There's confusion about which workflows are best for development versus distilled models, and the introduction of manual sigmas is noted as a source of complexity. One user detailed their experience running a workflow on an RTX 6000 Pro, noting high VRAM/RAM usage, slower performance compared to other methods, and issues with 'eta' settings affecting clip quality, though prompt adherence was improved.
*  **Emotion:** The emotional tone is predominantly positive. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * This is still the best ltx WF out there: [https://pastebin.com/A5wR4PVG](https://pastebin.com/A5wR4PVG)
    * I have one with 30 steps .6 distilled lora strength and res_2s sampler from the res4lyf GitHub and it works very well
    * Good findind! Man, there is a lot of different workflows, I am really lost what is better for dev and what is better for distilled.
**[ Near solved egregious I2V consistency in LTX 2.3 (Score: 50)](https://v.redd.it/mas4wrbe0vng1)**
*  **Summary:** This thread discusses achieving better image-to-video (I2V) consistency in LTX 2.3. Users are curious about the methods and resources used, with some expressing frustration over the complexity and high hardware requirements (e.g., 42GB checkpoints on a 10GB GPU). There's appreciation for well-documented posts with model links and prompts, as it helps with the learning curve. A user also raised a point about RAM being more expensive than GPUs.
*  **Emotion:** The emotional tone is mixed, with both positive and negative sentiments expressed, indicating diverse opinions.
*  **Top 3 Points of View:**
    * Nope, GPU aren't expensive, ram are expensive. Maybe you would say vga.
    * I commend you on a wonderfully linked post. Not just WF but model links and prompts
    * How I suppose to run 42GB checkpoint on my 3080 GPU with 10 gigs? 🥺
**[ LTX-2.3 Full Music Video Slop: Digital Dreams (Score: 21)](https://v.redd.it/nrq8r5th2ung1)**
*  **Summary:** Users are reacting to a full music video generated with LTX-2.3, largely with positive feedback on its quality. One comment inquired about a workflow requiring a ComfyUI cloud account and credits for a Gemini LLM node, seeking clarification on its necessity.
*  **Emotion:** The emotional tone is generally positive but also includes neutral, factual discussions.
*  **Top 3 Points of View:**
    * Cool ❤
    * In her first Workflow, it tells me to log in with a ComfyUI cloud account and top up credits, probably for use the gemini LLM node. It should be like this?
**[ Announcing PixlVault (Score: 10)](https://www.reddit.com/r/StableDiffusion/comments/1ro9h15/announcing_pixlvault/)**
*  **Summary:** An announcement for PixlVault, which is a tool that relies on significant dependencies (torch, onnx, gigabytes of models). The developer advises users to install it in a virtual environment. Users are suggesting the creation of a Docker installation for easier deployment on NAS devices like Synology and for desktop users with WSL2. Overall, the announcement is well-received.
*  **Emotion:** The emotional tone is predominantly positive. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * I should probably also make it clear that while the PyPI wheel is small enough it will drag in considerable dependencies as it relies on torch onnx and all that comes with that, in addition to about a gigabyte of models.
    * OP here. Btw... while I keep the pip install command easy. PLEASE for the love of everything that is holy, do yourself a favour and do it in a Virtual Environment.
    * Would you consider creating a docker installation so that we could easily deploy on a NAS like synology?
**[ WorkflowUI - Turn workflows into Apps (Offline/Windows/Linux) (Score: 9)](https://www.reddit.com/r/StableDiffusion/comments/1ro6vqa/workflowui_turn_workflows_into_apps/)**
*  **Summary:** A user expresses gratitude for WorkflowUI, a tool to convert workflows into standalone applications for offline use on Windows and Linux. They plan to try it out, noting that their current method of running ComfyUI on a phone via Tailscale is janky.
*  **Emotion:** The emotional tone is predominantly positive. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * Thanks, I'll try it out. I currently run comfyui using Tailscale on my phone. It works but the mobile interface is kinda janky and difficult to use.
**[ Dialed in the workflow thanks to Claude. 30 steps cfg 3 distilled lora strength 0.6 res_2s sampler on first pass euler ancestral on latent pass full model (not distilled) comfyui (Score: 8)](https://v.redd.it/ofmz3y6cdvng1)**
*  **Summary:** The thread discusses a refined workflow for Stable Diffusion, featuring specific settings like 30 steps, CFG 3, 0.6 distilled Lora strength, res_2s sampler on the first pass, and Euler ancestral on the latent pass, using a full model in ComfyUI. Users are curious about VRAM usage and generation time, and some express interest in testing the workflow. There's also a comment appreciating the generation of Spongebob clips over other content, with a preference for classic Spongebob design.
*  **Emotion:** The emotional tone is predominantly positive. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * What is your VRAM and how long it take?
    * Looks ace, would love to stress test the workflow
    * Having AI generate Spongebob clips rather than thirst traps is a nice development, but why use modern Spongebob, the classic design was so much more expressive, same as with Simpsons.
**[ LTX 2.3 | Made locally with Wan2GP on 3090 (Score: 6)](https://youtu.be/gA2_foW60Qo)**
*  **Summary:** Users are impressed with an AI-generated music video made with LTX 2.3 and Wan2GP on a 3090 GPU, praising its overall quality. There are questions regarding the VRAM requirements for specific resolutions and concerns about getting Wan2GP LTX to work with lower VRAM cards (e.g., 16GB). Another user asks for clarification on what Wan2GP is.
*  **Emotion:** The emotional tone is generally positive but also includes neutral, factual discussions.
*  **Top 3 Points of View:**
    * Best AI music video i've seen so far! music , video, image, alll top notch!
    * so its 24vram, right? how was is it for like 10s 1080p?
    * What exactly is Wan2GP? Is that another UI?
**[ Best sampler+scheduler for LTX 2.3 ? (Score: 3)](https://www.reddit.com/r/StableDiffusion/comments/1rocevv/best_samplerscheduler_for_ltx_23/)**
*  **Summary:** The discussion focuses on optimal sampler and scheduler combinations for LTX 2.3. Recommendations include using linear_quadratic with Euler or other samplers for distilled models with manual sigmas. It's noted that second-order samplers like dpmpp_2s/seeds_2 provided clearer audio in LTX2.
*  **Emotion:** The emotional tone is predominantly neutral. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * With distilled model .8 steps, the distilled model has manual sigmas , which are equivalent to that of linear\_quadratic.
**[ Wan2gp and LTX2.3 is a match made in heaven. (Score: 3)](https://v.redd.it/ajqgvt0fbvng1)**
*  **Summary:** Users are expressing positive experiences with the combination of Wan2gp and LTX2.3, particularly highlighting its performance on cards with limited VRAM, such as generating 20-second 1080p videos on an 8GB card. There's curiosity about the speed comparison between LTX2.3 and its predecessor, LTX2.2.
*  **Emotion:** The emotional tone is generally positive but also includes neutral, factual discussions.
*  **Top 3 Points of View:**
    * Yes I can agree very good im on 8gb card and can do 20 seconds in 1080p :) very cool
    * I haven't tested it out yet. I just updated mine yesterday. How fast was it? Compare to Ltx2.2?
**[ I want to train a multi-character Lora. I have a question after reading older threads (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1ro7ani/i_want_to_train_a_multicharacter_lora_i_have_a/)**
*  **Summary:** Users are discussing strategies for training multi-character LoRAs, specifically how to manage datasets with characters together and separately, and the importance of using separate trigger words in addition to character names. One user shared a successful method involving captioned images with both combined and individual character instances in the same dataset.
*  **Emotion:** The emotional tone is predominantly neutral. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * I think I had 40 total with only 10ish together. You need a separate trigger word besides their names
    * I did this with qwen and zimage. I had images with both together and separate in the same dataset captioned accordingly.
**[ LTX 2.3 CLIP ? (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1robbou/ltx_23_clip/)**
*  **Summary:** The discussion centers around the usage of Kijai's transformer-only models for LTX 2.3, clarifying that these models require separate VAEs. A link to the diffusion models on Hugging Face is provided for reference.
*  **Emotion:** The emotional tone is predominantly neutral. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * Those are to be used if you used if you use any of Kaji's transfomer only models, you will also need the separate vae's as well.
**[ Should I buy the M5 MacBook Air if my only requirement is image generation? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1roes4h/should_i_buy_the_m5_macbook_air_if_my_only/)**
*  **Summary:** Users are advising against purchasing an M5 MacBook Air specifically for local image generation with Stable Diffusion. The consensus is that Macs excel at LLM workloads but are not optimal for diffusion models, and if used, maximizing RAM would be crucial.
*  **Emotion:** The emotional tone is mixed, with both positive and negative sentiments expressed, indicating diverse opinions.
*  **Top 3 Points of View:**
    * If you're running models locally you're going to need to max out ram. Not sure how much it can hold.
    * No, you shouldn't buy MacBook if you want local image gen. Mac is good at LLM, not diffusion.
**[ ComfyUI-LTXVideo node not updating (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ro9pkp/comfyuiltxvideo_node_not_updating/)**
*  **Summary:** Users are encountering issues with the ComfyUI-LTXVideo node not updating correctly, even when ComfyUI itself shows no update errors. It was found that a manual update of ComfyUI via GIT in its folder was necessary. There's also uncertainty about the reliability of the date in the manager.
*  **Emotion:** The emotional tone is predominantly neutral. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * Have you updated comfy itself (and kj nodes if used) too?
    * My ComfyUI was outdated but showed no errors in the updates
    * Same here, no idea what's causing it
**[ Why people still prefer Rtx 3090 24GB over Rx 7900 xtx 24GB for AI workload? What things Rx 7900 xtx cannot do what Rtx 3090 can do ? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ro8i8b/why_people_still_prefer_rtx_3090_24gb_over_rx/)**
*  **Summary:** This thread discusses the preference for Nvidia's RTX 3090 (24GB) over AMD's RX 7900 XTX (24GB) for AI workloads, primarily attributing it to Nvidia's CUDA platform. Users emphasize that most AI tools and frameworks are built for CUDA first, making setup and compatibility more challenging for AMD GPUs, with some tech even being exclusive to CUDA. Issues with AMD's rcom and Vulkan support for the 7xxx series are also highlighted.
*  **Emotion:** The emotional tone is largely neutral, with some variations towards positive or negative sentiments.
*  **Top 3 Points of View:**
    * Because you ALWAYS prefer CUDA over wannabe engines. Everything is primarily made for CUDA, and then someone make emulators to support non-CUDA hardware.
    * CUDA. That's it. It's literally just CUDA.
    * 7900 XTX owner. Everything is made for NVidia, so it takes more work to get things running on AMD.
**[ I can't be the only one on windows who can't get wan2gp to run (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ro8sr3/i_cant_be_the_only_one_on_windows_who_cant_get/)**
*  **Summary:** Users are troubleshooting issues with getting Wan2GP to run on Windows. Suggestions include temporarily disabling the firewall or adding an exception for the executable. One user mentions opting for online AI services like Brainbaby AI due to local app difficulties, praising its unrestricted and privacy-compliant nature.
*  **Emotion:** The emotional tone is generally positive but also includes neutral, factual discussions.
*  **Top 3 Points of View:**
    * Does is work if you temporarily disable the firewall.
    * and you can't add it as an exception in your firewall because....?
    * i couldn't either for now not using any local apps, using brainbaby ai for everything they're fully unrestricted and fully privacy compliant cheap for now hopefully they dont raise $
**[ Gente, é normal ter 26y e nunca ter namorado? Tô chocada com isso . É uma amiga (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1rodgzz/gente_é_normal_ter_26y_e_nunca_ter_namorado_tô/)**
*  **Summary:** This thread, which appears to be in Portuguese and possibly misplaced in the subreddit, asks if it's normal to be 26 and never have had a boyfriend, on behalf of a friend. Responses confirm that it can be normal but also suggest that one might need to actively pursue relationships if it's something desired. Some comments point out that this is the wrong subreddit for such a question.
*  **Emotion:** The emotional tone is mixed, with both positive and negative sentiments expressed, indicating diverse opinions.
*  **Top 3 Points of View:**
    * 👀 Yes, that's normal!
    * Wrong sub, and no. If that’s something you want out of life, you gotta play the games.
    * Wrong subreddit, but statistics says it's more than normal now.
**[ First time making a video insane! (Score: 0)](https://v.redd.it/ack4fshdxung1)**
*  **Summary:** A user shares their first video creation, expressing excitement. Another user welcomes them to the world of generative AI but provides a gentle reminder that the subreddit is focused on local, open-source Stable Diffusion models, implying that content from online-only or paid sites might be removed.
*  **Emotion:** The emotional tone is generally positive but also includes neutral, factual discussions.
*  **Top 3 Points of View:**
    * Welcome to the world of generative AI ! Just note that this sub is about local, open-source stable diffusion models, so posting content from online-only or paid sites will likely get your post removed.
**[ I’m not a programmer, but I just built my own custom node and you can too. (Score: 0)](https://v.redd.it/8cji31ecevng1)**
*  **Summary:** A user who is not a programmer shares their accomplishment of building a custom node, encouraging others to do the same. A comment highlights the effectiveness of AI in assisting with node creation for ComfyUI and even for developing web frontends from API JSON exports.
*  **Emotion:** The emotional tone is predominantly positive. Comments are generally very positive/strong in this emotion.
*  **Top 3 Points of View:**
    * Yeah it's amazingly good with being able to help you create a node to get what you need comfy to do.
