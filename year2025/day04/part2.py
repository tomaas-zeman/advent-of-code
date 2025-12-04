from aocutils import Numpy
from year2025.day04.common import find_accessible_rolls


def run(data: list[str], is_test: bool):
    warehouse = Numpy.from_input_as_str(data)

    total_removed_rolls = 0

    while True:
        accessible_rolls = find_accessible_rolls(warehouse)

        if len(accessible_rolls) == 0:
            break

        total_removed_rolls += len(accessible_rolls)

        for [row, col] in accessible_rolls:
            warehouse[row, col] = "."

        accessible_rolls = []

    return total_removed_rolls


test_result = 43
