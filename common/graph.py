##########################################
# DEPRECATED: use 'common.utils' instead #
##########################################
from queue import PriorityQueue
from common.matrix import Matrix, Point
import sys
from collections import deque
from typing import Callable, Generic, TypeVar


T = TypeVar("T")

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

    queue = PriorityQueue[tuple[int, Point]]()
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


class BfsPath(Generic[T]):
    def __init__(self, nodes: list[T]) -> None:
        self.nodes = nodes

    def add_node(self, node: T):
        self.nodes.append(node)

    def copy(self):
        return BfsPath(self.nodes[:])

    def __str__(self) -> str:
        return ">".join([str(p.id) for p in self.nodes])


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
