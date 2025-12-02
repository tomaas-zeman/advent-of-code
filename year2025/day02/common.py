import re

from aocutils import as_ints

pattern_none = re.compile(rf"^(\d+?)\1+$")
patterns_n = {n: re.compile(rf"^(\d+?)\1{{{n}}}$") for n in range(1, 11)}


def is_invalid_id(id: str, repeats: int | None):
    pattern = pattern_none if repeats is None else patterns_n[repeats]
    return re.match(pattern, id)


def sum_of_invalid_ids(data: str, length: int) -> int:
    total = 0

    for bounds in data.split(","):
        [min, max] = as_ints(bounds.split("-"))
        total += sum(n for n in range(min, max + 1) if is_invalid_id(str(n), length))

    return total
