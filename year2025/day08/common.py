from __future__ import annotations
from collections import defaultdict
from math import prod, sqrt
import heapq
from itertools import combinations
import uuid

from aocutils import as_ints


class Box:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = Circuit(self)


class Pair:
    def __init__(self, box1: Box, box2: Box):
        self.box1 = box1
        self.box2 = box2
        # store squared distance to avoid expensive sqrt calls; ordering is preserved
        self.distance = sqrt(
            (box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2
        )


class Circuit:
    def __init__(self, initial_box: Box):
        self.id = uuid.uuid4()
        self.boxes = set([initial_box])

    def merge_with(self, circuit: Circuit):
        self.boxes.update(circuit.boxes)
        for box in circuit.boxes:
            box.circuit = self


def parse_input(data: list[str]) -> list[Box]:
    return [Box(*as_ints(line.split(","))) for line in data]


def all_pairs(boxes: list[Box]) -> list[Pair]:
    # Legacy: rarely used; prefer calling compute() with a limit so we don't
    # need to build all pairs. Keep function for completeness.
    return sorted(
        [Pair(box1, box2) for box1, box2 in combinations(boxes, 2)],
        key=lambda p: p.distance,
    )


_compute_cache: dict[tuple[str, ...], dict] = {}


def compute(data: list[str], limit: int) -> tuple[int, list[Pair]]:
    """Compute product of top-3 circuit sizes after merging `limit` closest pairs.

    This implementation avoids constructing all O(n^2) Pair objects when
    `limit` is much smaller than the total number of pairs. It uses
    `heapq.nsmallest` to select the `limit` smallest squared distances and
    memoizes results per input dataset to speed up repeated calls (e.g. during
    binary searches).
    """
    key = tuple(data)
    boxes = parse_input(data)
    n = len(boxes)

    # If we already computed pairs for this dataset and up to this limit,
    # reuse them.
    cache_entry = _compute_cache.get(key)
    if cache_entry is not None and cache_entry.get("limit", 0) >= limit:
        pairs = cache_entry["pairs"]
    else:
        # We will generate the `limit` smallest edges by squared distance.
        # Use indices to avoid creating Pair objects for all combinations.
        def gen_edges():
            for i in range(n):
                bx = boxes[i]
                xi, yi, zi = bx.x, bx.y, bx.z
                for j in range(i + 1, n):
                    b2 = boxes[j]
                    d2 = (xi - b2.x) ** 2 + (yi - b2.y) ** 2 + (zi - b2.z) ** 2
                    yield (d2, i, j)

        # If limit is large (close to total pairs) it's cheaper to build all
        # pairs and sort; otherwise use nsmallest which is more memory friendly.
        total_pairs = n * (n - 1) // 2
        k = min(limit, total_pairs)

        if k == total_pairs:
            # build all pairs
            raw = list(gen_edges())
            raw.sort(key=lambda t: t[0])
            selected = raw
        else:
            # nsmallest returns results in arbitrary order; sort them after
            selected = heapq.nsmallest(k, gen_edges(), key=lambda t: t[0])
            selected.sort(key=lambda t: t[0])

        pairs = [Pair(boxes[i], boxes[j]) for (_d2, i, j) in selected]
        # store in cache for future calls; we keep 'limit' so callers asking for
        # <= this limit can reuse cached prefix
        _compute_cache[key] = {"pairs": pairs, "limit": k}

    # apply merges for the requested prefix
    # reset circuits (they hold mutable state), so reconstruct boxes' circuits
    for box in boxes:
        box.circuit = Circuit(box)

    for pair in pairs[:limit]:
        if pair.box1.circuit != pair.box2.circuit:
            pair.box1.circuit.merge_with(pair.box2.circuit)

    circuits_sizes = defaultdict(int)
    for box in boxes:
        circuits_sizes[box.circuit] += 1

    return prod(sorted(circuits_sizes.values(), reverse=True)[:3]), pairs
