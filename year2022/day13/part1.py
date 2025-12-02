import json

from year2022.day13.common import compare


def run(data: list[str], is_test: bool):
    sum = 0
    for [a, b], i in [(data[i : i + 2], i) for i in range(0, len(data), 3)]:
        result = compare(json.loads(a), json.loads(b))
        if result < 0:
            sum += i // 3 + 1
    return sum


test_result = 13
