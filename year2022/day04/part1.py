import re

from aocutils import as_ints


def run(data: list[str], is_test: bool):
    result = 0
    for [x1, y1, x2, y2] in [as_ints(re.split("[,-]", line)) for line in data]:
        if (x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1):
            result += 1
    return result
