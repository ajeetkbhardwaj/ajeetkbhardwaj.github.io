---
layout: archive
title: "Team"
permalink: /team/
author_profile: true
---

Meet the team and my wonderful collaborators!

<div class="entries-list">
{% for post in site.team reversed %}
  {% include archive-single.html %}
{% endfor %}
</div>
