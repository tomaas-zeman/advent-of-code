from typing import List, Tuple, Dict
import re


class Instruction:
    def __init__(self, amount: int, from_stack: int, to_stack: int) -> None:
        self.amount = amount
        self.from_stack = from_stack - 1
        self.to_stack = to_stack - 1


def parse_input(data: List[str]):
    stacks: List[str] = [[] for _ in range(len(data[0]) // 4)]
    instructions: List[Instruction] = []

    for line in data:
        if "[" in line:
            groups = [line[i : i + 4] for i in range(0, len(line), 4)]
            for i in range(len(groups)):
                crate = re.search(".*\[(\w+)\].*", groups[i])
                if crate is not None:
                    stacks[i].insert(0, crate.groups()[0])
        if line.startswith("move"):
            [_, amount, _, from_stack, _, to_stack] = line.split(" ")
            instructions.append(Instruction(int(amount), int(from_stack), int(to_stack)))

    return (stacks, instructions)


def compute_result(data: List[str], bulk_move=False):
    [stacks, instructions] = parse_input(data)

    for instruction in instructions:
        items_to_move = stacks[instruction.from_stack][-instruction.amount :]
        stacks[instruction.from_stack] = stacks[instruction.from_stack][: -instruction.amount]
        stacks[instruction.to_stack] = stacks[instruction.to_stack] + (
            items_to_move if bulk_move else items_to_move[::-1]
        )

    return "".join([stack.pop() for stack in stacks])
