# FE-DPC research website

Project page for **Zero-Shot Function Encoder-Based Differentiable Predictive Control**, by Hassan Iqbal, Xingjian Li, Tyler Ingebrand, Adam Thorpe, Krishna Kumar, Ufuk Topcu, and Ján Drgoňa. Published at L4DC 2026, PMLR 331:299–315 (oral presentation).

- Website: https://solaris-jhu.github.io/FE-DPC-website/
- Published paper: https://proceedings.mlr.press/v331/iqbal26a.html
- Primary scientific version used here: https://arxiv.org/abs/2511.05757v3
- Research code, maintained separately: https://github.com/hassaniqbal209/DPCFunctionEncoder

This is a lightweight static site: HTML, CSS, a small JavaScript file, and local assets. The design adapts [TQPNet](https://solaris-jhu.github.io/TQPNet/): Fraunces headings, Inter body text, heritage blue, rounded resource buttons, restrained cards, and responsive layouts. The supplied graphical-abstract PDF is reproduced faithfully as vector SVG. Experimental plots are original author figures, not regenerated benchmark data.

## Preview and validation

No application build or package installation is required. From the parent directory, run `python -m http.server 8000`, then open `http://localhost:8000/FE-DPC-website/`. Serving the repository under its name also tests GitHub Pages subdirectory paths.

Run `python scripts/validate_site.py` from this repository before committing. It checks local HTML/CSS dependencies, anchors, citation metadata, table transcription, source-asset checksums, SVG safety, and basic accessibility structure. It is a static validator, not a substitute for browser review. `python scripts/stage_site.py` creates the deployment directory `_site/` from an explicit allowlist.

## Maintenance

- Edit scientific text in `index.html`. Keep the author order and full paper title intact.
- Before changing a substantive claim, update [docs/SOURCE_MAP.md](docs/SOURCE_MAP.md) with the supporting paper section, equation, figure, table, or pinned code path.
- Numerical measurements are transcribed in `data/table1.json` and displayed in the HTML table. The validator requires them to agree. Preserve the benchmark, baseline, units, and timing qualifications.
- Keep the distinctions between offline basis learning, offline policy learning, and online coefficient inference. Online inference still requires observations and a least-squares solve.
- Do not silently resolve the documented discrepancies in speedups, glycolytic parameter ranges, optimizer names, or code coverage. Verify a new source first.
- Keep citation metadata, JSON-LD, `citation.bib`, `CITATION.cff`, and visible publication information consistent.
- Notebook links intentionally pin research-code commit `001572e38136f70aed6ace621bc07f67335ef14f`. The main Code button follows the current repository.
- Check desktop and narrow mobile layouts, math, image scrolling, keyboard focus, copy/download citation, dark mode, browser logs, and the actual published URL after changes.

All fonts, math-rendering files, logos, and figures are served locally. No analytics, external font service, or framework is needed at runtime. Original figures remain static; there is no illustrative animation presented as experimental evidence. Reduced-motion CSS disables transitions and smooth scrolling.

## Assets and regeneration

[docs/ASSET_PROVENANCE.md](docs/ASSET_PROVENANCE.md) records sources, transformations, and licenses. `assets/manifest.json` records SHA-256 digests of the checked-in assets.

Original author PDFs are in `assets/figures/`. Optional regeneration requires Pillow and pypdfium2: `python scripts/render_figures.py`. Add `--svg` with Inkscape installed to regenerate the graphical-abstract SVG. `python scripts/make_social_preview.py` rebuilds the social card using the original diagram and locally hosted fonts. These scripts render existing figures; they do not generate scientific curves or rerun experiments. If assets change intentionally, run `python scripts/update_asset_manifest.py`, then review the provenance and validate again.

## Deployment

GitHub Pages uses `.github/workflows/pages.yml`. Every push to `main` runs validation, stages the static files, uploads the Pages artifact, and deploys it. Pull requests validate and build but do not deploy. Repository Settings → Pages → Source must be **GitHub Actions**. The deploy job has only the Pages and OIDC permissions required for deployment.

Check both the successful workflow and the live website. A source commit alone does not establish that publication succeeded. The maintenance documents stay in the repository; the public site contains research content and resource links.

## Attribution

The site code and adapted TQPNet styling are under Apache-2.0; see [LICENSE](LICENSE) and [NOTICE](NOTICE). Paper figures are credited to Iqbal et al. and retain their CC BY 4.0 provenance. Fonts and KaTeX retain their own included licenses. Institutional marks identify the authors' affiliations and research group; they are not relicensed as site code.
