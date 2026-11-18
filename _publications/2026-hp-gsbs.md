---
layout: publication
title: "HP-GSBS: Accelerating greedy state boundary search with reusable interval statistics"
permalink: /publication/hp-gsbs/
date: 2026-10-23
year: 2026
kind: preprint
preprint_server: arXiv
authors: "Yanzhe Zhao and Yongzhang Ji"
author_names: [Yanzhe Zhao, Yongzhang Ji]
authors_short: "Zhao, Y., and Ji, Y."
status: Under review at Neuroinformatics
venue: arXiv:2610.25898
doi: 10.48550/arXiv.2610.25898
doiurl: https://doi.org/10.48550/arXiv.2610.25898
paperurl: https://arxiv.org/abs/2610.25898
codeurl: https://github.com/JustinZHAO-05/HP-GSBS
bibtexurl: /files/bib/hp_gsbs_2026.bib
researchurl: /research/hp-gsbs/
contribution: "Core algorithm and code contributions, experimental analysis, and manuscript writing."
excerpt: "Reusable interval statistics and CPU/GPU implementations for efficient neural-state segmentation, evaluated with synthetic signals, EEG, and naturalistic fMRI."
---

HP-GSBS expresses repeated state-template calculations as reusable interval contributions and computes t-distance from correlation statistics. CPU, PyTorch CUDA and Triton paths support efficient neural-state analysis.

The paper reports median same-input speedups of 154-1,730 across controlled workloads, with matching reference boundary histories and selected state counts in all 168 tested optimized executions. EEG validation and a naturalistic fMRI application demonstrate use on multivariate neural recordings.
