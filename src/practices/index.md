---
title: Practices
layout: layouts/base.njk
---

# Practices

This library gathers exercises and prompts that invite you to write with your environments, rewild your approach to process, and attend to relationships between place, body, and language.

Below youll find practices drawn from the framework in this project. Each one includes access notes, steps, reflection questions, and theory roots.

{% if collections.practices %}
<ul class="practice-list">
{% for practice in collections.practices %}
  <li class="practice-item">
    <h2>
      <a href="{{ practice.url }}">{{ practice.data.title }}</a>
    </h2>
    {% if practice.data.duration or practice.data.intensity %}
    <p class="practice-meta">
      {% if practice.data.duration %}<span>{{ practice.data.duration }}</span>{% endif %}
      {% if practice.data.intensity %}<span>{{ practice.data.intensity }}</span>{% endif %}
    </p>
    {% endif %}
    {% if practice.data.tags %}
    <p class="practice-tags">
      {% for tag in practice.data.tags %}
      <span class="tag-pill">{{ tag }}</span>
      {% endfor %}
    </p>
    {% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}
