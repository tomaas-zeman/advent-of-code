from typing import Callable
from common.matrix import matrix_from_data, Matrix as Forest, Point as Tree


def compute_tree_scores(forest: Forest):
    def score(tree: Tree, range, coords: Callable[[Tree, int], tuple[int, int]]):
        score = 0
        for i in range:
            [row, col] = coords(tree, i)
            other = forest.point_at_safe(row, col)
            if other is not None and tree != other:
                score += 1
                if tree.value <= other.value:
                    break
        return score

    for tree in forest.all_points():
        tree.flag = (
            score(tree, range(tree.column, -1, -1), lambda t, i: (t.row, i))
            * score(tree, range(tree.column, forest.num_cols, 1), lambda t, i: (t.row, i))
            * score(tree, range(tree.row, -1, -1), lambda t, i: (i, t.column))
            * score(tree, range(tree.row, forest.num_rows, 1), lambda t, i: (i, t.column))
        )


def run(data: list[str], raw_data: list[str], is_test: bool):
    forest = matrix_from_data(data, convert_value=lambda x: int(x))
    compute_tree_scores(forest)
    return max([tree.flag for tree in forest.all_points() if tree.flag])
