from aocutils import Direction, Tuple
from year2015.day03.common import directions


def run(data: list[str], is_test: bool):
    santa = (0, 0)
    robosanta = (0, 0)
    visited = set([santa])

    for i in range(len(data[0])):
        d = data[0][i]
        if i % 2 == 0:
            santa = Tuple.add(santa, Direction.coord_change(directions[d]))
        else:
            robosanta = Tuple.add(robosanta, Direction.coord_change(directions[d]))
        visited.add(santa)
        visited.add(robosanta)

    return len(visited)
