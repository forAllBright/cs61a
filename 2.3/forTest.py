# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-18 22:30:50
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-18 22:38:46

from ucb import trace


@trace
def test(n):
    if n <= 1:
        print(n)
    else:
        test(n - 1)


test(10)


# def make_withdraw(bala):
#     def withdraw(num):
#         lo = bala - num
#         return lo

#     return withdraw


# demo = make_withdraw(100)
# print(demo(90))


def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        lo = balance - amount
        return lo
    return withdraw

wd = make_withdraw(20)
print(wd(5))
