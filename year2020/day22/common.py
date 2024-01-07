from aocutils import as_ints, split_list_by


def parse(data: list[str]) -> list[list[int]]:
    return [as_ints(group[1:])[::-1] for group in split_list_by(data, "")]


def compute_result(players: list[list[int]]):
    return sum((i + 1) * value for i, value in list(enumerate(max(players)))[::-1])
