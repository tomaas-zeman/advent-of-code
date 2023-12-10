import numpy as np
from enum import Enum
from itertools import permutations
from common.utils import Numpy


class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, -1)
    WEST = (0, 1)


class Pipe:
    def __init__(self, openings: list[Direction]):
        self.direction_change = {p[0]: p[1] for p in permutations(openings, 2)}

    def flows_to(self, flows_from: Direction) -> Direction:
        return self.direction_change[Pipe.output_to_input_direction(flows_from)]

    def allows_flow_from(self, direction: Direction) -> bool:
        return Pipe.output_to_input_direction(direction) in self.direction_change

    @staticmethod
    def output_to_input_direction(direction) -> Direction:
        match direction:
            case Direction.NORTH:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.NORTH
            case Direction.EAST:
                return Direction.WEST
            case Direction.WEST:
                return Direction.EAST


PIPES = {
    "|": Pipe([Direction.NORTH, Direction.SOUTH]),
    "-": Pipe([Direction.EAST, Direction.WEST]),
    "L": Pipe([Direction.NORTH, Direction.WEST]),
    "J": Pipe([Direction.NORTH, Direction.EAST]),
    "7": Pipe([Direction.SOUTH, Direction.EAST]),
    "F": Pipe([Direction.SOUTH, Direction.WEST]),
    ".": Pipe([]),
}


def initial_steps(maze: np.ndarray, start: tuple[int, int]):
    initial_steps = []
    for direction in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
        next_point = tuple(map(sum, zip(start, direction.value)))
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
            next_point = tuple(map(sum, zip(point, direction.value)))
            next_pipe = PIPES[maze[next_point]]
            next_path_positions.append((next_point, next_pipe.flows_to(direction)))
            visited[next_point] = True

        path = next_path_positions
        steps += 1

    return maze, visited, steps
