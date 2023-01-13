def f(human_age):
    wynik = 0
    for i in range(human_age):
        if i == 0 or i ==1:
            wynik += 10
        else:
            wynik += 4
    return wynik

#print(f(15))
#print(f(2))