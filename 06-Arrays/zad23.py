def bubblesort(array):
    for j in range(len(array)):
        for i in range(len(array)):
            if i != 0:
                if array[i] < array[i-1]:
                    temp = array[i]
                    array[i] = array[i-1]
                    array[i-1] = temp
        i=0
        j +=1
    return array

print(bubblesort([23,67,2,135,773,3,55]))
print(bubblesort([263,673,25,13576,7753,33,552]))
print(bubblesort([23543,647,244,1355,2773,3,455]))