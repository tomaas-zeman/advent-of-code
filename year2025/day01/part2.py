from typing import List
from year2025.day01.common import parse_input


def run(data: List[str], is_test: bool):
    zeros = 0
    dial = 50

    for direction, clicks in parse_input(data):
        for i in range(clicks):
            dial = (dial + direction) % 100
            if dial == 0:
                zeros += 1

    return zeros


test_result = 6
