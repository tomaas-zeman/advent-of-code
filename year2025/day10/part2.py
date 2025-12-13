import string
from z3 import Int, Optimize
from year2025.day10.common import parse_input


def run(data: list[str], is_test: bool):
    inputs = parse_input(data)

    total_presses = 0

    for input in inputs:
        buttons = [
            Int(f"button_{c}") for c in string.ascii_letters[: len(input.buttons)]
        ]

        optimize = Optimize()

        # only positive button presses
        for button in buttons:
            optimize.add(button >= 0)

        # effects of each button press
        for i in range(len(input.levels)):
            expression = 0
            for j in range(len(input.buttons)):
                if i in input.buttons[j]:
                    expression += buttons[j]
            optimize.add(expression == input.levels[i])

        # run the solver
        optimize.minimize(sum(buttons))
        optimize.check()

        model = optimize.model()

        for button in buttons:
            total_presses += int(str(model[button]))

    return total_presses


test_result = 33
