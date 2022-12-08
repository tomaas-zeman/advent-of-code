from year2022.day1.common import get_elves


def run(data: list[str], raw_data: list[str]):
    return max(get_elves(data))
