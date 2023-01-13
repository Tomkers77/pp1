array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a =1
for i in array:
    b =1
    for x in i:
        i[b-1] = a * b
        b += 1 
    a += 1
for j in array:
    for k in j:
        print(k, end=" ")
    print()
    