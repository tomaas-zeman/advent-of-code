import ast

from year2020.day18.common import compute


def run(data: list[str], is_test: bool):
    ops = {ast.Mult: lambda a, b: a + b, ast.Sub: lambda a, b: a * b}
    return compute(data, lambda line: line.replace("*", "-").replace("+", "*"), ops)


test_result = 23340
