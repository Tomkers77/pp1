def sum(n):
    suma = 0
    if n > 0:
        suma = n + sum(n-1)
        return suma
    if n == 0:
        return suma
x = 10       
print (sum(x))