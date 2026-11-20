---
layout: academic
title: Academic CV
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---
{% assign p = site.data.profile %}
<div class="site-wrap index-page cv-page">
  <header class="page-heading"><h1>Academic CV</h1><p class="page-lead">{{ p.fields }} &middot; {{ p.secondary_field }}</p><div class="text-links"><a class="button button-primary" href="{{ p.cv | relative_url }}"><i class="far fa-file-pdf" aria-hidden="true"></i> Academic CV</a><a class="button" href="{{ p.full_cv | relative_url }}"><i class="far fa-file-pdf" aria-hidden="true"></i> Full CV</a></div></header>
  <div class="cv-layout">
    <nav class="cv-index" aria-label="CV sections"><a href="#education">Education</a><a href="#interests">Research interests</a><a href="#experience">Research experience</a><a href="#publications">Publications</a><a href="#projects">Selected projects</a><a href="#training">Research training</a><a href="#independent-study">Additional coursework</a><a href="#coursework">Coursework</a><a href="#reading">Independent reading</a><a href="#skills">Skills &amp; languages</a></nav>
    <div class="cv-content">
      <section id="education"><h2>Education</h2><h3>{{ p.education.institution }}</h3><p>{{ p.education.degree }} &middot; {{ p.education.school }}<br>{{ p.education.dates }}</p><p>{{ p.education.description }}</p>{% include academic-standing.html %}</section>
      <section id="interests"><h2>Research Interests</h2><p>{{ p.interests }}</p><p>{{ p.trajectory }}</p><p><a href="{{ p.journey | relative_url }}">From robots to minds: read my intellectual journey. <i class="fas fa-arrow-right" aria-hidden="true"></i></a></p></section>
      <section id="experience"><h2>Research Experience</h2>{% for exp in site.data.experience %}
        {% if exp.project_id %}<article class="cv-experience"><h3>{{ exp.institution }} {{ exp.title }}</h3><p class="entry-date">{{ exp.dates }} &middot; {{ exp.team }}</p><p>{{ exp.research_summary }}</p></article>
        {% elsif exp.kind == 'research' %}<article class="cv-experience"><h3>{{ exp.title }}</h3><p class="entry-date">{{ exp.dates }} &middot; {{ exp.institution }}</p><p>{{ exp.summary }}</p>{% if exp.bullets %}<ul>{% for item in exp.bullets %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}</article>{% endif %}
      {% endfor %}</section>
      <section id="publications"><h2>Publications &amp; Preprints</h2>{% assign pubs = site.publications | sort: 'date' | reverse %}{% for pub in pubs %}{% include publication-row.html pub=pub %}{% endfor %}</section>
      <section id="projects"><h2>Selected Research and Projects</h2>
        {% assign featured = site.data.projects | where: 'featured', true | sort: 'priority' %}
        {% for project in featured %}<article class="cv-project"><h3><a href="{{ project.detail | relative_url }}">{{ project.title }}</a></h3>
          {% if project.links.video %}<p>{{ project.summary }} {{ project.approach }}</p><div class="text-links"><a href="{{ project.detail | relative_url }}">Project</a><a href="{{ project.links.github }}">Code</a><a href="{{ project.links.video }}">Presentation</a></div>
          {% else %}<p>{{ project.role }} {{ project.summary }}</p>{% endif %}</article>{% endfor %}
        <article class="cv-project"><h3>{{ p.neural_project.title }}</h3><p>{{ p.neural_project.summary }}</p></article>{% assign engineering = site.data.projects | where: 'main_cv', true | sort: 'priority' %}{% for project in engineering %}<article class="cv-project"><h3><a href="/projects/{{ project.id | downcase }}/">{{ project.title }}</a></h3><p>{{ project.summary }}</p></article>{% endfor %}<p><a href="{{ '/portfolio/' | relative_url }}">Complete project archive</a></p>
      </section>
      <section id="training"><h2>Research Training &amp; Summer Schools</h2>{% for exp in site.data.experience %}{% unless exp.kind == 'research' %}<article class="cv-experience" id="training-{{ exp.id }}"><h3>{{ exp.title }}</h3><p class="entry-date">{{ exp.dates }} &middot; {{ exp.institution }}</p><p>{{ exp.summary }}</p>{% if exp.certificate %}<div class="text-links"><a href="{{ exp.certificate }}">Certificate</a><a href="{{ exp.project | relative_url }}">Project</a><a href="{{ exp.video }}">Presentation</a></div>{% endif %}</article>{% endunless %}{% endfor %}</section>
      <section id="independent-study"><h2>Additional Certified Coursework</h2>{% for course in site.data.independent_study %}<article class="cv-experience"><h3>{{ course.title }}</h3><p class="entry-date">{{ course.institution }} &middot; {{ course.date | date: '%d %b %Y' }}</p><p>{{ course.summary }}{% if course.grade %} Overall score: {{ course.grade }}.{% endif %}</p><p><a href="{{ course.certificate }}">{{ course.status }} <i class="fas fa-external-link-alt" aria-hidden="true"></i></a></p></article>{% endfor %}</section>
      <section id="coursework"><h2>Coursework</h2>{% include course-list.html %}</section>
      <section id="reading"><h2>Independent Reading</h2>{% include reading-list.html %}</section>
      <section id="skills"><h2>Skills &amp; Languages</h2>{% for skill in p.skills %}<p><strong>{{ skill.title }}:</strong> {{ skill.text }}</p>{% endfor %}<p><strong>Languages:</strong> Chinese (native); English: {{ p.ielts }}.</p></section>
    </div>
  </div>
</div>
