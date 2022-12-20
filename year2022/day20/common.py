import numpy as np


def encode(index: int, number: int | str):
    return f"{index}:{number}"


def decode(item: str):
    return [int(x) for x in item.split(":")]


def find_zero_index(array: np.ndarray):
    for i in range(array.shape[0]):
        for j in range(array.shape[0]):
            if encode(j, 0) == array[i]:
                return i
    raise ValueError("You fucked it up. There is no ZERO")


def compute_coordinates(data: list[str], decryption_key: int, repeats: int):
    init_order = [encode(i, int(n) * decryption_key) for i, n in enumerate(data)]
    order = np.array(init_order)

    for _ in range(repeats):
        for item in init_order:
            decoded_index, n = decode(item)
            if n == 0:
                continue

            item_index = np.where(order == item)[0]
            order = np.delete(order, item_index)
            order = np.roll(order, -n % (len(data) - 1))
            order = np.insert(order, item_index, encode(decoded_index, n))
            order = np.roll(order, n % (len(data) - 1))

    zero_index = find_zero_index(order)
    return sum([decode(order[x % len(data)])[1] for x in [n + zero_index for n in [1000, 2000, 3000]]])
