from hashlib import md5


def run(data: list[str], is_test: bool):
    for n in range(0, 1_000_000):
        hash = md5(f"{data[0]}{n}".encode()).hexdigest()
        if hash.startswith('00000'):
            return n


test_result = 609043
