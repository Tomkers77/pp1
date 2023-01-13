def f(dictionary, x, y):
    wynik = 0
    for k in dictionary:
        for n in dictionary[k]:
            if x<= n <=y:
                wynik+=n
    return wynik

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))