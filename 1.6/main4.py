def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

def map_to_range(start,end,f):
    while start < end:
        print(f(start))
        start = start + 1

map_to_range(0,10,curried_pow(2))
##

def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

