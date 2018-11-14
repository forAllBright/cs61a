def summation(N,f):
    k,sum = 1, 0
    while k <= N:
        sum, k = sum+f(k),k+1
    return sum
def square(x):
    return x*x
    
print(summation(5, square))
print(summation(5, lambda x: 2*x))