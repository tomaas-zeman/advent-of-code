from collections import deque
from typing import Callable, Generic, TypeVar

from aocutils.matrix import Point

T = TypeVar("T")


class BfsPath(Generic[T]):
    def __init__(self, nodes: list[T]) -> None:
        self.nodes = nodes

    def add_node(self, node: T):
        self.nodes.append(node)

    def copy(self):
        return BfsPath(self.nodes[:])


def bfs(starting_point: Point, ending_point: Point, expansion: Callable[[Point], list[Point]]):
    queue = deque([BfsPath([starting_point])])

    while len(queue) > 0:
        path = queue.pop()
        last_point = path.nodes[-1]

        if last_point.flag:
            continue
        else:
            last_point.flag = True

        if last_point.id == ending_point.id:
            return path

        for point in expansion(last_point):
            if point not in path.nodes:
                new_path = path.copy()
                new_path.add_node(point)
                queue.appendleft(new_path)

    return None


def value_of(char: str):
    if char == "S":
        return ord("a")
    if char == "E":
        return ord("z")
    return ord(char)


def expansion(p: Point):
    return [n for n in p.neighbors() if value_of(n.value) - value_of(p.value) <= 1 and not n.flag]
