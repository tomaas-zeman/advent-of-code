from typing import List, Tuple, Dict

from common.matrix import matrix_from_data


def run(data: List[str]):
    matrix = matrix_from_data(data)

    while True:
        changes: Dict[Tuple[int, int], str] = {}

        for seat in matrix.all_points():
            if seat.value == '.':
                continue

            occupied_neighbours = len([n for n in seat.neighbours(True) if n.value == '#'])
            if seat.value == 'L' and occupied_neighbours == 0:
                changes[(seat.row, seat.column)] = '#'
            elif seat.value == '#' and occupied_neighbours >= 4:
                changes[(seat.row, seat.column)] = 'L'

        # apply changes - everything has to happen at once
        if len(changes) == 0:
            break

        for [row, column], new_value in changes.items():
            matrix.point_at(row, column).value = new_value

    return len([point for point in matrix.all_points() if point.value == '#'])
