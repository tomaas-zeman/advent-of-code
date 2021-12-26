from collections import deque

from year2021.day10.common import get_data

opening = '([{<'
closing = ')]}>'
points = {')': 3, ']': 57, '}': 1197, '>': 25137}


def run():
    lines = get_data()
    total_points = 0

    for line in lines:
        stack = deque()

        for char in line:
            if char in opening:
                stack.append(char)
            elif stack.pop() != opening[closing.index(char)]:
                total_points += points[char]

    return total_points
