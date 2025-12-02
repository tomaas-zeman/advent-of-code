dec_multiplier = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
snafu_mod = [("0", 0), ("1", 0), ("2", 0), ("=", 1), ("-", 1)]  #  tuple (result, carry)


def snafu_to_dec(snafu: str):
    return sum([dec_multiplier[snafu[::-1][i]] * (5**i) for i in range(len(snafu))])


def dec_to_snafu(dec: int):
    res = ""
    while dec > 0:
        mod = dec % 5
        res += snafu_mod[mod][0]
        dec //= 5
        dec += snafu_mod[mod][1]
    return res[::-1]


def run(data: list[str], is_test: bool):
    return dec_to_snafu(sum([snafu_to_dec(line) for line in data]))


test_result = '2=-1=0'
