from typing import List

from common.lists import as_ints

GOAL = 15353384  # result from part1


def run(data: List[str]):
    numbers = as_ints(data)
    index = 0
    last_index = numbers.index(GOAL)
    while index < last_index:
        range_index = 1
        while range_index < last_index:
            numbers_in_range = numbers[index: range_index]
            if sum(numbers_in_range) == GOAL:
                return min(numbers_in_range) + max(numbers_in_range)
            range_index += 1
        index += 1
