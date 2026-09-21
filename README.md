# RHAstra

RHAstra is a deliberately conservative scaffold for an AI-assisted search for a
geometric or spectral structure behind the Riemann zeta function.

The project does **not** try to prove RH by brute force. It treats the problem as
an inverse-spectral search:

    target arithmetic/spectral fingerprints
                ↓
        candidate space X
                ↓
      canonical operator / flow
                ↓
       trace / explicit formula
                ↓
        positivity / self-adjointness

## Research rules

1. A candidate receives credit only for structure that is generated naturally by
   the space/dynamics.
2. Known zeta-zero locations may be used in explicitly labeled calibration
   experiments, never as hidden input to a proposed construction.
3. Unknown and unimplemented claims stay unknown; they are not scored as partial
   success.
4. Every claim carries provenance: proved, derived, published claim,
   conjectural, heuristic, unknown, or not implemented.

## Target fingerprints

A serious candidate should eventually explain:

- the smooth Riemann–von Mangoldt counting law;
- primitive arithmetic lengths `log p` and repetitions `r log p`;
- the correct prime-power amplitudes;
- the archimedean / Γ-factor contribution;
- the functional equation as a natural symmetry or duality;
- a positivity or self-adjointness mechanism;
- natural extension to broader L-functions;
- GUE-like statistics as a late, non-identifying check.

## Candidate adapter contract

Every executable candidate implements:

```python
candidate.spectral_side(test_function)
candidate.geometric_side(test_function)
candidate.archimedean_side(test_function)
candidate.symmetry_report()
candidate.positivity_report()
```

The base interface lives in `rhastra/candidates/base.py`. Literature-only
descriptions are wrapped by `StaticCandidateAdapter`, whose numerical methods
raise `NotImplementedError` rather than pretending descriptive evidence is an
executable derivation.

## Calibration benchmark

`rhastra.explicit_formula` implements the Weil explicit-formula regression for

    f_sigma(x) = x^(-1/2) exp(-(log x)^2/(2 sigma^2)).

Its spectral side intentionally uses known zeta zeros from `mpmath`. Results are
therefore labeled `calibration-from-known-zeta-zeros` and are never admissible
as independent candidate evidence.

## Install and test

```bash
python -m pip install -e ".[dev]"
pytest
```

Legacy top-level scripts remain for exploratory use while functionality migrates
into the `rhastra` package.

## Current milestones

See [ROADMAP.md](ROADMAP.md). Milestone 2 establishes the executable candidate
boundary; Milestone 3 will define a constrained mutation grammar over candidate
geometry, dynamics, domains, measures, cocycles, and archimedean structure.
