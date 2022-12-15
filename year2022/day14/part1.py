from year2022.day14.common import Type, parse_input, pick_free


def run(data: list[str], raw_data: list[str], is_test: bool):
    matrix, sand_source = parse_input(data)

    steps = 0
    while True:
        free_point = pick_free(matrix, sand_source)
        free_point.value = Type.SAND

        if free_point.row == matrix.num_rows - 1:
            break
        steps += 1

    return steps
