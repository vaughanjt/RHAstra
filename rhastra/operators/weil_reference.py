"""Integral reference for the normalization audit (no zeta-zero input).

The legacy coefficients use special functions; this module evaluates the
correlation functional directly. It is intended for modest-mode regression
checks, not certified quadrature at arbitrarily high frequency.
"""
from __future__ import annotations

import mpmath as mp


def correlation(n: int, m: int, y, L):
    """Symmetrized correlation of zero-extended Fourier modes on [0,L]."""
    y = abs(mp.mpf(y))
    if y >= L:
        return mp.mpf(0)
    if n == m:
        return 2 * (1 - y / L) * mp.cos(2 * mp.pi * n * y / L)
    return (mp.sin(2 * mp.pi * m * y / L)
            - mp.sin(2 * mp.pi * n * y / L)) / (mp.pi * (n - m))


def archimedean_entry(n: int, m: int, L):
    """Infinite-tail normalization, with its tail integrated independently."""
    w0 = mp.mpf(2 if n == m else 0)
    # Every omega_nm has right derivative -2/L at zero.
    limit = w0 / 4 - 1 / L

    def integrand(y):
        if y == 0:
            return limit
        # expm1 avoids subtracting the constant term from two exponentials.
        omega = correlation(n, m, y, L)
        return (mp.expm1(y / 2) * omega + omega - w0) / (2 * mp.sinh(y))

    points = [L * k / max(4, 2 * max(abs(n), abs(m)))
              for k in range(max(4, 2 * max(abs(n), abs(m))) + 1)]
    local = mp.quad(integrand, points)
    tail = -w0 * mp.quad(lambda y: 1 / (2 * mp.sinh(y)), [L, mp.inf])
    return (mp.euler + mp.log(4 * mp.pi)) * w0 / 2 + local + tail


def arithmetic_entry(coefficients, n: int, m: int):
    """Direct correlation evaluation of real-place plus prime-power terms."""
    with mp.workdps(coefficients.dps):
        L = coefficients.L
        value = archimedean_entry(n, m, L)
        for _p, _q, weight, y in coefficients.prime_powers():
            value += weight * correlation(n, m, y, L)
        return +value


def odd_pole_vector(L, N: int):
    """Vector v with P_odd=-v v*, in the normalized odd Fourier basis."""
    if N < 1 or L <= 0:
        raise ValueError("L must be positive and N must be >= 1")
    A = 32 * L * mp.sinh(L / 4) ** 2
    return mp.matrix([mp.sqrt(32 * mp.pi**2 * A) * j
                      / (L**2 + 16 * mp.pi**2 * j**2)
                      for j in range(1, N + 1)])


def odd_weil_section(lift, N: int):
    """Full odd Weil section Q_odd=-K-v v*, including the pole term."""
    with mp.workdps(lift.coefficients.dps):
        v = odd_pole_vector(lift.coefficients.L, N)
        return -lift.finite_section(N) - v * v.T
