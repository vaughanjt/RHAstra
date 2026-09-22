"""Discrete odd-parity lift of the legacy Weil matrix.

The legacy project informally promoted the finite odd matrices to an integral
operator on L^2[0,L]. That step was not derived: the Fourier mode index was
continued to a real variable and then interpreted as physical position.

The mathematically immediate lift is instead coefficient-space based. For fixed
lambda, the matrix coefficients define a symmetric quadratic form on c_00(N),
a dense subspace of ell^2(N). Finite matrices are exact compressions of this
formal infinite matrix.

The canonical form realization is identified by a literature theorem; see
docs/candidates/odd_weil_normalization_audit.md. No RH claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math
from typing import Sequence

import mpmath as mp

from rhastra.candidates.base import EvidenceStatus
from .base import OperatorDomainReport


def _primes_upto(n: int) -> tuple[int, ...]:
    if n < 2:
        return ()
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return tuple(i for i, value in enumerate(sieve) if value)


def odd_block_from_sequences(
    a_positive: Sequence[complex | float | mp.mpf],
    b_positive: Sequence[complex | float | mp.mpf],
) -> mp.matrix:
    """Return the odd block implied by even a_n and odd B_n.

    The parent Cauchy--Loewner matrix is

        M_nm = a_n delta_nm + (B_m - B_n)/(n-m),  n != m,

    with a_{-n}=a_n and B_{-n}=-B_n. In the normalized odd basis
    (e_n-e_-n)/sqrt(2), n>=1,

        K_jj = a_j + B_j/j
        K_jk = 2 (j B_k - k B_j)/(j^2-k^2),  j != k.
    """
    if len(a_positive) != len(b_positive):
        raise ValueError("a_positive and b_positive must have the same length")
    N = len(a_positive)
    out = mp.matrix(N)
    for j0 in range(N):
        j = j0 + 1
        aj = a_positive[j0]
        bj = b_positive[j0]
        for k0 in range(N):
            k = k0 + 1
            bk = b_positive[k0]
            if j == k:
                out[j0, k0] = aj + bj / j
            else:
                out[j0, k0] = 2 * (j * bk - k * bj) / (j * j - k * k)
    return out


def full_cauchy_loewner_from_parity(
    a_nonnegative: Sequence[complex | float | mp.mpf],
    b_positive: Sequence[complex | float | mp.mpf],
) -> mp.matrix:
    """Build indices -N..N from a_0..a_N and B_1..B_N using parity."""
    N = len(b_positive)
    if len(a_nonnegative) != N + 1:
        raise ValueError("a_nonnegative must contain a_0 through a_N")

    def aval(n: int):
        return a_nonnegative[abs(n)]

    def bval(n: int):
        if n == 0:
            return mp.mpf("0")
        value = b_positive[abs(n) - 1]
        return value if n > 0 else -value

    indices = tuple(range(-N, N + 1))
    out = mp.matrix(2 * N + 1)
    for i, n in enumerate(indices):
        for j, m in enumerate(indices):
            if n == m:
                out[i, j] = aval(n)
            else:
                out[i, j] = (bval(m) - bval(n)) / (n - m)
    return out


def project_odd_block(full_matrix: mp.matrix) -> mp.matrix:
    """Project a parity-symmetric (-N..N)-indexed matrix to the odd subspace."""
    dim = full_matrix.rows
    if full_matrix.cols != dim or dim % 2 != 1:
        raise ValueError("full_matrix must be square with odd dimension 2N+1")
    N = (dim - 1) // 2
    out = mp.matrix(N)
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            out[j - 1, k - 1] = full_matrix[N + j, N + k] - full_matrix[N + j, N - k]
    return out


@dataclass(frozen=True)
class LegacyWeilCoefficients:
    """Coefficients matching the legacy executable and the correlation formula.

    The normalization was checked against Connes--Consani--Moscovici,
    arXiv:2511.22755v1, equation (4.4). The legacy class name is retained for
    compatibility. See docs/candidates/odd_weil_normalization_audit.md.
    """

    lambda_squared: float
    dps: int = 40

    def __post_init__(self) -> None:
        if self.lambda_squared < 2:
            raise ValueError("lambda_squared must be >= 2")
        if self.dps < 20:
            raise ValueError("dps must be >= 20")

    @property
    def L(self) -> mp.mpf:
        with mp.workdps(self.dps):
            return mp.log(self.lambda_squared)

    @lru_cache(maxsize=1)
    def prime_powers(self) -> tuple[tuple[int, int, mp.mpf, mp.mpf], ...]:
        """Return (p, p^k, log(p)/sqrt(p^k), log(p^k)) up to lambda^2."""
        with mp.workdps(self.dps):
            result: list[tuple[int, int, mp.mpf, mp.mpf]] = []
            for p in _primes_upto(int(math.floor(self.lambda_squared))):
                q = p
                while q <= self.lambda_squared:
                    result.append((p, q, mp.log(p) / mp.sqrt(q), mp.log(q)))
                    q *= p
            return tuple(result)

    @lru_cache(maxsize=None)
    def wr_diag(self, n: int) -> mp.mpf:
        """Legacy-code archimedean diagonal for |n|."""
        n = abs(int(n))
        with mp.workdps(self.dps):
            L = mp.log(self.lambda_squared)
            eL = mp.e**L
            constant = mp.euler + mp.log(4 * mp.pi * (eL - 1) / (eL + 1))
            zero_limit = mp.mpf("0.5") - 1 / L

            def integrand(x):
                if abs(x) < mp.mpf(10) ** (-(self.dps // 2)):
                    return zero_limit
                omega = 2 * (1 - x / L) * mp.cos(2 * mp.pi * n * x / L)
                return (mp.e ** (x / 2) * omega - 2) / (mp.e**x - mp.e**(-x))

            return constant + mp.quad(integrand, [0, L])

    @lru_cache(maxsize=None)
    def alpha(self, n: int) -> mp.mpf:
        """Legacy alpha_L(n), an odd function of n."""
        n = int(n)
        if n == 0:
            return mp.mpf("0")
        with mp.workdps(self.dps):
            L = mp.log(self.lambda_squared)
            nn = abs(n)
            z = mp.e ** (-2 * L)
            a = mp.mpf("0.25") + mp.pi * 1j * nn / L
            h = mp.hyp2f1(1, a, a + 1, z)
            f1 = mp.e ** (-L / 2) * mp.im(
                2 * L / (L + 4 * mp.pi * 1j * nn) * h
            )
            d = mp.im(mp.digamma(a)) / 2
            value = (f1 + d) / mp.pi
            return value if n > 0 else -value

    @lru_cache(maxsize=None)
    def coefficient(self, n: int) -> tuple[mp.mpf, mp.mpf]:
        """Return (a_n, B_n) for n>=1 in the legacy computational matrix."""
        n = int(n)
        if n < 1:
            raise ValueError("coefficient index n must be >= 1")
        with mp.workdps(self.dps):
            L = mp.log(self.lambda_squared)
            a_n = self.wr_diag(n)
            b_n = self.alpha(n)
            for _p, _q, weight, y in self.prime_powers():
                phase = 2 * mp.pi * n * y / L
                a_n += weight * 2 * (L - y) / L * mp.cos(phase)
                b_n += weight / mp.pi * mp.sin(phase)
            return +a_n, +b_n

    def positive_sequences(self, N: int) -> tuple[tuple[mp.mpf, ...], tuple[mp.mpf, ...]]:
        if N < 1:
            raise ValueError("N must be >= 1")
        pairs = tuple(self.coefficient(n) for n in range(1, N + 1))
        return tuple(x[0] for x in pairs), tuple(x[1] for x in pairs)


@dataclass(frozen=True)
class OddWeilOperatorLift:
    """Formal odd-parity operator on c_00 subset ell^2(N).

    This object provides coefficient formulas and finite compressions. The canonical
    form realization uses the literature result identified in the audit note.
    """

    coefficients: LegacyWeilCoefficients

    def entry(self, j: int, k: int) -> mp.mpf:
        if j < 1 or k < 1:
            raise ValueError("indices must be positive integers")
        aj, bj = self.coefficients.coefficient(j)
        _ak, bk = self.coefficients.coefficient(k)
        if j == k:
            return aj + bj / j
        return 2 * (j * bk - k * bj) / (j * j - k * k)

    def finite_section(self, N: int) -> mp.matrix:
        a, b = self.coefficients.positive_sequences(N)
        return odd_block_from_sequences(a, b)

    def quadratic_form(self, coefficients: Sequence[complex | float | mp.mpf]):
        """Quadratic form on a finitely supported coefficient vector."""
        if not coefficients:
            raise ValueError("coefficients must be non-empty")
        M = self.finite_section(len(coefficients))
        v = mp.matrix(coefficients)
        return (v.T.conjugate() * M * v)[0]

    def domain_report(self) -> OperatorDomainReport:
        return OperatorDomainReport(
            hilbert_space="ell^2(N_{>=1})",
            dense_core="c_00(N_{>=1}) (finitely supported sequences)",
            symmetry_status=EvidenceStatus.DERIVED,
            closability_status=EvidenceStatus.PUBLISHED_CLAIM,
            self_adjointness_status=EvidenceStatus.PUBLISHED_CLAIM,
            continuum_representation_status=EvidenceStatus.DERIVED,
            notes=(
                "Normalization and odd Fourier unitary map are identified in the audit. "
                "Canonical form realization follows by bounded perturbation of "
                "CCM arXiv:2511.22755v1 Props. 3.3-3.4 and Theorem 3.6. "
                "Minimal-operator essential self-adjointness is not claimed."
            ),
        )
