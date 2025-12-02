import sys
from operator import lt, gt

from year2022.day21.common import Monkey, parse_input, recursing_to_madness


def contains_humn(monkey: Monkey):
    if monkey.name == "humn":
        return True
    if not hasattr(monkey, "left") and not hasattr(monkey, "right"):
        return False
    return contains_humn(monkey.left) or contains_humn(monkey.right)


def get_comparison_direction(monkeys: dict[str, Monkey], humn_subtree: Monkey):
    monkeys["humn"].value = float(1000)
    result1 = recursing_to_madness(humn_subtree)
    monkeys["humn"].value = float(2000)
    result2 = recursing_to_madness(humn_subtree)
    return lt if result1 < result2 else gt


def run(data: list[str], is_test: bool):
    monkeys = parse_input(data)
    subtrees = {contains_humn(m): m for m in [monkeys["root"].left, monkeys["root"].right]}

    result_no_humn = recursing_to_madness(subtrees[False])

    number_min = 0
    number_max = sys.maxsize
    compare = get_comparison_direction(monkeys, subtrees[True])

    while True:
        number = float((number_max - number_min) // 2 + number_min)
        monkeys["humn"].value = number
        result_humn = recursing_to_madness(subtrees[True])

        if result_humn == result_no_humn:
            return number

        if compare(result_humn, result_no_humn):
            number_min = number
        else:
            number_max = number


test_result = 301.0
