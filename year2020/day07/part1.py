import re
from collections import deque


def parse_bags(data: list[str]) -> dict[str, list[str]]:
    bags = {}
    for line in data:
        [source, rest] = line.replace(".", "").split(" bags contain ")

        if rest == "no other bags":
            bags[source] = None
            continue

        for bag in [bag.strip()[2:] for bag in re.sub("[ ]bags?", "", rest).split(",")]:
            if bag not in bags:
                bags[bag] = []
            if bags[bag] is not None:
                bags[bag].append(source)

    return bags


def run(data: list[str], is_test: bool):
    can_hold_shiny_gold_bag = set()

    bags = parse_bags(data)
    stack = deque(bags["shiny gold"])
    while len(stack) > 0:
        bag = stack.pop()
        can_hold_shiny_gold_bag.add(bag)
        stack.extend(bags.get(bag, []))

    return len(can_hold_shiny_gold_bag)
