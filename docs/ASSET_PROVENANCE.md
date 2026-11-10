# Asset provenance and attribution

Retrieved/inspected 2026-11-09–10. SHA-256 values are in `assets/manifest.json`. Local assets avoid third-party requests at page load.

## Scientific figures

Primary archive: https://arxiv.org/src/2511.05757v3 . Original figure PDFs are retained without cropping or axis/legend changes. ArXiv records CC BY 4.0; figures are attributed to Hassan Iqbal, Xingjian Li, Tyler Ingebrand, Adam Thorpe, Krishna Kumar, Ufuk Topcu, and Ján Drgoňa, *Zero-Shot Function Encoder-Based Differentiable Predictive Control* (2026). License: https://creativecommons.org/licenses/by/4.0/ .

| Local asset | Source | Transformation |
|---|---|---|
| `assets/figures/graphical-abstract.pdf` | User-supplied `FE-NODE_method2.pdf`, identical to arXiv source `Figures/method/FE-NODE_method2.pdf` / Fig. 1 | Original bytes retained; SHA-256 `3186cd746e81fb27909163a0bab896207ade97e674a5aa95eaae7820b755c8a0` |
| `graphical-abstract.svg` | Above PDF | Inkscape PDF import with Poppler, plain SVG, text converted to paths; no semantic redesign |
| `graphical-abstract.png`, `graphical-abstract.webp` | Above PDF | pypdfium2 rendering at 2600 px width; PNG for the social-card script, WebP fallback asset |
| `van-der-pol.pdf`, `.webp` | Paper Fig. 3: `Figures/VDP/vpd_cl_trajectory_flatten.pdf` | Original PDF plus 2400 px target-width WebP |
| `two-tank.pdf`, `.webp` | Paper Fig. 4: `Figures/TT/cl_trajectory_plot_states_only.pdf` | Original PDF plus 2200 px target-width WebP |
| `glycolytic-model.pdf`, `.webp` | Paper Fig. 5: `Figures/GO/go_plot_coefficient_switching_2.pdf` | Original PDF plus 2200 px target-width WebP |
| `glycolytic-control.pdf`, `.webp` | Paper Fig. 6: `Figures/GO/go_state_error_only.pdf` | Original PDF plus 2200 px target-width WebP |
| `quadrotor.pdf`, `.webp` | Paper Fig. 7: `Figures/Quad/closed_loop_trajectories_2.pdf` | Original PDF plus 2400 px target-width WebP |
| `assets/social-preview.png` | Original graphical abstract plus paper title | 1200×630 card made by `scripts/make_social_preview.py`; no fabricated data |

`scripts/render_figures.py` reproduces conversions. The source PDFs provide exact vector fallbacks; conversion-library versions may change raster antialiasing. Figures are intentionally static to preserve the supplied graphical abstract and reported measurements. No stock or generated scientific imagery is used.

## Visual foundation and marks

- `template.css`: copied from https://solaris-jhu.github.io/TQPNet/static/css/style.css ; source project https://github.com/SOLARIS-JHU/TQPNet ; Apache-2.0, original `LICENSE` retained. `style.css` contains this page's adaptations. See `NOTICE`.
- `assets/logos/jhu-whiting.svg`, `solaris.png`, `rosei.png`: existing SOLARIS TQPNet assets at `https://solaris-jhu.github.io/TQPNet/static/logos/` with the same filenames. These are institutional/group marks, not newly designed artwork. Rights remain with their owners.
- `assets/logos/ut-austin.svg`: official university homepage logo, https://www.utexas.edu/themes/coresite/coretheme/images/logo.svg . Rights remain with The University of Texas at Austin.
- The marks identify affiliations/group context; no extra author affiliation is inferred from the logos.

The other supplied pages were inspected for presentation patterns: MI-DPC-UPHES, SD-DPC, Mixed-Integer DPC, PDE Control with DPC, CINOC, SCORE, Chiller Plant MI-DPC, and NeuralDAEs. No competing template or unverified experimental asset was mixed into the site.

## Fonts and mathematics

- `assets/fonts/font-0.ttf`, `font-1.ttf`: Fraunces, weights 500 and 600.
- `assets/fonts/font-2.ttf`, `font-3.ttf`, `font-4.ttf`: Inter, weights 400, 500, and 600.
- Font files obtained from Google's official Fonts CSS response for `Fraunces:opsz,wght@9..144,500;9..144,600` and `Inter:wght@400;500;600`, then hosted locally. Format is TrueType; filenames and `fonts.css` reflect the actual format.
- Licenses: `assets/fonts/Fraunces-OFL.txt` and `Inter-OFL.txt`, from https://github.com/google/fonts/tree/main/ofl/fraunces and https://github.com/google/fonts/tree/main/ofl/inter . SIL Open Font License 1.1.
- `assets/vendor/katex/`: KaTeX **0.16.22**, from the official npm distribution via https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/ . Includes `katex.min.js`, `contrib/auto-render.min.js` (stored as `auto-render.min.js`), stylesheet and WOFF2 fonts. The stylesheet's unused WOFF/TTF fallback URLs were removed; WOFF2 files are local. MIT license retained in `assets/vendor/katex/LICENSE`.

The Apache license for site code does not replace these third-party licenses or trademark rights.
