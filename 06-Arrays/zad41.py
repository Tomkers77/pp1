array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for i in array:
    print(i)

x = array[0]
y = array[-1]

array[0] = y
array[-1] =x

print()

for j in array:
    print(j)    