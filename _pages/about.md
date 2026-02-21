---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am Yuheng Ji (冀昱衡), a lyric poet, and a PhD candidate at the [Institute of Automation, Chinese Academy of Sciences (CASIA)](http://www.ia.cas.cn/). I am supervised by Prof. [Xiaolong Zheng](https://people.ucas.edu.cn/~xlzheng). My research interests include embodied AI and foundation models. 

I am also open to collaborative opportunities and research partnerships, feel free to email me: jiyuheng2023@ia.ac.cn.

<p align="center">
  <a href="mailto:jiyuheng2023@ia.ac.cn">Email</a> &nbsp;/&nbsp;
  <a href="https://scholar.google.com/citations?user=X4ILYUQAAAAJ&hl=en/">Google Scholar</a> &nbsp;/&nbsp;
  <a href="data/小岛集.pdf">Poetry Anthology</a>
</p>

<span class='anchor' id='news'></span>

# 🔥 News

- *2026.02*: 🎉 Three papers were accepted by **CVPR 2026**! Congratulations to all collaborators!
- *2026.01*: 🔥 Released [RoboBrain 2.5](https://github.com/FlagOpen/RoboBrain2.5) (core contributor).
- *2025.10*: 🔥 Released more advanced [RoboOS-NeXT](https://arxiv.org/abs/2510.26536) (first author).
- *2025.09*: 🎉 [Reason-RFT](https://tanhuajie.github.io/ReasonRFT/) accepted to **NeurIPS 2025** (first author).
- *2025.06*: 🎉 Released [RoboBrain 2.0](https://arxiv.org/abs/2507.02029) and [RoboOS](https://flagopen.github.io/RoboOS/) in **BAAI Conference 2025** (first author, core contributor).
- *2025.04*: 🌍 [RoboBrain 1.0](http://arxiv.org/abs/2502.21257/) selected for **CVPR 2025**’s official [Embodied AI Trends Commentary](https://cvpr.thecvf.com/Conferences/2025/News/AI_Enhanced_Robotics).
- *2025.02*: 🎉 [RoboBrain 1.0](http://arxiv.org/abs/2502.21257/) accepted to **CVPR 2025** (first author).

<span class='anchor' id='research-framework'></span>

# 🧭 Research Framework

My long-term aspiration is to build embodied agents with strong real-world generalization, so they can become productive forces in society and benefit all people equitably.  
The roadmap is a tightly coupled loop: **Evaluation & Analysis** informs the design of both methods and models; **Method Development** empowers **Model Construction**; model behavior and performance, in turn, validate and refine methods; together, methods and models support **System Expansion** toward scalable multi-agent intelligence.

![Research Framework](images/research_road.png)

### 1) Evaluation & Mechanism Analysis
This direction focuses on diagnosing what current models can and cannot do under real-world complexity, including spatial perception, temporal reasoning, and robustness under distribution shifts. The goal is to provide reliable evidence and design principles for downstream methods and models.

### 2) Method Development
This direction develops training and adaptation methods that improve reasoning quality and action reliability, especially for long-horizon embodied tasks. Typical themes include reinforcement learning, process-level rewards, and stronger intermediate reasoning representations.

### 3) Model Construction
This direction builds embodied foundation models that unify perception, reasoning, and planning. A key target is to obtain robust spatial-temporal cognition and practical decision-making ability in cluttered, dynamic, and multi-step environments.

### 4) System Expansion
This direction extends single-agent intelligence to scalable systems, including memory-centric architectures, multi-agent collaboration, and lifelong operation. The objective is to support deployment-ready embodied systems rather than isolated benchmarks.

<span class='anchor' id='publications'></span>

# 📝 Publications

Use the left-to-right menu below to browse detailed publications by category.

<div class="pub-browser">
<div class="pub-tabs" role="tablist" aria-label="Research modules">
  <button class="pub-tab is-active" type="button" data-cat="model">Model Construction</button>
  <button class="pub-tab" type="button" data-cat="method">Method Development</button>
  <button class="pub-tab" type="button" data-cat="evaluation">Evaluation & Mechanism Analysis</button>
  <button class="pub-tab" type="button" data-cat="system">System Expansion</button>
  <button class="pub-tab" type="button" data-cat="survey">Survey</button>
  <button class="pub-tab" type="button" data-cat="others">Others</button>
</div>

<div id="pub-list">

<div class='paper-box module-note' data-cat='model' data-order='5'>
<div class='paper-box-text' markdown="1">

In the **Model Construction** module, we were among the early works (CVPR 2025) to formulate embodied foundation models under a Brain+Cerebellum hierarchical architecture. The core distinction between embodied and general foundation models lies in whether abstract human intents (e.g., "I am thirsty") can be transformed into concrete control signals, such as subtask planning, affordance grounding, trajectory generation, and point-level action targets. As a core contributor, I have been deeply involved in developing the RoboBrain series.

</div>
</div>

<div class='paper-box' data-cat='model' data-order='10'><div class='paper-box-image'><div><div class="badge">Technical Report 2026</div><img src='images/robobrain25.png' alt="RoboBrain 2.5" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboBrain 2.5: Depth in Sight, Time in Mind.](https://arxiv.org/abs/2601.14352)

BAAI RoboBrain Team

<span style="color: red;">Core Contributor</span>, Technical Report 2026

[**Project**](https://superrobobrain.github.io/) <strong>|</strong>  [**Paper**](https://arxiv.org/abs/2601.14352) <strong>|</strong> [**Code**](https://github.com/FlagOpen/RoboBrain2.5) ![](https://img.shields.io/github/stars/FlagOpen/RoboBrain2.5) <strong>|</strong> [**Checkpoints**](https://huggingface.co/collections/BAAI/robobrain25)

RoboBrain 2.5 upgrades embodied intelligence along two key axes: depth-aware 3D spatial reasoning and dense temporal value estimation. It predicts physically grounded 3D manipulation traces and step-aware progress signals across viewpoints, improving fine-grained manipulation planning and execution feedback.

</div>
</div>

<div class='paper-box' data-cat='model' data-order='20'><div class='paper-box-image'><div><div class="badge">Technical Report 2025</div><img src='images/robobrain2.png' alt="RoboBrain 2.0" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboBrain 2.0: See Better. Think Harder. Do Smarter.](https://arxiv.org/abs/2507.02029)

BAAI RoboBrain Team

<span style="color: red;">First Author, Core Contributor</span>, Technical Report 2025

[**Project**](https://superrobobrain.github.io/robobrainv2/index.html) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2507.02029) <strong>|</strong> [**Code**](https://github.com/FlagOpen/RoboBrain2.0) ![](https://img.shields.io/github/stars/FlagOpen/RoboBrain2.0) <strong>|</strong> [**Checkpoints**](https://huggingface.co/collections/BAAI/robobrain20-6841eeb1df55c207a4ea0036)

RoboBrain 2.0 is an embodied vision-language foundation model family with 7B and 32B variants, designed to unify perception, reasoning, and planning for complex physical-world tasks. The 32B model reports leading performance on both spatial and temporal embodied benchmarks, with strong capabilities in affordance prediction, spatial referring, trajectory forecasting, closed-loop interaction, and multi-agent long-horizon planning.

</div>
</div>

<div class='paper-box' data-cat='model' data-order='30'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/robobrain.png' alt="RoboBrain" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete](https://arxiv.org/abs/2502.21257)

**Yuheng Ji\***, Huajie Tan\*, Jiayu Shi\*, Xiaoshuai Hao\*, Yuan Zhang, Hengyuan Zhang, Pengwei Wang, Mengdi Zhao, Yao Mu, Pengju An, Xinda Xue, Qinghang Su, Huaihai Lyu, Xiaolong Zheng, Jiaming Liu, Zhongyuan Wang, Shanghang Zhang

<span style="color: red;">First Author, CVPR 2025</span>

[**Project**](https://superrobobrain.github.io/robobrainv1/index.html) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2502.21257) <strong>|</strong> [**Code**](https://github.com/FlagOpen/RoboBrain) ![](https://img.shields.io/github/stars/FlagOpen/RoboBrain) <strong>|</strong> [**Checkpoints**](https://huggingface.co/BAAI/RoboBrain) <strong>|</strong> [**Datasets**](https://huggingface.co/datasets/BAAI/ShareRobot)

We developed **RoboBrain**, a VLM-based model that combines robotic and general multi-modal data, utilizes a multi-stage training strategy, and incorporates long videos and high-resolution images to improve its robotic manipulation capabilities. Extensive experiments demonstrate that RoboBrain achieves SOTA performance across various robotic tasks, highlighting its potential to advance robotic brain capabilities.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='10'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/reason-rft.png' alt="Reason-RFT" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Reason-RFT: Reinforcement Fine-Tuning for Visual Reasoning of Vision Language Models](https://tanhuajie.github.io/ReasonRFT/)

Huajie Tan\*, **Yuheng Ji\***, Xiaoshuai Hao\*, Minglan Lin, Pengwei Wang, Shanghang Zhang

<span style="color: red;">First Author, NeurIPS 2025</span>

[**Project**](https://tanhuajie.github.io/ReasonRFT/) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2503.20752) <strong>|</strong> [**Code**](https://github.com/tanhuajie/Reason-RFT) <strong>|</strong> [**Checkpoints**](https://github.com/tanhuajie/Reason-RFT?tab=readme-ov-file#--model-zoo) <strong>|</strong> [**Datasets**](https://huggingface.co/datasets/tanhuajie2001/Reason-RFT-CoT-Dataset)

We developed **Reason-RFT**, a reinforcement fine-tuning framework that enhances visual reasoning capabilities in vision-language models. Reason-RFT employs a two-phase training strategy: (1) SFT with curated CoT data to activate reasoning potential, followed by (2) GRPO-based reinforcement learning to generate diverse reasoning-response pairs.

</div>
</div>

<div class='paper-box' data-cat='system'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/RoboOS.png' alt="RoboOS" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration](https://arxiv.org/abs/2510.26536)

Huajie Tan\*, **Yuheng Ji\***, Cheng Chi\*, Xiansheng Chen\*, Zhongxia Zhao, Xiaoshuai Hao, Yaoxu Lyu, Mingyu Cao, Junkai Zhao, Huaihai Lyu, Enshen Zhou, Ning Chen, Yankai Fu, Cheng Peng, Wei Guo, Dong Liang, Zhuo Chen, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang

First Author, ArXiv 2025

[**Project**](https://flagopen.github.io/RoboOS/) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2510.26536) <strong>|</strong> [**Code**](https://github.com/FlagOpen/RoboOS) ![](https://img.shields.io/github/stars/FlagOpen/RoboOS)

We present **RoboOS**, a unified memory-based framework for multi-robot collaboration. At its core, the Spatio-Temporal–Embodiment Memory (STEM) integrates spatial, temporal, and embodiment information to support long-horizon learning, heterogeneous coordination, and fault recovery. Experiments in diverse tasks show RoboOS enables lifelong, scalable, and robust collaboration.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='20'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/robodopamine.png' alt="Robo-Dopamine" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation](https://arxiv.org/abs/2512.23703)

Huajie Tan\*, Sixiang Chen\*, Yijie Xu\*, Zixiao Wang, **Yuheng Ji**, Cheng Chi, Yaoxu Lyu, Zhongxia Zhao, Xiansheng Chen, Peterson Co, Shaoxuan Xie, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang

<span style="color: red;">CVPR 2026</span>

[**Project**](https://robo-dopamine.github.io/) <strong>|</strong>  [**Paper**](https://arxiv.org/abs/2512.23703) <strong>|</strong> [**Code**](https://github.com/FlagOpen/Robo-Dopamine) ![](https://img.shields.io/github/stars/FlagOpen/Robo-Dopamine) <strong>|</strong>  [**Checkpoints**](https://huggingface.co/collections/tanhuajie2001/robo-dopamine)

Robo-Dopamine introduces a step-aware multi-view reward modeling framework (Dopamine-Reward) and a policy-invariant shaping strategy (Dopamine-RL) for robotic RL. The method improves reward assessment quality and substantially boosts online policy learning efficiency on both simulated and real-world manipulation tasks.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='30'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/actionsketcher.png' alt="Action-Sketcher" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Action-Sketcher: From Reasoning to Action via Visual Sketches for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.01618)

Huajie Tan\*, Peterson Co\*, Yijie Xu\*, Shanyu Rong, **Yuheng Ji**, Cheng Chi, Xiansheng Chen, Qiongyu Zhang, Zhongxia Zhao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang

<span style="color: red;">CVPR 2026</span>

[**Project**](https://action-sketcher.github.io/) <strong>|</strong>  [**Paper**](https://arxiv.org/abs/2601.01618) <strong>|</strong> [**Code**](https://github.com/FlagOpen/Action-Sketcher) ![](https://img.shields.io/github/stars/FlagOpen/Action-Sketcher)

Action-Sketcher proposes a See-Think-Sketch-Act loop that inserts editable visual sketches as an intermediate representation between language reasoning and robot actions. This design improves grounding, long-horizon robustness, and interpretability in cluttered and dynamic manipulation environments.

</div>
</div>

<div class='paper-box' data-cat='evaluation'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/visualtrans.png' alt="VisualTrans" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VisualTrans: A Benchmark for Real-World Visual Transformation Reasoning](http://arxiv.org/abs/2508.04043)

**Yuheng Ji\***, Yipu Wang\*, Yuyang Liu, Xiaoshuai Hao, Yue Liu, Yuting Zhao, Huaihai Lyu, Xiaolong Zheng

First Author, ArXiv 2025

[**Paper**](http://arxiv.org/abs/2508.04043) <strong>|</strong> [**Code**](https://github.com/WangYipu2002/VisualTrans) <strong>|</strong> [**Datasets**](https://github.com/WangYipu2002/VisualTrans)

VisualTrans is the first real-world benchmark for Visual Transformation Reasoning (VTR), evaluating spatial, procedural and quantitative reasoning across 12 human-object interaction tasks. While current models perform well on static tasks, they show significant limitations in dynamic, multi-step reasoning, revealing critical gaps in temporal and causal understanding for intelligent systems.

</div>
</div>

<div class='paper-box' data-cat='evaluation'><div class='paper-box-image'><div><div class="badge">NeurIPS MATH-AI Workshop 2025</div><img src='images/mathsticks.png' alt="MathSticks" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MathSticks: A Benchmark for Visual Symbolic Compositional Reasoning with Matchstick Puzzles](http://arxiv.org/abs/2510.00483)

**Yuheng Ji\***, Huajie Tan\*, Cheng Chi\*, Yijie Xu, Yuting Zhao, Enshen Zhou, Huaihai Lyu, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang, Xiaolong Zheng

<span style="color: red;">First Author, NeurIPS MATH-AI Workshop 2025</span>

[**Paper**](http://arxiv.org/abs/2510.00483) <strong>|</strong> [**Code**](https://github.com/Yuheng2000/MathSticks) <strong>|</strong> [**Datasets**](https://huggingface.co/datasets/yuheng2000/MathSticks)

MathSticks is a benchmark for Visual Symbolic Compositional Reasoning (VSCR) that unifies visual perception, symbolic manipulation, and arithmetic consistency. Each task presents an incorrect matchstick equation in a seven-segment style. The goal is to move exactly one or two sticks—under strict stick-conservation and digit-legibility constraints—to make the equation mathematically correct.

</div>
</div>

<div class='paper-box' data-cat='survey'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/manipulation_survey.png' alt="Manipulation Survey" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey](https://arxiv.org/abs/2510.10903)

Shuanghao Bai, Wenxuan Song, Jiayi Chen, **Yuheng Ji**, Zhide Zhong, Jin Ynag, Han Zhao, Wanqi Zhou, Wei Zhao, Zhe Li, Pengxiang Ding, Cheng Chi, Haoang Li, Chang Xu, Xiaolong Zheng, Donglin Wang, Shanghang Zhang, Badong Chen

ArXiv 2025

[**Paper**](https://arxiv.org/abs/2510.10903) <strong>|</strong> [**Repo**](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)

Synthesizing over 1200+ publications, this survey restructures the landscape of robotic manipulation with a unified taxonomy for planning and control. We also provide the first systematic dissection of the key bottlenecks—data, utilization, and generalization—poised to define the next era of progress.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='50'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/ManipLVM.png' alt="ManipLVM-R1" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ManipLVM-R1: Reinforcement Learning for Reasoning in Embodied Manipulation with Large Vision-Language Models](https://arxiv.org/pdf/2505.16517)

Zirui Song\*, Guangxian Ouyang\*, Mingzhe Li, **Yuheng Ji**, Chenxi Wang, Zixiang Xu, Zeyu Zhang, Xiaoqing Zhang, Qian Jiang, Zhenhao Chen, Zhongzhi Li, Rui Yan, Xiuying Chen

<span style="color: red;">AAAI 2026</span>

[**Paper**](https://arxiv.org/pdf/2505.16517)

VLMs enhance robotic manipulation but rely on costly annotated data, limiting OOD adaptability. We propose ManipLVM-R1, a RL framework with verifiable rewards (RLVR), replacing supervision to optimize task outcomes for better generalization. Two rule-based rewards drive physical reasoning, achieving strong performance on fewer data and OOD scenarios.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='60'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='images/egoprompt.png' alt="EgoPrompt" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EgoPrompt: Prompt Learning for Egocentric Action Recognition](https://arxiv.org/abs/2508.03266)

Huaihai Lyu, Chaofan Chen, **Yuheng Ji**, Changsheng Xu

<span style="color: red;">ACM MM 2025</span>

[**Paper**](https://arxiv.org/abs/2508.03266)

EgoPrompt is a prompt-learning framework for egocentric action recognition that jointly models verbs and nouns by capturing their semantic relationships. It introduces a Unified Prompt Pool and a Diverse Pool Criteria to encourage rich, disentangled representations. EgoPrompt achieves state-of-the-art performance on Ego4D, EPIC-Kitchens, and EGTEA across various generalization benchmarks.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='80'><div class='paper-box-image'><div><div class="badge">AAAI 2025 (Oral)</div><img src='images/MinGRE.jpg' alt="MinGRE" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Alleviating Performance Disparity in Adversarial Spatiotemporal Graph Learning under Zero-inflated Distribution](https://arxiv.org/pdf/2404.13425)

Songran Bai, **Yuheng Ji**, Yue Liu, Xingwei Zhang, Xiaolong Zheng, Daniel Dajun Zeng

<span style="color: red;">AAAI 2025 (Oral)</span>

[**Paper**](https://arxiv.org/pdf/2404.13425)

Spatiotemporal graph learning under zero-inflated distribution is vital for urban risk management but is susceptible to adversarial attacks. Traditional adversarial training increases performance disparities between classes. We propose the MinGRE framework to reduce these disparities and enhance robustness.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='20'><div class='paper-box-image'><div><div class="badge">ICMR 2025</div><img src='images/advlora.jpg' alt="AdvLoRA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enhancing Adversarial Robustness of Vision-Language Models through Low-Rank Adaptation](https://arxiv.org/pdf/2404.13425)

**Yuheng Ji\***, Yue Liu\*, Zhicheng Zhang, Zhao Zhang, Yuting Zhao, Xiaoshuai Hao, Gang Zhou, Xingwei Zhang, Xiaolong Zheng

<span style="color: red;">First Author, ICMR 2025</span>

[**Paper**](https://arxiv.org/pdf/2404.13425)

We propose a parameter-efficient adversarial adaptation method named AdvLoRA by low-rank adaptation to improve the robustness of vision-language models.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='30'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='images/FastRSR.jpg' alt="FastRSR" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FastRSR: Efficient and Accurate Road Surface Reconstruction from Bird's Eye View](https://arxiv.org/abs/2504.09535)

Yuting Zhao\*, **Yuheng Ji\***, Xiaoshuai Hao, Shuxiao Li

<span style="color: red;">First Author, ACM MM 2025</span>

[**Paper**](https://arxiv.org/abs/2504.09535)

Road surface reconstruction is crucial for autonomous driving, enabling the understanding of road surface conditions. We present two BEV-based RSR models: FastRSR-mono and FastRSR-stereo, offering superior efficiency and accuracy across elevation error and processing speed.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='60'><div class='paper-box-image'><div><div class="badge">IROS 2025 (Oral)</div><img src='images/robomap.png' alt="Robust HD Map" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[What Really Matters for Robust Multi-Sensor HD Map Construction?](https://arxiv.org/abs/2501.01037)

Xiaoshuai Hao, Yuting Zhao, **Yuheng Ji**, Luanyuan Dai, Shuai Cheng, Rong Yin

<span style="color: red;">IROS 2025 (Oral)</span>

[**Paper**](https://arxiv.org/abs/2501.01037)

This paper enhances HD map construction robustness via data augmentation, a new fusion module, and modality dropout. It improves performance under sensor corruptions and achieves SOTA accuracy on NuScenes.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='70'><div class='paper-box-image'><div><div class="badge">ICME 2025 (Oral)</div><img src='images/msc-bench.png' alt="MSC-Bench" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MSC-Bench: Benchmarking and Analyzing Multi-Sensor Corruption for Driving Perception](https://msc-bench.github.io/)

Xiaoshuai Hao, Guanqun Liu, Yuting Zhao, **Yuheng Ji**, Mengchuan Wei, Haimei Zhao, Lingdong Kong, Rong Yin, Yu Liu

<span style="color: red;">ICME 2025 (Oral)</span>

[**Project**](https://msc-bench.github.io/) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2501.01037)

This work introduces the Multi-Sensor Corruption Benchmark (MSC-Bench), the first comprehensive benchmark aimed at evaluating the robustness of multi-sensor autonomous driving perception models against various sensor corruptions.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='40'><div class='paper-box-image'><div><div class="badge">C2 China 2023</div><img src='images/CCMH.jpg' alt="CCMH" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Hash Subspace from Large-Scale Multi-modal Pre-Training: A CLIP-Based Cross-modal Hashing Framework](https://link.springer.com/chapter/10.1007/978-981-99-9021-4_48)

**Yuheng Ji\***, Xingwei Zhang\*, Gang Zhou, Xiaolong Zheng, Daniel Dajun Zeng

<span style="color: red;">First Author, The 11st C2 China 2023 (Outstanding Paper Award)</span>


[**Paper**](https://link.springer.com/chapter/10.1007/978-981-99-9021-4_48)

We propose a cross-modal hashing framework called CCMH (CLIP-based Cross-Modal Hashing), which facilitates the transferability of a well-trained real-value semantic subspace to a hash semantic subspace.

</div>
</div>

<div class='paper-box' data-cat='survey'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/foundation_model_embodied.png' alt="Embodied Robot Manipulation Survey" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Embodied Robot Manipulation in the Era of Foundation Models: Planning and Learning Perspectives](https://arxiv.org/abs/2512.22983)

Shuanghao Bai, Wenxuan Song, Jiayi Chen, **Yuheng Ji**, Zhide Zhong, Jin Yang, Han Zhao, Wanqi Zhou, Zhe Li, Pengxiang Ding, Cheng Chi, Chang Xu, Xiaolong Zheng, Donglin Wang, Haoang Li, Shanghang Zhang, Badong Chen

ArXiv 2025

[**Paper**](https://arxiv.org/abs/2512.22983)

This survey revisits robot manipulation in the foundation-model era through a unified two-level abstraction: high-level planning and low-level control. It organizes algorithmic design choices, summarizes representative methods, and highlights open challenges in scalability, data efficiency, multimodal physical interaction, and safety.

</div>
</div>

<div class='paper-box' data-cat='evaluation'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/CroPond.png' alt="Cross-View Point Correspondence" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Towards Cross-View Point Correspondence in Vision-Language Models](https://arxiv.org/abs/2512.04686)

Yipu Wang\*, **Yuheng Ji\***, Yuyang Liu, Enshen Zhou, Ziqiang Yang, Yuxuan Tian, Ziheng Qin, Yue Liu, Huajie Tan, Cheng Chi, Zhiyuan Ma, Daniel Dajun Zeng, Xiaolong Zheng

First Author, ArXiv 2025

[**Project**](https://github.com/WangYipu2002/CrossPoint) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2512.04686)

This work introduces the Cross-View Point Correspondence task and CrossPoint-Bench to evaluate point-level cross-view grounding in VLMs. It further proposes CrossPoint-378K and CroPond to improve fine-grained correspondence accuracy for embodied affordance-centric interaction.

</div>
</div>

<div class='paper-box' data-cat='method' data-order='40'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/robotracer.png' alt="RoboTracer" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboTracer: Mastering Spatial Trace with Reasoning in Vision-Language Models for Robotics](https://arxiv.org/abs/2512.13660)

Enshen Zhou, Cheng Chi, Yibo Li, Jingkun An, Jiayuan Zhang, Shanyu Rong, Yi Han, **Yuheng Ji**, Mengzhen Liu, Pengwei Wang, Zhongyuan Wang, Lu Sheng, Shanghang Zhang

ArXiv 2025

[**Project**](https://zhoues.github.io/RoboTracer/) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2512.13660)

RoboTracer targets metric-grounded multi-step spatial tracing for robotics by combining 3D-aware supervised fine-tuning with reinforcement fine-tuning under metric-sensitive process rewards. It improves spatial referring, measuring, and long-horizon trace generation in real-world embodied settings.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='50'><div class='paper-box-image'><div><div class="badge">ArXiv 2025</div><img src='images/robomirror.png' alt="RoboMirror" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion](https://arxiv.org/abs/2512.23649)

Zhe Li, Cheng Chi, Boan Zhu, Yangyang Wei, Shuanghao Bai, **Yuheng Ji**, Yibo Peng, Tao Huang, Pengwei Wang, Zhongyuan Wang, S.-H. Gary Chan, Chang Xu, Shanghang Zhang

ArXiv 2025

[**Paper**](https://arxiv.org/abs/2512.23649)

RoboMirror proposes a retargeting-free video-to-humanoid-locomotion pipeline under the principle of "understand before imitate". By extracting visual motion intent from egocentric/third-person videos and conditioning diffusion policies, it narrows the gap between visual understanding and control.

</div>
</div>

<div class='paper-box' data-cat='others' data-order='10'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/GAPL.png' alt="GAPL" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Scaling Up AI-Generated Image Detection via Generator-Aware Prototypes](https://arxiv.org/abs/2512.12982)

Ziheng Qin\*, **Yuheng Ji\***, Renshuai Tao, Yuxuan Tian, Yuyang Liu, Yipu Wang, Xiaolong Zheng

<span style="color: red;">First Author, CVPR 2026</span>

[**Code**](https://github.com/UltraCapture/GAPL) <strong>|</strong> [**Paper**](https://arxiv.org/abs/2512.12982)

This work studies the scaling challenge of universal AI-generated image detection and proposes Generator-Aware Prototype Learning (GAPL). By combining canonical forgery prototypes with a two-stage low-rank adaptation strategy, it improves robustness across diverse generators.

</div>
</div>

</div>
</div>
<script>
  (function () {
    var root = document.querySelector('.pub-browser');
    if (!root) return;
    var tabs = root.querySelectorAll('.pub-tab');
    var cards = root.querySelectorAll('.paper-box[data-cat]');
    function activate(cat) {
      tabs.forEach(function (t) {
        t.classList.toggle('is-active', t.getAttribute('data-cat') === cat);
      });
      var visible = [];
      cards.forEach(function (card) {
        if (card.getAttribute('data-cat') === cat) {
          card.style.display = 'flex';
          visible.push(card);
        } else {
          card.style.display = 'none';
        }
      });
      visible.sort(function (a, b) {
        var ao = parseInt(a.getAttribute('data-order') || '9999', 10);
        var bo = parseInt(b.getAttribute('data-order') || '9999', 10);
        return ao - bo;
      });
      var container = root.querySelector('#pub-list');
      visible.forEach(function (card) {
        container.appendChild(card);
      });
    }
    tabs.forEach(function (tab) {
      tab.addEventListener('mouseenter', function () {
        activate(tab.getAttribute('data-cat'));
      });
      tab.addEventListener('focus', function () {
        activate(tab.getAttribute('data-cat'));
      });
      tab.addEventListener('click', function () {
        activate(tab.getAttribute('data-cat'));
      });
    });
    activate('model');
  })();
</script>

<span class='anchor' id='experience'></span>

# 💼 Experience

- PhD candidate student @ [Chinese Academy of Sciences, Institute of Automation (CASIA)](http://www.ia.cas.cn/), supervised by Prof. [Xiaolong Zheng](https://people.ucas.edu.cn/~xlzheng)
- Visiting student @ [Beijing Academy of Artificial Intelligence (BAAI)](https://www.baai.ac.cn/), supervised by Prof. [Shanghang Zhang](https://scholar.google.com/citations?user=voqw10cAAAAJ&hl=en), Dr. [Pengwei Wang](https://scholar.google.com/citations?user=2xR6P5AAAAAJ&hl=zh-CN&oi=ao) and Dr. [Cheng Chi](https://scholar.google.com/citations?user=wWGpskcAAAAJ&hl=en&oi=ao)
- Remote visiting student @ [National University of Singapore (NUS)](https://www.nus.edu.sg/), working with Ph.D. [Yue Liu](https://yueliu1999.github.io/)
- Bachelor of engineering @ [Northeastern University](http://english.neu.edu.cn/), supervised by Prof. Miao Fang

<span class='anchor' id='service'></span>

# 🤝 Services

- Reviewer for CVPR, ICLR, ICML, ICMR, ICME, AAAI

<span class='anchor' id='awards'></span>

# 🏆 Awards

- [2025] China National Scholarship for Master's Degree Students, National Award
- [2024] Merit Student, UCAS, School Award
- [2023] Outstanding Graduates, Provincial Award
- [2022] Recommendation for admission to CASIA
- [2022] Merit Student, Provincial Award
- [2022] China National Scholarship for Undergraduate Student, National Award
- [2021] China National Scholarship for Undergraduate Student, National Award
- [2020] China National Scholarship for Undergraduate Student, National Award
- [2019-2023] Scholarships, School Award

<span class='anchor' id='others'></span>

# 📎 Others

- [2024] 冀昱衡, 张曌, 郑晓龙, "大模型微调中的低秩性," 中国指挥与控制学会通讯 55 (1), 44-49.
- [2023] 冀昱衡, 张兴伟, 郑晓龙, "基于多模态预训练的跨模态检索算法研究," 中国指挥与控制学会通讯 46 (4), 10-16.
- [2023] 一种基于多模态预训练的跨模态哈希检索系统，发明专利，第一发明人
- [2023] 一种基于图神经网络的信用卡欺诈检测系统，发明专利，第一发明人
- [2023] 一种针对检索模型的在线隐私保护系统，发明专利，第二发明人
- [2022] 一种基于新闻主题句的文本情感分类系统，发明专利，第二发明人

<span class='anchor' id='projects'></span>

# 📌 Participation in Research Projects

在攻读硕博期间参与了以下项目研究，主要负责项目中跨模态信息语义融合与理解等专题研究工作：

- 新技术驱动的复杂社会系统管理, 国家杰出青年科学基金项目
- 基于多模态数据融合的智能社会风险预警研究, 国家自然科学基金重点项目
- 跨模态多语言大数据驱动的社会风险感知与理解, 2030—“新一代人工智能”重大项目
