from typing import List

from year2020.day4.common import parse_passports


def run(data: List[str], raw_data: List[str]):
    return len([p for p in parse_passports(data) if p.is_valid()])
