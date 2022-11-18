def power(x,n):
    if n > 1:
        return x * power(x,n-1)
    if n == 1:
        return x

print(power(5,3))