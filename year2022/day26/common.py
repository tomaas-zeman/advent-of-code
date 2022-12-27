import re


def decode(message: str, pattern: str):
    allowed_chars = re.compile(pattern)
    return "".join(
        [
            message[i]
            for i in range(len(message) - 1)
            if message[i] == message[i + 1] and allowed_chars.match(message[i])
        ]
    )
