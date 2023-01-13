def f(array1,array2):
    c = 0
    for i in array1:
        if array2.count(i) == 0:
            c = 1
    if c == 1:
        return "Nie jest podzbiorem"
    else:
        return "Jest podzbiorem"
            

print(f([2,3,2,5,8,1,9,8],[2,3,2,9,8,1,5,8]))
print(f([2,3,2,5,8,1,9,8],[25,76,3,2,24]))
print(f([2,3,2,5,8,1,9,8],[8,9,1,5,2,3,5,11,43]))