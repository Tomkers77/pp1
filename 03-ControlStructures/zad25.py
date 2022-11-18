a = int(input("Wpisz dlugosc pierwszego boku: "))
b = int(input("Wpisz dlugosc drugiego boku: "))
for i in range(a):
    if i==0 or i==(a-1):
        for j in range(b):
            print("*",end="")
    else:
        for j in range(b):
            if j==0 or j==(b-1):
                print("*",end="")
            else:
                print(end=" ")
    print()