array = [[-38, 19], [5,40],[-7,11],[29,16]]
m = 0
for i in array:
    for x in i:
        if x > m:
            m = x

a = 0
for i in array:
    b = 0
    for x in i:
        if x == m:
            print(f"Najwieksza liczba: {m}, Lokalizacja: [{a},{b}]")
        else:
            b+=1
    a+=1
           