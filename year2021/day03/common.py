def parse(data: list[str]):
    return [[int(bit) for bit in line.strip()] for line in data]
