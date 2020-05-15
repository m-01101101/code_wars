"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:
1 2 3
2 4 6
3 6 9
"""

def multiplication_table(size):
    meta_list = []
    list1 = []
    
    for i in range(size):
        list1.append(i + 1)

    meta_list.append(list1)

    for i in range(size-1):
        newlist = [x * (i+2) for x in list1]
        meta_list.append(newlist)

    return meta_list

"""
alternative approach

def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
"""    