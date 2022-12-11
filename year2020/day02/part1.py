from collections import Counter

from year2020.day02.common import parse_input_data


def run(data: list[str], raw_data: list[str]):
    passwords = parse_input_data(data)

    correct_passwords = 0
    for [min_count, max_count], letter, password in passwords:
        counter = Counter(password)
        if int(min_count) <= counter[letter] <= int(max_count):
            correct_passwords += 1

    return correct_passwords
