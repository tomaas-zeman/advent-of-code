from collections import defaultdict

from year2015.day23.common import run_program


def run(data: list[str], is_test: bool):
    registers = defaultdict(int)
    registers["a"] = 1
    run_program(data, registers)
    return registers["b"]
