from typing import List
from common.lists import as_ints


def run(data: List[str], raw_data: List[str]):
    codes = as_ints(data[0].split(","))

    # inputs (task description)
    codes[1] = 12
    codes[2] = 2

    i = 0
    while codes[i] != 99:
        opcode = codes[i]
        if opcode == 1:
            codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
        if opcode == 2:
            codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
        i += 4
    return codes[0]
