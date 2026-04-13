---
title: "Stable Diffusion Subreddit"
date: "2026-02-15"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["StableDiffusion", "AI", "ImageGeneration", "LoRA", "GPU"]
---

# Overall Ranking and Top Discussions
1.  [I got tired of guessing if my Character LoRA trainings were actually good, so I built a local tool to measure them scientifically. Here is MirrorMetric (Open Source and totally local)](https://www.reddit.com/gallery/1r5j8a8) (Score: 116)
    *   Users discuss MirrorMetric, an open-source tool for scientifically measuring Character LoRA training quality and consistency.
2.  [Which image edit model can reliably decensor manga/anime?](https://i.redd.it/5sahuir5upjg1.jpeg) (Score: 26)
    *   The thread seeks reliable image edit models for decensoring manga/anime, with recommendations for specific models like Klein 9B.
3.  [ZPix (formerly Z-Image Turbo for Windows) now supports LoRA hotswap and trigger word automatic insertion.](https://i.redd.it/lxj1xvfo3pjg1.png) (Score: 12)
    *   Announces ZPix updates including LoRA hotswap and trigger word auto-insertion, sparking user questions about ControlNet and other features.
4.  [Building an AI rig](https://www.reddit.com/r/StableDiffusion/comments/1r5lwf9/building_an_ai_rig/) (Score: 8)
    *   Community discusses optimal PC configurations for AI/video generation, focusing on GPU (e.g., RTX 5090) and RAM over CPU for VRAM-intensive tasks.
5.  [LTX2 Distilled Lipsync | Made locally on 3090](https://youtu.be/V9Yk8Tul6C4) (Score: 5)
    *   Showcases LTX2 for local lipsync animation on a 3090 GPU.
6.  [Ace Step 1.5 as sampling material](https://youtu.be/QsXmQauss5I) (Score: 4)
    *   Explores the audio quality of Ace Step 1.5 when used as sampling material.
7.  [Best AI of sound effects for Audio? Looking for the best AI to generate/modify SFX for game dev (Audio-to-Audio or Text-to-Audio)](https://www.reddit.com/r/StableDiffusion/comments/1r5o3c1/best_ai_of_sound_effects_for_audio_looking_for/) (Score: 2)
    *   Inquires about the best AI tools for generating/modifying sound effects for game development.
8.  [Wan2.2-Rapid-14B-AllInOne...Ignoring last frames entirely.](https://www.reddit.com/r/StableDiffusion/comments/1r5jwdx/wan22rapid14ballinoneignoring_last_frames_entirely/) (Score: 1)
    *   Troubleshooting an issue where Wan2.2-Rapid-14B-AllInOne ignores video's last frames.
9.  [Any way to add audio to video in LTX2?](https://www.reddit.com/r/StableDiffusion/comments/1r5piyy/any_way_to_add_audio_to_video_in_ltx2/) (Score: 1)
    *   Asks for methods to add audio to LTX2 generated videos, with a suggestion of Wan2GP.
10. [How can I change a character’s outfit in an anime video while keeping the original animation?](https://www.reddit.com/r/StableDiffusion/comments/1r5k5mw/how_can_i_change_a_characters_outfit_in_an_anime/) (Score: 0)
    *   Seeks advice on changing character outfits in anime videos while maintaining animation, suggesting LTX-2 or Wan 2.2 Animate.
11. [Non-Human Character Consistency?](https://www.reddit.com/r/StableDiffusion/comments/1r5j9b0/nonhuman_character_consistency/) (Score: 0)
    *   Discovers models and techniques for achieving consistent non-human character designs in Stable Diffusion.
12. [Searching for a LLM that isn't censored on "spicy" themes, for prompt improvement.](https://www.reddit.com/r/StableDiffusion/comments/1r5nmuw/searching_for_a_llm_that_isnt_censored_on_spicy/) (Score: 0)
    *   Looks for uncensored LLMs for prompt improvement on 'spicy' themes, recommending 'heretic' models and Grok.
13. [Is there any AI ( local prefered ) that can generate multiple image frame from one output](https://www.reddit.com/r/StableDiffusion/comments/1r5lanh/is_there_any_ai_local_prefered_that_can_generate/) (Score: 0)
    *   Queries about local AI tools capable of generating multiple image frames from a single output, mentioning Qwen image edit workflows.

# Detailed Analysis by Thread
**[I got tired of guessing if my Character LoRA trainings were actually good, so I built a local tool to measure them scientifically. Here is MirrorMetric (Open Source and totally local)](<https://www.reddit.com/gallery/1r5j8a8>)**
*  **Summary:**  The discussion revolves around I got tired of guessing if my Character LoRA trainings were actually good, so I built a local tool to measure them scientifically. Here is MirrorMetric (Open Source and totally local). Nice. Very interested. Do you also use it to evaluate different training checkpoints and lora model strengths?. Welldone, but you want an easy way to find out if your Lora looks alike? Generate 10+ pictures and put them on your iPhone gallery, scroll down to people and click on one of your Lora’s photo. And your iPhone will populate all the identical images. It 100% gets it for me. Does this only work with character lora?. Or does it also work with style/object loras?. First off, I'm not smart enough to comprehend any of this. Secondly thank you for the great work you have here. It's impressive that you made this, but it doesn't seem practical for most use cases. It's only useful if you're training on a real person's face and you have a dataset that inexplicably has that person's head in multiple directions. super interesting thing!. Andy has been training a lot of LoRAs recently. He has created MirrorMetric to analyze his generated images against his training dataset. It's a local Python script that uses InsightFace and generates a standalone interactive HTML dashboard. Ha, you want to know my approach to evaluating likeness? I’ve been putting generated images on my iPhone and waiting to see if it would group them to be the same person. I guess I prefer your way from now on haha! Seriously though, this looks awesome and I can’t wait to try it. Interesting! Does it work on anime?. There should be an extensible open source framework for LoRA training with ComfyUI level flexibility.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The tool (MirrorMetric) is impressive and provides a scientific way to evaluate LoRA trainings for character likeness, addressing the subjectivity of manual checking.
    * There are questions about the tool's applicability beyond simple character LoRAs, especially for complex scenarios like multiple outfits or stylistic training where 'better' is subjective.
    * Some users shared their own simpler, albeit less scientific, methods for evaluating LoRA likeness (e.g., iPhone photo grouping) and expressed excitement to try MirrorMetric.

**[Which image edit model can reliably decensor manga/anime?](<https://i.redd.it/5sahuir5upjg1.jpeg>)**
*  **Summary:**  The discussion revolves around Which image edit model can reliably decensor manga/anime?. It probably depends on what the model assumes is under the censor bars. If it is a finger it should work. if it is another appendage that most models are just not trained for then it's going to look weird i guess. All of them?. train a klein 9b lora for it. Klein 9B https://preview.redd.it/bsnfcvf22qjg1.png?width=831&format=png&auto=webp&s=b3d06b3c0a0a1add545dcf2f51e29c467ecd9af7
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Specific models like Klein 9B are recommended for reliable decensoring of manga/anime images.
    * The success of decensoring depends on what the model assumes is under the censor bars and if it has been trained for such content.
    * General affirmation that many image editing models can perform this task.

**[ZPix (formerly Z-Image Turbo for Windows) now supports LoRA hotswap and trigger word automatic insertion.](<https://i.redd.it/lxj1xvfo3pjg1.png>)**
*  **Summary:**  The discussion revolves around ZPix (formerly Z-Image Turbo for Windows) now supports LoRA hotswap and trigger word automatic insertion.. any chance of an anchor pics?. Does it support ControlNet?. PS: More features such as Generations History are coming. Stay tuned! ;). Nice ! Stable-difusion.cpp ?.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Users are interested in the new features like LoRA hotswap and trigger word automatic insertion, and future updates like generation history.
    * Questions were raised about support for other features like ControlNet and specific backend integrations (Stable-diffusion.cpp).
    * General positive reception for the tool's improvements.

**[Building an AI rig](<https://www.reddit.com/r/StableDiffusion/comments/1r5lwf9/building_an_ai_rig/>)**
*  **Summary:**  The discussion revolves around Building an AI rig. 2950x, dual 3090, 192gb ddr4 is my AI rig and daily driver desktop. Eventually it will be a dedicated AI server once I build a smaller more modern pc for my desktop. Hear me out. After the cost of the GPU and all the other stuff, power costs included it might be worth spending some time on something like Runpod to work out the sweet spot before investing your hard earned reddies. That CPU is pointless overkill for local video generation. CPU choice is almost irrelevant. Multi-gpu setups (can be) a pain for local AI and its not as simple as pressing "go". I would get a 5090 and at least 64gb of ram and call it good. either go with a rtx 5090 or rtx pro 6000 if you want the current best of the best for local system. There is a guy on YouTube hosting 6 M150 for local llm. No matter what you are going with you will regret it later. If you feel confident setting up multi-GPU (which isn't easy) your two 3090s will be the better choice, as VRAM beats everything if you are going for the large models. Also buying right now is insanity with the current prices, but its your money. Dual GPU setup is not good for diffusion. 3090 is old and can't work with modern technology which sped up generation times. 5090 32GB VRAM and 96-128GB RAM with any CPU is good for AI diffusion. Top of the line gen 5 NVME. > threadripper my brother in christ why. you do not need a massive cpu for video generation. as others have said, it's not really worth going dual gpu. get a 5090 and a normal cpu. The only decent upgrade I see from a 4090 is a pro 6000 with 96GB VRAM. As soon as a company allows a VRAM update nVidia will be toast, since their low RAM levels have *** me off for 2 years now, but until that happens there's really only one card worth having. To work comfortably with local video models you need between 80GB and 96GB combined VRAM/ RAM. The less resources you have, the more technical of a person you need to be to understand how to overcome limitations. Having 32GB VRAM and 128GB system RAM means
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Single, high-end GPUs like the RTX 5090 (or RTX Pro 6000) with ample VRAM (e.g., 32GB) are generally preferred over multi-GPU setups for AI diffusion, especially for video generation.
    * CPU choice is largely irrelevant for local video generation; the focus should be on GPU VRAM and system RAM (e.g., 96-128GB).
    * Concerns were raised about the high cost of components, the complexity of multi-GPU setups, and the rapid pace of hardware/software development potentially leading to regret.

**[LTX2 Distilled Lipsync | Made locally on 3090](<https://youtu.be/V9Yk8Tul6C4>)**
*  **Summary:**  The discussion revolves around LTX2 Distilled Lipsync | Made locally on 3090. <3.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The post showcases the successful local generation of lipsync animation using LTX2 on a 3090 GPU.

**[Ace Step 1.5 as sampling material](<https://youtu.be/QsXmQauss5I>)**
*  **Summary:**  The discussion revolves around Ace Step 1.5 as sampling material. how do you find the audio quality, as someone who's likely familiar with music/audio?.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The main point of discussion is the quality of audio generated by the Ace Step 1.5 model, particularly for users familiar with music/audio production.

**[Best AI of sound effects for Audio? Looking for the best AI to generate/modify SFX for game dev (Audio-to-Audio or Text-to-Audio)](<https://www.reddit.com/r/StableDiffusion/comments/1r5o3c1/best_ai_of_sound_effects_for_audio_looking_for/>)**
*  **Summary:**  The discussion revolves around Best AI of sound effects for Audio? Looking for the best AI to generate/modify SFX for game dev (Audio-to-Audio or Text-to-Audio). why would you need audio to audio for this when you can just type a prompt to get what you want?. Seconding this. Following.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Users are seeking recommendations for the best AI tools (Audio-to-Audio or Text-to-Audio) for generating or modifying sound effects, specifically for game development.
    * There's a question about the necessity of Audio-to-Audio when Text-to-Audio might suffice, implying a focus on prompt-based generation.
    * General interest in the topic, with users "seconding" and "following" the discussion.

**[Wan2.2-Rapid-14B-AllInOne...Ignoring last frames entirely.](<https://www.reddit.com/r/StableDiffusion/comments/1r5jwdx/wan22rapid14ballinoneignoring_last_frames_entirely/>)**
*  **Summary:**  The discussion revolves around Wan2.2-Rapid-14B-AllInOne...Ignoring last frames entirely.. Don't you need to use the official FFLF comfy node for Wan2.2?.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The primary concern is the Wan2.2-Rapid-14B-AllInOne model ignoring last frames during video generation.
    * A suggested solution is to use the official FFLF comfy node for Wan2.2 to address the issue.

**[Any way to add audio to video in LTX2?](<https://www.reddit.com/r/StableDiffusion/comments/1r5piyy/any_way_to_add_audio_to_video_in_ltx2/>)**
*  **Summary:**  The discussion revolves around Any way to add audio to video in LTX2?. Wan2GP. External audio.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The user is asking for methods to add audio to video generated with LTX2.
    * A specific tool/method, Wan2GP, for external audio is suggested.

**[How can I change a character’s outfit in an anime video while keeping the original animation?](<https://www.reddit.com/r/StableDiffusion/comments/1r5k5mw/how_can_i_change_a_characters_outfit_in_an_anime/>)**
*  **Summary:**  The discussion revolves around How can I change a character’s outfit in an anime video while keeping the original animation?. This is not something I have tried myself yet but if I understand correctly you can use LTX-2 for this. Just take the first frame, edit the image with the new clothes (qwen edit, gemini, etc) and then animate that edited image using the video as reference with LTX-2. I saved this one a while back cause I was looking for the same thing too https://www.reddit.com/r/comfyui/s/jUkm3jQVTs Though I haven’t tried it personally…. You can try Wan 2.2 Animate, though I'm not sure if an image of the character with the different outfit is enough or if you'll need (or it will be better) to provide a modified first frame. If you need to modify the first frame, you can do it with an image editing model, like Qwen Image Edit or Flux 2 Klein. You will most probably need to do it all in ComfyUI, though. Paid sites like Kling can do it, 10 - 15 second clips at a time. Not honestly sure how you would do it locally.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Users are seeking methods to change character outfits in anime videos while preserving original animation.
    * Solutions involve using models like LTX-2 or Wan 2.2 Animate, possibly combined with image editing models (e.g., Qwen Image Edit, Flux 2 Klein) to modify initial frames.
    * Some suggest that ComfyUI is likely necessary for such workflows, while paid services like Kling offer an alternative for shorter clips.

**[Non-Human Character Consistency?](<https://www.reddit.com/r/StableDiffusion/comments/1r5j9b0/nonhuman_character_consistency/>)**
*  **Summary:**  The discussion revolves around Non-Human Character Consistency?. Z-Image, Klein, Qwen and Anima are some of the current "newer" models that are suitable for this type of character.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The question is about achieving consistent non-human characters in Stable Diffusion.
    * Several newer models like Z-Image, Klein, Qwen, and Anima are recommended for training and maintaining consistency for cartoon-style or non-human characters.

**[Searching for a LLM that isn't censored on "spicy" themes, for prompt improvement.](<https://www.reddit.com/r/StableDiffusion/comments/1r5nmuw/searching_for_a_llm_that_isnt_censored_on_spicy/>)**
*  **Summary:**  The discussion revolves around Searching for a LLM that isn't censored on "spicy" themes, for prompt improvement.. Yeah, I use Grok on OpenRouter. It has zero morals. [https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard) here is the leaderboard, you can locally host a model if it doesn't fall under "proprietary"... . There are a ton for local use. I use Qwen3 VL 8b abliterated. I just saw another today that's the same but it's been tweaked specifically for this: https://huggingface.co/mradermacher/Qwen3-VL-8B-NSFW-Caption-V4-GGUF. For local check out Z engineer. https://huggingface.co/BennyDaBall He also has a ComfyUI node you can use. Heretic models are what you want, they have refusals removed so they can’t say no There are heretic versions of the popular ones, just search for any good model and add heretic. For example qwen 3 vl 8B instruct heretic.gguf or much larger ones depending on your gpu. Grok—it’s the only thing it’s still useful for, lol. Gpt-Oss 20b heresy is best and fast - [https://huggingface.co/MuXodious/gpt-oss-20b-RichardErkhov-heresy](https://huggingface.co/MuXodious/gpt-oss-20b-RichardErkhov-heresy).
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * Users are looking for uncensored LLMs, primarily for local use, to assist with prompt generation for 'spicy' themes without content restrictions.
    * Recommendations include specific 'Heretic' versions of models (e.g., Qwen 3 VL 8B instruct heretic, Gpt-Oss 20b heresy) which have refusal mechanisms removed.
    * Grok (on OpenRouter) is also mentioned as an uncensored option, along with resources like Hugging Face leaderboards for discovering such models.

**[Is there any AI ( local prefered ) that can generate multiple image frame from one output](<https://www.reddit.com/r/StableDiffusion/comments/1r5lanh/is_there_any_ai_local_prefered_that_can_generate/>)**
*  **Summary:**  The discussion revolves around Is there any AI ( local prefered ) that can generate multiple image frame from one output. People have created several workflows for this using Qwen image edit 2511.
*  **Emotion:** The overall emotional tone is predominantly neutral. Many comments were informative, technical, or inquisitive, focusing on practical aspects rather than strong feelings.
*  **Top 3 Points of View:**
    * The user is asking for local AI tools or workflows that can generate multiple image frames from a single output, implying animation or sequential image generation.
    * Workflows utilizing Qwen image edit 2511 are suggested as a way to achieve this.
