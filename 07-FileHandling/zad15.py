with open("sample3.txt",'r') as file:
    w = 1
    c = 0
    for line in file:
        if c != 5 or c == 0:
            print(f"{w}: {line}")
            c+=1
            w+=1
        else:
            p = input("Nacisnij enter aby wyswietlic kolejne 5 wierszy")
            c= 0
file.close()
