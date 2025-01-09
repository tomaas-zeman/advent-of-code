from itertools import combinations
from math import prod
from typing import Callable


Options = Callable[[set[int], int], set[int]]


def options(pkgs: set[int], size: int, weight: int) -> Options:
    return (set(c) for c in combinations(pkgs, size) if sum(c) == weight)


def find_smallest_groups(pkgs: set[int], weight: int):
    for n in range(1, len(pkgs)):
        groups = list(options(pkgs, n, weight))
        if len(groups) > 0:
            return groups


def setup_exists(initial_group: set[int], pkgs: set[int], weight: int, depth: int):
    if depth == 1:
        return sum(pkgs.difference(initial_group)) == weight

    remaining = pkgs.difference(initial_group)
    for size in range(len(remaining)):
        for group in options(remaining, size, weight):
            exists = setup_exists(group, remaining, weight, depth - 1)
            if exists:
                return True
    return False


def compute_quantum_entaglement(pkgs: set[int], groups: int):
    weight = sum(pkgs) / groups
    score = float("inf")
    smallest_groups = find_smallest_groups(pkgs, weight)

    for smallest_group in smallest_groups:
        if setup_exists(smallest_group, pkgs, weight, groups - 1):
            score = min(score, prod(smallest_group))

    return score
