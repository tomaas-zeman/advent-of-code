def letter_value(ascii: int):
    ascii_upper = 65
    ascii_lower = 97
    if ascii >= ascii_lower:
        return ascii - ascii_lower + 1
    return ascii - ascii_upper + 27
