from year2023.day03.common import Item, parse


def mul_adj_numbers(special: Item, numbers: list[Item]):
    adj_numbers = [
        o for o in numbers if o.row + 1 >= special.row >= o.row - 1 and o.span[0] - 1 <= special.span[0] <= o.span[1]
    ]
    if len(adj_numbers) == 2:
        return int(adj_numbers[0].value) * int(adj_numbers[1].value)
    return 0


def run(data: list[str], is_test: bool):
    numbers, specials = parse(data)
    return sum([mul_adj_numbers(s, numbers) for s in specials if s.value == "*"])


test_result = 467835
