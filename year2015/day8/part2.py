from typing import List


def encode(string: str):
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'


def run(data: List[str], raw_data: List[str]):
    return sum([len(encode(string)) - len(string) for string in data])
