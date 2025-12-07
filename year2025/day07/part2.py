from aocutils import ComplexMatrix


def run(data: list[str], is_test: bool):
    space = ComplexMatrix(data, should_store_value=lambda v: v in "S^")
    start = space.position_of("S")

    # position -> number of unique timelines reachable from that position
    cache: dict[complex, int] = {}

    def explore_space(beam: complex, explored_positions: set[complex]) -> int:
        if beam in cache:
            return cache[beam]

        if beam in explored_positions:
            return 0

        explored_positions.add(beam)
        next_position = beam + 1j

        if next_position.imag > len(data):
            return 1

        new_beams = (
            [next_position - 1, next_position + 1]
            if space[next_position] == "^"
            else [next_position]
        )

        number_of_timelines = sum(
            [explore_space(new_beam, explored_positions) for new_beam in new_beams]
        )

        cache[beam] = number_of_timelines
        return number_of_timelines

    return explore_space(start, set())


test_result = 40
