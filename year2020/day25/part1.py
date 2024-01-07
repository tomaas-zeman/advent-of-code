from aocutils import as_ints


def run(data: list[str], is_test: bool):
    card_key, door_key = as_ints(data)

    subject_number = 1
    loop_size = 1
    while True:
        subject_number *= 7
        subject_number %= 20201227

        if card_key == subject_number:
            break

        loop_size += 1

    encryption_key = 1
    for i in range(loop_size):
        encryption_key *= door_key
        encryption_key %= 20201227

    return encryption_key
