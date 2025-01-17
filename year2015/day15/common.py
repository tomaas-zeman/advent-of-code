import re

from aocutils import as_ints


# (name, capacity, durability, flavor, texture, calories)
Ingredient = tuple[str, int, int, int, int, int]


def parse(data: list[str]):
    ingredients: list[Ingredient] = []

    for line in data:
        name = line.split(":")[0]
        ingredients.append((name, *as_ints(re.findall("(-?\d+)", line))))

    return ingredients
