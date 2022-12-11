from __future__ import annotations
from enum import Enum


class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def compareWith(self, option: Option):
        if self.value - option.value in [-1, 2]:
            return Result.LOSS
        if self.value == option.value:
            return Result.DRAW
        return Result.WIN

    def optionForResult(self, result: Result):
        if result == Result.DRAW:
            return self
        if result == Result.LOSS:
            value = self.value - 1
            return Option(value if value > 0 else 3)
        value = self.value + 1
        return Option(value if value < 4 else 1)


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6
