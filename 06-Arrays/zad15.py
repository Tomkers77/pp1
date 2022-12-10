array = [[0,0,0],[0,0,0],[0,0,0]]

c = 0
d = 0

for i in array:
    for j in i:
        if d == c:
            array[d][c] = 1
        else:
            continue
        c += 1
    d += 1

for i in array:
    for x in i:
        print(x, end=" ")
    print()
