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
]
