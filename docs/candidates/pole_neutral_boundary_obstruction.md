# Why the pole-neutral subspace is not preserved by compressed prime shifts

Status: exact boundary identity derived below; direct integral regression and a
numerical witness. This rules out a particular shortcut, not all possible
projection or intertwining constructions. No additional compute is required
for the obstruction.

## The tempting shortcut

The structural model suggests starting with odd functions f on I=[0,L] such
that ell(f)=0. On that subspace the negative pole term disappears. A tempting
next step is to regard this as an invariant space for the prime-shift action.
That invariance is false after the support cutoff.

Let f be zero extended, f(L-x)=-f(x), and let

\[
 h(x)=\sinh((x-L/2)/2),\qquad
 \ell(f)=\sqrt2\int_0^Lh(x)f(x)\,dx.
\]

Write E for zero extension and P_I for restriction/cutoff. The symmetric
compressed translation is

\[
 S_y=P_I(\tau_y+\tau_{-y})E,\qquad 0<y<L.
\]

It is a bounded self-adjoint operator on L2(I), preserves reflection parity,
and is exactly the symmetric shift occurring in the prime correlation term.
The prime contribution to the arithmetic matrix is w_q S_log(q).

## Derive the defect without any matrix truncation

Changing variables separately in the two shifted terms gives

\[
 \ell(S_y f)/\sqrt2=
 \int_0^{L-y}h(t+y)f(t)dt+\int_y^Lh(t-y)f(t)dt.
\]

Since h(t+y)+h(t-y)=2 cosh(y/2)h(t), subtract the omitted pieces from the
full-interval integrals. Reflection oddness makes the two omitted integrals
equal. Consequently

\[
 \boxed{\ell(S_y f)=2\cosh(y/2)\ell(f)-\beta_y(f)},
\]

where the exact boundary functional is

\[
 \boxed{\beta_y(f)=2\sqrt2\int_{L-y}^Lh(t+y)f(t)dt.}
\]

Thus ell(f)=0 implies ell(S_y f)=-beta_y(f), not zero in general. This is a
physical-space identity for the shifted function itself; no finite Fourier
compression has been made.

## An analytic failure of invariance

For 0<y<L/2, choose a smooth odd function g supported in the interior
(y,L-y) with ell(g)!=0. Then beta_y(g)=0. Choose a smooth odd function f
supported near the endpoints with beta_y(f)!=0. The function

\[
 f_0=f-\frac{\ell(f)}{\ell(g)}g
\]

has ell(f_0)=0 but beta_y(f_0)=beta_y(f)!=0. Such functions can be constructed
from paired reflected bumps away from the midpoint and endpoints. This proves
that ker(ell) is not invariant under S_y in that range. In particular y=log 2,
L=log 20 satisfies the range condition.

Since S_y is self-adjoint, its orthogonal projection onto ker(ell) cannot
commute with S_y. Inserting that projection therefore changes the prime action;
it is not simply a restriction of the existing arithmetic operator.

This argument does **not** prove that the complete weighted sum, including the
archimedean term, fails to preserve the subspace: cancellations across terms
would require separate analysis. It does prove that preservation cannot be
justified one prime shift at a time by this support-cutoff construction.

## Reproducible witness

In the normalized two-mode odd basis, choose c proportional to (v_2,-v_1),
where v is the pole vector. This ensures exact neutrality symbolically.
`pole_boundary.py` evaluates the initial moment, the moment after the prime-2
shift, and the boundary functional by separate physical-space integrals.
Results at cutoff 20 are in `experiments/pole_boundary_witness.json`.
Tests cover the general identity at three shift lengths as well as this
neutral witness. No zeta zeros, eigenvectors, or fitted geometry are inputs.

## What an enlarged representation must retain

On the full real line, using the same exponential moment and compactly
supported f, symmetric translation obeys the moment identity with no defect.
But it enlarges support beyond I. Its omitted exterior contribution is exactly
beta_y(f). One can therefore retain an exterior boundary channel instead of
silently removing it. This explains the obstruction; it does not assign a
favorable sign to that channel or prove the Weil inequality.

An admissible next construction must do one of the following:

- use a larger dilation representation and retain its cutoff/boundary terms;
- derive a different projection with a justified correction formula;
- prove cancellation or domination of the defect in the complete form.

Merely projecting onto ker(ell), or treating compressed translations as a
unitary group, does not meet those requirements. Indeed compressed translations
do not satisfy the full translation group law.

## Connection to the source literature

The introduction and Theorem 1 of
[Connes–Consani, arXiv:2006.13771](https://arxiv.org/pdf/2006.13771)
explicitly distinguish a positive compressed trace from an invariant scaling
subspace. Their Sonin construction does not require the scaling action to
preserve the Sonin space; the comparison with the Weil distribution carries
additional work and hypotheses. Our boundary calculation is consistent with
that distinction, not a refutation of their method.

The next structural task is therefore a cutoff-correction identity in the
larger representation. The missing sign cannot be supplied by more numerical
precision alone.
