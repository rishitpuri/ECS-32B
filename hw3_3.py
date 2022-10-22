def ladder(n):
    if( n == 0 ):
        return 1
    elif (n < 0):
        return 0
    else:
        return ladder(n - 2) + ladder(n - 1)


n = 10
print(ladder(n))
