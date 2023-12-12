import itertools
import re


def create_spring_combinations(springs: str, pattern: re.Pattern):
    possible_replacements = itertools.product([".", "#"], repeat=springs.count("?"))
    for replacement in possible_replacements:
        result = re.sub("[?]", "{}", springs).format(*replacement)
        if pattern.match(result):
            yield result


def run(data: list[str], is_test: bool):
    combinations = 0

    for line in data:
        springs = "?".join([line.split(" ")[0] for _ in range(5)])
        conditions = line.split(" ")[1].split(",")*5
        pattern = re.compile(f'^[?.]*{"[?.]+".join(["#{" + n + "}" for n in conditions])}[?.]*$')
        combinations += len(list(c for c in create_spring_combinations(springs, pattern)))

    return combinations
