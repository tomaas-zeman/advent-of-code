from itertools import combinations
from typing import List

from common import as_ints


def run(data: List[str]):
    numbers = as_ints(data)
    buffer_size = 25
    index = 0
    while index + buffer_size < len(numbers):
        pairs = combinations(numbers[index: index + buffer_size], 2)
        current_number = numbers[index + buffer_size]
        if not any([a + b == current_number for a, b in pairs]):
            return current_number
        index += 1
