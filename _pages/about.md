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
<h2>latest posts</h2>
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

<h2>talks & research experiences</h2>
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

<h2>projects</h2>
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
      <td style="width: 12%; padding: 12px 0; vertical-align: top;">
        <span style="background-color: #28a745; color: white; padding: 3px 6px; border-radius: 4px; font-size: 0.8em; font-weight: bold;">PROJ</span>
      </td>
      <td style="width: 58%; padding: 12px 15px 12px 0; vertical-align: top;">
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


<h2>publications</h2>
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

I am currently a Research Intern at the Cloud Computing Lab and HIPC Lab, IIT Delhi, where I focus on building and evaluating LLM-based tools that automatically generate OpenAPI specifications from source API code.

Before joining IIT Delhi, I completed my M.Sc in Mathematics and Computing at Banaras Hindu University (BHU), Varanasi, where I worked at the DST-CIMS. My Master’s thesis was centered around [Discrete Differential Geometry and its Applications](master-thesis.pdf), supervised by [Prof. Bankteshwar Tiwari](https://www.bhu.ac.in/Site/FacultyProfile/45_233?FA000189).

My academic journey began with a B.Sc (Hons) in Applied Mathematics from Jamia Millia Islamia, New Delhi. Along the way, I also pursued a **[Data Science Specialization](https://gist.github.com/ajeetkbhardwaj/8b032fe2edc7f64b6a4d2a4295241622)** through NPTEL (IIT Madras), strengthen my skills in **Programming, Data Analytics, Machine Learning and Large Language Models**.

My research interests lie at the intersection of

- Discrete Differential Geometry and its Applications
- Modeling Complex Systems and Simulations
- Data Science and Machine Learning

I’m deeply fascinated by how mathematical models and machine learning tools can work together to solve real-world problems and advance research in scientific computing and AI-driven automation.

---

Research Experiances
====================

## 0. Research Intern (IIT Delhi)

*Cloud Computing and HIPC Lab (June-Present)*

1. **LLM + OpenAPI Specification**

   - *An automated tool was already build that extracts URLs, HTTP methods, request handlers, and dependencies from API source code, integrates them into curated prompt templates, and leverages large language models (LLMs) to generate accurate OpenAPI specifications.*
   - *My major contribution on this project was to testing the tool on python api such as treeherder, education-backend and django-DefectDojo etc. Our tool out perform, the other existing static compilation based tools such as Respector etc.*
2. **Multi-Agents + OpenAPI Specification**

   - Build mult-agents system for the openapi specification generation from the given API source code.

## 1. [Quantum Research Intern (QWorld)](https://gist.github.com/ajeetkbhardwaj/6595815a2af97a9326ebdf4ebe41bd16)

*Online(July to August 2024)*

- Implemented the HHL algorithm using Qiskit to solve partial differential equations (PDEs), focusing on the Wave Equation.
- Designed and executed quantum circuits on both simulators and IBM Quantum hardware, scaling computations up to 50+ qubits.
- Explored advanced quantum algorithms such as Variational Quantum Algorithms (VQA), and Shor's Algorithm etc.

## 2. [Machine Learning Intern (Devtern)](https://gist.github.com/ajeetkbhardwaj/0e7c9f663c0582d3e39c509d0302c8e5)

*Online(Feb to April 2024)*

- Developed accurate ML models using Logistic Regression and Decision Trees for Heart Disease Prediction and House Price Estimation, achieving over 90% accuracy.
- Built end-to-end ML pipelines, incorporating model design, training, optimization, and deployment via API development.
- Performed data preprocessing, including cleaning, feature transformation, and exploratory data analysis (EDA) to uncover insights from complex datasets.
- Applied techniques such as feature engineering, hyperparameter tuning, and model evaluation to enhance performance and interpretability of solutions.

---

Skills
======

- **Programming :** Python, C/C++, MATLAB, Julia, Qiskit, Pennylane.
- **Tools and Frameworks :** PyTorch, FastAPI, MLFlow, PDEToolBox
- **Artificial Intelligence :** Building, Training, Evaluating and Deplyment of Models and LLMs based Tools and Functional Workflow Design.
- **Data Driven Decision Making :** Statistical methods, Optimization methods, machine learning methods and deep learning methods.
- **Soft Skills:** : Problem Solving, Collaborative, Analytical Thinking and Communication.
- **Mathematical Methods** : Optimization, Mathematical Modelling of Complex Systems and Scientific Simulations and many more...

---

[Certificates &amp; Key Cources](https://gist.github.com/ajeetkbhardwaj/bd49f3589dfbb076fb21b3e0eab25db7)
==============================

0. **Mathematics**

   - Pure: Linear & Abstract Algebra, Real & Complex Analysis, Functional Analysis, Differential Geometry, Differential Manifolds, Euclidean & Analytical Geometry and many more...
   - Applied: Numerical Methods, ODE & PDE, Vector Calculus, Dynamical Systems, Graph Theory, Classical Mechanics, Calculus of Variations, Integral Equations, Simulation & Modeling, Statistical Techniques, Mathematical Optimization and many more...
1. **Computer Science**

   - Programming, Data Structures, Algorithm Design & Analysis, Computation Theory, Data Analytics
   - Machine Learning, Deep Learning, Data Science, Big Data Systems, Artificial Intelligence & Applications
2. **Quantum Computing**

   - Quantum Programming with Qiskit, IBM Quantum Computing Challenge (2024), Qiskit Global Summer School (2023 & 2024)

Languages
=========

0. Mother toung - Awadhi + Bhojpuri
1. Hindi
2. English
3. Sanskrit
4. Urdu


Remarks : There are few sites 
1. [Interview Master 360](https://ajeetkbhardwaj.github.io/Interview-Master-360/)
2. [AI Systems](https://ajeetkbhardwaj.github.io/ai-systems)
3. [AI for Developers](https://ajeetkbhardwaj.github.io/ai-for-developers)
