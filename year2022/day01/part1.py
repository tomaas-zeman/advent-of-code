from year2022.day01.common import get_elves


def run(data: list[str], raw_data: list[str]):
    return max(get_elves(data))
