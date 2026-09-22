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

1. A candidate receives credit only for structure that is **generated naturally**
   by the space/dynamics.
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

Every executable trace candidate implements:

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

## First operator candidate

RHAstra reconstructs the legacy odd Weil / Cauchy--Loewner kernel on
`c_00(N) ⊂ ell^2(N)`, with exact finite compressions.

The [normalization audit](docs/candidates/odd_weil_normalization_audit.md)
identifies its correlation test function and unitary Fourier representation.
The canonical self-adjoint form realization is attributed to an existing
literature theorem and a bounded-perturbation transfer (`published-claim`).
The old index-as-position continuum construction is not used.

The actual odd Weil positivity target includes a negative rank-one pole term:
`Q_odd = -K - v v*`. Proving `K <= 0` alone is insufficient. Positivity remains
conjectural; no operator spectrum is identified with the zeta zeros.

See [docs/candidates/odd_weil_operator.md](docs/candidates/odd_weil_operator.md).

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

## Current milestones

See [ROADMAP.md](ROADMAP.md). Milestone 2 establishes the executable candidate
boundary. The operator track is now pursuing the smallest mathematically
inevitable infinite-dimensional lift before any continuum geometry is assumed.
