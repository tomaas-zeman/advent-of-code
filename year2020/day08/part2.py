def toggle_instructions(data: list[str], modification_start_index: int):
    data_copy = [instruction for instruction in data]
    for i in range(modification_start_index, len(data_copy)):
        if "jmp" in data_copy[i]:
            data_copy[i] = data_copy[i].replace("jmp", "nop")
            return data_copy, i + 1
        if "nop" in data_copy[i]:
            data_copy[i] = data_copy[i].replace("nop", "jmp")
            return data_copy, i + 1
    return data_copy, modification_start_index


def run(data: list[str], raw_data: list[str]):
    acc = 0

    [modified_data, modification_start_index] = toggle_instructions(data, 0)
    while True:
        visited_instructions = []
        acc = 0
        index = 0
        while index < len(modified_data):
            if index in visited_instructions:
                [modified_data, modification_start_index] = toggle_instructions(data, modification_start_index)
                break

            visited_instructions.append(index)

            [instruction, value] = modified_data[index].split(" ")
            if instruction == "acc":
                acc += int(value)
                index += 1
            elif instruction == "jmp":
                index += int(value)
            else:
                index += 1

        if index == len(modified_data):
            return acc
