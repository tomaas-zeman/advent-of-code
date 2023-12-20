from year2023.day19.common import parse


def run(data: list[str], is_test: bool):
    workflows, parts = parse(data)

    result = 0
    for part in parts:
        next = workflows["in"].next(part)
        while next not in "AR":
            next = workflows[next].next(part)
        if next == "A":
            result += sum(part.props.values())

    return result
