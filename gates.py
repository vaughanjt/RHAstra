#!/usr/bin/env python3
"""Cheap rejection gates for Riemann-space candidates.

These are NOT proof tests. They reject obviously incompatible models before
expensive symbolic or formal work.
"""
import json, math, sys
from pathlib import Path

TWO_PI = 2.0 * math.pi

def riemann_von_mangoldt_smooth(T: float) -> float:
    if T <= 0:
        raise ValueError("T must be positive")
    return (T / TWO_PI) * math.log(T / TWO_PI) - T / TWO_PI + 7.0 / 8.0

def prime_sieve(n: int):
    keep = [True] * (n + 1)
    if n >= 0: keep[0] = False
    if n >= 1: keep[1] = False
    for p in range(2, int(n**0.5) + 1):
        if keep[p]:
            keep[p*p:n+1:p] = [False] * (((n - p*p)//p) + 1)
    return [i for i, v in enumerate(keep) if v]

def target_orbits(pmax=100, rmax=4):
    out = []
    for p in prime_sieve(pmax):
        for r in range(1, rmax + 1):
            L = r * math.log(p)
            A = math.log(p) / (p ** (r / 2.0))
            out.append((L, A, p, r))
    return sorted(out)

def compare_orbit_lengths(candidate_lengths, pmax=100, rmax=4, tol=1e-6):
    targets = target_orbits(pmax, rmax)
    tvals = [x[0] for x in targets]
    matched, misses = 0, []
    for x in candidate_lengths:
        d = min(abs(x-t) for t in tvals) if tvals else float("inf")
        if d <= tol:
            matched += 1
        else:
            misses.append((x, d))
    return {
        "candidate_count": len(candidate_lengths),
        "matched": matched,
        "match_fraction": (matched / len(candidate_lengths)) if candidate_lengths else 0.0,
        "misses": misses[:20]
    }

def structural_report(c):
    tf = c.get("trace_formula", {})
    op = c.get("operator", {})
    gen = c.get("generalization", {})
    fields = {
        "operator_canonicality": op.get("canonicality", "unknown"),
        "self_adjointness": op.get("self_adjoint_status", "unknown"),
        "trace_formula": tf.get("status", "missing"),
        "prime_lengths": tf.get("prime_length_status", "missing"),
        "prime_power_weights": tf.get("prime_power_weight_status", "missing"),
        "archimedean_term": tf.get("archimedean_status", "missing"),
        "dirichlet_L_extension": gen.get("dirichlet_L", "unknown"),
        "global_L_extension": gen.get("global_L_functions", "unknown"),
    }
    return {"id": c["id"], "name": c.get("name"), "fields": fields}

def main(path):
    data = json.loads(Path(path).read_text())
    print("Structural diagnostics (NOT rankings or probabilities):\n")
    for r in [structural_report(c) for c in data]:
        print(r["name"])
        for k, v in r["fields"].items():
            print(f"  {k:24s} {v}")
        print()

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "candidate_examples.json")
