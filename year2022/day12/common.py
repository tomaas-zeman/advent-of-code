from common.matrix import Point


def value_of(char: str):
    if char == "S":
        return ord("a")
    if char == "E":
        return ord("z")
    return ord(char)


def expansion(p: Point):
    return [n for n in p.neighbors() if value_of(n.value) - value_of(p.value) <= 1 and not n.flag]