f = input("Wpisz nazwe pliku: ")

c=0

with open(f,'r') as file:
     for line in file:
          c +=1
print (f"Ilosc linii w pliku: {c}")
file.close()
