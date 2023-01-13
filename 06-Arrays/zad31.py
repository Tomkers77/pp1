array = [24,26,7,543,2,2,5,6,7,8,3,23,4]
even = []
odd = []
for i in array:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Parzyste: {even}, nieparzyste: {odd}")