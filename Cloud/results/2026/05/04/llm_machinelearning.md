json
{
  "metadata": {
    "subreddit_name": "machinelearning",
    "date": "2026-05-04",
    "description": "Analysis of top discussions and trends in the machinelearning subreddit",
    "tags": ["AI", "ML", "Research", "Technology"]
  },
  "threads": [
    {
      "post_id": "1t311vb",
      "subreddit": "machinelearning",
      "post_score": 134,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t311vb/are_modern_ml_phds_becoming_too_incremental_or_is/",
      "post_content": "Are modern ML PhDs becoming too incremental, or is this just what research looks like now? [D]",
      "comments": [
        {
          "comment_id": "ojs1u21",
          "summary_date": "2026-05-04",
          "comment_summary": "It's pretty much standard for a PhD to be essentially zero risk and millimetrically incremental. Sadly.",
          "sentiment_score": 0.8565999865531921,
          "sentiment_label": "Negative"
        },
        {
          "comment_id": "ojsxn19",
          "summary_date": "2026-05-04",
          "comment_summary": "Linus Torvalds once said \"Many eyes make bugs shallow\". It is the same with PhD research, especially in a hyper-competitive field like ML. Almost every new idea has already crossed someone's mind. It's an issue of who is faster at staking a claim",
          "sentiment_score": 0.851431131362915,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojrv4jd",
          "summary_date": "2026-05-03",
          "comment_summary": "In every field the strength of a PhD student's scientific ability will vary. Some ML PhDs achieve substantial and significant contributions to the field, while others coast on the work of their lab mates and peers and scrape by. Your PhD is an opportunity to do the best science you can do",
          "sentiment_score": 0.7012442946434021,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojtdfuh",
          "summary_date": "2026-05-04",
          "comment_summary": "Everyone is more of a research engineer than a researcher today. This is probably due to the highly competitive environment.",
          "sentiment_score": 0.6948620676994324,
          "sentiment_label": "Positive"
        },
        {
          "comment_id": "ojruefc",
          "summary_date": "2026-05-03",
          "comment_summary": "Highly competitive environments favor incrementalism. Are you really going to risk spending several years focusing on a few deep problems, that might potentially go nowhere, while your competition is published continuously?",
          "sentiment_score": 0.6579311490058899,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojrz3kq",
          "summary_date": "2026-05-04",
          "comment_summary": "It’s always been incremental.",
          "sentiment_score": 0.657265841960907,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojt7xs6",
          "summary_date": "2026-05-04",
          "comment_summary": "ML PhDs will become lower quality because people will start cutting corners by using AI to propose research ideas.",
          "sentiment_score": 0.6417762637138367,
          "sentiment_label": "Positive"
        },
        {
          "comment_id": "ojtenod",
          "summary_date": "2026-05-04",
          "comment_summary": "Have you looked around at what PhD's in other fields are like? This is just what a PhD is.\n\nRelevant: https://matt.might.net/articles/phd-school-in-pictures/",
          "sentiment_score": 0.5877614617347717,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojrwql9",
          "summary_date": "2026-05-03",
          "comment_summary": "What are you talking about, PhD Research has always been incremental (https://matt.might.net/articles/phd-school-in-pictures/).\nNothing wrong with that.",
          "sentiment_score": 0.5747389197349548,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "oju3xkk",
          "summary_date": "2026-05-04",
          "comment_summary": "A paper got rejected by the AC even though it had top 10% scores. ACs are becoming more junior overtime.",
          "sentiment_score": 0.4552744925022125,
          "sentiment_label": "Negative"
        }
      ]
    },
    {
      "post_id": "1t3hxsy",
      "subreddit": "machinelearning",
      "post_score": 21,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t3hxsy/why_ssms_struggle_in_parameterconstrained/",
      "post_content": "Why SSMs struggle in parameter-constrained training: empirical findings at 25M parameters [R]",
      "comments": [
        {
          "comment_id": "ojx0j2a",
          "summary_date": "2026-05-04",
          "comment_summary": "There is a 3.26x gap between SSM in_proj and attention QKV on compressibility and SP4096 to SP8192 sign flip. The fix is upstream: train with a regularizer that nudges weights toward compressible distributions.",
          "sentiment_score": 0.9160686135292053,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojwbh0j",
          "summary_date": "2026-05-04",
          "comment_summary": "I personally find these negative results some of the most interesting.\nI also maybe biased as they read less like the usual AI hype nonsense.",
          "sentiment_score": 0.37012794613838196,
          "sentiment_label": "Positive"
        },
        {
          "comment_id": "ojv52p9",
          "summary_date": "2026-05-04",
          "comment_summary": "interesting how compression becomes the bottleneck here - never thought about LZMA performance on different weight distributions. The SP4096 to SP8192 flip is wild, makes me wonder if there's some sweet spot in sequence length where ssm advantages just evaporate completely.\n\nthat triton kernel stuff sounds like a nightmare to debug, especially the torch.compile quantizer issue.",
          "sentiment_score": 0.28795942664146423,
          "sentiment_label": "Neutral"
        }
      ]
    },
    {
      "post_id": "1t2wybh",
      "subreddit": "machinelearning",
      "post_score": 9,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t2wybh/struggling_with_chebyshev_filter_integration_in/",
      "post_content": "Struggling with Chebyshev Filter Integration in CNN — Any Advice? [R]",
      "comments": [
        {
          "comment_id": "ojrt1um",
          "summary_date": "2026-05-03",
          "comment_summary": "https://ieeexplore.ieee.org/abstract/document/8060555",
          "sentiment_score": 0.9648852348327637,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojr16pm",
          "summary_date": "2026-05-03",
          "comment_summary": "If the signals of interest are in the passband of the filter, then a CNN can conceivably learn the appropriate filter on raw data  to select it as part of its architecture.",
          "sentiment_score": 0.9434193968772888,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojv7ebz",
          "summary_date": "2026-05-04",
          "comment_summary": "i’d first check whether the filter is changing the signal in a way the cnn can’t already learn. if accuracy is basically unchanged across placements, it may be adding structure without adding useful information. try logging feature maps or running a simple ablation on filtered vs unfiltered inputs, otherwise u might just be tuning noise.",
          "sentiment_score": 0.8925529718399048,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojr571m",
          "summary_date": "2026-05-03",
          "comment_summary": "The filter itself is LTI, as are convolutions. The impulse response of a convolution is only as big as the kernel, whereas an IIR filter can have an impulse response that is long/big with far fewer trainable parameters.",
          "sentiment_score": 0.8626588582992554,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojr1326",
          "summary_date": "2026-05-03",
          "comment_summary": "What kind of data are you working with?\n\nIf you work with signals, and audio in particular, check DDSP",
          "sentiment_score": 0.649346113204956,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojr0g77",
          "summary_date": "2026-05-03",
          "comment_summary": "The results of the research are probably not that big of a boost for most research. One thing you could try is running the models on smaller datasets and seeing if the filters help in low data regimes.",
          "sentiment_score": 0.4187032878398895,
          "sentiment_label": "Positive"
        }
      ]
    },
    {
      "post_id": "1t3ogbw",
      "subreddit": "machinelearning",
      "post_score": 2,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t3ogbw/p_qlora_finetuning_of_qwen2515b_for_cefr_english/",
      "post_content": "[P] QLoRA Fine-Tuning of Qwen2.5-1.5B for CEFR English Proficiency Classification (A1–C2) [P]",
      "comments": [
        {
          "comment_id": "ojwrels",
          "summary_date": "2026-05-04",
          "comment_summary": "the model link : [yanou16/cefr-english-classifier · Hugging Face](https://huggingface.co/yanou16/cefr-english-classifier)",
          "sentiment_score": 0.9690724611282349,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojwm9dp",
          "summary_date": "2026-05-04",
          "comment_summary": "The C1/C2 confusion makes total sense. Even human raters struggle with that boundary sometimes. The Llama generation approach is clever but it might not capture enough of subtle discourse markers and advanced cohesion patterns that separate C2 from C1 level writing.",
          "sentiment_score": 0.8510081768035889,
          "sentiment_label": "Neutral"
        }
      ]
    },
    {
      "post_id": "1t3jmdc",
      "subreddit": "machinelearning",
      "post_score": 1,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t3jmdc/parax_v05_parametric_modeling_in_jax_p/",
      "post_content": "Parax v0.5: Parametric Modeling in JAX [P]",
      "comments": [
        {
          "comment_id": "ojwh2au",
          "summary_date": "2026-05-04",
          "comment_summary": "Nice, looks interesting. \nLogo looks ai-gened, IMO it's slightly offputting, lots of the JAX libraries follow the JAX-logo alphabet tensor shapes which has a nice unifying aesthetic.",
          "sentiment_score": 0.4024406373500824,
          "sentiment_label": "Positive"
        }
      ]
    },
    {
      "post_id": "1t3h6ug",
      "subreddit": "machinelearning",
      "post_score": 0,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t3h6ug/dtrying_to_switch_back_to_aiml_what_skills_are/",
      "post_content": "[D]Trying to switch back to AI/ML — what skills are actually in demand right now?[R]",
      "comments": [
        {
          "comment_id": "ojv2or4",
          "summary_date": "2026-05-04",
          "comment_summary": "Core ML fundamentals still matter a lot, especially for interviews and understanding what you’re doing. GenAI stuff (LLMS, Rag, langchain, etc.) is getting asked more, but companies want people who can build and deploy things, not just call APIs.",
          "sentiment_score": 0.8788681030273438,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojvzihq",
          "summary_date": "2026-05-04",
          "comment_summary": "Most of the jobs titled \"AI Engineer\" or even \"ML Engineer\" are currently focusing on applied LLMs (prompt, data, and backend engineering). There are still some roles where people do model training, but the field is increasingly relying on pretrained foundation models, rather than training a custom solution for each usecase.",
          "sentiment_score": 0.8596349954605103,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojvs53n",
          "summary_date": "2026-05-04",
          "comment_summary": "Number 3, Genai tools. There's probably more jobs writing wrappers for chatgpt or nanobanana, than there is for fundamental stuff for which you need to know deep learning. \n\nAt my current MLE job I did actual DL stuff but now I'm doing Agentic stuff which is more prompt engineering than actual engineering.",
          "sentiment_score": 0.8388723134994507,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojvjgxm",
          "summary_date": "2026-05-04",
          "comment_summary": "For job-readiness right now, I would focus on GenAI/RAG as the differentiator. LangChain is fine but it’s not the skill, the pipeline thinking is.",
          "sentiment_score": 0.7015119791030884,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojwp9l1",
          "summary_date": "2026-05-04",
          "comment_summary": "I don’t see a path back to where traditional ML approaches are popular at the vast majority of companies. For most applications just using an LLM is good enough and 1/100th of the effort.",
          "sentiment_score": 0.6737737059593201,
          "sentiment_label": "Negative"
        },
        {
          "comment_id": "ojv0pdf",
          "summary_date": "2026-05-04",
          "comment_summary": "The AI job market is becoming pretty bad, are you sure you want to enter it?",
          "sentiment_score": 0.49175092577934265,
          "sentiment_label": "Negative"
        }
      ]
    },
    {
      "post_id": "1t3savv",
      "subreddit": "machinelearning",
      "post_score": 0,
      "post_url": "https://www.reddit.com/r/MachineLearning/comments/1t3savv/how_do_you_experiment_with_a_very_large_model/",
      "post_content": "How do you experiment with a (very) large model architecture? [D]",
      "comments": [
        {
          "comment_id": "ojxdqzk",
          "summary_date": "2026-05-04",
          "comment_summary": "LLM is like a new baseball glove. At first, you think you're never gonna get a ball in there. But then you oil it up, work your fingers around in there a little, and pretty soon, you're pitching and catching.",
          "sentiment_score": 0.9242503643035889,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojxgi8t",
          "summary_date": "2026-05-04",
          "comment_summary": "Neural Scaling Laws are a well studied phenomenon to work with compute budget and large language models. The idea is to follow the laws to systematically change the parameters to preserve the trend better.",
          "sentiment_score": 0.8723112940788269,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojxdsv2",
          "summary_date": "2026-05-04",
          "comment_summary": "Another thing is they save lots of versions of the weights/models at different steps so you can experiment with the same 90% trained model multiple times. If you start from there it can change all those things you mentioned to still get good results (depending what it is you’re testing obviously.)",
          "sentiment_score": 0.78327476978302,
          "sentiment_label": "Neutral"
        },
        {
          "comment_id": "ojxd9pu",
          "summary_date": "2026-05-04",
          "comment_summary": "LR is not a replacement for batch size. All three methods will alter the distributions and you will probably not be able to accurately recreate results.",
          "sentiment_score": 0.5768634676933289,
          "sentiment_label": "Neutral"
        }
      ]
    }
  ]
}

---
title: "Machine Learning Subreddit"
date: "2026-05-04"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["AI", "ML", "Research", "Technology"]
---

# Overall Ranking and Top Discussions

1.  `[[D] Are modern ML PhDs becoming too incremental, or is this just what research looks like now?](https://www.reddit.com/r/MachineLearning/comments/1t311vb/are_modern_ml_phds_becoming_too_incremental_or_is/)` (Score: 134)
    *   This thread discusses whether modern ML PhDs are becoming too focused on incremental research due to the competitive nature of the field, or if this is simply the natural progression of research.
2.  `[[R] Why SSMs struggle in parameter-constrained training: empirical findings at 25M parameters](https://www.reddit.com/r/MachineLearning/comments/1t3hxsy/why_ssms_struggle_in_parameterconstrained/)` (Score: 21)
    *   This discussion delves into the reasons behind the struggles of State Space Models (SSMs) in parameter-constrained training, highlighting empirical findings related to compressibility and sequence length.
3.  `[[R] Struggling with Chebyshev Filter Integration in CNN — Any Advice?](https://www.reddit.com/r/MachineLearning/comments/1t2wybh/struggling_with_chebyshev_filter_integration_in/)` (Score: 9)
    *   Users are seeking advice on integrating Chebyshev filters into Convolutional Neural Networks (CNNs), with a focus on understanding their impact and potential benefits.
4.  `[[P] QLoRA Fine-Tuning of Qwen2.5-1.5B for CEFR English Proficiency Classification (A1–C2)](https://www.reddit.com/r/MachineLearning/comments/1t3ogbw/p_qlora_finetuning_of_qwen2515b_for_cefr_english/)` (Score: 2)
    *   This post details the fine-tuning of a Qwen2.5 model using QLoRA for classifying English proficiency levels, with discussion on model performance and potential limitations.
5.  `[Parax v0.5: Parametric Modeling in JAX [P]](https://www.reddit.com/r/MachineLearning/comments/1t3jmdc/parax_v05_parametric_modeling_in_jax_p/)` (Score: 1)
    *   This thread introduces Parax v0.5, a tool for parametric modeling in JAX, with comments touching on its aesthetics and integration within the JAX ecosystem.
6.  `[[D]Trying to switch back to AI/ML — what skills are actually in demand right now?[R]](https://www.reddit.com/r/MachineLearning/comments/1t3h6ug/dtrying_to_switch_back_to_aiml_what_skills_are/)` (Score: 0)
    *   Discussions revolve around the current in-demand skills for AI/ML roles, with a strong emphasis on Generative AI (GenAI), LLMs, and practical application development over traditional deep learning.
7.  `[How do you experiment with a (very) large model architecture? [D]](https://www.reddit.com/r/MachineLearning/comments/1t3savv/how_do_you_experiment_with_a_very_large_model/)` (Score: 0)
    *   This thread explores methodologies and best practices for experimenting with very large model architectures, including discussions on Neural Scaling Laws and model versioning.

# Detailed Analysis by Thread

**[[D] Are modern ML PhDs becoming too incremental, or is this just what research looks like now?](https://www.reddit.com/r/MachineLearning/comments/1t311vb/are_modern_ml_phds_becoming_too_incremental_or_is/) (Score: 134)**
*   **Summary:** The primary discussion revolves around whether ML PhDs are increasingly conducting incremental research due to intense competition and the pressure to publish, or if this is a normal aspect of research in a rapidly evolving field.
*   **Emotion:** The overall emotional tone is predominantly neutral, with some negative sentiment expressed regarding the perceived "incremental" nature of research and its potential impact on quality, while a few comments express a more positive outlook on the necessity and validity of incremental work.
*   **Top 3 Points of View:**
    *   A significant portion of the discussion suggests that competitive environments and the pressure to publish lead to incremental research, with some commenters lamenting this trend as a decrease in research quality.
    *   Another viewpoint is that this is a natural characteristic of PhD research in any field, and that the variance in individual ability and opportunity plays a larger role than the specific field of ML.
    *   Some users argue that incremental work is not inherently bad and can be impactful, while others point out that the hyper-competitive nature of ML research necessitates speed and staking claims early.

**[[R] Why SSMs struggle in parameter-constrained training: empirical findings at 25M parameters](https://www.reddit.com/r/MachineLearning/comments/1t3hxsy/why_ssms_struggle_in_parameterconstrained/) (Score: 21)**
*   **Summary:** This thread analyzes why State Space Models (SSMs) face challenges in parameter-constrained training. Key issues discussed include compressibility of weight distributions and the impact of sequence length on model performance, with empirical findings at 25M parameters.
*   **Emotion:** The emotional tone is overwhelmingly neutral, reflecting a technical discussion focused on empirical observations and potential solutions. Some appreciation is expressed for the "negative results" being less like typical AI hype.
*   **Top 3 Points of View:**
    *   A central argument is that the struggle is due to a statistical-prior mismatch and compressibility issues, suggesting that training with a regularizer nudging weights towards compressible distributions is a more effective fix than architectural changes.
    *   The SP4096 to SP8192 sign flip is identified as a canonical SSM failure mode, where state size must scale with sequence length to avoid recency bias; fixed parameter counts can lead to performance degradation at longer sequences.
    *   Technical details regarding kernel performance and mixed-precision issues are discussed, with an emphasis on how the selective-scan backward recomputation can be affected by memory pressure and numerical drift in lower precision.

**[[R] Struggling with Chebyshev Filter Integration in CNN — Any Advice?](https://www.reddit.com/r/MachineLearning/comments/1t3wybh/struggling_with_chebyshev_filter_integration_in/) (Score: 9)**
*   **Summary:** The discussion centers on a user's difficulty integrating Chebyshev filters into a CNN and seeks advice on how to proceed, explore its effectiveness, and understand its potential benefits over standard convolutional layers.
*   **Emotion:** The overall sentiment is neutral, indicating a problem-solving and advisory tone. Some commenters offer practical advice, while others suggest potential reasons for the filter's limited impact.
*   **Top 3 Points of View:**
    *   A common suggestion is to first verify if the Chebyshev filter is altering the signal in a way that the CNN cannot already learn; if accuracy remains unchanged, it might not be adding useful information.
    *   Users note the interchangeability between LTI filters and convolutions, but highlight that IIR filters like Chebyshev can have longer impulse responses with fewer parameters, which could be advantageous in specific scenarios (e.g., limited parameters or spatially large impulse responses).
    *   One piece of advice is to be honest with advisors about null results, as they are expected in research, and to consider testing the filter's effectiveness on smaller datasets to identify performance in low-data regimes.

**[[P] QLoRA Fine-Tuning of Qwen2.5-1.5B for CEFR English Proficiency Classification (A1–C2)](https://www.reddit.com/r/MachineLearning/comments/1t3ogbw/p_qlora_finetuning_of_qwen2515b_for_cefr_english/) (Score: 2)**
*   **Summary:** This post presents the fine-tuning of a Qwen2.5-1.5B model for classifying English proficiency (CEFR levels A1-C2) using QLoRA. The discussion touches on the model's performance and the challenges in distinguishing between C1 and C2 levels.
*   **Emotion:** The sentiment is neutral, with a generally positive reception to the work ("Pretty cool work!"). The discussion focuses on constructive feedback and potential areas for improvement.
*   **Top 3 Points of View:**
    *   There's an acknowledgment that the C1/C2 confusion is understandable, as even human raters find this boundary challenging.
    *   A question is raised about how the synthetic data generated by Llama holds up against real student writing, with curiosity about whether it captures the nuances of non-native patterns and errors.
    *   It's suggested that the synthetic generation might not be sufficiently capturing the subtle discourse markers and advanced cohesion patterns that truly differentiate C2 from C1 level writing.

**[Parax v0.5: Parametric Modeling in JAX [P]](https://www.reddit.com/r/MachineLearning/comments/1t3jmdc/parax_v05_parametric_modeling_in_jax_p/) (Score: 1)**
*   **Summary:** This thread introduces Parax v0.5, a new version of a tool for parametric modeling in JAX. The main comment expresses interest in the tool but offers a critique of its logo's aesthetic.
*   **Emotion:** The sentiment is positive, with the comment stating the tool "looks interesting." However, it also includes a minor critique of the logo.
*   **Top 3 Points of View:**
    *   The user finds the Parax v0.5 tool interesting and promising.
    *   A specific point of feedback is that the logo appears "AI-gened" and is slightly off-putting.
    *   A suggestion for a more unifying aesthetic is made by referencing the tensor shapes found in the JAX logo that other JAX libraries tend to follow.

**[[D]Trying to switch back to AI/ML — what skills are actually in demand right now?[R]](https://www.reddit.com/r/MachineLearning/comments/1t3h6ug/dtrying_to_switch_back_to_aiml_what_skills_are/) (Score: 0)**
*   **Summary:** This discussion focuses on the current job market for AI/ML professionals, with users seeking to understand which skills are most in demand. The consensus leans towards practical application of Generative AI (GenAI) and LLMs, as well as strong fundamentals and deployment capabilities.
*   **Emotion:** The emotional tone is a mix of concern and pragmatic advice. Some comments express a negative sentiment about the job market's direction ("becoming pretty bad"), while others offer neutral, helpful guidance on skill development.
*   **Top 3 Points of View:**
    *   A dominant viewpoint is that core ML fundamentals remain important, especially for interviews, but most roles now require practical experience with GenAI tools like LLMs, RAG, and LangChain, emphasizing building and deploying solutions.
    *   Many users note a shift in job titles like "AI Engineer" and "ML Engineer" towards applied LLMs (prompt engineering, data, backend) rather than core model training, with a reliance on pre-trained foundation models.
    *   There's a strong recommendation to combine ML basics with GenAI/RAG skills, focusing on end-to-end projects and pipeline thinking, as opposed to solely theoretical knowledge or traditional deep learning for every role.

**[How do you experiment with a (very) large model architecture? [D]](https://www.reddit.com/r/MachineLearning/comments/1t3savv/how_do_you_experiment_with_a_very_large_model/) (Score: 0)**
*   **Summary:** This thread explores effective methods for experimenting with large model architectures. Discussions include the application of Neural Scaling Laws, managing different versions of trained models, and the impact of hyperparameter choices on experimental reproducibility.
*   **Emotion:** The sentiment is primarily neutral, characterized by a technical and informative exchange of ideas and strategies for handling large models.
*   **Top 3 Points of View:**
    *   Neural Scaling Laws are recommended as a systematic approach to scaling large language models with a compute budget, ensuring parameter changes preserve trends.
    *   Saving multiple versions of model weights at different training stages is suggested as a way to enable experimentation with partially trained models, allowing for flexibility in testing various aspects.
    *   A caution is raised that methods like altering learning rates or batch sizes can change underlying distributions, potentially affecting the ability to accurately recreate results, and that smaller model experiments might show generalizability but lack exact accuracy.
