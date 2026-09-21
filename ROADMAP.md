# Roadmap

## Milestone 0 — Representation + targets  ✅
Create a common candidate genome and encode the known fingerprints we require.

## Milestone 1 — Exact-formula benchmark  ◐
A first numerical implementation now exists for a log-Gaussian test family in `explicit_formula_benchmark.py`.
Next, generalize it to a controlled library of smooth test functions.
This becomes the central regression suite.

Deliverables:
- test-function library (Gaussian in log-coordinate, compact approximations);
- spectral side from zeta zeros;
- arithmetic side from prime powers + archimedean term;
- precision/error accounting.

**Success criterion:** both sides agree numerically to controlled precision.

## Milestone 2 — Candidate trace adapters
Every candidate family must expose the same interface:

    candidate.spectral_side(f)
    candidate.geometric_side(f)
    candidate.archimedean_side(f)
    candidate.symmetry_report()
    candidate.positivity_form(f)

Start with "control" adapters:
1. a Selberg-like toy trace model;
2. Berry–Keating smooth-counting model;
3. finite-prime truncations of an adelic/scaling model.

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
2. compare exact-formula residuals;
3. search for counterexamples;
4. ask a theorem prover/LLM to state the missing lemma precisely;
5. formalize only the smallest high-value lemma.

## Milestone 5 — L-function generalization
A survivor must explain Dirichlet twists naturally. Later extend to automorphic L-functions.

## Research discipline

Tag every statement as:
- `proved`
- `published-claim`
- `conjectural`
- `heuristic`
- `unknown`

Never allow an AI-generated derivation to silently upgrade its own status.
