# Fistron

Fistron is the end-to-end autonomous Assurance as a Platform (AaaP). It works on top of the tools a team already has and proves quality and compliance with evidence. The name comes from the Czech *fištrón*: wit, knowing how to do it. Motto: **Assured, not assumed.** Principle: **Deterministic where it counts. AI where it helps.**

This repository is the single source of the Fistron brand: logo, wordmark, colours, type, the mascot Fištrónek (with Flaky) and the status icons used in the product GUI, on fistron.io and in the docs. Colour tokens match `src/styles/tokens.css` of the fistron.io repository.

## Voice

- English first. Short, concrete sentences. Say what Fistron does and what evidence backs it.
- Serious where it matters: the hero, claims, pricing, compliance. Never a joke in a headline.
- Humour lives in the details: the mascot, 404 pages, empty states, easter eggs, QE self-irony (flaky tests, "green" pipelines).
- Don't name a founder's employer or its products as examples or customers. Use Uyuni or generic examples.
- Not yet built? Say "In development", don't hide it.

Do: "2 checks failed. Fištrónek found the commit that broke them." Don't: "Oops! Something went wrong 😬".

## Colour

Indigo carries the brand, leaf is the one accent and always means "checked / OK". Use the role tokens (`surface-page`, `surface-card`, `heading`, `ink`, `muted`, `btn-*`), not raw hexes; they flip for the dark theme.

- Text: `ink` on `surface-page` and `paper` (16:1); `muted` for captions (6.7:1); `leaf-text`, never `leaf`, for green text (5.3:1).
- `leaf` is a fill: the checkbox, passed status, success. White on leaf is 3.05:1, so it is for the tick and large glyphs only, never body text.
- `pending` is for icons and borders (3.2:1), not text.
- `night` bands use `on-dark` / `on-dark-muted` text and the on-dark logo.
- Status colours (`status-*`) appear only inside status icons, always with their shape (tick, X, stripes, dash, "!"), so they read without colour.

## Type

IBM Plex Sans (400, 500, 600) and IBM Plex Mono (400). The website self-hosts them via `@fontsource/ibm-plex-sans` and `@fontsource/ibm-plex-mono`; anything else can load them from Google Fonts. Headings 600 with negative tracking (`h1`, `h2`), body 400 at 17px / 1.6, test ids and commands in mono (`code`). The wordmark is the only place weight 500 is used.

## Logo

The mark is **Fištrónek's head in one colour holding the green checkbox**. Print uses two colours at most: indigo and leaf. The eye and the gap around the checkbox are holes, not white ink, so the mark sits on any ground.

| Asset | Use |
| --- | --- |
| `logo/fistron-mark.svg` | Favicon, app icon, avatar, merch. Indigo head, leaf checkbox. |
| `logo/fistron-mark-on-dark.svg` | On `night` or photos: white head, leaf checkbox. |
| `logo/fistron-mark-one-colour.svg` | One-colour print: stamp, engraving, embroidery. The tick is cut out. |
| `logo/fistron-wordmark.svg` / `-on-dark.svg` | "Fistron" with the checkbox above the s. |
| `logo/fistron-lockup.svg` / `-on-dark.svg` | Mark + wordmark, both with their checkbox. Header, slides, documents. |

Rules:
- Clear space: the height of the checkbox on every side. Minimum size: mark 16px, wordmark 64px wide, lockup 120px wide.
- Don't recolour the head (indigo, white or one ink only), don't outline it, don't add the eyebrow or other pose details to the mark, don't put the checkbox anywhere else.
- No effects: no shadow, gradient, rotation or stretching.

## Wordmark

"Fistron" set in IBM Plex Sans 500, tracking -0.01em, with the brand checkbox **above the s**: the checkbox is 0.32em square and its bottom edge is level with the bottom edge of the dot on the i, so the two sit on one line and the box rises above the F. Use the SVG asset; when it must be live text (the website header at 26px), wrap the s in a relatively positioned span and place the checkbox with `position: absolute; left: 50%; top: 0.105em; width: 0.32em; height: 0.32em; transform: translateX(-50%)` (the span's content area starts 1.0385em above the baseline in IBM Plex Sans, and the dot's bottom edge is 0.613em above it: 1.0385 - 0.613 - 0.32 = 0.105em). The old placement where the ® would sit is retired.

## The checkbox

One shape is the brand: a rounded square, corner `radius-checkbox` (22.5% of the side), leaf fill, white tick with round caps and joins. The same box, in other colours and with other glyphs, is every status icon. Don't draw ticks without the box, and don't use the leaf box for anything but "checked / passed / OK".

## Fištrónek, the mascot

A crow in the "C" style: flat fills in two indigo shades (`crow-body`, `crow-wing`), beak `crow-beak`, a 3px `crow-outline` around every shape (light outline on dark pages, so no glow or rim effect is needed). He is built from eight parts (body, head, tuft, beak, eye with brow, wing, tail, legs) on one skeleton, so a new pose reuses them.

Eleven poses, each with one moving part. `mascot/fistronek-<pose>.svg` are animated and follow the page theme through `--crow-outline`, `--crow-leg` and `--color-indigo` when inlined; `mascot/static/` holds still versions for light grounds and `-on-dark` versions for dark grounds:

| Pose | Moves | Use |
| --- | --- | --- |
| main | blinks, checkbox pops | default, all good |
| investigating | wing with the magnifier | RCA, analysis running |
| skeptical | Flaky hops | review, doubtful result |
| chase | wing flaps, Flaky runs | flaky tests, quarantine |
| telescope | wing with telescope | predictive quality, roadmap |
| broom | sweeps | Suite Health, removing tests |
| stamp | stamp presses, checkbox pops | approvals, certification |
| conductor | baton, notes float | orchestration |
| chef | stirs, steam | setup wizard, "cooking" |
| desk | types, task gets ticked | local UI, reports |
| quarantine | Flaky shakes behind tape | quarantined tests |

Rules: only one part moves; loops are calm (0.35-3 s); everything stops under `prefers-reduced-motion`. He illustrates, he never replaces a status icon, and he never appears in a headline or next to pricing.

**Flaky** is the flaky-test gremlin: a round, spiky creature split down the middle, red (`status-failed`) left and leaf right. He appears only with the flaky state or in the mascot's scenes, never as a generic error.

## Status icons

Rounded squares on a 24 grid (20px box, `radius-checkbox`), in `status/status-<state>.svg`, animated by the classes in `status/status.css` when inlined; `status/animated/status-<state>.svg` carry their animation inside and move even as `<img>`. Shape tells the state; colour confirms it.

| State | Icon | Moves |
| --- | --- | --- |
| passed / met | leaf box, white tick | no |
| failed / not met | red box, white X | no |
| flaky | Flaky, half red / half green | wobbles, halves swap |
| quarantined | yellow box, ink hazard stripes | stripes drift slowly |
| running | pending outline, indigo arc | spins |
| pending / not run | pending outline, three dots | dots pulse |
| skipped | `control` box, dash | no |
| manual / not observed | dashed pending outline, dot | no |
| warning / needs input | amber box, ink "!" | no |

Rule: **only states that can still change on their own move**; final states are still. Sizes 16, 20 and 24px in tables and chips, 32px in legends. In big summaries, empty states and notifications use the head mark: holding the leaf checkbox when everything passed, frowning with a red X box when something failed. The head never goes into table rows.

## Repository layout

| Path | What |
| --- | --- |
| `tokens/tokens.json` | The tokens (source). Colours with light and dark values, type scale, spacing, radii. |
| `tokens/tokens.css` | Generated CSS custom properties. Names follow the fistron.io stylesheet: colours get a `color-` prefix (`--color-indigo`), except `surface-*`, `btn-*`, `status-*` and `crow-*`. Dark values under `[data-theme="dark"]` and `prefers-color-scheme: dark`. |
| `logo/` | Marks, wordmark, lockup, `favicon.svg` (follows the system theme), `favicon-32.png`, `app-icon.svg`, `apple-touch-icon.png`, `app-icon-512.png`. |
| `mascot/` | Eleven animated poses, `fistronek.css` (their animation), `static/` still versions. |
| `status/` | Nine status icons and `status.css` (their animation) for inlining in the GUI; `status/animated/` the same icons with the animation inside the file, for `<img>` (website, docs, README). |
| `scripts/` | The generators every file above comes from. |

## Using it

Copy the files you need into the consuming repository (website `public/`, GUI assets) and keep their names, so a later update is a plain copy. Inline SVG when it must animate or follow the theme; `<img>` shows the still default. Public URLs for quick use: `https://raw.githubusercontent.com/fistron-io/brand/main/<path>`.

## Building

```sh
npm install
pip install -r scripts/requirements.txt
python3 scripts/build.py
```

Change the sources (`tokens/tokens.json`, `scripts/*.py`), never the generated files. The wordmark is outlined from IBM Plex Sans 500 (`@fontsource/ibm-plex-sans`); PNG icons need `rsvg-convert` (librsvg). A new pose reuses the skeleton in `scripts/skeleton.py` and goes into `scripts/poses.py` with exactly one moving part.

## Licence

The Fistron name, logo, wordmark and mascot are not licensed for reuse; see `LICENSE.md`.
