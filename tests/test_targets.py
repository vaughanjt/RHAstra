import mpmath as mp
import pytest

from rhastra.targets import riemann_von_mangoldt_smooth


def test_counting_target_is_finite():
    value = riemann_von_mangoldt_smooth(1000)
    assert mp.isfinite(value)
    assert value > 0


def test_counting_target_rejects_nonpositive_height():
    with pytest.raises(ValueError):
        riemann_von_mangoldt_smooth(0)
