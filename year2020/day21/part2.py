from aocutils import flatten
from year2020.day21.common import parse, analyze_input


def get_unprocessed_allergen(allergens: dict[str, set[str]], processed_allergens: set[str]):
    for allergen in sorted(allergens.keys(), key=lambda key: len(allergens[key])):
        if allergen not in processed_allergens:
            return allergen


def remove_ingredient_from_others(ingredient: str, current_allergen: str, allergens_by_food: dict[str, list[str]]):
    for key in [k for k in allergens_by_food.keys() if k != current_allergen]:
        if ingredient in allergens_by_food[key]:
            allergens_by_food[key].remove(ingredient)


def run(data: list[str], is_test: bool):
    foods = parse(data)
    allergens_by_food, _ = analyze_input(foods)

    processed_allergens = set()
    while len(processed_allergens) < len(allergens_by_food):
        allergen = get_unprocessed_allergen(allergens_by_food, processed_allergens)
        ingredient = allergens_by_food[allergen][0]
        remove_ingredient_from_others(ingredient, allergen, allergens_by_food)
        processed_allergens.add(allergen)

    return ",".join(flatten([allergens_by_food[allergen] for allergen in sorted(allergens_by_food.keys())]))


test_result = 'mxmxvkd,sqjhc,fvjkl'
