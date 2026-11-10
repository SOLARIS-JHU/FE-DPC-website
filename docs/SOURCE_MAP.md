# Scientific source map

Audit date: 2026-11-10. This maintenance record is not part of the deployed page.

## Source priority and versions

1. **Primary scientific source:** [arXiv:2511.05757v3](https://arxiv.org/abs/2511.05757v3), revised 15 April 2026. The user supplied the unversioned URL, which resolved to v3 at inspection. The complete PDF, HTML, source TeX, figures, and Appendix A were read. The page summarizes this version; it does not silently combine older versions.
2. **Publication authority:** [PMLR paper record](https://proceedings.mlr.press/v331/iqbal26a.html), [published PDF](https://raw.githubusercontent.com/mlresearch/v331/main/assets/iqbal26a/iqbal26a.pdf), and [volume 331](https://proceedings.mlr.press/v331/). L4DC 2026; Proceedings of The 8th Annual Learning for Dynamics and Control Conference; pages 299–315. Oral presentation is identified by the official volume/program. The published numerical table was checked against arXiv v3; the values agree. Bibliography follows the publisher.
3. **Implementation:** [DPCFunctionEncoder at 001572e38136f70aed6ace621bc07f67335ef14f](https://github.com/hassaniqbal209/DPCFunctionEncoder/tree/001572e38136f70aed6ace621bc07f67335ef14f). This was the inspected repository HEAD, not a verified paper-specific tag. No claim of bitwise reproduction or of a full experiment rerun is made.
4. **Graphical abstract:** author-supplied `FE-NODE_method2.pdf`, identical by SHA-256 to `Figures/method/FE-NODE_method2.pdf` in the arXiv v3 source archive. Digest: `3186cd746e81fb27909163a0bab896207ade97e674a5aa95eaae7820b755c8a0`.
5. **Design only:** the nine reference sites supplied in the request. They provide no scientific evidence for this paper.

## Identity and bibliography

Exact title: **Zero-Shot Function Encoder-Based Differentiable Predictive Control**.

| Author order | Name on page | Affiliation in paper | Verified profile/resource |
|---|---|---|---|
| 1 | Hassan Iqbal | The University of Texas at Austin | https://oden.utexas.edu/people/directory/Hassan-Iqbal/ |
| 2 | Xingjian Li | The University of Texas at Austin | https://oden.utexas.edu/people/directory/Xingjian-Li/ |
| 3 | Tyler Ingebrand | The University of Texas at Austin | https://tyler-ingebrand.github.io/ |
| 4 | Adam Thorpe | The University of Texas at Austin | https://ajthor.github.io/ |
| 5 | Krishna Kumar | The University of Texas at Austin | https://www.geoelements.org/team/krishna-kumar |
| 6 | Ufuk Topcu | The University of Texas at Austin | https://ae.utexas.edu/person/ufuk-topcu/ |
| 7 | Ján Drgoňa | Johns Hopkins University | https://www.linkedin.com/in/drgona/ (linked by the existing SOLARIS project page) |

Affiliations reproduce the paper and are explicitly labeled as such. A current personal profile may show a later affiliation; do not overwrite historical paper affiliations with it. The publisher's BibTeX uses `Drgona, Jan`; the visible author list and scholarly metadata retain the accents. No DOI was invented.

## Claim-to-source map

| Public location / claim or equation | Primary evidence | Qualification / implementation cross-check |
|---|---|---|
| Opening: a dynamics representation and a coefficient-conditioned policy; no neural retraining at deployment | Abstract; §1; §3; Fig. 1; Algorithms 1–3 | Does not mean zero data or zero computation. Online coefficient solve remains. |
| Problem: unknown dynamics parameters ν, objective/constraint parameters ξ; xdot=f(x,u;ν) | §2, Eq. (1) | Full-state setting; not an output-feedback estimator. The page shows a condensed formulation rather than a verbatim abstract. |
| MPC online solve versus DPC offline policy training | §1–2 | Describes computational structure, not universal performance superiority. |
| FE-NODE representation fhat=sum c_j g_j and integrated state update | §3.1, Eq. (2); Appendix A.3, Algorithm 1 | RK4 in §4 and code `src/Integrator.py`; `src/getters.py` constructs bases. Shared basis parameters versus system-specific coefficients are retained. |
| Offline bases fit state-transition prediction error | §3.1; Algorithm 1 | `src/1.train_function_encoder.py`: `compute_coefficients`, prediction MSE, optimizer. |
| Offline policy pi_W(x;ξ,c); objective includes running cost, state/input penalties, terminal term | §3.2, Eq. (3); Algorithm 2 | `src/2.train_policy.py`: `System([policy, model_node])`, `PenaltyLoss`, policy optimizer. Condensed expectation is a website presentation of the sampled training objective. |
| Gradients through pretrained model to policy; no optimal-control supervision labels | §3.2; Fig. 1; Algorithm 2 | Pretrained FE model is used in the rollout. Optimizer parameters are policy parameters. |
| Online G,F and (G+λI)c=F; finite-difference derivative in F | §3.3; Algorithm 3 | Regularized empirical projection; not exact reconstruction of arbitrary unknown dynamics. The diagram keeps system observations, c, state/task input, policy output, and feedback connections. |
| Zero-shot means no neural-network retraining | Abstract; §3.3; Algorithms 1–3 | New observations and coefficient solve required. No claim that all online optimization is removed. |
| 100 coefficient samples in every benchmark | §4 introductory experimental setup | Not a timing batch size. |
| Basis counts 11 / 11 / 21 / 32 | §4 and Appendix A.2 | VDP / TT / GO / quadrotor respectively; not all use the same model size. |
| Van der Pol unknown μ and d∈{−1,1}; switch after 25 steps | §4, Van der Pol example; Fig. 3 | Numerical oscillator, not hardware. Figure includes uncontrolled and controlled cases. |
| Two-tank pump/valve, 700-step changing dynamics/reference rollout | §4, two-tank example; Fig. 4 | Upper panel is levels/reference; lower panel is pump/valve inputs and bounds, not error. |
| Glycolytic oscillator: stiff seven-state model, first state actuated/tracked | §4 glycolytic example; Appendix A.1 | Exact biochemical equations remain in paper; page does not claim biomedical/experimental validation. |
| GO horizon 50 for FE-DPC and WB-MPC; input saturation/reference offset | §4 glycolytic example; Fig. 6 | Original panels show x1 error and input. WB-MPC true dynamics baseline. |
| GO model comparison: changes every 500 steps; prediction reset every 50 | §4; Fig. 5 caption/text | This is not an uninterrupted 1500-step open-loop prediction. Reset qualification is retained in the expandable caption. |
| Quadrotor 12 states, 20 models, mass/inertia switches, 0.4 m reference | §4 quadrotor example; Fig. 7; Appendix A.1–A.2 | All simulation; stabilization reported within terminal-cost tolerance, not exact equilibrium/proof. |
| Quadrotor policy feeds inner feedback laws; yaw torque zero | Appendix A.1, quadrotor controls | α1,α2,α3 enter F=mg−10(h−α1)+3w, τφ=−(φ−α2)−p, τθ=−(θ−α3)−q; τψ=0. Do not describe policy as directly outputting physical thrust/torques. |
| Table values, fixed parameters, MSE to references, time in seconds | §4 quantitative comparison and Table 1 | Exact values in `data/table1.json`. Table is separate from switch demonstrations. Not per-step latency. |
| NVIDIA RTX 5090 | §4 introductory setup | CPU, timing batch, denominator/aggregation, repeat counts and uncertainty are not specified for Table 1. Do not infer them from notebook defaults. |
| Scope: full-state information and sufficiently representative historical trajectories | §2 assumptions; §3.1–3.3; §5 | Learned representation must be useful for encountered dynamics. No unconditional out-of-distribution guarantee. |
| Soft penalties do not certify feasibility | Eq. (3), §3.2 | Interpretation of stated training formulation. Bounded policy output in code is not a guarantee of state feasibility. |
| Representation results are prior work; no new universal control theorem | §3.1 citations/discussion; §5 | Distinguish representation approximation results from closed-loop stability/safety. |
| Code includes VDP, TT, GO notebooks and checkpoints, no quadrotor evaluation found | Inspected pinned repository tree; `src/evaluate_VDP.ipynb`, `src/evaluate_TT.ipynb`, `src/evaluate_GO.ipynb`, checkpoint directories | Statement is scoped to inspected release, not all authors' private/unpublished code. |

## Numerical transcription

| Table 1 row | FE-DPC MSE | WB-MPC MSE | FE-DPC time (s) | WB-MPC time (s) |
|---|---:|---:|---:|---:|
| Van der Pol | 0.002683 | 0.002653 | 0.53 | 1.21 |
| Two-tank | 0.008452 | 0.004164 | 1.13 | 6.75 |
| Glycolytic oscillator | 0.180299 | 0.032320 | 5.89 | 136.07 |
| Quadrotor | 0.022003 | 0.024208 | 1.93 | 155.85 |

MSE units are not independently assigned: the systems have different states/scalings. Compare methods within a benchmark. No error bars or statistical significance claims are added. The original paper does not supply enough timing context to support real-time or per-control-step latency claims.

## Discrepancies and limits of verification

1. **Speedup prose versus Table 1:** the paper gives 2.3–71.5×, but the quadrotor entries imply 155.85/1.93 ≈ 80.75×. The original table is preserved; the conflict is disclosed in the page's comparison notes. No speedup headline is used.
2. **MSE summary versus Table 1:** prose says MPC achieves the lowest tracking error across all examples; the quadrotor row has lower FE-DPC MSE. The table is retained and the exception described.
3. **Glycolytic parameter ranges:** main text uses k1∈{80,90,100}, K1∈{0.5,0.75}; Appendix A.2 gives k1∈[90,100], K1∈[0.5,1]. `src/Datasets/GlycolyticOscillatorDataset.py` has range defaults [90,100], [.5,1] but sampling choices include k1={80,90,100}, K1={.5,.75,1}. The page avoids claiming a single reconciled range.
4. **Training optimizer:** the paper describes Adam; `src/2.train_policy.py` uses AdamW (learning rate 2e−3), while evaluation notebooks construct AdamW with 1e−3. The page does not blend these into a single implementation/training specification.
5. **Code provenance:** no paper-specific release/tag or complete locked environment was established. The inspected training script contains a hardcoded Van der Pol checkpoint path and GPU-device assumptions. These are relevant maintenance/reproduction constraints, not claims about the research algorithm.
6. **Experiment coverage:** no quadrotor notebook/code was found in the inspected release. The quadrotor figure and claims are sourced from the paper/appendix, not falsely attributed to public code reproduction.
7. **No independent benchmark rerun:** source code, notebook cells and saved outputs, figures and checkpoints were inspected. Checkpoints were not executed or unpickled, and the reported numbers were not regenerated. Training a new model is outside website validation.
8. **No new empirical content:** all scientific plots are original paper figures. PDF-to-WebP/SVG conversion changes rendering only. The social card is a layout of the original diagram and the title, not a new scientific result.

## Inspected implementation paths

All paths below refer to the pinned commit above.

- `src/1.train_function_encoder.py`: data sampling, coefficient inference, prediction loss, basis training.
- `src/2.train_policy.py`: pretrained model wrapper, coefficient-conditioned policy, closed-loop `System`, objectives/constraints, policy optimization.
- `src/getters.py`: basis and policy construction, coefficient normalization/collection, checkpoint loading.
- `src/Integrator.py`: RK4 increment and neural ODE basis integration.
- `src/Policies/Policy.py`: coefficient normalization and bounded policy network.
- `src/Datasets/VanDerPolDataset.py`, `TwoTankDataset.py`, `GlycolyticOscillatorDataset.py`: system families, sampling, discrete-time simulation.
- `src/evaluate_VDP.ipynb`, `evaluate_TT.ipynb`, `evaluate_GO.ipynb`: checkpoint loading, true/learned models, CasADi comparisons, tracking MSE. Saved outputs include plots and numeric diagnostics; these are not substituted for Table 1.

## Maintenance rule

If a newer scientific version or code release is adopted, revise this map and the public version note together. Recheck all figures/table values and retain an explicit discrepancy record; do not silently repair the paper's numbers or infer unreported hardware/statistical settings.
