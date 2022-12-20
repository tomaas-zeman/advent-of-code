from common.utils import as_ints


def run(data: list[str], raw_data: list[str], is_test: bool):
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
