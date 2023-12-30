from typing import Type

import networkx as nx

from aocutils import Numpy, Point, Direction

slopes = {Direction.DOWN: "v", Direction.UP: "^", Direction.LEFT: "<", Direction.RIGHT: ">"}


def create_graph(data: list[str], new_graph: Type[nx.Graph]) -> tuple[nx.Graph, Point, Point]:
    maze = Numpy.from_input_as_str(data)
    start: Point = (0, 1)
    end: Point = (maze.shape[0] - 1, maze.shape[1] - 2)

    graph = new_graph()
    graph.add_node(start)
    graph.add_node(end)

    crossroads: set[Point] = set()
    visited: set[Point] = set()

    stack = [(start, 0, start)]
    while len(stack) > 0:
        point, length, prev_point = stack.pop()
        visited.add(point)

        if point == end:
            graph.add_edge(prev_point, point, weight=length)
            continue

        next_points = [p for p in Numpy.valid_neighbor_positions_of(point, maze) if maze[p] != "#"]

        if is_crossroad := len(next_points) > 2 and point not in crossroads:
            crossroads.add(point)
            graph.add_node(point)
            graph.add_edge(prev_point, point, weight=length)

        for next_point in next_points:
            if next_point in visited:
                if next_point in crossroads and next_point != prev_point:
                    graph.add_edge(prev_point, next_point, weight=length + 1)
            elif (
                maze[next_point] not in slopes.values()
                or slopes[Direction.infer_direction(point, next_point)] == maze[next_point]
            ):
                stack.append((next_point, 1 if is_crossroad else length + 1, point if is_crossroad else prev_point))

    return graph, start, end
