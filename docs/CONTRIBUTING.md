# Contributing

Thank you for your interest in contributing to **Compost the Workshop**.

This project combines an Eleventy-based static site with a small Python journaling CLI. Contributions that improve accessibility, clarity, pedagogy, or tooling are all welcome.

## Ways to contribute

- **Content and pedagogy**
  - Suggest clarifications or expansions for framework, practices, or workshop pages.
  - Propose new practices aligned with the existing strands and access commitments.
- **Accessibility and design**
  - Report issues with contrast, keyboard navigation, motion, or screen readers.
  - Suggest layout or copy changes that make the site more welcoming.
- **Code and tooling**
  - Improve Eleventy/Tailwind configuration.
  - Enhance the Rewild Journal CLI or its tests.
  - Refine CI, packaging, or documentation.

## Development setup

### Prerequisites

- **Node.js** (LTS recommended)
- **Python** 3.9 or newer

### Eleventy site

From the project root:

```bash
npm install
npm run start
```

This will build Tailwind CSS, watch for changes, and start the Eleventy dev server.

To build the static site for production:

```bash
npm run build
```

### Rewild Journal CLI

To run the CLI directly from the repo:

```bash
python rewild.py
# or
python rewild.py --output-dir ./journals
```

To install it as a local command (optional):

```bash
pip install .
rewild-journal --output-dir ./journals
```

### Tests

Python tests are written with `pytest`.

```bash
pip install pytest
pytest
```

The CI workflow in `.github/workflows/ci.yml` will run `npm run build` and `pytest` on each push and pull request.

## Style and guidelines

- **Content**
  - Use clear, invitational language.
  - Include access notes and alternatives where relevant.
  - Cite sources briefly when drawing on environmental humanities, Indigenous, queer, or disability studies.
- **Markdown and templates**
  - Prefer semantic headings and lists.
  - Keep front matter consistent with existing pages (e.g., `title`, `tags`, `duration`, `intensity`).
- **Python**
  - Target Python 3.9+.
  - Keep functions small and testable where possible.

## Submitting changes

1. Open an issue describing the change you have in mind (optional but helpful).
2. Fork the repository and create a feature branch.
3. Make your changes and add tests where appropriate.
4. Run `npm run build` (for site changes) and `pytest` (for CLI changes).
5. Open a pull request and describe:
   - What you changed and why.
   - Any accessibility or pedagogy considerations.

By contributing, you agree that your contributions will be licensed under the projects MIT License (see `LICENSE`).
