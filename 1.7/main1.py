def digital_sum(num):
    if(0<num<10):
        return num
    else:
        return (num%10) + int(digital_sum(num/10))

res = digital_sum(12345)
print(res)

def cascade(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)
cascade(100000)
