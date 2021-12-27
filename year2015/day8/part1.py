from typing import List


def run(data: List[str]):
    return sum([len(string) - (len(bytes(string, 'utf-8').decode('unicode_escape')) - 2) for string in data])
