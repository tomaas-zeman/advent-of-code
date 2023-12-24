from __future__ import annotations
from enum import Enum
from typing import Any, Generic, Iterator, TypeVar, Callable
import time
import os
import numpy as np

# (row, column) generic type alias
Point = tuple[int, int]

##############
# DECORATORS #
##############


def memoize(fn):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    def clear_cache():
        cache.clear()

    wrapper.clear_cache = clear_cache
    return wrapper


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Computation took {end_time - start_time:.3f} seconds")
        return result

    return wrapper


def raw_input(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    wrapper.uses_raw_input = True
    return wrapper


#########
# LISTS #
#########

T = TypeVar("T")
U = TypeVar("U")


def flatten(list_of_lists: list[list[T]]):
    return [item for sublist in list_of_lists for item in sublist]


def as_ints(list: list[str] | Iterator[str]):
    return [int(x) for x in list]


############
# MATRICES #
############


class Numpy:
    @staticmethod
    def print_matrix(matrix: np.ndarray, str_formatter: Callable[[str], str] = lambda x: x, separator=""):
        print(np.array2string(matrix, separator=separator, formatter={"str_kind": str_formatter}))  # type: ignore

    @staticmethod
    def from_input(data: list[str], dtype: T, value_convertor: Callable[[str], T]) -> np.ndarray[T]:
        matrix = np.empty((len(data), len(data[0])), dtype=dtype)
        for row_index, row in enumerate(data):
            for col_index, col in enumerate(row):
                matrix[row_index][col_index] = value_convertor(col)
        return matrix

    @staticmethod
    def from_input_as_str(data: list[str]):
        return Numpy.from_input(data, np.dtype("U100"), lambda x: x)

    @staticmethod
    def from_input_as_int(data: list[str]):
        return Numpy.from_input(data, np.uint8, int)

    @staticmethod
    def neighbors_of(point: tuple[int, int], matrix: np.ndarray, include_diagonals: bool = False):
        return [
            matrix[n] for n in Numpy.valid_neighbor_positions_of(point, matrix, include_diagonals=include_diagonals)
        ]

    @staticmethod
    def all_neighbor_positions_of(point: Point, include_diagonals: bool = False):
        positions = [
            (point[0] - 1, point[1]),
            (point[0] + 1, point[1]),
            (point[0], point[1] - 1),
            (point[0], point[1] + 1),
        ]
        if include_diagonals:
            positions += [
                (point[0] - 1, point[1] - 1),
                (point[0] - 1, point[1] + 1),
                (point[0] + 1, point[1] - 1),
                (point[0] + 1, point[1] + 1),
            ]
        return positions

    @staticmethod
    def valid_neighbor_positions_of(point: Point, matrix: np.ndarray, include_diagonals: bool = False):
        return [
            p
            for p in Numpy.all_neighbor_positions_of(point, include_diagonals=include_diagonals)
            if 0 <= p[0] < matrix.shape[0] and 0 <= p[1] < matrix.shape[1]
        ]

    @staticmethod
    def all_items(matrix: np.ndarray):
        items: list[tuple[Any, int, int]] = []
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                items.append((matrix[row_index, col_index], row_index, col_index))
        return items

    @staticmethod
    def are_neighbors(a: Point, b: Point):
        return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

    @staticmethod
    def is_valid_point(point: Point, matrix: np.ndarray):
        return 0 <= point[0] < matrix.shape[0] and 0 <= point[1] < matrix.shape[1]


#########
# TREES #
#########


class GenericNode(Generic[T]):
    def __init__(self, id: int, value: T):
        self.id = id
        self.value = value
        self.parent = None
        self.children: set[GenericNode[T]] = set()

    def set_parent(self, parent: GenericNode[T]):
        self.parent = parent

    def set_children(self, children: set[GenericNode[T]]):
        self.children = children

    def __eq__(self, other: GenericNode[T]):
        return self.id == other.id

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return str(self.value)


class BinaryTreeNode(Generic[T, U]):
    def __init__(self, id: U, value: T):
        self.id = id
        self.value = value
        self.left: BinaryTreeNode[T, U] | None = None
        self.right: BinaryTreeNode[T, U] | None = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def set_left(self, left: BinaryTreeNode[T, U]):
        self.left = left

    def set_right(self, right: BinaryTreeNode[T, U]):
        self.right = right


###########
# CONSOLE #
###########


class Console:
    class Color:
        RED = "0;31"
        GREEN = "0;32"
        YELLOW = "0;33"
        BLUE = "0;34"
        PURPLE = "0;35"
        CYAN = "0;36"
        LIGHT_GRAY = "0;37"
        DARK_GRAY = "1;30"
        BOLD_RED = "1;31"
        BOLD_CYAN = "1;32"
        BOLD_YELLOW = "1;33"
        BOLD_BLUE = "1;34"
        BOLD_PURPLE = "1;35"
        BOLD_CYAN = "1;36"
        WHITE = "1;37"

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def with_color(text: str, color: str | None):
        if color is None:
            return text
        return f"\x1B[{color}m{text}\x1B[0m"


########
# MISC #
########


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @classmethod
    def all(cls):
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT]

    @classmethod
    def opposite(cls, direction):
        return {
            cls.UP: cls.DOWN,
            cls.DOWN: cls.UP,
            cls.LEFT: cls.RIGHT,
            cls.RIGHT: cls.LEFT,
        }[direction]

    @classmethod
    def coord_change(cls, direction: Direction, factor=1) -> tuple[int, int]:
        # (row, col)
        return {
            cls.UP: (-1 * factor, 0),
            cls.DOWN: (1 * factor, 0),
            cls.LEFT: (0, -1 * factor),
            cls.RIGHT: (0, 1 * factor),
        }[direction]

    @classmethod
    def from_string(cls, string: str):
        return {
            "U": Direction.UP,
            "D": Direction.DOWN,
            "L": Direction.LEFT,
            "R": Direction.RIGHT,
        }[string]


class Coord:
    @staticmethod
    def add(*points: Point):
        return tuple(map(sum, zip(*points)))
