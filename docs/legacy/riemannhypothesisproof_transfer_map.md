# Legacy Transfer Map: RiemannHypothesisProof → RHAstra

## Purpose

The repository `vaughanjt/RiemannHypothesisProof` is treated here as an **experimental archive**, not as a claimed proof of the Riemann Hypothesis.

This transfer map extracts durable results from roughly 82 exploratory sessions while keeping four categories separate:

- **SURVIVES** — an identity, theorem, rigorous finite computation, or reproducible structural observation worth importing.
- **OPEN** — a formulation or conjecture that survived testing but still contains the RH-level obstacle.
- **KILLED** — a route that failed numerically, structurally, or logically and should become a rejection rule.
- **CIRCULAR** — a route whose decisive estimate was found to encode essentially the same difficulty as RH.

Nothing here upgrades an unpublished computational claim into a theorem. Every imported item must retain provenance.

## Executive transfer map

| ID | Finding | Disposition | Evidence | RHAstra use |
|---|---|---|---|---|
| L01 | Weil/explicit-formula reconstruction of the barrier | SURVIVES | exact/reference identity + numerical reproduction | calibration target only |
| L02 | Cauchy–Loewner form of the Weil matrix | SURVIVES | algebraic/derived structure, machine-precision checks | candidate/operator structure |
| L03 | Exact even/odd parity decomposition | SURVIVES | algebraic symmetry | mandatory structural gate |
| L04 | Lorentzian signature of the full matrix | OPEN | broad finite computation | conjecture, not evidence of RH |
| L05 | Finite interval verification of odd-block negativity | SURVIVES | interval arithmetic at sampled parameters | rigorous finite benchmark |
| L06 | Near-zero critical direction / extreme cancellation | SURVIVES | numerical spectral diagnostic | sensitivity/adversarial test |
| L07 | Cramér primes destroy the observed signature | SURVIVES | falsification experiment | prime-specificity control |
| L08 | Margin–drain concentration strategy | CIRCULAR | explicit random-prime stress test | reject generic concentration arguments |
| L09 | Naive heat-kernel/modular shortcut | KILLED | direct model mismatch / exact-formula reconstruction | prevent rediscovery |
| L10 | Primes → barrier → ESPRIT → approximate zero frequencies | SURVIVES | numerical inverse-spectral diagnostic | discovery diagnostic, never proof |
| L11 | Operator lift (K_{odd}=D+H) | OPEN | convergent finite-section evidence / formal analogy | high-priority operator candidate |
| L12 | Gauge-symmetry no-go for naive Hermitian transfer operators | SURVIVES | elementary unitary-equivalence argument | candidate rejection theorem |
| L13 | Spectral completeness in the operator program | OPEN | unresolved logical gap | explicit proof obligation |
| L14 | Finite-(T) arithmetic correction to GUE pair statistics | SURVIVES* | empirical preprint-level computation | optional spectral fingerprint |
| L15 | Peak–gap / “eigenvector rigidity” phenomenon | SURVIVES* | empirical preprint-level computation | optional eigenfunction fingerprint |

`SURVIVES*` means “worth reproducing,” not “established mathematical fact.”

---

## L01 — Explicit formula / Weil barrier is a calibration identity

**Disposition:** SURVIVES — calibration only.

Later sessions found that the computed barrier signal could be reconstructed from the Weil explicit-formula components to machine precision when the correct (L)-dependent amplitudes were used. This is important because it kills interpretations in which unexplained residual structure is treated as new geometry.

**RHAstra rule:** a model receives no discovery credit for reproducing a quantity that has been explicitly reconstructed from known zero/prime data. Use the identity only to calibrate trace-formula implementations.

**Sources**
- `.planning/STATE.md` — Sessions 49–50 report the residual collapsing to machine precision with the proper Weil amplitudes.
- `session79b_explicit_formula_forces_lorentzian.py` — explicitly treats the matrix construction as the arithmetic side of the explicit formula.

---

## L02 — Cauchy–Loewner structure of the matrix

**Disposition:** SURVIVES.

The matrix (M) was decomposed in the form

[
M_{nm}=a_ndelta_{nm}+rac{B_m-B_n}{n-m}, qquad n
e m,
]

with (a_n) and (B_n) determined by the archimedean and prime terms. The exploratory code reports machine-precision reconstruction of off-diagonal entries.

This is one of the strongest reusable structural findings because it converts a large opaque matrix into a structured divided-difference / singular-integral object.

**RHAstra use:** re-derive symbolically from definitions, then expose this as an executable candidate adapter rather than trusting the legacy numerical check.

**Sources**
- `session59b_cauchy_structure.py`
- `docs/lorentzian_weil_conjecture.tex`, Definition “Cauchy–Loewner structure.”

---

## L03 — Exact parity decomposition

**Disposition:** SURVIVES.

The involution (nmapsto -n) commutes with the matrix construction, producing independent even and odd blocks.

[
V_+={v:v_{-n}=v_n}, qquad
V_-={v:v_{-n}=-v_n}.
]

**RHAstra use:** any adapter built from this matrix family should preserve the symmetry exactly. Failure is an implementation error, not a novel effect.

**Source**
- `docs/lorentzian_weil_conjecture.tex`, parity decomposition.

---

## L04 — Lorentzian signature conjecture

**Disposition:** OPEN.

Across the tested range, the full matrix was observed to have at most one positive eigenvalue, while the odd block was negative definite. The archived paper formulates this as the **Lorentzian Weil Matrix Conjecture**.

This is potentially interesting, but it is not a proof shortcut: the archive itself concludes that the prime-specific arithmetic content is doing the hard work.

**RHAstra use:** treat signature as a candidate fingerprint and adversarial test, not as a premise.

**Source**
- `docs/lorentzian_weil_conjecture.tex`.

---

## L05 — Rigorous finite verification of odd-block negativity

**Disposition:** SURVIVES, strictly finite.

The archive contains a ball/interval-arithmetic implementation using a Sylvester-criterion check. The paper reports negative definiteness at 134 sampled parameter values over a large finite range.

This is materially stronger than ordinary floating-point eigenvalue plots, but it proves only those finite matrices at those finite parameters.

**RHAstra use:** reproduce a small subset independently and preserve them as regression tests.

**Sources**
- `session80b_interval_verification.py`
- `docs/lorentzian_weil_conjecture.tex`.

---

## L06 — The critical direction is a knife-edge cancellation

**Disposition:** SURVIVES as a diagnostic.

The largest odd-block eigenvalue approaches zero from below and is produced by a very delicate cancellation between archimedean and prime contributions. Legacy sessions report margins around (10^{-7})–(10^{-8}) in representative truncations.

**RHAstra use:** this should become a numerical-stability gate. Any mutation that “proves” negativity with a loose norm or Gershgorin-type estimate is suspect because the observed margin is many orders of magnitude smaller than generic component norms.

**Sources**
- `.planning/STATE.md`, Sessions 56–58.
- `docs/lorentzian_weil_conjecture.tex`, critical-direction discussion.

---

## L07 — Random prime-like sequences do not reproduce the signature

**Disposition:** SURVIVES as a falsification control.

Replacing actual primes with count-matched Cramér-model primes destroys the odd-block negative-definiteness / Lorentzian behavior in the reported experiments.

This is valuable because it says the phenomenon is not a generic consequence of “roughly prime density.” It depends on finer arithmetic organization.

**RHAstra use:** every arithmetic candidate should be tested against randomized-prime controls.

**Sources**
- `session54_cramer_concentration.py`
- `session79b_explicit_formula_forces_lorentzian.py`
- `docs/lorentzian_weil_conjecture.tex`.

---

## L08 — Generic concentration cannot close the margin–drain gap

**Disposition:** CIRCULAR / DEAD AS A GENERIC ROUTE.

Session 54 explicitly stress-tested the idea that a Cramér-type concentration bound might control the prime “drain.” Instead, the random-model standard deviation grows while the desired margin stays small; violation probability becomes worse at larger (L).

The archive’s conclusion is important: real primes are **atypically coordinated** relative to the naive random model, so a generic concentration inequality is not the missing theorem.

**RHAstra rejection rule:** do not spend compute on arguments whose decisive step is “the weighted prime phases should concentrate like independent noise.”

**Source**
- `session54_cramer_concentration.py`
- `.planning/STATE.md`, Session 54 summary.

---

## L09 — Naive heat-kernel / modular shortcut was killed

**Disposition:** KILLED.

The project tested several attempts to reinterpret the barrier as a classical heat-kernel or modular signal. Later reconstruction showed that the apparent residual modular content was explained by the explicit formula when the correct varying amplitudes were used.

**RHAstra rejection rule:** a visually suggestive modular or heat-kernel fit must beat the exact explicit-formula baseline out of sample. Otherwise it is not new structure.

**Source**
- `.planning/STATE.md`, Sessions 48–50.

---

## L10 — ESPRIT can recover approximate zero frequencies from the barrier

**Disposition:** SURVIVES as an inverse-spectral diagnostic.

One pipeline was

[
	ext{primes} ightarrow B(L) ightarrow 	ext{Hankel/ESPRIT} ightarrow
	ext{frequencies near zeta zeros}.
]

The ESPRIT rotation eigenvalues were numerically near the unit circle and recovered low zero frequencies approximately.

This is intriguing, but the attempted bridge “low displacement rank (Rightarrow) unitary ESPRIT matrix” did not become a proof. Later work also noted that some low-rank Hankel facts were generic and therefore non-identifying.

**RHAstra use:** use ESPRIT as a diagnostic for whether a candidate trace signal contains the correct spectral frequencies. Never treat frequency recovery as evidence that all zeros lie on the critical line.

**Sources**
- `session60_esprit_unitarity.py`
- `.planning/STATE.md`, Sessions 60a–60d.

---

## L11 — Operator lift (K_{odd}=D+H)

**Disposition:** OPEN; high priority for re-derivation.

Session 82 reframed finite odd-block matrices as sections of a singular integral operator

[
K_{mathrm{odd}}=D_{mathrm{odd}}+H_{mathrm{odd}},
]

with a multiplication part and a Cauchy-type integral part. Finite-section top eigenvalues were reported to stabilize.

This is directly relevant to RHAstra’s present inverse-spectral program because it asks for the **space and operator behind the matrix**, rather than another finite matrix inequality.

However, statements about boundedness, domains, self-adjointness, and exact equivalence to the Connes operator need functional-analytic proof; the legacy script contains exploratory assertions, not a formal operator construction.

**RHAstra use:** import as a candidate hypothesis, then rebuild from first principles with explicit domain, measure, kernel regularization, and self-adjointness proof obligations.

**Source**
- `session82_operator_lift.py`.

---

## L12 — Gauge-symmetry no-go theorem for naive transfer operators

**Disposition:** SURVIVES; recheck algebraically.

For transfer matrices whose (t)-dependence enters only through conjugate multiplicative phases, the archived operator paper proves

[
L(t)=D(t)L(0)D(t)^{-1},
]

with (D(t)) unitary. Therefore the spectrum is (t)-independent and cannot detect zeta zeros as crossings.

This is a cheap and useful elimination theorem.

**RHAstra rejection rule:** before numerically exploring any Hermitian arithmetic transfer operator, test whether its spectral parameter can be gauged away by unitary diagonal conjugation.

**Source**
- `docs/operator_framework.tex`, Gauge Symmetry theorem.

---

## L13 — Spectral completeness is the real Hilbert–Pólya gap

**Disposition:** OPEN.

The operator framework produced trajectories that numerically approach some zeros, but the unresolved step was to prove that **all** relevant trajectories land on **all** zeta zeros with no missing or spurious spectrum.

This is an excellent example of a proof obligation that must not be replaced by numerical matching.

**RHAstra use:** make “spectral completeness” an explicit gate for every Hilbert–Pólya-style candidate:
1. existence of the operator,
2. correct self-adjoint domain,
3. spectral counting law,
4. no missing spectral points,
5. no extraneous spectral points,
6. exact trace/arithmetic correspondence.

**Source**
- `docs/operator_framework.tex`.

---

## L14 — Finite-(T) deviations from GUE carry arithmetic frequencies

**Disposition:** SURVIVES* — reproduction required.

The archived finite-(T) study reports that deviations of zero pair statistics from a GUE baseline can be modeled using oscillations at prime-related frequencies, while higher-order tests were reported closer to GUE.

This is potentially useful as a **late-stage fingerprint**, not as a proof ingredient.

The claims are empirical and preprint-level; RHAstra should independently reproduce them before using them as candidate rejection criteria.

**Source**
- `docs/finite_T_pair_correlation.tex`.

---

## L15 — Peak–gap “eigenvector rigidity”

**Disposition:** SURVIVES* — reproduction required.

The archive reports a strong correlation between consecutive zero gaps and (|Z(t)|) at interval midpoints, much larger than the analogous characteristic-polynomial statistic in the chosen GUE comparison.

If robust, this suggests that matching zero eigenvalue statistics alone is insufficient: a candidate operator may also need non-Haar structure in its eigenfunctions/eigenvectors.

Again, this is an empirical exploratory claim and must be reproduced independently before it becomes an RHAstra gate.

**Source**
- `docs/eigenvector_rigidity.tex`.

---

## What should *not* be imported as “proof”

The legacy repository contains Lean files, theorem-shaped LaTeX, interval computations, and many statements labeled “proved” inside exploratory scripts. None of that by itself constitutes a formal proof of RH.

In particular:
- the Lean umbrella file imports auxiliary modules; it does not establish RH;
- finite interval verification does not establish the infinite parameter range;
- a conjecture equivalent or close to RH is a useful reformulation, not progress unless it exposes a genuinely easier theorem;
- numerical recovery of known zeros is a diagnostic, not spectral completeness.

## Immediate RHAstra actions

1. **Import L12 first** as a cheap no-go gate.
2. **Re-derive L02 + L03 symbolically** and put them under unit tests.
3. **Reproduce L05 at 3–5 parameters** using independent code and interval arithmetic.
4. **Build randomized-prime controls from L07/L08** into every arithmetic candidate benchmark.
5. **Prototype L11 as a formal candidate adapter**, with operator domain/self-adjointness marked `UNKNOWN` until proved.
6. Keep L14/L15 outside the core proof loop until independently reproduced.

## Source repository

Original experimental archive: `vaughanjt/RiemannHypothesisProof`.

This file intentionally records both successes and failures. In RHAstra, a killed approach is an asset if it prevents the search system from spending compute rediscovering the same dead end.
