from aocutils import as_ints
from year2015.day24.common import compute_quantum_entaglement


def run(data: list[str], is_test: bool):
    pkgs = set(as_ints(data))
    return compute_quantum_entaglement(pkgs, 4)
