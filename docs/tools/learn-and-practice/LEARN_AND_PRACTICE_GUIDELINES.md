# Learn & Practice Tool Guidelines

This folder contains interactive learning tools such as quizzes, reasoning tests, typing practice, and mathematics playgrounds.

## Source Of Truth

The Learn & Practice dashboard is:

```text
docs/tools/learn-and-practice/index.html
```

It reads learning tools from:

```text
docs/tools-data.js
```

The generated database is built from the `toolsData` array in `docs/index.html`.

## Add A New Tool

### 1. Create The File

Place the new page in this folder and use a lowercase kebab-case filename:

```text
docs/tools/learn-and-practice/my-new-quiz.html
```

Avoid spaces, uppercase letters, underscores, and special characters in filenames.

### 2. Use The Shared Page Shell

Every tool should include:

- Responsive viewport metadata
- A descriptive `<title>` and meta description
- `../../assets/img/favicon.svg`
- Tailwind CSS and Font Awesome when needed
- A consistent GenTools navbar linking to `../../index.html`
- A semantic `<main>` element
- A footer linking to the main tools page and legal pages
- Responsive behavior for mobile and desktop

Recommended shell:

```html
<body class="bg-slate-50 text-slate-800 flex flex-col min-h-screen">
    <nav class="sticky top-0 z-50 w-full shrink-0">
        <!-- GenTools navigation -->
    </nav>

    <main class="flex-grow w-full max-w-6xl mx-auto px-4 py-8 sm:px-6">
        <!-- Tool interface -->
    </main>

    <footer class="w-full shrink-0">
        <!-- Shared footer -->
    </footer>
</body>
```

For full-screen tools, keep the page in a vertical flow. Do not use `flex items-center justify-center` on `<body>` when the page also contains a navbar and footer.

### 3. Register The Tool

Add one object to the `toolsData` array in `docs/index.html`:

```javascript
{
    cat: 'Learn',
    url: 'tools/learn-and-practice/my-new-quiz.html',
    icon: 'fa-solid fa-puzzle-piece',
    color: 'indigo',
    title: 'My New Quiz',
    desc: 'Practice a specific skill with timed questions and instant feedback.'
}
```

Use `cat: 'Learn'`. The dashboard automatically displays every registry item in this category.

Supported card colors include `blue`, `indigo`, `purple`, `rose`, `emerald`, and `amber`.

### 4. Rebuild Generated Data

From the repository root, run:

```bash
node build-tools-data.js
```

Do not edit `docs/tools-data.js` manually. It is generated from `docs/index.html`.

### 5. Update The Sitemap

Add the public URL to `docs/sitemap.xml`:

```xml
<url>
  <loc>https://www.gentools.in/tools/learn-and-practice/my-new-quiz.html</loc>
  <lastmod>YYYY-MM-DD</lastmod>
</url>
```

The dashboard URL should remain listed as:

```text
https://www.gentools.in/tools/learn-and-practice/
```

### 6. Apply Shared Layout

If the page was created without the standard navbar/footer, run the layout automation from the repository root:

```bash
python3 organize_layout.py
```

The script calculates relative asset paths for pages in this folder.

## UI And UX Standards

### Learning Experience

- Show the subject and goal immediately.
- Keep one clear primary action per screen.
- Provide visible progress, score, timer, or completion state where relevant.
- Explain answers after quiz questions when explanations improve learning.
- Make restart and return-to-dashboard actions easy to find.
- Preserve user progress only when it is useful and privacy-safe.

### Responsive Layout

- Test narrow mobile widths and desktop layouts.
- Prevent horizontal overflow from long questions, formulas, tables, or buttons.
- Use flexible grids such as `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`.
- Keep touch targets at least 44px where practical.
- Do not hide essential controls behind hover-only interactions.

### Visual Language

- Match the GenTools visual language: clean surfaces, slate text, indigo accents, restrained shadows, and purposeful motion.
- Use cards only for genuinely framed tools or repeated items.
- Keep headings compact inside tool interfaces.
- Use familiar icons with accessible labels or tooltips.
- Avoid decorative clutter that competes with the question, graph, or practice area.

## Accessibility

- Use semantic headings in order.
- Give every form control a visible or programmatic label.
- Use `button type="button"` for non-submit actions.
- Make keyboard navigation possible for quizzes, controls, and canvas alternatives.
- Provide visible focus states.
- Use `aria-live` for timer, score, and result updates when appropriate.
- Do not rely on color alone to communicate correct, incorrect, selected, or disabled states.

## Performance And Privacy

- Keep processing client-side; do not upload learner data or files.
- Use `async` operations for expensive work and keep the UI responsive.
- Use `requestAnimationFrame` for canvas animation.
- Revoke temporary object URLs with `URL.revokeObjectURL()`.
- Clear timers and animation frames when restarting or leaving a tool.
- Avoid unnecessary external libraries. CDN dependencies must be HTTPS and documented in the page.
- Never place API keys, personal data, or secrets in client-side code.

## Validation Checklist

Before considering a new tool complete:

- [ ] Filename uses lowercase kebab-case.
- [ ] Tool is placed in `docs/tools/learn-and-practice/`.
- [ ] Navbar and footer align vertically with the page content.
- [ ] Tool is registered with `cat: 'Learn'` in `docs/index.html`.
- [ ] `node build-tools-data.js` completes successfully.
- [ ] Sitemap contains the public tool URL.
- [ ] Search finds the tool on the main landing page.
- [ ] Dashboard displays the tool card and opens the correct URL.
- [ ] Mobile and desktop layouts do not overflow.
- [ ] Keyboard and focus behavior works.
- [ ] Timers, listeners, animation frames, and object URLs are cleaned up.
- [ ] No console errors appear during normal use.
- [ ] JavaScript and HTML errors are checked in VS Code.

## Quick Verification

Run these commands from the repository root:

```bash
node build-tools-data.js
node --check build-tools-data.js
node --check docs/tools-data.js
xmllint --noout docs/sitemap.xml
```

Then open:

```text
docs/tools/learn-and-practice/index.html
```

Confirm that the new card appears, search works, and the card opens the new tool page.
