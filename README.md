<p align="center">
  <img src="src/favicon/android-chrome-192x192.png" alt="Compost the Workshop icon" width="96" height="96">
</p>

<h1 align="center">Compost the Workshop</h1>

<p align="center"><em>Rewilding creative writing in the Anthropocene.</em></p>

<p align="center">
  <a href="https://medium.com/@brennanbrown/how-to-rewild-your-writing-practice-21a8da9e1452?sk=bde0f9f367a73456c28122d51b5a5179">Read the essay on Medium</a>
  · <a href="#running-the-site-locally">Run the site</a>
  · <a href="#rewild-journal-cli">Rewild Journal CLI</a>
  · <a href="#project-structure">Project structure</a>
  · <a href="#support">Support</a>
  · <a href="#funding">Funding</a>
</p>

---

This repository contains an Eleventy-based static site and supporting tools that translate the essay **"Compost the Workshop: Rewilding Creative Writing in the Anthropocene"** into a small, accessible web experience.

The project offers:

- A framework for rewilding creative writing pedagogy.
- A growing library of ecological writing practices.
- A flexible **Wild Minds** workshop model.
- Notes on access and disabled ecologies.
- A reading list drawn from environmental humanities, Indigenous and queer ecologies, and disability studies.
- An experimental **terminal-based journaling tool** for students.

The public site is intended to live at: **https://rewilding.netlify.app**.

---

## Tech stack

- **Site:** [Eleventy](https://www.11ty.dev/) (static site generator)
- **Templating:** Nunjucks + Markdown
- **Styling:** [Tailwind CSS](https://tailwindcss.com/) with the Typography plugin
- **Deployment:** Netlify (via `netlify.toml`)
- **CLI tools:** Python 3 (simple journaling CLI in `cli/`)

---

## Running the site locally

### Prerequisites

- Node.js (LTS recommended)

### Install dependencies

From the project root:

```bash
npm install
```

### Run a development server

```bash
npm run start
```

This will:

- Build Tailwind CSS from `src/tailwind.css` into `src/styles.css`.
- Run Tailwind in `--watch` mode.
- Start the Eleventy dev server (typically at `http://localhost:8080`).

### Build for production

```bash
npm run build
```

The static site will be generated into the `_site/` directory.

---

## Project structure

- `docs/`
  - `SITE-SPEC.md` – design spec for the site.
  - `TODO.md` – project task list.
  - `SUPPORT.md` – support and troubleshooting notes.
  - `FUNDING.md` – ways to support the project.
  - `CONTRIBUTING.md` – guidelines for contributing.
  - `rewild-essay.md` – the underlying essay text.
- `CHANGELOG.md` – versioned change log.
- `.eleventy.js` – Eleventy configuration (collections and asset passthroughs).
- `netlify.toml` – Netlify build and dev settings.
- `robots.txt` / `sitemap.xml` – generated and/or passed through from `src/`.

### Site source (`src/`)

- `_data/`
  - `site.json` – site metadata (title, description, base URL, author).
  - `nav.json` – main navigation items.
- `_includes/layouts/`
  - `base.njk` – single shared layout with header, navigation, main, and footer.
- `styles.css` – compiled Tailwind CSS (do not edit directly; edit `tailwind.css`).
- `tailwind.css` – Tailwind source file (base, components, utilities, and custom classes).
- `index.md` – home page with an initial attunement practice.
- `framework/`
  - `index.md` – overview of the five-strand framework.
  - `ecology-of-mind.md` – strand page.
  - `nature-as-text.md` – strand page.
  - `indigenous-and-queer-lenses.md` – strand page.
  - `access-in-wilderness.md` – strand page.
  - `wild-minds-workshop.md` – strand page.
- `practices/`
  - `index.md` – dynamic listing of all practices.
  - `freewriting-as-rewilding.md`
  - `succession-writing.md`
  - `watershed-writing.md`
  - `mycelial-networks.md`
  - `composting-revision.md`
  - `writing-with-the-cycles.md`
  - `field-journal-nature-as-text.md`
- `workshop/`
  - `index.md` – Wild Minds overview with a 6-session arc.
  - `session-1-ecology-of-mind.md`
  - `session-2-nature-as-text.md`
  - `session-3-indigenous-queer.md`
  - `session-4-disabled-ecologies.md`
  - `session-5-composting-succession.md`
  - `session-6-reflection-futures.md`
- `access.md` – Access and Ecologies page.
- `resources.md` – reading list.
- `about.md` – About page for Brennan Kenneth Brown.
- `404.md` – custom not-found page.
- `robots.txt` – robots policy (passed through to `_site`).
- `sitemap.xml.njk` – template for the generated sitemap.

### CLI tools (`cli/` and `rewild.py`)

- `rewild.py` – small wrapper script that calls the Rewild Journal CLI.
- `cli/`
  - `__init__.py` – package marker.
  - `rewild_journal/`
    - `__init__.py` – exposes `main` for import.
    - `cli.py` – implementation of the journal CLI.

The CLI is intentionally separated into a package so it can be tested or reused later.

---

## Rewild Journal CLI

The Rewild Journal CLI is an experimental terminal tool for capturing place-based journal entries aligned with the projects pedagogy.

### Prerequisites

- Python 3.9 or newer is recommended.

### Running the CLI

From the project root:

```bash
python rewild.py
```

Optional arguments:

```bash
python rewild.py --output-dir ./journals
```

You will be prompted for:

- Name (required)
- Course / group (optional)
- Practice / prompt name (optional)
- Location
- Weather / atmosphere (optional)
- More-than-human presences (multi-line)
- Sensory notes (multi-line)
- Freewriting (multi-line)

For the multi-line sections, type as many lines as you like, then enter a single `.` on its own line to finish.

### Output

- Markdown files are saved under the chosen output directory (default: `./journals`).
- Filenames include a timestamp and a slug of the student name, for example:
  - `20251203-183500-brennan-kenneth-brown.md`
- Each file contains YAML-like front matter (student, course, practice, location, weather, created_at) and three sections:
  - More-than-human presences
  - Sensory notes
  - Freewriting

These files can be committed with the project, shared with instructors, or adapted into site content in future iterations.

---

## Deployment

This project is configured for deployment on **Netlify**.

- `netlify.toml` specifies:
  - Build command: `npm run build`
  - Publish directory: `_site`
  - Dev command/ports for `netlify dev`.
- `src/_data/site.json` includes the base URL used for canonical and Open Graph tags:
  - `https://rewilding.netlify.app`

To deploy:

1. Push this repository to a Git provider (GitHub, GitLab, etc.).
2. Create a new site on Netlify from that repository.
3. Ensure the site name (or custom domain) matches your desired URL.

Netlify will run `npm run build` and serve the contents of `_site/`.

---

## Support

If you run into issues or have questions:

- See **`SUPPORT.md`** for detailed guidance on getting help with the site and CLI.
- Check `TODO.md` and `CHANGELOG.md` to see if your concern is already noted.
- For bugs or feature requests, use the repositorys issue tracker.
- For more personal or access-related concerns, you can email **mail@brennanbrown.ca**.

## Funding

If you would like to support the work behind this project (writing, pedagogy design, accessibility work, and tooling), there are several options:

- See **`FUNDING.md`** for up-to-date links and details.
- Direct support via Ko-fi, Patreon, or GitHub Sponsors.
- Purchasing books or digital resources listed in `FUNDING.md`.

If financial support isnt possible, sharing the project, crediting it when you adapt exercises, or sending thoughtful feedback is equally appreciated.

## Notes and further work

- See `TODO.md` for remaining or future enhancements.
- Practices, framework pages, and workshop sessions are intended to evolve alongside the underlying essay.
- The CLI is experimental; it may grow to support multiple practice templates or integrate with the site in later versions.
