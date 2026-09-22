# Candidate: odd Weil coefficient operator

## Status

**OPEN. Not a proof of RH.**

This candidate is reconstructed from the Cauchy--Loewner matrix experiments in
`vaughanjt/RiemannHypothesisProof`, especially Sessions 59 and 82.

The reconstruction corrects a conceptual jump in Session 82.

## 1. What the finite data actually give us

For fixed (lambda), let (L=log(lambda^2)).  The full finite matrices have
Cauchy--Loewner structure

[
M_{nm}=a_ndelta_{nm}+rac{B_m-B_n}{n-m},qquad n
e m,
]

with parity

[
a_{-n}=a_n,qquad B_{-n}=-B_n.
]

Projecting to the normalized odd basis

[
e_n^-=rac{e_n-e_{-n}}{sqrt 2},qquad nge1,
]

gives the exact coefficient kernel

[
K_{jj}=a_j+rac{B_j}{j},
]

and, for (j
e k),

[
oxed{
K_{jk}=
rac{2(jB_k-kB_j)}{j^2-k^2}.
}
]

This formula is algebraic.  It does not use known zeta-zero locations.

For fixed (lambda), the coefficients (a_n,B_n) are defined for every
positive integer (n).  Therefore the immediately justified infinite object is
the quadratic form

[
q(c)=sum_{j,kge1}overline{c_j}K_{jk}c_k
]

on

[
c_{00}(mathbb N)subsetell^2(mathbb N).
]

Every finite odd matrix is an exact compression of this coefficient kernel.

## 2. Correction to the old Session 82 continuum lift

Session 82 wrote an operator on (L^2[0,L]),

[
(Kf)(x)=a(x)f(x)+int_0^L
rac{B(y)-B(x)}{x-y}f(y),dy,
]

after replacing the integer Fourier index (n) by a real variable (x).

That continuation is **not yet a derivation of a continuum operator**.

The same variable was being used in two incompatible roles:

1. (n) is a Fourier-mode / coefficient index in the original matrix;
2. (x) was then interpreted as a physical coordinate in (L^2[0,L]).

A legitimate (L^2) representation may exist, but it must be obtained from a
specified unitary transform or from an independent operator construction.
Analytic continuation of the matrix index alone does not establish it.

RHAstra therefore takes

[
oxed{ell^2(mathbb N)}
]

as the natural first Hilbert space and treats a continuum representation as an
open problem.

## 3. Current operator status

What is established in RHAstra:

- the coefficient kernel is real symmetric;
- the quadratic form is well-defined on finitely supported sequences;
- the finite sections are exact compressions;
- the odd parity reduction formula is exact;
- the arithmetic coefficients can be generated without zeta-zero input.

What is **not** established:

- closability of the quadratic form;
- existence/uniqueness of a self-adjoint realization;
- its precise operator domain;
- essential spectrum;
- compactness or relative compactness of any decomposition;
- equivalence with a Connes scaling-site operator;
- a unitary (L^2) continuum representation;
- (Kle0) on the closure/domain.

These are explicit proof obligations.

## 4. Archimedean normalization discrepancy found during reconstruction

The old repository contains two different formulas for the archimedean
diagonal.

The executable `connes_crossterm.py` used

[
C(L)+int_0^L
rac{
e^{x/2},2(1-x/L)cos(2pi n x/L)-2
}{
e^x-e^{-x}
},dx.
]

The later `docs/lorentzian_weil_conjecture.tex` draft states a different
integral, extending to infinity and omitting the ((1-x/L)) factor in the
finite interval term.

These are not algebraically identical.

The current class `LegacyWeilCoefficients` intentionally implements the
**executable-code normalization**, because that normalization generated the
legacy numerical experiments.  This choice is provenance, not endorsement.

Before theorem-level work, we must return to the underlying Connes--Consani /
Weil test-function derivation and establish the correct formula from source.

## 5. Why this candidate is still interesting

The finite odd sections show an extremely small upper spectral margin in the
legacy computations.  At the small regression point (lambda^2=20,N=3),
RHAstra obtains a largest eigenvalue near

[
-1.08	imes10^{-6}.
]

The point of retaining this number is not to advertise numerical evidence.  It
is a **sensitivity test**: any proposed analytic inequality that loses several
orders of magnitude cannot settle the sign.

The candidate also has an attractive structural feature: the prime information
enters through (a_n) and (B_n), while the parity projection forces a highly
structured Cauchy--Loewner kernel.  That is exactly the kind of constrained
operator family RHAstra is designed to examine.

## 6. Next proof obligations

### O1. Fix the normalization from first principles

Derive (a_n) and (B_n) directly from a named explicit-formula test function,
with no reliance on legacy code.

### O2. Establish coefficient asymptotics

Obtain rigorous bounds for

[
a_n,quad B_n,quad K_{jk}
]

as (j,k	oinfty), uniformly in the relevant (lambda) range.

This determines whether the form is closable and what natural domain to try.

### O3. Closability

Prove or disprove that (q) is closable on (c_{00}subsetell^2).

### O4. Self-adjoint realization

If closable, identify the associated operator and its domain.  Do not infer
self-adjointness from finite symmetric matrices.

### O5. Positivity/negativity mechanism

Only after O1--O4 should we attack

[
q(c)le0
]

for all (c) in the form domain.

### O6. Continuum representation

Search for a unitary transform (U) such that

[
UKU^{-1}
]

has a natural geometric or singular-integral realization.  This is where the
“hidden space” question re-enters.

The transform must be derived; it cannot be created by relabeling the mode
index as a coordinate.

## 7. RHAstra principle illustrated

This candidate is useful precisely because the reconstruction **reduced** the
number of claims we are willing to make.

The goal is not to preserve an old narrative.  It is to locate the smallest
mathematically inevitable object and then ask what additional structure is
actually forced.
