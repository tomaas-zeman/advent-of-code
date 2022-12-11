from collections import deque
from typing import Callable
from operator import add, mul


class Monkey:
    def __init__(
        self,
        items: list[int],
        operation: Callable[[int], int],
        test_divisible_by: int,
        dest_if_true: int,
        dest_if_false: int,
    ):
        self.items = deque(items)
        self.operation = operation
        self.test_divisible_by = test_divisible_by
        self.dest_if_true = dest_if_true
        self.dest_if_false = dest_if_false

        self.inspections_made = 0


def get_operation(operator: str, operand: str):
    operators = {"+": add, "*": mul}
    return lambda x: operators[operator](x, x if operand == "old" else int(operand))


def parse_input(data: list[str]):
    monkeys: list[Monkey] = []
    for monkey_data in [data[i : i + 7] for i in range(0, len(data), 7)]:
        items = [int(item.strip()) for item in monkey_data[1][16:].split(",")]
        operation = get_operation(monkey_data[2][21], monkey_data[2][23:])
        test_divisible_by = int(monkey_data[3][18:])
        dest_if_true = int(monkey_data[4][-1])
        dest_if_false = int(monkey_data[5][-1])
        monkeys.append(Monkey(items, operation, test_divisible_by, dest_if_true, dest_if_false))
    return monkeys


def run_monkey_business(monkeys: list[Monkey], rounds: int, worry_modifier: Callable[[int], int]):
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey.inspections_made += 1
                item = monkey.items.popleft()
                new_worry = worry_modifier(monkey.operation(item))
                dest_monkey = monkey.dest_if_true if new_worry % monkey.test_divisible_by == 0 else monkey.dest_if_false
                monkeys[dest_monkey].items.append(new_worry)

    inspections = sorted([m.inspections_made for m in monkeys], reverse=True)
    return inspections[0] * inspections[1]
