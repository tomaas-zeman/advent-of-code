from functools import cache
import math

@cache
def find_divisors(n):
    divisors = set()
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors
