from year2023.day12.common import get_arrangement_count


def parse_line(line: str) -> tuple[str, tuple[int]]:
    springs = line.split(" ")[0]
    conditions = tuple(map(int, line.split(" ")[1].split(",")))
    return springs, conditions


def run(data: list[str], is_test: bool):
    return get_arrangement_count(data, parse_line)
