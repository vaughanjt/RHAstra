"""Reference explicit-formula calculations used as calibration targets.

Known zeta zeros are numerical input here. This module must never be treated as
an independently derived candidate model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import mpmath as mp


@dataclass(frozen=True)
class LogGaussian:
    """f_sigma(x)=x^(-1/2) exp(-(log x)^2/(2 sigma^2))."""

    sigma: mp.mpf | float
    name: str = "log-gaussian"

    def __post_init__(self) -> None:
        sigma = mp.mpf(self.sigma)
        if sigma <= 0:
            raise ValueError("sigma must be positive")
        object.__setattr__(self, "sigma", sigma)

    def value(self, x):
        x = mp.mpf(x)
        if x <= 0:
            raise ValueError("x must be positive")
        u = mp.log(x)
        return x ** (-mp.mpf("0.5")) * mp.e ** (-(u * u) / (2 * self.sigma * self.sigma))

    def transform(self, s):
        return mp.sqrt(2 * mp.pi) * self.sigma * mp.e ** (
            (self.sigma * self.sigma / 2) * (s - mp.mpf("0.5")) ** 2
        )


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i, v in enumerate(sieve) if v]


def spectral_side(test_function: LogGaussian, zero_count: int = 20):
    """Reference spectral side using known critical-line zeros from mpmath."""
    if zero_count < 1:
        raise ValueError("zero_count must be >= 1")
    zsum = mp.mpf("0")
    for k in range(1, zero_count + 1):
        rho = mp.zetazero(k)
        zsum += 2 * mp.re(test_function.transform(rho))
    return (
        test_function.transform(0) - zsum + test_function.transform(1),
        zsum,
    )


def prime_power_side(test_function: LogGaussian, nmax: int = 1000):
    """Finite-prime side for the symmetric log-Gaussian family."""
    if nmax < 2:
        return mp.mpf("0")
    total = mp.mpf("0")
    for p in primes_upto(nmax):
        q = p
        while q <= nmax:
            total += 2 * mp.log(p) * test_function.value(q)
            q *= p
    return total


def archimedean_side(test_function: LogGaussian):
    """Real-place contribution in the Bombieri/Weil normalization used by this project."""
    local_constant = (mp.log(4 * mp.pi) + mp.euler) * test_function.value(1)

    def integrand(u):
        if abs(u) < mp.mpf("1e-20"):
            return mp.mpf("0.5")
        sigma = test_function.sigma
        return (mp.e ** (u / 2 - u * u / (2 * sigma * sigma)) - 1) / mp.sinh(u)

    integral = mp.quad(integrand, [0, mp.mpf(".01"), mp.mpf(".1"), 1, 5, 20, mp.inf])
    return local_constant + integral, local_constant, integral


def regression(test_function: LogGaussian, *, zero_count: int = 20, nmax: int = 1000):
    spectral, zsum = spectral_side(test_function, zero_count=zero_count)
    finite = prime_power_side(test_function, nmax=nmax)
    arch, constant, integral = archimedean_side(test_function)
    arithmetic = finite + arch
    return {
        "spectral_side": spectral,
        "zero_sum": zsum,
        "prime_power_sum": finite,
        "archimedean_constant": constant,
        "archimedean_integral": integral,
        "arithmetic_side": arithmetic,
        "residual": spectral - arithmetic,
        "provenance": "calibration-from-known-zeta-zeros",
    }
