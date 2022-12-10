array = [15,8,31,47,2,19]
print("Normalnie: ")
for i in array:
    print(i,end=" ")
print()

print("Odwrotnie: ")
c = 0
for i in range(len(array)):
    print(array[len(array)-1-c],end=" ")
    c+=1