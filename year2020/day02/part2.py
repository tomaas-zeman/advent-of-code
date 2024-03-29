from year2020.day02.common import parse_input_data


def run(data: list[str], is_test: bool):
    passwords = parse_input_data(data)

    correct_passwords = 0
    for [pos1, pos2], letter, password in passwords:
        if (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter):
            correct_passwords += 1

    return correct_passwords
