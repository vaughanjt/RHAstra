# RHAstra research handoff for Codex

Prepared 2026-09-22 for James Vaughan. This is a continuation brief, not a proof of the Riemann hypothesis (RH). Repository files are authoritative for implementation; independently check mathematical claims before extending them.

## Start here

Continue the structural research in **vaughanjt/RHAstra**. The user's guiding instruction is:

> Stop trying to bound the shadow; identify the operator/space producing it.

The immediate task is to construct or reject a larger-space representation that retains the exterior boundary contribution of compressed prime shifts, and derive its exact correction to the odd Weil form. Do not drift into increasingly large eigenvalue sweeps without a specific structural question.

The user authorized continued research, code, tests, and reviewable repository changes, and asked to be told if more compute would help. No extra compute has been necessary so far. Do not assume access to purchased compute or launch paid jobs. Do not merge the draft PR merely because this handoff says to continue.

## Repository and checkpoint

- Main repository: https://github.com/vaughanjt/RHAstra
- Working draft PR: https://github.com/vaughanjt/RHAstra/pull/5
- Branch: `research/weil-normalization-audit`
- PR status verified while preparing this handoff: **open, draft, not merged**.
- Remote head at handoff: `dd7107316dded9e9a0aabd92ebae36b7551d492b`
- Base at handoff: `16b5b0b09f8110802458995e77dd5ed7c24a66f9`
- Historical attempted-proof repository: https://github.com/vaughanjt/RiemannHypothesisProof

The older repository is a source of experiments and claims to audit, not a trusted proof. The user explicitly described it as an attempt, not a proof.

For a fresh checkout:

```bash
git clone https://github.com/vaughanjt/RHAstra.git
cd RHAstra
git switch research/weil-normalization-audit
python -m pip install -e ".[dev]"
python -m pytest
```

For an existing checkout, inspect status, instructions, branch, and remote before changing anything. Fetch the current PR state; it may have advanced. Read any applicable `AGENTS.md`. Preserve unrelated user work.

In the previous environment the local checkout was `/workspace/scratch/620cad5c369e/RHAstra`. Do not depend on that path surviving. Shell push lacked credentials, so GitHub connector file writes were used; remote commit history differs from local commits while carrying the intended files. Prefer a fresh remote checkout over assuming local commit ancestry matches. The last reported full suite was **24 tests passing** (about nine seconds), on Python 3.12 with mpmath 1.4.1 and pytest 9.1.1. No new test run was performed merely to write this handoff.

## Read these files in order

1. `README.md` and `ROADMAP.md` for project conventions; the detailed notes below contain the most recent research direction.
2. `docs/candidates/odd_weil_normalization_audit.md`
3. `docs/candidates/odd_weil_structural_model.md`
4. `docs/candidates/pole_neutral_boundary_obstruction.md`
5. `rhastra/operators/odd_weil.py`
6. `rhastra/operators/weil_reference.py`
7. `rhastra/operators/translation_energy.py`
8. `rhastra/operators/pole_boundary.py`
9. Corresponding tests and `experiments/` results.

`docs/candidates/odd_weil_operator.md` is the short candidate overview. The structural and boundary notes supersede its earlier emphasis on tail estimates as the immediate next task.

## Mathematical setup and conventions

Write \(L=\log(\lambda^2)>0\). The implementation currently accepts `lambda_squared >= 2`.

Zero-extend the orthonormal modes

\[
U_n(x)=L^{-1/2}e^{2\pi inx/L},\qquad x\in[0,L].
\]

Their normalized odd combinations give a unitary map onto the **reflection-odd subspace**, not all of \(L^2[0,L]\):

\[
(\mathcal Uc)(x)=i\sqrt{2/L}\sum_{n\ge1}c_n\sin(2\pi nx/L),
\qquad f(L-x)=-f(x).
\]

The arithmetic form is \(M=W_{\mathbb R}+\sum_pW_p\). Its odd coefficient kernel is

\[
K_{jj}=a_j+B_j/j,\qquad
K_{jk}=\frac{2(jB_k-kB_j)}{j^2-k^2}\quad(j\ne k).
\]

Here \(a_{-n}=a_n\), \(B_{-n}=-B_n\); the definitions and special-function formulas are in `LegacyWeilCoefficients`. They use arithmetic data, not known zeta zeros.

### Normalization resolved

The diagonal correlation is

\[
\omega_{nn}(y)=2(1-y/L)\cos(2\pi ny/L),\quad0\le y\le L.
\]

The triangular overlap factor is essential. Let \(C_0=\gamma+\log(4\pi)\). Splitting the archimedean integral at L produces

\[
C(L)=C_0+\log\frac{e^L-1}{e^L+1}.
\]

The executable legacy formula matches this convention. The later legacy TeX draft omitted the triangular factor and used the finite-tail-adjusted constant with an infinite integral, double-counting the tail. Existing executable coefficient values did not need changing.

### Operator status

A legitimate Fourier unitary representation replaces the old Session 82 heuristic of treating a Fourier index as a physical position. It does **not** validate Session 82's proposed pointwise Cauchy integral kernel.

The canonical self-adjoint form realization is attributed to a literature closed-form/core theorem plus bounded perturbation, recorded as `published-claim`. This does not establish essential self-adjointness of the minimal matrix operator on `c_00`, positivity, or a spectrum consisting of zeta-zero ordinates. A form-domain description uses the zero-extended function's Fourier transform weighted by \(\log(2+|t|)\). Keep form and operator domains distinct.

## Correction: the odd pole term survives

Define

\[
A_L=32L\sinh^2(L/4),\quad d_j=L^2+16\pi^2j^2,
\quad v_j=\sqrt{32\pi^2A_L}\frac{j}{d_j}.
\]

The pole block is \(P^-=-vv^*\), hence

\[
\boxed{Q^-=-K-vv^*.}
\]

The target is therefore \(-K\ge vv^*\), not merely \(K\le0\). Even proving the full odd inequality would leave even-sector and all-cutoff obligations.

For finite positive definite \(A_N=-K_N\), rank-one domination is equivalent to
\(r_N=v_N^*A_N^{-1}v_N\le1\). Use linear solves; check positivity before using this characterization. Do not assume a bounded inverse exists in the infinite-dimensional setting.

## Independent positive energy model

Let \(\tau_yf(x)=f(x-y)\) on the full real line, with f zero extended. Put

\[
\rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},\quad
w_q=\frac{\Lambda(q)}{\sqrt q},\quad y_q=\log q,
\quad1<q\le e^L.
\]

Only prime powers have nonzero weights. Define

\[
D_L[f]=\int_0^\infty\rho(y)\|\tau_yf-f\|_2^2dy
+\sum_qw_q\|\tau_{y_q}f-f\|_2^2.
\]

This is \(\|Tf\|^2\) in the explicit direct-sum Hilbert space described in the structural note. T is defined from shifts and positive weights, **not** by taking a square root of the target matrix. It is unbounded and has its finite-energy domain; do not claim it acts on all L2 functions.

With

\[
b_L=\log\pi-\psi(1/4)+2\sum_qw_q,
\qquad
\ell_L(f)=\sqrt2\int_0^Lf(x)\sinh((x-L/2)/2)dx,
\]

we derived and tested

\[
-K[f]=D_L[f]-b_L\|f\|^2,
\]

\[
\boxed{Q^-[f]=\|Tf\|^2-b_L\|f\|^2-|\ell_L(f)|^2.}
\]

For \(f=\mathcal Uc\), \(\ell_L(f)=-i\,v^Tc\). Positivity of D alone does not imply positivity after the mass and moment subtractions. The structural question is whether \(f\mapsto(\sqrt{b_L}f,\ell_L(f))\) is a contraction in the independently defined T-energy norm. This is a useful reformulation, **not** a proof or a discovery of inevitability.

Use full-line shifts plus zero extension. Periodic shifts give a different form.

## Latest result: exact boundary obstruction

The most recent work investigated whether the pole-neutral space \(\ker\ell_L\) could simply be preserved by compressed prime shifts. It cannot, in general.

Let E be zero extension, \(P_I\) the interval cutoff, and

\[
S_y=P_I(\tau_y+\tau_{-y})E,\quad0<y<L,
\quad h(t)=\sinh((t-L/2)/2).
\]

For odd f, an exact change of variables gives

\[
\boxed{\ell_L(S_yf)=2\cosh(y/2)\ell_L(f)-\beta_y(f)},
\]

\[
\boxed{\beta_y(f)=2\sqrt2\int_{L-y}^Lh(t+y)f(t)dt.}
\]

This is an identity for the physical shifted function, with **no Fourier truncation of its output**.

For \(0<y<L/2\), smooth reflected bumps prove non-invariance: choose an interior odd g with nonzero ell and zero beta, and an endpoint-supported odd f with nonzero beta. Then \(f-\ell(f)g/\ell(g)\) is pole neutral but has nonzero beta. Since S_y is self-adjoint, the orthogonal projection onto ker(ell) does not commute with this S_y.

Important limitation: this rules out a simple prime-by-prime invariance argument. It does not rule out cancellations in the complete weighted form, a different projection, or a larger intertwining representation.

On the full real line the exponential moment transforms without this defect, but support expands. The exterior contribution removed by the interval cutoff is exactly beta_y. **Retaining and controlling that exterior channel is the current next task.** Compressed translations do not obey the full translation group law and must not be treated as a unitary representation.

## Numerical checkpoints and tests

These are high-precision numerical regressions, not interval certificates or infinite-dimensional proofs.

| cutoff lambda_squared | N | 1-r_N | smallest eigenvalue of Q^-_N |
|---:|---:|---:|---:|
| 2 | 10 | 8.85240e-1 | 8.83245e-2 |
| 20 | 3 | 1.27536e-10 | 2.68092e-11 |
| 20 | 6 | 2.45646e-17 | 2.46053e-18 |
| 20 | 10 | 1.01769e-25 | 6.70954e-27 |
| 50 | 10 | 1.42189e-30 | 1.63614e-31 |

At cutoff 20, N=3, \(\lambda_{\max}(K)\approx-1.0838189478357864\times10^{-6}\). The much smaller positive Q gap illustrates why retaining the pole matters.

The nine-case probe uses cutoffs 2, 20, 50 and N=3,6,10. The hardest case was recomputed at 100 versus 70 digits; relative differences in the gap and minimum Q eigenvalue were about 4.3e-40. Near-alignment of finite extremizers does not establish a limiting vector or exact null state.

Boundary witness at L=log 20, y=log 2:

- c is the normalized two-mode vector proportional to (v_2,-v_1).
- Coefficients approximately (0.462059837105708, -0.886848750877987).
- Initial pole moment is zero symbolically.
- Shifted pole moment is approximately -0.561223085000262 i.
- Boundary defect is approximately +0.561223085000262 i.
- At 60 working digits the identity residual was about 1.6e-61.

Relevant artifacts:

- `experiments/translation_energy_probe.py`
- `experiments/translation_energy_results.json`
- `experiments/translation_energy_precision_check.json`
- `experiments/pole_boundary_witness.json`
- `tests/test_weil_normalization.py`
- `tests/test_translation_energy.py`
- `tests/test_pole_boundary.py`

Run the main probe from the repository root with:

```bash
python -m experiments.translation_energy_probe
```

The test suite also includes a fresh-process import check: a pre-existing circular import was fixed by lazily exporting `OddWeilOperatorCandidate` in `rhastra/candidates/__init__.py`.

## Primary literature and scope

1. Connes, Consani **and Moscovici**, *Zeta Spectral Triples*, arXiv:2511.22755v1:
   https://arxiv.org/html/2511.22755v1
   - Sections 2–4: conventions, form, basis, matrix formulas.
   - Propositions 3.3–3.4, Theorem 3.6: closed-form/core and spectral results used in the realization transfer.
   - Section 8 explicitly identifies missing steps. Do not treat finite spectral triples as a completed RH proof.
2. Connes and Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771:
   https://arxiv.org/pdf/2006.13771
   - Introduction and Theorem 1: positive compressed trace using the Sonin projection, with restricted support and transform-vanishing hypotheses.
   - Scaling does not have to preserve the Sonin space for their positive trace construction. Our boundary obstruction does not refute it.
   - The real-coordinate even Sonin space is not the same space as our logarithmic-coordinate odd subspace. An intertwiner must be constructed, not presumed from terminology.

## Recommended next work

1. Re-read the exact boundary identity and derive the full inside/outside block decomposition for the dilation action before imposing the cutoff.
2. Identify which positive trace or norm can be constructed on that larger space independently of the target inequality.
3. Compute the exact difference between that construction and Q^-, retaining the mass, pole, and boundary terms. Specify domains and convergence.
4. Test a concrete candidate on the existing prime-2 boundary witness. A proposal that silently drops beta_y is already rejected.
5. If using Sonin or semilocal geometry, establish the actual map, measures, support conditions, and correction formula. Do not extend the archimedean theorem to all primes by analogy.
6. Seek an analytic sign mechanism or a precise obstruction. Use finite probes to falsify structural guesses, not as substitutes for that mechanism.
7. Save substantive derivations, counterexamples, and meaningful tests in the repository; maintain explicit claim provenance and update the reviewable PR/branch as appropriate.

Do not silently replace this objective with a broad literature survey or brute-force size sweep. If a proposed compute job could resolve a specific uncertainty, explain its purpose, expected cost, and stopping criterion to the user first.

## Research discipline

- No proof of RH has been obtained.
- Do not infer positivity from self-adjointness, compact resolvent, symmetry, or finite tests.
- Do not use known zeta zeros as hidden input to an independent candidate. Existing explicit-formula zero-based benchmarks are calibration only.
- Distinguish algebraic derivations, attributed literature results, numerical evidence, conjectures, and open obligations.
- Independently audit prior agent claims, including this handoff; do not upgrade evidence status by repetition.
- Avoid circular constructions: a square root of Q, or an energy norm requiring the desired positivity, cannot explain that positivity independently.
- Separate the odd sector, even sector, fixed cutoff, and all-cutoff statements.
- Do not relabel the Fourier index as a spatial coordinate.
- A rejected shortcut is useful progress, but does not disprove broader operator approaches.

## Suggested first response to the user

Briefly confirm that you have read the handoff and repository notes, identify the retained-boundary representation as the active task, and begin the actual derivation. Continue autonomously with justified, reviewable work. The user has already asked to proceed and to be notified if additional compute becomes useful.
