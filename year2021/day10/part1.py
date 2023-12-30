from collections import deque

opening = "([{<"
closing = ")]}>"
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def run(data: list[str], is_test: bool):
    total_points = 0

    for line in data:
        stack = deque()

        for char in line:
            if char in opening:
                stack.append(char)
            elif stack.pop() != opening[closing.index(char)]:
                total_points += points[char]

    return total_points
