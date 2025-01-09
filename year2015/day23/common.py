def run_program(data: list[str], registers: dict[str, int]):
    ip = 0

    while ip < len(data):
        line = data[ip].replace(',', '').split(" ")

        if line[0] == "hlf":
            registers[line[1]] = registers[line[1]] // 2
        elif line[0] == "tpl":
            registers[line[1]] = registers[line[1]] * 3
        elif line[0] == "inc":
            registers[line[1]] += 1
        elif line[0] == "jmp":
            ip += int(line[1])
            continue
        elif line[0] == "jie":
            if registers[line[1]] % 2 == 0:
                ip += int(line[2])
                continue
        elif line[0] == "jio":
            if registers[line[1]] == 1:
                ip += int(line[2])
                continue

        ip += 1
