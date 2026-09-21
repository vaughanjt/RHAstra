# Riemann Space Lab — Milestone 0

This is a deliberately conservative scaffold for an AI-assisted search for a geometric/spectral
structure behind the Riemann zeta function.

The project does **not** attempt to "prove RH by brute force." It treats the problem as an
inverse spectral search:

    target arithmetic/spectral fingerprints
                ↓
        candidate space X
                ↓
      canonical operator / flow
                ↓
       trace / explicit formula
                ↓
        positivity / self-adjointness

## Design rule

A candidate is interesting only if the desired structure is **generated naturally** by the
space/dynamics. It should not be rewarded for inserting known zeta zeros into its operator by
definition.

## Primary target fingerprints

1. **Spectral counting law**

   Smooth Riemann–von Mangoldt term:

       N̄(T) = T/(2π) log(T/(2π)) - T/(2π) + 7/8

2. **Prime-orbit length structure**

   Primitive arithmetic lengths should arise naturally as

       L_p = log p

   with repetitions

       L_{p,r} = r log p.

3. **Prime-power amplitude structure**

   The oscillatory zero density suggested by the explicit formula has the schematic form

       d_osc(E) = -(1/π) Σ_p Σ_{r≥1} (log p)/p^(r/2) cos(E r log p).

   The exact normalization depends on the chosen test-function/trace-formula convention.
   We therefore test structural agreement before exact equality.

4. **Archimedean contribution**

   The Γ-factor / real-place term must emerge from the construction, not be added as an
   arbitrary correction.

5. **Functional-equation symmetry**

       ξ(s) = ξ(1-s)

   should correspond to a natural duality, involution, or geometric symmetry.

6. **Positivity / self-adjointness**

   A successful construction ultimately needs a mechanism that forces spectral parameters to
   be real (or an equivalent Weil-positivity statement).

7. **Family behavior**

   A real theory should have a natural way to pass from ζ(s) to broader L-functions, rather
   than being tuned only to one function.

8. **GUE statistics**

   This is useful, but it is intentionally a *late* gate because random-matrix universality
   makes it much less identifying than an exact prime/zero trace formula.

## Files

- `candidate_schema.json` — machine-readable "genome" for proposed spaces.
- `candidate_examples.json` — baseline descriptions of several known research directions.
- `gates.py` — inexpensive numerical/structural rejection tests.
- `benchmark.py` — sanity-checks target formulas using actual zeta zeros from `mpmath`.
- `explicit_formula_benchmark.py` — numerically checks a Weil explicit-formula identity for a log-Gaussian test family.
- `ROADMAP.md` — next milestones.

## Run

```bash
python -m pip install -r requirements.txt
python benchmark.py
python explicit_formula_benchmark.py
python gates.py candidate_examples.json
```

## What Milestone 0 can and cannot do

It can:
- enforce a common representation across otherwise incomparable approaches;
- reject candidates with the wrong counting asymptotics;
- compare proposed orbit lengths and amplitudes with the prime-power template;
- keep "evidence", "derived", and "assumed" claims separate.

It cannot yet:
- derive a trace formula from a geometric model;
- verify self-adjointness;
- prove positivity;
- synthesize genuinely new spaces.

Those become the core tasks of Milestones 1–3.
