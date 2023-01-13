def f(array2D):
    wynik=[]

    for i in range(len(array2D[0])):
        sum = 0
        for j in range(len(array2D)):
            sum += array2D[j][i]
        wynik.append(sum)
    return wynik   

print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]))    

