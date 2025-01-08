from itertools import combinations

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    containers = as_ints(data)
    valid = 0

    for n in range(1, len(containers) + 1):
        for c in combinations(containers, n):
            if sum(c) == (25 if is_test else 150):
                valid += 1
    
    return valid
