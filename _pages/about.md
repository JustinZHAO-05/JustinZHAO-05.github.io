---
permalink: /
title: "Yanzhe (Justin) Zhao"
subtitle: "Neuro-AI × Robotics & Control — brain-inspired intelligence for embodied agents"
description: "B.Eng. (Elite Honors Cohort), School of Future Technology, Tianjin University"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---


### Hi — I’m **Yanzhe (Justin) Zhao** (赵彦喆)

**B.Eng. (Elite Honors Cohort), School of Future Technology, Tianjin University.**  
I build **brain-inspired AI** for **embodied robots**, informed by neural and cognitive mechanisms.

**Research interests**
- **Neural learning rules** — biologically plausible credit assignment beyond backprop (*modulatory signals, local plasticity*).
- **Data/compute-efficient decision making** — brain-inspired world models & control for **zero/low-shot** transfer.
- **Embodied intelligence** — morphology + **optimal/safe control**; **DRL** for nonholonomic navigation in **narrow dead-ends**.

---

## News
- **2025-12-12 → 14** — *Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning* **accepted** at **CSAI 2025 (poster), Beijing**. [[PDF]](#) · [[Poster]](#) · [[Code]](https://github.com/JustinZHAO-05/cisDRL-RobotNav)
- **Ongoing** — *From SE(2) Hamilton Fast Marching to Mapless Control: Safe Expert-Guided TD3 for Narrow Dead-End Escape* (HFM reward shaping; expert-guided off/online RL). [[Preprint soon]](#)
- **Learning now** — UW **Computational Neuroscience**; Stanford **Machine Learning** & **Deep Learning** (certificate tracks).
- **Seeking** — **2026 Summer Research** in **Neuro-AI / Robotics & Control**.

---

## Publications & Preprints

**Conference**
- **Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning** (co-first).  
  *CSAI 2025 (poster).*  
  *Batched Gazebo maps, SAC policy, curriculum/evaluation pipeline.*  
  [[PDF]](#) · [[Poster]](#) · [[Code]](https://github.com/JustinZHAO-05/cisDRL-RobotNav) · [[BibTeX]](#bibtex-nondeadend)

<details id="bibtex-nondeadend">
<summary>BibTeX</summary>

```bibtex
@misc{denghan_nonholonomic_2025,
  title        = {Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning},
  author       = {Xiong, Denghan and Zhao, Yanzhe and Chen, Yutong and Wang, Zichun},
  year         = {2025},
  month        = nov,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17741676},
  url          = {https://doi.org/10.5281/zenodo.17741676},
  note         = {Preprint, accepted poster at CSAI 2025}
}
```

</details>

**Preprint (in preparation)**
- **From SE(2) Hamilton Fast Marching to Mapless Control: Safe Expert-Guided TD3 for Narrow Dead-End Escape**.  
  *SE(2) HFM fields for reward shaping; safe action envelopes; TD3; mapless deployment; ablations.*  
  [[Preprint soon]](#) · [[Code soon]](#)

---

## Selected Projects
*(Each item lists: Problem → Method → My role → Artifacts)*

**Eight-Cable-Driven Parallel Robot** — full-stack mechanism & control  
**Problem.** High-DOF cable robot with elasticity/coupling.  
**Method.** Kinematics/dynamics modeling; motor drivers; embedded control; CAD.  
**My role.** Built end-to-end system (SolidWorks, MATLAB, MCU), repeated demos.  
**Artifacts.** [[Code]](https://github.com/JustinZHAO-05/Eight-Cable-Driven-Parallel-Robot) · [[Docs-CN]](#) · [[Video]](#)

**Dead-End DRL Navigation** *(CSAI engineering)*  
**Problem.** Escape from narrow dead-end layouts with nonholonomic robot.  
**Method.** SAC; **batched** Gazebo map generator; curriculum + eval.  
**My role.** Problem formulation; training/eval pipeline; poster.  
**Artifacts.** [[Code]](https://github.com/JustinZHAO-05/cisDRL-RobotNav) · [[Video]](#)

**Safe Expert-Guided TD3 with HFM Reward Shaping** *(ongoing)*  
**Problem.** Safe, mapless narrow dead-end escape with SE(2) anisotropy.  
**Method.** HFM reward shaping; safe action envelopes; TD3; risk-aware PI.  
**My role.** Algorithm design; experiments; ablations; writing.  
**Artifacts.** [[Diagram]](#) · [[Preprint soon]](#) · [[Code soon]](#)

**ROSLander Mobile Manipulation Demo**  
**Problem.** Perception-to-manipulation pipeline on mobile base.  
**Method.** ROS/Ubuntu; SLAM (Cartographer/ORB-SLAM2), Nav2; YOLO-based perception; 6-DOF arm pick-place.  
**My role.** Stack integration; demos; docs.  
**Artifacts.** [[Video]](#) · [[Docs]](#)

**Auto-tracking Phone Gimbal (embedded)**  
**Problem.** Low-cost visual tracking with MCU + servos.  
**Method.** Sensor fusion; control on MCU; rapid prototyping.  
**My role.** Firmware & hardware prototype.  
**Artifacts.** [[Video]](#) · [[Docs-CN]](#) · [[Code soon]](#)

**Verilog Image Rotation (pure hardware)**  
**Problem.** 24-bit BMP **90° CCW** rotation on FPGA.  
**Method.** Streaming pipeline; timing/memory organization.  
**My role.** RTL design & testbench; documentation.  
**Artifacts.** [[Code]](https://github.com/JustinZHAO-05/VeriRotate) · [[Docs-CN]](#)

**Robotic Manipulation Assignments (NeoScholar × Imperial)**  
**Problem.** Manipulator simulation & custom gripper design.  
**Method.** MATLAB kinematics/dynamics; design analysis.  
**My role.** Implementation; report; achieved high course scores.  
**Artifacts.** [[Report]](#) · [[Code]](#)

> More videos, posters, and short write-ups are in **Portfolio**.

---

## Coursework & Skills
**Certificates / in progress**: UW *Computational Neuroscience*; Stanford *Machine Learning* & *Deep Learning*; Stanford *Convex Optimization*.

**Core at TJU (Control/Robotics)**:  
**Automatic Control**; **Signals & Systems**; **Electrical Machines**; Analog & Digital Electronics; Mechanical Design; Electronics & Circuits; Mechanics; **Robot Kinematics & Dynamics**.

**Math, Physics & CS Foundations @ TJU**  
- **Mathematics** — Mathematical Analysis (Calculus + **ODEs** + intro Real Analysis + **Integral Transforms**); Advanced Linear Algebra (**Abstract Algebra** foundations); **Probability & Mathematical Statistics**; Mathematical Physics Equations (**PDEs**).  
- **Physics** — **Mechanics**; Vibrations & Waves; Thermodynamics / Statistical Physics; **Electromagnetism**; Optics; **Quantum Mechanics**.  
- **Computing** — **C++ (Programming Principles)**; **Discrete Mathematics** (Data Structures & Algorithms); **Computer Organization & Architecture**; **Numerical Analysis**.



**Tools**: C++, Python (PyTorch), MATLAB/Simulink, ROS2, SolidWorks, Verilog, Docker, Linux.

---

## Open to Summer Research (2026)
Seeking positions in **Neuro-AI / brain-inspired representation & control / embodied intelligence**.  
Happy to share a **1-page research pitch** and prior artifacts (papers, code, videos). **Email me** to connect.

---

### （中文）关于我（简要）
关注**类脑智能与机器人控制**：一方面研究**大脑学习机制**（是否存在类反向传播的更新、如何进行高效的信号调制与归因），另一方面用这些洞见构建**更省数据与算力、强泛化**的世界模型与决策系统，并将其**具身到机器人**。  
已在 **CSAI 2025** 入选一篇“**非完整约束窄死胡同逃逸的深度强化学习**”（海报展示）；在做“**基于 SE(2) Hamilton 快速行进法的安全专家引导 TD3**”；完成多项工程项目（绳驱并联、ROSLander 移动操作等），欢迎交流合作。
