from enum import Enum
from year2022.day02.common import Option, Result


class Mapping(Enum):
    A = Option.ROCK
    B = Option.PAPER
    C = Option.SCISSORS
    X = Result.LOSS
    Y = Result.DRAW
    Z = Result.WIN


def run(data: list[str], is_test: bool):
    points = 0
    for line in data:
        enemy: Option = Mapping[line.split(" ")[0]].value
        result: Result = Mapping[line.split(" ")[1]].value
        points += result.value + enemy.optionForResult(result).value
    return points
