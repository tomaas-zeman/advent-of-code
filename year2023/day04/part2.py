from year2023.day04.common import parse


def run(data: list[str], is_test: bool):
    cards = parse(data)
    for i, card in enumerate(cards):
        for j in range(card.winning_card_count):
            cards[i + j + 1].counter += card.counter
    return sum([c.counter for c in cards])
