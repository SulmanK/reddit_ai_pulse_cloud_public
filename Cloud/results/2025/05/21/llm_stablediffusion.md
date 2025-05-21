---
title: "Stable Diffusion Subreddit"
date: "2025-05-21"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["stablediffusion", "AI", "opensource"]
---

# Overall Ranking and Top Discussions
1.  [One of the banes of this scene is when something new comes out](https://www.reddit.com/r/StableDiffusion/comments/1ks1iot/one_of_the_banes_of_this_scene_is_when_something/) (Score: 40)
    * Discusses the frustrations of open-source developers regarding access to high-end hardware and the rapid pace of AI advancements.
2.  [Badge Bunny Episode 0](https://v.redd.it/deu5h531862f1) (Score: 18)
    * Reactions to a new episode, with some noting its closed-source nature.
3.  [I made gradio interface for Bagel if you don't want to use don't want to run it through jupyter](https://github.com/ansmom/BagelGradio/tree/gradio-feat) (Score: 11)
    *  A user shares a Gradio interface for Bagel, but notes its high VRAM requirements and slowness.
4.  [How can I unblurr a picture I tried upscaling with supir it doesn't unblur it](https://i.redd.it/2m9ftqkdm62f1.png) (Score: 10)
    * Users are seeking methods to unblur images after upscaling, with suggestions including img2img and specific models.
5.  [How are these AI Influencers made?](https://www.reddit.com/r/StableDiffusion/comments/1ks2yiw/how_are_these_ai_influencers_made/) (Score: 5)
    * Discussion on the techniques and tools used to create AI influencers.
6.  [Most basic knowledge FAQ?](https://www.reddit.com/r/StableDiffusion/comments/1ks4xw3/most_basic_knowledge_faq/) (Score: 3)
    * Discusses the difficulty of creating a basic knowledge FAQ due to differing opinions.
7.  [Well done bro (Bagel demo)](https://i.redd.it/776pwos6t62f1.png) (Score: 2)
    * A link to an image of Bagel demo.
8.  [ComfyUI VS Forge classic](https://www.reddit.com/gallery/1ks5izo) (Score: 1)
    * Comparison of ComfyUI and Forge, with recommendations for using StabilityMatrix.
9.  [Please Help ComfyUI pics look really blurry.](https://www.reddit.com/r/StableDiffusion/comments/1ks0kwi/please_help_comfyui_pics_look_really_blurry/) (Score: 1)
    * Users troubleshoot blurry images in ComfyUI, suggesting checks for correct settings and negative prompts.
10. [Speed Up Vace](https://www.reddit.com/r/StableDiffusion/comments/1ks5i4c/speed_up_vace/) (Score: 1)
    * Discussion on speeding up Vace, with suggestions to try Kijai wrapper with all the additional stuff (Torch, sage...)
11. [Python code to run SDXL](https://www.reddit.com/r/StableDiffusion/comments/1ks78fw/python_code_to_run_sdxl/) (Score: 1)
    * Users ask for an error log.
12. [Crowdsourced Checkpoint(s) from Scratch?](https://www.reddit.com/r/StableDiffusion/comments/1ks0o37/crowdsourced_checkpoints_from_scratch/) (Score: 0)
    * Discusses the challenges and practicality of crowdsourcing checkpoints from scratch.
13. [AI OFM](https://www.reddit.com/r/StableDiffusion/comments/1ks2fop/ai_ofm/) (Score: 0)
    * The post is considered sketchy spam account.
14. [Can you bring me up to speed on open source alternatives?](https://www.reddit.com/r/StableDiffusion/comments/1ks2j6d/can_you_bring_me_up_to_speed_on_open_source/) (Score: 0)
    * Discussion on open source alternatives.
15. [Weird pixelated squares on generation](https://www.reddit.com/r/StableDiffusion/comments/1ks4g4i/weird_pixelated_squares_on_generation/) (Score: 0)
    * User found out that having too long prompts caused this issue.

# Detailed Analysis by Thread
**[One of the banes of this scene is when something new comes out (Score: 40)](https://www.reddit.com/r/StableDiffusion/comments/1ks1iot/one_of_the_banes_of_this_scene_is_when_something/)**
*  **Summary:**  Open-source developers are frustrated with the lack of access to high-end hardware. They can't afford the cloud credits to experiment at scale, and the open-source scene is bottlenecked by hardware, mostly thanks to NVIDIA’s pricing and availability.
*  **Emotion:** The overall emotional tone is positive, but there is some negative sentiment related to frustrations with hardware limitations.
*  **Top 3 Points of View:**
    * Open-source development is being held back by the high cost and limited availability of powerful GPUs.
    * Open-source tools are still valuable and can produce excellent results despite resource constraints.
    * Paid platforms have an advantage due to their greater access to resources, not necessarily superior intelligence or skills.

**[Badge Bunny Episode 0 (Score: 18)](https://v.redd.it/deu5h531862f1)**
*  **Summary:** Reactions to a new episode, with some noting its closed-source nature.
*  **Emotion:** The emotional tone is neutral.
*  **Top 3 Points of View:**
    * The video is closed source.
    * User is excited to try fantasy speaking.
    * The video is a bit questionable and unexpected.

**[I made gradio interface for Bagel if you don't want to use don't want to run it through jupyter (Score: 11)](https://github.com/ansmom/BagelGradio/tree/gradio-feat)**
*  **Summary:** You still need more than 24GB of vram to run it and it's pretty slow but it works. Hopefully somebody will deploy it to HF if they haven't already.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    * The interface is helpful for those who don't want to use Jupyter.
    * A screenshot of the interface should be included.
    * Users are concerned about NSFW filter.

**[How can I unblurr a picture I tried upscaling with supir it doesn't unblur it (Score: 10)](https://i.redd.it/2m9ftqkdm62f1.png)**
*  **Summary:** Users are seeking methods to unblur images after upscaling, with suggestions including img2img and specific models.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    * Use Img2Img with 0.4 - 0.5 denoise and canny controlnet.
    * Fix in low scale.with img to img, then throw into supir.
    * Try using a re-focusing model.

**[How are these AI Influencers made? (Score: 5)](https://www.reddit.com/r/StableDiffusion/comments/1ks2yiw/how_are_these_ai_influencers_made/)**
*  **Summary:** Discussion on the techniques and tools used to create AI influencers.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    *  Flux with LORAs and img-to-img is used.
    * Training the flux model in dreambooth leads to better consistency and overall results.
    * RTX 5090 or something with more vram will help.

**[Most basic knowledge FAQ? (Score: 3)](https://www.reddit.com/r/StableDiffusion/comments/1ks4xw3/most_basic_knowledge_faq/)**
*  **Summary:** All of that comes down to opinions so a sticky like that would be so contentious that it would just not work.
*  **Emotion:** The overall emotional tone is negative.
*  **Top 1 Point of View:**
    * A basic knowledge FAQ would be contentious and wouldn't work.

**[Well done bro (Bagel demo) (Score: 2)](https://i.redd.it/776pwos6t62f1.png)**
*  **Summary:** https://preview.redd.it/0m0qqpv7x62f1.png?width=1253&format=png&auto=webp&s=da681283958bd2a2d2ac00a78730531426d5dc67
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 0 Points of View:**

**[ComfyUI VS Forge classic (Score: 1)](https://www.reddit.com/gallery/1ks5izo)**
*  **Summary:** Comfy should be faster, but not by that amount. I recommend using StabilityMatrix to easily share models between comfy and other UIs.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Point of View:**
    * Comfy should be faster, but not by that amount.

**[Please Help ComfyUI pics look really blurry. (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ks0kwi/please_help_comfyui_pics_look_really_blurry/)**
*  **Summary:** Make sure you have correct Flux Vae, Clip and text encoders in their proper locations. Try putting something in the negative prompt such as "blurry", "Distorted" and "Low quality".
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    * Check Flux Vae, Clip, and text encoders.
    * Use negative prompts like "blurry," "distorted," and "low quality."
    * Ensure workflows are correct for the model being used.

**[Speed Up Vace (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ks5i4c/speed_up_vace/)**
*  **Summary:** Try Kijai wrapper with all the additional stuff (Torch, sage...) it should be much faster.
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 3 Points of View:**
    * Try Kijai wrapper.
    * Get the CauseVid lora from Kijai.
    * Try q5 or q4.

**[Python code to run SDXL (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ks78fw/python_code_to_run_sdxl/)**
*  **Summary:** you're not gonna get an answer unless provide us with an actual output (error log)
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Point of View:**
    * Provide an error log.

**[Crowdsourced Checkpoint(s) from Scratch? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ks0o37/crowdsourced_checkpoints_from_scratch/)**
*  **Summary:** Running multi-node in the same network is already hard, let alone across the internet. Without regularization using non-goon images, it will collapse. Corpo f-wads take the brunt of pretraining, which is expensive compared to just finetuning.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 1 Point of View:**
    * Running multi-node in the same network is already hard, let alone across the internet.

**[AI OFM (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ks2fop/ai_ofm/)**
*  **Summary:** Sketchy spam account, either a scam or useless
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Point of View:**
    * The account is a scam or useless.

**[Can you bring me up to speed on open source alternatives? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ks2j6d/can_you_bring_me_up_to_speed_on_open_source/)**
*  **Summary:** HiDream and HiDream V2 are good for generating image. For longer duration simple scene framepack based on hunyuan is a good choice. SkyReels V2 can do Diffusion forcing, which you "fused" multiple video into a infinite sequence. For
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Point of View:**
    * Hidream is good for generating images.

**[Weird pixelated squares on generation (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1ks4g4i/weird_pixelated_squares_on_generation/)**
*  **Summary:** Addendum: I have discovered having too long prompts caused this issue
*  **Emotion:** The overall emotional tone is neutral.
*  **Top 1 Points of View:**
   * Having too long prompts caused the issue.
