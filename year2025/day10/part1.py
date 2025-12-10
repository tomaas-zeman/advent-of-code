from itertools import combinations
import numpy as np
from year2025.day10.common import Input, parse_input


def calculate_min_presses(input: Input):
    for i in range(1, len(input.buttons)):
        expected = [0 if l == "." else 1 for l in input.lights]
        for combination in combinations(input.buttons, i):
            this = [0] * len(expected)
            for button in combination:
                for i in button:
                    this[i] = (this[i] + 1) % 2
                if np.array_equal(this, expected):
                    return len(combination)

    raise "Oops!"


def run(data: list[str], is_test: bool):
    inputs = parse_input(data)
    return sum([calculate_min_presses(input) for input in inputs])


test_result = 7
