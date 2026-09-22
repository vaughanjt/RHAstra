# Odd Weil normalization audit — 2026-09-22

Status: source identification and algebraic derivations, with numerical regression
checks. No RH proof. This supersedes the normalization uncertainty in the first
reconstruction; the legacy coefficient values are unchanged.

## Source and convention

Connes, Consani **and Moscovici**, [Zeta Spectral Triples, v1](https://arxiv.org/html/2511.22755v1),
Sections 2–4, supplies the relevant conventions. The executable matrix agrees
with its integral formula (4.4) and sine integral (4.5). Propositions 3.3–3.4
and Theorem 3.6 provide the closed-form/core and discrete-spectrum results used
below. These are attributed literature results, not new RHAstra proofs.

Write L=log(lambda_squared)>0. Use the zero-extended orthonormal functions

\[
 U_n(x)=L^{-1/2}e^{2\pi inx/L},\qquad 0\le x\le L.
\]

For 0<=y<=L define the symmetrized correlation

\[
 \omega_{nm}(y)=(U_n^**U_m)(y)+(U_n^**U_m)(-y).
\]

Direct integration over the overlap [y,L] gives

\[
 \omega_{nn}(y)=2(1-y/L)\cos(2\pi ny/L),\qquad
 \omega_{nm}(y)=\frac{\sin(2\pi my/L)-\sin(2\pi ny/L)}{\pi(n-m)}.
\]

The second formula is for n!=m. Both vanish outside [-L,L];
\(\omega_{nm}(0)=2\delta_{nm}\). The triangular factor is the length of
an overlap of two intervals. It cannot be discarded while keeping this basis.

## Resolve the tail exactly

Let C0=EulerGamma+log(4*pi). The real-place functional on this correlation is

\[
 A(\omega)=\frac{C_0}{2}\omega(0)+
 \int_0^\infty\frac{e^{y/2}\omega(y)-\omega(0)}{e^y-e^{-y}}\,dy.
\]

Splitting at L and substituting t=e^{-y} in the tail yields

\[
 \int_L^\infty\frac{dy}{e^y-e^{-y}}
 =\operatorname{atanh}(e^{-L})
 =\frac12\log\frac{e^L+1}{e^L-1}.
\]

Consequently the finite-interval constant is

\[
 C(L)=C_0+\log\frac{e^L-1}{e^L+1}.
\]

Thus `LegacyWeilCoefficients.wr_diag` has the correct normalization for these
correlations. The later legacy TeX expression is wrong in two separate ways:
it omits (1-y/L), and it uses C(L) together with the infinite tail, subtracting
that tail a second time. In an infinite-interval expression use C0; in the
finite-interval expression use C(L). In both, retain the triangular factor.

The off-diagonal follows from the same functional, with

\[
 \alpha_L(n)=\frac1\pi\int_0^L
 \frac{e^{y/2}\sin(2\pi ny/L)}{e^y-e^{-y}}\,dy.
\]

Adding the finite prime-power functional gives precisely the implemented
\(a_n,B_n\). No zero locations enter these computations.

## A legitimate continuum representation

Define a unitary map onto the reflection-odd subspace of L2[0,L]:

\[
 (\mathcal U c)(x)=\sum_{n\ge1}c_n\frac{U_n(x)-U_{-n}(x)}{\sqrt2}
 =i\sqrt{2/L}\sum_{n\ge1}c_n\sin(2\pi nx/L).
\]

Reflection here is x -> L-x. This is **not** onto all of L2[0,L]. Parseval
establishes unitarity onto that subspace. The multiplicative coordinate is
u=exp(x)/lambda, with measure du/u=dx. The coefficient matrix K is the odd
restriction of the arithmetic form M=W_R+sum W_p in this representation.
This repairs Session 82 by a basis transform, not by continuing n to a position.
It does not justify Session 82's proposed pointwise Cauchy integral kernel.

The cited closed Weil form Q has trigonometric polynomials as a form core.
Reflection preserves it. Projecting the core by (I-R)/2 gives an odd form core.
The pole form P is bounded and finite rank at fixed L, and M=P-Q. Therefore
-K=Q_odd-P_odd is a lower-semibounded closable form on c00. Its closure defines
a canonical self-adjoint realization of K, upper bounded with compact resolvent,
by bounded perturbation of the cited operator. This is a transfer of the
literature theorem through the identified unitary map. It does not assert
essential self-adjointness of the minimal matrix operator on c00.

A form-domain description, with f=Uc zero extended and unitary Fourier
transform F, is

\[
 \mathcal D=\left\{c\in\ell^2:
 \int_{\mathbb R}\log(2+|t|)|\mathcal F f(t)|^2dt<\infty\right\}.
\]

The associated operator domain is the set of c in this form domain for which
the closed form d -> k(d,c) is represented by an ell2 vector. No equality of
the operator domain with the form domain is asserted. Fixed-L compact
resolvent says nothing by itself about uniform estimates as L grows.

## The odd pole term does not vanish

This additional correction follows directly by integrating the pole functional
\(P_{nm}=\int_0^L2\cosh(y/2)\omega_{nm}(y)dy\), or projecting the legacy
rank-two matrix. Put

\[
 A_L=32L\sinh^2(L/4),\qquad d_j=L^2+16\pi^2j^2.
\]

Its odd block is

\[
 P^-_{jk}=-\frac{32\pi^2 A_L jk}{d_jd_k}=-v_jv_k,
 \qquad v_j=\sqrt{32\pi^2 A_L}\,\frac{j}{d_j}.
\]

Since v_j=O_L(1/j), v belongs to ell2. Hence the actual odd Weil form is

\[
 \boxed{Q^-=-K-vv^*.}
\]

The correct positivity target is

\[
 \boxed{-k(c,c)\ge|\langle v,c\rangle|^2\quad(c\in\mathcal D).}
\]

K<=0 is necessary but not sufficient. A one-dimensional example K=-1,
v=2 gives -K-vv*=-3. On v-perp the pole term vanishes, but not on the whole
odd subspace. The legacy manuscript's identification M_odd=-sigma^- therefore
needs this correction whenever sigma^- denotes the full odd Weil form.
Even satisfying this odd inequality would leave the even sector and the
all-cutoff criterion to address.

## What this settles and what remains

- Normalization: resolved for the stated correlation basis.
- Continuum representation: explicitly derived, onto the odd subspace.
- Closability/canonical realization: supported by the cited closed-form theorem
  and bounded perturbation, recorded as `published-claim` in the adapter.
- Negativity and the stronger rank-one domination: still conjectural.
- Uniform coefficient asymptotics and quantitative tail bounds: still open.

The next research target is rank-one domination for each cutoff, with controlled
finite-section errors. This audit does not infer it from small eigenvalues.
Numerical checks here are ordinary high-precision regressions, not interval
certificates of a global inequality.

At lambda_squared=20, N=3, 45-digit arithmetic gives

| Quantity | Numerical value |
|---|---:|
| largest eigenvalue of K | -1.08381894783578644235919e-6 |
| smallest eigenvalue of Q_odd | 2.680923428312066536381183e-11 |
| squared norm of truncated v | 1.02125375963373024533571 |

The smaller positive margin belongs to the actual odd Weil form. Neither
finite result proves a sign for larger sections or for other cutoffs.

For the subsequent structural direction, see [the translation-gradient model](odd_weil_structural_model.md). It constructs an independent positive energy and identifies exactly which mass and moment terms remain to be dominated.
