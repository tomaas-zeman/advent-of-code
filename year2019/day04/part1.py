from collections import Counter
from year2019.day04.common import count_valid_passwords


def run(data: list[str], raw_data: list[str]):
    def is_valid(password):
        return Counter(password).most_common(1)[0][1] > 1

    return count_valid_passwords([is_valid])
