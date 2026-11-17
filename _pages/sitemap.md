---
layout: academic
title: Sitemap
permalink: /sitemap/
author_profile: false
---
<div class="site-wrap index-page"><h1>Sitemap</h1><ul><li><a href="{{ '/' | relative_url }}">Home</a></li><li><a href="{{ '/publications/' | relative_url }}">Publications &amp; Preprints</a></li><li><a href="{{ '/portfolio/' | relative_url }}">Research &amp; Projects</a></li><li><a href="{{ '/cv/' | relative_url }}">Academic CV</a></li></ul><h2>Research &amp; Projects</h2><ul>{% assign projects = site.data.projects | sort: 'priority' %}{% for project in projects %}<li><a href="{% if project.detail %}{{ project.detail | relative_url }}{% else %}/projects/{{ project.id | downcase }}/{% endif %}">{{ project.title }}</a></li>{% endfor %}</ul></div>
