from collections import defaultdict
from itertools import permutations
import re


def parse(data: list[str]) -> dict[str, dict[str, int]]:
    seating = defaultdict(dict)
    for line in data:
        if m := re.match("(\w+) would (lose|gain) (\d+) .* next to (\w+)", line):
            name1, action, hapiness, name2 = m.groups()
            seating[name1][name2] = (
                -int(hapiness) if action == "lose" else int(hapiness)
            )

    for guest in list(seating.keys()):
        seating["me"][guest] = 0
        seating[guest]["me"] = 0

    return seating


def compute_hapiness(seating: dict[str, dict, str, int], include_myself: bool) -> int:
    hapiness = 0

    guests = (
        seating.keys() if include_myself else (k for k in seating.keys() if k != ME)
    )

    for perm in permutations(guests):
        perm_hapiness = 0
        for i in range(len(perm)):
            perm_hapiness += seating[perm[i]][perm[(i + 1) % len(perm)]]
            perm_hapiness += seating[perm[i]][perm[i - 1]]
        hapiness = max(hapiness, perm_hapiness)

    return hapiness
