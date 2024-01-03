import re
from functools import reduce

from portion import empty, closed

from aocutils import as_ints


def parse(data: list[str]) -> tuple[dict[str, int], list[list[int]]]:
    notes = {}
    ticket_variants = []

    for line in data:
        if ":" in line:
            if groups := as_ints(re.findall(r"(\d+)", line)):
                name = line.split(":")[0]
                notes[name] = reduce(lambda acc, r: acc.union(closed(*r)), zip(groups[::2], groups[1::2]), empty())
                continue

        ticket_variants.append(as_ints(line.split(",")))

    return notes, ticket_variants
