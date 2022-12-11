from year2020.day04.common import parse_passports


def run(data: list[str], raw_data: list[str]):
    return len([p for p in parse_passports(data) if p.is_valid()])
