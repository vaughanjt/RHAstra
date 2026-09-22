"""Run from repository root: python -m experiments.translation_energy_probe."""
import json
import mpmath as mp
from rhastra.operators.translation_energy import finite_diagnostic


def encode(value):
    if isinstance(value, mp.mpf):
        return mp.nstr(value, 45)
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    records = [finite_diagnostic(cutoff, N, 70)
               for cutoff in (2, 20, 50) for N in (3, 6, 10)]
    print(json.dumps(records, default=encode, indent=2))
