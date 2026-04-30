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
    <article data-step="01">
      <p class="research-path__label">Foundation</p>
      <h3>Robotics and Control Foundation</h3>
      <p>Built a systems-level base through automatic control, signal processing, robot kinematics, embedded systems, numerical methods, and full-stack robot projects.</p>
    </article>
    <article data-step="02">
      <p class="research-path__label">Transition</p>
      <h3>Learning and Decision Making</h3>
      <p>Used deep reinforcement learning for constrained navigation, connecting policy learning, spatial planning, and action under nonholonomic limits.</p>
    </article>
    <article data-step="03">
      <p class="research-path__label">Current focus</p>
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
    <h2>Structured training across elite engineering, research practice, neuroscience, and machine learning.</h2>
  </div>

  <div class="training-layout">
    <article class="training-feature">
      <p class="training-kicker">Elite undergraduate college</p>
      <h3>School of Future Technology, Intelligent Machine Platform</h3>
      <p>The School of Future Technology is Tianjin University's elite undergraduate college. The Intelligent Machine Platform honors track admits students through Gaokao-based selection and internal university selection.</p>
      <p>The first two years provide shared training in mathematics, physics, and engineering fundamentals. After sophomore-year major selection, I chose Automation.</p>
      <div class="training-feature__metrics">
        <div><strong>8/100</strong><span>Overall rank</span></div>
        <div><strong>1/8</strong><span>Junior specialization rank</span></div>
        <div><strong>91.54</strong><span>Weighted score</span></div>
        <div><strong>3.85/4.0</strong><span>GPA</span></div>
      </div>
    </article>

    <div class="training-timeline" aria-label="Research and training timeline">
      <article>
        <time>2026.07</time>
        <div>
          <h3>Computational Neuroscience Online Summer School</h3>
          <p>Neuromatch Academy. Upcoming training in computational neuroscience, neural data analysis, dynamical systems, learning, decision making, and cognition.</p>
        </div>
      </article>
      <article>
        <time>2025.07-08</time>
        <div>
          <h3>In-person Summer Research</h3>
          <p>NeoScholar and Imperial College London, supervised by Prof. Sen Wang. Developed and evaluated deep reinforcement learning methods for nonholonomic narrow dead-end escape, leading to the CSAI 2025 publication. Evaluation: A.</p>
        </div>
      </article>
      <article>
        <time>2025.03-06</time>
        <div>
          <h3>Robot Perception, Localization and Navigation</h3>
          <p>NeoScholar and Imperial College London audit covering SLAM, localization, navigation, and implementation-oriented robotics methods.</p>
        </div>
      </article>
      <article>
        <time>2024.10-2025.01</time>
        <div>
          <h3>Robotic Manipulation</h3>
          <p>NeoScholar and Imperial College London course with high score and CIEI certification; completed kinematics, dynamics, grasping, custom gripper design, and simulation assignments.</p>
        </div>
      </article>
      <article>
        <time>2024.07</time>
        <div>
          <h3>Computing Applications in Science and Engineering</h3>
          <p>University of Bristol Summer School. Used Java and Go for scientific computing; built satellite-control simulation and Arduino/networked sensing projects.</p>
        </div>
      </article>
    </div>
  </div>

  <div class="coursework-panel">
    <div class="section-heading section-heading--compact">
      <span>Selected Coursework</span>
      <h2>Course clusters supporting the current neuroscience and Neuro-AI direction.</h2>
    </div>
    <div class="coursework-grid">
      <article>
        <h3>Neuroscience and Machine Learning</h3>
        <p>Brain and Cognition; Intelligent Medical Signal Processing; Optimization-based Machine Learning; Deep Learning; Pattern Recognition and Brain-like Intelligence.</p>
      </article>
      <article>
        <h3>Mathematics and Computation</h3>
        <p>Mathematical Analysis; Advanced Linear Algebra; Probability and Mathematical Statistics; Equation of Mathematics and Physics; Numerical Computational Method; Discrete Mathematics.</p>
      </article>
      <article>
        <h3>Signals, Control, and Robotics</h3>
        <p>Signals and Systems; Automatic Control; Theory of Motor; Robot Kinematics and Dynamics; Computer Organization and Architecture; C++ Programming.</p>
      </article>
      <article>
        <h3>Online Certificates and Study</h3>
        <p>MITx Introduction to Differential Equations; DelftX MECH1x Building Robots: Electrical Drives; DelftX MECH2x Building Robots: Sensors and Data Acquisition; University of Padova Foundations of Signals and Systems; Stanford Machine Learning, Deep Learning, and Convex Optimization tracks; UW Computational Neuroscience materials.</p>
      </article>
    </div>
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
