import re
from typing import Callable
from common.utils import memoize


@memoize
def process(springs: str, conditions: tuple[str]) -> int:
    if len(conditions) == 0:
        return 0 if "#" in springs else 1

    if sum(conditions) + len(conditions) - 1 > len(springs):
        return 0

    count = 0
    offset = 0
    pattern = re.compile(f"^[#?]{{{conditions[0]}}}([?.]+|$)")

    while offset + conditions[0] <= len(springs):
        substring = springs[offset : offset + conditions[0] + 1]

        if pattern.match(substring):
            count += process(springs[offset + conditions[0] + 1 :], conditions[1:])

        if substring[0] == "#":
            break

        offset += 1

    return count


def get_arrangement_count(data: list[str], parse_line: Callable[[str], tuple[str, tuple[int]]]) -> int:
    combinations = 0

    for line in data:
        springs, conditions = parse_line(line)
        process.clear_cache()
        combinations += process(springs, conditions)

    return combinations
