from year2022.day10.common import instructions
from common.console import clear, with_color, Color

width = 40
height = 6


def is_light_pixel(position: int, sprite_mid_position: int):
    return sprite_mid_position - 1 <= position % width <= sprite_mid_position + 1


def draw_crt(crt: list[str]):
    for line in [crt[i : i + width] for i in range(0, len(crt), width)]:
        print("".join(line))


def run(data: list[str], raw_data: list[str]):
    value = 1
    step = 0
    crt = ["." for _ in range(width * height)]

    for line in [line.split(" ") for line in data]:
        instruction = instructions[line[0]]

        for _ in range(instruction.duration):
            if is_light_pixel(step, value):
                crt[step] = with_color('#', Color.CYAN)
            step += 1

        value = instruction.operation(value, line[1:])
    
    draw_crt(crt)
    return True
