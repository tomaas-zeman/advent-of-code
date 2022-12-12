from queue import PriorityQueue
from common.matrix import Matrix, Point
import sys


class Graph:
    def __init__(self, points: int):
        self.points = points
        self.edges = {}

    def add_edge(self, point1_id: int, point2_id: int, cost: int):
        if self.edges.get(point1_id, None) is None:
            self.edges[point1_id] = {}
        self.edges[point1_id][point2_id] = cost


def dijkstra(matrix: Matrix, graph: Graph, starting_point_id: int):
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
