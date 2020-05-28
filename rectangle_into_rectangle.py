"""
A "True Rectangle" is a rectangle with two different dimensions and four equal angles.

We want to decompose a given true rectangle into the minimum number of squares.
Then aggregate these generated squares together to form all the possible true rectangles.

You should take each square with its all adjacent squares or rectangles 
to form the resulting true rectangles list.
"""
from functools import reduce
from typing import List, DefaultDict
from itertools import combinations
from collections import defaultdict
data_dict = defaultdict(list)


def rectIntoRects(x: int, y: int) -> list:
    if x == y or x == 0 or y == 0:
        return None
    else:
        squares = []
        sq_area = 0
        total_area = x * y
        x2 = x
        while sq_area < total_area:

            squares.extend([y] * (x2 // y))
            squares.append(x2 % y)

            sq_area = reduce(lambda x, y: x + y, [i*i for i in squares])

            x2, y = (x2 % y), y - (x2 % y)
    
    squares.remove(0)

    for i in range(len(squares)):
        print([sum(squares[i:s]) for s in range(i+1, len(squares)+1)])





    # for i in range(len(squares)):  # take one height at a time
    # for i in range(len(squares)):
    #     data_dict[squares[i]].append([sum(squares[i:s:1])
    #                         for s in range(0, len(squares)+1)])
    
    # meta = []
    # sq_squares = [i*i for i in squares if i != 0]
    # for s in sq_squares:
    #     for i in range(len(sq_squares)):
    #         meta.append(sum(sq_squares[:i]))
    
    # squares.remove(0)
    # for s in squares[:]:  # s represents height
    #     for i in range(len(squares)): # something for length



