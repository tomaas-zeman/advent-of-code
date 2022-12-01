from typing import List
from year2022.day1.common import get_elves


def run(data: List[str]):
    return max(get_elves(data))

