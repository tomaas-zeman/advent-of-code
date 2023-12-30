from __future__ import annotations

import re
from operator import add, mul, sub, truediv
from typing import Callable


class Monkey:
    def __init__(self, name: str):
        self.name = name

    def set_value(self, value: float | Callable[[float, float], float]):
        self.value = value

    def set_left(self, left: Monkey):
        self.left = left

    def set_right(self, right: Monkey):
        self.right = right


def parse_input(data: list[str]):
    monkeys = {name: Monkey(name) for line in data if (name := line.split(":")[0])}

    number_monkey = re.compile(r"([a-z]+): (\d+)")
    operation_monkey = re.compile(r"([a-z]+): ([a-z]+) (.) ([a-z]+)")
    ops = {"+": add, "-": sub, "*": mul, "/": truediv}

    for line in data:
        if (match := number_monkey.match(line)) is not None:
            name, value = match.groups()
            monkeys[name].value = float(value)
        elif (match := operation_monkey.match(line)) is not None:
            name, left, op, right = match.groups()
            monkeys[name].value = ops[op]
            monkeys[name].left = monkeys[left]
            monkeys[name].right = monkeys[right]

    return monkeys


def recursing_to_madness(monkey: Monkey):
    value_or_fn = monkey.value  # for type guard

    if isinstance(value_or_fn, float):
        return value_or_fn

    return value_or_fn(recursing_to_madness(monkey.left), recursing_to_madness(monkey.right))
