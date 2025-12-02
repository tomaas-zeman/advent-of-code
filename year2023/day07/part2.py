from collections import Counter

from year2023.day07.common import Hand, Rank, calculate_winnings, get_rank, card_order


def get_rank_with_jokers(cards: str) -> Rank:
    count = Counter(cards.replace("J", ""))
    most_common = count.most_common(1)

    # Edge case - all jokers
    if len(most_common) == 0:
        return Rank.FIVE_OF_A_KIND

    return get_rank(cards.replace("J", most_common[0][0]))


def parse(data: list[str]) -> list[Hand]:
    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(
            Hand(cards, int(bid), [-1 if c == "J" else card_order.index(c) for c in cards], get_rank_with_jokers(cards))
        )
    return hands


def run(data: list[str], is_test: bool):
    hands = parse(data)
    return calculate_winnings(hands)


test_result = 5905
