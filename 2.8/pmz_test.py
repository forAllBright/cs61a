# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-27 21:55:45
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-27 21:56:56
###########################################
# 在装饰器内部嵌套函数中调用外层传入函数 是装饰前原函数还是装饰后函数 问题
###########################################

def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)  # 调用位置1
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 注意左边的变量是 fi，这种情况下在“调用位置1”处的 f 是原来的 fib
# fi = count_frames(fib)
# print(fi(24))  # 75025
# print(fi.max_count)  # 1
#
# # 左边的变量是 fib，这种情况下，在 counted的词法作用域中，fib 是装饰后的函数，因此在“调用位置1”的 f 是装饰后的 fib
# fib = count_frames(fib)
# print(fib(24))  # 75025
# print(fib.max_count)  # 24

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0
    return counted


fi = count(fib)
print(fi(19)) #6765
print(fi.call_count) #1

fib = count(fib)
print(fib(19)) #6765
print(fib.call_count) #13529