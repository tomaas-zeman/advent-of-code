def run(data: list[str], is_test: bool):
    return len([c for c in data[0] if c == "("]) - len([c for c in data[0] if c == ")"])
