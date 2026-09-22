import mpmath as mp
import pytest
from rhastra.operators.odd_weil import LegacyWeilCoefficients, OddWeilOperatorLift
from rhastra.operators.translation_energy import gradient_entry, mass_constant, finite_diagnostic
from rhastra.operators.weil_reference import odd_pole_vector


@pytest.mark.parametrize('cutoff', [2, 20, 50])
def test_gradient_model_matches_weil_arithmetic_form(cutoff):
    with mp.workdps(40):
        coeff = LegacyWeilCoefficients(cutoff, 40)
        lift = OddWeilOperatorLift(coeff)
        b = mass_constant(coeff)
        for j, k in [(1, 1), (1, 2), (2, 2), (2, 3)]:
            direct = gradient_entry(coeff, j, k)
            assert abs(direct - b*int(j == k) + lift.entry(j, k)) < mp.mpf('1e-28')


def test_mass_integral_and_pole_moment():
    with mp.workdps(40):
        # Independent real-space checks of the offset and moment normalization.
        integral = mp.quad(lambda y: mp.expm1(y/2)/mp.sinh(y) if y else mp.mpf('.5'), [0, 1, mp.inf])
        assert abs(mp.euler + mp.log(4*mp.pi) + integral
                   - (mp.log(mp.pi)-mp.digamma(mp.mpf('.25')))) < mp.mpf('1e-35')
        L = mp.log(20)
        v = odd_pole_vector(L, 3)
        for j in range(1, 4):
            moment = mp.sqrt(2)*mp.quad(lambda x: 1j*mp.sqrt(2/L)
                * mp.sin(2*mp.pi*j*x/L)*mp.sinh((x-L/2)/2), [0, L])
            assert abs(moment + 1j*v[j-1]) < mp.mpf('1e-35')


def test_extremizer_variational_identity():
    with mp.workdps(50):
        result = finite_diagnostic(20, 3, 50)
        # The normalized extremizer has pole/arithmetical-energy ratio r.
        arithmetic_energy = result['gradient_energy']-result['mass_energy']
        r = 1-result['one_minus_r']
        assert abs(result['pole_energy']/arithmetic_energy-r) < mp.mpf('1e-35')
        assert result['one_minus_r'] > 0
