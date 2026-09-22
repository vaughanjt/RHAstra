import mpmath as mp
import pytest
from rhastra.operators.pole_boundary import (
    neutral_vector, pole_moment, shifted_moment, boundary_defect,
)


@pytest.mark.parametrize('fraction', ['0.1', '0.37', '0.8'])
def test_exact_boundary_identity(fraction):
    with mp.workdps(45):
        L=mp.log(20)
        y=L*mp.mpf(fraction)
        c=[mp.mpf('.7'), mp.mpf('-.2'), mp.mpf('.3')]
        direct=shifted_moment(c,L,y)
        expected=2*mp.cosh(y/2)*pole_moment(c,L)-boundary_defect(c,L,y)
        assert abs(direct-expected)<mp.mpf('1e-38')


def test_prime_shift_does_not_preserve_pole_neutrality():
    with mp.workdps(45):
        L=mp.log(20)
        y=mp.log(2)
        c=neutral_vector(L)
        assert abs(pole_moment(c,L))<mp.mpf('1e-40')
        assert abs(shifted_moment(c,L,y))>mp.mpf('.01')
        assert abs(shifted_moment(c,L,y)+boundary_defect(c,L,y))<mp.mpf('1e-38')
