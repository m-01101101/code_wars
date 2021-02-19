"""
Write a function that returns a (custom) FizzBuzz sequence of the numbers 1 to 100.

The function should be able to take up to 4 arguments:

The 1st and 2nd arguments are strings, "Fizz" and "Buzz" by default;
The 3rd and 4th arguments are integers, 3 and 5 by default.
Thus, when the function is called without arguments,
it will return the classic FizzBuzz sequence up to 100:

When the function is called with (up to 4) arguments,
it should return a custom FizzBuzz sequence, for example:

('Hey', 'There')      -->  [ 1, 2, "Hey", 4, "There", "Hey", ... ]
('Foo', 'Bar', 2, 3)  -->  [ 1, "Foo", "Bar", "Foo", 5, "FooBar", 7, ... ]
"""


def fizzbuzz(f="Fizz", b="Buzz", i=3, j=5) -> list:

    # could replace if n % i == 0 with not
    return [
        (f + b)
        if n % i == 0 and n % j == 0
        else f
        if n % i == 0
        else b
        if n % j == 0
        else n
        for n in range(1, 101)
    ]
