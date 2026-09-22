import mpmath as mp

from rhastra.candidates.base import EvidenceStatus
from rhastra.candidates.odd_weil_operator import OddWeilOperatorCandidate
from rhastra.operators.odd_weil import (
    LegacyWeilCoefficients,
    OddWeilOperatorLift,
    full_cauchy_loewner_from_parity,
    odd_block_from_sequences,
    project_odd_block,
)


def max_abs_diff(A, B):
    return max(abs(A[i, j] - B[i, j]) for i in range(A.rows) for j in range(A.cols))


def test_odd_formula_is_exact_parity_projection():
    a0_to_n = [mp.mpf("2.0"), mp.mpf("1.1"), mp.mpf("-0.7"), mp.mpf("0.2")]
    b_positive = [mp.mpf("0.3"), mp.mpf("-0.4"), mp.mpf("0.9")]

    full = full_cauchy_loewner_from_parity(a0_to_n, b_positive)
    projected = project_odd_block(full)
    direct = odd_block_from_sequences(a0_to_n[1:], b_positive)

    assert max_abs_diff(projected, direct) < mp.mpf("1e-30")


def test_legacy_code_normalization_regression_lambda20():
    mp.mp.dps = 35
    lift = OddWeilOperatorLift(LegacyWeilCoefficients(lambda_squared=20, dps=35))
    M = lift.finite_section(3)

    expected = mp.matrix([
        ["-0.73300452891138994", "-0.38254350054196990", "-0.25787931639216183"],
        ["-0.38254350054196990", "-0.20066692009669372", "-0.13663551147937204"],
        ["-0.25787931639216183", "-0.13663551147937204", "-0.094846321159336919"],
    ])
    assert max_abs_diff(M, expected) < mp.mpf("1e-15")

    eigvals, _ = mp.eigsy(M)
    assert eigvals[-1] < 0
    assert abs(eigvals[-1] - mp.mpf("-1.0838189478357864e-6")) < mp.mpf("1e-15")


def test_domain_report_does_not_claim_self_adjointness_or_continuum_model():
    candidate = OddWeilOperatorCandidate(lambda_squared=20, dps=30)
    report = candidate.operator.domain_report()

    assert report.hilbert_space.startswith("ell^2")
    assert report.symmetry_status == EvidenceStatus.DERIVED
    assert report.closability_status == EvidenceStatus.UNKNOWN
    assert report.self_adjointness_status == EvidenceStatus.UNKNOWN
    assert report.continuum_representation_status == EvidenceStatus.NOT_IMPLEMENTED
    assert candidate.positivity_report().status == EvidenceStatus.CONJECTURAL
