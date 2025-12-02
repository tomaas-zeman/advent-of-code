from year2023.day03.common import parse, Item


def has_adj_special_char(number: Item, specials: list[Item]):
    return any(
        s
        for s in specials
        if number.row + 1 >= s.row >= number.row - 1 and number.span[0] - 1 <= s.span[0] <= number.span[1]
    )


def run(data: list[str], is_test: bool):
    numbers, specials = parse(data)
    return sum([int(n.value) for n in numbers if has_adj_special_char(n, specials)])


test_result = 4361
