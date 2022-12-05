from typing import List
from common.lists import as_ints


def run(data: List[str], raw_data: List[str]):
    for noun in range(0, 100):
        for verb in range(0, 100):
            codes = as_ints(data[0].split(","))
            codes[1] = noun
            codes[2] = verb

            i = 0
            while codes[i] != 99:
                opcode = codes[i]
                if opcode == 1:
                    codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
                if opcode == 2:
                    codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
                i += 4

            if codes[0] == 19690720:
                return 100 * noun + verb
