def parse(data: list[str]):
    sequence = [c for c in data[0]]
    rules = {pair: insert for pair, insert in [line.strip().split(" -> ") for line in data[2:]]}
    return [sequence, rules]
