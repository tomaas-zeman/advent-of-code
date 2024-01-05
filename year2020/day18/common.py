import ast
from typing import Callable


def evaluate_ast(node: ast.expr, ops: dict[ast.expr, Callable[[int, int], int]]):
    if isinstance(node, ast.BinOp):
        left = evaluate_ast(node.left, ops)
        right = evaluate_ast(node.right, ops)

        if any(isinstance(node.op, t) for t in [ast.Add, ast.Sub, ast.Mult]):
            return ops[type(node.op)](left, right)
    elif isinstance(node, ast.Constant):
        return node.value


# Not proud of it in any way but it works :X
def compute(
    data: list[str], line_replacement: Callable[[str], str], ops: dict[ast.expr, Callable[[int, int], int]]
) -> int:
    sum = 0
    for line in data:
        tree = ast.parse(line_replacement(line))
        sum += evaluate_ast(tree.body[0].value, ops)
    return sum
