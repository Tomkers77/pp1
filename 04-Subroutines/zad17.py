n = str(input("Wpisz zdanie: "))
m = str(input("Wpisz litere: "))
def liczenie(n,m):
    suma = 0
    for i in n:
        if i == m:
            suma +=1
    return suma
print(liczenie(n,m))
