from __future__ import annotations

from year2022.day19.common import get_geodes_opened


def run(data: list[str], is_test: bool):
    geodes_opened = get_geodes_opened(data, 24)
    return sum([id * res for id, res in geodes_opened.items()])
