import mpmath as mp
import pytest

from rhastra.operators.odd_weil import LegacyWeilCoefficients, OddWeilOperatorLift
from rhastra.operators.weil_reference import (
    arithmetic_entry, correlation, odd_pole_vector, odd_weil_section,
)


@pytest.mark.parametrize('cutoff', [2, 20, 50])
def test_coefficient_matrix_matches_direct_correlation_functional(cutoff):
    with mp.workdps(45):
        coeff = LegacyWeilCoefficients(cutoff, dps=45)
        lift = OddWeilOperatorLift(coeff)
        for j, k in [(1, 1), (1, 2), (2, 3), (3, 3)]:
            direct = arithmetic_entry(coeff, j, k) - arithmetic_entry(coeff, j, -k)
            assert abs(direct - lift.entry(j, k)) < mp.mpf('1e-30')


def test_correlation_formula_against_overlap_integrals():
    with mp.workdps(40):
        L = mp.log(20)
        y = L * mp.mpf('0.37')
        for n, m in [(0, 0), (1, 1), (1, 2), (2, -3)]:
            def mode(k, x):
                return mp.exp(2j * mp.pi * k * x / L) / mp.sqrt(L)
            direct = mp.quad(lambda x: mp.conj(mode(n, x-y)) * mode(m, x), [y, L])
            direct += mp.quad(lambda x: mp.conj(mode(n, x+y)) * mode(m, x), [0, L-y])
            assert abs(direct - correlation(n, m, y, L)) < mp.mpf('1e-35')


def test_odd_pole_term_against_direct_pole_integral():
    with mp.workdps(40):
        L = mp.log(20)
        v = odd_pole_vector(L, 3)
        for j in range(1, 4):
            for k in range(1, 4):
                direct = mp.quad(lambda y: 2 * mp.cosh(y / 2) * (
                    correlation(j, k, y, L) - correlation(j, -k, y, L)), [0, L])
                assert abs(direct + v[j-1] * v[k-1]) < mp.mpf('1e-35')
        lift = OddWeilOperatorLift(LegacyWeilCoefficients(20, dps=40))
        Q = odd_weil_section(lift, 3)
        assert mp.norm(Q + lift.finite_section(3)) > mp.mpf('0.1')
        # Merely a finite regression, not a positivity certificate for all N,L.
        values, _ = mp.eigsy(Q)
        assert values[0] > 0


def test_operator_import_in_fresh_process():
    # Full-suite ordering used to hide a circular package import.
    import subprocess
    import sys
    subprocess.run([sys.executable, "-c",
                    "from rhastra.operators import OddWeilOperatorLift; "
                    "from rhastra.candidates import OddWeilOperatorCandidate"],
                   check=True)
