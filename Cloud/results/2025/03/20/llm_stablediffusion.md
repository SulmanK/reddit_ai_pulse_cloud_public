---
title: "Stable Diffusion Subreddit"
date: "2025-03-20"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["stablediffusion", "AI", "image generation"]
---

# Overall Ranking and Top Discussions
1.  [training a lora locally with comfyui](https://www.reddit.com/r/StableDiffusion/comments/1jfrwmy/training_a_lora_locally_with_comfyui/) (Score: 7)
    *   The discussion revolves around the best applications and methods for training a LoRA (Low-Rank Adaptation) model locally using ComfyUI, with suggestions for alternative tools like Onetrainer and Kohya_ss.
2.  [What am I doing wrong? I've tried steps between 15-50, CFG between 1-5, and Denoise between 0.1 to 1.0 for the 2nd pass KSampler. Quality gets higher the higher the Denoise, but that completely changes the image, and I wanna keep that to the original. Tried with 4 different Turbo/Lightning LoRAs.](https://www.reddit.com/gallery/1jfqj7o) (Score: 5)
    *   The thread discusses image upscaling techniques in Stable Diffusion, specifically addressing issues with image quality and detail retention when using high denoise values and Turbo/Lightning LoRAs. Users recommend using upscalers and adjusting prompts to retain style.
3.  [This guy released a massive ComfyUI workflow for morphing AI textures... it's really impressive (TextureFlow)](https://www.youtube.com/watch?v=NSQLVNAe5Hc) (Score: 4)
    *   A user shares a ComfyUI workflow called TextureFlow for morphing AI textures, describing it as impressive. The full workflow image is linked in the comments.
4.  [AI my art, please! (I can’t figure it out on my computer. Tips would be appreciated!)](https://i.redd.it/5mbiw0f1kvpe1.jpeg) (Score: 3)
    *   The thread is about a user requesting AI assistance to generate art from their provided image, with other users sharing generated images and suggesting tools like InvokeAI. The moderators stepped in to ensure the thread doesn't turn into a "begging sub."
5.  [Im I crazy or this impressive?](https://x.com/k_matsumaru/status/1902263276718977362) (Score: 2)
    *   The discussion is centered on the impressive nature of AI-generated videos using tools like Kling AI and Wan 2.1, with users comparing their capabilities and hardware requirements.
6.  [How do I get this UI information? I need to know what extension group this node belongs to.](https://i.redd.it/5qrzpbd5avpe1.png) (Score: 1)
    *   The user is asking how to find what extension a node belongs to in ComfyUI and they were directed to core settings, ComfyUI Manager, and a specific GitHub repository.
7.  [How to retexture on ComfyUI?](https://www.reddit.com/r/StableDiffusion/comments/1jfqm5b/how_to_retexture_on_comfyui/) (Score: 1)
    *   The thread discusses techniques for retexturing in ComfyUI, distinguishing between retexturing 3D models and modifying video textures. Users suggest tools like Stableprojectorz for 3D models and video-to-video AI generators for videos.
8.  [Do you have any workflows to make the eyes more realistic? I've tried Flux, SDXL, with adetailer, inpaint and even Loras, and the results are very poor.](https://www.reddit.com/r/StableDiffusion/comments/1jfri3x/do_you_have_any_workflows_to_make_the_eyes_more/) (Score: 1)
    *   The discussion focuses on achieving more realistic eyes in AI-generated images using Stable Diffusion. Users share suggestions like using Adetailer, GFPGAN, and specific models like Splashed Mix DMD.
9.  [Using a VAE makes my generated art pixelated](https://www.reddit.com/r/StableDiffusion/comments/1jfsp37/using_a_vae_makes_my_generated_art_pixelated/) (Score: 1)
    *   The user is experiencing pixelation in their generated art when using a VAE (Variational Autoencoder). The solutions point to using the correct VAE for the model or not needing a separate VAE at all as most models include one.
10. [Turn the rifle to the right?](https://i.redd.it/2bvb8v60yvpe1.png) (Score: 0)
    *   The post is a request for help adjusting the angle of a rifle in an image for a book cover to comply with advertising policies, offering a tip for assistance.
11. [How can i recreate this corset dress based on one image?](https://i.redd.it/43fgde576vpe1.jpeg) (Score: 0)
    *   The user wants to recreate a corset dress from a single image. Suggestions include using IP-Adapter, ControlNet, I2V models like WAN with LoRA training, detailed prompt descriptions with Flux, and generating many images until a desired result is achieved.
12. [WAN is useless with characters when using image to video if you need preservation](https://v.redd.it/3c4d3np2dvpe1) (Score: 0)
    *   The thread discusses the limitations of using WAN for image-to-video generation, particularly regarding character consistency. Users share their experiences and offer advice on working within WAN's limitations by controlling camera movements and shot compositions.
13. [Are there any open-source alternatives to this?](https://www.reddit.com/gallery/1jfw94l) (Score: 0)
    *   A user is asking about open-source alternatives and another user says that a workflow can be made with SDXL or Flux.
14. [Why does my generated art look so different than other people's art?](https://www.reddit.com/r/StableDiffusion/comments/1jfssyo/why_does_my_generated_art_look_so_different_than/) (Score: 0)
    *   The discussion addresses why generated art looks different from others' results. Key points include matching settings, seeds, resolutions, using PNG info to import metadata, and considering the impact of seed generation device and the usage of extensions.
15. [Can anyone help me figure out what tools are generating these videos?](https://www.reddit.com/r/StableDiffusion/comments/1jfvfjn/can_anyone_help_me_figure_out_what_tools_are/) (Score: 0)
    *   A user asks for help identifying the tools used to generate certain videos, but receives a cryptic response.

# Detailed Analysis by Thread
**[training a lora locally with comfyui (Score: 7)](https://www.reddit.com/r/StableDiffusion/comments/1jfrwmy/training_a_lora_locally_with_comfyui/)**
*   **Summary:**  The discussion revolves around the best applications and methods for training a LoRA (Low-Rank Adaptation) model locally using ComfyUI.
*   **Emotion:** The overall emotional tone of the thread is Neutral, with a mix of positive and neutral comments. The sentiment scores range from 0.41 to 0.91, indicating a relatively balanced and informative discussion.
*   **Top 3 Points of View:**
    *   Using dedicated training applications like Onetrainer or Kohya_ss is more effective due to wider community support and development.
    *   Flux Gym is a good option for ease of use, though not specifically within ComfyUI.
    *   Kijai's Flux training nodes and workflow can be used, but SDXL or 1.5 training nodes for Comfy are not readily available.

**[What am I doing wrong? I've tried steps between 15-50, CFG between 1-5, and Denoise between 0.1 to 1.0 for the 2nd pass KSampler. Quality gets higher the higher the Denoise, but that completely changes the image, and I wanna keep that to the original. Tried with 4 different Turbo/Lightning LoRAs. (Score: 5)](https://www.reddit.com/gallery/1jfqj7o)**
*   **Summary:** The thread discusses image upscaling techniques in Stable Diffusion, specifically addressing issues with image quality and detail retention when using high denoise values and Turbo/Lightning LoRAs.
*   **Emotion:** The emotional tone of the thread is generally Neutral, with sentiment scores around 0.51 and 0.91.
*   **Top 3 Points of View:**
    *   Use upscaling with the extras tab in webforge for an unrefined upscale.
    *   Implement Ultimate SD Upscale in your workflow.
    *   If you want lower resolution with less detail, use an upscaler. Lightning and turbo are great for speed, but they lose a bit of prompt comprehension and quality.

**[This guy released a massive ComfyUI workflow for morphing AI textures... it's really impressive (TextureFlow) (Score: 4)](https://www.youtube.com/watch?v=NSQLVNAe5Hc)**
*   **Summary:**  A user shares a ComfyUI workflow called TextureFlow for morphing AI textures, describing it as impressive.
*   **Emotion:** The emotional tone of the thread is generally Positive. The sentiment scores are 0.91, reflecting enthusiasm about the shared workflow.
*   **Top 3 Points of View:**
    *   The full workflow image is linked.
    *   The workflow is impressive.

**[AI my art, please! (I can’t figure it out on my computer. Tips would be appreciated!) (Score: 3)](https://i.redd.it/5mbiw0f1kvpe1.jpeg)**
*   **Summary:** The thread is about a user requesting AI assistance to generate art from their provided image, with other users sharing generated images and suggesting tools.
*   **Emotion:** The emotional tone is primarily Neutral, with sentiment scores ranging from 0.56 to 0.97. There is one comment that expresses a Neutral sentiment regarding moderators taking action.
*   **Top 3 Points of View:**
    *   Several users provide generated images as assistance.
    *   InvokeAI is a suggested tool.
    *   Moderators warn against the thread becoming a "begging sub."

**[Im I crazy or this impressive? (Score: 2)](https://x.com/k_matsumaru/status/1902263276718977362)**
*   **Summary:** The discussion is centered on the impressive nature of AI-generated videos using tools like Kling AI and Wan 2.1, with users comparing their capabilities and hardware requirements.
*   **Emotion:** The thread exhibits a mix of Neutral and Negative sentiments. The sentiment scores range from 0.50 to 0.96, indicating diverse opinions and considerations.
*   **Top 3 Points of View:**
    *   Kling AI is a website (not an open-source tool) requiring significant computational power.
    *   Wan 2.1 can produce similar results but is not as easy or fast as Kling AI; it is not possible to run locally.
    *   Img2video seems better for image alterations than even Gemini.

**[How do I get this UI information? I need to know what extension group this node belongs to. (Score: 1)](https://i.redd.it/5qrzpbd5avpe1.png)**
*   **Summary:**  The user is asking how to find what extension a node belongs to in ComfyUI and they were directed to core settings, ComfyUI Manager, and a specific GitHub repository.
*   **Emotion:** The emotional tone of the thread is predominantly Neutral. The sentiment scores are mostly high, ranging from 0.53 to 0.97.
*   **Top 3 Points of View:**
    *   The node ID badge mode is in core ComfyUI settings.
    *   The extension can be found at a provided GitHub link.
    *   The extension can be found by searching for Allor in the ComfyUI Manager.

**[How to retexture on ComfyUI? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1jfqm5b/how_to_retexture_on_comfyui/)**
*   **Summary:** The thread discusses techniques for retexturing in ComfyUI, distinguishing between retexturing 3D models and modifying video textures.
*   **Emotion:** The emotional tone of the thread is Neutral. The sentiment score is 0.72.
*   **Top 3 Points of View:**
    *   Stableprojectorz might be handy if you want to retexture a 3D model.
    *   Midjourney,Sd, Flux are Image Tools which are good for a single image but lack temporal consistency which is needed for videos.
    *   Check for modern ai video generators.

**[Do you have any workflows to make the eyes more realistic? I've tried Flux, SDXL, with adetailer, inpaint and even Loras, and the results are very poor. (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1jfri3x/do_you_have_any_workflows_to_make_the_eyes_more/)**
*   **Summary:** The discussion focuses on achieving more realistic eyes in AI-generated images using Stable Diffusion.
*   **Emotion:** The emotional tone is mixed with Neutral and Negative sentiments.
*   **Top 3 Points of View:**
    *   Adetailer usually does the trick
    *   Give Splashed Mix DMD a try
    *   Try GFPGAN in Extras Tab

**[Using a VAE makes my generated art pixelated (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1jfsp37/using_a_vae_makes_my_generated_art_pixelated/)**
*   **Summary:**  The user is experiencing pixelation in their generated art when using a VAE (Variational Autoencoder).
*   **Emotion:** The emotional tone is Neutral. The sentiment scores range from 0.57 to 0.73.
*   **Top 3 Points of View:**
    *   The model is using the wrong VAE.
    *   Models typically have their own vae included in the checkpoint file, so you shouldn't need a separate one anyway.
    *   Double-check that you have the right VAE.

**[Turn the rifle to the right? (Score: 0)](https://i.redd.it/2bvb8v60yvpe1.png)**
*   **Summary:**  The post is a request for help adjusting the angle of a rifle in an image for a book cover to comply with advertising policies, offering a tip for assistance.
*   **Emotion:** The emotional tone is mixed between Negative and Neutral.
*   **Top 3 Points of View:**
    *   Amazon isn’t going to care about a 10 degree offset.
    *   Rotate the image 90 degrees and have the guy in profile
    *   The user needs the rifle to be adjusted to point to the right by about 10 degrees.

**[How can i recreate this corset dress based on one image? (Score: 0)](https://i.redd.it/43fgde576vpe1.jpeg)**
*   **Summary:** The user wants to recreate a corset dress from a single image.
*   **Emotion:** The emotional tone is Neutral, with sentiment scores ranging from 0.57 to 0.96.
*   **Top 3 Points of View:**
    *   It is not possible with one image.
    *   Use IP-Adapter and ControlNet.
    *    Describe it accurately in your prompt

**[WAN is useless with characters when using image to video if you need preservation (Score: 0)](https://v.redd.it/3c4d3np2dvpe1)**
*   **Summary:**  The thread discusses the limitations of using WAN for image-to-video generation, particularly regarding character consistency.
*   **Emotion:** The overall emotional tone of the thread is neutral, as most comments have sentiment scores around the neutral range (0.22 to 0.97).
*   **Top 3 Points of View:**
    *   WAN cheats when doing image to video.
    *   WAN works well for character consistency, but it isn't perfect.
    *   Character transitions through doors looks really janky

**[Are there any open-source alternatives to this? (Score: 0)](https://www.reddit.com/gallery/1jfw94l)**
*   **Summary:** A user is asking about open-source alternatives.
*   **Emotion:** The emotional tone is Neutral.
*   **Top 3 Points of View:**
    *   A workflow can be made with SDXL or Flux.

**[Why does my generated art look so different than other people's art? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1jfssyo/why_does_my_generated_art_look_so_different_than/)**
*   **Summary:** The discussion addresses why generated art looks different from others' results.
*   **Emotion:** The emotional tone of the thread is Neutral.
*   **Top 3 Points of View:**
    *   You need to use the same parameters and resolution.
    *   Use Hi-res fix x2 or face Adetailer plugin.
    *   Match the settings, including the seed number.

**[Can anyone help me figure out what tools are generating these videos? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1jfvfjn/can_anyone_help_me_figure_out_what_tools_are/)**
*   **Summary:** A user asks for help identifying the tools used to generate certain videos, but receives a cryptic response.
*   **Emotion:** The emotional tone is Positive.
*   **Top 3 Points of View:**
    *   Nice try, fatfellas.
