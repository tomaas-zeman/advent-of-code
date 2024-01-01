from __future__ import annotations

from math import prod

from year2022.day19.common import get_geodes_opened


def run(data: list[str], is_test: bool):
    geodes_opened = get_geodes_opened(data[: 2 if is_test else 3], 32)
    return prod(*geodes_opened.values())
