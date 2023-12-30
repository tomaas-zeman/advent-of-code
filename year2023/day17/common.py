from __future__ import annotations

import sys
from dataclasses import dataclass
from queue import PriorityQueue

import numpy as np

from aocutils import Direction, Numpy, Coord, Point


@dataclass(frozen=True)
class State:
    point: Point
    last_direction: Direction = None
    steps_in_one_direction: int = 1

    def __lt__(self, other: State):
        return hash(self.point) - hash(other.point)


def dijkstra(matrix: np.ndarray, starting_point: Point, max_straight_length: int, min_steps_to_turn: int) -> int:
    initial_state = State(starting_point)
    distances = {initial_state: 0}
    visited: set[State] = set()

    queue = PriorityQueue[tuple[int, State]]()
    queue.put((0, initial_state))

    while not queue.empty():
        distance, state = queue.get()

        if state in visited:
            continue

        visited.add(state)

        for direction in [
            d for d in Direction.all() if state.last_direction is None or d != Direction.opposite(state.last_direction)
        ]:
            next_coord = Coord.add(state.point, Direction.coord_change(direction))
            if not Numpy.is_valid_point(next_coord, matrix):
                continue

            if state.last_direction is not None:
                if direction == state.last_direction and state.steps_in_one_direction == max_straight_length:
                    continue
                if direction != state.last_direction and state.steps_in_one_direction < min_steps_to_turn:
                    continue

            next_state = State(
                next_coord, direction, 1 if direction != state.last_direction else state.steps_in_one_direction + 1
            )

            if not next_state in distances:
                distances[next_state] = sys.maxsize

            current_distance = distances[next_state]
            new_distance = distances[state] + matrix[next_coord]

            if new_distance < current_distance:
                distances[next_state] = new_distance
                queue.put((new_distance, next_state))

    return min(
        [distance for state, distance in distances.items() if state.point == (matrix.shape[0] - 1, matrix.shape[1] - 1)]
    )
