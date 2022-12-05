from typing import List
from year2019.day1.common import fuel_amount


def run(data: List[str], raw_data: List[str]):
    return sum([fuel_amount(int(mass)) for mass in data])
