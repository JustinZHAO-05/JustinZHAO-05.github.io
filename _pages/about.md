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
    <div class="identity-actions text-links"><a class="button button-primary" href="{{ p.cv | relative_url }}"><i class="far fa-file-pdf" aria-hidden="true"></i> Academic CV</a><a href="{{ p.full_cv | relative_url }}">Full CV</a><a href="{{ p.journey | relative_url }}">Intellectual journey</a><a href="mailto:{{ p.email }}">Email</a><a href="{{ p.orcid }}">ORCID</a></div>
  </div>
</section>
<section class="page-band" id="current-research"><div class="site-wrap section-space">
  <h2 class="section-title">Current Research</h2>
  <div class="dated-entry"><p class="entry-date">Jul 2026-Present</p><div><h3>Visiting Student &middot; Shanshan Qin Lab</h3><p><a class="quiet-link" href="https://ssqinlab.com/">Shanghai Jiao Tong University</a></p><ul class="research-lines"><li>Longitudinal neural recordings: representational drift and representational sparsity; modeling candidate drift mechanisms.</li><li>Undergraduate thesis: computational modeling of circadian clock networks.</li></ul><p class="current-exploration">Alongside these projects, I am pursuing exploratory work on language and subjective experience, with an interest in the evolutionary emergence of neural cognition.</p></div></div>
</div></section>
<section class="site-wrap section-space" id="research">
  <div class="section-heading-row"><h2 class="section-title">Selected Research</h2><a href="{{ '/portfolio/' | relative_url }}">All projects <i class="fas fa-arrow-right" aria-hidden="true"></i></a></div>
  {% assign featured = site.data.projects | where: 'featured', true | sort: 'priority' %}{% for project in featured %}{% include research-row.html project=project %}{% endfor %}
</section>
<section class="site-wrap section-space publication-section" id="publications">
  <div class="section-heading-row"><h2 class="section-title">Publications &amp; Preprints</h2><a href="{{ '/publications/' | relative_url }}">All publications</a></div>
  {% assign pubs = site.publications | sort: 'date' | reverse %}{% assign groups = 'preprint|published' | split: '|' %}{% for group in groups %}<h3 class="publication-group">{% if group == 'preprint' %}Preprints{% else %}Peer-Reviewed Publications{% endif %}</h3>{% for pub in pubs %}{% if pub.kind == group %}{% include publication-row.html pub=pub compact=true %}{% endif %}{% endfor %}{% endfor %}
</section>
<section class="journey-band" id="journey"><div class="site-wrap section-space">
  <div class="journey-heading"><p class="essay-kicker">An Evolving Research Path</p><h2>Academic &amp; Intellectual Journey</h2><p>From engineered agents to the neural mechanisms of cognition.</p></div>
  {% include journey-timeline.html %}
  <div class="journey-outro"><p>How everyday observations, language learning, and mathematical questions shaped my research interests.</p><a href="{{ p.journey | relative_url }}">Read my intellectual journey <i class="fas fa-arrow-right" aria-hidden="true"></i></a></div>
</div></section>
<section class="page-band" id="education"><div class="site-wrap section-space">
  <h2 class="section-title">Education</h2><h3 class="education-institution">{{ p.education.institution }}</h3><p>{{ p.education.degree }} &middot; {{ p.education.school }}<br>{{ p.education.dates }}</p><p class="education-description">{{ p.education.description }}</p>{% include academic-standing.html %}
</div></section>
<section class="site-wrap section-space" id="coursework">
  <h2 class="section-title">Selected Coursework</h2>{% include course-list.html preview=true %}<p><a href="{{ '/cv/#coursework' | relative_url }}">All coursework <i class="fas fa-arrow-right" aria-hidden="true"></i></a></p>
</section>
<section class="page-band" id="training"><div class="site-wrap section-space">
  <h2 class="section-title">Research Training &amp; Additional Coursework</h2>{% include home-training.html %}
</div></section>
<section class="site-wrap section-space" id="reading">
  <h2 class="section-title">Reading &amp; Foundations</h2><div class="reading-layout"><div class="reading-art" aria-label="Selected foundational texts">{% for book in site.data.reading %}{% if book.cover %}<a href="{{ book.url }}"><img src="{{ book.cover | relative_url }}" alt="{{ book.short_title }} by {{ book.authors }}" loading="lazy" width="110" height="165"></a>{% endif %}{% endfor %}</div><div>{% include reading-list.html %}</div></div>
</section>
<section class="page-band" id="contact"><div class="site-wrap section-space">
  <h2 class="section-title">Contact</h2><p>Research interests in computational and cognitive neuroscience, neurolinguistics, and the neural basis of experience.</p><div class="contact-row"><a href="mailto:{{ p.email }}">{{ p.email }}</a><div class="text-links"><a href="{{ p.github }}">GitHub</a><a href="{{ p.orcid }}">ORCID</a><a href="{{ p.cv | relative_url }}">Academic CV</a><a href="{{ p.full_cv | relative_url }}">Full CV</a></div></div>
</div></section>
