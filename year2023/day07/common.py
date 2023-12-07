from __future__ import annotations
from collections import Counter
from enum import Enum
from functools import cmp_to_key


card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Rank(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    def __init__(self, cards: str, bid: int, card_values: list[int], rank: Rank):
        self.cards = cards
        self.card_values = card_values
        self.bid = bid
        self.rank = rank

    @staticmethod
    def compare(one: Hand, two: Hand) -> int:
        if one.rank == two.rank:
            for i in range(len(one.cards)):
                if one.card_values[i] == two.card_values[i]:
                    continue
                return one.card_values[i] - two.card_values[i]
            return 0
        return one.rank.value - two.rank.value


def calculate_winnings(hands: list[Hand]) -> int:
    ranked_hands = sorted(hands, key=cmp_to_key(Hand.compare))
    return sum([(i + 1) * hand.bid for i, hand in enumerate(ranked_hands)])


def get_rank(cards: str) -> Rank:
    count = Counter(cards)
    if len(count) == 1:
        return Rank.FIVE_OF_A_KIND
    elif len(count) == 2:
        if 4 in count.values():
            return Rank.FOUR_OF_A_KIND
        else:
            return Rank.FULL_HOUSE
    elif len(count) == 3:
        if 3 in count.values():
            return Rank.THREE_OF_A_KIND
        else:
            return Rank.TWO_PAIR
    elif len(count) == 4:
        return Rank.ONE_PAIR
    else:
        return Rank.HIGH_CARD
