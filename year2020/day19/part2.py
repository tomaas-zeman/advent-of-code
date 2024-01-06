from year2020.day19.common import parse, compute


def run(data: list[str], is_test: bool):
    rules, messages = parse(data)
    rules["8"] = "42 | 42 8".split(" ")
    rules["11"] = "42 31 | 42 11 31".split(" ")
    return compute(rules, messages)
