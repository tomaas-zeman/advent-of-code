from typing import Callable
from common.matrix import matrix_from_data, Matrix as Forest, Point as Tree


def flag_visible_trees(forest: Forest):
    def mark_direction(
        range1: int, range2: int, initial_index: int, index_change: int, select_tree: Callable[[Forest, int, int], Tree]
    ):
        for i in range(range1):
            j = initial_index
            tallest = -1
            for _ in range(range2):
                tree = select_tree(forest, i, j)
                if tree.value > tallest:
                    tree.flag = 1
                    tallest = tree.value
                j += index_change

    selector = lambda forest, i, j: forest.point_at(i, j)
    mark_direction(forest.num_rows, forest.num_cols, 0, 1, selector)
    mark_direction(forest.num_rows, forest.num_cols, forest.num_cols - 1, -1, selector)

    selector = lambda forest, i, j: forest.point_at(j, i)
    mark_direction(forest.num_cols, forest.num_rows, 0, 1, selector)
    mark_direction(forest.num_cols, forest.num_rows, forest.num_rows - 1, -1, selector)


def run(data: list[str], is_test: bool):
    forest = matrix_from_data(data, convert_value=lambda x: int(x))
    flag_visible_trees(forest)
    return len([tree for tree in forest.all_points() if tree.flag == 1])
