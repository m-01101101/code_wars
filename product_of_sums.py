from typing import List


def find_product(inputs: List[int]) -> int:
    """
    Find two elements that add up to 2020 and return their product
    """
    needs = {2020 - i for i in inputs}

    for i in inputs:
        if i in needs:
            return i * (2020 - i)


# naive approach, compare every pair in the array, 
# results in n^2 comparisons

# this approach says, for each element, 
    # what is the delta i would need to get to the target
    # if that delta is in the list, i don't need to compare 
    # i can just take the product of the element in inputs and element i know is in needs


def find_product3(inputs: List[int]) -> int:
    """
    Find three elements that add up to 2020 and return their product
    """
    needs = {2020 - i - j: (i, j)
                for i in inputs
                for j in inputs
                if i != j}

    for i in inputs:
        if i in needs:
            j, k = needs[i]
            return i * j * k

# needs now becomes a dictionary that we look up
