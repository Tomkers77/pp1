array = [5,4,3,2,6,5]
wynik=""
for i in range(len(array)):
    if i != len(array)-1:
        wynik += (str(array[i])+", ")
    else:
        wynik += (str(array[i]))
print (wynik)