from year2022.day11.common import run_monkey_business, parse_input
import math


def run(data: list[str], is_test: bool):
    monkeys = parse_input(data)
    mod_by = math.prod([monkey.test_divisible_by for monkey in monkeys])
    return run_monkey_business(monkeys, 10000, lambda x: x % mod_by)
