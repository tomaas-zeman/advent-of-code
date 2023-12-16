import re
from year2023.day15.common import hash


def index_of(key: int, label: str, boxes: dict[int, list[str]]) -> int | None:
    for i, box in enumerate(boxes[key]):
        if label in box:
            return i
    return None


def compute_focusing_power(boxes: dict[int, list[str]]) -> int:
    power = 0
    for box_number, box in boxes.items():
        for lens_slot, lens in enumerate(box):
            focal_length = int(lens.split(" ")[1])
            power += (box_number + 1) * (lens_slot + 1) * focal_length
    return power


def run(data: list[str], is_test: bool):
    boxes = {i: [] for i in range(256)}

    for instruction in re.finditer(r"(\w+)([-=]){1}(\d*),?", data[0]):
        label, op = instruction.group(1), instruction.group(2)
        key = hash(label)
        index = index_of(key, label, boxes)

        if op == "-" and index is not None:
            boxes[key].pop(index)
        if op == "=":
            value = f"{label} {instruction.group(3)}"
            if index is not None:
                boxes[key][index] = value
            else:
                boxes[key].append(value)

    return compute_focusing_power(boxes)
