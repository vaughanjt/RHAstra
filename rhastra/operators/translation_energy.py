"""Zero-free translation-gradient model of the odd Weil form.

The positive gradient energy is constructed before asking whether its
subtracted mass and pole terms are dominated. No positive square root of
-K or of the Weil matrix is used to define the model.
"""
import mpmath as mp

from .odd_weil import LegacyWeilCoefficients, OddWeilOperatorLift
from .weil_reference import correlation, odd_pole_vector


def mass_constant(coefficients):
    with mp.workdps(coefficients.dps):
        return (mp.log(mp.pi) - mp.digamma(mp.mpf('0.25'))
                + 2 * sum((w for _, _, w, _ in coefficients.prime_powers()), mp.mpf(0)))


def odd_translation_gram(j, k, y, L):
    """Inner product of (tau_y-I)e_j and (tau_y-I)e_k on the full line."""
    return (2 * int(j == k) - correlation(j, k, y, L)
            + correlation(j, -k, y, L))


def gradient_entry(coefficients, j, k):
    """Independent quadrature of the positive translation-gradient energy."""
    with mp.workdps(coefficients.dps):
        L = coefficients.L
        def integrand(y):
            if y == 0:
                return mp.mpf(0)  # odd modes vanish at both endpoints
            return (mp.exp(-y/2) / (-mp.expm1(-2*y))
                    * odd_translation_gram(j, k, y, L))
        count = max(4, 2 * max(j, k))
        value = mp.quad(integrand, [L*k/count for k in range(count+1)])
        value += 2 * int(j == k) * mp.quad(
            lambda y: mp.exp(-y/2) / (-mp.expm1(-2*y)), [L, mp.inf])
        for _, _, w, y in coefficients.prime_powers():
            value += w * odd_translation_gram(j, k, y, L)
        return +value


def finite_diagnostic(cutoff, N, dps=60):
    """Probe the independently defined gradient model through its exact matrix.

    Numerical evidence only. LU solves avoid an explicit inverse. Positive
    definiteness is checked before reporting an A-energy extremizer.
    """
    if N < 1:
        raise ValueError('N must be positive')
    with mp.workdps(dps):
        coeff = LegacyWeilCoefficients(cutoff, dps)
        A = -OddWeilOperatorLift(coeff).finite_section(N)
        b = mass_constant(coeff)
        D = A + b * mp.eye(N)
        v = odd_pole_vector(coeff.L, N)
        Q = A - v*v.T
        ae, _ = mp.eigsy(A)
        qe, qu = mp.eigsy(Q)
        if ae[0] <= 0:
            raise ValueError('A_N is not numerically positive definite at this precision')
        c = mp.lu_solve(A, v)
        r = (v.T*c)[0]
        c /= mp.norm(c)
        qmode = qu[:, 0]
        # Compare the gap-minimizing direction with the pole extremizer.
        # These optimize different quotients and need not coincide.
        align = abs((qmode.T*c)[0]) ** 2
        energy = (c.T*D*c)[0]
        pole = abs((v.T*c)[0])**2
        vunit = v / mp.norm(v)
        neutral_norm = mp.sqrt(max(mp.mpf(0), 1-abs((vunit.T*c)[0])**2))
        return {
            'cutoff': cutoff, 'N': N, 'dps': dps,
            'mass_constant': b, 'min_A': ae[0], 'min_Q': qe[0],
            'one_minus_r': 1-r,
            'gradient_energy': energy, 'mass_energy': b, 'pole_energy': pole,
            'extremizer_Q': energy-b-pole,
            'min_Q_mode_alignment_squared': align,
            'pole_neutral_projection_norm': neutral_norm,
            'coefficients': list(c),
            'provenance': 'arithmetic-input; finite high-precision diagnostic; not interval-certified',
        }
