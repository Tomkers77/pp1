array = [15,8,31,47,2,19]
sum = 0
i = 0

print(array)
while i < len(array):
    sum += array[i]
    i+=1

sred = sum/len(array)
print("Srednia: ",sred)