# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-18 22:30:50
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-21 14:13:39

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


def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    elif numbers == None:
        return sum_numbers(list(range(1, 101)))
    else:
        if len(numbers) == 1:
            return numbers[0]
        else:
            return numbers[0] + sum_numbers(numbers[1:])


su = sum_numbers([])
print(su)


def sum_num(numbers=None):
    return sum(numbers) if numbers else sum(range(1,101))
print(sum_num([1,2]))





