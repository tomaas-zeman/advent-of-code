from itertools import combinations


def parse(data: list[str]):
    galaxies = [
        (row_index, col_index)
        for row_index, row in enumerate(data)
        for col_index, value in enumerate(row)
        if value == "#"
    ]
    empty_row_indexes = [row_index for row_index, row in enumerate(data) if all(c == "." for c in row)]
    empty_col_indexes = [col_index for col_index in range(len(data[0])) if all([row[col_index] == "." for row in data])]

    return galaxies, empty_row_indexes, empty_col_indexes


def empty_space(i: int, j: int, empty_indexes: list[int], expand_factor: int):
    return sum(expand_factor - 1 for empty_index in empty_indexes if min(i, j) < empty_index < max(i, j))


def sum_of_shortest_paths(data, expand_factor):
    galaxies, empty_row_indexes, empty_col_indexes = parse(data)
    pairs = list(combinations(galaxies, 2))

    return sum(
        [
            abs(p1[0] - p2[0])
            + empty_space(p1[0], p2[0], empty_row_indexes, expand_factor)
            + abs(p1[1] - p2[1])
            + empty_space(p1[1], p2[1], empty_col_indexes, expand_factor)
            for p1, p2 in pairs
        ]
    )
