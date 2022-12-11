from itertools import groupby
from common.lists import as_ints


def get_elves(data: list[str]) -> list[int]:
    return [sum(as_ints(calories)) for key, calories in groupby(data, key=lambda x: x != "") if key]
