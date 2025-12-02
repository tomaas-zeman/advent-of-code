from operator import mul

from year2023.day20.common import parse, Pulse, push_button


def run(data: list[str], is_test: bool):
    modules = parse(data)

    count = {Pulse.LOW: 0, Pulse.HIGH: 0}
    for _ in range(1000):
        signal_count, _ = push_button(modules)
        count[Pulse.LOW] += signal_count[Pulse.LOW]
        count[Pulse.HIGH] += signal_count[Pulse.HIGH]

    return mul(*count.values())


test_result = 11687500
