import re
from typing import List, Dict, Tuple


def parse_bags(data: List[str]) -> Dict[str, Tuple[str, int]]:
    bags = {}
    for line in data:
        [source, rest] = line.replace('.', '').split(' bags contain ')

        if rest == 'no other bags':
            bags[source] = None
            continue

        bags_in_source = [bag.strip() for bag in re.sub('[ ]bags?', '', rest).split(',')]
        bags[source] = {(bag[2:], int(bag[0:1])) for bag in bags_in_source}
    return bags


def compute_bags_in_series(bags: Dict[str, Tuple[str, int]], bag_name: str):
    if bags[bag_name] is None:
        return 1
    # +1 for the current bag
    return 1 + sum([
        sub_bag_count * compute_bags_in_series(bags, sub_bag_name)
        for [sub_bag_name, sub_bag_count] in bags[bag_name]
    ])


def run(data: List[str]):
    bags = parse_bags(data)
    return compute_bags_in_series(bags, 'shiny gold') - 1  # -1 for 'shiny gold'
