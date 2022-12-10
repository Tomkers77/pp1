tab = [-15,8,-31,47,-2,19]
max = tab[0]
min = tab[0]
for i in range(1,len(tab)):
    if tab[i] > max:
        max = tab[i]
    if tab[i] < min:
        min = tab[i]
print(max)
print(min)
