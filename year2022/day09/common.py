from common.matrix import Point


def move_head(point: Point, direction: str):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    row_change, column_change = directions[direction]
    return Point(point.row + row_change, point.column + column_change)


def move_tail(head: Point, tail: Point):
    if head.is_neighbor_of(tail):
        return tail
    row_delta = head.row - tail.row
    column_delta = head.column - tail.column
    row = head.row if abs(row_delta) < 2 else head.row - (row_delta // 2)
    column = head.column if abs(column_delta) < 2 else head.column - (column_delta // 2)
    return Point(row, column)


def count_visited_nodes(data: list[str], number_of_knots: int):
    visited = set()
    knots = [Point(0, 0) for i in range(number_of_knots)]

    visited.add(knots[-1])

    for step in data:
        [direction, amount] = step.split(" ")
        for _ in range(int(amount)):
            for i in range(number_of_knots):
                if i == 0:
                    knots[i] = move_head(knots[i], direction)
                else:
                    knots[i] = move_tail(knots[i - 1], knots[i])
            visited.add(knots[-1])

    return len(visited)
