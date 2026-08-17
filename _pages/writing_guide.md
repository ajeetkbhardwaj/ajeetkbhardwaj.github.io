---
permalink: /writing-guide/
title: "Content Writing Guide & Templates"
author_profile: true
---
Welcome to your complete guide for creating content on your modernized Jekyll site. This guide covers how to set up the Frontmatter (metadata) for different types of pages, and how to utilize the new modern CSS styling components.

---

## 1. Writing a Standard Blog Post

To create a new blog post, create a `.md` file inside the `_posts/` directory. The filename must follow the format `YYYY-MM-DD-title.md`.

### Post Frontmatter Template

Copy and paste this block at the very top of your `.md` file:

```yaml
---
title: "Your Amazing Post Title"
date: YYYY-MM-DD # e.g., 2026-08-17
permalink: /posts/YYYY/MM/your-amazing-post-title/
tags:
  - Tag1
  - Tag2
---
```

> **Tip**: The `permalink` should be unique and descriptive. It controls the final URL of your post.

---

## 2. Creating a Project Page

To add a new project to your portfolio, create a `.md` file inside the `_portfolio/` directory. The filename should be descriptive, like `YYYY-MM-DD-project-name.md`.

### Project Frontmatter Template

This template is used to generate the project cards on your "About" and "Projects" pages.

```yaml
---
title: "Project Title and Subtitle"
excerpt: "A short, one-sentence description of the project.<br/><img src='/images/portfolio/project-image.png' alt='Project Image'/>"
collection: portfolio
url: "https://github.com/your-repo/project"
category: "AI Systems"
---
```

- `title`: The main title of your project.
- `excerpt`: This is special. The text before the `<br/>` tag is used as the text description on the project card. The `<img>` tag provides the image for the card.
- `collection`: Must be `portfolio`.
- `url`: A link to the project (e.g., on GitHub).
- `category`: A category tag for the project.

---

## 3. Writing a Publication / Paper

To add a new publication, create a `.md` file inside the `_publications/` directory.

### Publication Frontmatter Template

Copy and paste this block at the very top of your `.md` file:

```yaml
---
title: "Paper Title Goes Here"
collection: publications
category: conferences # or "journals", "manuscripts"
permalink: /publication/YYYY-MM-DD-paper-title
date: YYYY-MM-DD
venue: 'Journal of Computer Science'
paperurl: '/files/paper.pdf'
slidesurl: '/files/slides.pdf'
bibtexurl: '/files/bibtex.txt'
citation: 'Your Name, A. (2026). "Paper Title." <i>Journal of Computer Science</i>.'
---
```

> **Note**: The `paperurl`, `slidesurl`, and `bibtexurl` fields automatically generate beautiful modern download buttons at the bottom of the article! Make sure the linked files exist in your `/files/` directory.

---

## 4. Using Modern UI Components

I have built modern UI systems directly into the site's CSS. Here is how you can use them in your Markdown files by adding HTML with specific classes.

### Modern Cards & Grids

You can create visually appealing cards and arrange them in grids. This is used on your "About" page for posts, projects, and research experience.

**Example for a list of items:**

```html
<div class="grid-layout">
  <div class="modern-card timeline-item">
    <div class="timeline-date">Jun 2025</div>
    <div class="timeline-content">
      <strong>Item Title</strong><br>
      <span style="color: var(--global-text-color-light);">A short description of the item.</span>
    </div>
  </div>
</div>
```

**Example for a grid of project cards:**

```html
<div class="project-grid">
  <div class="modern-card project-card">
    <!-- Content for project card -->
  </div>
</div>
```

### Buttons

To create a modern, pill-shaped button that links to another page, use the `btn--modern` class on an `<a>` tag.

```html
<a href="/portfolio/" class="btn--modern">View all Projects →</a>
```

### Badges

To add a small, colored badge (like the "PUB" badge on your publications list), use the `pill-badge` class.

```html
<span class="pill-badge">PUB</span>
```

### Blockquotes

To make a styled quote with a blue left-border and a subtle background tint, simply use the `>` character:

```markdown
> This is a very important quote that will stand out from the rest of the text.
```

### Links

Standard markdown links will automatically get the new hover-underline animation:

```markdown
This is a [beautiful animated link](https://google.com).
```

### Code Blocks & Copy Button

To create a block of code, use three backticks. It will automatically get syntax highlighting, rounded corners, a drop shadow, and a **"Copy" button**!

<pre>
```python
def hello_world():
    print("Modern UI is awesome!")
```
</pre>

### Mathematical Equations

We disabled the restrictive box formatting so your math flows naturally.

- For **Inline Math** (inside a sentence), wrap your LaTeX in single dollar signs: `$x_i \in \mathbb{R}^{d_m}$`.
- For **Block Math** (centered on its own line), wrap your LaTeX in double dollar signs: `$$ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} $$`

### Images

Any image you embed using standard markdown will automatically receive a soft drop-shadow and rounded corners:

```markdown
![Image Description](/images/my-cool-image.png)
```
