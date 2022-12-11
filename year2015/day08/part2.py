def encode(string: str):
    return '"' + string.replace("\\", "\\\\").replace('"', '\\"') + '"'


def run(data: list[str], raw_data: list[str]):
    return sum([len(encode(string)) - len(string) for string in data])
