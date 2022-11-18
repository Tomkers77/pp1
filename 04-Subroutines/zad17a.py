def liczenie(n,m):
    suma = 0
    for i in n:
        if i == m:
            suma +=1
    return suma
n = "You never get a second chance to make a first impression"
m = "e"
print(liczenie(n,m))