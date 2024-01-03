from collections import defaultdict
from functools import reduce

import numpy as np
from portion import empty

from year2020.day16.common import parse


def run(data: list[str], is_test: bool):
    if is_test:
        return True

    notes, ticket_variants = parse(data)
    all_ranges = reduce(lambda acc, r: acc.union(r), notes.values(), empty())
    valid_variants = np.array([v for v in ticket_variants if all(t in all_ranges for t in v)])

    options = defaultdict(list)
    for col in range(valid_variants.shape[1]):
        col_data = valid_variants[:, col]
        for name, interval in notes.items():
            if all(value in interval for value in col_data):
                options[name].append(col)

    for name1, cols1 in {k: v for k, v in sorted(options.items(), key=lambda item: len(item[1]))}.items():
        for name2, cols2 in options.items():
            if name1 != name2:
                [options[name2].remove(col) for col in cols1 if col in options[name2]]

    return reduce(
        lambda acc, index: acc * ticket_variants[0][index],
        [value[0] for key, value in options.items() if key.startswith("departure")],
        1,
    )
