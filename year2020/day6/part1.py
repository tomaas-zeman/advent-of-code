from typing import List


def run(data: List[str]):
    groups = []

    yes_answers = set()
    for line in data:
        if len(line) == 0:
            groups.append(yes_answers)
            yes_answers = set()
            continue
        yes_answers.update([answer for answer in line])
    groups.append(yes_answers)

    return sum([len(group) for group in groups])
