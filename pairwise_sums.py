"""getting lists pairs"""

q = [1, 2, 3, 4, 5]

# get all pairs
[(a, b) for i, a in enumerate(q) for j, b in enumerate(q)]

"""
[(1, 1),
 (1, 2),
 (1, 3),
 (1, 4),
 (1, 5),
 (2, 1),
 (2, 2),
 (2, 3),
 (2, 4),
 (2, 5),
 (3, 1),
 (3, 2),
 (3, 3),
 (3, 4),
 (3, 5),
 (4, 1),
 (4, 2),
 (4, 3),
 (4, 4),
 (4, 5),
 (5, 1),
 (5, 2),
 (5, 3),
 (5, 4),
 (5, 5)]
"""

# remove repitition by only looking at forward indicies
[(a, b) for i, a in enumerate(q) for j, b in enumerate(q) if i < j]

# output
"""
[(1, 2),
 (1, 3),
 (1, 4),
 (1, 5),
 (2, 3),
 (2, 4),
 (2, 5),
 (3, 4),
 (3, 5),
 (4, 5)]
"""

# get all pairwise sums, using a set
{a + b for i, a in enumerate(q) for j, b in enumerate(q) if i < j}

# {3, 4, 5, 6, 7, 8, 9}

# i < j ensures
# a appears before b in the list,
# avoids reptition,
# ensures we don't add the same number to itself
