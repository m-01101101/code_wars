# The array is either entirely comprised of odd integers 
# or entirely comprised of even integers 
# except for a single integer N
# find N

def find_outlier(integers):
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if i % 2 != 0]

    if len(even) == 1:
        result = int(even[0])
    else:
        result = int(odd[0])
        
    return result

"""
should have used:
return odds[0] if len(odds)<len(evens) else evens[0]
"""    