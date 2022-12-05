from typing import List
from year2022.day1.common import get_elves


def run(data: List[str], raw_data: List[str]):    
    return sum(sorted(get_elves(data))[-3:])
