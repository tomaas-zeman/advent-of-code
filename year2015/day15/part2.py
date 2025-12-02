from collections import Counter
from itertools import combinations_with_replacement
from math import prod

from year2015.day15.common import parse


def run(data: list[str], is_test: bool):
    ingredients = parse(data)

    score = 0

    for c in combinations_with_replacement(ingredients, 100):
        property_scores: list[int] = [0 for _ in range(5)]

        for ingredient, count in Counter(c).items():
            for i in range(5):
                property_scores[i] += ingredient[i + 1] * count

        if property_scores[-1] == 500:
            score = max(prod([s if s > 0 else 0 for s in property_scores[:-1]]), score)

    return score


test_result = 57600000
