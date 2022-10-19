a = input("\nWpisz dlugosc boku a: ")
b = input("Wpisz dlugosc boku b: ")
c = input("Wpisz dlugosc boku c: ")

from cmath import sqrt
"""
a = 3
b = 4
c = 5
"""
p = 0.5*(int(a)+int(b)+int(c))
area = sqrt(p*(p-int(a))*(p-int(b))*(p-int(c)))
print("\npole wynosi: ",area,"\n")