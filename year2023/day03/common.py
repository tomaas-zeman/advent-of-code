import re


class Item:
    def __init__(self, value, row: int, span: int) -> None:
        self.value = value
        self.row = row
        self.span = span


def parse(data: list[str]):
    numbers = []
    specials = []

    for row, line in enumerate(data):
        numbers.extend([Item(match.group(), row, match.span()) for match in re.finditer("\d+", line)])
        specials.extend([Item(match.group(), row, match.span()) for match in re.finditer("[^\d\.]", line)])

    return numbers, specials
