from aocutils import Numpy
from year2023.day21.common import extended_maze, walk


def run(data: list[str], is_test: bool):
    maze = Numpy.from_input_as_str(data)
    width = maze.shape[0]
    max_steps = 100 if is_test else (width // 2) * 3 + 1
    factor = (f if (f := max_steps // (width // 2)) % 2 == 1 else f + 1) + 2

    if is_test:
        return len(walk(extended_maze(maze, factor), max_steps))

    # Screw this task! After the attempt to fix off-by-one errors,
    # plotting multiple random results showed a quadratic relationship.
    #
    # ... which has also been PITA because it couldn't be solved with normal methods (sympy)

    y = [len(walk(extended_maze(maze, factor + i), (width // 2) + (width * i))) for i in range(3)]
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    x = (26501365 - (width // 2)) // width
    return (a * x**2) + (b * x) + c
