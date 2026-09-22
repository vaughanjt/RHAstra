# Roadmap

## Milestone 0 — Representation + targets ✅

Create a common candidate genome and encode the known fingerprints we require.

## Milestone 1 — Exact-formula benchmark ✅ baseline / ongoing expansion

A log-Gaussian Weil explicit-formula regression is implemented in
`rhastra/explicit_formula.py`.

Next expansion:
- additional admissible test-function families;
- explicit truncation/error accounting;
- precision sweeps.

## Milestone 2 — Candidate trace adapters ◐

Implemented:
- abstract `CandidateAdapter` contract;
- typed metadata, claims, symmetry and positivity reports;
- `StaticCandidateAdapter` for literature-only candidates;
- executable-trace gate;
- provenance gate rejecting known-zero leakage outside calibration;
- package metadata and pytest suite;
- GitHub Actions test workflow.

Next control adapters:
1. Selberg-like toy trace model;
2. Berry–Keating smooth-counting model;
3. finite-prime adelic/scaling toy model.

Milestone 2 is complete when at least two independent executable trace adapters
pass through the same test-function and gate interface.

## Operator Track A — Odd Weil coefficient operator ◐

The legacy Session 82 continuum lift has been reconstructed conservatively.

Established:
- exact Cauchy--Loewner parity reduction;
- natural coefficient-space core `c_00(N) ⊂ ell^2(N)`;
- real symmetric formal kernel;
- finite sections as exact compressions;
- arithmetic coefficient generator using the legacy executable normalization;
- regression test at a knife-edge finite section.

Normalization audit completed:
- executable diagonal matches the correlation functional;
- the finite tail constant and triangular overlap are derived;
- a unitary Fourier representation onto reflection-odd L2 is identified;
- closability/canonical realization are attributed to a literature theorem;
- the full odd Weil target is corrected to `-K >= v v*`.

Open proof obligations:
1. prove coefficient/tail estimates uniformly in the relevant cutoff range;
2. establish rank-one domination on the closed form domain;
3. address the even sector and all-cutoff quantifiers;
4. derive any claimed trace-spectrum identification independently.

See `docs/candidates/odd_weil_normalization_audit.md`.

## Milestone 3 — Mutation grammar

Allow constrained modifications of:
- quotient/group/action;
- measure;
- boundary/domain conditions;
- cocycles/local systems;
- archimedean component;
- operator ordering/self-adjoint extensions;
- cohomological degree;
- twists by characters.

Mutations are rejected if they merely insert known zero locations.

## Milestone 4 — Automated conjecture loop

For each survivor:
1. derive symbolic asymptotics;
2. compare explicit-formula residuals;
3. search for counterexamples;
4. state the smallest missing lemma precisely;
5. formalize only the highest-value surviving lemma.

## Milestone 5 — L-function generalization

A survivor must explain Dirichlet twists naturally. Later extend to broader
automorphic L-functions.

## Research discipline

Every claim must remain tagged as one of:
- `proved`
- `derived`
- `published-claim`
- `conjectural`
- `heuristic`
- `unknown`
- `not-implemented`

An AI-generated derivation may not upgrade its own evidentiary status without an
independent check.
