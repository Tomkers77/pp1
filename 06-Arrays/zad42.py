array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for j in array:
    print(j)

for i in range(len(array)):
    x = array[i][0]
    y = array[i][-1]
    array[i][0] = y
    array[i][-1] = x

print()

for j in array:
    print(j)