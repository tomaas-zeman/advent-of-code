from typing import List, Tuple, Dict
import re


class Instruction:
    def __init__(self, amount: int, from_stack: int, to_stack: int) -> None:
        self.amount = amount
        self.from_stack = from_stack - 1
        self.to_stack = to_stack - 1


def parse_input(data: List[str]):
    stacks: Dict[int, List[str]] = {}
    instructions: List[Instruction] = []

    for line in data:
        if '[' in line:
            groups = [line[i : i + 4] for i in range(0, len(line), 4)]
            for i in range(len(groups)):
                crate = re.search(".*\[(\w+)\].*", groups[i])
                if i not in stacks:
                    stacks[i] = []
                if crate is not None:
                    stacks[i].insert(0, crate.groups()[0])
        if line.startswith("move"):
            [amount, from_stack, to_stack] = [
                int(x) for x in re.search(".*?(\d+).*?(\d+).*?(\d+)", line).groups()
            ]
            instructions.append(Instruction(amount, from_stack, to_stack))

    return (stacks, instructions)
