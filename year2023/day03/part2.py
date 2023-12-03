from year2023.day03.common import Item, parse


def get_adj_items(main: Item, others: list[Item]):
    return [o for o in others if o.row + 1 >= main.row >= o.row - 1 and o.span[0] - 1 <= main.span[0] <= o.span[1]]


def mul_adj_numbers(special: Item, numbers: list[Item]):
    adj_numbers = get_adj_items(special, numbers)
    if len(adj_numbers) == 2:
        return int(adj_numbers[0].value) * int(adj_numbers[1].value)
    return 0


def run(data: list[str], is_test: bool):
    numbers, specials = parse(data)
    return sum([mul_adj_numbers(s, numbers) for s in specials if s.value == "*"])
