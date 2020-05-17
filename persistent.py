"""
Write a function, persistence, 
that takes in a positive parameter num and returns its multiplicative persistence, 
the number of times you must multiply the digits until you reach a single digit.

For example:
```
 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 ```
"""

def persistence(num):
    # turn num into a list
    num = [int(x) for x in list(str(num))]
    result = 1
    count = 0
    # if len 1, return 0, else
    while len(num) > 1:
        for _ in num:
            # multiply each element
            # could use 
                #  reduce((lambda x, y: x * y), num) 
            # not entirely sure how it keeps track
            result = result * _
        # add one to the count
        count += 1
        # resign the result into the list
        num = [int(x) for x in list(str(result))]
        # reset result to 1 for our for loop
        result = 1
    return count

"""
Alternative solution

Tried to something similar at first
Assume the 1 is the initial multiplication

from operator import mul
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(mul,[int(x) for x in str(n)],1)
        i+=1
    return i

"""    