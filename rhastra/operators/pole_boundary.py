"""Boundary defect of compressed symmetric shifts on the pole-neutral space."""
import mpmath as mp
from .weil_reference import odd_pole_vector


def odd_function(c, x, L):
    if x < 0 or x > L:
        return mp.mpc(0)
    return 1j * mp.sqrt(2/L) * sum(
        (c[j-1]*mp.sin(2*mp.pi*j*x/L) for j in range(1, len(c)+1)), mp.mpf(0))


def neutral_vector(L):
    """Two-mode unit vector, exactly pole neutral in symbolic arithmetic."""
    v = odd_pole_vector(L, 2)
    c = mp.matrix([v[1], -v[0]])
    return c / mp.norm(c)


def pole_moment(c, L):
    return -1j * (odd_pole_vector(L, len(c)).T * mp.matrix(c))[0]


def shifted_moment(c, L, y):
    """Direct moment of P_I(tau_y+tau_-y)P_I f, without mode truncation."""
    if not 0 < y < L:
        raise ValueError('require 0 < y < L')
    points = sorted(set([mp.mpf(0), y, L-y, L]))
    return mp.sqrt(2)*mp.quad(lambda x: mp.sinh((x-L/2)/2) * (
        odd_function(c, x-y, L)+odd_function(c, x+y, L)), points)


def boundary_defect(c, L, y):
    """Moment lost at the upper boundary, doubled by odd symmetry."""
    if not 0 < y < L:
        raise ValueError('require 0 < y < L')
    return 2*mp.sqrt(2)*mp.quad(lambda t: mp.sinh((t+y-L/2)/2)
                             * odd_function(c, t, L), [L-y, L])
