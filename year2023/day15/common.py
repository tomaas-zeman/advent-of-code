def hash(text: str):
    code = 0
    for char in text:
        code += ord(char)
        code *= 17
        code %= 256
    return code