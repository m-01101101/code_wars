def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
    return v + 1


def josephus_survivor(n, k):
    return reduce(lambda x, y: (x + k) % y, xrange(0, n + 1)) + 1


def josephus_survivor(n, k):

    increment = k - 1
    tracker = 0
    result = []
    index = []

    iter = range(1, n + 1)

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
    return result[-1]
