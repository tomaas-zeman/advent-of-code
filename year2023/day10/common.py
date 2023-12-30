from itertools import permutations

import numpy as np

from aocutils import Direction, Numpy


class Pipe:
    def __init__(self, openings: list[Direction]):
        self.direction_change = {p[0]: p[1] for p in permutations(openings, 2)}

    def flows_to(self, flows_from: Direction) -> Direction:
        return self.direction_change[Direction.opposite(flows_from)]

    def allows_flow_from(self, direction: Direction) -> bool:
        return Direction.opposite(direction) in self.direction_change


PIPES = {
    "|": Pipe([Direction.UP, Direction.DOWN]),
    "-": Pipe([Direction.RIGHT, Direction.LEFT]),
    "L": Pipe([Direction.UP, Direction.RIGHT]),
    "J": Pipe([Direction.UP, Direction.LEFT]),
    "7": Pipe([Direction.DOWN, Direction.LEFT]),
    "F": Pipe([Direction.DOWN, Direction.RIGHT]),
    ".": Pipe([]),
}


def initial_steps(maze: np.ndarray, start: tuple[int, int]):
    initial_steps = []
    for direction in Direction.all():
        next_point = tuple(map(sum, zip(start, Direction.coord_change(direction))))
        if not Numpy.is_valid_point(next_point, maze):
            continue

        next_pipe = PIPES[maze[next_point]]
        if next_pipe.allows_flow_from(direction):
            initial_steps.append((next_point, next_pipe.flows_to(direction)))

    return initial_steps


def walk_path(data: list[str]):
    maze = Numpy.from_input_as_str(data)
    start = np.argwhere(maze == "S")[0]
    visited = np.full(maze.shape, False)
    path = initial_steps(maze, start)

    # visit initial nodes
    for point, _ in path + [start]:
        visited[point] = True

    steps = 1
    while any(p[0] != path[0][0] for p in path):
        next_path_positions = []
        for point, direction in path:
            next_point = tuple(map(sum, zip(point, Direction.coord_change(direction))))
            next_pipe = PIPES[maze[next_point]]
            next_path_positions.append((next_point, next_pipe.flows_to(direction)))
            visited[next_point] = True

        path = next_path_positions
        steps += 1

    return maze, visited, steps
