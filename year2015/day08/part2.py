def encode(string: str):
    return '"' + string.replace("\\", "\\\\").replace('"', '\\"') + '"'


def run(data: list[str], is_test: bool):
    return sum([len(encode(string)) - len(string) for string in data])
