import os


class Color:
    BLACK = "0;30"
    RED = "0;31"
    GREEN = "0;32"
    YELLOW = "0;33"
    BLUE = "0;34"
    PURPLE = "0;35"
    CYAN = "0;36"
    LIGHT_GRAY = "0;37"
    DARK_GRAY = "1;30"
    BOLD_RED = "1;31"
    BOLD_CYAN = "1;32"
    BOLD_YELLOW = "1;33"
    BOLD_BLUE = "1;34"
    BOLD_PURPLE = "1;35"
    BOLD_CYAN = "1;36"
    WHITE = "1;37"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def with_color(text: str, color: Color):
    return f"\x1B[{color}m{text}\x1B[0m"
