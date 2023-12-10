import numpy as np
from common.utils import Numpy
from year2023.day10.common import PIPES, combine, initial_steps


def run(data: list[str], is_test: bool):
    maze = Numpy.from_input_as_str(data)
    path = initial_steps(maze, np.argwhere(maze == "S")[0])
    steps = 1

    while any(p[0] != path[0][0] for p in path):
        next_path_positions = []
        for point, direction in path:
            next_point = combine(point, direction)
            next_pipe = PIPES[maze[next_point]]
            next_path_positions.append((next_point, next_pipe.flows_to(direction)))

        path = next_path_positions
        steps += 1

    return steps
