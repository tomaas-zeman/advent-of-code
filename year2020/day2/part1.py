from collections import Counter
from typing import List

from year2020.day2.common import parse_input_data


def run(data: List[str], raw_data: List[str]):
    passwords = parse_input_data(data)

    correct_passwords = 0
    for [min_count, max_count], letter, password in passwords:
        counter = Counter(password)
        if int(min_count) <= counter[letter] <= int(max_count):
            correct_passwords += 1

    return correct_passwords
