# A translation-gradient space behind the odd Weil matrix

Status: algebraically derived model, checked by independent integral regressions.
The desired contraction is unproved. No claim of a new RH proof or a new
literature result is made. This follows the normalization audit and changes the
research emphasis from entrywise bounds to a structural norm comparison.

## 1. Construct the space before asking for positivity

Set L=log(lambda_squared), extend f in L2[0,L] by zero to the real line, and
restrict to f(L-x)=-f(x). Let tau_y f(x)=f(x-y). Define

\[
 \rho(y)=\frac{e^{y/2}}{e^y-e^{-y}},\quad
 w_q=\frac{\Lambda(q)}{\sqrt q},\quad y_q=\log q,
 \qquad 1<q\le e^L.
\]

Only prime powers have nonzero w_q. Consider the independently specified space

\[
 \mathcal G_L=L^2((0,\infty)\times\mathbb R,\rho(y)dy\,dx)
 \ \oplus\!\!\bigoplus_{1<q\le e^L,\ \Lambda(q)>0}L^2(\mathbb R,dx).
\]

Define the translation-gradient map

\[
 Tf=\left((\tau_y-I)f,\ \{\sqrt{w_q}(\tau_{y_q}-I)f\}_q\right).
\]

Its squared norm is the nonnegative energy

\[
 D_L[f]=\int_0^\infty\rho(y)\|\tau_y f-f\|_2^2dy
       +\sum_q w_q\|\tau_{y_q}f-f\|_2^2.
\]

The map is unbounded with domain consisting of functions of finite energy;
finite odd Fourier sums belong to it. We do not assert it is defined on every
L2 function. Full-line translation and zero extension are essential: periodic
translation would produce a different form.

This construction uses only ordinary translations and positive weights, not
zeta zeros or a square root of a matrix whose positivity is in question.
It is the energy of a symmetric nonlocal jump operator restricted by zero
extension to a finite interval. The continuous part has logarithmic high
frequency growth. In multiplicative coordinates the jumps become dilations.

## 2. Derive the mass subtraction

Let a_f(y)=Re<f,tau_y f>. Then

\[
 \|\tau_yf-f\|^2=2\|f\|^2-2a_f(y).
\]

Substitute this into the real-place functional fixed in the audit. The finite
constant that remains is

\[
 b_\infty=\gamma+\log(4\pi)+
 \int_0^\infty\frac{e^{y/2}-1}{\sinh y}\,dy
 =\log\pi-\psi(1/4)>0.
\]

The integral is finite at zero and infinity. For a prime-power contribution,
\(-2w_q a_f(y_q)=w_q\|\tau_{y_q}f-f\|^2-2w_q\|f\|^2\).
Therefore, with

\[
 b_L=b_\infty+2\sum_qw_q,
\]

we get the exact identity, first on finite sums,

\[
 \boxed{-K[f]=D_L[f]-b_L\|f\|^2.}
\]

This is a positive energy **with a subtracted mass**. Positivity of D_L does not
imply positivity of -K. Nor does compact resolvent imply the required lower
bound. For y>=L the supports do not overlap, giving
\(D_L[f]\ge2\|f\|^2\int_L^\infty\rho(y)dy>0\) for nonzero f. Thus D_L itself
is coercive at each fixed L, independently of RH; this crude bound does not
establish the needed mass threshold.

## 3. Identify the pole as a concrete moment

Use the odd Fourier unitary from the audit. Define

\[
 \ell_L(f)=\sqrt2\int_0^L f(x)\sinh((x-L/2)/2)\,dx.
\]

For f=Uc, direct integration gives \(\ell_L(f)=-i\,v^Tc\), with v as in the
audit. Hence

\[
 \boxed{Q^-[f]=\|Tf\|_{\mathcal G_L}^2
          -b_L\|f\|_2^2-|\ell_L(f)|^2.}
\]

Define \(Bf=(\sqrt{b_L}f,\ell_L(f))\) in L2[0,L] direct sum C. The precise
structural problem is now:

> Does B extend as a contraction from the completion of the odd test functions
> in the independently defined T-energy norm?

The answer is equivalent to the desired odd Weil inequality, not a proof of
it. The value of this formulation is that both spaces and maps have explicit
arithmetic definitions before any positivity assumption. Defining T instead
as the square root of -K would not provide that independence.

## 4. What the numerical experiment is allowed to tell us

`translation_energy.py` computes the gradient entries by direct quadrature.
Tests compare those entries against -K+b_L I and check the pole moment by a
separate real-space integral. This checks the model, not its global sign.

The probe additionally solves A_N c=v_N, A_N=-K_N, **only after checking numerical
positive definiteness**, then normalizes c in ell2. This is the finite maximizer
of the pole-to-A-energy ratio. It is not used to construct the gradient space.
The probe records separately D energy, mass, pole energy, the remaining gap,
and alignment with the lowest Q eigenvector. No root finding or known-zero
input is used. Reported precision is working precision, not an error certificate.

A small gap is not evidence of a hidden contraction by itself. A candidate
mechanism should predict these directions or explain the cancellation without
fitting them. In particular, the pole extremizer and the lowest-Q mode optimize
different quotients; numerical overlap cannot identify an infinite-limit state.

## 5. The geometrically motivated projection route

Connes and Consani's [archimedean study](https://arxiv.org/pdf/2006.13771),
Theorem 1, constructs a positive trace using the Sonin projection. Its space
consists of even functions on the real line whose functions and Fourier
transforms vanish on a central interval. The theorem has specific support and
transform-vanishing conditions; it is not an all-prime proof.

In our centered logarithmic coordinate, oddness forces the transform value at
zero to vanish. Imposing ell_L(f)=0 also kills both pole evaluations. This
makes the pole-neutral odd subspace a natural comparison space for that route.
The small-support theorem still requires its actual support and smoothness
hypotheses; no extension to all cutoffs is asserted here. Our odd log-coordinate
space is not the even real-coordinate Sonin space: an intertwining map must be
constructed, not presumed from the parity names.

The [later spectral-triple paper](https://arxiv.org/html/2511.22755v1),
Section 8, identifies missing convergence/ground-state steps in its own program.
We must not treat its finite spectral construction as a completed norm
factorization for this form.

## 6. Concrete next structural question

Seek a prime-compatible dilation representation and a projection for which
Q^- is a positive trace/norm, or is bounded below by one with a controlled
remainder. Start on the pole-neutral odd subspace, and explicitly retain the
additional obligation of recovering the omitted pole direction.

Every proposed mechanism must specify:

1. The Hilbert space, measure, action, and operator domains independently of Q.
2. How every prime-power shift and the archimedean density arise.
3. The exact correction between its positive norm/trace and our Q^-.
4. Why that correction has the required sign, or a counterexample rejecting it.

No such projection/intertwiner has been established in this work. The gradient
model is an exact structural baseline for testing one. It avoids presenting a
renamed positivity inequality as a solution.

## 7. Finite probe results

| cutoff | N | 1-r_N | smallest Q eigenvalue |
|---:|---:|---:|---:|
| 2 | 3 | 9.15246e-01 | 1.12872e-01 |
| 2 | 6 | 8.96482e-01 | 9.64593e-02 |
| 2 | 10 | 8.85240e-01 | 8.83245e-02 |
| 20 | 3 | 1.27536e-10 | 2.68092e-11 |
| 20 | 6 | 2.45646e-17 | 2.46053e-18 |
| 20 | 10 | 1.01769e-25 | 6.70954e-27 |
| 50 | 3 | 8.78355e-12 | 4.01832e-12 |
| 50 | 6 | 1.53686e-20 | 3.03608e-21 |
| 50 | 10 | 1.42189e-30 | 1.63614e-31 |

At cutoffs 20 and 50, the pole extremizers closely align with the lowest-Q modes (squared overlaps above 0.99999999 at the sampled sizes). The pole-neutral projection norms increase over these samples; this does not establish a limiting vector or an exact null direction.

The hardest reported case, cutoff 50 and N=10, was recomputed at 100 digits. Relative differences from 70 digits were {'one_minus_r': '4.2995639e-40', 'min_Q': '4.2734137e-40'}. This guards against gross cancellation error but is not rigorous certification.

## Follow-up: a cutoff obstruction

The [pole-neutral boundary audit](pole_neutral_boundary_obstruction.md) shows that individual compressed prime shifts do not preserve the pole-neutral subspace. Any proposed projection/intertwiner must retain or control this exact boundary defect.
