from year2022.day23.common import do_round, parse_input, enlarge_map
import numpy as np


def run(data: list[str], is_test: bool):
    elves, map = parse_input(data)
    steps = 10
    map = enlarge_map(map, steps, elves)

    for _ in range(steps):
        do_round(elves, map)

    elves = np.where(map == "#")
    return np.count_nonzero(map[min(elves[0]) : max(elves[0]) + 1, min(elves[1]) : max(elves[1]) + 1] == ".")
