import numpy as np
from common.utils import Numpy
from year2023.day10.common import PIPES, combine, initial_steps


def run(data: list[str], is_test: bool):
    maze = Numpy.from_input_as_str(data)
    start = np.argwhere(maze == "S")[0]
    visited = np.full(maze.shape, False)

    path = initial_steps(maze, start)
    for point, _ in path + [start]:
        visited[point] = True
    
    steps = 1
    while any(p[0] != path[0][0] for p in path):
        next_path_positions = []
        for point, direction in path:
            next_point = combine(point, direction)
            next_pipe = PIPES[maze[next_point]]
            next_path_positions.append((next_point, next_pipe.flows_to(direction)))
            visited[next_point] = True

        path = next_path_positions
        steps += 1
    
    counter = 0
    for row in range(maze.shape[0]):
        inside = False
        for col in range(maze.shape[1]):
            if maze[(row, col)] in "|F7" and visited[(row, col)]:
                inside = not inside
            if inside and not visited[(row, col)]:
                counter += 1

    Numpy.print_matrix(maze)
    return counter
