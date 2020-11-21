#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply(*args):
    """Return the product of all the arguments. ::

        >>> multiply(0, 1, 2, 3)
        0
        >>> multiply(1, 2, 3)
        6
    """
    result = args[0]
    for arg in args[1:]:
        result *= arg
    return result

print(multiply(0, 1, 2, 3))
print(multiply(1, 2, 3))

# -----------------------------------------------------------------
import random
from functools import reduce

numbers = [random.randint(0, 100) for _ in range(10)]
print(numbers)
print(f"Max is: {reduce(lambda x, y: x if x > y else y, numbers)}")

# -----------------------------------------------------------------

from typing import Iterable


def num2text(number: int) -> Iterable[str]:
    """Convert an integer into a generator of strings

    Example
    -------
    >>> list(num2text(567435))
    ['five', 'six', 'seven', 'four', 'three', 'five']

    """
    nums = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    num2str = {str(i): name for i, name in enumerate(nums)}
    for num in str(number):
        yield num2str[num]


list(num2text(567435))

# -----------------------------------------------------------------
import time


def timeit(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        stop = time.time()
        print("`{func}` required: {time}s".format(func=func.__name__, time=stop - start))
        return result
    return wrapper


# -----------------------------------------------------------------
import time


def bettertimeit(nice=False, msg="`{func}` required: {time}"):
    def decorator(func):

        def beautiful(x):
            symbols = ('s', 'ms', 'µs', 'ns')
            step = 1e3
            if nice:
                for i, symbol in enumerate(symbols):
                    value = x * step ** i
                    if value // 1:
                        break
            else:
                value = x
                symbol = symbols[0]
            return "%5.2f%s" % (value, symbol)

        def wrapper(*args, **kargs):
            start = time.time()
            result = func(*args, **kargs)
            stop = time.time()
            print(msg.format(func=func.__name__, time=beautiful(stop - start)))
            return result

        return wrapper

    return decorator
