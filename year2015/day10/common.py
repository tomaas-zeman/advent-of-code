def expand(data: list[str], rounds: int):
    digits = data[0]
    for _ in range(rounds):
        next_digits = ""
        buffer = digits[0]
        for j in range(1, len(digits)):
            if buffer[-1] == digits[j]:
                buffer += digits[j]
            else:
                next_digits += f"{len(buffer)}{int(buffer[-1])}"
                buffer = digits[j]
        next_digits += f"{len(buffer)}{int(buffer[-1])}"
        digits = next_digits

    return len(digits)
