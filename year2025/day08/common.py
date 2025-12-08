from __future__ import annotations
from collections import defaultdict
from math import prod, sqrt
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
    return sorted(
        [Pair(box1, box2) for box1, box2 in combinations(boxes, 2)],
        key=lambda p: p.distance,
    )


def compute(data: list[str], limit: int) -> tuple[int, list[Pair]]:
    boxes = parse_input(data)
    pairs = all_pairs(boxes)

    for pair in pairs[:limit]:
        if pair.box1.circuit != pair.box2.circuit:
            pair.box1.circuit.merge_with(pair.box2.circuit)

    circuits_sizes = defaultdict[Circuit, int](lambda: 0)
    for box in boxes:
        circuits_sizes[box.circuit] += 1

    return prod(sorted(circuits_sizes.values(), reverse=True)[:3]), pairs
