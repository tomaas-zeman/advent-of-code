from year2025.day08.common import compute


def run(data: list[str], is_test: bool):
    circuit_sizes, _ = compute(data, 10 if is_test else 1000)
    return circuit_sizes


test_result = 40
