from aocutils import Point
from year2020.day24.common import get_initial_black_positions, Direction, next_position


def all_positions_in_distance(distance: int) -> list[Point]:
    positions = []
    for q in range(-distance, distance + 1):
        for r in range(-distance, distance + 1):
            for s in range(-distance, distance + 1):
                if q + r + s == 0:
                    positions.append((q, r, s))
    return positions


def neighbors(position: Point) -> list[Point]:
    return [next_position(position, direction) for direction in Direction.all()]


def get_updates(blacks: set[Point], distance: int):
    remove = set()
    add = set()

    for position in all_positions_in_distance(distance):
        black_neighbors = len([neighbor for neighbor in neighbors(position) if neighbor in blacks])
        if position in blacks and black_neighbors == 0 or black_neighbors > 2:
            remove.add(position)
        if position not in blacks and black_neighbors == 2:
            add.add(position)

    return remove, add


def run(data: list[str], is_test: bool):
    blacks = get_initial_black_positions(data)
    initial_distance = max(max([abs(coord) for coord in black]) for black in blacks)

    for step in range(100):
        remove, add = get_updates(blacks, initial_distance + step + 1)
        blacks.difference_update(remove)
        blacks.update(add)

    return len(blacks)
