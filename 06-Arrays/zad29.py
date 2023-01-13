array = [2,3,2,5,8,1,9,8]
elem = []
num = int(input("Wpisz liczbe: "))
for i in array:
    if i > num:
        elem.append(i)
if len(elem) != 0:
    print (f"Liczby z tablicy wieksze od wprowadzonej: {elem}")
else:
    print("W tablicy nie ma wiekszych liczb")