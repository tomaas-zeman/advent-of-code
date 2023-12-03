from year2023.day03.common import parse, Item


def get_adj_items(main: Item, others: list[Item]):
    return [
        o for o in others if main.row + 1 >= o.row >= main.row - 1 and main.span[0] - 1 <= o.span[0] <= main.span[1]
    ]


def run(data: list[str], is_test: bool):
    numbers, specials = parse(data)
    return sum([int(n.value) for n in numbers if any(get_adj_items(n, specials))])
