from typing import List
from collections import Counter
from year2019.day4.common import count_valid_passwords


def run(data: List[str], raw_data: List[str]):
    def is_valid(password):
        return any([count == 2 for _, count in Counter(password).items()])

    return count_valid_passwords([is_valid])
