from collections import deque

import numpy as np


class Elf:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.movement_priority = 0

    def set_offset(self, value: int):
        self.row += value
        self.col += value

    def no_elf_in_positions(self, map: np.ndarray, diffs: list[tuple[int, int]]):
        return all([map[self.row + d_row][self.col + d_col] == "." for d_row, d_col in diffs])

    def suggest_movement(self, map: np.ndarray):
        def north():
            if self.no_elf_in_positions(map, [(-1, -1), (-1, 0), (-1, 1)]):
                return (self.row - 1, self.col)

        def south():
            if self.no_elf_in_positions(map, [(1, -1), (1, 0), (1, 1)]):
                return (self.row + 1, self.col)

        def west():
            if self.no_elf_in_positions(map, [(-1, -1), (0, -1), (1, -1)]):
                return (self.row, self.col - 1)

        def east():
            if self.no_elf_in_positions(map, [(-1, 1), (0, 1), (1, 1)]):
                return (self.row, self.col + 1)

        movements = deque([north(), south(), west(), east()])
        movements.rotate(-(self.movement_priority % 4))
        movements = list(filter(None, movements))
        self.movement_priority += 1

        if len(movements) != 4 and len(movements) != 0:
            return movements[0]

    def move_to(self, row: int, col: int, map: np.ndarray):
        map[self.row][self.col] = "."
        map[row][col] = "#"
        self.row = row
        self.col = col

    def __str__(self) -> str:
        return f"{self.row}:{self.col}"


def parse_input(data: list[str]):
    elves = []
    map = np.empty((len(data), len(data[0])), dtype=str)
    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            map[row_index][col_index] = col
            if col == "#":
                elves.append(Elf(row_index, col_index))

    return elves, map


def do_round(elves: list[Elf], map: np.ndarray):
    suggestions: dict[tuple[int, int], list[Elf]] = {}
    for elf in elves:
        suggestion = elf.suggest_movement(map)
        if suggestion is not None:
            if suggestion not in suggestions:
                suggestions[suggestion] = []
            suggestions[suggestion].append(elf)

    for row, col, elf in [(coord[0], coord[1], elves[0]) for coord, elves in suggestions.items() if len(elves) == 1]:
        elf.move_to(row, col, map)

    return len(suggestions) == 0


def enlarge_map(map: np.ndarray, steps: int, elves: list[Elf]):
    map = np.pad(map, steps, constant_values=".")
    for elf in elves:
        elf.set_offset(steps)
    return map
