from year2023.day07.common import Hand, calculate_winnings, card_order, get_rank


def parse(data: list[str]) -> list[Hand]:
    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid), [card_order.index(c) for c in cards], get_rank(cards)))
    return hands


def run(data: list[str], is_test: bool):
    hands = parse(data)
    return calculate_winnings(hands)


test_result = 6440
