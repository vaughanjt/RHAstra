"""First-class RHAstra representation of the legacy odd Weil operator idea."""

from __future__ import annotations

from typing import Any

from .base import (
    CandidateAdapter,
    CandidateMetadata,
    Claim,
    EvidenceStatus,
    PositivityReport,
    SymmetryReport,
    TraceTestFunction,
)
from rhastra.operators.odd_weil import LegacyWeilCoefficients, OddWeilOperatorLift


class OddWeilOperatorCandidate(CandidateAdapter):
    """Operator candidate whose trace-formula adapter is intentionally incomplete."""

    def __init__(self, lambda_squared: float, dps: int = 40):
        self.operator = OddWeilOperatorLift(
            LegacyWeilCoefficients(lambda_squared=lambda_squared, dps=dps)
        )

    @property
    def metadata(self) -> CandidateMetadata:
        return CandidateMetadata(
            candidate_id="legacy-odd-weil-ell2",
            name="Odd Weil Cauchy–Loewner coefficient operator",
            family="odd Weil form with canonical self-adjoint realization",
            description=(
                "Natural coefficient-space lift of the odd-parity Weil matrix "
                "to a symmetric quadratic form on c_00 subset ell^2(N)."
            ),
            references=(
                "vaughanjt/RiemannHypothesisProof session59b_cauchy_structure.py",
                "vaughanjt/RiemannHypothesisProof session82_operator_lift.py",
            ),
            claims=(
                Claim(
                    "Finite odd matrices are exact compressions of the coefficient kernel.",
                    EvidenceStatus.DERIVED,
                    "RHAstra algebraic parity reduction",
                ),
                Claim(
                    "The formal kernel is symmetric on c_00.",
                    EvidenceStatus.DERIVED,
                    "RHAstra algebraic parity reduction",
                ),
                Claim(
                    "A canonical self-adjoint form realization on ell^2 exists.",
                    EvidenceStatus.PUBLISHED_CLAIM,
                    "CCM arXiv:2511.22755v1 Props. 3.3-3.4; normalization audit",
                ),
                Claim(
                    "The operator is non-positive on its full domain.",
                    EvidenceStatus.CONJECTURAL,
                    "legacy Lorentzian Weil Matrix conjecture",
                ),
            ),
        )

    def spectral_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        raise NotImplementedError(
            "No spectral trace formula has been derived for the ell^2 operator candidate."
        )

    def geometric_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        raise NotImplementedError(
            "Prime coefficients are implemented, but not as an independent trace-formula side."
        )

    def archimedean_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        raise NotImplementedError(
            "Archimedean coefficients are implemented, but not as an independent trace-formula side."
        )

    def symmetry_report(self) -> SymmetryReport:
        return SymmetryReport(
            functional_equation_mechanism=None,
            duality="exact n -> -n parity before odd projection",
            random_matrix_class=None,
            status=EvidenceStatus.DERIVED,
            notes="Parity is exact; a deeper functional-equation mechanism is not yet derived.",
        )

    def positivity_report(self) -> PositivityReport:
        return PositivityReport(
            mechanism="conjectured non-positivity of the odd coefficient-space quadratic form",
            status=EvidenceStatus.CONJECTURAL,
            notes=(
                "Finite negative sections are evidence only. Full odd Weil positivity "
                "requires the stronger inequality -K >= v v*, including the "
                "negative rank-one pole term. See the normalization audit."
            ),
        )
