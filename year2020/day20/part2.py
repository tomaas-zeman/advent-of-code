###############################################################################################
# Not proud of this messy solution but it was the last task that year, so as long as it works #
# It's reasonably fast at least ...                                                           #
###############################################################################################
from collections import deque
from functools import reduce
from itertools import product, pairwise

import numpy as np

from aocutils import flatten
from year2020.day20.common import find_common_edges, parse, Tile, generate_variations


def find_path_to_corner(common_edges: dict[int, list[int]]):
    corners = [tile for tile, neighbors in common_edges.items() if len(neighbors) == 2]
    queue = deque([[corners[0]]])

    while queue:
        path = queue.pop()

        next_tiles = [tile for tile in common_edges[path[-1]] if tile not in path]
        for next_tile in next_tiles:
            next_path = path + [next_tile]
            if next_tile in corners:
                return next_path
            else:
                queue.appendleft(next_path)


def get_tile_order(common_edges: dict[int, list[int]]) -> list[list[int]]:
    top_row_tile_ids = find_path_to_corner(common_edges)
    ids = [top_row_tile_ids]

    for _ in range(len(top_row_tile_ids) - 1):
        all_used_ids = set(flatten(ids))

        new_row_ids = []
        for prev_tile_id in ids[-1]:
            new_row_ids.append([id for id in common_edges[prev_tile_id] if id not in all_used_ids][0])

        ids.append(new_row_ids)

    return ids


def assemble_picture(tiles: list[Tile], common_edges: dict[int, list[int]]) -> list[list[np.ndarray]]:
    tiles_by_id = {t.id: t for t in tiles}
    tile_order = get_tile_order(common_edges)

    picture = []

    # top row setup
    for left_tile_id, right_tile_id in pairwise(tile_order[0]):
        left_variations = tiles_by_id[left_tile_id].variations() if len(picture) == 0 else [picture[0][-1]]
        right_variations = tiles_by_id[right_tile_id].variations()

        for left, right in product(left_variations, right_variations):
            if np.array_equal(left[:, -1], right[:, 0]):
                if len(picture) == 0:
                    picture.append([left, right])
                else:
                    picture[0].append(right)
                break

    # remaining rows
    for prev_row_index, row in enumerate(tile_order[1:]):
        new_picture_row = []

        for col_index, bottom_tile_id in enumerate(row):
            for top, bottom in product([picture[prev_row_index][col_index]], tiles_by_id[bottom_tile_id].variations()):
                if np.array_equal(top[-1, :], bottom[0, :]):
                    new_picture_row.append(bottom)
                    break

        picture.append(new_picture_row)

    return picture


def strip_borders(picture: list[list[np.ndarray]]) -> np.ndarray:
    final_image = None

    for row in picture:
        stripped_row = reduce(
            lambda acc, col: np.concatenate([acc, col[1:-1, 1:-1]], axis=1), [c for c in row[1:]], row[0][1:-1, 1:-1]
        )
        if final_image is None:
            final_image = stripped_row
        else:
            final_image = np.concatenate([final_image, stripped_row], axis=0)

    return final_image


def pattern_matches(pattern: np.ndarray, picture_slice: np.ndarray):
    for i in range(pattern.shape[0]):
        for j in range(pattern.shape[1]):
            if pattern[i][j] == "#" and pattern[i][j] != picture_slice[i][j]:
                return False
    return True


def count_pattern_occurrences(pattern: np.ndarray, picture: np.ndarray):
    for variation in generate_variations(picture):
        matches = 0

        for row in range(variation.shape[0] - pattern.shape[0] + 1):
            for col in range(variation.shape[1] - pattern.shape[1] + 1):
                picture_slice = variation[row : row + pattern.shape[0], col : col + pattern.shape[1]]
                if pattern_matches(pattern, picture_slice):
                    matches += 1

        if matches > 0:
            return matches

    raise Exception("No sea monsters found!")


def run(data: list[str], is_test: bool):
    tiles = parse(data)
    common_edges = find_common_edges(tiles)
    intermediate_picture = assemble_picture(tiles, common_edges)
    picture = strip_borders(intermediate_picture)

    pattern = np.array(
        [
            [c for c in "                  # "],
            [c for c in "#    ##    ##    ###"],
            [c for c in " #  #  #  #  #  #   "],
        ]
    )

    matches = count_pattern_occurrences(pattern, picture)
    pattern_hashes = np.count_nonzero(pattern == "#")
    picture_hashes = np.count_nonzero(picture == "#")

    return picture_hashes - (matches * pattern_hashes)
