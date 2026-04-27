---
title: 'Automated LaTeX Research Writing Environment'
date: 2026-04-27
permalink: /posts/2026/04/27-automated-latex-research-writing-environment/
tags:
  - Research
  - Collaborations
  - Writing
  - Systems
---
>  **"Write-Once, Compile-Anywhere"** — A containerized academic paper workflow using Docker, VSCode, and TeX Live.

Writing research papers in LaTeX has one persistent problem: every collaborator has a different local TeX installation, causing packages to break, fonts to go missing, and hours lost to environment debugging. This project solves that permanently by encapsulating the entire TeX Live engine inside a **Docker Dev Container**, giving every author — on any machine — an identical, reproducible environment.

---

## Table of Contents

1. [The Problem This Solves](#1-the-problem-this-solves)
2. [System Architecture](#2-system-architecture)
3. [Project Structure](#3-project-structure)
4. [The Dev Container: `.devcontainer/devcontainer.json`](#4-the-dev-container-devcontainerjson)
   - [Base Image](#41-base-image)
   - [VSCode Extensions &amp; Settings](#42-vscode-extensions--settings)
   - [The Two-Tool Recipe: `latexmk` + `copy_pdf`](#43-the-two-tool-recipe-latexmk--copy_pdf)
   - [Lifecycle Hooks](#44-lifecycle-hooks)
5. [Package Management: `tex-packages.txt`](#5-package-management-tex-packagestxt)
6. [The Root Document: `main.tex`](#6-the-root-document-maintex)
   - [Package Stack Explained](#61-package-stack-explained)
   - [Author &amp; Metadata Block](#62-author--metadata-block)
   - [Document Body &amp; Input Structure](#63-document-body--input-structure)
7. [The Style Engine: `arxiv.sty`](#7-the-style-engine-arxivsty)
   - [Page Geometry](#71-page-geometry)
   - [Running Headers with fancyhdr](#72-running-headers-with-fancyhdr)
   - [Custom Title Rendering](#73-custom-title-rendering)
   - [Abstract Styling](#74-abstract-styling)
   - [Typography Tuning](#75-typography-tuning)
8. [Writing Sections Modularly](#8-writing-sections-modularly)
9. [The Full Compilation Pipeline](#9-the-full-compilation-pipeline)
10. [Day-to-Day Workflow](#10-day-to-day-workflow)
11. [Extending the Template](#11-extending-the-template)

---

## 1. The Problem This Solves

Academic LaTeX setups suffer from three chronic issues:

| Problem                         | Symptom                                              | Root Cause                              |
| ------------------------------- | ---------------------------------------------------- | --------------------------------------- |
| **Environment Drift**     | `! LaTeX Error: File 'cleveref.sty' not found`     | Different TeX Live versions per machine |
| **Junk File Pollution**   | `.aux`, `.log`, `.out` files everywhere in git | No output directory isolation           |
| **Auto-compile Slowness** | Editor freezes during large documents                | Auto-build on every keystroke           |

This project addresses all three:

- **Docker** locks the TeX Live version across all machines.
- **`.tmp/` output dir** keeps auxiliary files out of the working tree.
- **Manual compilation** (`autoBuild.run: "never"`) keeps the editor responsive.

---

## 2. System Architecture

```mermaid
graph TD
    classDef ide fill:#0984e3,stroke:#74b9ff,stroke-width:2px,color:#ffffff;
    classDef container fill:#00b894,stroke:#55efc4,stroke-width:2px,color:#ffffff;
    classDef action fill:#fdcb6e,stroke:#ffeaa7,stroke-width:2px,color:#2d3436;

    subgraph Your_Local_Machine
        VSC["VSCode<br>────────<br>• LaTeX Workshop<br>• GitLens"]:::ide
        Doc["Docker Dev Container<br>(qmcgaw/latexdevcontainer)<br>────────<br>• TeX Live 2026<br>• latexmk, tlmgr<br>• BibTeX, synctex"]:::container
  
        Edit["Edit .tex files<br>in sections/"]:::action
        Compile["Compile to PDF<br>────────<br>output → .tmp/<br>copy → main.pdf"]:::action
    end

    VSC <-->|"Volume Mount / RPC"| Doc
    VSC --> Edit
    Doc --> Compile
  
    style Your_Local_Machine fill:#fdfdfd,stroke:#b2bec3,stroke-width:2px,color:#2d3436
```

**Component roles:**

| Component                              | Role                                                           |
| -------------------------------------- | -------------------------------------------------------------- |
| **Docker**                       | Isolates TeX Live — no local installation needed              |
| **`qmcgaw/latexdevcontainer`** | Pre-built image with full TeX Live + latexmk                   |
| **VSCode Dev Containers**        | Tunnels your editor into the container filesystem              |
| **LaTeX Workshop**               | Handles keyboard-triggered compilation and PDF preview         |
| **`tlmgr`**                    | TeX Live package manager — installs from `tex-packages.txt` |
| **GitLens**                      | Co-author collaboration and blame tracking                     |

---

## 3. Project Structure

```
latex-template/
├── .devcontainer/
│   └── devcontainer.json      # Container + editor configuration
├── sections/
│   ├── 00-abstract.tex        # Abstract content
│   ├── 01-introduction.tex    # Section 1
│   ├── 02-methodology.tex     # Section 2
│   └── 03-results.tex         # Section 3
├── bib/
│   └── references.bib         # BibTeX bibliography database
├── figures/                   # All images/charts (referenced via \includegraphics)
├── .tmp/                      # Auto-generated: .aux, .log, .out, .synctex.gz
├── arxiv.sty                  # Custom arXiv-style LaTeX class
├── main.tex                   # Root document (wiring only — no content here)
├── main.pdf                   # Final compiled output
└── tex-packages.txt           # One package name per line
```

> **Rule**: Never write paper content in `main.tex`. It is configuration only — title, authors, `\input{}` commands, and bibliography. All prose goes into `sections/`.

This separation prevents merge conflicts when two authors edit different sections simultaneously.

---

## 4. The Dev Container: `devcontainer.json`

This single JSON file is the heart of the entire system. It tells VSCode exactly what Docker image to use, which extensions to install, and what commands to run at startup.

```json
{
  "name": "Lightweight LaTeX Project",
  "image": "qmcgaw/latexdevcontainer:latest",
  ...
}
```

### 4.1 Base Image

```json
"image": "qmcgaw/latexdevcontainer:latest"
```

`qmcgaw/latexdevcontainer` is a purpose-built Docker image containing:

- **TeX Live** (full distribution)
- **latexmk** — a Perl-based build tool that runs pdflatex/bibtex the right number of times automatically
- **synctex** — enables click-to-source navigation between PDF and `.tex` file
- **tlmgr** — the TeX Live package manager

Using `:latest` ensures you always get the most recent TeX Live snapshot. Pin to a specific tag (e.g., `:2026`) for reproducibility in long-running projects.

---

### 4.2 VSCode Extensions & Settings

```json
"extensions": [
  "James-Yu.latex-workshop",   // Compilation, PDF preview, snippets
  "eamodio.gitlens"            // Git blame, history, collaboration
],
"settings": {
  "latex-workshop.latex.autoBuild.run": "never",   // Manual only
  "latex-workshop.view.pdf.viewer": "tab",          // PDF in editor tab
  "latex-workshop.latex.outDir": ".tmp",            // Isolate aux files
  "files.autoSave": "off"                           // Don't trigger builds on idle save
}
```

**Why `autoBuild.run: "never"`?**

Auto-build fires the compiler on every save. For large documents with bibliography passes, this can take 10–30 seconds. Manual compilation (`Cmd+Opt+B`) gives you control — compile when *you* are ready, not when the editor decides.

**Why `outDir: ".tmp"`?**

By redirecting all auxiliary output to `.tmp/`, your working directory stays clean. The `.gitignore` excludes `.tmp/` entirely, so collaborators never see your intermediate files.

---

### 4.3 The Two-Tool Recipe: `latexmk` + `copy_pdf`

The compilation pipeline is defined as a **recipe** — an ordered list of tools:

```json
"latex-workshop.latex.recipes": [
  {
    "name": "latexmk_and_copy",
    "tools": ["latexmk", "copy_pdf"]
  }
]
```

**Tool 1 — `latexmk`**: Compiles the document

```json
{
  "name": "latexmk",
  "command": "latexmk",
  "args": [
    "-pdf",                    // Produce PDF output
    "-f",                      // Force compilation even on errors
    "-interaction=nonstopmode",// Don't pause for user input on errors
    "-synctex=1",              // Enable click-to-source sync
    "-outdir=.tmp",            // Send all aux files to .tmp/
    "%DOC%"                    // Placeholder for main.tex path
  ]
}
```

`latexmk` is smarter than running `pdflatex` manually. It detects whether a bibliography pass (`bibtex`/`biber`) is needed, and re-runs pdflatex until all cross-references are resolved — automatically.

**Tool 2 — `copy_pdf`**: Moves the output to the project root

```json
{
  "name": "copy_pdf",
  "command": "cp",
  "args": [
    ".tmp/%DOCFILE%.pdf",   // Source: inside the hidden .tmp/ dir
    "./%DOCFILE%.pdf"       // Destination: project root (main.pdf)
  ]
}
```

Since `latexmk` sends output to `.tmp/`, the final PDF would be buried there. This second tool copies it back to the project root so it is easy to find, share, and commit.

---

### 4.4 Lifecycle Hooks

```json
"postCreateCommand": "tlmgr update --self && if [ -f tex-packages.txt ]; then tlmgr install $(cat tex-packages.txt); fi",
"postStartCommand": "rm -rf .tmp"
```

**`postCreateCommand`** — runs once when the container is first created:

1. Updates `tlmgr` itself
2. Reads `tex-packages.txt` and installs every package listed

This means adding a package is as simple as adding its name to `tex-packages.txt` and rebuilding the container — no `sudo tlmgr install` magic required.

**`postStartCommand`** — runs every time the container starts:

- Cleans the `.tmp/` directory, ensuring every compilation starts fresh

---

## 5. Package Management: `tex-packages.txt`

```
amsmath
amsfonts
graphicx
hyperref
geometry
fancyhdr
booktabs
microtype
cleveref
lipsum
natbib
doi
url
times
units
```

Each line is a TeX Live package name, installed via `tlmgr install`. The `postCreateCommand` reads this file with:

```bash
tlmgr install $(cat tex-packages.txt)
```

**What each package does:**

| Package                    | Purpose                                                                   |
| -------------------------- | ------------------------------------------------------------------------- |
| `amsmath` / `amsfonts` | Mathematical symbols, environments (`align`, `equation`)              |
| `graphicx`               | `\includegraphics{}` for figures                                        |
| `hyperref`               | Clickable links, PDF metadata (`pdftitle`, `pdfauthor`)               |
| `geometry`               | Page margins and layout                                                   |
| `fancyhdr`               | Custom running headers and footers                                        |
| `booktabs`               | Professional-quality tables (`\toprule`, `\midrule`, `\bottomrule`) |
| `microtype`              | Subtle kerning and font expansion for better typography                   |
| `cleveref`               | Smart cross-references:`\cref{fig:1}` → "Figure 1" automatically       |
| `natbib`                 | Author-year citation styles (`\citep{}`, `\citet{}`)                  |
| `doi`                    | Clickable DOI links in bibliography                                       |
| `times`                  | Times New Roman font (matches arXiv preprint style)                       |
| `units`                  | Consistent formatting for physical units                                  |

---

## 6. The Root Document: `main.tex`

`main.tex` is the **wiring harness** of the paper. It loads packages, sets metadata, and stitches together section files — but contains zero paper content itself.

### 6.1 Package Stack Explained

```latex
\documentclass{article}

% Load the arXiv style
\usepackage{arxiv}

\usepackage[utf8]{inputenc}   % Accept UTF-8 source files (accented chars, symbols)
\usepackage[T1]{fontenc}      % Use modern 8-bit font encoding for proper PDF glyphs
\usepackage{hyperref}         % Clickable links + PDF metadata
\usepackage{url}              % Format URLs properly
\usepackage{booktabs}         % Professional tables
\usepackage{amsfonts}         % \mathbb{R}, \mathcal{L}, etc.
\usepackage{nicefrac}         % Inline fractions: \nicefrac{1}{2} → ½
\usepackage{microtype}        % Optical margin alignment and font expansion
\usepackage{cleveref}         % Smart cross-references
\usepackage{graphicx}         % Figure inclusion
\usepackage{natbib}           % Author-year citations
\usepackage{doi}              % DOI hyperlinks

\graphicspath{{figures/}}     % All \includegraphics{} searches here
```

The **load order matters**. `hyperref` must come after most other packages but before `cleveref`. `cleveref` must always be loaded last among cross-referencing packages. This order is already correct in the template.

---

### 6.2 Author & Metadata Block

```latex
\title{Advanced Numerical Methods for Partial Differential Equations}

\author{
  \href{https://orcid.org/0000-0000-0000-0000}{\includegraphics[scale=0.06]{ocid.jpg}}
  \hspace{1mm}Ajeet Kumar Bhardwaj\thanks{Corresponding author.} \\
  Department of Applied Mathematics\\
  Your University Name\\
  \texttt{your.email@university.edu} \\
  \And
  Co-Author Name \\
  Department of Physics\\
  Another University\\
  \texttt{coauthor@university.edu} \\
}

\renewcommand{\shorttitle}{Advanced Numerical Methods}

\hypersetup{
  pdftitle={Advanced Numerical Methods for PDEs},
  pdfsubject={math.NA},
  pdfauthor={Ajeet KB, Co-Author},
  pdfkeywords={Numerical Methods, PDEs, Discrete Geometry},
}
```

Key points:

- **`\And`** separates multiple authors in the arXiv style (single line) — `\AND` forces a line break between author groups.
- **`\thanks{}`** creates a footnote — used for corresponding author markers.
- **`\shorttitle`** populates the running header on subsequent pages (defined in `arxiv.sty`).
- **`\hypersetup`** embeds metadata directly in the PDF file — essential for indexing by Google Scholar and arXiv.

---

### 6.3 Document Body & Input Structure

```latex
\begin{document}
\maketitle

\begin{abstract}
    \input{sections/00-abstract}
\end{abstract}

\keywords{Numerical Methods \and PDEs \and Discrete Geometry}

\input{sections/01-introduction}
\input{sections/02-methodology}
\input{sections/03-results}

\bibliographystyle{unsrtnat}
\bibliography{bib/references}

\end{document}
```

`\input{}` is a simple textual inclusion — it pastes the file contents at that point. This is different from `\include{}` which adds page breaks and has caching behavior. For modular sections, `\input{}` is the right choice.

**Section file naming convention:**

```
sections/
├── 00-abstract.tex       # \begin{abstract}...\end{abstract} content
├── 01-introduction.tex   # \section{Introduction}
├── 02-methodology.tex    # \section{Methodology}
└── 03-results.tex        # \section{Results}
```

The numeric prefix (`00-`, `01-`) keeps files sorted in filesystem order matching paper order — crucial when multiple authors are browsing the directory.

---

## 7. The Style Engine: `arxiv.sty`

`arxiv.sty` is a custom LaTeX style file that replicates the arXiv preprint look. It overrides default `article` class geometry, typography, and title rendering.

### 7.1 Page Geometry

```latex
\usepackage[verbose=true,letterpaper]{geometry}
\AtBeginDocument{
  \newgeometry{
    textheight=9in,
    textwidth=6.5in,
    top=1in,
    headheight=14pt,
    headsep=25pt,
    footskip=30pt
  }
}
```

`\AtBeginDocument{}` defers the geometry call until after all packages load — preventing packages like `hyperref` from overriding these settings. This sets standard US letter margins matching the arXiv PDF format.

```latex
\widowpenalty=10000   % Forbid widows (single line at top of page)
\clubpenalty=10000    % Forbid orphans (single line at bottom of page)
\flushbottom          % Force all pages to same height
\sloppy               % Relax line-breaking strictness (reduces overfull \hboxes)
```

### 7.2 Running Headers with fancyhdr

```latex
\usepackage{fancyhdr}
\fancyhf{}                              % Clear all header/footer fields
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0.4pt}    % Thin rule below header

\rhead{\scshape \footnotesize \headeright}   % Right: "A Preprint"
\chead{\shorttitle}                           % Center: short title
\cfoot{\thepage}                              % Center footer: page number
```

The three commands `\rhead`, `\chead`, `\cfoot` define a three-zone header/footer. `\shorttitle` is the custom command set in `main.tex` via `\renewcommand{\shorttitle}{...}`.

### 7.3 Custom Title Rendering

The `\@maketitle` redefinition is the most complex part of `arxiv.sty`:

```latex
\renewcommand{\@maketitle}{ 
  \vbox{
    \hsize\textwidth
    \vskip 0.1in
    \@toptitlebar          % Horizontal rule above title
    \centering
    {\LARGE\sc \@title\par}   % Title: large + small caps
    \@bottomtitlebar       % Horizontal rule below title
    \textsc{\undertitle}\\ % "A Preprint" subtitle
    \vskip 0.1in
    % Author table (supports \And and \AND separators)
    \begin{tabular}[t]{c}\bf\rule{\z@}{24pt}\@author\end{tabular}
  }
}
```

`\@toptitlebar` and `\@bottomtitlebar` are internal commands that draw `2pt`-thick horizontal rules framing the title — the visual signature of arXiv preprints.

### 7.4 Abstract Styling

```latex
\renewenvironment{abstract}
{
  \centerline{\large \bfseries \scshape Abstract}
  \begin{quote}
}
{
  \end{quote}
}
```

Replaces the default `abstract` environment. The title "Abstract" is rendered centered, bold, and in small caps. The body is wrapped in `\begin{quote}` for indentation.

### 7.5 Typography Tuning

```latex
% Compact section spacing
\renewcommand{\section}{
  \@startsection{section}{1}{\z@}
    {-2.0ex \@plus -0.5ex \@minus -0.2ex}  % Space above
    { 1.5ex \@plus  0.3ex \@minus  0.2ex}   % Space below
    {\large\bf\raggedright}            % Font style
}
```

The space parameters use `\@plus` / `\@minus` for **rubber lengths** — TeX's elastic spacing that allows the layout engine to compress or expand spacing within given tolerances to avoid overfull pages.

Font sizes are explicitly redefined to match arXiv's compact style:

```latex
\renewcommand{\normalsize}{\@setfontsize\normalsize\@xpt\@xipt}  % 10pt / 11pt leading
\renewcommand{\large}{\@setfontsize\large\@xiipt{14}}            % 12pt / 14pt leading
\renewcommand{\LARGE}{\@setfontsize\LARGE\@xviipt{20}}           % 17pt / 20pt leading
```

---

## 8. Writing Sections Modularly

Each section file is a standalone LaTeX fragment:

**`sections/00-abstract.tex`**

```latex
This is the abstract for the preprint. It summarizes the research findings and methodology.
```

No `\begin{abstract}` — that wrapper lives in `main.tex`. The section file is just the prose.

**`sections/01-introduction.tex`**

```latex
\section{Introduction}
\label{sec:intro}

Welcome to the lightweight LaTeX collaboration environment.
Start typing here. Press \texttt{Ctrl+Alt+B} (or \texttt{Cmd+Opt+B} on Mac)
to manually compile your document.
```

**Cross-referencing between sections:**

```latex
% In 02-methodology.tex
As described in \cref{sec:intro}, the problem is well-posed.

% In 03-results.tex
\begin{figure}[ht]
  \centering
  \includegraphics{convergence_plot}   % loads figures/convergence_plot.pdf/.png
  \caption{Convergence of the numerical scheme.}
  \label{fig:convergence}
\end{figure}

As shown in \cref{fig:convergence}, the method converges at order $\mathcal{O}(h^2)$.
```

`\cref{}` from the `cleveref` package automatically prepends "Figure", "Section", "Table", etc., based on the label prefix — no manual "Figure~\ref{}" needed.

**Citations:**

```latex
% bib/references.bib
@article{smith2023,
  author  = {Smith, J.},
  title   = {Numerical Methods for PDEs},
  journal = {J. Comput. Math.},
  year    = {2023},
  volume  = {41},
  pages   = {1--20},
  doi     = {10.1000/xyz123}
}

% In any section file:
Recent work by \citet{smith2023} shows that...   % Smith (2023) shows that...
This is a known result \citep{smith2023}.         % (Smith, 2023)
```

---

## 9. The Full Compilation Pipeline

When you press `Cmd+Opt+B`, this happens:

```
1. latexmk starts
   │
   ├── pdflatex main.tex         (pass 1: resolves \labels, writes .aux)
   ├── bibtex .tmp/main           (resolves \cite{} → bibliography entries)
   ├── pdflatex main.tex         (pass 2: inserts bibliography)
   └── pdflatex main.tex         (pass 3: resolves all cross-references)
   │
   Output: .tmp/main.pdf
   │
2. copy_pdf runs
   └── cp .tmp/main.pdf ./main.pdf

Final: main.pdf in project root ✓
```

**Why 3 pdflatex passes?**

LaTeX resolves references in two phases:

- **Pass 1**: Writes label positions to `.aux`
- **Pass 2** (after bibtex): Inserts bibliography numbers
- **Pass 3**: Uses updated `.aux` to correctly number all `\ref{}` and `\cref{}` calls

`latexmk` detects when references stabilize and stops automatically.

---

## 10. Day-to-Day Workflow

### First-Time Setup

```bash
# 1. Clone the repo
git clone https://github.com/ajeetkbhardwaj/latex-template
cd latex-template

# 2. Open in VSCode
code .
# → Click "Reopen in Container" when prompted
# → Wait for Docker image pull + tlmgr package install (~2-5 min first time)
```

### Writing

```bash
# Edit a section
# open sections/02-methodology.tex
# write your content

# Compile
# Mac:           Cmd + Opt + B
# Windows/Linux: Ctrl + Alt + B

# View PDF
# Mac:           Cmd + Opt + V
```

### Adding a Package

```bash
# 1. Add to tex-packages.txt
echo "pgfplots" >> tex-packages.txt

# 2. Rebuild container
# Cmd+Shift+P → "Dev Containers: Rebuild Container"

# 3. Use in main.tex
# \usepackage{pgfplots}
```

### Collaboration & Git

```bash
# End of session — push your changes
git add sections/02-methodology.tex bib/references.bib
git commit -m "Drafted methodology section, added 3 citations"
git push origin main
```

> **Tip**: Commit individual section files separately. Your co-authors can pull changes to `sections/01-introduction.tex` without conflicting with your edits to `sections/02-methodology.tex`.

### Clean Compile

```bash
# If compilation behaves strangely, force a clean rebuild:
rm -rf .tmp
# Then Cmd+Opt+B
```

The `postStartCommand` in `devcontainer.json` does this automatically on container restart.

---

## 11. Extending the Template

### Add a New Section

```bash
# 1. Create the file
touch sections/04-discussion.tex

# 2. Add content
cat > sections/04-discussion.tex << 'EOF'
\section{Discussion}
\label{sec:discussion}

Your discussion content here.
EOF

# 3. Wire it into main.tex
# Add: \input{sections/04-discussion}
# before \bibliographystyle{...}
```

### Add Math Environments

```latex
% Numbered equation
\begin{equation}
  \label{eq:heat}
  \frac{\partial u}{\partial t} = \alpha \nabla^2 u
\end{equation}

% Multi-line aligned (requires amsmath)
\begin{align}
  \nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \label{eq:gauss} \\
  \nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align}

% Reference it anywhere
See \cref{eq:heat} for the heat equation.
```

### Add Figures

```bash
# Place image in figures/
cp my_plot.pdf figures/convergence_plot.pdf
```

```latex
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.8\textwidth]{convergence_plot}
  \caption{Convergence rate of the proposed scheme.}
  \label{fig:convergence}
\end{figure}
```

### Add a Table

```latex
\begin{table}[ht]
  \centering
  \caption{Comparison of methods.}   % Caption ABOVE for tables (booktabs convention)
  \label{tab:comparison}
  \begin{tabular}{lcc}
    \toprule
    Method       & Order & Runtime (s) \\
    \midrule
    Euler        & 1     & 0.12        \\
    Runge-Kutta  & 4     & 0.45        \\
    Adams-Bashforth & 3  & 0.31        \\
    \bottomrule
  \end{tabular}
\end{table}
```

### Change Citation Style

```latex
% In main.tex, change:
\bibliographystyle{unsrtnat}   % Numbered, sorted by appearance

% Options:
% plainnat   → [1] numbered, sorted alphabetically
% abbrvnat   → abbreviated author names
% ieeenat    → IEEE style
% apalike    → APA author-year
```

---

## Summary

This template gives you a production-grade academic writing environment in under 5 minutes. The key design decisions are:

1. **Docker isolation** → zero "works on my machine" problems
2. **Modular `sections/`** → merge-conflict-free collaboration
3. **`.tmp/` output dir** → clean working tree, clean git history
4. **Manual compilation** → fast, responsive editor
5. **`tex-packages.txt`** → declarative, team-shared package management
6. **`arxiv.sty`** → professional preprint formatting without NeurIPS/ICML class files

---

*Built for academic researchers · Docker + VSCode + TeX Live · arXiv preprint style*

### Citation

```bibtex
@software{latex-template,
  title={Automated LaTeX Research Writing Environment},
  author={Ajeet Kumar},
  profile={https://ajeetkbhardwaj.github.io},
  year={2026},
  url={https://github.com/ajeetkbhardwaj/latex-template},
  license={MIT}
}
```
