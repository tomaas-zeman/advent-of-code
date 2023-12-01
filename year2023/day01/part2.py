import re

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def to_int(number):
    if number in words:
        return words[number]
    return number

def run(data: list[str], is_test: bool):
    sum = 0
    for line in data:
        numbers = re.findall(f"(?=(\\d|{'|'.join(words.keys())}))", line)
        sum += int(f"{to_int(numbers[0])}{to_int(numbers[-1])}")
    return sum
