array = [-15,8,-31,47,-2,19]
c=0
ma = 0
mi = 0
for i in array:
    if i == 0:
        mi = array[0]
        ma = array[0]
    else:
        if array[c] > ma:
            ma = array[c] 
        if array[c] < mi:
            mi = array[c]
        c+=1
print(ma)
print(mi)