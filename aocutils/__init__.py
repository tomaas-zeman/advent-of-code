from __future__ import annotations

import os
import time
from enum import Enum
from random import randint
from typing import Any, Generic, Iterator, TypeVar, Callable

import matplotlib.pyplot as plot
import networkx as nx
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Generic type alias
# (row, column)
# (x, y, z)
Point = tuple[int, ...]


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


def as_ints(list: list[str] | Iterator[str] | tuple[str, ...]):
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
            for col_index, value in enumerate(row):
                items.append((value, row_index, col_index))
        return items

    @staticmethod
    def are_neighbors(a: Point, b: Point):
        return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

    @staticmethod
    def is_valid_point(point: Point, matrix: np.ndarray):
        return 0 <= point[0] < matrix.shape[0] and 0 <= point[1] < matrix.shape[1]

    @staticmethod
    def plot_3d_as_cubes(matrix: np.ndarray):
        figure = plot.figure()
        ax = figure.add_subplot(111, projection="3d")

        cube_vertices = np.array(
            [[0, 0, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0], [1, 1, 0], [1, 1, 1], [0, 1, 1]]
        )

        cube_sides = [
            [cube_vertices[i] for i in [0, 1, 2, 3]],
            [cube_vertices[i] for i in [4, 5, 6, 7]],
            [cube_vertices[i] for i in [0, 3, 7, 4]],
            [cube_vertices[i] for i in [1, 2, 6, 5]],
            [cube_vertices[i] for i in [0, 1, 5, 4]],
            [cube_vertices[i] for i in [2, 3, 7, 6]],
        ]

        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                for z in range(matrix.shape[2]):
                    if matrix[x, y, z]:
                        faces = [np.array(face) + [x, y, z] for face in cube_sides]
                        cube = Poly3DCollection(faces, alpha=0.5, edgecolor="k", facecolors="bgrcmy"[randint(0, 5)])
                        ax.add_collection3d(cube)

        ax.set_xlim(0, matrix.shape[0])
        ax.set_ylim(0, matrix.shape[1])
        ax.set_zlim(0, matrix.shape[2])
        ax.set_box_aspect([1, 1, 1])

        plot.show()


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


class _Console:
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

    def __getattr__(self, color: str):
        def apply(text):
            print(Console.with_color(text, getattr(Console.Color, color.upper())))

        return apply

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def with_color(text: str, color: str | None):
        if color is None:
            return text
        return f"\x1B[{color}m{text}\x1B[0m"


Console = _Console()

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
    def opposite(cls, direction: Direction):
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

    @classmethod
    def infer_direction(cls, p1: Point, p2: Point):
        diff = (p1[0] - p2[0], p1[1] - p2[1])
        if all(x != 0 for x in diff):
            raise AttributeError("Unsupported diagonal direction")
        if diff[0] != 0:
            return Direction.UP if diff[0] > 0 else Direction.DOWN
        if diff[1] != 0:
            return Direction.LEFT if diff[1] > 0 else Direction.RIGHT


class Tuple:
    @staticmethod
    def add(*tuples: tuple[int, ...]):
        return tuple(map(sum, zip(*tuples)))

    @staticmethod
    def sub(*tuples: tuple[int, ...]):
        return tuple(map(lambda t: t[0] - t[1], zip(*tuples)))

    @staticmethod
    def mul(t: tuple[int, ...], multiplier: int):
        return tuple(n * multiplier for n in t)


##########
# Graphs #
##########


class Graph:
    @staticmethod
    def draw(graph: nx.Graph, edge_labels=False):
        layout = nx.spring_layout(graph, scale=2, seed=255)
        nx.draw(graph, layout, with_labels=True, node_size=2000)

        if edge_labels:
            nx.draw_networkx_edge_labels(
                graph, layout, edge_labels={(n1, n2): d["weight"] for n1, n2, d in graph.edges(data=True)}
            )

        plot.show()
