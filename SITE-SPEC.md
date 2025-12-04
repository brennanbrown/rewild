# Rewild Creative Writing Site Spec (11ty)

## 1. Purpose and Goals

- **Purpose**
  - Provide a simple, accessible 11ty static site that performs the experience of a "rewilded" creative writing workshop.
  - Translate the essay’s framework into navigable pages and reusable practices.

- **Goals**
  - **Rewild the mind:** Center freewriting, experimentation, and process over polished product.
  - **Treat place as text:** Prompt visitors to attend to their immediate surroundings as primary texts.
  - **Foreground relationship:** Emphasize writing *with* environments and communities rather than writing *about* them as objects.
  - **Center Indigenous, queer, and disabled ecologies:** Keep these lenses structurally present rather than treating them as optional extras.
  - **Design for access:** Recognize all bodies as environmental, and support multiple modes of engagement (indoor, outdoor, stationary, mobile).
  - **Honor cycles:** Use seasonal and ecological cycles (succession, composting, watersheds, mycelial networks) as structural metaphors.

Audience: creative writing instructors, students, independent writers, and environmental humanities practitioners.

---

## 2. Experience Principles

- **Trailhead, not classroom**
  - The site is an invitation into practice, not a closed syllabus.
  - Every major page nudges users to look away from the screen and into their surroundings.

- **Gardens, not dashboards**
  - Soft structure with multiple paths and cross-links rather than a single linear course.
  - Embrace meandering exploration and non-linear reading.

- **All bodies are environmental**
  - Each practice includes concrete access notes and alternatives for different bodies and contexts.

- **Relationship over extraction**
  - Resources frame writing as relational, accountable, and situated.

---

## 3. Information Architecture

### Top-level navigation

- **Home**
  - Short manifesto; introduce "composting the workshop" and rewilding creative writing.
  - Offer a simple entry practice inviting users to attend to their immediate environment.

- **Framework**
  - Overview of the pedagogical framework distilled from the essay.
  - Five sub-sections:
    - Ecology of Mind
    - Nature-as-Text
    - Indigenous and Queer Lenses
    - Access in Wilderness / Disabled Ecologies
    - Wild Minds Workshop Model

- **Practices**
  - Library of exercises and prompts (freewriting, succession writing, watershed writing, mycelial mapping, composting, seasonal cycles, field journals, etc.).

- **Wild Minds Workshop**
  - A suggested multi-week or modular workshop path using the above practices.

- **Access and Ecologies**
  - Articulate disabled ecologies as both a design principle and a teaching stance.

- **Resources**
  - Works cited, recommended readings, and optional downloadable materials.

Optional future entry point: **Seasons / Cycles** (Spring, Summer, Autumn, Winter) as a thematic filter into practices.

---

## 4. Content Model and Page Types

### 4.1 Home Page

**Intent:** explain the project in plain language and invite immediate, embodied practice.

- **Sections**
  - Short statement of the problem with conventional workshops and the rewilding response.
  - One "begin here" practice suited to most contexts (including indoors).
  - Three quick pathways:
    - "I am a teacher" → Framework + Wild Minds Workshop.
    - "I am a writer" → Practices.
    - "I am curious about the theory" → Framework + Resources.


### 4.2 Framework Pages

Map to the essay’s five major sections.

- **Framework overview page**
  - Briefly introduce rewilding creative writing as ecological pedagogy.

- **Five subpages**
  - Ecology of Mind
  - Nature-as-Text
  - Indigenous and Queer Lenses
  - Access in Wilderness / Disabled Ecologies
  - Wild Minds Workshop Model

Each subpage contains:

- Concept summary (1–3 paragraphs).
- One anchor quote from the essay.
- 2–4 "gateway" practices linked from the Practices collection.
- A short "for instructors" section.
- A short "for solo writers" section.


### 4.3 Practice Pages

The Practices collection is the core of the site.

**Examples of practices drawn from the essay:**

- Freewriting as rewilding
- Succession writing
- Watershed writing
- Mycelial networks and rhizomatic mapping
- Composting and revision
- Seasonal cycles writing
- Field journaling and nature-as-text
- Indigenous-informed listening practices (carefully framed and cited)
- Queer ecology genre-crossing exercises
- Crip ecological sensory mapping and micro-environment attention

**Front matter / metadata for each practice:**

- `title`
- `tags` (for filtering), examples:
  - `practice`, `ecology-of-mind`, `nature-as-text`
  - `lens:indigenous`, `lens:queer`, `lens:crip`
  - `season:spring` etc.
  - `context:solo`, `context:classroom`, `context:online`, `context:outside`, `context:inside`
  - `access:seated`, `access:low-vision-friendly`, etc.
- `duration` (approximate time or short/medium/long)
- `intensity` (gentle / moderate / deep)

**Body structure:**

- Opening invitation: a brief, non-prescriptive setup.
- Access notes: clear adaptations and alternatives.
- Step-by-step guidance.
- Reflection prompts (3–5 questions).
- Optional craft notes: how the practice can feed revision or structure.
- Theory root system: very short note with one or more citations from the Resources.


### 4.4 Wild Minds Workshop Path

Provide a scaffold for instructors and independent learners.

- **Overview page**
  - Explain the rotating-location model, environmental attunement, portfolio thinking, and ecological feedback.
  - Offer a suggested multi-week arc (for example, 6–10 sessions), each with:
    - Theme
    - Place options and access notes
    - Recommended practices from the library
    - Suggested reflection and portfolio elements

- **Optional per-session pages**
  - Theme
  - Location ideas and contingencies
  - Attunement practice
  - Linked practices
  - Discussion prompts
  - Assessment / portfolio suggestions


### 4.5 Access and Ecologies Page

State how disabled ecologies shape both the pedagogy and the site itself.

- Summarize key ideas:
  - All bodies are environmental.
  - Outdoor movement is not the only or primary path to ecological relation.
  - Disabled perspectives transform environmental thinking and practice.

- Explain design commitments:
  - Built-in adaptations for practices.
  - Attention to classroom and interior ecologies.
  - Technical web accessibility practices (semantic HTML, good contrast, keyboard navigation, minimal required motion).


### 4.6 Resources / Works Cited

- Works cited adapted from the essay, with basic web formatting.
- Recommended readings with short annotations.
- Optional downloadables:
  - Field journal template.
  - Session planner.
  - Short syllabus capsule describing the Wild Minds workshop.

---

## 5. Visual and Interaction Design

### Visual language

- Metaphors: wild gardens, mycelial networks, maps, compost layers, seasonal cycles.
- Aesthetic: calm, readable typography with gentle color accents; no cluttered widgets.
- Possible seasonal flavoring via accent colors or small indicators (optional, not required for first version).


### Interaction (progressive enhancement)

The first version of the site should work fully without JavaScript. Enhancements can be added later.

- Attunement timer (optional enhancement)
  - Simple, unobtrusive timer on practice pages for 5–15 minute observation periods.

- Random practice chooser (optional enhancement)
  - A button that picks a practice at random, optionally constrained by context or access tags.


---

## 6. Eleventy Implementation Plan

### 6.1 Directory structure

- Project root
  - `SITE-SPEC.md`
  - `TODO.md`
  - `CHANGELOG.md`
  - `package.json`
  - `.eleventy.js`
  - `src/`
    - `_data/`
      - `site.json`
    - `_includes/`
      - `layouts/`
        - `base.njk`
    - `styles.css`
    - `index.md` (Home)
    - `framework/`
      - `index.md` (overview; later individual pages per section)
    - `practices/`
      - `index.md` (listing; later individual practice pages)
    - `workshop/`
      - `index.md` (overview; later optional session pages)
    - `access.md`
    - `resources.md`


### 6.2 Eleventy configuration

- Use `src` as the input directory and `_site` as the output directory.
- Use Eleventy’s default `_data` and `_includes` locations inside `src/`.
- Keep the first implementation minimal: a single `base.njk` layout, simple header navigation, and unstyled semantic HTML.

Example configuration intent:

- `input`: `src`
- `output`: `_site`
- Use Markdown for content pages with Nunjucks layouts.


### 6.3 Collections (future)

These can be added as the project grows:

- `practices`: markdown files in `src/practices/`.
- `framework`: markdown files in `src/framework/`.
- `workshop`: markdown files in `src/workshop/`.

Each collection can later be used to automatically build listing and detail pages.

---

## 7. Roadmap (short)

1. Initialize Eleventy project and basic layout.
2. Implement Home, Framework overview, Practices index, Workshop overview, Access page, and Resources page as simple Markdown pages.
3. Begin adding individual Practice pages, each with access notes and reflection prompts.
4. Flesh out Framework subpages and Wild Minds session scaffolding.
5. Iterate on visual design and add progressive enhancements (timers, random practice chooser) as needed.
