<!-- Copilot instructions for the TournamentSchedule static site -->
# Quick Guide for AI Coding Agents

This repository is a small static single-page site. The goal of this file is to give an AI coding agent immediate, actionable knowledge to be productive without guesswork.

- **Project type**: Static HTML/CSS/JS single-page calendar at `index.html` (no build system, no package.json).
- **How to run**: Open `index.html` in a browser (or use a simple local server, e.g. `python -m http.server`). Use browser devtools to test mobile layout (toggle device toolbar).

**Big picture / architecture**
- Single view: `index.html` contains layout, styling and all logic. There are no other source files.
- The page builds a calendar grid dynamically from JS using:
  - `year`, `month` constants (month index 0–11; current file sets `month = 11`).
  - `firstDayOfMonth`, `startIndex`, `daysInMonth`, `totalCells` to compute cell positions.
- Events are injected at render time via the `events` array and helpers `insertEvents` / `addEvent`.

**Key data patterns and examples**
- Event item (single-day): `{ day: 7, name: "Mahado Nexus", type: "nexus", stream: false }` — matches a specific day number.
- Weekly/multi-week event: `{ weekly: true, weekday: 2, weeks: [1,3,4,5], name: "TNT OCG", type: "ocg", stream: true }` — `weekday` uses `Date.getDay()` (0=Sun..6=Sat); `weeks` is week-of-month (calculated with `startIndex`).
- When adding events, follow existing fields: `day` OR `weekly`, `weekday`, `weeks`, `name`, `type`, `stream`.

**CSS / classes to be aware of**
- Day container: `.day`; other-month days get `.other`.
- Visual state classes: `.past`, `.today`, `.hof` (animated), notes `.note`.
- Event types map to CSS classes and styles: `.ocg`, `.ae`, `.tnt`, `.genesys`, `.nexus`, `.edison`, `.tour`, `.hof` — use these names for new events.
- Stream indicator: `.has-stream` on a `.note` adds a TV icon via `::before`.

**Behavioral conventions (important)**
- Mobile breakpoint: `window.innerWidth <= 768` is used in JS to change rendering and to hide empty `.day` elements.
- The filtering UI (`.filter` checkboxes) toggles visibility by setting `style.display` on `.note.<type>` elements; on mobile the code additionally hides `.day` elements that have no visible notes.
- Popups are rendered into `#popup-area` via `showPopup(ev)` and removed by `closePopup()`.

**Debugging and quick edits**
- To debug date calculations: modify `month` and `year` at top of the script and reload.
- To see why a day is hidden on mobile: inspect the `.day` element and check if child `.note` elements have `style.display='none'`.
- To add a new event type, add a CSS block matching the class name (see existing examples) and add entries to the `events` array.

**Integration / external dependencies**
- Background image is loaded from an external URL in CSS (`background: url('https://i.postimg.cc/...')`). There are no other external scripts or packages.

**What NOT to change without confirming**
- Do not assume there is a build step — files are served directly.
- Avoid moving logic out of `index.html` unless you also provide updated run/debug instructions and a minimal local server workflow.

If anything here is unclear or you'd like me to include CI, test harnesses, or split code into modules, tell me which direction to take and I will update this file and the code accordingly.

Suggested commit message when updating behavior: "docs: add/refresh Copilot instructions for TournamentSchedule (index.html)"
