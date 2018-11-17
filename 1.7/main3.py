#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from ucb import trace
from functools import wraps
def trace1(fn):
    @wraps(fn)
    def inner(x):
        print("calling",fn,"argument",x)
        return fn(x)
    return inner


@trace1
def square(x):
    return x*x
@trace
def sum_square_up_to(n):
    k=1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

