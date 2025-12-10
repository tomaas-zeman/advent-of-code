from dataclasses import dataclass
import re
from aocutils import as_ints


@dataclass
class Input:
    lights: str
    buttons: list[list[int]]
    levels: list[int]


def parse_input(data: list[str]) -> list[Input]:
    lights_pattern = re.compile(r"\[([.#]+)\]")
    buttons_pattern = re.compile(r"\((\d+(?:,\d+)*)\)")
    levels_pattern = re.compile(r"\{([\d,]+)\}")

    inputs = []

    for line in data:
        lights = re.search(lights_pattern, line)[1]
        buttons = [as_ints(b.split(",")) for b in re.findall(buttons_pattern, line)]
        levels = as_ints(re.search(levels_pattern, line)[1].split(","))
        inputs.append(Input(lights, buttons, levels))

    return inputs
