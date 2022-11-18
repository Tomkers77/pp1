n0=0
n1=1
suma=0
for i in range(0,50):
    if i ==0:
        print(n0,end=" ")
    elif i ==1:
        print(n1,end=" ")
    else:
        suma = n0 + n1
        print (suma,end=" ")
        n0=n1
        n1=suma