"""Descriptive adapter for literature candidates that do not yet expose calculations."""

from __future__ import annotations

from typing import Any, Mapping

from .base import (
    CandidateAdapter,
    CandidateMetadata,
    Claim,
    EvidenceStatus,
    PositivityReport,
    SymmetryReport,
    TraceTestFunction,
)


_STATUS = {
    item.value: item for item in EvidenceStatus
}


class StaticCandidateAdapter(CandidateAdapter):
    """Wrap candidate JSON without pretending descriptive fields are executable mathematics."""

    def __init__(self, record: Mapping[str, Any]):
        self.record = dict(record)

    @property
    def metadata(self) -> CandidateMetadata:
        claims = tuple(
            Claim(
                statement=c["claim"],
                status=_STATUS.get(c.get("status", "unknown"), EvidenceStatus.UNKNOWN),
                source=c.get("source"),
            )
            for c in self.record.get("claims", [])
        )
        return CandidateMetadata(
            candidate_id=self.record["id"],
            name=self.record.get("name", self.record["id"]),
            family=self.record.get("space", {}).get("kind", "unknown"),
            description=self.record.get("space", {}).get("description", ""),
            references=tuple(self.record.get("references", [])),
            claims=claims,
        )

    def _unimplemented(self, part: str) -> None:
        raise NotImplementedError(
            f"{self.metadata.candidate_id}: {part} is descriptive only; "
            "an executable derivation must be implemented before numerical credit is given"
        )

    def spectral_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        self._unimplemented("spectral_side")

    def geometric_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        self._unimplemented("geometric_side")

    def archimedean_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        self._unimplemented("archimedean_side")

    def symmetry_report(self) -> SymmetryReport:
        s = self.record.get("symmetries", {})
        return SymmetryReport(
            functional_equation_mechanism=s.get("functional_equation_mechanism"),
            duality=s.get("duality"),
            random_matrix_class=s.get("expected_rmt_class"),
            status=EvidenceStatus.PUBLISHED_CLAIM if any(
                (s.get("functional_equation_mechanism"), s.get("duality"), s.get("expected_rmt_class"))
            ) else EvidenceStatus.UNKNOWN,
            notes="Descriptive literature metadata; not derived by this adapter.",
        )

    def positivity_report(self) -> PositivityReport:
        op = self.record.get("operator", {})
        status = op.get("self_adjoint_status", "unknown")
        evidence = (
            EvidenceStatus.PROVED if status == "proved"
            else EvidenceStatus.PUBLISHED_CLAIM if status in {"partial", "conjectural"}
            else EvidenceStatus.UNKNOWN
        )
        return PositivityReport(
            mechanism=None,
            status=evidence,
            notes=f"Recorded self-adjointness status: {status}. No positivity form is implemented.",
        )
