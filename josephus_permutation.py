# works but too inefficient
def josephus(n, k):
    if not type(n) == list:
        raise TypeError

    increment = k - 1
    tracker = 0
    result = []
    index = []
    # len inefficient for string lists
    # lazy, trying to speed up
    try:
        if type(n[0]) == int or type(n[0] == bool):
            len_n = len(n)
        elif type(n[0]) == str:
            len_n = 0
            for i in set(n):
                len_n += 1
    except IndexError:
        len_n = 0

    while len(result) < len_n:
        for a, b in enumerate(n):
            if b in result:
                pass
            elif tracker < increment:
                tracker += 1
            elif b not in result:
                result.append(b)
                index.append(a)
                tracker = 0
    return result, index

# elegant solution


def josephus(xs, k):
    i = 0
    ys = []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys

"""
this looks like a perfect use case for reduce
"""
