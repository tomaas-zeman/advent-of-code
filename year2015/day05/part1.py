from itertools import pairwise
import re


def is_nice(string: str) -> bool:
    if len(re.findall("([aeiou])", string)) < 3:
        return False
    if len([pair for pair in pairwise(string) if pair[0] == pair[1]]) == 0:
        return False
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in string:
            return False
    return True


def run(data: list[str], is_test: bool):
    return len([s for s in data if is_nice(s)])
