def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k = term(k) + total, k+1
    return total
    
def square(x):
    return x*x

def pi_summantion(n):
    return summation(n, lambda x: 8 / ((4*x-3) * (4*x-1)))

def suqare_summantio(n):
    return summation(n, square)

print(pi_summantion(1e6))
print(suqare_summantio(4))
