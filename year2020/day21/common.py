import re
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce

from aocutils import split_list_by, flatten


@dataclass
class Food:
    ingredients: list[str]
    allergens: list[str]


def parse(data: list[str]):
    return [Food(*split_list_by(re.findall(r"(\w+)", line), "contains")) for line in data]


def map_by_allergen(foods: list[Food]) -> dict[str, list[Food]]:
    food_by_allergen = defaultdict(list)
    for food in foods:
        for allergen in food.allergens:
            food_by_allergen[allergen].append(food)
    return food_by_allergen


def intersect_allergens_by_food(all_foods: list[Food]) -> dict[str, list[str]]:
    intersections = {}
    for allergen, foods in map_by_allergen(all_foods).items():
        intersections[allergen] = list(
            reduce(lambda acc, f: acc.intersection(f.ingredients), foods, set(foods[0].ingredients))
        )
    return intersections


def analyze_input(foods: list[Food]):
    allergens_by_food = intersect_allergens_by_food(foods)

    ingredients_with_allergens = set(flatten(allergens_by_food.values()))

    ingredients_without_allergens = set(flatten([f.ingredients for f in foods]))
    ingredients_without_allergens.difference_update(ingredients_with_allergens)

    return allergens_by_food, ingredients_without_allergens
