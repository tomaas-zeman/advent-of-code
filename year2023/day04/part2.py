from year2023.day04.common import parse


def run(data: list[str], is_test: bool):
    cards = parse(data)
    for i, card in enumerate(cards):
        winning_cards_count = len(set(card.winning).intersection(set(card.scratched)))
        for j in range(winning_cards_count):
            cards[i + j + 1].counter += card.counter
    return sum([c.counter for c in cards])
