def compare(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int and type(b) == list:
        return compare([a], b)
    if type(a) == list and type(b) == int:
        return compare(a, [b])

    for i in range(min(len(a), len(b))):
        item_comparison = compare(a[i], b[i])
        if item_comparison != 0:
            return item_comparison

    return len(a) - len(b)
