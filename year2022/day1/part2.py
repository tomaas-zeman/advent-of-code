from year2022.day1.common import get_elves


def run(data: list[str], raw_data: list[str]):
    return sum(sorted(get_elves(data))[-3:])
