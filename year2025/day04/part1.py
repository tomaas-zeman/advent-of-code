from aocutils import Numpy
from year2025.day04.common import find_accessible_rolls


def run(data: list[str], is_test: bool):
    warehouse = Numpy.from_input_as_str(data)
    return len(find_accessible_rolls(warehouse))


test_result = 13
