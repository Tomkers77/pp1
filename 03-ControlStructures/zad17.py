x = int(input("Wpisz wspolrzedna x: "))
y = int(input("Wpisz wspolrzedna y: "))
if x>0 and y>0:
    print(f"Punkt ({x},{y}) nalezy do pierwszej cwiartki")
elif x<0 and y>0:
     print(f"Punkt ({x},{y}) nalezy do drugiej cwiartki")
elif x<0 and y<0:
     print(f"Punkt ({x},{y}) nalezy do trzeciej cwiartki")
elif x>0 and y<0:
     print(f"Punkt ({x},{y}) nalezy do czwartej cwiartki")
else:
     print(f"Punkt ({x},{y}) to srodek ukladu")