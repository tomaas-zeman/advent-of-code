def run(data: list[str], is_test: bool):
    count = 0
    for i in range(len(data[0])):
        c = data[0][i]
        count += 1 if c == "(" else -1
        if count < 0:
            return i + 1 

