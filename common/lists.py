from typing import List


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def as_ints(list: List[str]):
    return [int(x) for x in list]
