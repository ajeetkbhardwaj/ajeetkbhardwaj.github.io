---
permalink: /about/
title: "About"
author_profile: true
---

I am **currently looking for Job**, was a Research Intern and Project Assistant at the Cloud Computing Lab and HIPC Lab, IIT Delhi under [Prof. Abhilash Jindal](https://abhilash-jindal.com/), where i had focused on building and evaluating LLM-based tools called [Speculator](https://github.com/ajeetkbhardwaj/Speculator) and design multi-agentic systems [Lean4Agent](https://github.com/ajeetkbhardwaj/Lean4Agent)

Before joining IIT Delhi, I completed my M.Sc in Mathematics and Computing at Banaras Hindu University (BHU), Varanasi, where I worked at the DST-CIMS. My Master’s thesis was centered around [Discrete Differential Geometry and its Applications](/files/master-thesis.pdf), supervised by [Prof. Bankteshwar Tiwari](https://www.bhu.ac.in/Site/FacultyProfile/45_233?FA000189).

My academic journey began with a B.Sc (Hons) in Applied Mathematics from Jamia Millia Islamia, New Delhi. Along the way, I also pursued a **[Data Science Specialization](https://gist.github.com/ajeetkbhardwaj/8b032fe2edc7f64b6a4d2a4295241622)** through NPTEL (IIT Madras), strengthening my skills in **Programming, Data Analytics, Machine Learning, and Large Language Models**.

<div style="clear: both;"></div>

<br>

<h2>Research Experience</h2>
<div class="grid-layout">
  <div class="modern-card timeline-item">
    <div class="timeline-date">Jun 2025</div>
    <div class="timeline-content">
      <strong>Cloud Computing and HIPC Lab, IIT Delhi</strong><br>
      <span style="color: var(--global-text-color-light);">
      Speculator - LLM System for OpenAPI Specification Generation from Source Code.<br> Lean4Agent - Multi-Agent System for Lean4 Code and Proof Generation from Mathematical Problems(Natural Language).</span>
    </div>
  </div>
  
  <div class="modern-card timeline-item">
    <div class="timeline-date">Jul 2024</div>
    <div class="timeline-content">
      <strong>QWorld Quantum Research</strong><br>
      <span style="color: var(--global-text-color-light);"> - Solving Wave PDE by HHL Quantum Algorithm(Qiskit) <br> 
      - Implemented and Practiced Variational Quantum Algorithms like VQEs.
      </span>
    </div>
  </div>
  
  <div class="modern-card timeline-item">
    <div class="timeline-date">Feb 2024</div>
    <div class="timeline-content">
      <strong>Devtern</strong><br>
      <span style="color: var(--global-text-color-light);">Machine Learning Intern developing end-to-end ML pipelines</span>
    </div>
  </div>
</div>

<h2>Latest Posts</h2>
<!-- This liquid loop automatically fetches your latest 5 posts from your _posts folder -->
<div class="grid-layout">
  {% for post in site.posts limit:5 %}
  <div class="modern-card timeline-item" style="padding: 16px 24px;">
    <div class="timeline-date" style="font-size: 0.85em;">{{ post.date | date: "%b %d, %Y" }}</div>
    <div class="timeline-content">
      <strong><a href="{{ post.url }}">{{ post.title }}</a></strong>
    </div>
  </div>
  {% endfor %}
</div>
<div style="text-align: right; margin-top: 16px; margin-bottom: 32px;">
  <a href="/year-archive/" class="btn--modern">View all Posts &rarr;</a>
</div>

<h2>Latest Projects</h2>
<style>
  .project-text-only img, 
  .project-text-only br {
    display: none !important;
  }
  .project-img-only {
    font-size: 0;
    color: transparent;
    line-height: 0;
  }
  .project-img-only p {
    margin: 0;
  }
</style>
<div class="project-grid">
  {% for project in site.portfolio %}
  <div class="modern-card project-card">
    <div class="project-img-only">
      {{ project.excerpt | markdownify }}
    </div>
    <h3 class="project-card-title"><a href="{{ project.url }}">{{ project.title }}</a></h3>
    <div class="project-card-excerpt project-text-only">
      {{ project.excerpt | markdownify }}
    </div>
  </div>
  {% endfor %}
</div>
<div style="text-align: right; margin-top: 16px; margin-bottom: 32px;">
  <a href="/portfolio/" class="btn--modern">View all Projects &rarr;</a>
</div>

<h2>Publications</h2>
<!-- In your current theme, publications are usually stored in the _publications folder. -->
<div class="grid-layout">
  {% for paper in site.publications %}
  <div class="modern-card timeline-item">
    <div class="timeline-date" style="min-width: 60px;">
      <span class="pill-badge">PUB</span>
    </div>
    <div class="timeline-content">
      <strong><a href="{{ paper.url }}" style="font-size: 1.1em;">{{ paper.title }}</a></strong><br>
      <div style="font-size: 0.9em; color: var(--global-text-color-light); margin-top: 4px;">{{ paper.citation }}</div>
    </div>
  </div>
  {% endfor %}
</div>
<div style="text-align: right; margin-top: 16px; margin-bottom: 32px;">
  <a href="/publications/" class="btn--modern">View all Publications &rarr;</a>
</div>
