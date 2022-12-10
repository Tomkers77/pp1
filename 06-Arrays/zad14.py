array = [[True,False],[True,False],[True,False]]
c = 0
d = 0
for i in array:
    for j in i:
        if j == True:
            array[d][c] = False
            c += 1
        else:
            array[d][c] = True
            c += 1
    c = 0
    d += 1
print (array)