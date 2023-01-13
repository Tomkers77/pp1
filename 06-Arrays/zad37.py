array = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7],[8,7,1,1,5]]
wynik = 0
for tablica in array:
    for x in range(len(tablica)):
        if x == len(tablica)-1:
            wynik += tablica[x]
print (wynik)