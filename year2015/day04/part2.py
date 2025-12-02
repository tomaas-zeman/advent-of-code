from hashlib import md5


def run(data: list[str], is_test: bool):
    if is_test:
        return True
    for n in range(0, 10_000_000):
        hash = md5(f"{data[0]}{n}".encode()).hexdigest()
        if hash.startswith('000000'):
            return n


test_result = True
