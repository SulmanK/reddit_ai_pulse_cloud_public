---
title: "Stable Diffusion Subreddit"
date: "2026-02-25"
description: "Analysis of top discussions and trends in the stablediffusion subreddit"
tags: ["Stable Diffusion", "AI Models", "Creative AI"]
---

# Overall Ranking and Top Discussions
1.  [Latent Library v1.0.2 Released (formerly AI Toolbox)](https://i.redd.it/vl5w7g5avnlg1.png) (Score: 85)
    *   Thanks to the OP for creating this, certainly a lot of people could use this tool. -EDITED- I'm assuming this runs entirely locally? Would you consider adding a feature to include custom "metadata" in the form of a comment or note? Nano banana doesn't include metadata with the prompt. It would be great to have everything in one place and not rely on Google Sheets.
2.  [Qwen 3.5 FP8 weights are now open](https://huggingface.co/collections/Qwen/qwen35) (Score: 41)
    *   Thats a big checkpoint! Great that they open them up though even if you need a rack of datacenter GPU's to run it properly. My goodness.
3.  [Z-Image Base/Turbo and/or Klein 9B - Character Lora Training... Im so exhausted](https://www.reddit.com/r/StableDiffusion/comments/1reooh8/zimage_baseturbo_andor_klein_9b_character_lora/) (Score: 7)
    *   Honestly i think LoRAs as a training method are totaly obsolete... Nanobanana uses references with no training and produced amazing consistency in one hand and total flexibility in the other. Loras simply cant do that, escpecially if characters deviate from mainstream archetypes the models were trained on. ZIT/ZIB retain 80% of face and body consistency.
4.  [Try-On, Klein 4B, No LoRA (Odd Poses, Impressive)](https://i.redd.it/7ufjwgei9plg1.gif) (Score: 7)
    *   https://preview.redd.it/jddfoc1s9plg1.jpeg?width=3200&format=pjpg&auto=webp&s=0f105b34b60dc3265acab2c12d8f58b112dede8a All images in a big image.
5.  [AI is an Awesome Hobby](https://i.redd.it/pvd29r5ozolg1.png) (Score: 5)
    *   Except that a lot of people here want to use it to scam people with their ai influencers. Real influencers are a big enough problem already, we don't need more fake ones. Ai still impacts cost to others.
6.  [Unpopular opinion: 90% of AI music videos still look like creepy puppets. What’s the ACTUAL 2026 workflow for flawless lip-syncing?](https://www.reddit.com/r/StableDiffusion/comments/1relpdj/unpopular_opinion_90_of_ai_music_videos_still/) (Score: 3)
    *   Maybe your best shot would be recording someone singing the lyrics and do some motion v2v process It will be a while before v2v technology gets very good.
7.  [Help with Wan2GP custom model install.](https://www.reddit.com/r/StableDiffusion/comments/1relh2f/help_with_wan2gp_custom_model_install/) (Score: 2)
    *   Did you read [this](https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/FINETUNES.md) and attempt to follow it? Can you post your json on pastebin and share a link?
8.  [Best model to make logos / icons?](https://www.reddit.com/r/StableDiffusion/comments/1reh2zf/best_model_to_make_logos_icons/) (Score: 1)
    *   All local is quite bad with them. U can try recraft or train lora you can try something like [logodiffusion.com](http://logodiffusion.com) or just use chat gpt, it can do good results if you know how to prompt, the only issue is that it offers no variety so if someone else prompted something similar, they'll most probably get 90% similar logo to yours.
9.  [Help needed with Forge UI](https://www.reddit.com/r/StableDiffusion/comments/1rekmak/help_needed_with_forge_ui/) (Score: 1)
    *   My guess is that you're trying to use https://localhost:.... to load the UI -- just use http: .
10. [Question about current state of character consistency](https://www.reddit.com/r/StableDiffusion/comments/1relfno/question_about_current_state_of_character/) (Score: 1)
    *   Are you going for photorealistic or anime / illustrated characters?
11. [Z-Image Turbo character LoRA ruining face detail and mole](https://www.reddit.com/r/StableDiffusion/comments/1rel2ry/zimage_turbo_character_lora_ruining_face_detail/) (Score: 0)
    *   Does any prompt you use to bring about your character talk about the mole and placement of the mole? From playing around a lot on ZiT even on some image to image items, helping explain what details need to show up on the end product and where tend to help ZiT put things back in the right spot. Have you tried describing it in the text part of your dataset?
12. [Is training a model of person still worth it or use a service instead?](https://www.reddit.com/r/StableDiffusion/comments/1regjei/is_training_a_model_of_person_still_worth_it_or/) (Score: 0)
    *   I've started training Flux loras maybe a month ago (job/studies/personal life in the way of truly commiting to learning the ropes) and for the 3 I've done, it seems to be worth it. Inherent FluxD issues aside, the likes are uncanny, you literally can't tell it's a generated image if your workflow and prompts are good enough. You can train your own LORA or finetune SD models at home or with colab hardware, all you need is maybe 20-100 high quality images (i've had success with as few as six).
13. [AI Cinematic Series - Story System](https://www.reddit.com/r/StableDiffusion/comments/1rely4h/ai_cinematic_series_story_system/) (Score: 0)
    *   Why “ChatGPT → eBook” Is a Spam, Not a Book
14. [Ai Model Anime Help](https://www.reddit.com/gallery/1rejhor) (Score: 0)
    *   Seedream It's probably a cloud one like nano banana pro.
15. [🥰AI🥰](https://i.redd.it/yi9bttpa3plg1.jpeg) (Score: 0)
    *   Another anti-technology lunatic? I don't think you know what stable diffusion is
16. [I made my very first ai short film!](https://www.reddit.com/r/StableDiffusion/comments/1rei4zp/i_made_my_very_first_ai_short_film/) (Score: 0)
    *   Wow man Epic!! The cinematography is simply awesome. As you said thr script and direction was a bit all over the place but I totally get what your intention and what the story is.

# Detailed Analysis by Thread
**[Latent Library v1.0.2 Released (formerly AI Toolbox) (Score: 85)](https://i.redd.it/vl5w7g5avnlg1.png)**
*   **Summary:** Thanks to the OP for creating this, certainly a lot of people could use this tool. -EDITED- I'm assuming this runs entirely locally? Would you consider adding a feature to include custom "metadata" in the form of a comment or note? Nano banana doesn't include metadata with the prompt. It would be great to have everything in one place and not rely on Google Sheets. Ill check this out. Sounds exactly like something ive needed keeps getting better - metadata-ai-toolbox-latent-viewer! best of the bunch. thank you Does this support things like filtering a library of images/videos to show just those that used a certain LoRA? What is it? Downloading.... This code base actually has tests in it. The UI looks vibe coded. Use the frontend skill from Anthropic. macos yay! heads up: to get it up you need to recursively clear quarantine on the entire bundle: sudo xattr -cr "/Applications/Latent Library.app" If the app is still in your Downloads or wherever you mounted it from, adjust the path accordingly. After running that, try opening it normally. Does it do image to image compare? Even when zoomed in?
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.70) with mentions of 4 Positive.
*   **Top 3 Points of View:**
    *   Users appreciate the new Latent Library (formerly AI Toolbox) as a useful tool for managing Stable Diffusion assets, with many expressing excitement to try it.
    *   There are requests for new features, such as custom metadata/notes for prompts and filtering capabilities (e.g., by LoRA).
    *   Technical questions arise regarding local operation, image comparison, and specific installation steps for macOS, along with some feedback on UI design.
**[Qwen 3.5 FP8 weights are now open (Score: 41)](https://huggingface.co/collections/Qwen/qwen35)**
*   **Summary:** Thats a big checkpoint! Great that they open them up though even if you need a rack of datacenter GPU's to run it properly. My goodness. >397B Hm, will this run on my android phone? Which one generates images? wow just tested it for a bit in chat qwen website. actually pretty good. it knows more about comfyui nodes than other llm's i feel like
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.68) with mentions of 2 Positive.
*   **Top 3 Points of View:**
    *   Users are impressed and surprised by the large size of the Qwen 3.5 FP8 weights but appreciative of their open release.
    *   There's curiosity about the practical requirements to run such a large model (e.g., GPU needs) and its specific functionalities, especially for image generation.
    *   Initial tests indicate positive performance, with one user noting its strong knowledge of ComfyUI nodes.
**[Z-Image Base/Turbo and/or Klein 9B - Character Lora Training... Im so exhausted (Score: 7)](https://www.reddit.com/r/StableDiffusion/comments/1reooh8/zimage_baseturbo_andor_klein_9b_character_lora/)**
*   **Summary:** Honestly i think LoRAs as a training method are totaly obsolete... Nanobanana uses references with no training and produced amazing consistency in one hand and total flexibility in the other. Loras simply cant do that, escpecially if characters deviate from mainstream archetypes the models were trained on. ZIT/ZIB retain 80% of face and body consistency. For full consistency you need to use multiple model pipeline and inpainting. LTX studio has a feature to keep characters consistent. The classic two loras together wombo combo has surprisingly good results for me. I'm not saying this to be mean, but imagine if you had purchased an entry level 16GB card to learn on instead of renting Runpods. Both my character trained in ZIB or Klein came out great. I do more repetitions on the dataset with better quality. Try a larger dataset if you can. And 6k steps. Musabi trainer project is available in GitHub. It is automatically deployed to dockerhub as container. It will train a LoRA against Z-image base 9B model. I have one data set with 247 pics for a character and with my config I am getting max similarity and resemblance in ZIB and ZIT Same brother, stuck in the exact same situation as you.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.69) with mentions of 2 Positive.
*   **Top 3 Points of View:**
    *   There's debate about the effectiveness of LoRAs for character consistency, with some suggesting they are obsolete compared to reference-based methods like Nanobanana or multi-model pipelines.
    *   Several users offer practical advice for improving LoRA training: using larger datasets (e.g., 247-300+ images), higher step counts (6k), better captioning, and experimenting with resolutions and combined LoRAs.
    *   Concerns are raised about the cost of training (renting Runpods) versus investing in hardware, and an alternative training project (Musabi trainer) is suggested.
**[Try-On, Klein 4B, No LoRA (Odd Poses, Impressive) (Score: 7)](https://i.redd.it/7ufjwgei9plg1.gif)**
*   **Summary:** https://preview.redd.it/jddfoc1s9plg1.jpeg?width=3200&format=pjpg&auto=webp&s=0f105b34b60dc3265acab2c12d8f58b112dede8a All images in a big image.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.96).
*   **Top 3 Points of View:**
    *   The post is primarily a showcase of the Klein 4B model's capabilities for 'try-on' images without LoRA, highlighting its impressive performance with odd poses.
    *   A user provides a link to an aggregate image of all examples.
**[AI is an Awesome Hobby (Score: 5)](https://i.redd.it/pvd29r5ozolg1.png)**
*   **Summary:** Except that a lot of people here want to use it to scam people with their ai influencers. Real influencers are a big enough problem already, we don't need more fake ones. Ai still impacts cost to others. The only problem with it being a hobby is that duke energy can use it as an excuse to raise prices by 150% to every household. True hobbies wouldn’t negatively impact anyone True, but still my parents want me out of the house each day and my therapist wants me to find a friend who isn't online. https://www.reddit.com/r/StableDiffusion/comments/1rensp2/ai/?utm_source=share&utm_medium=mweb3x&utm_name=mweb3xcss&utm_term=1&utm_content=share_button
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.71).
*   **Top 3 Points of View:**
    *   AI as a hobby is seen positively by the original poster, but others raise concerns about its societal impacts, such as the potential for AI influencers to scam people.
    *   Another viewpoint highlights potential negative economic impacts, like AI driving up energy costs.
    *   Some comments reflect personal challenges related to the hobby, such as social isolation.
**[Unpopular opinion: 90% of AI music videos still look like creepy puppets. What’s the ACTUAL 2026 workflow for flawless lip-syncing? (Score: 3)](https://www.reddit.com/r/StableDiffusion/comments/1relpdj/unpopular_opinion_90_of_ai_music_videos_still/)**
*   **Summary:** Maybe your best shot would be recording someone singing the lyrics and do some motion v2v process It will be a while before v2v technology gets very good. kijai/ComfyUI-LivePortraitKJ or similar might be what you want. You’d need someone perform the song in the correct way, then use the reference video to drive liveportrait to generate the reference data for face animation to control the face of your character frame by frame. A lot of work. But gets you what you want. Probably. better load up on allergy meds cuz, ai videos are far from perfect. The AI tends to smooth out a character's face when animating the mouth and jaw. LTX-2 is the best tool for this type of content. Here is an example of a music video that was rendered at 1080p on a meager RTX 3080 (10 GB VRAM) with 32GB system memory. The keyframes were done on Nano Banana Pro People been making music videos without showing a singer for generations.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.69) with mentions of 2 Positive.
*   **Top 3 Points of View:**
    *   Many agree that current AI lip-syncing for music videos is still imperfect and can result in 'creepy puppet' visuals.
    *   Suggested workflows for better lip-syncing involve video-to-video (v2v) processes, using reference videos for face animation with tools like ComfyUI-LivePortraitKJ, or utilizing specialized tools like LTX-2.
    *   There are observations that AI models tend to smooth out facial details when animating, and a reminder that music videos don't always require a visible, singing character.
**[Help with Wan2GP custom model install. (Score: 2)](https://www.reddit.com/r/StableDiffusion/comments/1relh2f/help_with_wan2gp_custom_model_install/)**
*   **Summary:** Did you read [this](https://github.com/deepbeepmeep/Wan2GP/blob/main/docs/FINETUNES.md) and attempt to follow it? Can you post your json on pastebin and share a link?
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.62).
*   **Top 3 Points of View:**
    *   A user offers assistance by asking if the official documentation was consulted and requests the JSON configuration to help debug the installation issue.
**[Best model to make logos / icons? (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1reh2zf/best_model_to_make_logos_icons/)**
*   **Summary:** All local is quite bad with them. U can try recraft or train lora you can try something like [logodiffusion.com](http://logodiffusion.com) or just use chat gpt, it can do good results if you know how to prompt, the only issue is that it offers no variety so if someone else prompted something similar, they'll most probably get 90% similar logo to yours. It's not really possible to generate good ones that are production ready. Ideogram Technically the best. They specialize in logos and graphics. Available as an API node in Comfy. Not free however. The closest to professional logo / icons is Flux.2 Dev. Qwen Image May be this https://github.com/Nutlope/logocreator You need model with strong text rendering capabilities. So Qwen Image.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.77) with mentions of 1 Negative.
*   **Top 3 Points of View:**
    *   General consensus is that local models are currently poor for production-ready logos, suggesting specialized platforms like Ideogram, logodiffusion.com, or specific models like Flux.2 Dev or Qwen Image for text rendering.
    *   Some mention training LoRAs as an alternative for local generation.
    *   ChatGPT is suggested as a tool for logo generation, with a caveat about lack of variety.
**[Help needed with Forge UI (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1rekmak/help_needed_with_forge_ui/)**
*   **Summary:** My guess is that you're trying to use https://localhost:.... to load the UI -- just use http: .
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.81).
*   **Top 3 Points of View:**
    *   A user suggests a common troubleshooting step: ensure `http:` is used instead of `https:` when loading the UI.
**[Question about current state of character consistency (Score: 1)](https://www.reddit.com/r/StableDiffusion/comments/1relfno/question_about_current_state_of_character/)**
*   **Summary:** Are you going for photorealistic or anime / illustrated characters?
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.58).
*   **Top 3 Points of View:**
    *   A clarifying question is posed: whether the user is aiming for photorealistic or anime/illustrated characters, as this affects consistency strategies.
**[Z-Image Turbo character LoRA ruining face detail and mole (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1rel2ry/zimage_turbo_character_lora_ruining_face_detail/)**
*   **Summary:** Does any prompt you use to bring about your character talk about the mole and placement of the mole? From playing around a lot on ZiT even on some image to image items, helping explain what details need to show up on the end product and where tend to help ZiT put things back in the right spot. Have you tried describing it in the text part of your dataset? For example, "a photograph of a woman with a mole on the right side of her neck."
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.57).
*   **Top 3 Points of View:**
    *   Users suggest refining prompts to explicitly describe specific details like moles and their placement to help the model retain them.
    *   Another tip is to include such detailed descriptions in the text part of the dataset used for training.
**[Is training a model of person still worth it or use a service instead? (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1regjei/is_training_a_model_of_person_still_worth_it_or/)**
*   **Summary:** I've started training Flux loras maybe a month ago (job/studies/personal life in the way of truly commiting to learning the ropes) and for the 3 I've done, it seems to be worth it. Inherent FluxD issues aside, the likes are uncanny, you literally can't tell it's a generated image if your workflow and prompts are good enough. I've trained all three on a set of about 30 images, and the best LoRA is for the person that had the best mix of poses, perspectives, clothes, expressions. You can train your own LORA or finetune SD models at home or with colab hardware, all you need is maybe 20-100 high quality images (i've had success with as few as six). Posing a person is a separate challenge, and there are solutions to that too. Have you tried WAN? Training a model of a person can make it harder to create images of that person with someone else. I feel like all the answers are missing the point. I doesn't matter if you use a service, train a model or use some edit model yourself. None of the three will inherently know how the person looks from an angle that was never presented to them. So use the method that's the cheapest and fastest and generate as many images as you need until you hit the lottery.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.67) with mentions of 1 Positive.
*   **Top 3 Points of View:**
    *   Training personal LoRAs (e.g., with Flux) is considered worthwhile by some, yielding uncanny resemblance with good workflows and prompts, even with small datasets.
    *   Others emphasize that the method (service vs. self-training) is less important than iteratively generating images until satisfactory results are achieved, as no method inherently knows all angles of a person.
    *   A point is made that training a model of a specific person might make it harder to create images of that person with others.
**[AI Cinematic Series - Story System (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1rely4h/ai_cinematic_series_story_system/)**
*   **Summary:** Why “ChatGPT → eBook” Is a Spam, Not a Book
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.74).
*   **Top 3 Points of View:**
    *   The only comment expresses skepticism about AI-generated content quality, specifically comparing 'ChatGPT → eBook' to spam rather than a genuine book.
**[Ai Model Anime Help (Score: 0)](https://www.reddit.com/gallery/1rejhor)**
*   **Summary:** Seedream It's probably a cloud one like nano banana pro. Aren’t they actual manhwa that’s being made into videos?
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.78).
*   **Top 3 Points of View:**
    *   Suggestions for AI anime models include 'Seedream' and 'nano banana pro' (a cloud-based model).
    *   A question is raised whether the examples might be actual manhwa converted to videos rather than AI-generated.
**[🥰AI🥰 (Score: 0)](https://i.redd.it/yi9bttpa3plg1.jpeg)**
*   **Summary:** Another anti-technology lunatic? I don't think you know what stable diffusion is I didn't think the cringe level of the original post could be topped. Congratulations, you have exceeded my expectations.
*   **Emotion:** The overall tone is predominantly Neutral (average score: 0.62) with mentions of 1 Positive.
*   **Top 3 Points of View:**
    *   Comments express criticism and sarcasm towards the original post, with users questioning the poster's understanding of Stable Diffusion.
    *   One comment praises the ability to top the 'cringe level' of the original post, indicating negative sentiment towards the post itself.
    *   Another comment labels the poster as an 'anti-technology lunatic', suggesting a dismissive attitude towards the post's implied message.
**[I made my very first ai short film! (Score: 0)](https://www.reddit.com/r/StableDiffusion/comments/1rei4zp/i_made_my_very_first_ai_short_film/)**
*   **Summary:** Wow man Epic!! The cinematography is simply awesome. As you said thr script and direction was a bit all over the place but I totally get what your intention and what the story is. It's a PTSD war veteran drowning his sorrow in booze and in a some bizarre manic flashback climbs into a bath, clothed, which further fuels his flashbacks of being at war out at sea. But I dont get the conclusion, it wasn't him that crashed? Maybe a friend? And the damage he sees on the can after the flashback is a hallucination basically? Anyway I really dig it and can see the time and and effort this took. Did you do the sound design and mix aswell?
*   **Emotion:** The overall tone is predominantly Positive (average score: 0.83).
*   **Top 3 Points of View:**
    *   Users highly praise the cinematography of the AI short film, calling it 'epic' and 'awesome'.
    *   There's feedback on the narrative, noting the script and direction were 'a bit all over the place' but understanding the intended story (PTSD war veteran flashbacks).
    *   Questions arise about specific plot points (e.g., the conclusion, the crash, hallucinations) and the sound design.
