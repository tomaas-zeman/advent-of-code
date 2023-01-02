def run(data: list[str], is_test: bool):
    visited_instructions = []
    acc = 0
    index = 0
    while index < len(data):
        if index in visited_instructions:
            return acc

        visited_instructions.append(index)

        [instruction, value] = data[index].split(" ")
        if instruction == "acc":
            acc += int(value)
            index += 1
        elif instruction == "jmp":
            index += int(value)
        else:
            index += 1
