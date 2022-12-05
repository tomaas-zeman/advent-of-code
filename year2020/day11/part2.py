from typing import List, Dict, Tuple

from common.matrix import matrix_from_data, Point


def find_neighbour(seat: Point, delta_row: int, delta_col: int):
    matrix = seat.matrix
    step = 1
    while 0 <= seat.row + delta_row * step < matrix.num_rows and 0 <= seat.column + delta_col * step < matrix.num_cols:
        neighbour = matrix.point_at(seat.row + delta_row * step, seat.column + delta_col * step)
        if neighbour is not None and neighbour.value != '.':
            return neighbour
        step += 1
    return None


def find_neighbours(seat: Point):
    return [
        n for n in [
            find_neighbour(seat, 0, 1),
            find_neighbour(seat, 0, -1),
            find_neighbour(seat, 1, 0),
            find_neighbour(seat, -1, 0),
            find_neighbour(seat, 1, 1),
            find_neighbour(seat, -1, -1),
            find_neighbour(seat, 1, -1),
            find_neighbour(seat, -1, 1),
        ]
        if n is not None
    ]


def run(data: List[str], raw_data: List[str]):
    matrix = matrix_from_data(data)
    while True:
        changes: Dict[Tuple[int, int], str] = {}

        for seat in matrix.all_points():
            if seat.value == '.':
                continue

            occupied_neighbours = len([n for n in find_neighbours(seat) if n.value == '#'])
            if seat.value == 'L' and occupied_neighbours == 0:
                changes[(seat.row, seat.column)] = '#'
            elif seat.value == '#' and occupied_neighbours >= 5:
                changes[(seat.row, seat.column)] = 'L'

        # apply changes - everything has to happen at once
        if len(changes) == 0:
            break

        for [row, column], new_value in changes.items():
            matrix.point_at(row, column).value = new_value

    return len([point for point in matrix.all_points() if point.value == '#'])
