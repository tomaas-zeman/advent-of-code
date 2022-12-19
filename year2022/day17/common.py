import numpy as np


CAVE_TOP_BUFFER = 3
CAVE_WIDTH = 7


class Rock:
    def __init__(self, initial_shape: np.ndarray) -> None:
        self.height = initial_shape.shape[0]
        self.width = initial_shape.shape[1]
        self.initial_shape = initial_shape
        self.shape = np.pad(initial_shape, ((0, 0), (2, CAVE_WIDTH - 2 - self.width)), constant_values=0)
        self.h_position = 2
        self.v_position = 0

    def new(self):
        return Rock(self.initial_shape)

    def can_move_left(self, cave: np.ndarray):
        def not_blocked_by_rocks():
            allowed = []
            for column in range(self.width):
                cave_slice = cave[:, self.h_position - 1 + column]
                rock_slice = self.shape[:, self.h_position + column]
                allowed += [
                    rock_slice[row] == 0 or cave_slice[row + self.v_position] != 1 for row in range(self.height)
                ]
            return all(allowed)

        def not_blocked_by_cave():
            return all([v == 0 for v in self.shape[:, 0]])

        return not_blocked_by_cave() and not_blocked_by_rocks()

    def can_move_right(self, cave: np.ndarray):
        def not_blocked_by_rocks():
            allowed = []
            for column in range(self.width):
                cave_slice = cave[:, self.h_position + self.width - column]
                rock_slice = self.shape[:, self.h_position + self.width - 1 - column]
                allowed += [
                    rock_slice[row] == 0 or cave_slice[row + self.v_position] != 1 for row in range(self.height)
                ]
            return all(allowed)

        def not_blocked_by_cave():
            return all([v == 0 for v in self.shape[:, -1]])

        return not_blocked_by_cave() and not_blocked_by_rocks()

    def can_move_down(self, cave: np.ndarray):
        allowed = []
        for row in range(self.height):
            rock_slice = self.shape[-1 - row, :]
            cave_slice = cave[self.v_position + self.height - row, :]
            allowed += [cave_slice[column] != 1 or rock_slice[column] != 1 for column in range(CAVE_WIDTH)]
        return all(allowed)

    def blow(self, direction: str, cave: np.ndarray):
        if direction == "<" and self.can_move_left(cave):
            self.shape = np.roll(self.shape, -1, axis=1)
            self.h_position -= 1
        if direction == ">" and self.can_move_right(cave):
            self.shape = np.roll(self.shape, 1, axis=1)
            self.h_position += 1

    def fall(self, cave: np.ndarray):
        can_fall = self.can_move_down(cave)
        if can_fall:
            self.v_position += 1
        return can_fall


prototypes = [
    Rock(np.array([[1, 1, 1, 1]])),
    Rock(np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])),
    Rock(np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])),
    Rock(np.array([[1], [1], [1], [1]])),
    Rock(np.array([[1, 1], [1, 1]])),
]


def resize_cave(cave: np.ndarray, height: int):
    if height > 0:
        return np.pad(cave, ((height, 0), (0, 0)), constant_values=0)
    return cave[abs(height) :, :]


def settle_rock(cave: np.ndarray, rock: Rock):
    for row in range(rock.height):
        for column in range(CAVE_WIDTH):
            cave[(row + rock.v_position, column)] = min(
                cave[(row + rock.v_position, column)] + rock.shape[(row, column)], 1
            )


def row_of_tower_top(cave: np.ndarray):
    return min(np.nonzero(cave)[0])


def get_tower_size(cave: np.ndarray):
    return cave.shape[0] - row_of_tower_top(cave) - 1  # -1 for floor
