def count_partitions(n,m):
    if(m==1):
        return 1
    elif (n<0):
        return 0
    elif (n==0):
        return 1
    else:
        return count_partitions(n,m-1) + count_partitions(n-m,m)

num = count_partitions(20,20)
print(num)
