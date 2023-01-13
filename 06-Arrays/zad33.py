import random
array = [random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999)]

ramka = "-"*33
print(ramka)

for i in array:
    print(f"|{i:>3}", end="")
    
print("|")
print(ramka)