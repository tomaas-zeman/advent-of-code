from typing import List

from year2020.day4.common import parse_passports


def run(data: List[str]):
    return len([p for p in parse_passports(data) if p.has_mandatory_fields()])
