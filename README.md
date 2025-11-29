## Daily_tools — GitHub Pages site

This repository contains multiple small tools (HTML pages) and is prepared to be published using GitHub Pages.

What I changed for GitHub Pages compatibility:

- Moved all site files into the `/docs` directory (GitHub Pages can serve from `main` branch -> `docs` folder).
- Converted `compress.php` into a static `docs/compress.html` (GitHub Pages does not run PHP).
- Added `docs/.nojekyll` to ensure static files are served without Jekyll processing.

How to enable GitHub Pages for this repo (quick steps):

1. Go to your repository on GitHub -> Settings -> Pages.
2. Under "Build and deployment", choose "Source" -> select "Deploy from a branch".
3. Select branch `main` and folder `/docs`.
4. Save. After a few minutes the site should be available at `https://<username>.github.io/<repo>`.

Notes & recommendations:

- GitHub Pages does not execute server-side languages (PHP). Keep server-side logic off the site or host it elsewhere.
- If you want automatic builds or a different publish path (e.g., use `gh-pages` branch), I can add a GitHub Action workflow to push the site there.
- If you'd prefer your site to be at the repository root (no `/docs`), I can move files differently or set up a build/publish action.

If you want, I can also:
- Add a small site header/footer to every page so navigation is consistent across tools
- Configure a workflow for automatic publishing (example: build & deploy to `gh-pages` branch)
- Add a custom domain (`CNAME`) file if you have one

Tell me which option you'd like next and I will continue.
# Daily_tools
Make easy your task with online free tools
