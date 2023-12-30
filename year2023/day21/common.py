from collections import deque
from enum import Enum

import numpy as np

from aocutils import Point, Numpy


class Tile(Enum):
    START = "S"
    CENTER = "X"
    ROCK = "#"
    PLOT = "."
    VISITED = "O"


def print_maze(maze: np.ndarray, visited: set[Point]):
    for row in range(maze.shape[0]):
        print(f"{row:03d} ", end="")
        for col in range(maze.shape[1]):
            if (row, col) in visited:
                if maze[row][col] != Tile.START:
                    print(f"{Tile.VISITED.value} ", end="")
                else:
                    print(f"{Tile.START.value} ", end="")
            else:
                print(f"{maze[row][col]} ", end="")
        print()


def get_starting_point(maze: np.ndarray) -> Point:
    row, col = np.argwhere(maze == Tile.START.value)[0]
    return row, col


def extended_maze(maze: np.ndarray, factor: int) -> np.ndarray:
    starting_point = get_starting_point(maze)
    extension = np.copy(maze)
    extension[starting_point] = Tile.CENTER.value

    new_rows = []
    for i in range(factor):
        new_row = []
        for j in range(factor):
            if i == factor // 2 and j == factor // 2:
                new_row.append(maze)
            else:
                new_row.append(extension)
        new_rows.append(np.concatenate(new_row, axis=1))

    return np.concatenate(new_rows, axis=0)


def walk(maze: np.ndarray, max_steps: int) -> set[Point]:
    starting_point = get_starting_point(maze)

    visited: set[Point] = set()
    result: set[Point] = set()
    queue = deque([(starting_point, 0)])

    while len(queue) > 0:
        current_position, step = queue.pop()

        if step == max_steps:
            continue

        for next_position in Numpy.valid_neighbor_positions_of(current_position, maze):
            if maze[next_position] != Tile.ROCK.value and next_position not in visited:
                visited.add(next_position)
                queue.appendleft((next_position, step + 1))
                if step % 2 == 1 if max_steps % 2 == 0 else step % 2 == 0:
                    result.add(next_position)

    return result
