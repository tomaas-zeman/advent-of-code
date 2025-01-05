from aocutils import Direction, Tuple
from year2015.day03.common import directions


def run(data: list[str], is_test: bool):
    position = (0, 0)
    visited = set([position])

    for d in data[0]:
        position = Tuple.add(position, Direction.coord_change(directions[d]))
        visited.add(position)

    return len(visited)
