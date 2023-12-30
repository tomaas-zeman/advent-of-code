from __future__ import annotations

from typing import Callable


def has_increasing_digits(password: str):
    for i in range(1, len(password)):
        if int(password[i - 1]) > int(password[i]):
            return False

    return True


def count_valid_passwords(additional_conditions: list[Callable[[str], bool]]):
    valid_passwords = 0
    for number in range(108457, 562041):
        if has_increasing_digits(str(number)) and all([cond(str(number)) for cond in additional_conditions]):
            valid_passwords += 1
    return valid_passwords
