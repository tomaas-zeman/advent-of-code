from itertools import groupby
import math
from common.utils import as_ints


def run(data: list[str], is_test: bool):
    jolts = sorted(as_ints(data))
    diffs = list(map(lambda x, y: x - y, jolts + [jolts[-1] + 3], [0] + jolts))
    return math.prod(
        (2 ** (len(match) - 1)) - (1 if len(match) == 4 else 0)
        for key, group in groupby(diffs)
        if key == 1 and len((match := list(group))) > 1
    )
