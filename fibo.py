# -*- coding: UTF-8 -*-
def fib(n):
    """print a Fibonacci series"""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
