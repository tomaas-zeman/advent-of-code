from enum import Enum
from year2022.day02.common import Option


class Mapping(Enum):
    A = Option.ROCK
    B = Option.PAPER
    C = Option.SCISSORS
    X = Option.ROCK
    Y = Option.PAPER
    Z = Option.SCISSORS


def run(data: list[str], raw_data: list[str], is_test: bool):
    points = 0
    for line in data:
        [enemy, me] = [Mapping[x].value for x in line.split(" ")]
        points += me.compareWith(enemy).value + me.value
    return points
