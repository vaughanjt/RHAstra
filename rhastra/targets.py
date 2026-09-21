"""Known target-side formulas used to reject incompatible candidate models."""

from __future__ import annotations

import mpmath as mp


def riemann_von_mangoldt_smooth(T: float | mp.mpf) -> mp.mpf:
    """Smooth zero-counting term, omitting S(T) and inverse-power corrections."""
    T = mp.mpf(T)
    if T <= 0:
        raise ValueError("T must be positive")
    return T / (2 * mp.pi) * mp.log(T / (2 * mp.pi)) - T / (2 * mp.pi) + mp.mpf(7) / 8
