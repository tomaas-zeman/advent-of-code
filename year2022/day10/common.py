from typing import Callable


class Instruction:
    def __init__(self, duration: int, operation: Callable[[int, list], int]) -> None:
        self.duration = duration
        self.operation = operation


instructions = {"noop": Instruction(1, lambda x, _: x), "addx": Instruction(2, lambda x, args: x + int(args[0]))}
