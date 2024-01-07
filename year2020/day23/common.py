from __future__ import annotations

from dataclasses import dataclass
from functools import reduce

from aocutils import as_ints


@dataclass
class Data:
    cups: list[Cup]
    cups_by_value: dict[int, Cup]
    highest_number: int


@dataclass
class Cup:
    value: int


def parse(data: list[str], additional_cups: list[int]) -> Data:
    cups = [Cup(value) for value in as_ints([c for c in data[0]]) + additional_cups]
    for i, cup in enumerate(cups):
        cup.prev = cups[i - 1]
        cup.next = cups[(i + 1) % len(cups)]

    cups_by_value = {c.value: c for c in cups}
    highest_number = max(cups_by_value.keys())

    return Data(cups, cups_by_value, highest_number)


def make_steps(data: Data, total_steps: int):
    current_cup = data.cups[0]

    for move in range(total_steps):
        pick = list(reduce(lambda acc, _: acc + [acc[-1].next], range(2), [current_cup.next]))
        pick_values = [c.value for c in pick]

        # Join cups before and after pick
        after_pick_cup = pick[-1].next
        current_cup.next = after_pick_cup
        after_pick_cup.prev = current_cup

        # Find destination cup
        dst_cup_value = (current_cup.value - 1) % (data.highest_number + 1)
        while dst_cup_value in pick_values or dst_cup_value <= 0:
            dst_cup_value = (dst_cup_value - 1) % (data.highest_number + 1)
        dst_cup = data.cups_by_value[dst_cup_value]

        # Place pick after destination cup
        after_dst_cup = dst_cup.next
        pick[0].prev = dst_cup
        dst_cup.next = pick[0]
        after_dst_cup.prev = pick[-1]
        pick[-1].next = after_dst_cup

        # Move cursor
        current_cup = current_cup.next
