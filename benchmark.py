#!/usr/bin/env python3
"""Benchmark known zeta targets. Requires mpmath.

This establishes the target side of the inverse problem; it does not test RH.
"""
import mpmath as mp

mp.mp.dps = 40

def Nbar(T):
    T = mp.mpf(T)
    return T/(2*mp.pi)*mp.log(T/(2*mp.pi)) - T/(2*mp.pi) + mp.mpf(7)/8

def first_zeros(n=20):
    return [mp.im(mp.zetazero(k)) for k in range(1, n+1)]

def normalized_gaps(gammas):
    """Crude local unfolding using mean density log(T/2π)/(2π)."""
    out = []
    for a, b in zip(gammas, gammas[1:]):
        mid = (a+b)/2
        rho_bar = mp.log(mid/(2*mp.pi))/(2*mp.pi)
        out.append((b-a)*rho_bar)
    return out

if __name__ == "__main__":
    zs = first_zeros(25)
    print("First 10 imaginary parts of nontrivial zeta zeros:")
    for i, z in enumerate(zs[:10], 1):
        print(f"{i:2d}  {float(z):.12f}")

    T = zs[-1]
    print("\nAt T =", float(T))
    print("actual zero count =", len(zs))
    print("smooth Nbar(T)    =", float(Nbar(T)))
    print("residual          =", float(len(zs)-Nbar(T)))

    gaps = normalized_gaps(zs)
    print("\nFirst 10 crudely unfolded gaps:")
    print(" ".join(f"{float(x):.4f}" for x in gaps[:10]))
