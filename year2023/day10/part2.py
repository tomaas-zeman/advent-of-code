from year2023.day10.common import walk_path


def run(data: list[str], is_test: bool):
    maze, visited, _ = walk_path(data)

    counter = 0
    for row in range(maze.shape[0]):
        inside = False
        for col in range(maze.shape[1]):
            if maze[(row, col)] in "|F7" and visited[(row, col)]:
                inside = not inside
            if inside and not visited[(row, col)]:
                counter += 1

    return counter
