"""Candidate-space interfaces and descriptive adapters."""

from .base import (
    CandidateAdapter,
    CandidateMetadata,
    Claim,
    EvidenceStatus,
    PositivityReport,
    SymmetryReport,
    TraceDecomposition,
)
from .static import StaticCandidateAdapter

__all__ = [
    "CandidateAdapter",
    "CandidateMetadata",
    "Claim",
    "EvidenceStatus",
    "PositivityReport",
    "SymmetryReport",
    "TraceDecomposition",
    "StaticCandidateAdapter",
    "OddWeilOperatorCandidate",
]


def __getattr__(name):
    # The operator base imports EvidenceStatus; eagerly importing its adapter
    # here re-enters the partly initialized operators package.
    if name == "OddWeilOperatorCandidate":
        from .odd_weil_operator import OddWeilOperatorCandidate
        return OddWeilOperatorCandidate
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
