# Legacy Transfer Map: RiemannHypothesisProof → RHAstra

## Purpose

The repository \`vaughanjt/RiemannHypothesisProof\` is treated as an **experimental archive**, not as a claimed proof of the Riemann Hypothesis.

The transfer rule is simple:

- **SURVIVES** — reusable identity, theorem, rigorous finite check, or reproducible structural observation.
- **OPEN** — promising formulation with a proof-level obstacle still present.
- **KILLED** — route falsified or structurally invalid in the legacy work.
- **CIRCULAR** — decisive estimate was found to encode essentially the same difficulty as RH.

Nothing is promoted to theorem status merely because it appeared in a paper draft, script, or Lean file.

## Executive map

| ID | Finding | Status | RHAstra use |
|---|---|---:|---|
| L01 | Weil / explicit-formula reconstruction of the barrier | SURVIVES | calibration only |
| L02 | Cauchy–Loewner form of the Weil matrix | SURVIVES | operator structure |
| L03 | Exact even/odd parity decomposition | SURVIVES | structural gate |
| L04 | Lorentzian signature of the full matrix | OPEN | conjecture + stress test |
| L05 | Finite interval verification of odd-block negativity | SURVIVES | rigorous finite regression |
| L06 | Near-zero critical direction / extreme cancellation | SURVIVES | sensitivity gate |
| L07 | Cramér primes destroy the observed signature | SURVIVES | randomized negative control |
| L08 | Margin–drain concentration strategy | CIRCULAR | rejection rule |
| L09 | Naive heat-kernel / modular shortcut | KILLED | rejection rule |
| L10 | Primes → barrier → ESPRIT → approximate zero frequencies | SURVIVES | diagnostic only |
| L11 | Odd Weil operator lift | OPEN | high-priority operator candidate |
| L12 | Gauge-symmetry no-go for naive Hermitian transfer operators | SURVIVES | cheap rejection theorem |
| L13 | Spectral completeness in the operator program | OPEN | mandatory proof obligation |
| L14 | Finite-T arithmetic correction to GUE pair statistics | SURVIVES* | optional late-stage fingerprint |
| L15 | Peak-gap “eigenvector rigidity” | SURVIVES* | optional eigenfunction fingerprint |

\`SURVIVES*\` means “worth reproducing independently,” not “established mathematical fact.”

---

## L01 — Explicit formula / Weil barrier

Later sessions reconstructed the computed barrier signal from the explicit-formula components once the correct parameter-dependent amplitudes were used.

**Use:** calibration only. A model gets no discovery credit for reproducing a quantity built from known zero/prime data.

**Sources**
- legacy \`.planning/STATE.md\`, Sessions 49–50
- legacy \`session79b_explicit_formula_forces_lorentzian.py\`

---

## L02 — Cauchy–Loewner structure

The finite Weil matrix has off-diagonal structure

\[
M_{nm}=\frac{B_m-B_n}{n-m}, \qquad n\neq m,
\]

with a separate diagonal sequence.

The arithmetic prime contribution and the archimedean alpha contribution both fit this divided-difference form.

**Use:** core structured-matrix / operator representation.

**Important reconstruction note:** the old executable and later paper draft disagree on the archimedean diagonal normalization. RHAstra therefore treats the structural divided-difference identity as durable, while the exact diagonal formula remains a first-principles proof obligation.

**Sources**
- legacy \`session59b_cauchy_structure.py\`
- legacy \`connes_crossterm.py\`
- legacy \`docs/lorentzian_weil_conjecture.tex\`

---

## L03 — Exact parity decomposition

The involution \(n\mapsto -n\) splits the matrix into exact even and odd blocks.

**Use:** mandatory implementation invariant.

RHAstra has now re-derived the odd block algebraically.

---

## L04 — Lorentzian signature conjecture

The legacy computations repeatedly observed one positive direction in the full matrix and negative definiteness in the odd block.

**Status:** OPEN.

The archive itself eventually concluded that the prime-specific arithmetic content is doing the hard work, so this is a reformulation / fingerprint, not a shortcut.

---

## L05 — Finite interval verification

The archive contains ball-arithmetic Sylvester checks for negative definiteness at sampled finite parameters.

**Use:** finite regression targets only.

A finite interval proof at sampled parameters is not an argument for the infinite parameter range.

---

## L06 — Knife-edge critical direction

The top odd eigenvalue can sit extremely close to zero. Representative legacy margins were around \(10^{-7}\) to \(10^{-8}\).

**Use:** numerical sensitivity gate.

Any proposed analytic inequality that loses several orders of magnitude should be rejected early.

---

## L07 — Cramér primes fail

Count-matched random prime-like sequences did not reproduce the observed odd-block negativity / Lorentzian behavior.

**Use:** randomized-prime negative control.

This shows the phenomenon depends on more than prime density.

---

## L08 — Generic margin–drain concentration

The Cramér stress tests showed that a generic concentration argument gets worse, not better, in the tested regime.

**Status:** CIRCULAR / dead as a generic route.

**Rejection rule:** do not assume weighted prime phases behave like independent noise unless that assumption itself is proved with the required strength.

---

## L09 — Naive heat-kernel / modular shortcut

Several apparent modular or heat-kernel signals disappeared after the exact explicit-formula structure was accounted for.

**Status:** KILLED.

**Rejection rule:** a new fitted structure must beat the exact explicit-formula baseline out of sample.

---

## L10 — ESPRIT frequency recovery

The legacy pipeline

\[
\text{primes} \to \text{barrier signal} \to \text{ESPRIT} \to \text{frequencies}
\]

recovered approximate low zeta-zero frequencies.

**Use:** inverse-spectral diagnostic only.

Frequency recovery is not spectral completeness and is not evidence that all zeros lie on the critical line.

---

## L11 — Odd Weil operator lift

### Legacy claim

Session 82 promoted the finite odd matrices to an operator on \(L^2[0,L]\) by replacing the Fourier mode index \(n\) with a real variable.

### RHAstra correction

That step is not a derivation of a continuum operator. The same variable was used as both:

1. a Fourier / coefficient index, and
2. a physical coordinate.

The mathematically immediate lift is instead the coefficient-space quadratic form on

\[
c_{00}(\mathbb N)\subset \ell^2(\mathbb N).
\]

If the full Cauchy–Loewner data satisfy

\[
a_{-n}=a_n,\qquad B_{-n}=-B_n,
\]

then the exact odd kernel is

\[
K_{jj}=a_j+\frac{B_j}{j},
\]

and for \(j\neq k\),

\[
K_{jk}=\frac{2(jB_k-kB_j)}{j^2-k^2}.
\]

RHAstra now implements this object.

**Established:** real symmetric form on \(c_{00}\), exact finite compressions.

**Still open:** closability, self-adjoint realization, domain, continuum representation, and global non-positivity.

**RHAstra source**
- \`docs/candidates/odd_weil_operator.md\`
- \`rhastra/operators/odd_weil.py\`

---

## L12 — Gauge-symmetry no-go

For a class of Hermitian transfer matrices whose spectral parameter enters only through multiplicative conjugate phases, the parameter can be removed by diagonal unitary conjugation:

\[
L(t)=D(t)L(0)D(t)^{-1}.
\]

The spectrum is therefore independent of \(t\).

**Use:** cheap pre-compute rejection gate for proposed operator families.

---

## L13 — Spectral completeness

The old operator program could numerically land some eigenvalue trajectories near zeros, but it never proved that all and only the correct spectral points occur.

**Mandatory Hilbert–Pólya gates:**
1. define the operator;
2. prove the domain/self-adjointness;
3. derive the counting law;
4. prove no missing spectrum;
5. prove no spurious spectrum;
6. derive the exact arithmetic trace structure.

---

## L14 — Finite-T arithmetic correction to GUE

The legacy pair-correlation work reports prime-frequency structure in finite-height deviations from the GUE limit.

**Status:** empirical / reproduction required.

**Use:** optional late-stage fingerprint after independent reproduction.

---

## L15 — Peak-gap “eigenvector rigidity”

The archive reports a strong correlation between zeta gap size and \(|Z(t)|\) between zeros, much larger than the chosen GUE characteristic-polynomial control.

**Status:** empirical / reproduction required.

If robust, it suggests that matching eigenvalue statistics alone is insufficient; candidate eigenfunctions may also carry arithmetic structure.

---

## What is explicitly not transferred as proof

- the Lean umbrella file does not prove RH;
- theorem-shaped LaTeX does not establish theorem status;
- finite computation does not establish the infinite range;
- numerical zero recovery is not spectral completeness;
- a reformulation equivalent to RH is only useful if it exposes a genuinely easier theorem.

## Source repository

Original archive: \`vaughanjt/RiemannHypothesisProof\`.
