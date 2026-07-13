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
date: YYYY-MM-DD
permalink: /posts/YYYY/MM/title/
tags:
  - Tag1
  - Tag2
---
```

---

## 2. Writing a Publication / Paper

To add a new publication, create a `.md` file inside the `_publications/` directory.

### Publication Frontmatter Template
Copy and paste this block at the very top of your `.md` file:
```yaml
---
title: "Paper Title Goes Here"
collection: publications
category: conferences
permalink: /publication/YYYY-MM-DD-paper-title
date: YYYY-MM-DD
venue: 'Journal of Computer Science'
paperurl: 'http://academicpages.github.io/files/paper.pdf'
slidesurl: 'http://academicpages.github.io/files/slides.pdf'
bibtexurl: 'http://academicpages.github.io/files/bibtex.txt'
citation: 'Kumar, Ajeet. (2026). "Paper Title." <i>Journal of Computer Science</i>.'
---
```
> **Note**: The `paperurl`, `slidesurl`, and `bibtexurl` fields automatically generate the beautiful modern download buttons at the bottom of the article!

---

## 3. Formatting Modern Content

I have built modern UI systems directly into the site's CSS. Here is how you trigger them natively in Markdown:

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
To create a block of code, use three backticks. It will automatically get the syntax highlighting, rounded corners, drop shadows, and the **"Copy" button**!
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
