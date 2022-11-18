n = int(input("Wpisz liczbe: "))
i = 2
for i in range(n):
    if i!=1 and i!=n:
        if n%i==0:
            break
        else:
            print(n,end=" ")