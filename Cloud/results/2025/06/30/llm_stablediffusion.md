---
title: "Stable Diffusion Subreddit"
date: "2025-06-30"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["stablediffusion", "AI", "image generation"]
---

# Overall Ranking and Top Discussions
1.  [Techniques to join small videos and create a longer one ... and not be noticed!](https://www.reddit.com/r/StableDiffusion/comments/1loe9vs/techniques_to_join_small_videos_and_create_a/) (Score: 6)
    * The discussion revolves around using Vace to create longer videos by blending smaller video segments, focusing on techniques to maintain coherence and avoid noticeable transitions.
2.  [I keep getting flashes with Wan](https://v.redd.it/kax908p5l3af1) (Score: 5)
    * This thread discusses a user experiencing flashes while using Wan and seeks solutions. Suggestions include using Causvid lora and replacing the tiled VAE decoder.
3.  [Image to Text generator](https://www.reddit.com/r/StableDiffusion/comments/1lodne3/image_to_text_generator/) (Score: 2)
    * This thread is about image to text generators with users suggesting the Flux Kontext model, Flux inpainting model, JoyCaption, and ollama nodes for ComfyUI.
4.  [Styles LORAs for Flux Kontext Dev](https://www.reddit.com/gallery/1lod3fe) (Score: 1)
    * Users are sharing and discussing Styles LORAs developed for Flux Kontext, with links to Civitai profiles and feedback on the generated images.
5.  [Frustrated: 24GB GPU, hours of training, and still no progress for image-to-image generation](https://www.reddit.com/r/StableDiffusion/comments/1locq4j/frustrated_24gb_gpu_hours_of_training_and_still/) (Score: 1)
    * A user expresses frustration about the lack of progress in image-to-image generation despite having a 24GB GPU and spending hours training. Others suggest checking the setup, using a Lora for a well-known model, and looking for install issues.
6.  [Best practices when using local AI Image/Video generation like Forge or ComfyUI?](https://www.reddit.com/r/StableDiffusion/comments/1loczyg/best_practices_when_using_local_ai_imagevideo/) (Score: 1)
    * Discussion centers around best practices for using local AI image/video generation tools like Forge and ComfyUI, with concerns about custom nodes and security.
7.  [Face similarity measurement tool?](https://www.reddit.com/r/StableDiffusion/comments/1loevcw/face_similarity_measurement_tool/) (Score: 1)
    * The thread is about finding a face similarity measurement tool, with suggestions including open source python recognition and Cubiq's FaceAnalysis node.
8.  [Help! Best CUDA + PyTorch + xformers versions for Stable Diffusion?](https://www.reddit.com/r/StableDiffusion/comments/1loeww1/help_best_cuda_pytorch_xformers_versions_for/) (Score: 1)
    * This thread discusses the best CUDA, PyTorch, and xformers versions for Stable Diffusion, suggesting skipping xformers until it updates and using sd-webui-forge-classic or Automatic1111.
9.  [Need help! Training LoRA blurry, and deformed face/body](https://www.reddit.com/r/StableDiffusion/comments/1lofyeo/need_help_training_lora_blurry_and_deformed/) (Score: 1)
    * A user needs help with blurry and deformed faces/bodies while training LoRA. Suggestions include training locally, using mirrored images, and using a Flux model.
10. [Kontext Hyper-realism](https://i.redd.it/ip84f29cq3af1.gif) (Score: 0)
    * The discussion is about hyper-realism using Kontext, with comments on the model's tendency to increase head sizes and potential model collapse.
11. [How long does it exactly take to download Stable Diffusion?? It's been 4 hours.](https://www.reddit.com/gallery/1lodcc6) (Score: 0)
    * A user asks how long it takes to download Stable Diffusion, with responses suggesting something might be wrong and recommending alternative downloads like ComfyUI.
12. [Please, provide instructions on how to use Runpod Comfyui](https://www.reddit.com/r/StableDiffusion/comments/1loczge/please_provide_instructions_on_how_to_use_runpod/) (Score: 0)
    * A user requests instructions on how to use Runpod Comfyui, and is advised to watch ryanontheinside video.
13. [How do you specify characters in a prompt?](https://www.reddit.com/r/StableDiffusion/comments/1lodqdm/how_do_you_specify_characters_in_a_prompt/) (Score: 0)
    * This thread is about specifying characters in a prompt, with suggestions including regional prompting, emphasis, and using Flux models.
14. [How to shard a model?](https://www.reddit.com/r/StableDiffusion/comments/1loeadq/how_to_shard_a_model/) (Score: 0)
    * A user asks how to shard a model, and gets pointed to a script for converting Flux to diffusers format.
15. [apply FLUX KONTEXT on a video?](https://www.reddit.com/r/StableDiffusion/comments/1lofo55/apply_flux_kontext_on_a_video/) (Score: 0)
    * This thread discusses applying FLUX KONTEXT on a video, with a user having issues with batch processing and suggestions to avoid changing each frame with latent noise.
16. [Can someone ELI5 how to do inpainting with Flux on ComfyUI?](https://www.reddit.com/r/StableDiffusion/comments/1loft2k/can_someone_eli5_how_to_do_inpainting_with_flux/) (Score: 0)
    * A user requests a simple explanation on how to do inpainting with Flux on ComfyUI, and gets a link to a tutorial.

# Detailed Analysis by Thread
**[Techniques to join small videos and create a longer one ... and not be noticed! (Score: 6)](https://www.reddit.com/r/StableDiffusion/comments/1loe9vs/techniques_to_join_small_videos_and_create_a/)**
*  **Summary:**  The discussion revolves around using Vace to create longer videos by blending smaller video segments. Key aspects include feeding the last few frames of the first video to generate the next few, compensating for color drift and saturation, and using a loop method for blending.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Vace is a useful tool for video creation by blending frames.
    * Color drift and saturation need to be compensated for.
    * Looping techniques can be used to blend videos, but might cause hallucinations.

**[I keep getting flashes with Wan (Score: 5)](https://v.redd.it/kax908p5l3af1)**
*  **Summary:** The user is experiencing flashes while using Wan and seeks solutions. Suggestions include using Causvid lora and replacing the tiled VAE decoder.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * The user is experiencing an issue (flashes) with the Wan setup.
    * Using Causvid Lora might resolve the issue.
    * Replacing the tiled VAE decoder with the regular VAE decoder may help.

**[Image to Text generator (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1lodne3/image_to_text_generator/)**
*  **Summary:** This thread discusses available image-to-text generators, with recommendations including the Flux Kontext model, JoyCaption, and ollama nodes for ComfyUI. Some of the tools are uncensored.
*  **Emotion:** Neutral, with some negativity associated with captioning for model creation.
*  **Top 3 Points of View:**
    * Flux Kontext model and Flux inpainting model might be able to do this using ComfyUI.
    * JoyCaption is uncensored and available on Huggingface.
    * Ollama nodes for ComfyUI can load an uncensored LLM to interpret images.

**[Styles LORAs for Flux Kontext Dev (Score: 1)](https://www.reddit.com/gallery/1lod3fe)**
*  **Summary:** Users are sharing and discussing Styles LORAs developed for Flux Kontext, with links to Civitai profiles and feedback on the generated images.
*  **Emotion:** Primarily Neutral, with some positive sentiments.
*  **Top 3 Points of View:**
    * Civitai profile is shared for testing the LORAs.
    * Some users prefer specific images as they better represent the intended style.
    * Users are curious about how well the LORAs transform subjects.

**[Frustrated: 24GB GPU, hours of training, and still no progress for image-to-image generation (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1locq4j/frustrated_24gb_gpu_hours_of_training_and_still/)**
*  **Summary:** A user is frustrated with a lack of progress in image-to-image generation despite sufficient resources. Suggestions include checking the setup, using a Lora for a well-known model, and looking for install issues.
*  **Emotion:** Predominantly Neutral.
*  **Top 3 Points of View:**
    * There might be an issue with the training setup (e.g., OneTrainer, Kohya/LoRA Easy Training Scripts).
    * Training a Lora for a well-known model might be more efficient.
    * An install issue (python, driver, CUDA) could be the root cause of no output.

**[Best practices when using local AI Image/Video generation like Forge or ComfyUI? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1loczyg/best_practices_when_using_local_ai_imagevideo/)**
*  **Summary:** Discussion centers around best practices for using local AI image/video generation tools like Forge and ComfyUI, with concerns about custom nodes and security.
*  **Emotion:** A mix of Positive and Negative, with a generally Neutral tone.
*  **Top 3 Points of View:**
    * Forge can be used without community nodes.
    * There are security concerns about the ComfyUI community relying on custom nodes.
    * Well-known nodes obtained through ComfyUI Manager should be safe, and the source code can be inspected.

**[Face similarity measurement tool? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1loevcw/face_similarity_measurement_tool/)**
*  **Summary:** The thread is about finding a face similarity measurement tool, with suggestions including open source python recognition and Cubiq's FaceAnalysis node.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Open source python recognition is an option
    * Cubiq's FaceAnalysis node works pretty well
    * SECourses YouTube might have some tools but it may be paywalled

**[Help! Best CUDA + PyTorch + xformers versions for Stable Diffusion? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1loeww1/help_best_cuda_pytorch_xformers_versions_for/)**
*  **Summary:** This thread discusses the best CUDA, PyTorch, and xformers versions for Stable Diffusion, suggesting skipping xformers until it updates and using sd-webui-forge-classic or Automatic1111.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * xformers really wants the previous version of torch, and should be skipped till it updates.
    * sd-webui-forge-classic is pretty well updated.
    * Xformers has some problems working with cuda 12.8 & higher than torch 2.7.0.

**[Need help! Training LoRA blurry, and deformed face/body (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1lofyeo/need_help_training_lora_blurry_and_deformed/)**
*  **Summary:** A user needs help with blurry and deformed faces/bodies while training LoRA. Suggestions include training locally, using mirrored images, and using a Flux model.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Train locally using diffusion-pipe or comfyui.
    * Avoid using mirrored images
    * Try using Flux if you want realism or any of the better photorealistic models.

**[Kontext Hyper-realism (Score: 0)](https://i.redd.it/ip84f29cq3af1.gif)**
*  **Summary:** The discussion is about hyper-realism using Kontext, with comments on the model's tendency to increase head sizes and potential model collapse.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * The model increases head sizes.
    * So this is consecutive editing on top of editing
    * The model could be facing model collapse

**[How long does it exactly take to download Stable Diffusion?? It's been 4 hours. (Score: 0)](https://www.reddit.com/gallery/1lodcc6)**
*  **Summary:** A user asks how long it takes to download Stable Diffusion, with responses suggesting something might be wrong and recommending alternative downloads like ComfyUI.
*  **Emotion:** Neutral
*  **Top 3 Points of View:**
    * Something is wrong and everything should be deleted and tried again.
    * It's a strange question since Stable Diffusion is not a program and there's no way to know where exactly you're downloading A1111 from and what files are those.
    * Download ComfyUI portable build from this page: [https://github.com/comfyanonymous/ComfyUI/releases](https://github.com/comfyanonymous/ComfyUI/releases)

**[Please, provide instructions on how to use Runpod Comfyui (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1loczge/please_provide_instructions_on_how_to_use_runpod/)**
*  **Summary:** A user requests instructions on how to use Runpod Comfyui, and is advised to watch ryanontheinside video.
*  **Emotion:** Neutral
*  **Top 1 Point of View:**
    * Look up the video of ryanontheinside

**[How do you specify characters in a prompt? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1lodqdm/how_do_you_specify_characters_in_a_prompt/)**
*  **Summary:** This thread is about specifying characters in a prompt, with suggestions including regional prompting, emphasis, and using Flux models.
*  **Emotion:** Neutral, with some negative sentiments.
*  **Top 3 Points of View:**
    * Regional prompting is what you need
    * Matters on the model you use.
    * For Flux, you can do this to some extent by being very explicit in your prompt.

**[How to shard a model? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1loeadq/how_to_shard_a_model/)**
*  **Summary:** A user asks how to shard a model, and gets pointed to a script for converting Flux to diffusers format.
*  **Emotion:** Neutral
*  **Top 1 Point of View:**
    * There is a script at this link:
[https://github.com/huggingface/diffusers/blob/main/scripts/convert\_flux\_to\_diffusers.py](https://github.com/huggingface/diffusers/blob/main/scripts/convert_flux_to_diffusers.py)

**[apply FLUX KONTEXT on a video? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1lofo55/apply_flux_kontext_on_a_video/)**
*  **Summary:** This thread discusses applying FLUX KONTEXT on a video, with a user having issues with batch processing and suggestions to avoid changing each frame with latent noise.
*  **Emotion:** Negative
*  **Top 2 Points of View:**
    * The user is having issues applying FLUX KONTEXT on a video.
    * Trying to change each frame with latent noise is a terrible ideia

**[Can someone ELI5 how to do inpainting with Flux on ComfyUI? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1loft2k/can_someone_eli5_how_to_do_inpainting_with_flux/)**
*  **Summary:** A user requests a simple explanation on how to do inpainting with Flux on ComfyUI, and gets a link to a tutorial.
*  **Emotion:** Neutral
*  **Top 1 Point of View:**
    * This tutorial could help the user:
[https://comfyui-wiki.com/en/tutorial/advanced/flux-fill-workflow-step-by-step-guide](https://comfyui-wiki.com/en/tutorial/advanced/flux-fill-workflow-step-by-step-guide)
