import math

from year2023.day20.common import parse, Pulse, push_button, PART2_END_MODULE


def run(data: list[str], is_test: bool):
    if is_test:
        return "None"

    modules = parse(data)

    # From the input data
    # [qz, cq, jx, tt] --> all qn high --low--> rx
    #
    # In general: synchronized 'high' periods of qn inputs
    button_push_count = 0
    result = {}
    while True:
        button_push_count += 1
        _, end_module_sync_pulses = push_button(modules)

        for input, pulse in end_module_sync_pulses.items():
            if input not in result and pulse == Pulse.HIGH:
                result[input] = button_push_count

        if len(result) == len(modules[PART2_END_MODULE].pulses):
            break

    return math.lcm(*result.values())
