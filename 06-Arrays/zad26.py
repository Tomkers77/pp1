array = [5,1,9,6,1]
x = 0
y = 0
for i in array:
    x = max(array)
    if i > y and i<x:
        y = i
print(y)