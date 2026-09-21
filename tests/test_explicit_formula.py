import mpmath as mp

from rhastra.explicit_formula import LogGaussian, regression


def test_log_gaussian_explicit_formula_regression():
    mp.mp.dps = 35
    result = regression(LogGaussian(0.2), zero_count=20, nmax=1000)
    assert result["provenance"] == "calibration-from-known-zeta-zeros"
    assert abs(result["residual"]) < mp.mpf("1e-25")
