def count_frames(f):
    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
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

#
# fib = count_frames(fib)
# print(fib(24))
# print(fib.max_count)


############################################################################################################
# memoization decorator

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)

    counted.call_count = 0
    return counted

def memoization(f):
    cache = {}
    def inner(n):
        nonlocal cache
        if n in cache:
            return cache[n]
        else:
            cache[n]=f(n)
            return cache[n]
    return inner

# fibb = memoization(fib)
# print(fibb(10))
#
# fib = count_frames(fib)
# fibbb = memoization(fib)
# print(fibbb(24))
# print("**{}**".format(fib.max_count))

counted_fib = count(fib)
fib  = memoization(counted_fib)
## 要是需要将装饰后的函数进行递归，必须将装饰（）后的函数重新赋值给原来函数名，其实装饰器已经做到这一点
print(fib(19))
print(counted_fib.call_count)
