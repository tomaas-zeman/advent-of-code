from typing import List, Tuple


def parse_input(data: List[str]) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    for instruction in data:
        direction = -1 if instruction[0] == "L" else 1
        clicks = int(instruction[1:])
        result.append((direction, clicks))
    return result
