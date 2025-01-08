import re
from typing import Callable


expected = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(data: list[str]) -> list[dict[str, int]]:
    things = [
        "children",
        "cats",
        "samoyeds",
        "pomeranians",
        "akitas",
        "vizslas",
        "goldfish",
        "trees",
        "cars",
        "perfumes",
    ]
    aunts = []

    for line in data:
        aunt = {}
        for thing in things:
            if m := re.search(f"{thing}: (\d+)", line):
                aunt[thing] = int(m.group(1))
        aunts.append(aunt)

    return aunts


def find_aunt_suzie(aunts: list[dict[str, int]], validator: Callable[[str, int], bool]):
    for i in range(len(aunts)):
        aunt = aunts[i]
        if all(validator(thing, count) for thing, count in aunt.items()):
            return i + 1
