# Academic Website

This repository contains the source code for my personal academic and professional portfolio, available at [ajeetkbhardwaj.github.io](https://ajeetkbhardwaj.github.io/).

The site is built using [Jekyll](https://jekyllrb.com/) and is based on the [Academic Pages](https://academicpages.github.io/) theme. It serves as a central hub for my blog posts, project portfolio, and publications.

## Content

The website features a variety of content, including:

- **Blog Posts**: In-depth articles on topics like C programming, custom build systems, AI/ML model optimization, and research writing environments.
- **Portfolio**: A showcase of my data science and machine learning projects.
- **Publications**: A list of my academic papers and manuscripts.

For a guide on how to add or edit content, please see the Content Writing Guide.

## Local Development

You can preview changes locally before pushing them to GitHub by running a local Jekyll server.

### Prerequisites

1. Make sure you have Ruby, Bundler, and Node.js installed.

   On Debian/Ubuntu-based systems:

   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install ruby-dev ruby-bundler nodejs
   ```

   On macOS (using Homebrew):

   ```bash
   brew install ruby
   brew install node
   gem install bundler
   ```
2. Install the required Ruby gems from the `Gemfile`:

   ```bash
   bundle install
   ```

   If you encounter permission errors, you can install the gems locally:

   ```bash
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```

### Serving the Site

Run the Jekyll server:

```bash
bundle exec jekyll serve -l -H localhost
```

The site will be available at `http://localhost:4000`. The server will automatically rebuild and refresh pages when you make changes to the source files.

## Using Docker

As an alternative to installing dependencies locally, you can use Docker to run the site in a container.

### Docker Compose

1. Ensure you have Docker installed.
2. Build and run the container:
   ```bash
   docker-compose build --no-cache
   docker compose up
   docker compose down
   ```

The site will be accessible at `http://localhost:4000`.

### VS Code Dev Container

If you use Visual Studio Code, you can use the Dev Container feature. VS Code should prompt you to "Reopen in Container". This will set up the environment and serve the site for you automatically.

## Deployment

The site is automatically deployed via GitHub Pages whenever changes are pushed to the `main` branch of this repository.

---

 *This site is based on the Academic Pages template, which was forked from the Minimal Mistakes Jekyll Theme.*
