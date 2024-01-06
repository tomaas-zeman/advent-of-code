import re

from aocutils import memoize, split_list_by

Rules = dict[str, list[str] | str]


# Just a perf optimization (3x speedup)
def invalid_combination(prefix: str, messages: list[str]):
    @memoize
    def invalid_combination_memoized(memoized_prefix: str):
        return not any(m.startswith(memoized_prefix) for m in messages)

    return invalid_combination_memoized(prefix)


def parse(data: list[str]) -> tuple[Rules, list[str]]:
    rule_group, messages = split_list_by(data, "")

    rules = {}
    for line in rule_group:
        id, next = line.split(": ")
        if match := re.match(r'"([ab])"', next):
            rules[id] = match.group(1)
        else:
            rules[id] = next.split(" ")

    return rules, messages


def compute(rules: Rules, messages: list[str]):
    results = []

    states: list[tuple[list[str] | str, int]] = [(rules["0"], 0)]
    while states:
        state, index = states.pop()

        if invalid_combination("".join(state[:index]), messages):
            continue

        if all(c.isalpha() for c in state):
            results.append(state)
            continue

        next = rules[state[index]]

        if isinstance(next, str):
            state[index] = next
            states.append((state, index + 1))
            continue

        for part in split_list_by(next, "|"):
            states.append((state[:index] + part + state[index + 1 :], index))

    return len(set(["".join(r) for r in results]).intersection(set(messages)))
