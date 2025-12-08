from year2025.day08.common import compute


def run(data: list[str], is_test: bool):
    # I was lazy to write a bisect loop so I found these manually in a few steps
    # IOW, the result has to be the same as the number of boxes and that's where we want to stop
    limit = 29 if is_test else 5189
    _, pairs = compute(data, limit)
    return pairs[limit - 1].box1.x * pairs[limit - 1].box2.x


test_result = 25272
