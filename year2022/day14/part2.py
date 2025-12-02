from year2022.day14.common import Type, parse_input, pick_free


def run(data: list[str], is_test: bool):
    matrix, sand_source = parse_input(data)

    # mark floor
    for column in range(matrix.num_cols):
        matrix.point_at(matrix.num_rows - 1, column).value = Type.ROCK

    steps = 0
    while True:
        free_point = pick_free(matrix, sand_source)
        free_point.value = Type.SAND
        steps += 1

        if free_point == sand_source:
            break

        # uncomment for animation
        # if steps % 100 == 0:
        #     time.sleep(0.1)
        #     os.system('clear')
        #     print(matrix)

    return steps


test_result = 93
