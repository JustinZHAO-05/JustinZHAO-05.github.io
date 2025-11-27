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
I study **Neuro-AI × Robotics & Control**: understanding neural/cognitive mechanisms of human intelligence and using them to build **brain-inspired AI** embodied in **robots**.

- **Research focus**
  - *Neural learning mechanisms*: Does the brain perform “backprop-like” updates or alternative optimization? What signals and architectures enable efficient credit assignment?
  - *Data/compute-efficient world models & decision making*: brain-inspired representations and control for strong **generalization** under limited data/compute.
  - *From neural dynamics to cognition & consciousness*: bridges from the “easy problems” to structures that support subjective experience and high-level cognition.
  - *Robotics/control*: morphology & **optimal control** for robust closed-loop behavior; safe RL for nonholonomic navigation in **narrow dead-ends**.

---

## News
- **[Dec 12–14, 2025]** Our paper **“Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning”** is **accepted** to **The 9th International Conference on Computer Science and Artificial Intelligence (CSAI 2025)**, **poster** in Beijing.  
  PDF/Poster and code below.
- **Ongoing**: **From SE(2) Hamilton Fast Marching to Mapless Control: Safe Expert-Guided TD3 for Narrow Dead-End Escape** (reward shaping with Hamiltonian Fast Marching; expert-guided off/online RL).  
- **Learning now**: UW **Computational Neuroscience**, Stanford **Machine Learning** and **Deep Learning** (certificate tracks).  
- **Seeking 2026 Summer Research** in **Neuro-AI / Robotics & Control**.

---

## Selected Publication
- **Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning** (co-first author), **CSAI 2025 (poster)**.  
  *Gazebo training maps, SAC-based policy, batched curriculum & evaluation.*  
  **Code:** <https://github.com/JustinZHAO-05/cisDRL-RobotNav>  
  **Poster:** (to appear) • **PDF:** (to appear) • **BibTeX:** (to appear)

*Preprint in preparation*  
- **From SE(2) Hamilton Fast Marching to Mapless Control: Safe Expert-Guided TD3 for Narrow Dead-End Escape**.  
  *HFM reward shaping, safe expert envelopes, SE(2) anisotropy; mapless deployment with risk-aware policy improvement.*  
  (TechRxiv/Zenodo preprint link to appear; code release planned.)

---

## Featured Projects (Engineering & Research)

These projects **demonstrate a broad toolchain**: C++, Python, MATLAB, embedded development (MCU/Verilog), **basic AI** (computer vision & DRL), **ROS/robotics**, and **SolidWorks** for mechanism/CAD.


**Eight-Cable-Driven Parallel Robot** — full-stack design & control  
- Repo: <https://github.com/JustinZHAO-05/Eight-Cable-Driven-Parallel-Robot>  
- *What I did*: mechanism & CAD (SolidWorks), kinematics/dynamics, motor control & drivers, embedded code, MATLAB/Sim; complete videos, photos, and Chinese documentation.  
- *Why it matters*: high-DOF cable robots demand precise state estimation + robust control under elasticity and coupling.

**Dead-End DRL Navigation (CSAI work, engineering side)**  
- Repo: <https://github.com/JustinZHAO-05/cisDRL-RobotNav>  
- *Contrib*: problem formulation, SAC pipeline, Gazebo **batched** training map generator, training/eval workflows, making poster.  

**Safe Expert-Guided TD3 with HFM Reward Shaping (ongoing)**  
- *Contrib*: SE(2) HFM fields for reward shaping; safe action envelopes; TD3 training; mapless deployment; ablations.  
- *Artifacts*: diagrams, experiments, preprint & code (to appear).

**ROSlander Mobile Manipulation Demo**  
- *What I did*: ROS/Ubuntu stack integration; **SLAM**, navigation, YOLO-based perception; arm pick-place; human-pose controlled gestures.  
- *Artifacts*: demo videos & docs.

**Auto-tracking Phone Gimbal (embedded)**  
- MCU + servos + sensors; early prototype videos; Chinese docs (code to be cleaned and uploaded).  

**Verilog image rotation (pure hardware)**  
- Repo: <https://github.com/JustinZHAO-05/VeriRotate>  
- *What I did*: 24-bit BMP **90° CCW rotation** pipeline in Verilog; timing & memory organization; Chinese documentation.

**Robotic Manipulation assignments (NeoScholar × Imperial)**  
- MATLAB simulation of a manipulator and custom gripper design (with high scores); reports + code available.

> More videos, posters, and short write-ups are in **Portfolio**. Each project page lists: problem → method → results → **my contribution** → code/video.

---

## Coursework (selected & in-progress, certificate tracks)

- **Computational Neuroscience** (UW) — neuron models, population coding, learning rules, perceptual decision.
- **Machine Learning** (Stanford) & **Deep Learning** — supervised/unsupervised, optimization, regularization; modern DL stacks.
- **Convex Optimization**(Stanford)
- **Control/Robotics at TJU** — Automatic Control, Signals & Systems, Electronics & Circuits, Mechanics, Robot Kinematics & Dynamics.

**Mathematics, Physics & CS Foundations @ TJU**
- **Mathematical Analysis** — Calculus + introductory Real Analysis + **Integral Transforms**  
- **Advanced Linear Algebra** — Linear Algebra + **Abstract Algebra** (foundations)  
- **Probability & Mathematical Statistics**  
- **Mathematical Physics Equations** — **PDEs**  
- **Fundamental Physics**  
- **Computing Core** — **C++ (Programming Principles)**, **Discrete Mathematics** (Data Structures & Algorithms), **Computer Organization & Architecture**, **Numerical Analysis**


---

## Open to Summer Research (2026)
I’m looking for **summer research** in labs working on **neural learning rules, brain-inspired representation & control, machine learning and embodied intelligence**.  
If you see a fit, please email me — I’m happy to share a 1-page research pitch and prior artifacts (papers, code, videos).

---


### (中文) 关于我（简要）
我关注 **类脑智能与机器人控制**：一方面探索**大脑学习机制**（是否存在类反向传播的更新、如何进行高效分配与优化），另一方面用这些洞见去构建**更节省数据与算力、具备强泛化**的世界模型与决策系统，并将其**具身到机器人**。我已在 **CSAI 2025** 入选一篇 **非完整约束窄死胡同逃逸的深度强化学习** 论文（海报展示），并在开展 **基于 SE(2) Hamilton 快速行进法的安全专家引导 TD3** 新课题；工程侧完成多项机器人项目（绳驱并联、ROSLander 移动操作等），欢迎交流合作。
