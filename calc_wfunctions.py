def zero(*op):
    if len(op) == 0:
        return 0
    else:
        y = 0
        # using * unpacks a tuple, so need to return first element
        return op[0](y)

def one(*op):
    if len(op) == 0:
        return 1
    else:
        y = 1
        return op[0](y)

def two(*op):
    if len(op) == 0:
        return 2
    else:
        y = 2
        return op[0](y)

def three(*op):
    if len(op) == 0:
        return 3
    else:
        y = 3
        return op[0](y)

def four(*op):
    if len(op) == 0:
        return 4
    else:
        y = 4
        return op[0](y)
   
def five(*op):
    if len(op) == 0:
        return 5
    else:
        y = 5
        return op[0](y)

def six(*op):
    if len(op) == 0:
        return 6
    else:
        y = 6
        return op[0](y)

def seven(*op):
    if len(op) == 0:
        return 7
    else:
        y = 7
        return op[0](y)

def eight(*op):
    if len(op) == 0:
        return 8
    else:
        y = 8
        return op[0](y) 

def nine(*op):
    if len(op) == 0:
        return 9
    else:
        y = 9
        return op[0](y) 
"""
create operators by returning a function
def g(y):
    def f(x):
        return x + y
    return f # returns a higher order function

equivalent to;
def g(y):
    return lambda x: x + y

g(y)(x) = x + y
g = lambda y: (lambda x: x + y)
"""    

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y
    
def times(y):
    return lambda x: x * y
    
def divided_by(y):
    return lambda x: x // y


"""
Much cleaner solution

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
"""

"""
Martijn

import operator


def _gennumbers():
    numbers = "zero one two three four five six seven eight nine".split()
    for i, name in enumerate(numbers):
        def num(op=lambda v: v, _v=i):
            return op(_v)
        globals()[name] = num


def _genoperators():
    ops = {
        'plus': operator.add,
        'minus': operator.sub,
        'times': operator.mul,
        'divided_by': operator.floordiv,
    }
    for name, op in ops.items():
        def oper(b, _op=op):
            return lambda a: _op(a, b)
        globals()[name] = oper


_gennumbers()
_genoperators()
"""
