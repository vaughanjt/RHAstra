#!/usr/bin/env python3
"""Numerical benchmark of Weil's explicit formula in the form quoted by Bombieri.

Choose
    f_sigma(x) = x^(-1/2) exp(-(log x)^2 / (2 sigma^2))

Then
    f~_sigma(s) = sqrt(2*pi) sigma exp((sigma^2/2)(s-1/2)^2).

This program uses known critical-line zeros returned by mpmath as numerical data.
It is a regression benchmark, NOT a proof of RH.
"""
import mpmath as mp
mp.mp.dps = 40

def f(x, sigma):
    x = mp.mpf(x)
    u = mp.log(x)
    return x**(-mp.mpf("0.5")) * mp.e**(-(u*u)/(2*sigma*sigma))

def mellin(s, sigma):
    return mp.sqrt(2*mp.pi) * sigma * mp.e**(
        (sigma*sigma/2) * (s-mp.mpf("0.5"))**2
    )

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n+1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n-p*p)//p)+1)
    return [i for i, v in enumerate(sieve) if v]

def spectral_side(sigma, zero_count=100):
    zsum = mp.mpf("0")
    for k in range(1, zero_count+1):
        rho = mp.zetazero(k)
        zsum += 2 * mp.re(mellin(rho, sigma))
    return mellin(0, sigma) - zsum + mellin(1, sigma), zsum

def prime_power_side(sigma, nmax=100000):
    total = mp.mpf("0")
    for p in primes_upto(nmax):
        q = p
        while q <= nmax:
            total += 2 * mp.log(p) * f(q, sigma)
            q *= p
    return total

def archimedean_side(sigma):
    local_constant = (mp.log(4*mp.pi) + mp.euler) * f(1, sigma)
    def integrand(u):
        if abs(u) < mp.mpf("1e-20"):
            return mp.mpf("0.5")
        return (mp.e**(u/2-u*u/(2*sigma*sigma)) - 1) / mp.sinh(u)
    integral = mp.quad(integrand, [0, .01, .1, 1, 5, 20, mp.inf])
    return local_constant + integral, local_constant, integral

def check(sigma, zero_count=100, nmax=100000):
    sigma = mp.mpf(str(sigma))
    lhs, zsum = spectral_side(sigma, zero_count)
    finite = prime_power_side(sigma, nmax)
    arch, const, integ = archimedean_side(sigma)
    rhs = finite + arch
    return {
        "sigma": sigma,
        "spectral_side": lhs,
        "zero_sum": zsum,
        "prime_power_sum": finite,
        "archimedean_constant": const,
        "archimedean_integral": integ,
        "arithmetic_side": rhs,
        "residual": lhs-rhs,
    }

if __name__ == "__main__":
    print("Weil explicit-formula regression benchmark")
    print("(Known zeros are numerical input; this is not an RH proof.)\n")
    for sigma in [0.15, 0.20, 0.25, 0.30, 0.40]:
        r = check(sigma)
        print(f"sigma = {float(r['sigma']):.2f}")
        print(f"  spectral side     {mp.nstr(r['spectral_side'], 18)}")
        print(f"  arithmetic side   {mp.nstr(r['arithmetic_side'], 18)}")
        print(f"  residual          {mp.nstr(r['residual'], 8)}")
        print(f"  zero contribution {mp.nstr(r['zero_sum'], 10)}")
        print(f"  prime powers      {mp.nstr(r['prime_power_sum'], 10)}")
        print()
