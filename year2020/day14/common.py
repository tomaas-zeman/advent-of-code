import re
from dataclasses import dataclass
from itertools import product

from aocutils import as_ints


@dataclass
class Mask:
    bits: str

    def apply_to_input(self, number: int) -> int:
        for i, bit in enumerate(self.bits[::-1]):
            if bit == "0":
                number &= ~(1 << i)
            if bit == "1":
                number |= 1 << i
        return number

    def apply_to_address(self, address: int) -> list[int]:
        floating_positions = [i for i in range(len(self.bits)) if self.bits[::-1][i] == "X"]
        combinations = product([0, 1], repeat=len(floating_positions))
        addresses = []

        for combination in combinations:
            combination_index = 0
            tmp_address = int(address)

            for i, bit in enumerate(self.bits[::-1]):
                if bit == "1":
                    tmp_address |= 1 << i
                if bit == "X":
                    if combination[combination_index] == 1:
                        tmp_address |= 1 << i
                    else:
                        tmp_address &= ~(1 << i)
                    combination_index += 1

            addresses.append(tmp_address)

        return addresses


def compute(data: list[str], apply_mask_to_address=False, apply_mask_to_input=False):
    mask = None
    memory = {}

    for line in data:
        if match := re.search(r"mask = ([01X]+)", line):
            mask = Mask(match.group(1))
        elif match := re.search(r"mem\[(\d+)] = (\d+)", line):
            mem_slot, value = as_ints(match.groups())

            if apply_mask_to_input:
                memory[mem_slot] = mask.apply_to_input(value)

            if apply_mask_to_address:
                for address in mask.apply_to_address(mem_slot):
                    memory[address] = value

    return sum(memory.values())
