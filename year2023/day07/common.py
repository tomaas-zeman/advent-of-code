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
    def __init__(self, cards: str, bid: int, enable_jokers=False):
        self.cards = cards
        self.card_values = [-1 if c == "J" and enable_jokers else card_order.index(c) for c in self.cards]
        self.bid = bid
        self.rank = self.get_rank_with_jokers(cards) if enable_jokers else self.get_rank(cards)

    def get_rank(self, cards: str) -> Rank:
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

    def get_rank_with_jokers(self, cards: str) -> Rank:
        count = Counter(cards.replace("J", ""))
        most_common = count.most_common(1)

        # Edge case - all jokers
        if len(most_common) == 0:
            return Rank.FIVE_OF_A_KIND

        return self.get_rank(cards.replace("J", most_common[0][0]))

    @staticmethod
    def compare(one: Hand, two: Hand) -> int:
        if one.rank == two.rank:
            for i in range(len(one.cards)):
                if one.card_values[i] == two.card_values[i]:
                    continue
                return one.card_values[i] - two.card_values[i]
            return 0
        return one.rank.value - two.rank.value


def parse_hands(data: list[str], enable_jokers: bool = False) -> list[Hand]:
    hands = []
    for line in data:
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid), enable_jokers=enable_jokers))
    return hands


def calculate_winnings(hands: list[Hand]) -> int:
    ranked_hands = sorted(hands, key=cmp_to_key(Hand.compare))
    return sum([(i + 1) * hand.bid for i, hand in enumerate(ranked_hands)])
