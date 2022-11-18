wiek_l = int(input("wpisz wiek psa w ludzkich latach: "))
wiek_p = 0
for i in range(wiek_l):
    if i<2:
        wiek_p = wiek_p + 10.5
    else:
        wiek_p = wiek_p + 4
print(f"Wiek psa w psich latach: {wiek_p}")
