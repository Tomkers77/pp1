array = [2,3,2,5,8,1,9,8]
elem = []
for i in array:
    if array.count(i)==1:
        elem.append(i)

print(f"Tablica: {array}")
print(f"Elementy: {elem}")