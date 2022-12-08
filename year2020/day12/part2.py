from year2020.day12.common import Direction, Rotation, compute_new_position


def rotate_waypoint(ship: tuple[int, int], waypoint: tuple[int, int], degree: int):
    sector = (degree / 90) % 4
    diff_horizontal = ship[0] - waypoint[0]
    diff_vertical = ship[1] - waypoint[1]
    if sector == 1:
        return ship[0] + diff_vertical, ship[1] - diff_horizontal
    if sector in [2, -2]:
        return ship[0] + diff_horizontal, ship[1] + diff_vertical
    if sector == 3:
        return ship[0] - diff_vertical, ship[1] + diff_horizontal
    return waypoint


def run(data: list[str], raw_data: list[str]):
    ship = (0, 0)  # (horizontal, vertical), positive is south/east
    waypoint = (10, -1)

    for line in data:
        movement = line[0]
        value = int(line[1:])
        if movement in ["N", "S", "E", "W"]:
            waypoint = compute_new_position(waypoint, Direction[movement], value)
        elif movement in ["L", "R"]:
            waypoint = rotate_waypoint(ship, waypoint, value * Rotation[movement].value)
        else:
            shift_h = (waypoint[0] - ship[0]) * value
            shift_v = (waypoint[1] - ship[1]) * value
            ship = ship[0] + shift_h, ship[1] + shift_v
            waypoint = waypoint[0] + shift_h, waypoint[1] + shift_v

    return abs(ship[0]) + abs(ship[1])
