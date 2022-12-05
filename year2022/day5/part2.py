from typing import List
from year2022.day5.common import parse_input


def run(data: List[str], raw_data: List[str]):
    [stacks, instructions] = parse_input(raw_data)

    for instruction in instructions:
        items_to_move = stacks[instruction.from_stack][-instruction.amount:]
        stacks[instruction.from_stack] = stacks[instruction.from_stack][:-instruction.amount]
        stacks[instruction.to_stack] = stacks[instruction.to_stack] + items_to_move

    return "".join([stack.pop() for stack in stacks])
