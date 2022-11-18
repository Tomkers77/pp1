def zakres(x,y,n):
    if n <=y and n >= x:
        return True
    else:
        return False

x = int(input("Wpisz dolny zakres: "))
y = int(input("Wpisz gorny zakres: "))
if x < y:
    z = int(input("Wpisz jakas liczbe: "))
    print(zakres(x,y,z))
else:
    print("Dolny zakres musi byc mniejszy od gornego")