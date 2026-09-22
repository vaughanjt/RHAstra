"""Core rejection gates.

A gate returns PASS, FAIL, or NOT_EVALUATED. Unknown evidence is never silently
converted into success.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from rhastra.candidates.base import CandidateAdapter, TraceTestFunction


class GateState(StrEnum):
    PASS = "pass"
    FAIL = "fail"
    NOT_EVALUATED = "not-evaluated"


@dataclass(frozen=True)
class GateResult:
    name: str
    state: GateState
    details: str
    diagnostics: dict[str, Any] | None = None


def provenance_gate(*, uses_known_zero_locations: bool, calibration: bool = False) -> GateResult:
    """Reject leakage of known zero locations into a purported candidate construction."""
    if uses_known_zero_locations and not calibration:
        return GateResult(
            name="provenance",
            state=GateState.FAIL,
            details="Known zeta-zero locations are used by a non-calibration candidate.",
        )
    return GateResult(
        name="provenance",
        state=GateState.PASS,
        details="No prohibited zero-location leakage detected.",
    )


def executable_trace_gate(
    candidate: CandidateAdapter,
    test_function: TraceTestFunction,
    *,
    tolerance: float | None = None,
    **kwargs: Any,
) -> GateResult:
    """Require an executable trace decomposition; optionally enforce a residual tolerance."""
    try:
        result = candidate.trace_decomposition(test_function, **kwargs)
    except NotImplementedError as exc:
        return GateResult(
            name="executable-trace",
            state=GateState.NOT_EVALUATED,
            details=str(exc),
        )

    if tolerance is None:
        return GateResult(
            name="executable-trace",
            state=GateState.PASS,
            details="All three trace components executed.",
            diagnostics={"residual": result.residual},
        )

    magnitude = abs(result.residual)
    state = GateState.PASS if magnitude <= tolerance else GateState.FAIL
    return GateResult(
        name="executable-trace",
        state=state,
        details=f"|residual|={magnitude} with tolerance={tolerance}",
        diagnostics={"residual": result.residual, "tolerance": tolerance},
    )
