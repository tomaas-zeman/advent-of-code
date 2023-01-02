from year2020.day04.common import parse_passports


def run(data: list[str], is_test: bool):
    return len([p for p in parse_passports(data) if p.has_mandatory_fields()])
