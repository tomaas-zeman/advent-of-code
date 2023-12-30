import math

from year2022.day11.common import run_monkey_business, parse_input


def run(data: list[str], is_test: bool):
    monkeys = parse_input(data)
    return run_monkey_business(monkeys, 20, lambda x: math.floor(x // 3))
