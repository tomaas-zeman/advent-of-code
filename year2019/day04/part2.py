from collections import Counter

from year2019.day04.common import count_valid_passwords


def run(data: list[str], is_test: bool):
    def is_valid(password):
        return any([count == 2 for _, count in Counter(password).items()])

    return count_valid_passwords([is_valid])
