# my attempt
def move_zeros(array):
    """Place all zeros at the end of the string, preserving the order of other elements.
    False not equivalent to 0"""
    # False regarded as == 0, but None and empty is not, so added or statement
    result = list(filter(lambda x: x != 0 or x is False, array))
    # Originally used count(0) for len but same issue with counting false
    result.extend([0 for i in list(range(0, (len(array) - len(result))))])
    return result


# best practice1
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))


# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# Check if the number 5 is an integer:
# x = isinstance(5, int)


# clever
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


"""
To explain a little: sorted() will sort an iterable of inputs (in this case, array), 
by whatever metric you define. 
If you gave it a list of ints and didn't tell it how to sort, 
it would sort them as you'd expect - smallest first.

However, you can tell sorted() what you want to sort by, with the key argument. 
key must be a function that returns something orderable.

In this case, our function to sort by is a lambda function, 
which is just a shorthand way of writing a function inline.
What does this function do?
It returns True if x==0 and type(x) is not bool. 
So, all your 0s and 0.0s (and complex 0i + 0js? I don't know about those enough) will return True, 
while everything else - any non-zero int, or any str will return False. 
Also, False will return False,
because even though False == 0, type(False) is bool.

Alright, so we've got a bunch of True/False values as our key outputs...
how the heck does the rest of this work?!

Well, now we sort by the keys.
Since False is equivalent to 0 and True is equivalent to 1, we put all of our False before all of our True. 
This means we put all of our (int, or str, or False) before all of our (0 or 0.0 or 0i + 0j).

Ok, fine, but how come it doesn't screw up the order of things?
If I sort (3, 2, 1) by their keys (True, True, True) why do I get (3, 2, 1) back out?
Because Python's sort is a stable sort.
That means, if two items compare equal, the first one in is the first one out. 
So, everything that gets a False stays in order, and everything that was True (aka 0-ish) stays in order;
but all the False come before all the True.

This solution is exceedingly clever... but not AT ALL best practice.
I've glossed over a bunch of details,
and it requires you to know things like Python uses stable sort 
and the only falsey values this function wants to keep "in place" is False... 
it would be really difficult to maintain/understand this code without a solid Python background,
or a ton of comments.
"""
