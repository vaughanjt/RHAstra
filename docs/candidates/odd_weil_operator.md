# Candidate: odd Weil coefficient operator

**OPEN. Not a proof of RH.**

The initial reconstruction corrected the legacy Session 82 substitution of a
continuous position for an integer Fourier index. The subsequent
[normalization audit](odd_weil_normalization_audit.md) resolves the normalization,
identifies an actual unitary representation, and corrects the positivity target.

For fixed L=log(lambda_squared), even a_n and odd B_n give the exact odd kernel

\[
 K_{jj}=a_j+B_j/j,\qquad
 K_{jk}=\frac{2(jB_k-kB_j)}{j^2-k^2}\quad(j\ne k).
\]

It defines a real symmetric form on c00 in ell2; finite sections are exact
compressions. Arithmetic coefficients use no zeta-zero input.

The class name `LegacyWeilCoefficients` is retained for compatibility. Its
executable normalization is now matched to the defining correlation functional.
The later legacy TeX diagonal omitted an overlap factor and double-counted an
archimedean tail; the executable coefficient values do not need to change.

## Evidence status

| Claim | Status |
|---|---|
| Exact parity reduction | Derived algebraically |
| Normalization | Source matched; independent integral regressions |
| Unitary model | Derived onto reflection-odd L2[0,L] |
| Closable form, canonical self-adjoint realization | Literature theorem plus bounded-perturbation transfer; `published-claim` |
| Compact resolvent at each fixed cutoff | Same literature transfer |
| Minimal matrix operator essentially self-adjoint on c00 | Not claimed |
| K non-positive | Conjectural |
| Full odd Weil positivity | Stronger conjectural rank-one domination |
| Uniform cutoff estimates | Open |
| A trace spectrum consisting of zeta-zero ordinates | Not established |

At lambda_squared=20, N=3, the largest eigenvalue of K is approximately
-1.08381895e-6. This is a numerical sensitivity check, not an infinite-dimensional
proof. The full odd Weil matrix differs: Q_odd=-K-vv*, with nonzero v defined in
the audit. Thus K<=0 alone is insufficient.

## Next work

Derive useful uniform coefficient/tail bounds and attack the precise inequality
-k(c,c)>=|<v,c>|^2 on the form domain. The even sector remains a separate
obligation. A legitimate Fourier representation does not validate the old
Session 82 pointwise integral kernel.
