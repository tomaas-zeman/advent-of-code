import re


class Card:
    def __init__(self, id: int, winning_numbers: list[int], scratched_numbers: list[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers
        self.winning_card_count = len(set(winning_numbers).intersection(set(scratched_numbers)))
        self.counter = 1


def parse(data: list[str]) -> list[Card]:
    cards = []
    for line in data:
        match = re.search(r"Card *(\d+): ([\d ]+) \| ([\d ]+)", line)
        if match is not None:
            winning_numbers = [int(n) for n in match.group(2).split()]
            scratched_numbers = [int(n) for n in match.group(3).split()]
            cards.append(Card(int(match.group(1)), winning_numbers, scratched_numbers))
    return cards
