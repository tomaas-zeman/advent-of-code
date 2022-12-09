from __future__ import annotations
from typing import Generic, TypeVar, Callable, Any
from uuid import uuid4

from common.lists import flatten

V = TypeVar("V")
F = TypeVar("F")


class Point(Generic[V, F]):
    def __init__(self, row: int, column: int, value: V | None = None, id: int | None = None):
        self.row = row
        self.column = column
        self.value = value if value is not None else uuid4()
        self.id = id
        self.matrix = None
        self.flag = None

    def set_flag(self, flag: F):
        self.flag = flag

    def set_matrix(self, matrix: Matrix):
        self.matrix = matrix

    def set_value(self, value: V):
        self.value = value

    def neighbors(self, diagonals=False) -> list[Point]:
        if self.matrix is None:
            return []
        return self.matrix.neighbors_of(self, diagonals)

    def is_neighbor_of(self, other: Point):
        return abs(self.row - other.row) <= 1 and abs(self.column - other.column) <= 1

    def __eq__(self, other: Point):
        if self.id is not None and other.id is not None:
            return self.id == other.id
        return self.row == other.row and self.column == other.column

    def __lt__(self, other):
        if self.id is not None and other.id is not None:
            return self.id - other.id
        return self.row - other.row + self.column - other.column < 0

    def __hash__(self):
        return hash((self.row, self.column))

    def __str__(self):
        return str(self.value)


class Matrix(Generic[V, F]):
    def __init__(self, rows: list[list[Point]]):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])
        self.mapped_by_id = {point_id: point for point_id, point in enumerate(self.all_points())}

    def point_by_id(self, point_id: int):
        return self.mapped_by_id[point_id]

    def point_at(self, row: int, column: int):
        if row < 0 or column < 0:
            return None
        try:
            return self.rows[row][column]
        except:
            return None

    def neighbors_of(self, point: Point, diagonals=False):
        values = [
            self.point_at(point.row, point.column - 1),
            self.point_at(point.row, point.column + 1),
            self.point_at(point.row - 1, point.column),
            self.point_at(point.row + 1, point.column),
        ]

        if diagonals:
            values = values + [
                self.point_at(point.row - 1, point.column - 1),
                self.point_at(point.row - 1, point.column + 1),
                self.point_at(point.row + 1, point.column - 1),
                self.point_at(point.row + 1, point.column + 1),
            ]

        return [v for v in values if v is not None]

    def all_points(self) -> list[Point[V, F]]:
        return flatten(self.rows)

    def __str__(self):
        return "\n".join([" ".join([str(p) for p in row]) for row in self.rows])


def matrix_from_data(data: list[str], item_sep=None, convert_value: Callable[[str], V] = lambda x: x) -> Matrix[V, Any]:
    rows = []

    for line_index, line in enumerate(data):
        line = line.strip()
        items = line if item_sep is None else line.split(item_sep)
        rows.append(
            [
                Point(line_index, item_index, convert_value(item), (line_index * len(items)) + item_index)
                for item_index, item in enumerate(items)
            ]
        )

    matrix = Matrix(rows)

    # add backwards reference to matrix for all points
    for point in matrix.all_points():
        point.matrix = matrix

    return matrix


def matrix_from_file(file_path: str, item_sep=None, convert_value=lambda x: int(x)) -> Matrix:
    """Deprecated. Use #matrix_from_data() instead"""
    with open(file_path) as file:
        data = [line.strip() for line in file.readlines()]
        return matrix_from_data(data, item_sep, convert_value)
