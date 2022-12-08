import re

struct = dict[str, set[tuple[str, int]] | None]


def parse_bags(data: list[str]):
    bags: struct = {}
    for line in data:
        [source, rest] = line.replace(".", "").split(" bags contain ")

        if rest == "no other bags":
            bags[source] = None
            continue

        bags_in_source = [bag.strip() for bag in re.sub("[ ]bags?", "", rest).split(",")]
        bags[source] = {(bag[2:], int(bag[0:1])) for bag in bags_in_source}
    return bags


def compute_bags_in_series(bags: struct, bag_name: str):
    series = bags[bag_name]
    if series is None:
        return 1
    # +1 for the current bag
    return 1 + sum(
        [sub_bag_count * compute_bags_in_series(bags, sub_bag_name) for [sub_bag_name, sub_bag_count] in series]
    )


def run(data: list[str], raw_data: list[str]):
    bags = parse_bags(data)
    return compute_bags_in_series(bags, "shiny gold") - 1  # -1 for 'shiny gold'
