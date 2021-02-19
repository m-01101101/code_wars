# subtract list b from list a


def array_diff(a, b):
    new_list = []
    for i in a:
        if i not in b:
            new_list.append(i)
    return new_list


def array_diff_alt(a, b):
    return [x for x in a if x not in set(b)]


# useful to know
# if it had been removing from both lists
# use sets
# this remove duplicates from both and allows you to subtract
list(set(a) - set(b))
