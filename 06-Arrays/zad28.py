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
    if len(array)%2 ==0:
        return (array[int(len(array)/2)-1] + array[int(len(array)/2)])/2
    else:
        return array[int(len(array)/2)]

print(bubblesort([1,0,9,4,6]))
print(bubblesort([6,8,3,1,5,7]))