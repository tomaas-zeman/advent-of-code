from queue import PriorityQueue

from day15.common import get_data


class Graph:
    def __init__(self, point_num):
        self.point_num = point_num
        self.edges = {}

    def add_edge(self, point_1, point_2, cost):
        if self.edges.get(point_1, None) is None:
            self.edges[point_1] = {}
        self.edges[point_1][point_2] = cost


def dijkstra(matrix, graph, starting_point):
    distances = {n: float('inf') for n in range(graph.point_num)}
    distances[starting_point] = 0

    queue = PriorityQueue()
    queue.put((0, matrix.point_by_id(starting_point)))

    while not queue.empty():
        [_, point] = queue.get()
        point.visited = True
        for neighbour in [p for p in matrix.neighbours_of(point) if not p.visited]:
            new_distance = distances[point.id] + graph.edges[neighbour.id][point.id]
            current_distance = distances[neighbour.id]
            if new_distance < current_distance:
                distances[neighbour.id] = new_distance
                queue.put((distances[neighbour.id], matrix.point_by_id(neighbour.id)))

    return distances


def add_visited_feature_to_points(matrix):
    for point in matrix.all_points():
        point.visited = False


def compute_risk(matrix):
    add_visited_feature_to_points(matrix)

    graph = Graph(matrix.num_rows * matrix.num_cols)

    for row_index in range(matrix.num_rows):
        for column_index in range(matrix.num_cols):
            point = matrix.point_at(row_index, column_index)

            if column_index < matrix.num_cols - 1:
                point_id_right = point.id + 1
                point_right = matrix.point_at(row_index, column_index + 1)
                graph.add_edge(point.id, point_id_right, point.value)
                graph.add_edge(point_id_right, point.id, point_right.value)

            if row_index < matrix.num_rows - 1:
                point_id_down = point.id + matrix.num_cols
                point_down = matrix.point_at(row_index + 1, column_index)
                graph.add_edge(point.id, point_id_down, point.value)
                graph.add_edge(point_id_down, point.id, point_down.value)

    return dijkstra(matrix, graph, 0)[matrix.num_rows * matrix.num_cols - 1]


def run():
    return compute_risk(get_data())
