"""
bootstrapping a solution to help visualise the answer
"""
import pandas as pd
import random

columns = ['n', 'k', 'survivor', 'index', 'n % k', 'n % k-1']
index = list(range(1, 100))

df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0)  # with 0s rather than NaNs

[random.randint for i ]


def josephus_survivor(n, k):

    increment = k - 1
    tracker = 0
    result = []
    index = []

    it = range(1, n+1)

    while len(result) < n:
        for a, b in enumerate(it):
            if b in result:
                pass
            elif tracker < increment:
                tracker += 1
            elif b not in result:
                result.append(b)
                index.append(a)
                tracker = 0
    return result[-1]


def josephus_survivor_position(n, k):

    increment = k - 1
    tracker = 0
    result = []
    index = []

    iter = range(1, n+1)

    while len(result) < n:
        for a, b in enumerate(iter):
            if b in result:
                pass
            elif tracker < increment:
                tracker += 1
            elif b not in result:
                result.append(b)
                index.append(a)
                tracker = 0
    return index[-1]
