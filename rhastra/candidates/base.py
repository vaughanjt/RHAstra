"""Strict interface that every Riemann-space candidate must implement.

The contract separates numerical derivation from descriptive/literature claims.
Unknown or unimplemented structure must remain explicit.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Mapping, Protocol


class EvidenceStatus(StrEnum):
    PROVED = "proved"
    DERIVED = "derived"
    PUBLISHED_CLAIM = "published-claim"
    CONJECTURAL = "conjectural"
    HEURISTIC = "heuristic"
    UNKNOWN = "unknown"
    NOT_IMPLEMENTED = "not-implemented"


@dataclass(frozen=True)
class Claim:
    statement: str
    status: EvidenceStatus
    source: str | None = None


@dataclass(frozen=True)
class CandidateMetadata:
    candidate_id: str
    name: str
    family: str
    description: str
    references: tuple[str, ...] = ()
    claims: tuple[Claim, ...] = ()


@dataclass(frozen=True)
class SymmetryReport:
    functional_equation_mechanism: str | None
    duality: str | None
    random_matrix_class: str | None
    status: EvidenceStatus = EvidenceStatus.UNKNOWN
    notes: str = ""


@dataclass(frozen=True)
class PositivityReport:
    mechanism: str | None
    status: EvidenceStatus
    notes: str = ""


@dataclass(frozen=True)
class TraceDecomposition:
    spectral: Any
    geometric: Any
    archimedean: Any
    residual: Any
    status: EvidenceStatus = EvidenceStatus.DERIVED
    diagnostics: Mapping[str, Any] = field(default_factory=dict)


class TraceTestFunction(Protocol):
    """Minimal test-function contract used by trace-formula adapters."""

    name: str

    def value(self, x: Any) -> Any:
        ...

    def transform(self, s: Any) -> Any:
        ...


class CandidateAdapter(ABC):
    """Common experimental interface for a candidate arithmetic geometry."""

    @property
    @abstractmethod
    def metadata(self) -> CandidateMetadata:
        ...

    @abstractmethod
    def spectral_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        """Return the candidate's spectral contribution derived from its model."""
        ...

    @abstractmethod
    def geometric_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        """Return the candidate's finite-place / periodic-orbit contribution."""
        ...

    @abstractmethod
    def archimedean_side(self, test_function: TraceTestFunction, **kwargs: Any) -> Any:
        """Return the candidate's archimedean / real-place contribution."""
        ...

    @abstractmethod
    def symmetry_report(self) -> SymmetryReport:
        ...

    @abstractmethod
    def positivity_report(self) -> PositivityReport:
        ...

    def trace_decomposition(self, test_function: TraceTestFunction, **kwargs: Any) -> TraceDecomposition:
        """Evaluate all implemented trace pieces and compute spectral-(geometric+archimedean)."""
        spectral = self.spectral_side(test_function, **kwargs)
        geometric = self.geometric_side(test_function, **kwargs)
        archimedean = self.archimedean_side(test_function, **kwargs)
        return TraceDecomposition(
            spectral=spectral,
            geometric=geometric,
            archimedean=archimedean,
            residual=spectral - geometric - archimedean,
        )
