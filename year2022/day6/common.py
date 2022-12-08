def index_of_n_distinct_chars(line: str, n: int):
    for i in range(n, len(line)):
        if len(set(line[i - n : i])) == n:
            return i
