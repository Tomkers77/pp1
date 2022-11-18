def liczenie(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma
n = 7182
print(liczenie(n))