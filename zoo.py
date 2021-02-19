"""
You're working in a number zoo,
it seems that one of the numbers has gone missing!

Write a function that takes a shuffled list of unique numbers 
from 1 to n with one element missing (which can be any number including n). 
Return this missing number.

Examples:
[1, 3, 4]  =>  2
[1, 2, 3]  =>  4
[4, 2, 3]  =>  1

Note, elements will be unique
"""

# attempt 1, works but too inefficient for large list


def find_missing_number(y):
    # sort list
    y = sorted(y)
    # check if first element 1
    if y[0] != 1:
        missing = 1
    else:
        # by default, set missing to be element not in the list
        missing = len(y) + 1
        holding = 1
        for i in y:
            if i > holding:
                # if element is greater than what is expect (holding)
                # then assign missing and break if and for loop using return
                missing = i - 1
                return missing
            holding += 1
    return missing


# same thing
def find_missing_num(b):
    b = sorted(b)
    missing = len(b) + 1
    for i in b:
        if b.index(i) + 1 != i:
            missing = b.index(i) + 1
            return missing
    return missing


# solution, without using loops
def find_missing(b):
    b = set(b)
    r = set(range(1, len(b) + 1))
    if r == b:
        missing = len(b) + 1
        return missing
    else:
        missing = b - r
        return list(missing)[0]


"""
Alternative, clever solution

def find_missing_number(a):
    n = len(a) + 1
    return n * (n + 1) // 2 - sum(a)
"""
