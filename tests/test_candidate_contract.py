import json
from pathlib import Path

import pytest

from rhastra.candidates import StaticCandidateAdapter
from rhastra.explicit_formula import LogGaussian
from rhastra.gates.core import GateState, executable_trace_gate, provenance_gate


ROOT = Path(__file__).resolve().parents[1]


def test_static_candidate_preserves_unknown_as_unimplemented():
    records = json.loads((ROOT / "candidate_examples.json").read_text())
    adapter = StaticCandidateAdapter(records[0])
    result = executable_trace_gate(adapter, LogGaussian(0.2))
    assert result.state == GateState.NOT_EVALUATED


def test_known_zero_leakage_is_rejected_outside_calibration():
    result = provenance_gate(uses_known_zero_locations=True, calibration=False)
    assert result.state == GateState.FAIL


def test_known_zero_use_is_allowed_for_labeled_calibration():
    result = provenance_gate(uses_known_zero_locations=True, calibration=True)
    assert result.state == GateState.PASS
