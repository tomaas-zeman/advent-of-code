import re


def parse(data: list[str]) -> tuple[str, dict[str, dict[str, str]]]:
    instructions = data[0]

    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    mapping = {
        match.group(1): {"L": match.group(2), "R": match.group(3)}
        for line in data[2:]
        if (match := pattern.match(line))
    }

    return instructions, mapping
