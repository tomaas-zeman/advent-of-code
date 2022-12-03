from typing import List
from year2022.day3.common import letter_value


def run(data: List[str]):
    sum = 0
    for line in data:
        first = line[0 : len(line) // 2]
        second = line[len(line) // 2 :]
        common_letter = set(first).intersection(second).pop()
        sum += letter_value(ord(common_letter))
    return sum
