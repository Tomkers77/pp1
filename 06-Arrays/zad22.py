def f(array1,array2):
    wynik=[]
    for i in array1:
        c = 0
        for j in array2:
            if i == j:
                c = 1
        if c == 0:
            wynik.append(i)
    return wynik
        
print(f([4,36,12,28,9,44,5],[5,1,36]))

