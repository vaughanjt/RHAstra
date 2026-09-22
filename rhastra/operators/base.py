"""Shared metadata for operator candidates."""

from __future__ import annotations

from dataclasses import dataclass

from rhastra.candidates.base import EvidenceStatus


@dataclass(frozen=True)
class OperatorDomainReport:
    """What is actually established about an operator realization."""

    hilbert_space: str
    dense_core: str
    symmetry_status: EvidenceStatus
    closability_status: EvidenceStatus
    self_adjointness_status: EvidenceStatus
    continuum_representation_status: EvidenceStatus
    notes: str = ""
