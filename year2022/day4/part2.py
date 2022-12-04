from typing import List
from common.lists import as_ints
import re


def run(data: List[str]):
    result = 0
    for [x1, y1, x2, y2] in [as_ints(re.split("[,-]", line)) for line in data]:
        if (x1 <= y2 and y1 >= x2) or (x2 <= y1 and y2 >= x1):
            result += 1
    return result
