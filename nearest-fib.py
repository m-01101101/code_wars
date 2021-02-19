"""
Given a positive integer (n) find the nearest fibonacci number to (n).

If there are more than one fibonacci with equal distance to the given number return the smallest one.

Do it in a efficient way. 5000 tests with the input range 1 <= n <= 2^512 should not exceed 200 ms.
"""
# TODO
import math

golden_ratio = 1.61803398875


def fib_n(n: int) -> float:
    return int((pow(golden_ratio, n) - pow((1 - golden_ratio), n))) / math.sqrt(n - 1)
