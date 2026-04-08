---
permalink: /
title: "Ajeet Kumar"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am currently a Research Intern at the Cloud Computing Lab and HIPC Lab, IIT Delhi, where I focus on building and evaluating LLM-based tools that automatically generate OpenAPI specifications from source API code.

Before joining IIT Delhi, I completed my M.Sc in Mathematics and Computing at Banaras Hindu University (BHU), Varanasi, where I worked at the DST-CIMS. My Master’s thesis was centered around [Discrete Differential Geometry and its Applications](master-thesis.pdf), supervised by [Prof. Bankteshwar Tiwari](https://www.bhu.ac.in/Site/FacultyProfile/45_233?FA000189).

My academic journey began with a B.Sc (Hons) in Applied Mathematics from Jamia Millia Islamia, New Delhi. Along the way, I also pursued a **[Data Science Specialization](https://gist.github.com/ajeetkbhardwaj/8b032fe2edc7f64b6a4d2a4295241622)** through NPTEL (IIT Madras), strengthening my skills in **Programming, Data Analytics, Machine Learning, and Large Language Models**.

<div style="clear: both;"></div>

<br>
<h2>Latest Posts</h2>
<!-- This liquid loop automatically fetches your latest 5 posts from your _posts folder -->
<div class="table-responsive">
  <table style="width: 100%; border-collapse: collapse; border: none;">
    {% for post in site.posts limit:5 %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="width: 20%; padding: 8px 0; color: #666;">{{ post.date | date: "%b %d, %Y" }}</td>
      <td style="padding: 8px 0;"><a href="{{ post.url }}">{{ post.title }}</a></td>
    </tr>
    {% endfor %}
  </table>
</div>

<h2>Talks & Research Experiences</h2>
<div class="table-responsive">
  <table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="border-bottom: 1px solid #eee;">
      <td style="width: 20%; padding: 8px 0; color: #666;">Jun 2024</td>
      <td style="padding: 8px 0;"><strong>Cloud Computing and HIPC Lab, IIT Delhi</strong> — LLM & Multi-Agent systems for OpenAPI Specification Generation</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px 0; color: #666;">Jul 2024</td>
      <td style="padding: 8px 0;"><strong>QWorld Quantum Research</strong> — Implemented HHL algorithm using Qiskit to solve PDEs</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px 0; color: #666;">Feb 2024</td>
      <td style="padding: 8px 0;"><strong>Devtern</strong> — Machine Learning Intern developing end-to-end ML pipelines</td>
    </tr>
  </table>
</div>

<h2>Projects</h2>
<style>
  .project-text-only img, 
  .project-text-only br {
    display: none !important;
  }
  .project-img-only {
    font-size: 0;
    color: transparent;
    line-height: 0;
    text-align: right;
  }
  .project-img-only p {
    margin: 0;
  }
  .project-img-only img {
    max-width: 100%;
    height: auto;
    max-height: 150px;
    border-radius: 6px;
  }
</style>
<div class="table-responsive">
  <table style="width: 100%; border-collapse: collapse; border: none;">
    {% for project in site.portfolio %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="width: 70%; padding: 12px 15px 12px 0; vertical-align: top;">
        <strong><a href="{{ project.url }}">{{ project.title }}</a></strong><br>
        <div class="project-text-only" style="font-size: 0.9em; color: #555; margin-top: 8px;">
          {{ project.excerpt | markdownify }}
        </div>
      </td>
      <td style="width: 30%; padding: 12px 0; vertical-align: top;" aria-hidden="true">
        <div class="project-img-only">
          {{ project.excerpt | markdownify }}
        </div>
      </td>
    </tr>
    {% endfor %}
  </table>
</div>


<h2>Publications</h2>
<!-- In your current theme, publications are usually stored in the _publications folder. 
     This loop will list them out similar to the al-folio style -->
<div class="table-responsive">
  <table style="width: 100%; border-collapse: collapse; border: none;">
    {% for paper in site.publications %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="width: 10%; padding: 12px 0;">
        <span style="background-color: #007bff; color: white; padding: 3px 6px; border-radius: 4px; font-size: 0.8em; font-weight: bold;">PUB</span>
      </td>
      <td style="padding: 12px 0;">
        <strong><a href="{{ paper.url }}">{{ paper.title }}</a></strong><br>
        <span style="font-size: 0.9em; color: #555;">{{ paper.citation }}</span>
      </td>
    </tr>
    {% endfor %}
  </table>
</div>