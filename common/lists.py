##########################################
# DEPRECATED: use 'common.utils' instead #
##########################################
from typing import TypeVar, Iterator

T = TypeVar("T")


def flatten(list_of_lists: list[list[T]]) -> list[T]:
    return [item for sublist in list_of_lists for item in sublist]


def as_ints(list: list[str] | Iterator[str]):
    return [int(x) for x in list]
