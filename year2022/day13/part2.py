import json
from functools import cmp_to_key
from typing import Any

from year2022.day13.common import compare


def run(data: list[str], is_test: bool):
    input: list[Any] = [json.loads(line) for line in data + ["[2]", "[6]"] if len(line) > 0]
    input.sort(key=cmp_to_key(compare))
    return (input.index([2]) + 1) * (input.index([6]) + 1)


test_result = 140
