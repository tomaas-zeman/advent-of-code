from typing import List

from common.lists import as_ints


def run(data: List[str], raw_data: List[str]):
    jolts = as_ints(data)
    diffs = {diff: 0 for diff in range(1, 4)}

    prev_jolt = 0
    for jolt in sorted(jolts + [max(jolts) + 3]):
        diffs[jolt - prev_jolt] += 1
        prev_jolt = jolt

    return diffs[1] * diffs[3]
