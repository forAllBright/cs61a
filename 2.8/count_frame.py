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


fib = count_frames(fib)
print(fib(24))
print(fib.max_count)