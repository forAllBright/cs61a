# -*- coding: utf-8 -*-
# @Author: pmz
# @Date:   2018-11-23 12:00:32
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-27 18:26:58

from hw04 import *

move_stack(9, 1, 3)


def make_anonymous_factorial():
  def func1(factorial_function):
    def func2(k):
      return factorial_function(factorial_function, k)
    return func2

  def factorial(recursive_func, k):
    if k == 1:
      return k
    else:
      return k * recursive_func(recursive_func, k-1)

  return func1(factorial)

print(make_anonymous_factorial()(4))




