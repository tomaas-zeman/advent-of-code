from __future__ import annotations

import sys
from queue import PriorityQueue
from typing import Callable, Any, Generic, TypeVar

from aocutils import flatten
from aocutils.matrix import matrix_from_file, matrix_from_data

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


class DijkstraGraph:
    def __init__(self, points: int):
        self.points = points
        self.edges = {}

    def add_edge(self, point1_id: int, point2_id: int, cost: int):
        if self.edges.get(point1_id, None) is None:
            self.edges[point1_id] = {}
        self.edges[point1_id][point2_id] = cost


def dijkstra(matrix: Matrix, graph: DijkstraGraph, starting_point_id: int):
    distances = {n: sys.maxsize for n in range(graph.points)}
    distances[starting_point_id] = 0

    queue = PriorityQueue[tuple[int, MatrixPoint]]()
    queue.put((0, matrix.point_by_id(starting_point_id)))

    while not queue.empty():
        [_, point] = queue.get()

        # flag
        # False=not visited
        # True=visited
        point.flag = True
        for neighbor in [p for p in matrix.neighbors_of(point) if not p.flag]:
            new_distance = distances[point.id] + graph.edges[neighbor.id][point.id]
            current_distance = distances[neighbor.id]
            if new_distance < current_distance:
                distances[neighbor.id] = new_distance
                queue.put((distances[neighbor.id], matrix.point_by_id(neighbor.id)))

    return distances


def parse(data: list[str]):
    return matrix_from_data(data, convert_value=lambda x: int(x))
