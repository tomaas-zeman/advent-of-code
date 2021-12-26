from math import ceil
from typing import List


def count_trees_on_path(movement_right: int, movement_down: int, matrix: List[List[str]]) -> int:
    trees_on_path = 0
    for step in range(ceil(len(matrix) / movement_down)):
        row = step * movement_down
        col = (step * movement_right) % len(matrix[0])
        if matrix[row][col] == '#':
            trees_on_path += 1

    return trees_on_path
