---
title: "Stable Diffusion Subreddit"
date: "2025-02-06"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["stablediffusion", "AI", "image generation"]
---

# Overall Ranking and Top Discussions
1.  [[D] Consistent face 3x3 generator with FLUX (wf in first comment)](https://www.reddit.com/gallery/1ij7pqb) (Score: 71)
    * Discusses a workflow for generating a 3x3 grid of images with consistent character faces using the FLUX.1 depth LoRA.
2.  [Flux LoRa look great; SD LoRa do not. Is this normal?](https://www.reddit.com/r/StableDiffusion/comments/1ij9kgz/flux_lora_look_great_sd_lora_do_not_is_this/) (Score: 3)
    * A user asks why Flux LoRAs seem to work better than SD LoRAs, and seeks advice on improving SD LoRA results.
3.  [Does OC'ing your GPU make significant benefit?](https://www.reddit.com/r/StableDiffusion/comments/1ij8evj/does_ocing_your_gpu_make_significant_benefit/) (Score: 2)
    *  Asks about the benefits of overclocking a GPU for stable diffusion.
4.  [Issues with inpainting (fade between new and original)](https://www.reddit.com/r/StableDiffusion/comments/1ijadh2/issues_with_inpainting_fade_between_new_and/) (Score: 2)
    *  Seeks solutions for a fading issue encountered while inpainting images.
5.  [how to remove noise after separating frequency](https://www.reddit.com/r/StableDiffusion/comments/1ijbcp3/how_to_remove_noise_after_separating_frequency/) (Score: 2)
    *  Asks for advice on removing noise after separating image frequencies.
6.  [Has anyone tried a negative lora in hunyuan yet?](https://www.reddit.com/r/StableDiffusion/comments/1ijc44l/has_anyone_tried_a_negative_lora_in_hunyuan_yet/) (Score: 2)
    *  Queries whether anyone has experimented with negative LoRAs in Hunyuan.
7.  [AMD users, has anyone figured out how to have Hip SDK Zluda, alongside the latest gaming drivers?](https://www.reddit.com/r/StableDiffusion/comments/1ij8n5p/amd_users_has_anyone_figured_out_how_to_have_hip/) (Score: 1)
    *  Asks about configuring Hip SDK Zluda with the latest gaming drivers on AMD GPUs.
8.  [Anyone aware of this  illustrious OpenPose model? Does  it work?](https://www.reddit.com/r/StableDiffusion/comments/1ij946z/anyone_aware_of_this_illustrious_openpose_model/) (Score: 1)
    *  Asks about the knowledge of OpenPose model.
9.  [Please Help me fix this error: cannot import name 'BERT_PRETRAINED_MODEL_ARCHIVE_MAP' from 'custom_mesh_graphormer.modeling.bert.modeling_bert](https://www.reddit.com/r/StableDiffusion/comments/1ij94cu/please_help_me_fix_this_error_cannot_import_name/) (Score: 1)
    *  Asks for help in resolving an import error related to BERT models.
10. [Need help making art](https://www.reddit.com/r/StableDiffusion/comments/1ij9ga1/need_help_making_art/) (Score: 1)
    *  User seeks guidance on creating art using stable diffusion.
11. [Fantasy gangsters](https://www.reddit.com/r/StableDiffusion/comments/1ijajqs/fantasy_gangsters/) (Score: 1)
    *  A user is looking for advice on generating fantasy-themed gangster images.
12. [Q on control nets](https://www.reddit.com/r/StableDiffusion/comments/1ijbvru/q_on_control_nets/) (Score: 1)
    *  A user seeks assistance with ControlNets.
13. [Massive swap on SSD with Flux](https://www.reddit.com/r/StableDiffusion/comments/1ijd72e/massive_swap_on_ssd_with_flux/) (Score: 1)
    *  Reports a problem with excessive SSD usage when using Flux.
14. [I wonder we dont need designers anymore, AI can create epic outfits randomly.](https://www.reddit.com/gallery/1ij9ztt) (Score: 0)
    * Wonders whether AI will replace designers.

# Detailed Analysis by Thread
**[Consistent face 3x3 generator with FLUX (wf in first comment) (Score: 71)](https://www.reddit.com/gallery/1ij7pqb)**
*  **Summary:** This post shares a workflow for generating a 3x3 grid of images with consistent character faces using the FLUX.1 depth LoRA. The author provides links to the workflow on CivitAI and Patreon, along with instructions on how to use it. They also suggest using specific upscaling models and LoRAs to avoid issues like the "Flux chin."
*  **Emotion:** The overall emotional tone of the thread is neutral, with a high sentiment score.
*  **Top 3 Points of View:**
    * The provided workflow allows for generating a 3x3 grid with the same character face in 9 different poses and with small expression differences
    * Suggests using the 8xNMKDFaces160000G\_v10.pt upscaling model.
    * Recommends using additional LoRAs to enhance skin details and refine faces from previous character LoRAs.

**[Flux LoRa look great; SD LoRa do not. Is this normal? (Score: 3)](https://www.reddit.com/r/StableDiffusion/comments/1ij9kgz/flux_lora_look_great_sd_lora_do_not_is_this/)**
*  **Summary:** A user is experiencing better results with Flux LoRAs compared to SD LoRAs and asks if this is a common experience. Other users offer potential solutions and explanations, such as the choice of models, tagging, and training settings.
*  **Emotion:** The overall emotional tone of the thread is neutral, with a slight positive sentiment.
*  **Top 3 Points of View:**
    * Flux is absolutely perfect for the most part.
    * Pony base are difficult to work with and even more if you are trying to do realism with it.
    * Kohya is harder to understand, but it's normally better than toolkit and more up to date.

**[Does OC'ing your GPU make significant benefit? (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1ij8evj/does_ocing_your_gpu_make_significant_benefit/)**
*  **Summary:** The post asks whether overclocking a GPU significantly improves performance in stable diffusion. Commenters suggest that overclocking is often a waste of energy and that power limiting the GPU can provide similar performance with lower power consumption and heat.
*  **Emotion:** The overall emotional tone of the thread is neutral to positive.
*  **Top 3 Points of View:**
    * Overclocking is pretty much a waste of energy for image generation workloads.
    * Lowering the GPU's max power to 80% of normal can result in only a 1-3% performance loss.
    * Power limiting the GPU to 70% can reduce heat and electricity usage while maintaining around 95% of original generation speed.

**[Issues with inpainting (fade between new and original) (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1ijadh2/issues_with_inpainting_fade_between_new_and/)**
*  **Summary:** A user is experiencing a fading issue when inpainting images and seeks advice on how to resolve it. Commenters suggest enabling "soft inpainting," lowering the denoising strength, and considering the use of a dedicated inpainting model like Flux Fill.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * Enabling the "soft inpainting" option can help the inpainted area blend better with the surrounding image.
    * Lowering the denoising strength can prevent the prompt from being generated from scratch.
    * Flux has a dedicated inpainting model called Flux Fill.

**[how to remove noise after separating frequency (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1ijbcp3/how_to_remove_noise_after_separating_frequency/)**
*  **Summary:** The post requests advice on removing noise from an image after frequency separation. The commenter suggests that the noise is likely in the high frequency layer and can be removed manually using a light blur brush or by separating the frequency layers into finer bands.
*  **Emotion:** The overall emotional tone is positive.
*  **Top 3 Points of View:**
    * The noise is probably in the high frequency.
    * You can remove it manually by saving the freq layer and using a light blur brush over the face, avoiding the eyes.
    * An even better way would be to use an image editor and separate the freq layers into even finer bands and do the same thing to the layer that has the noise before recombining the layers.

**[Has anyone tried a negative lora in hunyuan yet? (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1ijc44l/has_anyone_tried_a_negative_lora_in_hunyuan_yet/)**
*  **Summary:** The post simply asks if anyone has tried a negative LoRA in Hunyuan.
*  **Emotion:** The overall emotional tone is negative.
*  **Top 3 Points of View:**
    * Nope

**[AMD users, has anyone figured out how to have Hip SDK Zluda, alongside the latest gaming drivers? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ij8n5p/amd_users_has_anyone_figured_out_how_to_have_hip/)**
*  **Summary:** The post asks about the configuration of Hip SDK Zluda alongside the latest gaming drivers for AMD users.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * You dont need pro driver, just hip.
    * The last time I tried Zluda it did not require any special drivers.
    * So what you telling me is. You checked HIP and installed other junk from the installer?

**[Anyone aware of this  illustrious OpenPose model? Does  it work? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ij946z/anyone_aware_of_this_illustrious_openpose_model/)**
*  **Summary:** The post ask about OpenPose model.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * [removed]

**[Please Help me fix this error: cannot import name 'BERT_PRETRAINED_MODEL_ARCHIVE_MAP' from 'custom_mesh_graphormer.modeling.bert.modeling_bert (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ij94cu/please_help_me_fix_this_error_cannot_import_name/)**
*  **Summary:** The post reports an import error and seeks a solution. A commenter provides a link to a relevant GitHub issue.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * No viewpoints expressed other than pointing to a GitHub issue for a potential solution.

**[Need help making art (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ij9ga1/need_help_making_art/)**
*  **Summary:** A user requests assistance with making art, and a commenter suggests ForgeUI.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * ForgeUI is an easy UI to start with if you have a good enough pc to run locally.

**[Fantasy gangsters (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ijajqs/fantasy_gangsters/)**
*  **Summary:** The post is about generating images of fantasy gangsters.
*  **Emotion:** The overall emotional tone of the thread is negative.
*  **Top 3 Points of View:**
    * Some models aren't good for fantasy, try with loras, or, if not, do inpaint using fantasy models.

**[Q on control nets (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ijbvru/q_on_control_nets/)**
*  **Summary:** The post seek help with ControlNets.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * Tons of YouTube channels have a step-by-step processes to install control for SDXL it’s very easy.

**[Massive swap on SSD with Flux (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1ijd72e/massive_swap_on_ssd_with_flux/)**
*  **Summary:** The post report a problem with excessive SSD usage when using Flux.
*  **Emotion:** The overall emotional tone of the thread is negative.
*  **Top 3 Points of View:**
    * Absolutely not normal. You're losing 150GB of storage space when you queue a generation?

**[I wonder we dont need designers anymore, AI can create epic outfits randomly. (Score: 0)](https://www.reddit.com/gallery/1ij9ztt)**
*  **Summary:** The post poses a question about whether AI will replace designers.
*  **Emotion:** The overall emotional tone of the thread is neutral.
*  **Top 3 Points of View:**
    * Can AI turn that into a sewing pattern?
    * One of the designer job is to convince that their work is good.
    * No. Designers will likely still exist but they will use AI in their tool chains.
