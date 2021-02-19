def create_phone_number(n):
    num = ""
    for i in "".join(str(n)):
        if i.isdigit():
            num += i
    return "(" + num[0:3] + ") " + num[3:6] + "-" + num[6:]


# super clean
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# map iterates of the list and turns eachs to a string
# it applies any function, but here we say, make string
# doesn't get caught with [ or , because it's iterating over a list
def create_phone_number(n):
    n = "".join(map(str, n))
    return "(%s) %s-%s" % (n[:3], n[3:6], n[6:])


"""
map() function returns a map object
(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax :
map(fun, iter)
"""
