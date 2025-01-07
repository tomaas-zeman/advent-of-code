def has_straight(pwd):
    for i in range(len(pwd) - 2):
        if ord(pwd[i]) + 2 == ord(pwd[i + 1]) + 1 == ord(pwd[i + 2]):
            return True
    return False


def has_valid_chars(pwd):
    invalid_chars = "iol"
    for c in invalid_chars:
        if c in pwd:
            return False
    return True


def has_two_pairs(pwd):
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i + 1]:
            for j in range(i + 2, len(pwd) - 1):
                if pwd[j] == pwd[j + 1]:
                    return True
    return False


def next(pwd):
    ord_a = 97
    ord_z = 122
    ords = list(map(lambda c: ord(c), pwd))
    i = -1
    while abs(i) < len(pwd):
        if ords[i] < ord_z:
            ords[i] += 1
            return "".join(map(lambda o: chr(o), ords))
        else:
            ords[i] = ord_a
            i -= 1


def next_valid_pwd(pwd):
    checks = [has_straight, has_two_pairs, has_valid_chars]
    while True:
        if all(map(lambda check: check(pwd), checks)):
            return pwd
        pwd = next(pwd)
