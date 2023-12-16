from itertools import groupby
import numpy as np
from common.utils import Numpy


def can_fix_smudge(left_slice: np.ndarray, right_slice: np.ndarray) -> bool:
    return np.count_nonzero(left_slice != right_slice) == 1


def find_mirror_index(data: list[str], is_horizontal, with_smudge_fix=False) -> int | None:
    map = Numpy.from_input_as_str(data)
    size = map.shape[0] if is_horizontal else map.shape[1]

    for index in range(size - 1):
        smudge_fixed = True if not with_smudge_fix else False

        for offset in range(size // 2 + 1):
            before = index - offset
            after = index + offset + 1
            if before < 0 or after >= size:
                if smudge_fixed:
                    return index + 1
                break

            before_slice = map[[before], :] if is_horizontal else map[:, [before]]
            after_slice = map[[after], :] if is_horizontal else map[:, [after]]
            if not np.array_equal(before_slice, after_slice):
                if with_smudge_fix and can_fix_smudge(before_slice, after_slice):
                    smudge_fixed = True
                else:
                    break

    return None


def get_result(data: list[str], with_smudge_fix=False) -> int:
    result = 0

    for key, map_interator in groupby(data, key=lambda x: x != ""):
        map = list(map_interator)
        if not key:
            continue

        if mirror := find_mirror_index(map, is_horizontal=True, with_smudge_fix=with_smudge_fix):
            result += mirror * 100
        elif mirror := find_mirror_index(map, is_horizontal=False, with_smudge_fix=with_smudge_fix):
            result += mirror

    return result
