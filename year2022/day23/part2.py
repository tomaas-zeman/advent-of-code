from year2022.day23.common import do_round, enlarge_map, parse_input


def run(data: list[str], is_test: bool):
    elves, map = parse_input(data)
    steps = 1000
    map = enlarge_map(map, steps, elves)

    rounds = 1
    while True:
        nobody_moved = do_round(elves, map)
        if nobody_moved:
            break
        rounds += 1

    return rounds


test_result = 20
