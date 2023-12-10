from __future__ import annotations
from typing import Any, Generic, Iterator, TypeVar, Callable
import time
import os
import numpy as np


##############
# DECORATORS #
##############


def memoize(fn):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

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

V = TypeVar("V")
F = TypeVar("F")


class MatrixPoint(Generic[V, F]):
    def __init__(self, row: int, col: int, value: V, id: int = 0, eq_by_id: bool = False):
        self.row = row
        self.col = col
        self.value = value
        self.id = id
        self.flag = None
        self.eq_by_id = eq_by_id

    def set_flag(self, flag: F):
        self.flag = flag

    def set_value(self, value: V):
        self.value = value

    def is_neighbor_of(self, other: MatrixPoint[V, F]):
        return abs(self.row - other.row) <= 1 and abs(self.col - other.col) <= 1

    def __eq__(self, other: MatrixPoint[V, F]):
        if self.eq_by_id and self.id is not None and other.id is not None:
            return self.id == other.id
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __str__(self):
        return str(self.value)


P = TypeVar("P", bound=MatrixPoint)


class Matrix(Generic[P]):
    def __init__(self, rows: list[list[P]]):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.points_by_id = {point_id: point for point_id, point in enumerate(self.all_points())}

    def point_by_id(self, point_id: int):
        return self.points_by_id[point_id]

    def point_at(self, row: int, col: int):
        return self.rows[row][col]

    def __point_at(self, row: int, col: int):
        if row < 0 or col < 0:
            return None
        try:
            return self.rows[row][col]
        except:
            return None

    def neighbors_of(self, point: P, include_diagonals=False):
        values = [
            self.__point_at(point.row, point.col - 1),
            self.__point_at(point.row, point.col + 1),
            self.__point_at(point.row - 1, point.col),
            self.__point_at(point.row + 1, point.col),
        ]

        if include_diagonals:
            values = values + [
                self.__point_at(point.row - 1, point.col - 1),
                self.__point_at(point.row - 1, point.col + 1),
                self.__point_at(point.row + 1, point.col - 1),
                self.__point_at(point.row + 1, point.col + 1),
            ]

        return [v for v in values if v is not None]

    def all_points(self):
        return flatten(self.rows)

    def __str__(self):
        return "\n".join([" ".join([str(p) for p in row]) for row in self.rows])

    @staticmethod
    def from_input(
        data: list[str], item_sep=None, convert_value: Callable[[str], V] = lambda x: x
    ) -> Matrix[MatrixPoint[V, Any]]:
        rows = []

        for row_index, line in enumerate(data):
            line = line.strip()
            items = line if item_sep is None else line.split(item_sep)
            rows.append(
                [
                    MatrixPoint(row_index, col_index, convert_value(item), (row_index * len(items)) + col_index)
                    for col_index, item in enumerate(items)
                ]
            )

        return Matrix(rows)


class Numpy:
    # (row, column) type for Numpy
    Point = tuple[int, int]

    @staticmethod
    def print_matrix(matrix: np.ndarray, str_formatter: Callable[[str], str] = lambda x: x):
        print(np.array2string(matrix, separator="", formatter={"str_kind": str_formatter}))  # type: ignore

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
