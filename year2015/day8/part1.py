from typing import List


def run(data: List[str]):
    result = 0
    for string in data:
        decoded_string = bytes(string, 'utf-8').decode('unicode_escape')
        result += len(string) - (len(decoded_string) - 2)
    return result
