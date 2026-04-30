---
layout: home
permalink: /
title: "Yanzhe (Justin) Zhao"
description: "Computational Neuroscience | Cognitive Neuroscience | Neuro-AI"
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

{% assign projects = site.data.projects | sort: "priority" %}

<section class="home-hero" id="top">
  <div class="home-hero__copy">
    <nav class="home-hero__quicklinks" aria-label="Profile quick links">
      <a href="#research">Research</a>
      <a href="/portfolio/">Projects</a>
      <a href="/publications/">Publications</a>
      <a href="/cv/">CV</a>
    </nav>
    <h1>Yanzhe (Justin) Zhao</h1>
    <p class="home-hero__subtitle">Computational Neuroscience | Cognitive Neuroscience | Neuro-AI</p>
    <p class="home-hero__summary">
      B.Eng. in Automation student at the School of Future Technology, Tianjin University. The School of Future Technology is Tianjin University's elite undergraduate college, and its Intelligent Machine Platform honors track admits students through Gaokao-based selection and internal university selection.
    </p>
    <p class="home-hero__summary">
      After two years of shared training in mathematics, physics, and engineering fundamentals, I selected Automation as my major. I now study how neural and cognitive mechanisms can inform computational models of learning, prediction, and representation.
    </p>
    <p class="home-hero__summary">
      My academic path started from robotics, control, and reinforcement learning. It is now centered on computational and cognitive neuroscience, with particular interest in world models, predictive processing, neural mechanisms of natural language acquisition, and embodied cognition.
    </p>
    <div class="home-hero__actions">
      <a class="btn btn--primary" href="/cv/">View CV</a>
      <a class="btn btn--inverse" href="/portfolio/">Explore Projects</a>
    </div>
  </div>
  <aside class="home-hero__profile" aria-label="Academic profile summary">
    <img src="/images/profile-web.jpg" alt="Yanzhe Zhao formal portrait">
    <div class="fact-grid">
      <div><strong>8/100</strong><span>Overall rank</span></div>
      <div><strong>1/8</strong><span>Junior specialization rank</span></div>
      <div><strong>91.54</strong><span>Weighted score</span></div>
      <div><strong>3.85/4.0</strong><span>GPA</span></div>
    </div>
  </aside>
</section>

<section class="home-section research-band" id="research">
  <div class="section-heading">
    <span>Research Direction</span>
    <h2>From embodied control to computational models of mind and brain.</h2>
  </div>
  <div class="research-path">
    <article>
      <h3>Robotics and Control Foundation</h3>
      <p>Built a systems-level base through automatic control, signal processing, robot kinematics, embedded systems, numerical methods, and full-stack robot projects.</p>
    </article>
    <article>
      <h3>Learning and Decision Making</h3>
      <p>Used deep reinforcement learning for constrained navigation, connecting policy learning, spatial planning, and action under nonholonomic limits.</p>
    </article>
    <article>
      <h3>Computational and Cognitive Neuroscience</h3>
      <p>Now focusing on neural computation, predictive processing, world models, cognitive maps, language learning, and Neuro-AI models that can be tested scientifically.</p>
    </article>
  </div>
</section>

<section class="home-section publication-band" id="publications">
  <div class="section-heading">
    <span>Publication</span>
    <h2>Peer-reviewed work on deep reinforcement learning for constrained spatial navigation.</h2>
  </div>
  <article class="publication-feature">
    <p class="publication-feature__venue">CSAI 2025 | ACM Proceedings | pp. 126-131</p>
    <h3>Nonholonomic Narrow Dead-End Escape with Deep Reinforcement Learning</h3>
    <p>Denghan Xiong, <strong>Yanzhe Zhao</strong>, Yutong Chen, and Zichun Wang. Proceedings of the 2025 9th International Conference on Computer Science and Artificial Intelligence.</p>
    <div class="publication-feature__links">
      <a href="https://doi.org/10.1145/3788149.3788204">ACM DOI</a>
      <a href="https://dblp.org/rec/conf/csai/XiongZCW25">DBLP</a>
      <a href="https://arxiv.org/abs/2511.22338">arXiv</a>
      <a href="/files/bib/nonholonomic_deadend_2025.bib">BibTeX</a>
    </div>
  </article>
</section>

<section class="home-section" id="projects">
  <div class="section-heading section-heading--row">
    <div>
      <span>Selected Projects</span>
      <h2>Evidence of neuroscience readiness, applied ML, AI implementation, and engineering depth.</h2>
    </div>
    <a href="/portfolio/">All projects</a>
  </div>
  <div class="project-grid project-grid--featured">
    {% for project in projects limit: 8 %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
</section>

<section class="home-section coursework-band" id="training">
  <div class="section-heading">
    <span>Coursework and Training</span>
    <h2>A math-heavy engineering base extended into neuroscience and modern machine learning.</h2>
  </div>
  <div class="coursework-grid">
    <article>
      <h3>Elite Engineering Program</h3>
      <p>School of Future Technology, Intelligent Machine Platform honors track: selective admission, intensive foundational training in the first two years, then free major selection after the sophomore year.</p>
    </article>
    <article>
      <h3>Junior Fall</h3>
      <p>Equation of Mathematics and Physics; Theory of Motor; Numerical Computational Method.</p>
    </article>
    <article>
      <h3>Junior Spring</h3>
      <p>Brain and Cognition; Intelligent Medical Signal Processing; Optimization-based Machine Learning; Deep Learning; Pattern Recognition and Brain-like Intelligence.</p>
    </article>
    <article>
      <h3>July 2026</h3>
      <p>Neuromatch Academy Computational Neuroscience online summer school.</p>
    </article>
    <article>
      <h3>Online Certificates</h3>
      <p>MITx Introduction to Differential Equations; DelftX MECH1x Building Robots: Electrical Drives; DelftX MECH2x Building Robots: Sensors and Data Acquisition.</p>
    </article>
    <article>
      <h3>Core Strengths</h3>
      <p>Mathematical modeling, programming, reproducible workflows, technical writing, and cross-disciplinary translation between systems engineering and neuroscience.</p>
    </article>
  </div>
</section>

<section class="home-section contact-band" id="contact">
  <div class="section-heading">
    <span>Contact</span>
    <h2>Open to research conversations in computational neuroscience, cognitive neuroscience, and Neuro-AI.</h2>
  </div>
  <div class="contact-actions">
    <a href="mailto:justinzhaoyz@outlook.com">justinzhaoyz@outlook.com</a>
    <a href="https://github.com/JustinZHAO-05">GitHub</a>
    <a href="https://orcid.org/0009-0003-5342-6611">ORCID</a>
  </div>
</section>
