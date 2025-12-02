from aocutils import flatten
from year2020.day21.common import parse, analyze_input


def run(data: list[str], is_test: bool):
    foods = parse(data)
    _, ingredients_without_allergens = analyze_input(foods)

    return sum([1 for i in flatten([f.ingredients for f in foods]) if i in ingredients_without_allergens])


test_result = 5
