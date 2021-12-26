from collections import deque

from day10.common import get_data

opening = '([{<'
closing = ')]}>'
points = {')': 1, ']': 2, '}': 3, '>': 4}


def run():
    lines = get_data()
    total_points = []

    for line in lines:
        stack = deque()

        invalid_line = False
        for char in line:
            if char in opening:
                stack.append(char)
            elif stack.pop() != opening[closing.index(char)]:
                invalid_line = True
                break

        if invalid_line:
            continue

        line_points = 0
        for char in list(stack)[::-1]:
            line_points *= 5
            line_points += points[closing[opening.index(char)]]

        total_points.append(line_points)

    return sorted(total_points)[(len(total_points) - 1) // 2]
