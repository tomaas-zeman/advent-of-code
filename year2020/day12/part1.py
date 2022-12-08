from year2020.day12.common import Direction, Rotation, compute_new_position


def turn_ship(degree: int, current_direction: Direction):
    return Direction((current_direction.value + (degree / 90)) % 4)


def run(data: list[str], raw_data: list[str]):
    position = (0, 0)  # (horizontal, vertical), positive is south/east
    direction = Direction.E

    for line in data:
        movement = line[0]
        value = int(line[1:])
        if movement in ["N", "S", "E", "W"]:
            position = compute_new_position(position, Direction[movement], value)
        elif movement in ["L", "R"]:
            direction = turn_ship(value * Rotation[movement].value, direction)
        else:
            position = compute_new_position(position, direction, value)

    return abs(position[0]) + abs(position[1])
