from functools import reduce

from portion import empty

from aocutils import flatten
from year2020.day16.common import parse


def run(data: list[str], is_test: bool):
    notes, ticket_variants = parse(data)
    all_ranges = reduce(lambda acc, r: acc.union(r), notes.values(), empty())
    return sum(ticket for ticket in flatten(ticket_variants[1:]) if ticket not in all_ranges)


test_result = 71
