"""
Find the sum of all numbers with the same digits including duplicates.
However, due to the fact that this is a performance edition kata, num can go up to 10**10000.
That's a number with 10001 digits(at most).
All numbers tested for will be positive.
"""

import math
from itertools import permutations
from functools import reduce
import random
import time


def sum_arrangements(n: int) -> int:
    # permutations creates n! tuples
    # in each tuple the digits of n are represented as a string
    # (123) -> ('1', '2', '3')
    _list = permutations(str(n))

    # ''.join converts a tuple into a string
    # ('1', '2', '3') -> ('123'), then convert to int
    # ≡ sum([int(''.join(x)) for x in _list]), (time.time() - start)
    return reduce(lambda x, y: x + y, map(lambda x: int(''.join(x)), _list))


def sum_arrangements_(n: int) -> int:
    # len(n)! possibilities
    n = str(n)
    len_n = len(n)
    p = math.factorial(len_n)
    unique_positions = p // len_n
    arranged_sum = 0

    # the sum of digits in each index will be the same
    # sum one index, multiple by unique_positions
    # d = sum([int(x) for x in n]) * unique_positions
    d = reduce(lambda x, y: int(x)+int(y), n) * unique_positions

    # need to apply power of tens
    # for i in reversed(range(len_n)):
    #     arranged_sum += (10 ** i) * d
    arranged_sum = reduce(
        lambda x, y: x + y,
        map(lambda i: (10 ** i) * d, reversed(range(len_n)))
        )

    return arranged_sum

# sum_arrangements(123) returns 1332 # 123 + 132 + 213 + 231 + 312 + 321 = 1332
assert sum_arrangements(123) == 1332
assert sum_arrangements_(123) == 1332
assert sum_arrangements(1185) == 99990
assert sum_arrangements_(1185) == 99990

# random.seed(23)
# t = 10**10
# test = random.randint(t, t*2)

# start = time.time()
# a = sum_arrangements(test)
# end = time.time()
# print(f'answer; {a}, sum_arrangements took {round(end - start, 3)}')

# start2 = time.time()
# b = sum_arrangements_(test)
# end2 = time.time()
# print(f'answer; {b}, sum_arrangements_ took {round(end2 - start2, 3)}')
