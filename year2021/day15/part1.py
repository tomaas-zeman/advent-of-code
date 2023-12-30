from year2021.day15.common import dijkstra, DijkstraGraph, parse


def compute_risk(matrix):
    graph = DijkstraGraph(matrix.num_rows * matrix.num_cols)

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


def run(data: list[str], is_test: bool):
    return compute_risk(parse(data))
