json
[
    {
        "post_id": "1swa26o",
        "subreddit": "machinelearning",
        "post_score": 55,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swa26o/why_do_only_big_ml_labs_dominate_widelyused/",
        "post_content": "Why do only big ML labs dominate widely-used models despite many open-source pretrained models smaller labs could do RL on? [D]",
        "comments": [
            {
                "comment_id": "oifb0xu",
                "summary_date": "2026-04-26",
                "comment_summary": "https://arxiv.org/abs/2104.03113",
                "sentiment_score": 0.9639546275138855,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiekqh2",
                "summary_date": "2026-04-26",
                "comment_summary": "Budget.",
                "sentiment_score": 0.9584391117095947,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oif5ttj",
                "summary_date": "2026-04-26",
                "comment_summary": "The big US labs pay insane amounts of cash for manual human-created datasets. The scale of data ops these companies have is massive with layers of vendors and contractors. Surge/Scale AI worth $30bn despite being annotator farms.",
                "sentiment_score": 0.9452205896377563,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiek2ak",
                "summary_date": "2026-04-26",
                "comment_summary": "1- proprietary high quality pretraining data\n\n2- proprietary high quality RLVR environments\n\nBoth are very very expensive",
                "sentiment_score": 0.9183326363563538,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oietua3",
                "summary_date": "2026-04-26",
                "comment_summary": "These guys have access to the most CUDA cores, the most memory and the most open source knowledge. When training, they can set their models too use more memory and use more cores.",
                "sentiment_score": 0.9015580415725708,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oie6hg6",
                "summary_date": "2026-04-26",
                "comment_summary": "Deepseek and Kimi have the compute and pretraining budget, but they do not have the implicit feedback loop from deploying at openai/anthropic scale.",
                "sentiment_score": 0.8972607851028442,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oie0ug4",
                "summary_date": "2026-04-26",
                "comment_summary": "Qwen, Kimi, deepseek are for most casual consumers on par with American models, but their main market is in Asia. Modern RL takes a lot of compute and you can train a lot.",
                "sentiment_score": 0.8671151399612427,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oie6pc5",
                "summary_date": "2026-04-26",
                "comment_summary": "At frontier scale, RL is expensive as $2.68/hr+ for one h100. The model has to fit the VRAM. It's prone to reward hacking.",
                "sentiment_score": 0.82805997133255,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oie8x3k",
                "summary_date": "2026-04-26",
                "comment_summary": "US labs keep finding new ways to improve the reward signal for things like prompt adherence. OSM labs generate new, higher quality post-training datasets from every new wave of proprietary models and focus their research efforts into less computationally intensive breakthroughs.",
                "sentiment_score": 0.7677674293518066,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oie5fkp",
                "summary_date": "2026-04-26",
                "comment_summary": "Many times these models do well in bench marks but real world usage is a bit shaky in my experience",
                "sentiment_score": 0.4587031900882721,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1swkxx1",
        "subreddit": "machinelearning",
        "post_score": 42,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swkxx1/can_geometric_deep_learning_lead_eliminate_the/",
        "post_content": "Can Geometric Deep Learning lead eliminate the need of \"Brute Force\" pre-training [D]",
        "comments": [
            {
                "comment_id": "oij50im",
                "summary_date": "2026-04-27",
                "comment_summary": "Stronger inductive biases mean you need less data, but you also cap what the model can learn outside those constraints. Transformers won because they traded efficiency for generality and threw compute at it.",
                "sentiment_score": 0.8352971076965332,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oigqmnb",
                "summary_date": "2026-04-26",
                "comment_summary": "All inductive biases result in increased performance on some data and worse performance on other data. The 'right' biases are a property of your data and determining them is a learning problem.",
                "sentiment_score": 0.7362470030784607,
                "sentiment_label": "Negative"
            },
            {
                "comment_id": "oihiog1",
                "summary_date": "2026-04-27",
                "comment_summary": "Finding the right inductive biases and invariances in the architecture is very hard and expensive. Data based machine learning is cheaper than a generic model that learns it all through data.",
                "sentiment_score": 0.7350026369094849,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oigcora",
                "summary_date": "2026-04-26",
                "comment_summary": "A model needs inductive biases to be able to force it to learn invariances. Structural models have been a thing in the statistics literature for many years before the deep learning boom.",
                "sentiment_score": 0.7041074633598328,
                "sentiment_label": "Positive"
            },
            {
                "comment_id": "oigh0as",
                "summary_date": "2026-04-26",
                "comment_summary": "Knowing what invariances and equivariances you need is not always as simply done as said, anyways I think researchers spend too little time considering the problem as such",
                "sentiment_score": 0.7018080949783325,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oikbbke",
                "summary_date": "2026-04-27",
                "comment_summary": "The \"baked in invariance = less data needed\" intuition holds cleanly for things like molecular property prediction where you know the symmetry group ahead of time. It gets messier fast when symmetries are approximate or compositional rather than exact.",
                "sentiment_score": 0.6081945896148682,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oigf6fr",
                "summary_date": "2026-04-26",
                "comment_summary": "There are some cases where symmetries in a model are too strong. With enough data augmentations, learning the right inductive biases is quite doable and cheap. AF3 randomly rotates and translates during training and it's arguably the best cofolding model right now",
                "sentiment_score": 0.5697176456451416,
                "sentiment_label": "Positive"
            },
            {
                "comment_id": "oigdre6",
                "summary_date": "2026-04-26",
                "comment_summary": "When you make the architecture equivariant, it becomes less expressive and it limits the capabilities of models. Some new architectures like Platonic transformers aims to tackle this.",
                "sentiment_score": 0.5670394897460938,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oigiev8",
                "summary_date": "2026-04-26",
                "comment_summary": "GDL is a nice mechanical formalism to describe model architectures, none the less it's more descriptive than predictive. It's insightful but not that many things came out of it.\n\nWe still need pre training and scaling, and we still use equivariance: self-attention is permutation equivariant, image patches need CNN's to encode, etc.",
                "sentiment_score": 0.4848966896533966,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oigoxk5",
                "summary_date": "2026-04-26",
                "comment_summary": "It is hard for geometry to preserve trait of many datas in llm. Maybe something like rieman manifold can represent complicated geometry space, but it costs a lot even if it improves model performance slightly. That is why it is uncommon. But who knows, someone makes great theory to apply",
                "sentiment_score": 0.4783332049846649,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1sx3p40",
        "subreddit": "machinelearning",
        "post_score": 27,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sx3p40/how_do_you_test_ai_agents_in_production_the/",
        "post_content": "How do you test AI agents in production? The unpredictability is overwhelming.[D]",
        "comments": [
            {
                "comment_id": "oilbg4k",
                "summary_date": "2026-04-27",
                "comment_summary": "Test contracts, not exact outputs.\n\nYou must also check tool choice, step order, schema, safety, and task success on fixed scenarios. Add edge cases and adversarial inputs. Track pass rates, not single runs.\n\nAnd make sure to use an LLM judge as one signal, not the gate. Rely on logs and production traces to catch regressions.",
                "sentiment_score": 0.9491135478019714,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik6e5s",
                "summary_date": "2026-04-27",
                "comment_summary": "We use Moyai to cluster production traces and evaluate them against normal business logic.",
                "sentiment_score": 0.9459342360496521,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oikqfud",
                "summary_date": "2026-04-27",
                "comment_summary": "Llms helps you create the scripts/use cases for 99% of use cases. When the user is inputting their query, llms auto complete with one of the 100 possible queries and they fill in the blanks.",
                "sentiment_score": 0.9355444312095642,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oikev55",
                "summary_date": "2026-04-27",
                "comment_summary": "DeepEval helps us with promoting changes, unsupervised clustering and error analysis on telemetry data.",
                "sentiment_score": 0.9214711785316467,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik91pi",
                "summary_date": "2026-04-27",
                "comment_summary": "An LLM is a non-deterministic tool. It's worth the extra effort and cost to use it.",
                "sentiment_score": 0.7857335209846497,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oilvyfw",
                "summary_date": "2026-04-27",
                "comment_summary": "Here's a take: Don't.\n\nIf you find that you need repeatable, trustworthy QA - for whatever reason - do not tie it to an LLM.",
                "sentiment_score": 0.6903235912322998,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oilfrz9",
                "summary_date": "2026-04-27",
                "comment_summary": "LLM evaluation is not trivial and depends on the specific application. It's not like deploying a unit test and forget about it.",
                "sentiment_score": 0.6395372748374939,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oikohdn",
                "summary_date": "2026-04-27",
                "comment_summary": "The action trace angle is the right one to make it practical to emit a structured event log from your agent. The hard part is deciding which branch points are load-bearing enough to formalize as invariants.",
                "sentiment_score": 0.6118488311767578,
                "sentiment_label": "Positive"
            },
            {
                "comment_id": "oik1wzy",
                "summary_date": "2026-04-27",
                "comment_summary": "Agent probably has a finite set of valid tool sequences for a given task. Write assertions against the action trace to test the agent's behaviour.",
                "sentiment_score": 0.6088517904281616,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik0b2g",
                "summary_date": "2026-04-27",
                "comment_summary": "The only way forward is to grow your evaluation dataset over time.",
                "sentiment_score": 0.5992904901504517,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1svzgin",
        "subreddit": "machinelearning",
        "post_score": 22,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1svzgin/how_to_collect_evidence_for_llm_reviewer_d/",
        "post_content": "How to collect evidence for LLM reviewer? [D]",
        "comments": [
            {
                "comment_id": "oidp1q7",
                "summary_date": "2026-04-26",
                "comment_summary": "Send a private note to the AC with your concerns that the review was LLM written and not relevant, with accompanying evidence.",
                "sentiment_score": 0.9262862801551819,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik7l3p",
                "summary_date": "2026-04-27",
                "comment_summary": "Just reply point-by-point in your rebuttal and, if needed, report it to the AC as a low-quality review instead of trying to prove LLM use since that’s basically impossible.",
                "sentiment_score": 0.8754006624221802,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oidptz6",
                "summary_date": "2026-04-26",
                "comment_summary": "hard to prove it’s llm-written, and acs usually don’t care about that part. focus on showing where the review is wrong or irrelevant, specific mismatches, not applicable baselines, misunderstandings. that’s more likely to move the outcome.",
                "sentiment_score": 0.8481464982032776,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oibyr9z",
                "summary_date": "2026-04-26",
                "comment_summary": "You respond to the points and hope that the other reviewers and the AC read it. You can try to tag the AC and explain your concerns, but if you have a good AC they will already see that the reviewer didn't reply to your rebuttal. If you have a bad AC there is nothing you can do",
                "sentiment_score": 0.7303335666656494,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oidchyo",
                "summary_date": "2026-04-26",
                "comment_summary": "LLM-written reviews tend to have perfect grammar but awkward conceptual gaps. C citation errors, wrong venue names, wrong paper titles, overly generic criticism and missing the novel part of the novel while criticizing something standard are also common.",
                "sentiment_score": 0.5730831027030945,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oic81dk",
                "summary_date": "2026-04-26",
                "comment_summary": "I'd report him for LLM usage since this is a hot topic at the moment. While low quality reviews have been around since the beginning of peer review. \n\nHaving said that, it highly depends on your AC if there will be any action or consequences. Don't get your hopes up that this will be resolved.",
                "sentiment_score": 0.41431960463523865,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1sx0bnx",
        "subreddit": "machinelearning",
        "post_score": 20,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sx0bnx/maths_vs_machine_learning_publishing_venues_d/",
        "post_content": "Maths vs machine learning publishing venues [D]",
        "comments": [
            {
                "comment_id": "oikzlkg",
                "summary_date": "2026-04-27",
                "comment_summary": "since you mentioned being a mathematician,you might want to look at information and interference. they specialize the intraction of maths and data science",
                "sentiment_score": 0.9264917373657227,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiko7rr",
                "summary_date": "2026-04-27",
                "comment_summary": "What is a good journal for some people might not be to others, I would for example consider a journal that has 60-pages long theoretical papers to not be useful for me.\n\nRule of thumb is, the best place to submit os the journal from which most of your references are",
                "sentiment_score": 0.6592676639556885,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijib6g",
                "summary_date": "2026-04-27",
                "comment_summary": "For TCS you're better off with STOC, FOCS, SODA, or COLT. ACM or SIAM are decent if you want to submit to a journal. Annals of Statistics or JASA are good for statsy papers. JML",
                "sentiment_score": 0.4928513467311859,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijhvu1",
                "summary_date": "2026-04-27",
                "comment_summary": "Sounds ideal for JMLR",
                "sentiment_score": 0.48557278513908386,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1swuw9g",
        "subreddit": "machinelearning",
        "post_score": 19,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swuw9g/freshman_in_ml_how_do_you_identify_actually_open/",
        "post_content": "freshman in ML: how do you identify actually open research problems? [D]",
        "comments": [
            {
                "comment_id": "oiieqc2",
                "summary_date": "2026-04-27",
                "comment_summary": "Professors are likely to understand the open problems.",
                "sentiment_score": 0.8862446546554565,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiicrep",
                "summary_date": "2026-04-27",
                "comment_summary": "Some advice my buddy‘s supervisor gave: find the craziest/best paper in your desired field and read through their future work.\n\nEvery paper has a future work section.",
                "sentiment_score": 0.787224292755127,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiidq85",
                "summary_date": "2026-04-27",
                "comment_summary": "ngl i spent months thinking i had original ideas only to find papers from 2022 doing exactly that. what actually helped stop reading papers first, start with github issues and workshop discussions. that's where you see what's actually stuck vs what just looks stuck on arxiv.",
                "sentiment_score": 0.7533871531486511,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oij624j",
                "summary_date": "2026-04-27",
                "comment_summary": "LLMs are very helpful to organize papers in a wiki like structure\n[https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)\n\nI have currently a pipeline where I ingest all the papers I am interested in (around 35 so far) and then use the whole wiki as a context to the LLM when asking research questions.",
                "sentiment_score": 0.6334439516067505,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiicqed",
                "summary_date": "2026-04-27",
                "comment_summary": "In ML research, you study probability, linear algebra, topology, real analysis and develop in depth knowledge in them. Then you study research papers and you identify their weaknesses and flaws. That skill will only come when you have deep knowledge of maths.",
                "sentiment_score": 0.6021038889884949,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiii3bh",
                "summary_date": "2026-04-27",
                "comment_summary": "Research i.e. Scientific method, is already designed for this. Apply the objective, question, hypothesis loop iteratively and it follows naturally. There is a reason why papers are structured the way they are.",
                "sentiment_score": 0.5968148112297058,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiiczt4",
                "summary_date": "2026-04-27",
                "comment_summary": "I think it should start with your interest. See what you want to build, then explore what is available, and finally see what open source has already solved, and what is that piece you want to solve based on your requirements/interests.",
                "sentiment_score": 0.45566868782043457,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiilshq",
                "summary_date": "2026-04-27",
                "comment_summary": "your research ideas likely *** (no offense). the prof will have a much better read of the field and will be able to recommend potential avenues",
                "sentiment_score": 0.3214726150035858,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1sw5b44",
        "subreddit": "machinelearning",
        "post_score": 15,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sw5b44/going_from_3b7b_dense_to_nemotron_3_nano_hybrid/",
        "post_content": "Going from 3B/7B dense to Nemotron 3 Nano (hybrid Mamba-MoE) for multi-task reasoning — what changes in the fine-tuning playbook? [D]",
        "comments": [
            {
                "comment_id": "oij7ax8",
                "summary_date": "2026-04-27",
                "comment_summary": "freezing the router and LoRA-ing expert FFNs is the safer first move, unfreezing the router early tends to destabilize load balancing before task gradients settle. track per-expert activation counts per task so you catch silent degradation. for your simpler subtasks like classification or routing, ZeroGPU handles those separatly.",
                "sentiment_score": 0.8896723985671997,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oidzmfl",
                "summary_date": "2026-04-26",
                "comment_summary": "The first step in a routing experiment is to freeze the router for one run and log expert utilization per capability, expert choice, entropy, dropped/overflow tokens, and before/after deltas against the base model. The failure mode is recurrent/state behavior becoming unstable",
                "sentiment_score": 0.8724101781845093,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oidmkgx",
                "summary_date": "2026-04-26",
                "comment_summary": "i’d strongly lean toward freezing the router on first passes and only LoRA-ing experts + attention, otherwise you risk destabilizing routing before your signal is even clean. then treat eval as per-capability slices, not aggregate, because it’s very easy for one task to quietly collapse if it gets under-routed.",
                "sentiment_score": 0.7322189211845398,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oidta3c",
                "summary_date": "2026-04-26",
                "comment_summary": "40-80k synthetic examples from Sonnet 4.6 and Opus 4.7 for 20% is going to cost a pretty hefty sum to generate. It costs me anywhere from $100 to $200 to run Sonnet on a 2.5k query benchmark set. I",
                "sentiment_score": 0.5587561130523682,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oid1u5b",
                "summary_date": "2026-04-26",
                "comment_summary": "Nemo's architecture makes sense for multi-task reasoning, but he should be worried about the hybrid complications. Jamba's MoE router behavior under LoRA was trickier than expected. SSM projections in Mamba-2 have some numerical quirks under low-rank updates",
                "sentiment_score": 0.25873488187789917,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1swfftl",
        "subreddit": "machinelearning",
        "post_score": 14,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swfftl/speculative_decoding_implementations_eagle3/",
        "post_content": "Speculative Decoding Implementations: EAGLE-3, Medusa-1, PARD, Draft Models, N-gram and Suffix Decoding from scratch [P]",
        "comments": [
            {
                "comment_id": "oifnuja",
                "summary_date": "2026-04-26",
                "comment_summary": "https://www.reddit.com/r/LocalLLaMA/s/pTxlNNiAvi",
                "sentiment_score": 0.9593836665153503,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oif66yg",
                "summary_date": "2026-04-26",
                "comment_summary": "This is good",
                "sentiment_score": 0.892943799495697,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1swtk3h",
        "subreddit": "machinelearning",
        "post_score": 13,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swtk3h/submitting_to_top_ml_conferences_without_sharing/",
        "post_content": "Submitting to top ML Conferences without Sharing code [D]",
        "comments": [
            {
                "comment_id": "oii5v0s",
                "summary_date": "2026-04-27",
                "comment_summary": "Never share your code. ( unless you plan to make it public) Ideas get published. Codes get copied.",
                "sentiment_score": 0.9424856901168823,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiiqpd0",
                "summary_date": "2026-04-27",
                "comment_summary": "No one will stole those codes. \n\nIf they really like an idea, they will use Claude Code to reproduce a new one.",
                "sentiment_score": 0.9304923415184021,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiineid",
                "summary_date": "2026-04-27",
                "comment_summary": "If the paper describes something that I could conceivably implement, no code is needed. This is limited to things that are simple-ish and don't require proprietary data. If you provide code but not the data, I can be understanding.",
                "sentiment_score": 0.7769604921340942,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oij1p26",
                "summary_date": "2026-04-27",
                "comment_summary": "I want to gather feedback on whether we should stop sharing code in submissions and publish them after acceptance.",
                "sentiment_score": 0.7573348879814148,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oij6j87",
                "summary_date": "2026-04-27",
                "comment_summary": "Reviewers treat code as a proxy for \"could this actually run\" so removing it can create skepticism even if your method section is solid.",
                "sentiment_score": 0.7502622008323669,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiipci5",
                "summary_date": "2026-04-27",
                "comment_summary": "From my experience with ARR and A* ACL conferences, a statement in the paper to publicly share the code was perceived positively by the reviewers. It wasn't necessary to already share the code with the paper when submitting for review.",
                "sentiment_score": 0.7073743939399719,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiiabxs",
                "summary_date": "2026-04-27",
                "comment_summary": "The two comments are literally the dilemma OP is facing rip, I vote for not sharing the code if its valuable enough atp, happened to me :)",
                "sentiment_score": 0.692462146282196,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiibpws",
                "summary_date": "2026-04-27",
                "comment_summary": "If your code has lots of optional flags and to-be-implemented things, I would focus on stripping those. And plant the flag by having a preprint up.",
                "sentiment_score": 0.6480040550231934,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oii3xty",
                "summary_date": "2026-04-27",
                "comment_summary": "You don't need to share code for a submission. No one will steal your code during the review process and after it's published.",
                "sentiment_score": 0.4190281331539154,
                "sentiment_label": "Positive"
            }
        ]
    },
    {
        "post_id": "1sx8xpa",
        "subreddit": "machinelearning",
        "post_score": 11,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sx8xpa/what_do_reviewers_actually_mean_when_they_say_the/",
        "post_content": "What do reviewers actually mean when they say the paper sound more like a technical report? [D]",
        "comments": [
            {
                "comment_id": "oil9u58",
                "summary_date": "2026-04-27",
                "comment_summary": "A paper needs a hypothesis and then your experiment/pathway to prove or disprove it. \n\nIf you just 'did a thing' and then reported on it, it would only be a technical documentation and not much more. \n\nThat could be the problem.",
                "sentiment_score": 0.9452651143074036,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oimc4oj",
                "summary_date": "2026-04-27",
                "comment_summary": "depending on the context this could also mean showing the results but not expanding on the methodology enough for reproducibility, lack of ablations, etc. Eg the kinds of “releases” we tend to see from the big companies now",
                "sentiment_score": 0.9104712605476379,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oil7z0y",
                "summary_date": "2026-04-27",
                "comment_summary": "Lack of novelty, just reporting what you have done instead of insightful benchmarking/discussions, likely a pipeline/implementation paper",
                "sentiment_score": 0.7886682152748108,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oil33mz",
                "summary_date": "2026-04-27",
                "comment_summary": "It's not about the format but what you have written. \n\nI am not 100% sure what they mean by that but my hypothesis is that you provided a list of different approaches to solve a problem, or ran some benchmarks without specifying very clearly a new research problem.",
                "sentiment_score": 0.5872696042060852,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oillfpb",
                "summary_date": "2026-04-27",
                "comment_summary": "Most undergrad academic work teaches how to write technical reports rather than research papers. Academic papers are written to disseminate a proposition to a science community.",
                "sentiment_score": 0.564902126789093,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oil80v4",
                "summary_date": "2026-04-27",
                "comment_summary": "A paper is not the description of experiments and results. The focus should be on the main concept of the paper. The sweet spot is to put enough technical details (numbers, formula ecc) but not more than necessary.",
                "sentiment_score": 0.5480817556381226,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oilmhjj",
                "summary_date": "2026-04-27",
                "comment_summary": "You already got your best answers, I'll add a short one. \n\nThe engineering is engineering, but the science is not sciencing.",
                "sentiment_score": 0.5459123849868774,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oilqgjx",
                "summary_date": "2026-04-27",
                "comment_summary": "Lack of novelty",
                "sentiment_score": 0.4313906133174896,
                "sentiment_label": "Negative"
            }
        ]
    },
    {
        "post_id": "1swwsin",
        "subreddit": "machinelearning",
        "post_score": 9,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swwsin/value_of_top_conference_workshop_papers_for_phd/",
        "post_content": "Value of top conference workshop papers for PhD admissios [D]",
        "comments": [
            {
                "comment_id": "oijk5vh",
                "summary_date": "2026-04-27",
                "comment_summary": "I got my PhD thanks to a workshop paper during my undergrad",
                "sentiment_score": 0.9851135015487671,
                "sentiment_label": "Positive"
            },
            {
                "comment_id": "oiixka2",
                "summary_date": "2026-04-27",
                "comment_summary": "Some workshops' papers will appear in the proceedings. Most mature workshops have more rigorous review and better publicity. Many use the opportunity as a quick way to validate a preliminary finding or submit a small work.",
                "sentiment_score": 0.8116298317909241,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiioz89",
                "summary_date": "2026-04-27",
                "comment_summary": "While some will have Main papers not all will achieve it and better have some publication than none",
                "sentiment_score": 0.7142539620399475,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oiktq0m",
                "summary_date": "2026-04-27",
                "comment_summary": "The publication itself is a minor boost. It might be a better boost if it was a research that you lead most of the work and are the first author. It overall doesn't hurt, but I wouldn't pay conference participation out of pocket for it if your university doesn't cover it",
                "sentiment_score": 0.7082257866859436,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijbw81",
                "summary_date": "2026-04-27",
                "comment_summary": "Quantity helps too, so if you can do both go for it. I had 14 peer reviewed papers and that was a large part of what got me into Stanford.",
                "sentiment_score": 0.6332166194915771,
                "sentiment_label": "Positive"
            },
            {
                "comment_id": "oijo54s",
                "summary_date": "2026-04-27",
                "comment_summary": "Workshop papers are useful as they show you can take a project end to end and write it up and engage with a research community.",
                "sentiment_score": 0.5391446948051453,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oil43z9",
                "summary_date": "2026-04-27",
                "comment_summary": "workshop papers are important for PhD students. Top researchers publish in workshops all the time. Industry gives importance to workshop papers if the workshops are strongly aligned to what they are doing.",
                "sentiment_score": 0.46815410256385803,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1sx35es",
        "subreddit": "machinelearning",
        "post_score": 5,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sx35es/int8_quantization_gives_me_better_accuracy_than/",
        "post_content": "INT8 quantization gives me better accuracy than FP16 ! [D]",
        "comments": [
            {
                "comment_id": "oik81ni",
                "summary_date": "2026-04-27",
                "comment_summary": "To pick between quantization:\nfp16 if values are smaller\nbf16 if values are large, or are accumulated\nint8: values are equally distributed\nfp8: values are normally distributed",
                "sentiment_score": 0.9636095762252808,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik681i",
                "summary_date": "2026-04-27",
                "comment_summary": "Eh, can see it happening, fp16 has some serious issues with small models due to only having 5bit exponent. bfloat16 is often appropriate in this instance.",
                "sentiment_score": 0.8286135196685791,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijxsxx",
                "summary_date": "2026-04-27",
                "comment_summary": "It's far more likely you're experiment is bad then INT8 outperforming FP16. Run this on real data not a toy example and then see what happens. Plenty of sets on Kaggle to test with along with others results to compare against.",
                "sentiment_score": 0.7361661791801453,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oik592y",
                "summary_date": "2026-04-27",
                "comment_summary": "There are 3 possibilities regarding the quantization of int8 data. It can be done with data, with more relevant data or on other settings.",
                "sentiment_score": 0.579903244972229,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijxfum",
                "summary_date": "2026-04-27",
                "comment_summary": "Cancelation of errors?",
                "sentiment_score": 0.44919919967651367,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1sx6vlm",
        "subreddit": "machinelearning",
        "post_score": 4,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1sx6vlm/cvpr_workshop_decisions_d/",
        "post_content": "CVPR Workshop Decisions [D]",
        "comments": [
            {
                "comment_id": "oiknvj8",
                "summary_date": "2026-04-27",
                "comment_summary": "I submitted to a workshop. The notification deadline has already passed, and I didn't see any reviews.",
                "sentiment_score": 0.7683731913566589,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1swxx1v",
        "subreddit": "machinelearning",
        "post_score": 4,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swxx1v/three_limitations_i_keep_hitting_with/",
        "post_content": "Three limitations I keep hitting with retrieval-augmented generation in production and I'm running out of ideas [D]",
        "comments": [
            {
                "comment_id": "oij62uq",
                "summary_date": "2026-04-27",
                "comment_summary": "There are problems with the retrieval of data from a too weak general LLM model guiding the retrieval. The timeline problam is also a model capability issue.",
                "sentiment_score": 0.9363723993301392,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijjzqb",
                "summary_date": "2026-04-27",
                "comment_summary": "The negative knowledge problem is the one that bit us hardest. Similarity thresholds don't work because you're using a continuous score to answer a binary question. After retrieval, after classification, the model asks the model explicitly \"does any of this actually answer the question?\" before synthesis.",
                "sentiment_score": 0.8248718976974487,
                "sentiment_label": "Neutral"
            },
            {
                "comment_id": "oijuhj0",
                "summary_date": "2026-04-27",
                "comment_summary": "The scatter problem only got better when we ran a query-decomposition pre-pass that pulls dimensions from corpus metadata (states) and does per-dimension retrieval. Negative knowledge needed a separate coverage map index, small one with just chunk titles and summaries embedded. For",
                "sentiment_score": 0.7881050705909729,
                "sentiment_label": "Neutral"
            }
        ]
    },
    {
        "post_id": "1swsshs",
        "subreddit": "machinelearning",
        "post_score": 3,
        "post_url": "https://www.reddit.com/r/MachineLearning/comments/1swsshs/building_an_operational_tool_for_heavy_industry/",
        "post_content": "Building an operational tool for heavy industry — Seeking \"real world\" data and site reality [R]",
        "comments": [
            {
                "comment_id": "oihydj5",
                "summary_date": "2026-04-27",
                "comment_summary": "I built data pipelines for logistics and fleet ops before. If you need help building the data ingestion side I do that work for a flat fee.",
                "sentiment_score": 0.6114678978919983,
                "sentiment_label": "Neutral"
            }
        ]
    }
]
---
title: "Machine Learning Subreddit"
date: "2026-04-27"
description: "Analysis of top discussions and trends in the machinelearning subreddit"
tags: ["machinelearning", "AI", "data science", "deep learning"]
---

# Overall Ranking and Top Discussions
1.  [[D] Why do only big ML labs dominate widely-used models despite many open-source pretrained models smaller labs could do RL on?](https://www.reddit.com/r/MachineLearning/comments/1swa26o/why_do_only_big_ml_labs_dominate_widelyused/) (Score: 55)
    *   Users discuss the reasons behind the dominance of large ML labs in creating widely-used models, exploring factors like budget, proprietary data, hardware access, and the advantages of large-scale data operations.
2.  [[D] Can Geometric Deep Learning lead eliminate the need of "Brute Force" pre-training](https://www.reddit.com/r/MachineLearning/comments/1swkxx1/can_geometric_deep_learning_lead_eliminate_the/) (Score: 42)
    *   The discussion revolves around whether Geometric Deep Learning can reduce the reliance on extensive pre-training, with participants debating the trade-offs of inductive biases, the generality of transformers, and the practical challenges of identifying and implementing correct symmetries.
3.  [[D] How do you test AI agents in production? The unpredictability is overwhelming.](https://www.reddit.com/r/MachineLearning/comments/1sx3p40/how_do_you_test_ai_agents_in_production_the/) (Score: 27)
    *   This thread explores strategies for testing AI agents in production, focusing on methods like testing contracts instead of exact outputs, using LLM judges, analyzing production traces, and the challenges posed by the inherent unpredictability of these agents.
4.  [[D] How to collect evidence for LLM reviewer?](https://www.reddit.com/r/MachineLearning/comments/1svzgin/how_to_collect_evidence_for_llm_reviewer_d/) (Score: 22)
    *   The conversation centers on how to identify and present evidence if a reviewer's feedback appears to be AI-generated, discussing common signals of LLM-written reviews and strategies for appealing or reporting such cases.
5.  [[D] freshman in ML: how do you identify actually open research problems?](https://www.reddit.com/r/MachineLearning/comments/1swuw9g/freshman_in_ml_how_do_you_identify_actually_open/) (Score: 19)
    *   Newcomers to Machine Learning seek advice on how to find open research problems, with suggestions including consulting professors, examining future work sections of papers, looking at GitHub issues, and leveraging LLMs for paper organization.
6.  [[D] Going from 3B/7B dense to Nemotron 3 Nano (hybrid Mamba-MoE) for multi-task reasoning — what changes in the fine-tuning playbook?](https://www.reddit.com/r/MachineLearning/comments/1sw5b44/going_from_3b7b_dense_to_nemotron_3_nano_hybrid/) (Score: 15)
    *   Users discuss the considerations and changes needed when fine-tuning a hybrid Mamba-MoE model compared to dense models, focusing on aspects like router freezing, expert utilization, and potential instability in recurrent states.
7.  [[P] Speculative Decoding Implementations: EAGLE-3, Medusa-1, PARD, Draft Models, N-gram and Suffix Decoding from scratch](https://www.reddit.com/r/MachineLearning/comments/1swfftl/speculative_decoding_implementations_eagle3/) (Score: 14)
    *   A post sharing implementations of various speculative decoding techniques, with a brief positive reception.
8.  [[D] Submitting to top ML Conferences without Sharing code](https://www.reddit.com/r/MachineLearning/comments/1swtk3h/submitting_to_top_ml_conferences_without_sharing/) (Score: 13)
    *   The community debates the pros and cons of sharing code when submitting to top ML conferences, considering concerns about idea theft versus the benefits of reproducibility and reviewer trust.
9.  [[D] What do reviewers actually mean when they say the paper sound more like a technical report?](https://www.reddit.com/r/MachineLearning/comments/1sx8xpa/what_do_reviewers_actually_mean_when_they_say_the/) (Score: 11)
    *   Reviewers' feedback about a paper sounding like a "technical report" is analyzed, with discussions covering lack of hypothesis, insufficient methodology, absence of novelty, and the distinction between describing what was done versus telling a compelling scientific story.
10. [[D] Value of top conference workshop papers for PhD admissios](https://www.reddit.com/r/MachineLearning/comments/1swwsin/value_of_top_conference_workshop_papers_for_phd/) (Score: 9)
    *   The value of publishing in top conference workshops for PhD admissions is discussed, with opinions varying on its impact, though generally seen as beneficial for demonstrating research capability and community engagement.
11. [[D] INT8 quantization gives me better accuracy than FP16 !](https://www.reddit.com/r/MachineLearning/comments/1sx35es/int8_quantization_gives_me_better_accuracy_than/) (Score: 5)
    *   A user reports better accuracy with INT8 quantization than FP16, leading to a discussion about potential reasons, including experimental setup, data distribution, and specific layer characteristics.
12. [[D] CVPR Workshop Decisions](https://www.reddit.com/r/MachineLearning/comments/1sx6vlm/cvpr_workshop_decisions_d/) (Score: 4)
    *   A user shares their experience of a missed notification deadline for a CVPR workshop submission.
13. [[D] Three limitations I keep hitting with retrieval-augmented generation in production and I'm running out of ideas](https://www.reddit.com/r/MachineLearning/comments/1swxx1v/three_limitations_i_keep_hitting_with/) (Score: 4)
    *   Users discuss common challenges in production RAG systems, such as query decomposition, handling negative knowledge, and timeline accuracy, offering potential solutions like query decomposition, coverage map indexes, and explicit date-bucketed retrieval.
14. [[R] Building an operational tool for heavy industry — Seeking "real world" data and site reality](https://www.reddit.com/r/MachineLearning/comments/1swsshs/building_an_operational_tool_for_heavy_industry/) (Score: 3)
    *   A user with experience in data pipelines for logistics and fleet operations offers help with data ingestion for an operational tool targeting heavy industry.

# Detailed Analysis by Thread

**[[D] Why do only big ML labs dominate widely-used models despite many open-source pretrained models smaller labs could do RL on?](https://www.reddit.com/r/MachineLearning/comments/1swa26o/why_do_only_big_ml_labs_dominate_widelyused/) (Score: 55)**
*   **Summary:** This thread explores why large ML research labs tend to dominate the development of widely-used models, even when smaller labs have access to open-source pre-trained models. The discussion highlights that factors beyond model architecture, such as substantial budgets for proprietary data acquisition, extensive data operations, access to cutting-edge hardware, and sophisticated RL environments, are crucial for achieving and maintaining dominance. The cost and complexity of data annotation and RL training are emphasized as significant barriers for smaller entities.
*   **Emotion:** The overall emotional tone is neutral, with users presenting factual reasons and observations about the industry.
*   **Top 3 Points of View:**
    *   **Financial and Data Dominance:** The primary argument is that big labs possess significantly larger budgets, allowing them to invest heavily in creating and acquiring high-quality, manually curated datasets and proprietary RL environments, which are prohibitively expensive for smaller labs.
    *   **Hardware and Infrastructure Advantages:** Access to superior hardware, particularly GPUs with more memory and processing power, enables larger models and more complex training. This, combined with leveraging open-source knowledge, allows for continuous scaling.
    *   **Production Feedback Loop:** A key differentiator is the "production feedback loop" from deploying models at scale, which provides invaluable real-world usage data that smaller labs cannot replicate, enabling faster iteration and alignment improvements.

**[[D] Can Geometric Deep Learning lead eliminate the need of "Brute Force" pre-training](https://www.reddit.com/r/MachineLearning/comments/1swkxx1/can_geometric_deep_learning_lead_eliminate_the/) (Score: 42)**
*   **Summary:** The discussion questions whether Geometric Deep Learning (GDL) can reduce the necessity for extensive "brute force" pre-training. Participants explore the idea that incorporating specific inductive biases and symmetries into architectures could lead to more data-efficient learning. However, they also note that transformers' success came from their generality and computational scale, and GDL's effectiveness is often domain-specific where symmetries are well-understood, contrasting with real-world problems where identifying such symmetries is challenging or where approximate symmetries are more common.
*   **Emotion:** The overall tone is neutral to slightly negative when discussing the difficulties and limitations of GDL.
*   **Top 3 Points of View:**
    *   **Inductive Biases vs. Generality:** A core debate is whether specific inductive biases in GDL lead to data efficiency for certain tasks but also limit generalization, versus the broad applicability and computational power of transformer architectures that learn from vast amounts of data.
    *   **Learning Biases vs. Encoding Biases:** Some argue that "the right" inductive biases are data-dependent and should be learned by the machine, not pre-encoded by humans, suggesting that encoding biases is akin to replacing machine learning with human learning.
    *   **Practicality and Domain Specificity:** GDL shows promise in domains with known geometry (e.g., molecular structures, physics simulations) but becomes more complex when symmetries are approximate or compositional. The difficulty in identifying the correct biases and the potential for them to be "too strong" are highlighted.

**[[D] How do you test AI agents in production? The unpredictability is overwhelming.](https://www.reddit.com/r/MachineLearning/comments/1sx3p40/how_do_you_test_ai_agents_in_production_the/) (Score: 27)**
*   **Summary:** This thread addresses the significant challenge of testing unpredictable AI agents in production environments. The consensus leans towards testing "contracts" (expected behaviors and constraints) rather than exact outputs. Key strategies discussed include verifying tool choices, step order, schema adherence, safety, and task success on fixed scenarios, using LLM judges cautiously, and relying on production logs and traces. The inherent non-determinism of LLMs is a major concern, leading some to suggest avoiding tight coupling with LLMs for critical QA.
*   **Emotion:** The tone is predominantly neutral, reflecting a practical discussion of technical challenges and solutions.
*   **Top 3 Points of View:**
    *   **Test Contracts, Not Outputs:** A strong recommendation is to focus on testing the agent's adherence to predefined contracts, including tool usage, step order, schema validation, and task success rates, rather than expecting consistent verbatim outputs.
    *   **Action Trace and Deterministic Assertions:** A promising approach involves emitting structured event logs from the agent that capture decision context at each branch point. Deterministic assertions can then be written against these logs to verify critical business rules and invariants, making testing more stable.
    *   **Challenges of LLM Non-Determinism:** The inherent unpredictability of LLMs is a core problem. Some advise against tying repeatable QA directly to LLMs, while others suggest strategies to manage this, such as using LLM judges as one signal among many and accepting that some use-cases may fail due to non-determinism.

**[[D] How to collect evidence for LLM reviewer?](https://www.reddit.com/r/MachineLearning/comments/1svzgin/how_to_collect_evidence_for_llm_reviewer_d/) (Score: 22)**
*   **Summary:** This discussion focuses on how to handle academic reviews that may have been written by an LLM. The primary advice is to focus on the *content* of the review, highlighting its inaccuracies, irrelevance, or conceptual gaps, rather than trying to definitively prove LLM authorship, which is difficult. Users suggest reporting low-quality reviews to the Area Chair (AC) and emphasizing substantive criticisms to influence the outcome. Signals for potential LLM writing include perfect grammar with conceptual flaws, citation errors, and generic criticism.
*   **Emotion:** The tone is neutral, with a pragmatic approach to dealing with a perceived problem in academic peer review.
*   **Top 3 Points of View:**
    *   **Focus on Content, Not Authorship:** The consensus is that proving LLM authorship is challenging and often not the AC's primary concern. Instead, one should focus on refuting the review's claims based on their substance (errors, irrelevance, lack of novelty) to make a stronger case.
    *   **Report to Area Chair (AC):** Users suggest directly informing the AC about concerns regarding the review's quality, especially if it seems poorly reasoned or irrelevant, rather than engaging in a debate about LLM use.
    *   **Identifying LLM-like Signals:** Common indicators of LLM-written reviews include perfect grammar but awkward conceptual misunderstandings, factual errors like hallucinated citations, overly generic feedback, and missing the paper's core novelty.

**[[D] Maths vs machine learning publishing venues [D]](https://www.reddit.com/r/MachineLearning/comments/1sx0bnx/maths_vs_machine_learning_publishing_venues_d/) (Score: 20)**
*   **Summary:** This thread discusses the differences and suitability of publishing venues for mathematics versus machine learning. Participants suggest specific conferences (STOC, FOCS, SODA, COLT for theory) and journals (ACM, SIAM, Annals of Statistics, JASA, JMLR) based on the nature of the research, with a general sentiment that conferences are often more respected than journals in ML theory, and that the best journal is often where one's references come from.
*   **Emotion:** The tone is neutral, offering advice on academic publishing.
*   **Top 3 Points of View:**
    *   **Conference vs. Journal Preference:** For theoretical computer science (TCS) and ML theory, top conferences are often considered more prestigious and widely read than journals. Journals are seen as less accessible and read primarily by reviewers.
    *   **Venue Suitability Based on Field:** Specific venues are recommended based on the research area: STOC, FOCS, SODA, and COLT for theory; Annals of Statistics and JASA for "statsy" papers; and JMLR for pure ML papers, ideally with a preceding conference version.
    *   **Reference-Based Journal Selection:** A pragmatic rule of thumb is to submit to journals from which most of the references in one's own paper are drawn, as this indicates a relevant audience.

**[[D] freshman in ML: how do you identify actually open research problems?](https://www.reddit.com/r/MachineLearning/comments/1swuw9g/freshman_in_ml_how_do_you_identify_actually_open/) (Score: 19)**
*   **Summary:** This thread offers advice to newcomers in Machine Learning on how to discover open research problems. Suggestions include consulting professors, examining the "future work" sections of impactful papers, delving into GitHub issues and workshop discussions to find practical stuck points rather than just theoretical ones, and using LLMs to organize research papers and generate insights from synthesized information. A strong emphasis is placed on building a deep foundational knowledge in mathematics and statistics as a prerequisite for identifying research gaps.
*   **Emotion:** The tone is neutral and helpful, aimed at guiding junior researchers.
*   **Top 3 Points of View:**
    *   **Leverage Existing Research and Experts:** A common piece of advice is to read the "future work" sections of top papers in a field and to consult with professors or senior researchers who have a better grasp of the research landscape and open problems.
    *   **Look Beyond Published Papers:** Some users suggest that truly "stuck" problems are often discussed in less formal settings like GitHub issues or workshop discussions, which can offer a more direct view of current challenges than polished academic papers.
    *   **Build Strong Foundational Knowledge:** A crucial point is that identifying research gaps requires deep expertise in foundational areas like probability, linear algebra, and analysis, allowing one to critically evaluate existing work and identify weaknesses or unaddressed areas.

**[[D] Going from 3B/7B dense to Nemotron 3 Nano (hybrid Mamba-MoE) for multi-task reasoning — what changes in the fine-tuning playbook?](https://www.reddit.com/r/MachineLearning/comments/1sw5b44/going_from_3b7b_dense_to_nemotron_3_nano_hybrid/) (Score: 15)**
*   **Summary:** This discussion focuses on the practicalities of fine-tuning a hybrid Mamba-MoE model (Nemotron 3 Nano) for multi-task reasoning, as opposed to simpler dense models. Key considerations involve the stability of the MoE router, the impact of LoRA on different model components (router vs. experts), and the need for fine-grained evaluation. Users recommend strategies like freezing the router initially, tracking expert utilization per task, and being cautious with numerical stability in Mamba layers due to potential quirks with low-rank updates. Budget considerations for generating synthetic data are also highlighted.
*   **Emotion:** The tone is neutral and technical, reflecting a discussion among practitioners on model fine-tuning.
*   **Top 3 Points of View:**
    *   **Router Management is Key:** A primary concern is the MoE router's behavior. It's recommended to freeze the router in early fine-tuning stages to prevent destabilizing load balancing, and to only apply LoRA to expert FFNs and attention layers to ensure stable learning.
    *   **Fine-grained Evaluation is Crucial:** Aggregate evaluation metrics can be misleading. Users emphasize tracking expert utilization per capability or task, and creating separate evaluation slices for different skills to catch silent degradation or under-routing issues in specific tasks.
    *   **Hybrid Complexity and Budget:** The transition to a hybrid Mamba-MoE architecture introduces new complexities, particularly concerning numerical stability in Mamba layers with low-rank updates and the potential for recurrent state instability. Generating sufficient synthetic data for such models also carries a significant cost.

**[[P] Speculative Decoding Implementations: EAGLE-3, Medusa-1, PARD, Draft Models, N-gram and Suffix Decoding from scratch](https://www.reddit.com/r/MachineLearning/comments/1swfftl/speculative_decoding_implementations_eagle3/) (Score: 14)**
*   **Summary:** This post shares implementations of various speculative decoding techniques. The primary comment is a link to a related discussion, and another comment simply states "This is good," indicating a positive but brief reception.
*   **Emotion:** The overall emotion is positive, albeit with minimal discussion.
*   **Top 3 Points of View:**
    *   **Resource Sharing:** The post primarily serves as a resource for implementations.
    *   **Positive Reception:** A user briefly acknowledges the quality of the shared implementations.
    *   **Cross-referencing:** A linked discussion points to related content, broadening the scope of the resource.

**[[D] Submitting to top ML Conferences without Sharing code](https://www.reddit.com/r/MachineLearning/comments/1swtk3h/submitting_to_top_ml_conferences_without_sharing/) (Score: 13)**
*   **Summary:** This thread delves into the practice of withholding code during submissions to top ML conferences. Arguments against sharing code often cite concerns about ideas being stolen or code being copied, especially if the research is valuable. Counterarguments emphasize that reviewers often use code as a proxy for reproducibility and that withholding it can create skepticism. Some suggest that if code is not shared, providing exact configurations and evaluation protocols can aid reproduction, and that stating an intent to publicly share code after acceptance is viewed positively.
*   **Emotion:** The tone is neutral, reflecting a balanced debate on academic publishing ethics and practices.
*   **Top 3 Points of View:**
    *   **Protecting Valuable IP:** Some users believe that if their code contains valuable IP or unique implementations, it is better not to share it during the review process to prevent others from copying it.
    *   **Reproducibility and Reviewer Skepticism:** A significant concern is that withholding code can lead to reviewer skepticism, as code is often seen as a crucial element for verifying claims and ensuring reproducibility, especially for complex or novel methods.
    *   **Alternative Approaches to Sharing:** For those hesitant to share code, suggestions include providing detailed configuration, clear evaluation protocols, or stating an intention to release code publicly upon acceptance, which can mitigate some of the negative perceptions.

**[[D] What do reviewers actually mean when they say the paper sound more like a technical report?](https://www.reddit.com/r/MachineLearning/comments/1sx8xpa/what_do_reviewers_actually_mean_when_they_say_the/) (Score: 11)**
*   **Summary:** This thread unpacks the common reviewer comment that a paper sounds like a "technical report" rather than a research paper. The consensus is that it signifies a lack of novelty, a focus on describing experiments and results without a compelling scientific narrative or hypothesis, insufficient methodology for reproducibility, or a failure to clearly articulate the paper's contribution and its connection to the broader field. The distinction is drawn between detailing "what was done" versus presenting a "story" with a clear "why" that engages the reader.
*   **Emotion:** The tone is neutral and analytical, aimed at clarifying academic review feedback.
*   **Top 3 Points of View:**
    *   **Lack of Hypothesis and Scientific Narrative:** A technical report often details experiments and results without a clear hypothesis or a narrative that explains the "why" behind the research. A true research paper should present a compelling story about a problem, its importance, and the insights gained.
    *   **Insufficient Novelty and Depth:** Reviewers may perceive a paper as a technical report if it lacks significant novelty, provides only a description of work done without insightful benchmarking or discussion, or reads like an implementation/pipeline paper.
    *   **Focus on Description vs. Dissemination:** The fundamental difference lies in the goal: technical reports aim to describe actions, while research papers aim to disseminate a proposition and pique interest. If the contribution is hard to infer, it leans towards a technical report.

**[[D] Value of top conference workshop papers for PhD admissios](https://www.reddit.com/r/MachineLearning/comments/1swwsin/value_of_top_conference_workshop_papers_for_phd/) (Score: 9)**
*   **Summary:** This discussion examines the weight given to workshop papers from top conferences in PhD admissions. While not as strong as main conference papers, they are generally considered beneficial, especially for undergraduates, as they demonstrate the ability to complete a project end-to-end, write it up, and engage with the research community. Some users shared personal anecdotes of workshop papers contributing to their PhD acceptance. The value is seen as a "nice signal" that doesn't hurt but shouldn't necessarily be pursued at significant personal expense if main papers are already in progress.
*   **Emotion:** The tone is neutral and informative, offering guidance to prospective PhD students.
*   **Top 3 Points of View:**
    *   **Demonstrates Research Capability:** Workshop papers show an applicant can take a project from inception to publication, engage with the research community, and communicate findings, which is valuable for demonstrating research potential.
    *   **Complementary to Main Papers:** While not a substitute for major conference publications, workshop papers can serve as a beneficial addition, especially for undergraduates who may not yet have a primary paper.
    *   **Quantity and Alignment:** The quantity of peer-reviewed papers can be a factor, and workshops offer a way to increase one's publication record. Alignment with the target research area can also increase their impact.

**[[D] INT8 quantization gives me better accuracy than FP16 !](https://www.reddit.com/r/MachineLearning/comments/1sx35es/int8_quantization_gives_me_better_accuracy_than/) (Score: 5)**
*   **Summary:** A user reports that INT8 quantization yielded better accuracy than FP16, prompting a discussion about potential reasons. Suggestions include issues with FP16's limited exponent bits for small models, the possibility of experimental flaws, the type of data used (real vs. toy), specific task characteristics that might favor INT8, and whether certain layers (like norms) were treated differently during quantization. The idea of error cancellation is also briefly mentioned.
*   **Emotion:** The tone is neutral, focused on technical troubleshooting and understanding.
*   **Top 3 Points of View:**
    *   **FP16 Limitations and Alternatives:** FP16 can have issues with small models due to its limited exponent range, making bfloat16 a more appropriate alternative in such cases.
    *   **Experimental Rigor and Data:** The observed outcome might be due to experimental design flaws or the use of toy data. Running tests on real-world datasets and comparing against established results is recommended.
    *   **Quantization Method and Layer Specifics:** The accuracy difference could stem from how quantization was applied (e.g., data-aware vs. not, different settings) or if specific layers were treated differently between FP16 and INT8, which can impact performance.

**[[D] CVPR Workshop Decisions](https://www.reddit.com/r/MachineLearning/comments/1sx6vlm/cvpr_workshop_decisions_d/) (Score: 4)**
*   **Summary:** A user reports submitting a paper to a CVPR workshop, that the notification deadline has passed, and they have not yet received any reviews.
*   **Emotion:** The tone is neutral, stating a factual observation about a submission status.
*   **Top 3 Points of View:**
    *   **Delayed Notifications:** The primary point is that notification deadlines for workshop submissions may pass without immediate communication.
    *   **Lack of Reviews:** The user has not seen any reviews for their submission.
    *   **Uncertainty:** The situation indicates an ongoing process with no clear outcome yet.

**[[D] Three limitations I keep hitting with retrieval-augmented generation in production and I'm running out of ideas](https://www.reddit.com/r/MachineLearning/comments/1swxx1v/three_limitations_i_keep_hitting_with/) (Score: 4)**
*   **Summary:** This thread addresses recurring issues in production Retrieval-Augmented Generation (RAG) systems, including query decomposition, handling "negative knowledge" (when no relevant information is found), and timeline accuracy. Users suggest that these problems often stem from a weak underlying LLM. Proposed solutions involve better query decomposition (e.g., using metadata), separate classification steps to handle negative knowledge, and explicit date-bucketed retrieval for timeline accuracy. The effectiveness of different reranker setups is also mentioned.
*   **Emotion:** The tone is neutral and problem-solving oriented.
*   **Top 3 Points of View:**
    *   **Weak LLM as Root Cause:** Several users posit that the limitations are often symptoms of a general LLM that is not strong enough to decompose complex queries, interpret retrieved chunks accurately, or manage temporal information effectively.
    *   **Improved Retrieval Strategies:** Solutions proposed include pre-passing queries for decomposition, using metadata to guide retrieval, employing separate classification steps to identify irrelevant chunks, and using coverage map indexes to provide confident "no answer" responses.
    *   **Handling Temporal Data:** For timeline accuracy, specific strategies like date-bucketed retrieval and fetching pre/post data separately are suggested to enforce comparative structures.

**[[R] Building an operational tool for heavy industry — Seeking "real world" data and site reality](https://www.reddit.com/r/MachineLearning/comments/1swsshs/building_an_operational_tool_for_heavy_industry/) (Score: 3)**
*   **Summary:** A user with experience in building data pipelines for logistics and fleet operations offers their expertise to help with the data ingestion side of an operational tool for heavy industry. They highlight the common gap between board-level perceptions and on-site realities and praise the poster's initiative to consult with operators first.
*   **Emotion:** The tone is neutral and helpful, with a touch of positive reinforcement for the poster's approach.
*   **Top 3 Points of View:**
    *   **Data Ingestion Expertise:** The commenter offers specialized skills in building data pipelines to handle messy logs, sensors, and manual entries.
    *   **Understanding Industry Gaps:** They acknowledge the real disparity between what management sees and what happens in practice on the ground.
    *   **Importance of Operator Consultation:** The commenter strongly endorses talking to end-users and operators as a crucial first step, noting that skipping this often leads to building ineffective tools.
