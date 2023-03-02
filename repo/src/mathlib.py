"""
@file mathlib.py
@brief Math functions for calculator
"""

import math
def add(x, y):
    """
    @param x x
    @param y y

    @return x + y
    """
    return x + y

def sub(x, y):
    """
    @param x x
    @param y y

    @return x - y
    """
    return x - y

def mul(x, y):
    """
    @param x x
    @param y y

    @return x * y
    """
    return x * y

def div(x, y):
    """
    @param x x
    @param y y

    @return x / y
    """
    return x / y

def mod(x, y):
    """
    @param x x
    @param y y

    @return x % y
    """
    return x % y

def fact(n):
    """
    @param x x

    @return x!
    """
    factorial = 1
    if(n < 0):
        raise ValueError("n must not be a negative number")
    if(not isinstance(n, int)):
        raise ValueError("n must be an integer")
    else:
        for i in range(1, n+1):
            factorial = factorial * i
    return factorial

def power(x, n):
    """
    @param x x
    @param n n

    @return x^n
    """
    return x ** n

def sqrt(x):
    """
    @param x x

    @return Square root of x
    """
    if(x < 0):
        raise ValueError("x must not be a negative number")
    return x ** (1/2)

def nrt(x, n):
    """
    @param x x
    @param n n

    @return n-th root of x
    """
    if(x < 0):
        raise ValueError("x must not be a negative number")
    return x ** (1/n)

def sin(x):
    """
    @param x x

    @return sinus of x
    """
    return math.sin(math.radians(x))
