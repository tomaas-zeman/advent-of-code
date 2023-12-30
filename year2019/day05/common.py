from enum import Enum

from aocutils import as_ints


class OpCode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THEN = 7
    EQUALS = 8
    INTERRUPT = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


def get_arg_value(codes: list[int], mode: Mode, i: int):
    if mode == Mode.IMMEDIATE:
        return codes[i]
    return codes[codes[i]]


def compute_diagnostic_code(data: list[str], input: int):
    codes = as_ints(data[0].split(","))
    diagnostic_code = None

    i = 0
    while codes[i] != OpCode.INTERRUPT.value:
        instruction = f"{codes[i]:05}"

        opcode = OpCode(int(instruction[3:]))
        [_, param2_mode, param1_mode] = [Mode(int(mode)) for mode in instruction[0:3]]

        if opcode == OpCode.ADD:
            codes[codes[i + 3]] = get_arg_value(codes, param1_mode, i + 1) + get_arg_value(codes, param2_mode, i + 2)
            i += 4
        elif opcode == OpCode.MULTIPLY:
            codes[codes[i + 3]] = get_arg_value(codes, param1_mode, i + 1) * get_arg_value(codes, param2_mode, i + 2)
            i += 4
        elif opcode == OpCode.INPUT:
            codes[codes[i + 1]] = input
            i += 2
        elif opcode == OpCode.OUTPUT:
            diagnostic_code = get_arg_value(codes, param1_mode, i + 1)
            i += 2
        elif opcode == OpCode.JUMP_IF_TRUE:
            if get_arg_value(codes, param1_mode, i + 1) != 0:
                i = get_arg_value(codes, param2_mode, i + 2)
            else:
                i += 3
        elif opcode == OpCode.JUMP_IF_FALSE:
            if get_arg_value(codes, param1_mode, i + 1) == 0:
                i = get_arg_value(codes, param2_mode, i + 2)
            else:
                i += 3
        elif opcode == OpCode.LESS_THEN:
            if get_arg_value(codes, param1_mode, i + 1) < get_arg_value(codes, param2_mode, i + 2):
                codes[codes[i + 3]] = 1
            else:
                codes[codes[i + 3]] = 0
            i += 4
        elif opcode == OpCode.EQUALS:
            if get_arg_value(codes, param1_mode, i + 1) == get_arg_value(codes, param2_mode, i + 2):
                codes[codes[i + 3]] = 1
            else:
                codes[codes[i + 3]] = 0
            i += 4
        else:
            raise KeyError("Unsupported opcode " + opcode.name)

    return diagnostic_code
