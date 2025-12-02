from year2020.day23.common import parse, make_steps


def run(data: list[str], is_test: bool):
    data = parse(data, [i for i in range(len(data[0]) + 1, 1_000_001)])
    make_steps(data, 10_000_000)
    return data.cups_by_value[1].next.value * data.cups_by_value[1].next.next.value


test_result = 149245887792
