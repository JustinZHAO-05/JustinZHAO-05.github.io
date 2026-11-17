---
layout: academic
permalink: /
title: Yanzhe Zhao
description: Computational and Cognitive Neuroscience, Neurolinguistics. Research, publications, and academic CV of Yanzhe Zhao.
author_profile: false
redirect_from:
  - /about/
  - /about.html
---
{% assign p = site.data.profile %}
<section class="site-wrap identity" id="top">
  <div class="identity-grid">
    <img class="identity-photo" src="{{ p.portrait | relative_url }}" alt="Yanzhe Zhao" width="180" height="270" fetchpriority="high">
    <div class="identity-heading"><h1>{{ p.name }}</h1><p class="identity-fields">{{ p.fields }}<br>{{ p.secondary_field }}</p></div>
    <div class="identity-about"><p>{{ p.intro }}</p><p>{{ p.interests_short }}</p><p class="identity-degree">B.Eng. Automation &middot; Expected July 2027</p></div>
    <div class="identity-actions text-links"><a class="button button-primary" href="{{ p.cv | relative_url }}"><i class="far fa-file-pdf" aria-hidden="true"></i> Academic CV</a><a href="{{ p.full_cv | relative_url }}">Full CV</a><a href="mailto:{{ p.email }}">Email</a><a href="{{ p.orcid }}">ORCID</a></div>
  </div>
</section>
<section class="page-band" id="current-research"><div class="site-wrap section-space"><h2 class="section-title">Current Research</h2><div class="dated-entry"><p class="entry-date">Jul 2026-Present</p><div><h3>Visiting Student &middot; Shanshan Qin Lab</h3><p><a class="quiet-link" href="https://ssqinlab.com/">Shanghai Jiao Tong University</a></p><ul class="research-lines"><li>Longitudinal neural recordings: representational drift and representational sparsity; modeling candidate drift mechanisms.</li><li>Circadian clock networks: initiating an undergraduate thesis project.</li></ul></div></div></div></section>
<section class="site-wrap section-space" id="research"><div class="section-heading-row"><h2 class="section-title">Selected Research</h2><a href="{{ '/portfolio/' | relative_url }}">All projects <i class="fas fa-arrow-right" aria-hidden="true"></i></a></div>{% assign featured = site.data.projects | where: 'featured', true | sort: 'priority' %}{% for project in featured %}{% include research-row.html project=project %}{% endfor %}</section>
<section class="site-wrap section-space publication-section" id="publications"><div class="section-heading-row"><h2 class="section-title">Publications &amp; Preprints</h2><a href="{{ '/publications/' | relative_url }}">All publications</a></div>{% assign pubs = site.publications | sort: 'date' | reverse %}{% assign groups = 'preprint|published' | split: '|' %}{% for group in groups %}<h3 class="publication-group">{% if group == 'preprint' %}Preprints &amp; Manuscripts Under Review{% else %}Peer-Reviewed Publications{% endif %}</h3>{% for pub in pubs %}{% if pub.kind == group %}{% include publication-row.html pub=pub compact=true %}{% endif %}{% endfor %}{% endfor %}</section>
<section class="page-band" id="education"><div class="site-wrap section-space"><h2 class="section-title">Education</h2><h3 class="education-institution">{{ p.education.institution }}</h3><p>{{ p.education.degree }} &middot; {{ p.education.school }}<br>{{ p.education.dates }}</p><p class="education-description">{{ p.education.description }}</p>{% include academic-standing.html %}</div></section>
<section class="site-wrap section-space" id="training"><h2 class="section-title">Selected Coursework</h2>{% include course-list.html preview=true %}<p><a href="{{ '/cv/#coursework' | relative_url }}">All coursework <i class="fas fa-arrow-right" aria-hidden="true"></i></a></p></section>
<section class="page-band" id="contact"><div class="site-wrap section-space"><h2 class="section-title">Training &amp; Contact</h2>{% assign training = site.data.experience | where: 'id', 'neuromatch' | first %}<div class="training-row"><div><h3>Neuromatch Academy &middot; Computational Neuroscience</h3><p>July 2026 &middot; Interactive track and course project &middot; 128 hours</p></div><div class="text-links"><a href="{{ training.certificate }}">Certificate</a><a href="{{ training.video }}">Presentation</a></div></div><div class="contact-row"><a href="mailto:{{ p.email }}">{{ p.email }}</a><div class="text-links"><a href="{{ p.github }}">GitHub</a><a href="{{ p.orcid }}">ORCID</a><a href="{{ p.cv | relative_url }}">Academic CV</a><a href="{{ p.full_cv | relative_url }}">Full CV</a></div></div></div></section>
