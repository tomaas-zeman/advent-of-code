from aocutils import ComplexMatrix


def run(data: list[str], is_test: bool):
    space = ComplexMatrix(data, should_store_value=lambda v: v in "S^")
    beams = set([space.position_of("S")])
    splits = set()

    while len(beams) > 0:
        next_position = beams.pop() + 1j

        if next_position.imag > len(data):
            continue

        if space[next_position] == "^":
            new_beams = [next_position - 1, next_position + 1]
            beams.update(new_beams)
            splits.add(next_position)
        else:
            beams.add(next_position)

    return len(splits)


test_result = 21
