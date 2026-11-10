# Website validation

Audit: 2026-11-10.

- Full arXiv v3 paper, Appendix A, PMLR record/PDF, pinned research code, evaluation notebook cells/outputs and original figures inspected. Claims and discrepancies recorded in SOURCE_MAP.md. No benchmark rerun claimed.
- Supplied graphical abstract matches the arXiv source PDF byte-for-byte. All plotted axes, legends and units retained. Figure captions checked visually against the actual panels.
- Static validator passes: local HTML/CSS dependencies, anchors, 51 asset checksums, exact Table 1 transcription, visible/downloadable citation consistency, scholarly author order, SVG integrity, basic accessibility structure.
- Chrome desktop and 390×844 and 320×740 mobile viewports checked. No document-level horizontal overflow. Large figures/equations/tables scroll within their containers on narrow screens.
- All 10 images load after scrolling/opening the expandable results. KaTeX renders 17 mathematical expressions with zero error elements. Browser warning/error log is empty.
- Citation copying succeeds; keyboard Tab reaches the download link with a visible focus outline. Native expandable results open correctly. Static figures have original PDF/vector links and descriptive alternatives.
- Reduced-motion CSS and dark-mode styles reviewed in source; no synthetic scientific animation is included. Dark-mode rendering was not separately emulated.
- Main paper, arXiv, code, pinned notebooks and author profiles return HTTP 200. Three JHU institutional homepages return HTTP 403 to automated fetches; retained as official canonical institutional links rather than reported as broken. Detailed responses are in link-checks.json.
- GitHub Pages workflow [42739180653](https://github.com/SOLARIS-JHU/FE-DPC-website/actions/runs/42739180653) completed successfully (build and deploy) for commit af0c6be81b77e0b484d35c18d0568a351b13c4a9.
- Published URL https://solaris-jhu.github.io/FE-DPC-website/ opened in Chrome and verified at desktop and mobile sizes. All 10 images loaded; 17 math expressions rendered with no error elements or browser warnings/errors. Citation copying and expandable results work on the live page.
- All 56 deployed page/asset files returned HTTP 200 and matched local bytes exactly; see live-checks.json.
- Screenshots: published-desktop.jpg and published-mobile.jpg. No deployment blocker remains.
